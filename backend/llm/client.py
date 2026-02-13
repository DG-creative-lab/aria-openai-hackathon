from __future__ import annotations

import json
import re
import time
from typing import Dict, List, Literal, Optional

try:
    from openai import (
        APIConnectionError,
        APIStatusError,
        APITimeoutError,
        OpenAIError,
        RateLimitError,
    )
except Exception:
    APIConnectionError = Exception
    APIStatusError = Exception
    APITimeoutError = Exception
    OpenAIError = Exception
    RateLimitError = Exception

from .config import LLMConfig
from .providers.openai_compatible import OpenAICompatibleProvider


class LLMClient:
    def __init__(self, config: LLMConfig):
        self.config = config
        # Current architecture uses OpenAI-compatible provider for both OpenRouter and OpenAI.
        self.provider = OpenAICompatibleProvider(config)

    def _call_with_retries(
        self,
        messages: List[Dict[str, str]],
        model: str,
        response_format: Literal["json_object", "text", ""] | None,
        max_tokens: int,
        temperature: float,
    ) -> str:
        last_err: Exception | None = None
        for attempt in range(1, self.config.max_retries + 1):
            try:
                return self.provider.complete(
                    messages=messages,
                    model=model,
                    temperature=temperature,
                    response_format=response_format,
                    max_tokens=max_tokens,
                    timeout_s=self.config.timeout_s,
                )
            except (RateLimitError, APITimeoutError, APIConnectionError) as e:
                last_err = e
                time.sleep(min(8.0, self.config.backoff_base_s * (2 ** (attempt - 1))))
            except APIStatusError as e:
                last_err = e
                status = getattr(e, "status_code", None) or getattr(e, "status", None)
                if status and int(status) < 500:
                    break
                if attempt < self.config.max_retries:
                    time.sleep(min(8.0, self.config.backoff_base_s * (2 ** (attempt - 1))))
            except OpenAIError as e:
                last_err = e
                break
            except Exception as e:
                last_err = e
                break
        raise RuntimeError(f"LLM call failed after {self.config.max_retries} attempts: {last_err}")

    def call_model(
        self,
        messages: List[Dict[str, str]],
        response_format: Literal["json_object", "text", ""] | None = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        model: Optional[str] = None,
    ) -> str:
        model_name = model or self.config.model_name
        temp = self.config.temperature if temperature is None else float(temperature)
        max_tok = self.config.max_tokens if max_tokens is None else int(max_tokens)

        models = [model_name]
        if self.config.fallback_model_name and self.config.fallback_model_name != model_name:
            models.append(self.config.fallback_model_name)

        last_err: Exception | None = None
        for m in models:
            try:
                return self._call_with_retries(
                    messages=messages,
                    model=m,
                    response_format=response_format,
                    max_tokens=max_tok,
                    temperature=temp,
                )
            except Exception as e:
                last_err = e
                continue
        raise RuntimeError(str(last_err) if last_err else "LLM call failed")

    def call_json(
        self,
        messages: List[Dict[str, str]],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        model: Optional[str] = None,
    ) -> Dict:
        txt = self.call_model(
            messages=messages,
            response_format="json_object",
            max_tokens=max_tokens,
            temperature=temperature,
            model=model,
        )
        try:
            return json.loads(txt)
        except Exception:
            m = re.search(r"\{.*\}", txt, flags=re.S)
            if m:
                return json.loads(m.group(0))
            raise

    def health_check(self) -> Dict:
        try:
            res = self.call_json(
                [
                    {"role": "system", "content": "You are a minimal JSON responder."},
                    {"role": "user", "content": 'Return {"ok":true,"model":"X"} strictly as JSON.'},
                ],
                max_tokens=16,
            )
            return {
                "ok": True,
                "provider": self.config.provider,
                "model": self.config.model_name,
                "fallback_model": self.config.fallback_model_name,
                "reply": res,
            }
        except Exception as e:
            return {
                "ok": False,
                "error": str(e),
                "provider": self.config.provider,
                "model": self.config.model_name,
                "fallback_model": self.config.fallback_model_name,
            }


_DEFAULT_CLIENT: LLMClient | None = None


def get_default_client() -> LLMClient:
    global _DEFAULT_CLIENT
    if _DEFAULT_CLIENT is None:
        _DEFAULT_CLIENT = LLMClient(LLMConfig.from_env())
    return _DEFAULT_CLIENT

