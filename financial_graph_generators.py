
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

def plot_profit_step(df_middle, font_path):
    font_prop = FontProperties(fname=font_path)
    labels = list(df_middle.keys())
    values = [df_middle[label]['当期'] for label in labels]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(labels, values)
    ax.set_title("利益ステップ", fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    ax.set_xticklabels(labels, fontproperties=font_prop)
    plt.tight_layout()
    output_path = "/mnt/data/profit_step_only.png"
    plt.savefig(output_path)
    plt.close()
    return output_path

def plot_cf(cf_values, font_path, title):
    font_prop = FontProperties(fname=font_path)
    labels = [item["label"] for item in cf_values]
    values = [item["amount"] for item in cf_values]

    fig, ax = plt.subplots(figsize=(10, 6))
    cumulative = 0
    for i, (label, value) in enumerate(zip(labels, values)):
        ax.bar(label, value, bottom=cumulative if value < 0 else 0)
        cumulative += value

    ax.set_title(title, fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    ax.set_xticklabels(labels, fontproperties=font_prop)
    plt.tight_layout()
    output_path = "/mnt/data/cf_waterfall_labeled.png"
    plt.savefig(output_path)
    plt.close()
    return output_path

def plot_bs_vertical_grouped_stacked(bs_data, font_path, years, title):
    font_prop = FontProperties(fname=font_path)
    fig, ax = plt.subplots(figsize=(10, 6))

    labels = list(bs_data.keys())
    bar_width = 0.35
    index = range(len(labels))

    for i, year in enumerate(years):
        values = [bs_data[label][year] for label in labels]
        ax.bar(
            [x + bar_width * i for x in index],
            values,
            bar_width,
            label=year
        )

    ax.set_xlabel('科目', fontproperties=font_prop)
    ax.set_ylabel('金額（百万円）', fontproperties=font_prop)
    ax.set_title(title, fontproperties=font_prop)
    ax.set_xticks([x + bar_width for x in index])
    ax.set_xticklabels(labels, fontproperties=font_prop)
    ax.legend(prop=font_prop)
    ax.grid(True)

    output_path = "/mnt/data/bs_vertical_grouped_stacked.png"
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return output_path
