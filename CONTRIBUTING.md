# Contributing to API Hub

First off, thank you for considering contributing to API Hub. This project aims to build the definitive API marketplace for African developers, and every contribution helps.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Commit Guidelines](#commit-guidelines)
- [Branch Naming Convention](#branch-naming-convention)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Review Process](#review-process)
- [Release Process](#release-process)
- [Getting Help](#getting-help)

---

## Code of Conduct

We are committed to providing a welcoming and harassment-free experience for everyone.

### Our Standards

- Be respectful and inclusive
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, trolling, or insulting comments
- Publishing others' private information
- Other unethical or unprofessional conduct

### Enforcement

Project maintainers have the right to remove, edit, or reject comments, commits, code, issues, and other contributions that do not align with this Code of Conduct.

---

## Getting Started

### Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11+ | Backend |
| Node.js | 20+ | Frontend (future) |
| Docker | 24+ | Local infrastructure |
| Docker Compose | 2.20+ | Local services |
| Git | 2.40+ | Version control |
| Make | 4.0+ | Task runner |

### First Time Setup

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/API-HUB.git
cd API-HUB

# 2. Add the main repository as an upstream remote
git remote add upstream https://github.com/Aldorax/API-HUB.git

# Note: To sync your fork with the latest updates from upstream, run:
# git pull upstream main

# 3. Navigate to the backend directory
cd apps/backend

# 4. Copy environment variables
cp .env.example .env
# Edit .env with your values (at minimum, change JWT_SECRET_KEY)

# 5. Install dependencies and setup virtual environment
make dev-install

# 6. Start local infrastructure (PostgreSQL & Redis)
make dc-up

# 7. Run database migrations
make migrate

# 8. Start development server
make dev
```

Your local instance will be available at `http://localhost:8000`  
Interactive API docs: `http://localhost:8000/docs`

---

## Development Setup

### Available Make Commands

| Command | Description |
|---------|-------------|
| `make dev` | Start development server with auto-reload |
| `make test` | Run all tests |
| `make test-cov` | Run tests with coverage report |
| `make format` | Format code with Black |
| `make lint` | Lint code with Ruff |
| `make type-check` | Run MyPy type checking |
| `make check` | Run all code quality checks |
| `make migrate` | Run database migrations |
| `make migrate-new msg="..."` | Create new migration |
| `make dc-up` | Start Postgres and Redis containers |
| `make dc-down` | Stop containers |
| `make clean` | Clean virtual environment and cache |

### Running Individual Components

```bash
# Backend only
make dev

# Tests only
make test

# Specific test file
pytest tests/test_auth.py -v

# Celery worker (background tasks)
make worker

# Celery beat scheduler (cron jobs)
make beat
```

---

## Commit Guidelines

We follow **Conventional Commits** specification for consistent and automated changelog generation.

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(auth): add magic link authentication` |
| `fix` | Bug fix | `fix(proxy): handle timeout errors gracefully` |
| `docs` | Documentation only | `docs(readme): update installation instructions` |
| `style` | Code style (formatting, semicolons, etc.) | `style(backend): format with black` |
| `refactor` | Code change that neither fixes bug nor adds feature | `refactor(proxy): extract routing logic to separate module` |
| `perf` | Performance improvement | `perf(db): add index on user_email column` |
| `test` | Adding missing tests | `test(auth): add tests for magic link expiry` |
| `chore` | Maintenance tasks | `chore(deps): update fastapi to 0.115.0` |
| `ci` | CI/CD changes | `ci(github): add test workflow` |
| `revert` | Revert previous commit | `revert: revert feat(auth) commit abc123` |

### Scopes

| Scope | Description |
|-------|-------------|
| `auth` | Authentication and magic links |
| `proxy` | API gateway and request proxying |
| `billing` | Usage metering, invoicing, payments |
| `api` | API listing and discovery |
| `provider` | Provider dashboard and onboarding |
| `consumer` | Consumer dashboard and subscriptions |
| `admin` | Admin panel and moderation |
| `db` | Database models, migrations |
| `celery` | Background tasks |
| `docker` | Docker configuration |
| `ci` | CI/CD pipelines |
| `deps` | Dependency updates |
| `docs` | Documentation |

### Subject

- Use imperative, present tense: "add" not "added" nor "adds"
- First letter lowercase
- No dot at the end
- Maximum 72 characters

### Body

- Explain **what** and **why**, not how
- Wrap at 72 characters
- Use bullet points for multiple changes

### Footer

- Reference issues: `Closes #123`, `Fixes #456`
- Breaking changes: `BREAKING CHANGE: description`

### Valid Commit Examples

```bash
# Simple commit
feat(auth): add magic link authentication for login

# With body
fix(proxy): handle timeout when provider API is slow

When provider API takes more than 30 seconds to respond,
the gateway now returns 504 Gateway Timeout instead of
hanging indefinitely.

Closes #42

# Breaking change
refactor(billing): change commission calculation method

BREAKING CHANGE: Commission is now calculated on subtotal
before tax instead of after tax. This affects provider
payout amounts.

# Multiple scopes
feat(api,provider): add OpenAPI spec upload support

- Providers can now upload OpenAPI spec files
- API documentation is auto-generated
- Test console uses spec for request validation
```

### Commit Tools

```bash
# Install commitizen for guided commits
pip install commitizen

# Then use
cz commit
```

---

## Branch Naming Convention

| Branch Type | Format | Example |
|-------------|--------|---------|
| Feature | `feature/<issue-number>-<short-description>` | `feature/42-magic-link-auth` |
| Bugfix | `bugfix/<issue-number>-<short-description>` | `bugfix/99-proxy-timeout` |
| Hotfix | `hotfix/<version>-<short-description>` | `hotfix/v1.0.1-payout-crash` |
| Release | `release/<version>` | `release/v1.0.0` |
| Documentation | `docs/<short-description>` | `docs/api-gateway` |
| Experiment | `experiment/<short-description>` | `experiment/new-proxy-engine` |

### Branch Lifecycle

```bash
# Create feature branch from main
git checkout main
git pull origin main
git checkout -b feature/42-magic-link-auth

# After PR is merged, delete branch
git checkout main
git pull origin main
git branch -d feature/42-magic-link-auth
```

---

## Pull Request Process

### Before Submitting

- [ ] Run `make check` (formatting, linting, type checking)
- [ ] Run `make test` (all tests pass)
- [ ] Update documentation if needed
- [ ] Add tests for new functionality
- [ ] Ensure commit messages follow conventions
- [ ] Rebase on latest `main`

### PR Title Format

Same as commit format: `<type>(<scope>): <description>`

Example: `feat(auth): add magic link authentication`

### PR Description Template

```markdown
## Description

<!-- Provide a clear description of what this PR does -->

## Related Issue

<!-- Link to the issue this PR addresses -->
Closes #123

## Type of Change

- [ ] feat: new feature
- [ ] fix: bug fix
- [ ] docs: documentation update
- [ ] refactor: code refactor
- [ ] perf: performance improvement
- [ ] test: test update
- [ ] chore: maintenance

## Testing

<!-- Describe how you tested your changes -->

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed

## Screenshots (if applicable)

<!-- Add screenshots for UI changes -->

## Checklist

- [ ] My code follows the project's coding standards
- [ ] I have added tests that prove my fix/feature works
- [ ] I have updated the documentation
- [ ] My commit messages follow the conventional commits spec
- [ ] I have rebased on the latest main branch
- [ ] All CI checks pass

## Additional Context

<!-- Any other information that would help reviewers -->
```

### PR Review Process

1. **Submit PR** – Fill out template, request reviewers
2. **CI Checks** – Automated tests, linting, type checking must pass
3. **Review** – At least one maintainer must approve
4. **Changes** – Address review feedback, push updates
5. **Merge** – Squash and merge (maintainers only)

### PR Merge Requirements

| Requirement | Status |
|-------------|--------|
| CI passes | ✅ Required |
| At least 1 approval | ✅ Required |
| No merge conflicts | ✅ Required |
| Tests pass | ✅ Required |
| Documentation updated | ⚠️ If applicable |
| Breaking change flagged | ⚠️ If applicable |

---

## Coding Standards

### Python (Backend)

| Tool | Purpose | Command |
|------|---------|---------|
| Black | Code formatting | `make format` |
| Ruff | Linting | `make lint` |
| MyPy | Type checking | `make type-check` |

### Python Style Guide

```python
# Imports order
# 1. Standard library
import json
from typing import Optional

# 2. Third-party
from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String

# 3. Local
from src.models import User
from src.services import auth_service

# Type hints required
async def get_user(user_id: int, db: AsyncSession) -> Optional[User]:
    """Get user by ID.

    Args:
        user_id: The user's ID
        db: Database session

    Returns:
        User object if found, None otherwise
    """
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Python files | snake_case | `auth_service.py` |
| Python classes | PascalCase | `UserModel` |
| Python functions | snake_case | `get_user_by_email` |
| Python constants | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| Environment variables | UPPER_SNAKE_CASE | `DATABASE_URL` |

---

## Testing Guidelines

### Writing Tests

```python
# tests/test_auth.py
import pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.asyncio
async def test_magic_link_request():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/auth/magic-link",
            json={"email": "test@example.com"}
        )
        assert response.status_code == 200
        assert response.json()["message"] == "Magic link sent"
```

### Running Tests

```bash
# All tests
make test

# Specific test file
pytest tests/test_auth.py -v

# Specific test function
pytest tests/test_auth.py::test_magic_link_request -v

# With coverage
make test-cov

# Skip slow tests
pytest tests/ -v -m "not slow"
```

### Coverage Requirements

| Area | Minimum Coverage |
|------|------------------|
| Core services | 90% |
| API routes | 85% |
| Models | 80% |
| Utils | 70% |

---

## Documentation

### Where to Document

| Location | What to Document |
|----------|------------------|
| `README.md` | Project overview, quick start |
| `CONTRIBUTING.md` | Contribution guidelines (this file) |
| `docs/architecture.md` | System architecture |
| Docstrings | Functions, classes, modules |
| Inline comments | Complex logic, edge cases |

### Docstring Format (Google Style)

```python
def calculate_commission(amount: float, provider_rate: float) -> float:
    """Calculate platform commission for a transaction.

    The commission is calculated as (amount * platform_rate) where
    platform_rate is the current commission percentage configured
    in settings.

    Args:
        amount: Transaction amount in Naira
        provider_rate: Provider's commission rate (0.0 to 1.0)

    Returns:
        Commission amount in Naira

    Raises:
        ValueError: If amount is negative or provider_rate outside [0,1]

    Example:
        >>> calculate_commission(1000, 0.20)
        200.0
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not 0 <= provider_rate <= 1:
        raise ValueError("Provider rate must be between 0 and 1")

    return amount * provider_rate
```

---

## Issue Reporting

### Bug Report Template

```markdown
## Description
<!-- Clear description of the bug -->

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll to '...'
4. See error

## Expected Behavior
<!-- What should have happened -->

## Actual Behavior
<!-- What actually happened -->

## Environment
- OS: [e.g., Ubuntu 22.04]
- Python Version: [e.g., 3.11]
- FastAPI Version: [e.g., 0.115.0]

## Additional Context
<!-- Screenshots, logs, etc. -->
```

### Feature Request Template

```markdown
## Problem Statement
<!-- What problem does this feature solve? -->

## Proposed Solution
<!-- How should it work? -->

## Alternatives Considered
<!-- What other approaches did you consider? -->

## Use Case
<!-- Who will use this and when? -->

## Additional Context
<!-- Any other information -->
```

---

## Review Process

### Reviewer Responsibilities

- [ ] Code follows style guide
- [ ] Tests are adequate
- [ ] Documentation is updated
- [ ] No security issues
- [ ] No performance regressions
- [ ] Commit messages are clear

### Review Comments Format

```markdown
# Suggestion (non-blocking)
**Suggestion:** Consider using a more descriptive variable name here.

# Required Change (blocking)
**Required:** Add error handling for the case where the API key is invalid.

# Question
**Question:** Why did you choose this approach over using a decorator?

# Praise
**Nice:** Great test coverage on this function!
```

### Approval Criteria

| Role | Required |
|------|----------|
| Author | Self-review complete |
| Reviewer 1 | Code review approval |
| CI | All checks pass |
| Maintainer | Final merge approval |

---

## Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible features
- **PATCH**: Backward-compatible bug fixes

### Release Checklist

```markdown
## Release vX.Y.Z Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in pyproject.toml
- [ ] Release branch created
- [ ] PR merged to main
- [ ] Tag created: git tag vX.Y.Z
- [ ] Release notes drafted
- [ ] Deployed to staging
- [ ] Smoke tests pass
- [ ] Deployed to production
```

### Creating a Release

```bash
# 1. Create release branch
git checkout -b release/v1.0.0

# 2. Update version in pyproject.toml
# Change version = "1.0.0"

# 3. Update CHANGELOG.md

# 4. Commit changes
git commit -m "chore(release): bump version to v1.0.0"

# 5. Push and create PR
git push origin release/v1.0.0

# 6. After PR merges, tag the release
git checkout main
git pull origin main
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

---

## Getting Help

### Communication Channels

| Channel | Purpose |
|---------|---------|
| GitHub Issues | Bug reports, feature requests |
| GitHub Discussions | Questions, ideas, general discussion |
| Email | `support@naijaapihub.com` |

### Before Asking for Help

1. Check the documentation
2. Search existing issues
3. Check if your question has been answered in Discussions
4. Try to reproduce the issue in isolation

### How to Ask

```markdown
**What are you trying to do?**
[Clear description]

**What have you tried?**
[Steps you've taken]

**What error messages are you seeing?**
[Full error output]

**What environment are you using?**
[OS, Python version, etc.]
```

---

## Recognition

Contributors will be recognized in:

- `CONTRIBUTORS.md` file
- Release notes
- Project website (coming soon)

---

## License

By contributing to API Hub, you agree that your contributions will be licensed under the project's proprietary license.

---

**Thank you for contributing to API Hub! 🚀**
```

This updated version uses your correct repo URL, project name, and directory structure. You can now copy this into your `CONTRIBUTING.md` file.