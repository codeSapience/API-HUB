import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Naija API Hub")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/naija_api_hub"
    )

    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # JWT
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "change-me-in-production")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    MAGIC_LINK_EXPIRY_MINUTES: int = int(os.getenv("MAGIC_LINK_EXPIRY_MINUTES", "15"))

    # Email
    RESEND_API_KEY: str = os.getenv("RESEND_API_KEY", "")
    FROM_EMAIL: str = os.getenv("FROM_EMAIL", "noreply@naijaapihub.com")

    # Stripe
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")

    # Paystack
    PAYSTACK_SECRET_KEY: str = os.getenv("PAYSTACK_SECRET_KEY", "")

    # Platform
    PLATFORM_COMMISSION_PERCENT: float = float(os.getenv("PLATFORM_COMMISSION_PERCENT", "20.0"))


settings = Settings()
