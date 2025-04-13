from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List, Union
from financial_graph_generators import (
    plot_bs_vertical_grouped_stacked,
    plot_profit_step_chart,
    plot_cf_waterfall_chart
)

app = FastAPI()

DEFAULT_FONT_PATH = "/mnt/data/NotoSerifJP-Regular.ttf"

# ====== モデル定義 ======
class BSInput(BaseModel):
    bs_data: Dict[str, Dict[str, Dict[str, float]]]
    font_path: str = DEFAULT_FONT_PATH
    years: List[str]
    title: str

class ProfitStepInput(BaseModel):
    df_middle: Dict[str, Dict[str, float]]
    font_path: str = DEFAULT_FONT_PATH

class CFEntry(BaseModel):
    label: str
    amount: float

class CFInput(BaseModel):
    cf_values: List[CFEntry]
    font_path: str = DEFAULT_FONT_PATH
    title: str

# ====== エンドポイント定義 ======
@app.post("/plot_bs")
def plot_bs(input_data: BSInput):
    path = plot_bs_vertical_grouped_stacked(
        bs_data=input_data.bs_data,
        font_path=input_data.font_path,
        years=input_data.years,
        title=input_data.title
    )
    return {"image_path": path}

@app.post("/plot_profit_step")
def plot_profit_step(input_data: ProfitStepInput):
    path = plot_profit_step_chart(
        df_middle=input_data.df_middle,
        font_path=input_data.font_path
    )
    return {"image_path": path}

@app.post("/plot_cf")
def plot_cf(input_data: CFInput):
    cf_dict = [{"label": item.label, "amount": item.amount} for item in input_data.cf_values]
    path = plot_cf_waterfall_chart(
        cf_values=cf_dict,
        font_path=input_data.font_path,
        title=input_data.title
    )
    return {"image_path": path}
