from __future__ import annotations

import json
from typing import Any, Dict, List, Literal

from openai import OpenAI

from ..config import LLMConfig


class OpenAICompatibleProvider:
    """Thin adapter over the OpenAI-compatible chat completions API."""

    def __init__(self, config: LLMConfig):
        self._cfg = config
        if not self._cfg.api_key:
            need = "OPENROUTER_API_KEY" if self._cfg.provider == "openrouter" else "OPENAI_API_KEY"
            raise RuntimeError(f"{need} is not set.")
        self._client = OpenAI(api_key=self._cfg.api_key, base_url=self._cfg.base_url)

    def complete(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float,
        response_format: Literal["json_object", "text", ""] | None,
        max_tokens: int,
        timeout_s: float,
    ) -> str:
        kwargs: Dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "timeout": timeout_s,
        }
        if response_format:
            kwargs["response_format"] = {"type": response_format}

        if self._cfg.provider == "openrouter":
            headers: Dict[str, str] = {"X-Title": self._cfg.app_name}
            if self._cfg.app_url:
                headers["HTTP-Referer"] = self._cfg.app_url
            kwargs["extra_headers"] = headers

        res = self._client.chat.completions.create(**kwargs)
        msg = res.choices[0].message
        content = getattr(msg, "content", None)

        if isinstance(content, str):
            text = content.strip()
            if text:
                return text

        if isinstance(content, list):
            parts: List[str] = []
            for p in content:
                if isinstance(p, dict) and p.get("type") == "text" and p.get("text"):
                    parts.append(str(p["text"]))
            text = "\n".join(parts).strip()
            if text:
                return text

        # Trigger retry/fallback path in client when provider returns empty content.
        meta = {
            "refusal": getattr(msg, "refusal", None),
            "tool_calls": getattr(msg, "tool_calls", None),
        }
        raise RuntimeError(f"empty_model_response:{json.dumps(meta, default=str)}")
