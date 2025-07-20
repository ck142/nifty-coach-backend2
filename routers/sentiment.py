
from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter(prefix="/api", tags=["Sentiment APIs"])

@router.get("/today_summary")
def get_today_summary():
    return {
        "sentiment": "Bullish",
        "confidence": 72,
        "recommendedTrades": [
            {"symbol": "NIFTY25JUL18400CE", "side": "BUY", "confidence": "84%"},
            {"symbol": "BANKNIFTY25JUL42000PE", "side": "SELL", "confidence": "78%"},
            {"symbol": "RELIANCE", "side": "BUY", "confidence": "74%"},
        ]
    }

@router.get("/sentiment_history")
def get_sentiment_history():
    base_date = datetime(2025, 7, 19)
    history = []
    sentiments = ["Bullish", "Bearish", "Neutral"]
    for i in range(15):
        day = base_date - timedelta(days=i)
        sent = sentiments[i % 3]
        history.append({
            "date": day.strftime("%Y-%m-%d"),
            "predicted": sent,
            "confidence": 60 + (i % 15),
            "expected": "+0.5% to +1%" if sent == "Bullish" else "-0.5% to -1%" if sent == "Bearish" else "-0.2% to +0.2%",
            "actual": "+0.65%" if i % 2 == 0 else "-0.42%",
            "correct": i % 3 != 0
        })
    return {"history": history}
