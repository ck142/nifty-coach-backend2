from fastapi import APIRouter
from db.database import SessionLocal
from db.models import Trade
from utils.dhan_api import fetch_trades
from sqlalchemy.exc import IntegrityError
from datetime import datetime

router = APIRouter()

@router.post("/sync_trades")
def sync_trades():
    db = SessionLocal()
    new_count = 0
    try:
        trades = fetch_trades()
        for trade in trades:
            new_trade = Trade(
                order_id=trade["order_id"],
                symbol=trade["symbol"],
                side=trade["side"],
                qty=trade["qty"],
                price=trade["price"],
                timestamp=trade.get("timestamp", datetime.utcnow())
            )
            db.add(new_trade)
            try:
                db.commit()
                new_count += 1
            except IntegrityError:
                db.rollback()  # order_id already exists
        return {"message": f"Synced {new_count} new trades", "trades": trades}
    finally:
        db.close()

@router.get("/get_trades")
def get_trades():
    db = SessionLocal()
    try:
        trades = db.query(Trade).order_by(Trade.timestamp.desc()).limit(500).all()
        return [
            {
                "order_id": t.order_id,
                "symbol": t.symbol,
                "side": t.side,
                "qty": t.qty,
                "price": t.price,
                "timestamp": t.timestamp
            }
            for t in trades
        ]
    finally:
        db.close()
