from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import urllib.request
from financial_graph_generators import (
    generate_balance_sheet_graph,
    generate_profit_waterfall_chart,
    generate_cashflow_waterfall_chart
)

app = FastAPI(
    title="財務三表グラフ生成API",
    description="決算書データをもとに財務三表のグラフを生成するAPI",
    version="1.0.0",
    servers=[
        {"url": "https://gpts-financial-api.onrender.com", "description": "Render上の本番環境"}
    ]
)

# フォント定義と自動取得設定
FONT_PATH = "./NotoSerifJP-Regular.ttf"
FONT_URL = "https://raw.githubusercontent.com/shunsuke-chocolate/gpts-financial-api/main/NotoSerifJP-Regular.ttf"

if not os.path.exists(FONT_PATH):
    try:
        urllib.request.urlretrieve(FONT_URL, FONT_PATH)
    except Exception as e:
        print(f"フォントの取得に失敗しました: {e}")

os.makedirs("output", exist_ok=True)

@app.get("/graph/balance-sheet")
def get_balance_sheet():
    output_path = "output/balance_sheet.png"
    generate_balance_sheet_graph(FONT_PATH, output_path)
    return FileResponse(output_path, media_type="image/png")

@app.get("/graph/profit-step")
def get_profit_step():
    output_path = "output/profit_step.png"
    generate_profit_waterfall_chart(FONT_PATH, output_path)
    return FileResponse(output_path, media_type="image/png")

@app.get("/graph/cashflow")
def get_cashflow():
    output_path = "output/cashflow.png"
    generate_cashflow_waterfall_chart(FONT_PATH, output_path)
    return FileResponse(output_path, media_type="image/png")
