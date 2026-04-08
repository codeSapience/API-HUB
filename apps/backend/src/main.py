from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.api.v1 import auth, users  # import auth router, and users
from scalar_fastapi import get_scalar_api_reference

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    debug=settings.DEBUG,
    docs_url="/scalar" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.DEBUG else ["https://app.naijaapihub.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")  # add this line


# Health check endpoint
@app.get("/health", tags=["System"])
async def health_check():
    """Check if the API is running."""
    return {"status": "ok"}


# Root endpoint
@app.get("/", tags=["System"])
async def root():
    """Welcome message."""
    return {
        "name": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs" if settings.DEBUG else None,
    }


@app.get("/docs", include_in_schema=False)
async def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=f"{settings.APP_NAME} API Reference",
    )


# Future routes will be included here as they are created:
# from src.api.v1 import auth, apis, subscriptions, proxy
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
# app.include_router(apis.router, prefix="/api/v1/apis", tags=["APIs"])
# etc.
