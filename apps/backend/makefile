# ============================================================
# Naija API Hub - Makefile
# ============================================================
# Usage: make <command>
# Commands: help, install, dev, migrate, test, lint, format, etc.
# ============================================================

# Variables
PYTHON := python3
VENV := .venv
PYTHON_VENV := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
UVICORN := $(VENV)/bin/uvicorn
BLACK := $(VENV)/bin/black
RUFF := $(VENV)/bin/ruff
MYPY := $(VENV)/bin/mypy
PYTEST := $(VENV)/bin/pytest
ALEMBIC := $(VENV)/bin/alembic
CELERY := $(VENV)/bin/celery

# Docker (for local Postgres + Redis)
DOCKER_COMPOSE := docker-compose

# App settings
APP_MODULE := src.main:app
HOST := 0.0.0.0
PORT := 8000

# ============================================================
# Help (default command)
# ============================================================
.PHONY: help
help:
	@echo "Naija API Hub - Available Commands"
	@echo "===================================="
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make install      - Create virtual environment and install dependencies"
	@echo "  make dev-install  - Install with dev dependencies"
	@echo "  make clean        - Remove virtual environment and cache files"
	@echo ""
	@echo "Development:"
	@echo "  make dev          - Run FastAPI dev server (with auto-reload)"
	@echo "  make docker-up    - Start Postgres and Redis containers"
	@echo "  make docker-down  - Stop containers"
	@echo "  make migrate      - Run database migrations"
	@echo "  make migrate-new  - Create new migration (msg=description)"
	@echo "  make shell        - Open Python shell with app context"
	@echo ""
	@echo "Workers & Background:"
	@echo "  make worker       - Start Celery worker"
	@echo "  make beat         - Start Celery beat scheduler"
	@echo ""
	@echo "Code Quality:"
	@echo "  make format       - Format code with Black"
	@echo "  make lint         - Run Ruff linter"
	@echo "  make type-check   - Run MyPy type checker"
	@echo "  make check        - Run all checks (format, lint, type-check)"
	@echo ""
	@echo "Testing:"
	@echo "  make test         - Run all tests"
	@echo "  make test-cov     - Run tests with coverage report"
	@echo "  make test-watch   - Run tests in watch mode"
	@echo ""
	@echo "Database:"
	@echo "  make db-reset     - Reset database (drop all tables, remigrate)"
	@echo "  make db-seed      - Seed database with test data"
	@echo ""
	@echo "Production:"
	@echo "  make prod         - Run production server (no auto-reload)"
	@echo "  make docker-build - Build production Docker image"
	@echo ""
	@echo "Utilities:"
	@echo "  make logs         - View Docker logs"
	@echo "  make psql         - Connect to Postgres database"
	@echo "  make redis-cli    - Connect to Redis"

# ============================================================
# Setup & Installation
# ============================================================
.PHONY: install
install:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Upgrading pip..."
	$(PIP) install --upgrade pip
	@echo "Installing dependencies..."
	$(PIP) install -e .
	@echo "Installation complete!"
	@echo "Run 'make dev-install' to add dev dependencies"

.PHONY: dev-install
dev-install: install
	@echo "Installing dev dependencies..."
	$(PIP) install -e ".[dev]"
	@echo "Dev dependencies installed!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Copy .env.example to .env and fill in values"
	@echo "  2. Run 'make docker-up' to start database and Redis"
	@echo "  3. Run 'make migrate' to setup database schema"
	@echo "  4. Run 'make dev' to start the server"

.PHONY: clean
clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV)
	@echo "Removing Python cache files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "Removing test coverage files..."
	rm -rf .pytest_cache .coverage htmlcov
	@echo "Removing mypy cache..."
	rm -rf .mypy_cache
	@echo "Clean complete!"

# ============================================================
# Development Server
# ============================================================
.PHONY: dev
dev:
	@echo "Starting FastAPI development server..."
	$(UVICORN) $(APP_MODULE) --reload --host $(HOST) --port $(PORT)

.PHONY: prod
prod:
	@echo "Starting FastAPI production server..."
	$(UVICORN) $(APP_MODULE) --host $(HOST) --port $(PORT)

# ============================================================
# Docker (Local Infrastructure)
# ============================================================
.PHONY: docker-up
docker-up:
	@echo "Starting Postgres and Redis containers..."
	$(DOCKER_COMPOSE) up -d
	@echo "Containers started!"
	@echo "Postgres: localhost:5432"
	@echo "Redis: localhost:6379"

.PHONY: docker-down
docker-down:
	@echo "Stopping containers..."
	$(DOCKER_COMPOSE) down
	@echo "Containers stopped"

.PHONY: docker-build
docker-build:
	@echo "Building production Docker image..."
	docker build -t naija-api-hub:latest .

.PHONY: logs
logs:
	$(DOCKER_COMPOSE) logs -f

