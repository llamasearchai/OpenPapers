"""Mock data fixtures for comprehensive testing."""

from typing import Dict, List, Any

# Mock paper data for different sources
MOCK_ARXIV_PAPER = {
    "id": "2103.12345",
    "title": "Attention Is All You Need",
    "authors": ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Łukasz Kaiser", "Illia Polosukhin"],
    "date": "2017-06-12",
    "abstract": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.",
    "journal": "arXiv:1706.03762",
    "doi": "10.48550/arXiv.1706.03762",
    "url": "https://arxiv.org/abs/1706.03762",
    "source": "arxiv",
    "categories": ["cs.CL", "cs.LG"]
}

MOCK_CROSSREF_PAPER = {
    "id": "10.1038/nature12373",
    "title": "CRISPR-Cas systems for editing, regulating and targeting genomes",
    "authors": ["Jennifer A. Doudna", "Emmanuelle Charpentier"],
    "date": "2014-02-28",
    "abstract": "The Clustered Regularly Interspaced Short Palindromic Repeats (CRISPR) and CRISPR-associated (Cas) systems have revolutionized biotechnology and biomedical applications. This review discusses the mechanisms, applications, and future prospects of CRISPR-Cas systems.",
    "journal": "Nature Biotechnology",
    "doi": "10.1038/nbt.2842",
    "url": "https://doi.org/10.1038/nbt.2842",
    "source": "crossref",
    "publisher": "Nature Publishing Group"
}

MOCK_PUBMED_PAPER = {
    "id": "25393562",
    "title": "CRISPR-Cas9 genome editing in human cells",
    "authors": ["Patrick D. Hsu", "David A. Scott", "Joshua A. Weinstein", "F. Ann Ran", "Silvana Konermann", "Vineeta Agarwala", "Yinqing Li", "Eli J. Fine", "Xuebing Wu", "Ophir Shalem", "Thomas J. Cradick", "Luciano A. Marraffini", "Gang Bao", "Feng Zhang"],
    "date": "2014-11-01",
    "abstract": "CRISPR-Cas9 is a versatile genome editing technology that has revolutionized biomedical research. This paper describes the development and application of CRISPR-Cas9 for genome editing in human cells.",
    "journal": "Cell",
    "doi": "10.1016/j.cell.2014.11.013",
    "url": "https://pubmed.ncbi.nlm.nih.gov/25393562/",
    "source": "pubmed",
    "pmid": "25393562"
}

MOCK_SEMANTIC_SCHOLAR_PAPER = {
    "id": "649def34f8be52c8b66281af98ae884c09aef38b",
    "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "authors": ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"],
    "date": "2018-10-11",
    "abstract": "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers.",
    "journal": "arXiv:1810.04805",
    "doi": "10.48550/arXiv.1810.04805",
    "url": "https://arxiv.org/abs/1810.04805",
    "source": "semanticscholar",
    "venue": "arXiv",
    "year": 2018,
    "citation_count": 45230,
    "influential_citation_count": 1250
}

MOCK_GOOGLE_SCHOLAR_PAPER = {
    "id": "test_gs_id_123",
    "title": "Deep Learning",
    "authors": ["Ian Goodfellow", "Yoshua Bengio", "Aaron Courville"],
    "date": "2016-01-01",
    "abstract": "Deep learning is a subset of machine learning in artificial intelligence that has networks capable of learning unsupervised from data that is unstructured or unlabeled.",
    "journal": "MIT Press",
    "doi": None,
    "url": "https://www.deeplearningbook.org/",
    "source": "googlescholar",
    "citations": 15420
}

# Mock search results
MOCK_ARXIV_SEARCH_RESULTS = [
    MOCK_ARXIV_PAPER,
    {
        "id": "2001.12345",
        "title": "Generative Adversarial Networks",
        "authors": ["Ian J. Goodfellow", "Jean Pouget-Abadie", "Mehdi Mirza", "Bing Xu", "David Warde-Farley", "Sherjil Ozair", "Aaron Courville", "Yoshua Bengio"],
        "date": "2014-06-10",
        "abstract": "We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G.",
        "journal": "arXiv:1406.2661",
        "doi": "10.48550/arXiv.1406.2661",
        "url": "https://arxiv.org/abs/1406.2661",
        "source": "arxiv"
    }
]

MOCK_CROSSREF_SEARCH_RESULTS = [
    MOCK_CROSSREF_PAPER,
    {
        "id": "10.1126/science.aaa6090",
        "title": "Development and applications of CRISPR-Cas9 for genome engineering",
        "authors": ["Feng Zhang"],
        "date": "2014-11-28",
        "abstract": "The CRISPR-Cas9 system has been adapted for genome editing in many organisms. This review covers the development and applications of CRISPR-Cas9 technology.",
        "journal": "Cell",
        "doi": "10.1016/j.cell.2014.11.010",
        "url": "https://doi.org/10.1016/j.cell.2014.11.010",
        "source": "crossref"
    }
]

