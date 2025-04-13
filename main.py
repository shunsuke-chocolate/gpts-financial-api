
from fastapi import FastAPI, Request
from financial_graph_generators import (
    plot_profit_step_chart,
    plot_bs_vertical_grouped_stacked,
    plot_cf_waterfall_labeled
)
import json

app = FastAPI()

@app.post("/plot_profit_step")
async def plot_profit_step(request: Request):
    body = await request.json()
    df_middle = body["df_middle"]
    if isinstance(df_middle, str):
        df_middle = json.loads(df_middle)
    font_path = body.get("font_path", "./fonts/NotoSerifJP-Regular.ttf")
    image_path = plot_profit_step_chart(df_middle, font_path)
    return {"image_path": image_path}

@app.post("/plot_bs")
async def plot_bs(request: Request):
    body = await request.json()
    bs_data = body["bs_data"]
    if isinstance(bs_data, str):
        bs_data = json.loads(bs_data)
    font_path = body.get("font_path", "./fonts/NotoSerifJP-Regular.ttf")
    years = body.get("years", [])
    title = body.get("title", "")
    image_path = plot_bs_vertical_grouped_stacked(bs_data, years, font_path, title)
    return {"image_path": image_path}

@app.post("/plot_cf")
async def plot_cf(request: Request):
    body = await request.json()
    cf_values = body["cf_values"]
    if isinstance(cf_values, str):
        cf_values = json.loads(cf_values)
    font_path = body.get("font_path", "./fonts/NotoSerifJP-Regular.ttf")
    title = body.get("title", "")
    image_path = plot_cf_waterfall_labeled(cf_values, font_path, title)
    return {"image_path": image_path}
