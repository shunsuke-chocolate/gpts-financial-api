
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import json
import os

from financial_graph_generators import (
    plot_bs_vertical_grouped_stacked_categorized,
    plot_profit_step_chart,
    plot_cashflow_waterfall
)

app = FastAPI()

FONT_PATH_DEFAULT = "./fonts/NotoSerifJP-Regular.ttf"

class BSInput(BaseModel):
    bs_data: Dict
    font_path: Optional[str] = None
    years: List[str]
    title: str

class ProfitStepInput(BaseModel):
    df_middle: Dict
    font_path: Optional[str] = None

class CFItem(BaseModel):
    label: str
    amount: float

class CFInput(BaseModel):
    cf_values: List[CFItem]
    font_path: Optional[str] = None
    title: str

@app.post("/plot_bs")
def plot_bs(input_data: BSInput):
    try:
        font_path = input_data.font_path or FONT_PATH_DEFAULT
        return plot_bs_vertical_grouped_stacked_categorized(
            input_data.bs_data,
            font_path,
            input_data.years,
            input_data.title
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"貸借対照表グラフ生成エラー: {str(e)}")

@app.post("/plot_profit_step")
def plot_profit_step(input_data: ProfitStepInput):
    try:
        font_path = input_data.font_path or FONT_PATH_DEFAULT
        return plot_profit_step_chart(
            input_data.df_middle,
            font_path
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"利益ステップグラフ生成エラー: {str(e)}")

@app.post("/plot_cf")
def plot_cf(input_data: CFInput):
    try:
        font_path = input_data.font_path or FONT_PATH_DEFAULT
        return plot_cashflow_waterfall(
            input_data.cf_values,
            font_path,
            input_data.title
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"キャッシュフローグラフ生成エラー: {str(e)}")
