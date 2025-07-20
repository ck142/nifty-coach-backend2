from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import trades, sentiment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trades.router)
app.include_router(sentiment.router)

@app.get("/")
def root():
    return {"message": "Nifty Coach Backend running"}