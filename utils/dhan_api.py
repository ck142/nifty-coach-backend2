import os
import requests
from datetime import datetime

def fetch_trades():
    client_id = os.getenv("DHAN_CLIENT_ID")
    token = os.getenv("DHAN_ACCESS_TOKEN")

    # Replace with actual Dhan endpoint if known
    url = "https://api.dhan.co/orders"  # Example placeholder
    headers = {
        "access-token": token,
        "client-id": client_id
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        trades = []
        for trade in data:
            trades.append({
                "order_id": trade.get("order_id"),
                "symbol": trade.get("symbol"),
                "side": trade.get("transaction_type"),
                "qty": trade.get("filled_quantity", 0),
                "price": trade.get("average_price", 0.0),
                "timestamp": trade.get("order_timestamp", datetime.utcnow().isoformat())
            })
        return trades
    except Exception as e:
        print("Failed to fetch trades:", e)
        return []