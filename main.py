from fastapi import FastAPI
from routes.stock import router as stock_router
from routes.compare import router as compare_router

app = FastAPI()

app.include_router(stock_router)
app.include_router(compare_router)