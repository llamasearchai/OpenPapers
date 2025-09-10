.PHONY: help install dev-install test lint format clean build docker-build docker-run

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install the package
	pip install -e .

dev-install: ## Install with development dependencies
	pip install -e ".[dev]"

test: ## Run tests
	pytest -v

test-cov: ## Run tests with coverage
	pytest --cov=src/scipaper --cov-report=html

lint: ## Run linting
	ruff check src/ tests/

format: ## Format code
	ruff format src/ tests/

type-check: ## Run type checking
	basedpyright src/ tests/

clean: ## Clean up cache files and build artifacts
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.pyd" -delete
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/

build: ## Build the package
	python -m build

docker-build: ## Build Docker image
	docker build -t scipaper:latest .

docker-run: ## Run Docker container
	docker run --rm -p 8000:8000 --env-file .env scipaper:latest

docker-compose-up: ## Run with docker-compose
	docker compose up --build

health: ## Check application health
	scipaper health

dev: ## Run in development mode
	uvicorn scipaper.main:app --host 0.0.0.0 --port 8000 --reload

all: clean lint test build ## Run full CI pipeline
