
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ValidationError
from typing import Any, Dict
from financial_graph_generators import plot_profit_step, plot_bs_vertical_grouped_stacked, plot_cf_waterfall

app = FastAPI()

class ProfitStepInput(BaseModel):
    df_middle: Dict[str, Dict[str, float]]
    font_path: str

class BSInput(BaseModel):
    bs_data: Dict[str, Dict[str, list]]
    font_path: str
    years: list
    title: str

class CFInput(BaseModel):
    cf_values: list
    font_path: str
    title: str

@app.post("/plot_profit_step")
async def plot_profit_step_endpoint(payload: Dict[str, Any]):
    data = payload.get("data")
    if not data:
        raise HTTPException(status_code=400, detail="Missing 'data' field")
    try:
        validated_data = ProfitStepInput(**data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    image_path = plot_profit_step(validated_data.df_middle, validated_data.font_path)
    return {"image_path": image_path}

@app.post("/plot_bs")
async def plot_bs_endpoint(payload: Dict[str, Any]):
    data = payload.get("data")
    if not data:
        raise HTTPException(status_code=400, detail="Missing 'data' field")
    try:
        validated_data = BSInput(**data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    image_path = plot_bs_vertical_grouped_stacked(validated_data.bs_data, validated_data.font_path, validated_data.years, validated_data.title)
    return {"image_path": image_path}

@app.post("/plot_cf")
async def plot_cf_endpoint(payload: Dict[str, Any]):
    data = payload.get("data")
    if not data:
        raise HTTPException(status_code=400, detail="Missing 'data' field")
    try:
        validated_data = CFInput(**data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    image_path = plot_cf_waterfall(validated_data.cf_values, validated_data.font_path, validated_data.title)
    return {"image_path": image_path}
