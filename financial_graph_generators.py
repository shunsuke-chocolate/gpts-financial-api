
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 出力先ディレクトリの作成
output_dir = "/mnt/data"
os.makedirs(output_dir, exist_ok=True)

# 1. 貸借対照表の縦型積み上げグラフ
def plot_bs_vertical_grouped_stacked_categorized(bs_data, font_path, years, title):
    font_prop = FontProperties(fname=font_path)
    x = np.arange(len(years))
    width = 0.35

    color_scheme_grouped = {
        "資産": {
            "流動資産合計": "#80DEEA",
            "固定資産合計": "#26C6DA"
        },
        "負債・純資産": {
            "流動負債合計": "#FFE082",
            "固定負債合計": "#FFB300",
            "純資産合計": "#FF6F00"
        }
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    bottoms = [0] * len(years)
    for label, color in color_scheme_grouped["資産"].items():
        values = bs_data["資産"].get(label, [0, 0])
        ax.bar(x - width/2, values, width, bottom=bottoms,
               label=f"資産：{label}", color=color, edgecolor="white")
        bottoms = [b + v for b, v in zip(bottoms, values)]

    bottoms = [0] * len(years)
    for label, color in color_scheme_grouped["負債・純資産"].items():
        values = bs_data["負債・純資産"].get(label, [0, 0])
        ax.bar(x + width/2, values, width, bottom=bottoms,
               label=f"負債・純資産：{label}", color=color, edgecolor="white")
        bottoms = [b + v for b, v in zip(bottoms, values)]

    ax.set_title(title, fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontproperties=font_prop)
    ax.legend(prop=font_prop, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    path = os.path.join(output_dir, "bs_vertical_grouped_stacked_categorized.png")
    plt.savefig(path)
    plt.close()
    return path

# 2. 損益ステップグラフ
def plot_profit_step_chart(df_middle, font_path):
    font_prop = FontProperties(fname=font_path)

    利益ステップ = [
        ("売上総利益", df_middle.loc["売上総利益"]["当期"]),
        ("営業利益", df_middle.loc["営業利益"]["当期"]),
        ("経常利益", df_middle.loc["経常利益"]["当期"]),
        ("税引前利益", df_middle.loc["税金等調整前当期純利益"]["当期"]),
        ("当期純利益", df_middle.loc["当期純利益"]["当期"])
    ]

    labels = [x[0] for x in 利益ステップ]
    values = [x[1] for x in 利益ステップ]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(labels, values, color="#4FC3F7", edgecolor="black")

    for i, val in enumerate(values):
        ax.text(i, val + max(values) * 0.01, f"{int(val):,}", ha="center", va="bottom",
                fontproperties=font_prop, fontsize=10)

    ax.set_title("利益ステップ構造：売上総利益から当期純利益まで", fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xticklabels(labels, fontproperties=font_prop)
    plt.tight_layout()
    path = os.path.join(output_dir, "profit_step_only.png")
    plt.savefig(path)
    plt.close()
    return path

# 3. キャッシュフロー ウォーターフォール
def plot_cashflow_waterfall(cf_values, font_path, title):
    font_prop = FontProperties(fname=font_path)
    labels = ["期首残高", "営業CF", "投資CF", "財務CF", "期末残高"]
    values = cf_values

    cumulative = [values[0]]
    for v in values[1:-1]:
        cumulative.append(cumulative[-1] + v)
    cumulative.append(values[-1])  # 期末残高（表示値）

    colors = []
    for i, val in enumerate(values):
        if i == 0 or i == len(values) - 1:
            colors.append("#4FC3F7")
        elif val >= 0:
            colors.append("#81C784")
        else:
            colors.append("#E57373")

    fig, ax = plt.subplots(figsize=(12, 6))
    for i in range(len(values)):
        bottom = cumulative[i - 1] if i != 0 else 0
        height = values[i] if i == 0 else cumulative[i] - bottom
        ax.bar(labels[i], height, bottom=bottom if i != 0 else 0,
               color=colors[i], edgecolor="black")
        ax.text(i, bottom + height / 2, f"{cumulative[i]:,}",
                ha='center', va='center', fontproperties=font_prop, fontsize=10)

    ax.set_title(title, fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    ax.set_xticklabels(labels, fontproperties=font_prop)
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}"))
    plt.tight_layout()
    path = os.path.join(output_dir, "cashflow_waterfall_corrected.png")
    plt.savefig(path)
    plt.close()
    return path
