# Contributing to SciPaper

Thank you for your interest in contributing to SciPaper! We welcome contributions from the community and are grateful for your help in making this project better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
- [Code Style](#code-style)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

This project adheres to a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/OpenPapers.git
   cd OpenPapers
   ```

3. **Set up the development environment**:
   ```bash
   # Create virtual environment
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # Install with development dependencies
   make dev-install
   ```

4. **Verify the setup**:
   ```bash
   make test
   make health
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix existing issues
- **Features**: Add new functionality
- **Documentation**: Improve docs, tutorials, or examples
- **Tests**: Add or improve test coverage
- **Tools**: Development tools, CI/CD improvements
- **UI/UX**: Improve user interfaces or CLI experience

### Finding Issues to Work On

- Check the [GitHub Issues](https://github.com/llamasearchai/OpenPapers/issues) page
- Look for issues labeled `good first issue` or `help wanted`
- Comment on issues you'd like to work on to avoid duplicate work

## Development Workflow

### 1. Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/issue-number-description
```

### 2. Make Your Changes

- Write clear, focused commits
- Add tests for new functionality
- Update documentation as needed
- Follow the code style guidelines

### 3. Test Your Changes

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run linting
make lint

# Run type checking
basedpyright src/ tests/
```

### 4. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with conventional format
git commit -m "feat: add new feature description

- Detailed explanation of changes
- Any breaking changes
- Related issue numbers"
```

### 5. Push and Create Pull Request

```bash
# Push your branch
git push origin feature/your-feature-name

# Create a Pull Request on GitHub
```

## Testing

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_sources.py -v

# Run with coverage
make test-cov

# Run tests matching pattern
pytest -k "test_search" -v
```

### Writing Tests

- Place tests in `tests/` directory
- Use descriptive test names: `test_should_do_something_when_condition`
- Use pytest fixtures for setup/teardown
- Mock external dependencies
- Test both success and error cases
- Aim for high test coverage

Example test structure:
```python
import pytest
from scipaper.core.fetcher import Fetcher

class TestFetcher:
    def test_search_returns_results(self):
        """Test that search returns expected results."""
        fetcher = Fetcher()
        # Test implementation
        pass

    def test_search_handles_errors_gracefully(self):
        """Test that search handles errors appropriately."""
        # Test implementation
        pass
```

## Code Style

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type annotations for all function parameters and return values
- Write docstrings for all public functions, classes, and modules
- Use descriptive variable and function names
- Keep functions focused and under 50 lines when possible

### Code Quality Tools

```bash
# Linting and formatting
ruff check src/ tests/
ruff format src/ tests/

# Type checking
basedpyright src/ tests/

# Import sorting
ruff check --select I src/ tests/
```

### Documentation

- Use Google-style docstrings
- Document all public APIs
- Include examples in docstrings where helpful
- Keep README and other docs up to date

## Commit Guidelines

This project uses [Conventional Commits](https://conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect code meaning (formatting, etc.)
- `refactor`: Code changes that neither fix bugs nor add features
- `test`: Adding or correcting tests
- `chore`: Changes to build process, tools, or auxiliary files

### Examples

```bash
git commit -m "feat: add Google Scholar source support

- Implement Google Scholar API integration
- Add comprehensive error handling
- Include tests for new functionality

Closes #123"

git commit -m "fix: handle empty search results

Fix crash when API returns empty result set
Add proper error handling for edge cases"

git commit -m "docs: update installation instructions

- Add Docker installation method
- Clarify Python version requirements
- Include troubleshooting section"
```

## Pull Request Process

### Before Submitting

1. **Update your branch** with the latest changes from main:
   ```bash
   git fetch origin
   git rebase origin/develop
   ```

2. **Run the full test suite**:
   ```bash
   make all
   ```

3. **Update documentation** if needed

4. **Squash commits** if you have many small commits:
   ```bash
   git rebase -i HEAD~n  # Where n is number of commits
   ```

### Pull Request Template

When creating a PR, please include:

- **Title**: Clear, descriptive title using conventional commit format
- **Description**: Detailed explanation of changes
- **Related Issues**: Link to any related issues (#123)
- **Breaking Changes**: Note any breaking changes
- **Testing**: Describe how the changes were tested
- **Screenshots**: If UI changes, include screenshots

### Review Process

1. **Automated Checks**: GitHub Actions will run tests and linting
2. **Code Review**: Maintainers will review the code
3. **Feedback**: Address any feedback from reviewers
4. **Approval**: PR will be merged once approved

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

- **Clear title** describing the issue
- **Steps to reproduce** the problem
- **Expected behavior** vs actual behavior
- **Environment info**:
  - Python version
  - Operating system
  - SciPaper version
- **Error messages** or stack traces
- **Minimal example** to reproduce the issue

### Feature Requests

For feature requests, please include:

- **Clear description** of the proposed feature
- **Use case** or problem it solves
- **Proposed implementation** if you have ideas
- **Alternatives considered**

## Recognition

Contributors will be recognized in:
- GitHub repository contributors list
- CHANGELOG.md for significant contributions
- Project documentation

Thank you for contributing to SciPaper!
