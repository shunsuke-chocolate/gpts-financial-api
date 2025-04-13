
import matplotlib.pyplot as plt
import os

def plot_profit_step(df_middle, font_path):
    fig, ax = plt.subplots()
    labels = list(df_middle.keys())
    values = [v['当期'] for v in df_middle.values()]
    ax.bar(labels, values)
    output_path = "/mnt/data/profit_step.png"
    plt.title("利益ステップ")
    plt.savefig(output_path)
    plt.close()
    return output_path

def plot_bs_vertical_grouped_stacked(bs_data, font_path, years, title):
    fig, ax = plt.subplots()
    categories = list(bs_data.keys())
    for i, cat in enumerate(categories):
        vals = bs_data[cat]
        ax.bar(years, vals, label=cat)
    output_path = "/mnt/data/bs_stacked.png"
    plt.title(title)
    plt.legend()
    plt.savefig(output_path)
    plt.close()
    return output_path

def plot_cf_waterfall(cf_values, font_path, title):
    fig, ax = plt.subplots()
    labels = [d["label"] for d in cf_values]
    amounts = [d["amount"] for d in cf_values]
    ax.bar(labels, amounts)
    output_path = "/mnt/data/cf_waterfall.png"
    plt.title(title)
    plt.savefig(output_path)
    plt.close()
    return output_path
