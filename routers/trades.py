from fastapi import APIRouter
from db.database import get_db_connection
from utils.dhan_api import fetch_trades
from datetime import datetime

router = APIRouter()

@router.post("/sync_trades")
def sync_trades():
    conn = get_db_connection()
    cursor = conn.cursor()
    trades = fetch_trades()

    new_trades = 0
    for trade in trades:
        try:
            cursor.execute(
                "INSERT INTO trades (order_id, symbol, side, qty, price, timestamp) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (order_id) DO NOTHING",
                (
                    trade["order_id"],
                    trade["symbol"],
                    trade["side"],
                    trade["qty"],
                    trade["price"],
                    trade["timestamp"]
                )
            )
            new_trades += 1
        except Exception as e:
            print("Error inserting trade:", e)

    conn.commit()
    cursor.close()
    conn.close()
    return {"message": f"Synced {new_trades} new trades", "trades": trades}