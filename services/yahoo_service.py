import yfinance as yf

def get_stock_info(stock_id: str):

    stock = yf.Ticker(stock_id + ".TW")

    return stock.info