# ============================================================
# Database Migrations
# ============================================================
.PHONY: migrate
migrate:
	@echo "Running database migrations..."
	$(ALEMBIC) upgrade head

.PHONY: migrate-new
migrate-new:
	@if [ -z "$(msg)" ]; then \
		echo "Error: Please provide a migration message. Usage: make migrate-new msg='description'"; \
		exit 1; \
	fi
	@echo "Creating new migration: $(msg)"
	$(ALEMBIC) revision --autogenerate -m "$(msg)"

.PHONY: migrate-down
migrate-down:
	@echo "Reverting last migration..."
	$(ALEMBIC) downgrade -1

.PHONY: db-reset
db-reset:
	@echo "WARNING: This will delete all data in the database!"
	@read -p "Are you sure? (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		echo "Resetting database..."; \
		$(ALEMBIC) downgrade base; \
		$(ALEMBIC) upgrade head; \
		echo "Database reset complete!"; \
	else \
		echo "Cancelled."; \
	fi

.PHONY: db-seed
db-seed:
	@echo "Seeding database with test data..."
	$(PYTHON_VENV) -c "from src.seed import seed_database; seed_database()"

.PHONY: psql
psql:
	@echo "Connecting to Postgres..."
	$(DOCKER_COMPOSE) exec postgres psql -U postgres -d naija_api_hub

.PHONY: redis-cli
redis-cli:
	@echo "Connecting to Redis..."
	$(DOCKER_COMPOSE) exec redis redis-cli

# ============================================================
# Celery Workers
# ============================================================
.PHONY: worker
worker:
	@echo "Starting Celery worker..."
	$(CELERY) -A src.tasks.worker worker --loglevel=info

.PHONY: beat
beat:
	@echo "Starting Celery beat scheduler..."
	$(CELERY) -A src.tasks.worker beat --loglevel=info

# ============================================================
# Code Quality
# ============================================================
.PHONY: format
format:
	@echo "Formatting code with Black..."
	$(BLACK) src/ tests/

.PHONY: lint
lint:
	@echo "Linting with Ruff..."
	$(RUFF) check src/ tests/

.PHONY: lint-fix
lint-fix:
	@echo "Linting and auto-fixing with Ruff..."
	$(RUFF) check src/ tests/ --fix

.PHONY: type-check
type-check:
	@echo "Type checking with MyPy..."
	$(MYPY) src/

.PHONY: check
check: format lint type-check
	@echo "All checks passed!"

.PHONY: pre-commit
pre-commit:
	@echo "Running pre-commit hooks..."
	$(VENV)/bin/pre-commit run --all-files

# ============================================================
# Testing
# ============================================================
.PHONY: test
test:
	@echo "Running tests..."
	$(PYTEST) tests/ -v

.PHONY: test-cov
test-cov:
	@echo "Running tests with coverage..."
	$(PYTEST) tests/ -v --cov=src --cov-report=term-missing --cov-report=html
	@echo "Coverage report generated at htmlcov/index.html"

.PHONY: test-watch
test-watch:
	@echo "Running tests in watch mode..."
	$(PYTEST) tests/ -v --looponfail

.PHONY: test-integration
test-integration:
	@echo "Running integration tests..."
	$(PYTEST) tests/ -v -m integration

# ============================================================
# Shell & Utilities
# ============================================================
.PHONY: shell
shell:
	@echo "Starting Python shell with app context..."
	$(PYTHON_VENV) -c "import asyncio; from src.main import app; from src.database import AsyncSessionLocal; from src.config import settings; print('App loaded. Use await for async functions.')" || true
	$(PYTHON_VENV) -m IPython || $(PYTHON_VENV)

.PHONY: env
env:
	@echo "Environment variables:"
	@echo "PYTHON=$(PYTHON)"
	@echo "VENV=$(VENV)"
	@echo "DATABASE_URL=postgresql://postgres:postgres@localhost:5432/naija_api_hub"
	@echo "REDIS_URL=redis://localhost:6379/0"

# ============================================================
# Quick Start (All-in-One)
# ============================================================
.PHONY: quickstart
quickstart:
	@echo "========================================="
	@echo "Naija API Hub - Quick Start"
	@echo "========================================="
	@echo ""
	@echo "Step 1: Installing dependencies..."
	@$(MAKE) dev-install
	@echo ""
	@echo "Step 2: Starting Docker containers..."
	@$(MAKE) docker-up
	@echo ""
	@echo "Step 3: Running migrations..."
	@$(MAKE) migrate
	@echo ""
	@echo "Step 4: Starting development server..."
	@echo ""
	@echo "========================================="
	@echo "Naija API Hub is running at http://localhost:8000"
	@echo "API docs available at http://localhost:8000/docs"
	@echo "========================================="
	@$(MAKE) dev