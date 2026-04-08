# Naija API Hub

**API marketplace for African developers.**  
Discover, integrate, and monetize APIs – built with FastAPI, PostgreSQL, and Redis.

---

## Overview

Naija API Hub is a platform where developers can:
- **Consume** APIs (SMS, verification, payments, utilities) with one API key and unified billing.
- **Provide** APIs (list, monetize, manage subscribers) with automatic metering and payouts.

Built for Nigeria and Africa – with local pricing, local support, and data residency.

---

## Features

- 🔐 **Magic link authentication** – No passwords, email‑based login.
- 👥 **Role‑based access** – Consumer, Provider, Admin roles.
- 🔑 **API key management** – Generate/revoke keys for gateway access.
- 🧩 **API variant model** – Categorised, versioned API listings.
- 📊 **Usage metering** – Track requests per subscription.
- 🐳 **Containerised dependencies** – Postgres & Redis via Docker Compose.
- 📚 **Scalar API docs** – Interactive reference at `/docs`.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI (Python 3.11+) |
| **Database** | PostgreSQL 15 (async SQLAlchemy) |
| **Cache / Queue** | Redis 7 |
| **Migrations** | Alembic |
| **Auth** | JWT (magic links via Resend) |
| **Container** | Docker & Docker Compose |
| **Task runner** | Makefile |

---

## Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Make
- Git

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/naija-api-hub.git
cd naija-api-hub/apps/backend

# 2. Create environment file
cp .env.example .env
# Edit .env – at least set JWT_SECRET_KEY (openssl rand -hex 32)

# 3. Install dependencies & setup virtual environment
make dev-install

# 4. Start PostgreSQL and Redis containers
make dc-up

# 5. Run database migrations
make migrate

# 6. Start the development server
make dev
```

The API will be available at `http://localhost:8000`.  
Interactive documentation: `http://localhost:8000/docs`

---

## Available Make Commands

| Command | Description |
|---------|-------------|
| `make dev` | Run FastAPI dev server (auto‑reload) |
| `make dc-up` | Start Postgres & Redis containers |
| `make dc-down` | Stop containers |
| `make migrate` | Apply database migrations |
| `make migrate-new msg="..."` | Generate a new migration |
| `make test` | Run tests |
| `make format` | Format code with Black |
| `make lint` | Lint with Ruff |
| `make check` | Format, lint, type‑check |
| `make clean` | Remove virtual environment and caches |

---


## Testing

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run a specific test
pytest tests/test_auth.py -v
```

---

## Deployment

Build the production Docker image:
```bash
make docker-build
```

Run the container:
```bash
docker run -d --env-file .env -p 8000:8000 naija-api-hub-backend:latest
```

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on commits, PRs, and coding standards.

---

## License

Proprietary – all rights reserved.

---

## Contact

- Email: support@naijaapihub.com
- Discord: Souske.aldini

---

**Built with ❤️ in Nigeria.**