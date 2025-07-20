from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers.trades import router as trades_router
from routers.sentiment import router as sentiment_router
from db.database import Base, engine
import db.models

from routers import sentiment

load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

app.include_router(sentiment.router)

# Enable CORS (adjust allow_origins for production if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(trades_router)
app.include_router(sentiment_router)

# Health check endpoint
@app.get("/ping")
def ping():
    return {"message": "pong"}