from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import yfinance as yf
import plotly.graph_objects as go

router = APIRouter()

@router.get("/stock/{stock_id}", response_class=HTMLResponse)
def get_stock(stock_id: str):

    stock = yf.Ticker(stock_id + ".TW")

    info = stock.info
    hist = stock.history(period="6mo")
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["Close"],
            mode="lines",
            name="股價"
        )
    )
    
    chart_html = fig.to_htma(full_htma=False)

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
    
    {chart_html}
    
    """