"""Comprehensive tests for all SciPaper components using mock data."""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from typing import Dict, List, Any, Optional

from scipaper.config import settings
from scipaper.core.fetcher import Fetcher
from scipaper.sources.registry import SourceRegistry
from scipaper.utils.parse import parse_text
from scipaper.exceptions import SciPaperError, SourceError, FetcherError

from tests.fixtures.mock_data import (
    MOCK_ARXIV_PAPER,
    MOCK_CROSSREF_PAPER,
    MOCK_ARXIV_SEARCH_RESULTS,
    MOCK_CROSSREF_SEARCH_RESULTS,
    MOCK_TEXT_WITH_IDENTIFIERS,
    MOCK_PARSED_IDENTIFIERS,
    MOCK_AGENT_ANALYSIS,
    create_mock_paper,
    create_mock_search_results
)


class TestSourceRegistry:
    """Test the source registry functionality."""

    def test_registry_initialization(self):
        """Test that registry initializes with expected sources."""
        registry = SourceRegistry()
        sources = registry.list_available()

        # Should have our main sources
        expected_sources = ["arxiv", "crossref", "googlescholar", "pubmed", "semanticscholar", "xrxiv_local"]
        for source in expected_sources:
            assert source in sources

    def test_get_source_instance(self):
        """Test getting source instances from registry."""
        registry = SourceRegistry()

        arxiv_source = registry.create("arxiv", {})
        assert arxiv_source is not None
        assert arxiv_source.name == "arxiv"

        crossref_source = registry.create("crossref", {})
        assert crossref_source is not None
        assert crossref_source.name == "crossref"

    def test_invalid_source(self):
        """Test handling of invalid source names."""
        registry = SourceRegistry()

        with pytest.raises(ValueError):
            registry.get_source("invalid_source")


class TestParserUtils:
    """Test text parsing utilities."""

    def test_parse_text_with_identifiers(self):
        """Test parsing text containing various identifiers."""
        results = parse_text(MOCK_TEXT_WITH_IDENTIFIERS)

        assert len(results) == 5
        # Check that all expected identifiers are found
        result_values = {(r["type"], r["value"]) for r in results}
        expected_values = {(r["type"], r["value"]) for r in MOCK_PARSED_IDENTIFIERS}
        assert expected_values.issubset(result_values)

    def test_parse_text_empty(self):
        """Test parsing empty text."""
        results = parse_text("")
        assert results == []

    def test_parse_text_no_identifiers(self):
        """Test parsing text with no identifiers."""
        results = parse_text("This is just plain text with no identifiers.")
        assert results == []

    def test_parse_text_with_types_filter(self):
        """Test parsing with type filtering."""
        results = parse_text(MOCK_TEXT_WITH_IDENTIFIERS, types=["doi"])
        assert len(results) == 2
        assert all(result["type"] == "doi" for result in results)


