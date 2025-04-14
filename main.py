
from fastapi import FastAPI, Request
from financial_graph_generators import (
    plot_profit_step_only,
    plot_cf_waterfall_labeled,
    plot_bs_vertical_grouped_stacked
)

app = FastAPI()

@app.post("/plot_profit_step")
async def plot_profit_step(request: Request):
    body = await request.json()
    data = body.get("data", {})
    df_middle = data.get("df_middle")
    font_path = data.get("font_path", "./NotoSerifJP-Regular.ttf")
    image_path = plot_profit_step_only(df_middle, font_path)
    return {"image_path": image_path}

@app.post("/plot_cf")
async def plot_cf(request: Request):
    body = await request.json()
    data = body.get("data", {})
    cf_values = data.get("cf_values")
    font_path = data.get("font_path", "./NotoSerifJP-Regular.ttf")
    title = data.get("title", "")
    image_path = plot_cf_waterfall_labeled(cf_values, font_path, title)
    return {"image_path": image_path}

@app.post("/plot_bs")
async def plot_bs(request: Request):
    body = await request.json()
    data = body.get("data", {})
    bs_data = data.get("bs_data")
    font_path = data.get("font_path", "./NotoSerifJP-Regular.ttf")
    years = data.get("years", [])
    title = data.get("title", "")
    image_path = plot_bs_vertical_grouped_stacked(bs_data, font_path, years, title)
    return {"image_path": image_path}
