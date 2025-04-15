import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.font_manager import FontProperties
import os

FONT_PATH = "./fonts/NotoSerifJP-Regular.ttf"

def get_font():
    if os.path.exists(FONT_PATH):
        return FontProperties(fname=FONT_PATH)
    else:
        return FontProperties()  # fallback

def plot_profit_waterfall_chart(pl_data: dict, title: str, output_path: str):
    font_prop = get_font()
    fig, ax = plt.subplots(figsize=(12, 6))

    labels = list(pl_data.keys())
    values = list(pl_data.values())
    cumulative = [0]
    for v in values[:-1]:
        cumulative.append(cumulative[-1] + v)
    cumulative = cumulative[:-1]
    colors = ['green' if val >= 0 else 'red' for val in values]

    for i, (label, val, bottom) in enumerate(zip(labels, values, cumulative)):
        ax.bar(label, val, bottom=bottom, color=colors[i])
        ax.text(i, bottom + val / 2, f"{val:,.0f}", ha='center', va='center',
                fontproperties=font_prop, fontsize=10)

    ax.set_title(title, fontproperties=font_prop, fontsize=14)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontproperties=font_prop, rotation=45)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}"))

    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