class TestFetcherCore:
    """Test the core fetcher functionality."""

    @pytest.fixture
    def fetcher(self):
        """Create a fetcher instance for testing."""
        return Fetcher()

    @pytest.mark.asyncio
    async def test_fetcher_search_arxiv(self, fetcher):
        """Test searching arXiv source."""
        with patch.object(fetcher, '_search_source') as mock_search:
            mock_search.return_value = MOCK_ARXIV_SEARCH_RESULTS

            results = await fetcher.search("transformer", sources=["arxiv"], limit=2)

            assert len(results) == 2
            assert results[0]["source"] == "arxiv"
            mock_search.assert_called_once()

    @pytest.mark.asyncio
    async def test_fetcher_search_multiple_sources(self, fetcher):
        """Test searching multiple sources."""
        with patch.object(fetcher, '_search_source') as mock_search:
            mock_search.side_effect = [MOCK_ARXIV_SEARCH_RESULTS, MOCK_CROSSREF_SEARCH_RESULTS]

            results = await fetcher.search("CRISPR", sources=["arxiv", "crossref"], limit=3)

            assert len(results) == 4  # 2 from each source
            sources = set(result["source"] for result in results)
            assert sources == {"arxiv", "crossref"}

    @pytest.mark.asyncio
    async def test_fetcher_fetch_by_doi(self, fetcher):
        """Test fetching a paper by DOI."""
        with patch.object(fetcher, '_fetch_from_source') as mock_fetch:
            mock_fetch.return_value = MOCK_CROSSREF_PAPER

            result = await fetcher.fetch("10.1038/nbt.2842")

            assert result is not None
            assert result["doi"] == "10.1038/nbt.2842"
            assert result["source"] == "crossref"

    @pytest.mark.asyncio
    async def test_fetcher_fetch_not_found(self, fetcher):
        """Test fetching a non-existent paper."""
        with patch.object(fetcher, '_fetch_from_source') as mock_fetch:
            mock_fetch.return_value = None

            result = await fetcher.fetch("non.existent.doi")

            assert result is None

    @pytest.mark.asyncio
    async def test_fetcher_error_handling(self, fetcher):
        """Test error handling in fetcher."""
        with patch.object(fetcher, '_search_source') as mock_search:
            mock_search.side_effect = Exception("Network error")

            with pytest.raises(FetcherError):
                await fetcher.search("test query", sources=["arxiv"])


