from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .dependencies.database import engine, Base
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination

from .routes import product
from .routes import category
from .routes import order
from .routes import payment_methods
from .routes import payment_notifications
from .routes import payment_callback
from .routes import user
from .routes import admin
from .routes import auth
from .routes import article_category
from .routes import article
from .routes import language  # 新增
from .routes import upload  # 新增

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"OMG! The client sent invalid data!: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router, prefix="/api/v1", tags=["products"])
app.include_router(category.router, prefix="/api/v1", tags=["categories"])
app.include_router(order.router, prefix="/api/v1", tags=["orders"])
app.include_router(payment_methods.router, prefix="/api/v1", tags=["payment-methods"])
app.include_router(payment_notifications.router, prefix="/api/v1", tags=["payment_notifications"])
app.include_router(payment_callback.router, prefix="/api/v1", tags=["payment_callback"])
app.include_router(user.router, prefix="/api/v1", tags=["user"])
app.include_router(admin.router, prefix="/api/v1", tags=["admin"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(article_category.router, prefix="/api/v1", tags=["article-categories"])
app.include_router(article.router, prefix="/api/v1", tags=["articles"])
app.include_router(language.router, prefix="/api/v1", tags=["language"])  # 新增
app.include_router(upload.router, prefix="/api/v1", tags=["upload"])  # 新增

add_pagination(app)
