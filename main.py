from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
from financial_graph_generators import (
    plot_bs_vertical_grouped_stacked,
    plot_profit_step_only,
    plot_cf_waterfall_labeled
)

app = FastAPI()


class BSInput(BaseModel):
    bs_data: Dict[str, Dict[str, float]]
    font_path: str
    years: List[str]
    title: str


class ProfitStepInput(BaseModel):
    df_middle: Dict[str, float]
    font_path: str


class CFItem(BaseModel):
    label: str
    amount: float


class CFInput(BaseModel):
    cf_values: List[CFItem]
    font_path: str
    title: str


@app.post("/plot_bs")
def plot_bs(input_data: BSInput):
    output_path = plot_bs_vertical_grouped_stacked(
        input_data.bs_data,
        input_data.font_path,
        input_data.years,
        input_data.title
    )
    return {"path": output_path}


@app.post("/plot_profit_step")
def plot_profit_step(input_data: ProfitStepInput):
    output_path = plot_profit_step_only(
        input_data.df_middle,
        input_data.font_path
    )
    return {"path": output_path}


@app.post("/plot_cf")
def plot_cf(input_data: CFInput):
    cf_data = [item.dict() for item in input_data.cf_values]
    output_path = plot_cf_waterfall_labeled(
        cf_data,
        input_data.font_path,
        input_data.title
    )
    return {"path": output_path}
