from stock import Stock
import math

# Managing stocks, recording trades, and calculating metrics.
class StockMarket:
    def __init__(self):
        self.stocks: Dict[str, Stock] = {}
    
    def add_stock(self, stock: Stock):
        self.stocks[stock.symbol] = stock
    
    def calculate_gbce_all_share_index(self) -> float:
        prices = [stock.calculate_volume_weighted_stock_price() for stock in self.stocks.values() if stock.calculate_volume_weighted_stock_price() > 0]
        if not prices:
            return 0
        product = math.prod(prices)
        return product ** (1 / len(prices))
