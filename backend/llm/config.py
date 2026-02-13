from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

try:
    from dotenv import find_dotenv, load_dotenv
    load_dotenv(find_dotenv(), override=False)
except Exception:
    pass


@dataclass(frozen=True)
class LLMConfig:
    provider: str
    model_name: str
    fallback_model_name: str
    api_key: str
    base_url: str
    app_name: str
    app_url: Optional[str]
    temperature: float
    timeout_s: float
    max_tokens: int
    max_retries: int
    backoff_base_s: float

    @staticmethod
    def from_env() -> "LLMConfig":
        provider = os.getenv("LLM_PROVIDER", "openrouter").strip().lower()
        model_name = os.getenv("MODEL_NAME","openai/gpt-oss-120b" )
        fallback_model_name = os.getenv("FALLBACK_MODEL_NAME", "openrouter/aurora-alpha")
        base_url = os.getenv(
            "OPENAI_BASE_URL",
            "https://openrouter.ai/api/v1" if provider == "openrouter" else "https://api.openai.com/v1",
        )
        api_key = (
            os.getenv("OPENROUTER_API_KEY", "")
            if provider == "openrouter"
            else os.getenv("OPENAI_API_KEY", "")
        ).strip()
        return LLMConfig(
            provider=provider,
            model_name=model_name,
            fallback_model_name=fallback_model_name,
            api_key=api_key,
            base_url=base_url,
            app_name=os.getenv("OPENROUTER_APP_NAME", "ARIA Mission Control"),
            app_url=os.getenv("OPENROUTER_APP_URL"),
            temperature=float(os.getenv("LLM_TEMPERATURE", "0.2")),
            timeout_s=float(os.getenv("LLM_TIMEOUT_S", "60")),
            max_tokens=int(os.getenv("LLM_MAX_TOKENS", "512")),
            max_retries=int(os.getenv("LLM_MAX_RETRIES", "5")),
            backoff_base_s=float(os.getenv("LLM_BACKOFF_BASE_S", "0.5")),
        )

