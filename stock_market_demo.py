from stock import Stock
from trade import Trade
from stock_market import StockMarket
from datetime import datetime
import math

class StockMarketDemo:
    def run():
        market = StockMarket()

        stock_tea = Stock("TEA", "Common", 0, 0, 100)
        stock_pop = Stock("POP", "Common", 8, 0, 100)
        stock_ale = Stock("ALE", "Common", 23, 0, 60)
        stock_gin = Stock("GIN", "Preferred", 8, 2, 100)
        stock_joe = Stock("JOE", "Common", 13, 0, 250)

        market.add_stock(stock_tea)
        market.add_stock(stock_pop)
        market.add_stock(stock_ale)
        market.add_stock(stock_gin)
        market.add_stock(stock_joe)

        stock_pop.record_trade(10, "BUY", 120)
        stock_pop.record_trade(15, "SELL", 125)

        print("Dividend Yield for POP:", stock_pop.calculate_dividend_yield(120))
        print("P/E Ratio for POP:", stock_pop.calculate_pe_ratio(120))
        print("Volume Weighted Stock Price for POP:", stock_pop.calculate_volume_weighted_stock_price())
        print("GBCE All Share Index:", market.calculate_gbce_all_share_index())

if __name__ == "__main__":
    StockMarketDemo.run()