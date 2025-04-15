from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from financial_graph_generators import (
    generate_balance_sheet_graph,
    generate_profit_step_chart,
    generate_cashflow_waterfall_chart
)

app = FastAPI(
    title="財務三表グラフ生成API",
    description="決算書データをもとに財務三表のグラフを生成するAPI",
    version="1.0.0"
)

# フォントパス（※ローカルにあるものを直接指定）
FONT_PATH = "./NotoSerifJP-Regular.ttf"
os.makedirs("output", exist_ok=True)

@app.get("/graph/balance-sheet")
def get_balance_sheet():
    output_path = "output/balance_sheet.png"
    generate_balance_sheet_graph(FONT_PATH, output_path)
    return FileResponse(output_path, media_type="image/png")

@app.get("/graph/profit-step")
def get_profit_step():
    output_path = "output/profit_step.png"
    generate_profit_step_chart(FONT_PATH, output_path)
    return FileResponse(output_path, media_type="image/png")

@app.get("/graph/cashflow")
def get_cashflow():
    output_path = "output/cashflow.png"
    generate_cashflow_waterfall_chart(FONT_PATH, output_path)
    return FileResponse(output_path, media_type="image/png")
