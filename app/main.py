from fastapi import FastAPI
from app.database import engine
from app.models import Base
from .routers.v1 import company as v1_company_routes
from .routers.v1 import ambassador as v1_ambassador_routes
from .routers.v1 import session as v1_session_routes

app = FastAPI()

app.include_router(v1_company_routes.router, prefix="/api/v1/company", tags=["v1 - Sessions"])
app.include_router(v1_ambassador_routes.router, prefix="/api/v1/ambassador", tags=["v1 - Brand Ambassadors"])
app.include_router(v1_session_routes.router, prefix="/api/v1/session", tags=["v1 - Sessions"])

# Create database tables (only in dev mode; in production, use migrations)
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

