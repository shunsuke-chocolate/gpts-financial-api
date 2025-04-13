from fastapi import FastAPI
from pydantic import BaseModel
from financial_graph_generators import (
    plot_bs_vertical_grouped_stacked_categorized,
    plot_profit_step_chart,
    plot_cashflow_waterfall
)
import pandas as pd

app = FastAPI()

class BSInput(BaseModel):
    bs_data: dict
    font_path: str
    years: list
    title: str

class ProfitStepInput(BaseModel):
    df_middle: dict
    font_path: str

class CFInput(BaseModel):
    cf_values: list
    font_path: str
    title: str

@app.post("/plot_bs")
def call_plot_bs(input: BSInput):
    path = plot_bs_vertical_grouped_stacked_categorized(
        bs_data=input.bs_data,
        font_path=input.font_path,
        years=input.years,
        title=input.title
    )
    return {"image_path": path}

@app.post("/plot_profit_step")
def call_plot_profit_step(input: ProfitStepInput):
    df = pd.DataFrame(input.df_middle)
    path = plot_profit_step_chart(df, input.font_path)
    return {"image_path": path}

@app.post("/plot_cf")
def call_plot_cf(input: CFInput):
    path = plot_cashflow_waterfall(
        cf_values=input.cf_values,
        font_path=input.font_path,
        title=input.title
    )
    return {"image_path": path}
