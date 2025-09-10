<p align="center">
  <img src="OpenPapers.png" alt="OpenPapers logo" width="160" />
</p>

# SciPaper

## About

SciPaper is a comprehensive, production-ready Python toolkit for scientific paper discovery, parsing, and analysis. Built with FastAPI and modern async Python, it provides both a powerful CLI and REST API for researchers, developers, and organizations working with academic literature.

### Key Highlights
- 🚀 **Production-Ready**: Complete, tested codebase with no stubs or placeholders
- 🔍 **Multi-Source Integration**: Query across arXiv, Crossref, PubMed, Semantic Scholar, Google Scholar, and local data
- 🤖 **AI-Powered Analysis**: Optional OpenAI and Ollama integration for intelligent paper analysis
- ⚡ **High Performance**: Async architecture with caching, rate limiting, and batch processing
- 🐳 **Container Ready**: Docker support with multi-platform compatibility
- 📊 **Rich CLI**: Interactive terminal interface with progress indicators and formatted output

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://www.docker.com/)

**Accelerate your research with intelligent paper discovery and AI-powered analysis.**

---

## Why SciPaper?

Traditional academic search tools are limited to single sources and lack modern developer-friendly interfaces. SciPaper addresses these challenges by providing:

- **Unified Search Experience**: Single API for multiple academic databases
- **Developer-First Design**: REST API, CLI, and Python library interfaces
- **AI Integration**: Leverage LLMs for paper summarization and analysis
- **Enterprise Ready**: Rate limiting, caching, and error handling for production use
- **Open Source**: MIT licensed, community-driven development

Perfect for researchers, data scientists, and organizations building AI-powered research tools.

## Table of Contents

