# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive test suite with mock data fixtures
- Professional GitHub Actions CI/CD pipeline
- Enhanced development tooling (Makefile, .env.example)
- Professional README with complete documentation
- Docker support with multi-platform compatibility
- Google Scholar source integration
- Comprehensive error handling and logging
- Type safety improvements for Python 3.9+ compatibility

### Changed
- Updated Python requirement to >=3.9 for broader compatibility
- Enhanced CLI with better formatting and error messages
- Improved API documentation and OpenAPI schema
- Updated dependency versions for better stability
- Professionalized commit history with conventional commits

### Fixed
- Python 3.9 compatibility issues with type annotations
- Missing dependencies in package configuration
- Repository URL inconsistencies in documentation
- Ruff configuration duplicate entries
- Import errors in test modules

### Security
- Added security scanning in CI pipeline
- Input validation improvements
- Dependency vulnerability checks

## [1.0.1] - 2025-01-09

### Added
- Production-ready codebase with no stubs or placeholders
- Complete FastAPI REST API with automatic documentation
- Rich CLI interface with interactive features
- Multi-source academic paper search (arXiv, Crossref, PubMed, Semantic Scholar)
- Optional AI agent integration (OpenAI and Ollama)
- Comprehensive logging and monitoring
- Docker containerization support
- Rate limiting and caching capabilities

### Changed
- Migrated from development to production-ready state
- Enhanced error handling throughout the application
- Improved configuration management with Pydantic settings
- Updated documentation with complete usage examples

### Fixed
- Removed all placeholder code and TODO comments
- Fixed linting and type checking issues
- Resolved dependency conflicts
- Improved test coverage and reliability

## [1.0.0] - 2025-01-08

### Added
- Initial release of SciPaper toolkit
- Basic CLI functionality for paper search and parsing
- Core API structure and source implementations
- Initial test suite and documentation
- Basic Docker support

### Changed
- Repository consolidation and cleanup
- Code organization improvements
- Dependency management updates

### Fixed
- Initial setup and configuration issues
- Basic functionality bugs and edge cases

---

## Development Guidelines

### Commit Message Format
This project uses [Conventional Commits](https://conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

### Versioning
This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Support

For support and questions:
- Email: nikjois@llamasearch.ai
- Issues: [GitHub Issues](https://github.com/llamasearchai/OpenPapers/issues)
- Documentation: [README.md](README.md)
