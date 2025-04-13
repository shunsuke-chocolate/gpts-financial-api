
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_profit_step_only(df_middle, font_path):
    df = pd.DataFrame(df_middle)
    fig, ax = plt.subplots(figsize=(8, 5))
    values = list(df["当期"])
    labels = df.index.tolist()
    ax.bar(labels, values)
    if os.path.exists(font_path):
        plt.rcParams["font.family"] = font_path
    image_path = "/mnt/data/profit_step_only.png"
    plt.savefig(image_path)
    plt.close()
    return image_path

def plot_cf_waterfall_labeled(cf_values, font_path, title):
    labels = [item["label"] for item in cf_values]
    values = [item["amount"] for item in cf_values]
    fig, ax = plt.subplots(figsize=(10, 6))
    cum_values = [0]
    for v in values[:-1]:
        cum_values.append(cum_values[-1] + v)
    for i in range(len(values)):
        ax.bar(labels[i], values[i], bottom=cum_values[i] if i > 0 else 0)
    if os.path.exists(font_path):
        plt.rcParams["font.family"] = font_path
    ax.set_title(title)
    image_path = "/mnt/data/cf_waterfall_labeled.png"
    plt.savefig(image_path)
    plt.close()
    return image_path

def plot_bs_vertical_grouped_stacked(bs_data, font_path, years, title):
    df = pd.DataFrame(bs_data)
    fig, ax = plt.subplots(figsize=(10, 6))
    df.T.plot(kind="bar", stacked=True, ax=ax)
    if os.path.exists(font_path):
        plt.rcParams["font.family"] = font_path
    ax.set_title(title)
    image_path = "/mnt/data/bs_vertical_grouped_stacked.png"
    plt.savefig(image_path)
    plt.close()
    return image_path
