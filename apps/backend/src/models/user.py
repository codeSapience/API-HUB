from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    roles = Column(JSON, default=["consumer"])  # consumer, provider, admin
    is_active = Column(Boolean, default=True)
    provider_name = Column(String(255), nullable=True)
    payout_details = Column(JSON, nullable=True)  # bank account, paystack email
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
