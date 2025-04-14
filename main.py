from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Optional
import uvicorn
from financial_graph_generators import (
    plot_bs_vertical_grouped_stacked,
    plot_profit_step_only,
    plot_cf_waterfall_labeled
)
from financial_pdf_parser import extract_structured_financial_data

app = FastAPI(title="Financial Graph API", version="1.0.0")

# ==== データモデル定義 ====
class BSInput(BaseModel):
    bs_data: Dict[str, Dict[str, float]] = Field(...,
        example={
            "資産": {"流動資産": 50000, "固定資産": 100000},
            "負債・純資産": {"流動負債": 30000, "固定負債": 70000, "純資産": 50000}
        })
    years: List[str] = Field(..., min_items=1)
    font_path: Optional[str] = "./NotoSerifJP-Regular.ttf"
    title: Optional[str] = "貸借対照表"

    @validator('bs_data')
    def validate_bs_data(cls, v):
        required_sections = ["資産", "負債・純資産"]
        for section in required_sections:
            if section not in v:
                raise ValueError(f"必須セクション '{section}' が存在しません")
        return v

class ProfitStepInput(BaseModel):
    df_middle: Dict[str, Dict[str, float]] = Field(...,
        example={
            "売上総利益": {"当期": 50000},
            "営業利益": {"当期": 30000}
        })
    font_path: Optional[str] = "./NotoSerifJP-Regular.ttf"

class CFItem(BaseModel):
    label: str
    amount: float

class CFInput(BaseModel):
    cf_values: List[CFItem] = Field(..., min_items=3)
    font_path: Optional[str] = "./NotoSerifJP-Regular.ttf"
    title: Optional[str] = "キャッシュフロー分析"

# ==== APIエンドポイント ====
@app.post("/plot_bs")
async def generate_bs_graph(data: BSInput):
    try:
        image_path = plot_bs_vertical_grouped_stacked(
            data.bs_data,
            data.years,
            data.font_path,
            data.title
        )
        return {"image_path": image_path}
    except FileNotFoundError as e:
        raise HTTPException(400, detail=f"フォントエラー: {str(e)}")
    except KeyError as e:
        raise HTTPException(400, detail=f"必須データ不足: {str(e)}")
    except Exception as e:
        raise HTTPException(500, detail=f"内部エラー: {str(e)}")

@app.post("/plot_profit_step")
async def generate_profit_graph(data: ProfitStepInput):
    required_keys = ["売上総利益", "営業利益", "経常利益", "税引前当期純利益", "当期純利益"]
    missing = [k for k in required_keys if k not in data.df_middle]
    if missing:
        raise HTTPException(400, detail=f"必須項目不足: {missing}")
    
    try:
        image_path = plot_profit_step_only(data.df_middle, data.font_path)
        return {"image_path": image_path}
    except Exception as e:
        raise HTTPException(500, detail=f"グラフ生成エラー: {str(e)}")

@app.post("/plot_cf")
async def generate_cf_graph(data: CFInput):
    try:
        image_path = plot_cf_waterfall_labeled(
            [item.dict() for item in data.cf_values],
            data.font_path,
            data.title
        )
        return {"image_path": image_path}
    except KeyError as e:
        raise HTTPException(400, detail=f"不正なデータ形式: {str(e)}")
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

@app.post("/parse_pdf")
async def parse_financial_pdf(pdf_url: str):
    try:
        return extract_structured_financial_data(pdf_url)
    except Exception as e:
        raise HTTPException(500, detail=f"PDF解析エラー: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
