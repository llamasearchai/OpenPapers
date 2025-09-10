# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Repository overview
- SciPaper is a Python (3.9+) project that provides both a CLI and a FastAPI REST API for discovery, parsing, and analysis of scientific papers. It also includes optional AI agent functionality (OpenAI or Ollama) for analysis.
- Packaging/entrypoint: setuptools via pyproject.toml; console_script entrypoint "scipaper" points to scipaper.cli:main. Source code lives under src/.
- Primary modules:
  - scipaper/main.py: creates FastAPI app and mounts v1 routers (system, search, fetch, parse, advanced_search, recommendations, agents).
  - scipaper/core: Fetcher orchestrates multi-source queries with retry, basic rate limiting, and optional Redis cache; AdvancedSearchEngine adds query expansion, filtering, and ranking; PaperRecommendationEngine provides content/collaborative/citation/hybrid recs.
  - scipaper/sources: BaseSource ABC; registry registers built-in sources; implementations for arXiv, Crossref, PubMed, Semantic Scholar, Xrxiv local JSONL, Google Scholar, IEEE Xplore.
  - scipaper/api/v1/routers: request/response models and endpoints that call core services.
  - scipaper/agents: PaperAgent chooses OpenAI or Ollama; agents/server exposes POST /api/v1/agents/run.
  - scipaper/utils: identifier extraction and parse helpers; simple export utilities.
  - scipaper/config.py: pydantic-settings backed configuration, loading from .env.

Common commands
- Environment setup
  - python -m venv .venv
  - source .venv/bin/activate
  - pip install -e ".[dev]"
  - Create a .env at repo root with relevant settings (see Configuration section below).
  - Note: The code imports some packages not listed in pyproject dependencies (fastapi-pagination, slowapi, aioredis, psutil, fpdf). If you use API pagination, rate limiting, Redis caching, system monitoring, or PDF export features, install these: pip install fastapi-pagination slowapi aioredis psutil fpdf

- Linting/formatting/type-checking
  - Ruff lint: ruff check src/ tests/
  - Ruff format: ruff format src/ tests/
  - Type check: pyright src/ tests/ (or basedpyright src/ tests/ if the pyright CLI is not available)

- Tests
  - Run all: pytest -q
  - Run a specific file: pytest tests/test_pubmed.py -q
  - Run a subset by name: pytest -k "semanticscholar" -q
  - Optionally with coverage (requires pytest-cov): pytest --cov=src/scipaper

- CLI usage
  - Health: scipaper health
  - Search: scipaper search "transformer neural networks" --sources arxiv,crossref --limit 5
  - Fetch: scipaper fetch "10.1038/nature12373"
  - Parse identifiers: scipaper parse "Check doi:10.1038/nature12373 and arXiv:2103.12345"
  - Agent analysis: scipaper agent "Analyze impact of transformer architecture on NLP" --limit 3

- API server
  - Local run (reload): uvicorn scipaper.main:app --host 0.0.0.0 --port 8000 --reload
  - Docker (build + run):
    - docker build -t scipaper:latest .
    - docker run --rm -p 8000:8000 --env-file .env scipaper:latest
  - Docker Compose (hot reload, mounts source): docker compose up --build
  - Auth: Some endpoints use a simple bearer check. Include: -H "Authorization: Bearer your-api-key-here"

High-level architecture and flow
- Requests (CLI or API) call into the core Fetcher, which:
  - Validates source list against a registry of BaseSource implementations.
  - Applies basic rate limiting (slowapi) per request and retries transient errors with exponential backoff.
  - Optionally checks a Redis cache by key; cache failures degrade gracefully.
  - Aggregates and normalizes results across sources, then sorts/limits.
- Advanced search expands queries and applies server-side filtering and ranking before returning results plus metadata about the search process.
- Recommendations build a user profile (liked/read papers, interests) and combine content, collaborative, and citation signals to generate and enrich recommendations.
- Sources encapsulate provider-specific logic:
  - HTTP APIs (Semantic Scholar, Crossref, PubMed) via httpx AsyncClient with resilient error handling.
  - Synchronous client libraries (arxiv, scholarly, ieeeexplore) are called via asyncio.to_thread.
  - Local JSONL (Xrxiv) scans a dump file for matches.
- Agents layer selects an AI backend:
  - OpenAI via chat.completions (if OPENAI_API_KEY is set) or Ollama via local HTTP API; includes simple validation and iterative refinement.
- Configuration is centralized (pydantic-settings) and read from .env by default.

Configuration (env)
- OpenAI: OPENAI_API_KEY, OPENAI_MODEL (default gpt-4o-mini), OPENAI_TEMPERATURE (default 0.2)
- Ollama: OLLAMA_HOST (default localhost), OLLAMA_PORT (default 11434), OLLAMA_MODEL (default llama3.2)
- API: FASTAPI_HOST (default 0.0.0.0), FASTAPI_PORT (default 8000), FASTAPI_DEBUG (default false)
- External: SEMANTICSCHOLAR_API_KEY (optional), CROSSREF_USER_AGENT (default identifies SciPaper), PUBMED_EMAIL, PUBMED_API_KEY (optional)
- Files: DOWNLOADS_DIR (default ./downloads), XRXIV_DUMP_PATH (default ./data/xrxiv.jsonl)
- Logging: LOG_LEVEL (default INFO)

Project rules for assistants
- Do not use emojis, stubs, or placeholders in code or docs added to this repo. Ensure all contributions are complete.

Important notes
- API pagination: scipaper/api/v1/routers/search.py imports fastapi_pagination (Page, paginate). Install fastapi-pagination before running the API, or remove the pagination dependency from the router if not needed.
- Caching: core/fetcher.py refers to settings.redis_url and aioredis; the env variable and dependency are not declared in pyproject. Caching paths handle failures gracefully, but to enable Redis set a REDIS URL in settings and install aioredis.
- System monitoring in core/monitoring.py imports psutil; install if you plan to use those helpers.
- PDF export in utils/export.py imports fpdf; install if you need PDF export.
- There is a secondary scipaper_cli package mirrored under src/; the primary CLI entrypoint is scipaper (from scipaper/cli.py).

This WARP.md intentionally omits generic development advice and file-by-file listings; it focuses on repository-specific commands and architecture.

