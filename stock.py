from datetime import datetime, timedelta
from typing import List, Dict
import math
from trade import Trade

# Representing a stock with attributes like symbol, type, last dividend, fixed dividend, and par value.
class Stock:
    def __init__(self, symbol: str, stock_type: str, last_dividend: float, fixed_dividend: float, par_value: float):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades: List[Trade] = []
    
    def calculate_dividend_yield(self, price: float) -> float:
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if self.stock_type == "Common":
            return self.last_dividend / price
        elif self.stock_type == "Preferred":
            return (self.fixed_dividend * self.par_value) / price
        else:
            raise ValueError("Invalid stock type.")
    
    def calculate_pe_ratio(self, price: float) -> float:
        dividend = self.last_dividend if self.stock_type == "Common" else (self.fixed_dividend * self.par_value)
        if dividend == 0:
            return float('inf')  # P/E ratio is undefined if dividend is 0
        return price / dividend
    
    def record_trade(self, quantity: int, trade_type: str, price: float):
        if trade_type not in {"BUY", "SELL"}:
            raise ValueError("Trade type must be 'BUY' or 'SELL'.")
        self.trades.append(Trade(datetime.now(), quantity, trade_type, price))
    
    def calculate_volume_weighted_stock_price(self) -> float:
        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        recent_trades = [trade for trade in self.trades if trade.timestamp >= five_minutes_ago]
        total_price_quantity = sum(trade.price * trade.quantity for trade in recent_trades)
        total_quantity = sum(trade.quantity for trade in recent_trades)
        return total_price_quantity / total_quantity if total_quantity > 0 else 0