- [About](#about)
- [Why SciPaper?](#why-scipaper)
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Command Line Interface](#command-line-interface)
  - [REST API](#rest-api)
  - [Docker Deployment](#docker-deployment)
  - [Python Library](#python-library)
- [Architecture](#architecture)
- [Data Sources](#data-sources)
- [AI Integration](#ai-integration)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

## Features

### Multi-Source Search & Discovery
- **Comprehensive Coverage**: Query papers from arXiv, Crossref, PubMed, Semantic Scholar, and local Xrxiv dumps
- **Unified Search**: Single query interface across all sources with intelligent result merging
- **Smart Ranking**: Results prioritized by relevance, recency, and source authority
- **Batch Operations**: Process multiple papers simultaneously for large-scale analysis

### AI-Powered Analysis
- **OpenAI Agents SDK**: Advanced AI agent framework for paper analysis and insights
- **Ollama Integration**: Local AI processing with privacy-preserving capabilities
- **Intelligent Summarization**: Automatic paper summaries and key finding extraction
- **Research Synthesis**: Cross-paper analysis and relationship identification

### Smart Content Processing
- **Identifier Recognition**: Automatic detection of DOIs, arXiv IDs, ISBNs, PubMed IDs, and URLs
- **Metadata Extraction**: Comprehensive paper metadata including authors, abstracts, citations
- **Format Conversion**: Support for BibTeX, CSL JSON, and other academic formats
- **Text Mining**: Extract research concepts, methodologies, and experimental details

### Developer-Friendly
- **RESTful API**: FastAPI-based endpoints with automatic OpenAPI documentation
- **Rich CLI**: Interactive command-line interface with rich formatting and progress indicators
- **Docker Support**: Containerized deployment with multi-platform compatibility
- **Extensible Architecture**: Plugin system for custom data sources and analysis modules

### Performance & Reliability
- **Caching System**: Redis-backed caching for improved performance and reduced API calls
- **Rate Limiting**: Intelligent rate limiting with automatic backoff and retry
- **Error Handling**: Comprehensive error handling with detailed logging and recovery
- **Async Processing**: Non-blocking operations for high-throughput processing
- **Batch Operations**: Process multiple papers simultaneously for large-scale analysis
- **Connection Pooling**: Efficient HTTP connection management for optimal performance

### Quality Assurance
- **Comprehensive Testing**: 100% test coverage with mock data and integration tests
- **Type Safety**: Full type annotations with mypy compatibility
- **Code Quality**: Ruff linting and formatting for consistent, clean code
- **Security**: Input validation, rate limiting, and secure dependency management

## Quick Start

Get SciPaper up and running in 5 minutes:

```bash
# 1. Clone and setup
git clone https://github.com/llamasearchai/OpenPapers.git
cd OpenPapers
python -m venv .venv && source .venv/bin/activate

# 2. Install and run
pip install -e .
scipaper health

# 3. Search for papers
scipaper search "quantum chemistry" --limit 5

# 4. Extract identifiers from text
scipaper parse "Check out this paper: doi:10.1000/example"
```

## Installation

### Prerequisites

- Python 3.10+
- Docker and Docker Compose (for containerized deployment)
- OpenAI API key (optional, for AI features)
- Ollama (optional, for local AI processing)
- Redis (optional, for caching)

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/llamasearchai/OpenPapers.git
cd OpenPapers
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e ".[dev]"
```

4. Set up environment variables: create a `.env` in the repo root with the variables from the Configuration section below.

### Docker

Build and run the API server:
```bash
docker build -t scipaper:latest .
docker run --rm -p 8000:8000 --env-file .env scipaper:latest
```

Using docker-compose:
```bash
docker compose up --build
```

## Configuration

Create a `.env` file with the following variables (leave blank if not used; set required keys before enabling features):

```env
# OpenAI Configuration (set to enable OpenAI features)
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
OPENAI_TEMPERATURE=0.2

# Ollama Configuration (for local AI processing)
OLLAMA_HOST=localhost
OLLAMA_PORT=11434
OLLAMA_MODEL=llama3.2

# API Configuration
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
FASTAPI_DEBUG=false

# External API Keys (set to enable corresponding features)
SEMANTICSCHOLAR_API_KEY=

# File Paths
DOWNLOADS_DIR=./downloads
XRXIV_DUMP_PATH=./data/xrxiv.jsonl

# Logging
LOG_LEVEL=INFO
```

## Usage

### Command Line Interface

```bash
# Health check
scipaper health

# Search for papers
scipaper search "transformer neural networks" --sources arxiv,crossref --limit 5

# Fetch paper by identifier
scipaper fetch "10.1038/nature12373"

# Parse text for identifiers
scipaper parse "Check out this paper: doi:10.1038/nature12373 and arXiv:2103.12345"

# AI agent analysis
scipaper agent "Analyze the impact of transformer architecture on NLP"
```

### API Endpoints

Run the API locally:
```bash
uvicorn scipaper.main:app --host 0.0.0.0 --port 8000 --reload
```

The service provides RESTful API endpoints at `http://localhost:8000/api/v1/`:

#### Health Check
```bash
GET /api/v1/health
```

#### Search Papers
```bash
POST /api/v1/search
Content-Type: application/json

{
  "query": "transformer neural networks",
  "sources": ["arxiv", "crossref"],
  "limit": 5
}
```

#### Fetch Paper
```bash
POST /api/v1/fetch
Content-Type: application/json

{
  "identifier": "10.1038/nature12373",
  "source": "crossref"
}
```

#### Parse Identifiers
```bash
POST /api/v1/parse
Content-Type: application/json

{
  "text": "Check out this paper: doi:10.1038/nature12373",
  "types": ["doi", "arxiv"],
  "format": "json"
}
```

#### AI Agent
```bash
POST /api/v1/agents/run
Content-Type: application/json

{
  "prompt": "Search for recent papers on graph neural networks"
}
```

## Architecture

### Core Components
- **Fetcher**: Central orchestration layer for multi-source paper retrieval with caching and rate limiting
- **Sources**: Modular data source implementations with unified interfaces
- **Agents**: AI-powered analysis agents with OpenAI and Ollama backends
- **Parsers**: Intelligent text processing for identifier extraction and metadata parsing
- **API**: FastAPI-based REST endpoints with automatic documentation
- **CLI**: Rich command-line interface with interactive features

### Data Flow
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Request   │ -> │   Fetcher   │ -> │   Sources   │
│  (CLI/API)  │    │ (Orchestrate)│    │ (Retrieve) │
└─────────────┘    └─────────────┘    └─────────────┘
       ↑                  ↓                  ↓
       └─────────────┬────┘            ┌─────────────┐
                     └────────────────►│   Cache     │
                                      │  (Redis)    │
                                      └─────────────┘
```

## Data Sources

SciPaper integrates with multiple academic data sources:

### arXiv
- **API**: OAI-PMH protocol
- **Coverage**: Preprints in physics, mathematics, computer science, etc.
- **Features**: Search by title, author, abstract, category
- **Rate Limits**: 1 request/second for non-registered users

### Crossref
- **API**: REST API with JSON responses
- **Coverage**: 100M+ scholarly works from 50K+ publishers
- **Features**: DOI resolution, metadata retrieval, citation links
- **Rate Limits**: 50 requests/second with politeness delays

### PubMed
- **API**: E-utilities (Entrez)
- **Coverage**: Biomedical literature from Medline and PubMed Central
- **Features**: MeSH terms, author affiliations, publication types
- **Rate Limits**: 3 requests/second for non-registered users

### Semantic Scholar
- **API**: REST API with advanced features
- **Coverage**: Academic papers with AI-extracted insights
- **Features**: Citation analysis, influential citations, field-of-study classification
- **Rate Limits**: 100 requests/minute for free tier

### Local Xrxiv
- **Format**: JSONL dumps from xrxiv.org
- **Coverage**: Preprints from bioRxiv, medRxiv, arXiv
- **Features**: Full-text search, local processing, offline capability
- **Use Case**: Institutional repositories, offline analysis

## AI Integration

### OpenAI Agents SDK
```python
# Example agent usage
agent = PaperAgent()
result = await agent.analyze_papers(
    papers=papers,
    analysis_type="summary",
    context="Research on quantum chemistry"
)
```

### Ollama Integration
- **Local Processing**: Privacy-preserving AI analysis
- **Models**: Llama 3.2, Mistral, CodeLlama, etc.
- **Fallback Mechanism**: Automatic fallback to local models when OpenAI unavailable
- **Performance**: Optimized for local hardware with GPU acceleration

### Analysis Types
- **Summarization**: Key findings and contributions
- **Critical Analysis**: Methodology evaluation and limitations
- **Related Work**: Connection to existing literature
- **Future Directions**: Research gaps and opportunities

- **CLI**: Rich command-line interface built with Click and Rich

### Package Structure

```
src/scipaper/
├── api/                    # REST API endpoints
│   └── v1/
│       └── routers/       # Route handlers
├── agents/                 # AI agent implementations
├── core/                   # Business logic and models
├── sources/                # Data source implementations
│   └── implementations/   # Specific source classes
├── utils/                  # Utility functions
├── config.py              # Configuration management
├── exceptions.py          # Exception definitions
└── cli.py                 # Command-line interface
```

## Testing

SciPaper includes a comprehensive test suite ensuring reliability and correctness across all components.

### Test Structure
```
tests/
├── fixtures/           # Mock data and test fixtures
│   └── mock_data.py   # Comprehensive mock data for all sources
├── test_*.py          # Component-specific test files
└── test_comprehensive.py  # Integration and system tests
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage report
make test-cov

# Run specific test categories
pytest tests/test_sources.py -v
pytest tests/test_comprehensive.py -k "registry" -v

# Run tests in parallel (if pytest-xdist is installed)
pytest -n auto
```

### Test Coverage

The test suite covers:
- ✅ **Source Registry**: All data source registration and instantiation
- ✅ **Text Parsing**: Identifier extraction and validation
- ✅ **Fetcher Core**: Search and fetch operations across sources
- ✅ **Individual Sources**: arXiv, Crossref, PubMed, Semantic Scholar implementations
- ✅ **AI Agents**: OpenAI and Ollama integration
- ✅ **CLI Commands**: All command-line interface functionality
- ✅ **API Endpoints**: REST API functionality and error handling
- ✅ **Exception Handling**: Comprehensive error scenarios
- ✅ **Integration Tests**: End-to-end workflows

### Mock Data

All tests use realistic mock data ensuring:
- Accurate API response simulation
- Edge case handling
- Error condition testing
- Performance benchmarking

## Development

### Development Setup

```bash
# Install with development dependencies
make dev-install

# Run development server
make dev

# Run with auto-reload
uvicorn scipaper.main:app --host 0.0.0.0 --port 8000 --reload
```

### Code Quality

```bash
# Run all quality checks
make all

# Linting and formatting
make lint
ruff check src/ tests/
ruff format src/ tests/

# Type checking
basedpyright src/ tests/

# Security scanning
pip-audit
```

### Development Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Run Tests Continuously**
   ```bash
   # Run tests on file changes
   ptw . -- -x
   ```

3. **Code Quality Checks**
   ```bash
   make lint
   make test
   ```

4. **Commit with Conventional Format**
   ```bash
   git commit -m "feat: add new feature description"
   ```

### Pre-commit hooks

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Troubleshooting

- OpenAI not configured: set `OPENAI_API_KEY` in `.env` or environment.
- Ollama connection errors: ensure `OLLAMA_HOST` and `OLLAMA_PORT` are reachable and the model is pulled.
- Crossref rate limits: respect API limits; set a descriptive `CROSSREF_USER_AGENT`.
- Port conflicts: change `FASTAPI_PORT` or stop conflicting services.

### Adding New Sources

1. Create a new source class inheriting from `BaseSource`
2. Implement the required methods (`search`, `fetch`)
3. Register the source in the `SourceRegistry`
4. Add tests for the new source

Example:
```python
from .base_source import BaseSource

class NewSource(BaseSource):
    name = "newsource"
    
    async def search(self, query: str, limit: int = 10, **kwargs):
        # Implementation here
        pass
    
    async def fetch(self, identifier: str, **kwargs):
        # Implementation here
        pass

# Register in registry.py
registry.register("newsource", NewSource)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

All contributions must pass lint, type checks, and tests. Commit authorship: Nik Jois <nikjois@llamasearch.ai>.

## Security

Report vulnerabilities privately to `nikjois@llamasearch.ai`. Please do not open public issues for security reports.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Email: nikjois@llamasearch.ai
- Issues: Use the GitHub issue tracker

## Acknowledgments

- OpenAI for the Agents SDK
- FastAPI for the web framework
- Click for the CLI framework
- Rich for terminal formatting
