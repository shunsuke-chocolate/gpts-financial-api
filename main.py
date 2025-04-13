
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from financial_graph_generators import (
    plot_profit_step,
    plot_cf,
    plot_bs_vertical_grouped_stacked
)

app = FastAPI()

class ProfitStepInput(BaseModel):
    df_middle: Dict[str, Dict[str, float]]
    font_path: str

class CFItem(BaseModel):
    label: str
    amount: float

class CFInput(BaseModel):
    cf_values: List[CFItem]
    font_path: str
    title: str

class BSInput(BaseModel):
    bs_data: Dict[str, Dict[str, float]]
    font_path: str
    years: List[str]
    title: str

@app.post("/plot_profit_step")
def generate_profit_step_chart(data: ProfitStepInput):
    try:
        output_path = plot_profit_step(data.df_middle, data.font_path)
        return {"image_path": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/plot_cf")
def generate_cf_chart(data: CFInput):
    try:
        cf_dicts = [item.dict() for item in data.cf_values]
        output_path = plot_cf(cf_dicts, data.font_path, data.title)
        return {"image_path": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/plot_bs")
def generate_bs_chart(data: BSInput):
    try:
        output_path = plot_bs_vertical_grouped_stacked(data.bs_data, data.font_path, data.years, data.title)
        return {"image_path": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