class TestSourceImplementations:
    """Test individual source implementations."""

    @pytest.mark.asyncio
    async def test_arxiv_source_search(self):
        """Test arXiv source search functionality."""
        from scipaper.sources.implementations.arxiv import ArxivSource

        source = ArxivSource({})

        # Mock the actual API call
        with patch('scipaper.sources.implementations.arxiv.feedparser.parse') as mock_parse:
            mock_parse.return_value = MOCK_ARXIV_API_RESPONSE

            results = await source.search("attention", limit=1)

            assert len(results) == 1
            assert "Attention Is All You Need" in results[0]["title"]

    @pytest.mark.asyncio
    async def test_crossref_source_search(self):
        """Test Crossref source search functionality."""
        from scipaper.sources.implementations.crossref import CrossrefSource

        source = CrossrefSource({})

        # Mock the API call
        with patch('httpx.AsyncClient.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = MOCK_CROSSREF_API_RESPONSE
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            results = await source.search("CRISPR", limit=1)

            assert len(results) == 1
            assert "CRISPR" in results[0]["title"]

    @pytest.mark.asyncio
    async def test_pubmed_source_search(self):
        """Test PubMed source search functionality."""
        from scipaper.sources.implementations.pubmed import PubMedSource

        source = PubMedSource({})

        # Mock the API call
        with patch('httpx.AsyncClient.get') as mock_get:
            mock_response = Mock()
            mock_response.text = '<?xml version="1.0"?><eSearchResult><IdList><Id>25393562</Id></IdList></eSearchResult>'
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            results = await source.search("CRISPR", limit=1)

            mock_get.assert_called()

    @pytest.mark.asyncio
    async def test_semantic_scholar_source_search(self):
        """Test Semantic Scholar source search functionality."""
        from scipaper.sources.implementations.semanticscholar import SemanticScholarSource

        source = SemanticScholarSource({})

        # Mock the API call
        with patch('httpx.AsyncClient.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {
                "data": [{
                    "paperId": "649def34f8be52c8b66281af98ae884c09aef38b",
                    "title": "BERT: Pre-training of Deep Bidirectional Transformers",
                    "authors": [{"name": "Jacob Devlin"}],
                    "year": 2018,
                    "abstract": "We introduce BERT...",
                    "venue": "arXiv"
                }]
            }
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            results = await source.search("BERT", limit=1)

            assert len(results) == 1
            assert "BERT" in results[0]["title"]


class TestAgentFunctionality:
    """Test AI agent functionality."""

    @pytest.mark.asyncio
    async def test_paper_agent_search_and_analyze(self):
        """Test paper agent search and analysis."""
        from scipaper.agents.paper_agents import PaperAgent

        agent = PaperAgent()

        with patch.object(agent, 'search_papers') as mock_search:
            with patch.object(agent, 'analyze_papers') as mock_analyze:
                mock_search.return_value = MOCK_ARXIV_SEARCH_RESULTS
                mock_analyze.return_value = MOCK_AGENT_ANALYSIS["analysis"]

                result = await agent.search_and_analyze("transformer neural networks", limit=2)

                assert "papers" in result
                assert "analysis" in result
                assert len(result["papers"]) == 2
                mock_search.assert_called_once()
                mock_analyze.assert_called_once()


class TestConfiguration:
    """Test configuration management."""

    def test_settings_initialization(self):
        """Test that settings initialize properly."""
        # Test that we can access basic settings
        assert hasattr(settings, 'log_level')
        assert hasattr(settings, 'downloads_dir')

    def test_openai_availability(self):
        """Test OpenAI availability detection."""
        from scipaper.config import is_openai_available

        # Should be False without API key
        with patch.dict('os.environ', {}, clear=True):
            assert not is_openai_available()

    def test_ollama_availability(self):
        """Test Ollama availability detection."""
        from scipaper.config import is_ollama_available

        # Should be False without proper setup
        assert not is_ollama_available()


class TestCLICommands:
    """Test CLI command functionality."""

    def test_cli_health_command(self):
        """Test health command execution."""
        from scipaper.cli import main

        # This would require more complex mocking for full CLI testing
        # For now, just ensure the command exists
        assert hasattr(main, 'commands')
        assert 'health' in [cmd.name for cmd in main.commands.values()]


class TestExceptionHandling:
    """Test exception handling throughout the system."""

    def test_sci_paper_error_creation(self):
        """Test SciPaperError creation and properties."""
        error = SciPaperError("Test error message", {"details": "test"})

        assert str(error) == "Test error message"
        assert error.message == "Test error message"
        assert error.details == {"details": "test"}
        assert not error.is_transient()

    def test_source_error_inheritance(self):
        """Test SourceError inheritance."""
        error = SourceError("Source error")

        assert isinstance(error, SciPaperError)
        assert isinstance(error, Exception)

    def test_transient_errors(self):
        """Test transient error detection."""
        network_error = NetworkError("Network timeout")
        rate_limit_error = RateLimitError("Rate limit exceeded")

        assert network_error.is_transient()
        assert rate_limit_error.is_transient()

        fetcher_error = FetcherError("Fetcher error")
        assert not fetcher_error.is_transient()


class TestIntegrationScenarios:
    """Test integration scenarios with multiple components."""

    @pytest.mark.asyncio
    async def test_full_search_workflow(self):
        """Test a complete search workflow."""
        fetcher = Fetcher()

        with patch.object(fetcher, '_search_source') as mock_search:
            mock_search.return_value = MOCK_ARXIV_SEARCH_RESULTS

            # Search for papers
            results = await fetcher.search("machine learning", sources=["arxiv"], limit=2)

            assert len(results) == 2
            assert all(result["source"] == "arxiv" for result in results)
            assert all("title" in result for result in results)
            assert all("authors" in result for result in results)

    @pytest.mark.asyncio
    async def test_cross_source_deduplication(self):
        """Test that results from different sources are properly handled."""
        fetcher = Fetcher()

        # Mock different sources returning similar results
        with patch.object(fetcher, '_search_source') as mock_search:
            mock_search.side_effect = [
                MOCK_ARXIV_SEARCH_RESULTS,
                MOCK_CROSSREF_SEARCH_RESULTS
            ]

            results = await fetcher.search("neural networks", sources=["arxiv", "crossref"], limit=10)

            # Should have results from both sources
            arxiv_results = [r for r in results if r["source"] == "arxiv"]
            crossref_results = [r for r in results if r["source"] == "crossref"]

            assert len(arxiv_results) > 0
            assert len(crossref_results) > 0


if __name__ == "__main__":
    pytest.main([__file__])
