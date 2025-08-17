from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="WeTreat Backend")

# CORS configuration
origins = ["*"]  # Adjust for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Optional: Alembic migrations on startup
@app.on_event("startup")
async def run_alembic_migrations():
    try:
        if os.getenv("RUN_MIGRATIONS", "true") == "true":
            print("⚙️ Running Alembic migrations...")
            from alembic import command
            from alembic.config import Config
            cfg = Config("alembic.ini")
            command.upgrade(cfg, "head")
            print("✅ Alembic migration completed.")
    except Exception as e:
        print("❌ Alembic migration failed:", str(e))

# Include your routers here (comment out until files exist)
# from app.api.routes import auth, intake, admin, physician, consultations
# app.include_router(auth.router)
# app.include_router(intake.router)
# app.include_router(admin.router)
# app.include_router(physician.router)
# app.include_router(consultations.router)
