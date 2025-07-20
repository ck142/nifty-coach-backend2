from fastapi import APIRouter

router = APIRouter()

@router.get("/sentiment/today")
def get_today_sentiment():
    return {
        "date": "2025-07-20",
        "overall_sentiment": "Bullish",
        "confidence": 67,
        "top_trades": [
            "Buy NIFTY 50 25600 CE",
            "Short Bank NIFTY Futures",
            "Bull Call Spread on Reliance"
        ]
    }

@router.get("/sentiment/history")
def get_sentiment_history():
    return [
        {"date": "2025-07-19", "predicted": "Bullish", "actual": "Bullish", "was_correct": True},
        {"date": "2025-07-18", "predicted": "Bearish", "actual": "Bullish", "was_correct": False}
    ]