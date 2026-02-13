from __future__ import annotations

from typing import Literal

from ..llm import get_default_client


def call_model(
    messages: list[dict[str, str]],
    response_format: Literal["json_object", "text", ""] | None = None,
    max_tokens: int | None = None,
    temperature: float | None = None,
    model: str | None = None,
) -> str:
    """
    Backward-compatible facade used by planner/chat.
    Delegates to the centralized LLM client layer.
    """
    return get_default_client().call_model(
        messages=messages,
        response_format=response_format,
        max_tokens=max_tokens,
        temperature=temperature,
        model=model,
    )


def call_json(
    messages: list[dict[str, str]],
    max_tokens: int | None = None,
    temperature: float | None = None,
    model: str | None = None,
) -> dict:
    return get_default_client().call_json(
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        model=model,
    )


def health_check() -> dict:
    return get_default_client().health_check()

