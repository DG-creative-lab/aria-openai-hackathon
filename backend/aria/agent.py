from __future__ import annotations
import os, json, time, typing as t

# pip install groq
from groq import Groq

# --- Load .env automatically ---
try:
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv(), override=False)
except Exception as e:
    print("⚠️ Could not load .env:", e)

# Try to import public exceptions if available; fall back gracefully.
try:
    from groq import (
        GroqError,
        APIConnectionError,
        APITimeoutError,
        RateLimitError,
        APIStatusError,
    )
except Exception:  # SDKs change; keep running even if names move
    GroqError = Exception
    APIConnectionError = Exception
    APITimeoutError = Exception
    RateLimitError = Exception
    APIStatusError = Exception

# ---------- env ----------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME   = os.getenv("MODEL_NAME", "openai/gpt-oss-20b")

LLM_TEMPERATURE   = float(os.getenv("LLM_TEMPERATURE", "0.2"))
LLM_TIMEOUT_S     = float(os.getenv("LLM_TIMEOUT_S", "60"))
LLM_MAX_TOKENS    = int(os.getenv("LLM_MAX_TOKENS", "512"))
LLM_MAX_RETRIES   = int(os.getenv("LLM_MAX_RETRIES", "5"))
LLM_BACKOFF_BASE  = float(os.getenv("LLM_BACKOFF_BASE_S", "0.5"))

# ---------- singleton ----------
_CLIENT: Groq | None = None
def get_client() -> Groq:
    """Cached Groq client instance."""
    global _CLIENT
    if _CLIENT is None:
        if not GROQ_API_KEY:
            raise RuntimeError("GROQ_API_KEY is not set.")
        # Groq() picks up api_key and default base URL; timeout is set per-request below.
        _CLIENT = Groq(api_key=GROQ_API_KEY)
    return _CLIENT

# ---------- core call ----------
def _chat_create(
    messages: list[dict[str, str]],
    model: str = MODEL_NAME,
    temperature: float = LLM_TEMPERATURE,
    response_format: t.Literal["json_object","text",""] | None = None,
    max_tokens: int = LLM_MAX_TOKENS,
) -> str:
    """
    Low-level call with retries; returns assistant message content.
    """
    last_err: Exception | None = None
    for attempt in range(1, LLM_MAX_RETRIES + 1):
        try:
            kwargs: dict[str, t.Any] = dict(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=LLM_TIMEOUT_S,  # per-request timeout
            )
            if response_format:
                kwargs["response_format"] = {"type": response_format}

            r = get_client().chat.completions.create(**kwargs)
            return r.choices[0].message.content or ""
        except (RateLimitError, APITimeoutError, APIConnectionError) as e:
            last_err = e
            time.sleep(min(8.0, LLM_BACKOFF_BASE * (2 ** (attempt - 1))))
        except APIStatusError as e:
            last_err = e
            status = getattr(e, "status_code", None) or getattr(e, "status", None)
            if not status or int(status) < 500 or attempt == LLM_MAX_RETRIES:
                break
            time.sleep(min(8.0, LLM_BACKOFF_BASE * (2 ** (attempt - 1))))
        except GroqError as e:
            last_err = e
            break
        except Exception as e:
            last_err = e
            break
    raise RuntimeError(f"LLM call failed after {LLM_MAX_RETRIES} attempts: {last_err}")

# ---------- public helpers ----------
def call_model(
    messages: list[dict[str, str]],
    response_format: t.Literal["json_object","text",""] | None = None,
    max_tokens: int = LLM_MAX_TOKENS,
    temperature: float = LLM_TEMPERATURE,
    model: str = MODEL_NAME,
) -> str:
    return _chat_create(
        messages=messages,
        model=model,
        temperature=temperature,
        response_format=response_format,
        max_tokens=max_tokens,
    )

def call_json(
    messages: list[dict[str, str]],
    max_tokens: int = LLM_MAX_TOKENS,
    temperature: float = LLM_TEMPERATURE,
    model: str = MODEL_NAME,
) -> dict:
    txt = call_model(messages, response_format="json_object",
                     max_tokens=max_tokens, temperature=temperature, model=model)
    try:
        return json.loads(txt)
    except Exception:
        import re
        m = re.search(r"\{.*\}", txt, flags=re.S)
        if m:
            return json.loads(m.group(0))
        raise

def health_check() -> dict:
    try:
        res = call_json(
            [
                {"role":"system","content":"You are a minimal JSON responder."},
                {"role":"user","content":'Return {"ok":true,"model":"X"} strictly as JSON.'}
            ],
            max_tokens=16,
        )
        return {"ok": True, "provider":"groq", "model": MODEL_NAME, "reply": res}
    except Exception as e:
        return {"ok": False, "error": str(e), "provider":"groq", "model": MODEL_NAME}
