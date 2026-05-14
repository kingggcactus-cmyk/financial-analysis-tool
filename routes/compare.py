from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from services.yahoo_service import get_stock_info

router = APIRouter()

@router.get("/compare/{stock1}/{stock2}", response_class=HTMLResponse)
def compare(stock1: str, stock2: str):

    info1 = get_stock_info(stock1)
    info2 = get_stock_info(stock2)

    return f"""
    <html>

    <head>
        <title>股票比較</title>
    </head>

    <body>

        <h1>{stock1} vs {stock2}</h1>

        <table border="1" cellpadding="10">

            <tr>
                <th>項目</th>
                <th>{stock1}</th>
                <th>{stock2}</th>
            </tr>

            <tr>
                <td>公司名稱</td>
                <td>{info1.get("longName")}</td>
                <td>{info2.get("longName")}</td>
            </tr>

            <tr>
                <td>股價</td>
                <td>{info1.get("currentPrice")}</td>
                <td>{info2.get("currentPrice")}</td>
            </tr>

            <tr>
                <td>EPS</td>
                <td>{info1.get("trailingEps")}</td>
                <td>{info2.get("trailingEps")}</td>
            </tr>

            <tr>
                <td>本益比</td>
                <td>{info1.get("trailingPE")}</td>
                <td>{info2.get("trailingPE")}</td>
            </tr>

            <tr>
                <td>ROE</td>
                <td>{info1.get("returnOnEquity")}</td>
                <td>{info2.get("returnOnEquity")}</td>
            </tr>

        </table>

    </body>

    </html>
    """