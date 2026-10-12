# AI Interface Specification

## 1. Overview
Defines the software contract for the assistant's AI module before integrating actual LLM APIs. Operates deterministically without external network calls.

## 2. Inputs & Outputs

### Input: `AIRequest`
- `query` (str, required): Raw text query from user.
- `context` (dict, optional): Metadata or conversation context. Default: `{}`.
- `max_tokens` (int, optional): Generation length limit. Default: `256`.
- `temperature` (float, optional): Sampling temperature (`0.0` - `1.0`). Default: `0.0`.

### Output: `AIResponse`
- `reply` (str): Generated or fallback response text.
- `source` (str): Origin of answer (`"rules"`, `"fallback"`, or `"llm"`).
- `confidence` (float): Confidence score between `0.0` and `1.0`.
- `metadata` (dict): Diagnostics (e.g., error reason, fallback flags).

## 3. Function Signatures

```python
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(frozen=True)
class AIRequest:
    query: str
    context: Dict[str, Any] = field(default_factory=dict)
    max_tokens: int = 256
    temperature: float = 0.0


@dataclass(frozen=True)
class AIResponse:
    reply: str
    source: str
    confidence: float
    metadata: Dict[str, Any] = field(default_factory=dict)


def query_ai_service(request: AIRequest) -> AIResponse:
    """Entry point for the AI service contract.

    Validates request and delegates to rule matching or fallback.
    No remote LLM API calls are executed yet.
    """
    raise NotImplementedError("Stub interface: LLM calls not implemented.")


def fallback_handler(query: str, reason: str) -> AIResponse:
    """Returns a deterministic safe response on service unavailability or missed intent."""
    return AIResponse(
        reply="I cannot answer this query right now. Please check official office notices.",
        source="fallback",
        confidence=0.0,
        metadata={"fallback_triggered": True, "reason": reason},
    )
```

## 4. Errors
- `InvalidQueryError`: Query is empty or whitespace-only. Fails fast without triggering fallback.
- `ContextPayloadError`: Malformed or oversized context payload.
- `ServiceUnavailableError`: Triggered on missing API keys, rule misses, or offline mode; caught internally to run fallback.

## 5. Fallback Strategy
- **Trigger**: Missing credentials, rule miss, or unhandled exceptions.
- **Behavior**: Never bubble unhandled exceptions to users.
- **Result**: Returns `AIResponse` with `source="fallback"`, `confidence=0.0`, and a canned message.