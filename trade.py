from datetime import datetime

# Storing trade details with timestamp, quantity, buy/sell indicator, and price.
class Trade:
    def __init__(self, timestamp: datetime, quantity: int, trade_type: str, price: float):
        self.timestamp = timestamp
        self.quantity = quantity
        self.trade_type = trade_type
        self.price = price