from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from gpts_chart_generator import plot_profit_waterfall_chart

app = FastAPI(
    title="財務グラフ生成API",
    description="損益計算書・貸借対照表・CFのグラフを生成します。",
    version="1.0.0",
    servers=[
        {"url": "https://gpts-financial-api.onrender.com", "description": "本番API"}
    ]
)

@app.get("/graph/profit-step")
def get_profit_step():
    data = {
        "売上高": 1_285_005,
        "売上原価": -894_648,
        "売上総利益": 390_356 - 894_648,
        "販管費": -353_947,
        "営業利益": 36_409,
        "営業外収益": 6_134,
        "営業外費用": -1_706,
        "経常利益": 40_837,
        "特別利益": 154,
        "特別損失": -14_714,
        "税引前利益": 26_277,
        "法人税等": -11_938,
        "当期純利益": 14_338
    }
    output_path = "output/profit_step.png"
    os.makedirs("output", exist_ok=True)
    plot_profit_waterfall_chart(data, "2025年2月期 損益計算書ウォーターフォール", output_path)
    return FileResponse(output_path, media_type="image/png")
