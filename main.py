from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import yfinance as yf

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>財報API成功</h1>"

@app.get("/stock/{stock_id}", response_class=HTMLResponse)
def get_stock(stock_id: str):

    stock = yf.Ticker(stock_id + ".TW")

    info = stock.info

    return f"""
    <h1>股票財報資訊</h1>

    <p>股票代號：{stock_id}</p>

    <hr>

    <p>公司名稱：{info.get("longName")}</p>

    <p>股價：{info.get("currentPrice")}</p>

    <p>EPS：{info.get("trailingEps")}</p>

    <p>本益比：{info.get("trailingPE")}</p>

    <p>毛利率：{info.get("grossMargins")}</p>

    <p>營益率：{info.get("operatingMargins")}</p>

    <p>ROE：{info.get("returnOnEquity")}</p>

    <p>負債比：{info.get("debtToEquity")}</p>
    """

@app.get("/compare/{stock1}/{stock2}", response_class=HTMLResponse)
def compare(stock1: str, stock2: str):

    s1 = yf.Ticker(stock1 + ".TW")
    s2 = yf.Ticker(stock2 + ".TW")

    info1 = s1.fast_info
    info2 = s2.fast_info

    return f"""
    <h1>股票比較</h1>

    <table border="1" cellpadding="10">

        <tr>
            <th>項目</th>
            <th>{stock1}</th>
            <th>{stock2}</th>
        </tr>

        <tr>
            <td>股價</td>
            <td>{info1.get("lastPrice")}</td>
            <td>{info2.get("lastPrice")}</td>
        </tr>

        <tr>
            <td>今日最高</td>
            <td>{info1.get("dayHigh")}</td>
            <td>{info2.get("dayHigh")}</td>
        </tr>

        <tr>
            <td>今日最低</td>
            <td>{info1.get("dayLow")}</td>
            <td>{info2.get("dayLow")}</td>
        </tr>

    </table>
    """