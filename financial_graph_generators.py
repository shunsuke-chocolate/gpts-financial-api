
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import os

def load_font(font_path):
    if not font_path or not os.path.isfile(font_path):
        font_path = "./NotoSerifJP-Regular.ttf"
    return fm.FontProperties(fname=font_path)

def plot_bs_vertical_grouped_stacked(bs_data, years, font_path, title):
    font_prop = load_font(font_path)

    assets = bs_data.get("資産", {})
    liabilities_and_net_assets = bs_data.get("負債・純資産", {})

    df_assets = pd.DataFrame(assets, index=years)
    df_ln = pd.DataFrame(liabilities_and_net_assets, index=years)

    fig, ax = plt.subplots(figsize=(10, 6))
    df_assets.plot(kind="bar", stacked=True, position=0, width=0.4, ax=ax, label="資産", legend=True)
    df_ln.plot(kind="bar", stacked=True, position=1, width=0.4, ax=ax, label="負債・純資産", legend=True)

    ax.set_title(title, fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    ax.legend(prop=font_prop)
    plt.xticks(rotation=0, fontproperties=font_prop)
    plt.tight_layout()
    output_path = "bs_vertical_grouped_stacked.png"
    plt.savefig(output_path)
    return output_path

def plot_profit_step_only(df_middle, font_path):
    font_prop = load_font(font_path)
    step_keys = ["売上総利益", "営業利益", "経常利益", "税引前当期純利益", "当期純利益"]

    values = [df_middle.get(k, {}).get("当期", 0) for k in step_keys]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(step_keys, values)
    ax.set_title("利益ステップグラフ", fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.tight_layout()
    output_path = "profit_step_only.png"
    plt.savefig(output_path)
    return output_path

def plot_cf_waterfall(cf_values, font_path, title):
    font_prop = load_font(font_path)

    df = pd.DataFrame(cf_values)
    df["cumulative"] = df["amount"].cumsum()
    df["start"] = df["cumulative"].shift(fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(len(df)):
        color = "green" if df["amount"][i] >= 0 else "red"
        ax.bar(df["label"][i], df["amount"][i], bottom=df["start"][i], color=color)

    ax.set_title(title, fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.tight_layout()
    output_path = "cf_waterfall_labeled.png"
    plt.savefig(output_path)
    return output_path
