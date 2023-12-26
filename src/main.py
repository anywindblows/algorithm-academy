from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api import api_router
from src.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
        allow_headers=[
            'Content-Type',
            'Set-Cookie',
            'Access-Control-Allow-Headers',
            'Access-Control-Allow-Origin',
            'Authorization',
        ],
    )

app.include_router(api_router)