# Mock API responses
MOCK_ARXIV_API_RESPONSE = {
    "feed": {
        "entry": [
            {
                "id": "http://arxiv.org/abs/1706.03762v5",
                "title": "Attention Is All You Need",
                "summary": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks...",
                "author": [
                    {"name": "Ashish Vaswani"},
                    {"name": "Noam Shazeer"}
                ],
                "published": "2017-06-12T17:57:37Z",
                "category": {"@term": "cs.CL"}
            }
        ]
    }
}

MOCK_CROSSREF_API_RESPONSE = {
    "message": {
        "DOI": "10.1038/nbt.2842",
        "title": ["CRISPR-Cas systems for editing, regulating and targeting genomes"],
        "author": [
            {"given": "Jennifer A.", "family": "Doudna"},
            {"given": "Emmanuelle", "family": "Charpentier"}
        ],
        "published": {"date-parts": [[2014, 2, 28]]},
        "abstract": "The Clustered Regularly Interspaced Short Palindromic Repeats (CRISPR)...",
        "container-title": ["Nature Biotechnology"],
        "publisher": "Nature Publishing Group"
    }
}

# Mock identifiers for parsing tests
MOCK_TEXT_WITH_IDENTIFIERS = """
Check out this amazing paper on transformers: https://arxiv.org/abs/1706.03762
Also see the Nature Biotechnology paper at doi:10.1038/nbt.2842
And this one from Cell: https://doi.org/10.1016/j.cell.2014.11.013
"""

MOCK_PARSED_IDENTIFIERS = [
    {
        "type": "doi",
        "value": "10.1038/nbt.2842",
        "position": "127"
    },
    {
        "type": "doi",
        "value": "10.1016/j.cell.2014.11.013",
        "position": "184"
    },
    {
        "type": "arxiv",
        "value": "1706.03762",
        "position": "69"
    },
    {
        "type": "url",
        "value": "https://arxiv.org/abs/1706.03762",
        "position": "47"
    },
    {
        "type": "url",
        "value": "https://doi.org/10.1016/j.cell.2014.11.013",
        "position": "168"
    }
]

# Mock agent responses
MOCK_AGENT_ANALYSIS = {
    "query": "transformer neural networks",
    "sources": ["arxiv", "crossref"],
    "papers": MOCK_ARXIV_SEARCH_RESULTS,
    "analysis": "The transformer architecture represents a fundamental breakthrough in neural network design. Key innovations include self-attention mechanisms and parallel processing capabilities that have revolutionized natural language processing and other domains."
}

# Mock configuration for testing
MOCK_CONFIG = {
    "OPENAI_API_KEY": "test-key",
    "OPENAI_MODEL": "gpt-4",
    "OLLAMA_HOST": "localhost",
    "OLLAMA_PORT": 11434,
    "FASTAPI_HOST": "0.0.0.0",
    "FASTAPI_PORT": 8000,
    "LOG_LEVEL": "INFO"
}

# Helper functions for creating mock objects
def create_mock_paper(**overrides) -> Dict[str, Any]:
    """Create a mock paper with default values."""
    base_paper = {
        "id": "test-paper-123",
        "title": "Test Paper Title",
        "authors": ["Test Author"],
        "date": "2023-01-01",
        "abstract": "This is a test paper abstract.",
        "journal": "Test Journal",
        "doi": "10.1234/test.doi",
        "url": "https://example.com/paper",
        "source": "test"
    }
    base_paper.update(overrides)
    return base_paper

def create_mock_search_results(count: int = 5, source: str = "test") -> List[Dict[str, Any]]:
    """Create a list of mock search results."""
    return [
        create_mock_paper(
            id=f"{source}-paper-{i}",
            title=f"Test Paper {i}",
            source=source
        )
        for i in range(count)
    ]

def create_mock_fetcher_response(success: bool = True, **kwargs) -> Dict[str, Any]:
    """Create a mock fetcher response."""
    if success:
        return create_mock_paper(**kwargs)
    return None

# Export all mock data
__all__ = [
    "MOCK_ARXIV_PAPER",
    "MOCK_CROSSREF_PAPER",
    "MOCK_PUBMED_PAPER",
    "MOCK_SEMANTIC_SCHOLAR_PAPER",
    "MOCK_GOOGLE_SCHOLAR_PAPER",
    "MOCK_ARXIV_SEARCH_RESULTS",
    "MOCK_CROSSREF_SEARCH_RESULTS",
    "MOCK_ARXIV_API_RESPONSE",
    "MOCK_CROSSREF_API_RESPONSE",
    "MOCK_TEXT_WITH_IDENTIFIERS",
    "MOCK_PARSED_IDENTIFIERS",
    "MOCK_AGENT_ANALYSIS",
    "MOCK_CONFIG",
    "create_mock_paper",
    "create_mock_search_results",
    "create_mock_fetcher_response"
]
