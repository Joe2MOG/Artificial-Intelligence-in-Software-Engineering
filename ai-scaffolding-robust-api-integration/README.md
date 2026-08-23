# AI: Scaffolding a Robust API Integration

## AI Tool Used
Gemini (Flash, extended thinking)

## Files
- `sentiment_analyzer_initial.py` — the original sentiment analysis
  script, with basic exception handling but no authentication.
- `sentiment_analyzer_refactored.py` — the AI-refactored version,
  which securely reads an API key from the
  `TEXT_PROCESSING_API_KEY` environment variable and sends it via
  an `Authorization: Bearer <key>` header, and adds explicit
  `Timeout` and `ConnectionError` exception handlers ahead of the
  general `RequestException` catch.

## Technique
Contextual Prompting — the full original script was included
directly in the AI prompt as context, alongside an explicit,
specific description of the two required changes (secure API key
handling and two additional exception types), rather than a vague
generic refactoring request.

## Verification
Ran the refactored script with a dummy API key
(`TEXT_PROCESSING_API_KEY=DUMMY_KEY`). The request reached the
real API and was rejected with `403 Forbidden`, correctly caught
by the existing `HTTPError` handler. Independently confirmed via
Python's class hierarchy that `Timeout` and `ConnectionError` both
inherit from `RequestException`, verifying the new exception
handlers are correctly ordered above the general case rather than
being unreachable dead code.
