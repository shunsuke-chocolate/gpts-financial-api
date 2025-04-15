import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import urllib.request

def ensure_font(font_path):
    if not os.path.exists(font_path):
        FONT_URL = "https://raw.githubusercontent.com/shunsuke-chocolate/gpts-financial-api/main/NotoSerifJP-Regular.ttf"
        urllib.request.urlretrieve(FONT_URL, font_path)


def generate_balance_sheet_graph(font_path, output_path):
    ensure_font(font_path)
    fp = FontProperties(fname=font_path)
    
    categories = ["流動資産", "固定資産", "流動負債", "固定負債", "純資産"]
    values = [500000, 300000, 200000, 100000, 500000]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(["資産合計"]*2 + ["負債・純資産"]*3, values, color=["skyblue", "skyblue", "salmon", "salmon", "lightgreen"])
    ax.set_title("貸借対照表（百万円）", fontproperties=fp)
    ax.set_ylabel("金額", fontproperties=fp)
    ax.set_xticklabels(categories, fontproperties=fp, rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def generate_profit_waterfall_chart(font_path, output_path):
    ensure_font(font_path)
    fp = FontProperties(fname=font_path)

    raw_values = {
        "売上高": 1285005,
        "売上原価": -894648,
        "販管費": -353947,
        "営業外収益": 6134,
        "営業外費用": -1706,
        "特別利益": 154,
        "特別損失": -14714,
        "法人税等合計": -11938,
        "当期純利益": 34140,
    }

    fig, ax = plt.subplots(figsize=(12, 6))
    categories = list(raw_values.keys())
    values = list(raw_values.values())

    cumulative = [0]
    for v in values[:-1]:
        cumulative.append(cumulative[-1] + v)
    cumulative = cumulative[:-1]

    colors = ['green' if val >= 0 else 'red' for val in values]
    for i, (label, val, bottom) in enumerate(zip(categories, values, cumulative)):
        ax.bar(label, val, bottom=bottom, color=colors[i])
        ax.text(i, bottom + val / 2, f"{val:,.0f}", ha='center', va='center', fontproperties=fp, fontsize=10)

    ax.set_title("2025年2月期 ウエルシア 損益計算書 滝チャート（百万円）", fontproperties=fp, fontsize=14)
    ax.set_ylabel("金額", fontproperties=fp)
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, fontproperties=fp, rotation=45)
    ax.tick_params(axis='y', labelsize=10)
    plt.yticks(fontproperties=fp)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def generate_cashflow_waterfall_chart(font_path, output_path):
    ensure_font(font_path)
    fp = FontProperties(fname=font_path)

    labels = ["期首残高", "営業CF", "投資CF", "財務CF", "期末残高"]
    values = [100000, 50000, -20000, -15000, 115000]

    cumulative = [values[0]]
    for v in values[1:-1]:
        cumulative.append(cumulative[-1] + v)
    cumulative = cumulative[:-1]

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (label, val, bottom) in enumerate(zip(labels[1:], values[1:-1], cumulative)):
        ax.bar(label, val, bottom=bottom, color='blue' if val >= 0 else 'orange')
        ax.text(i+1, bottom + val/2, f"{val:,.0f}", ha='center', va='center', fontproperties=fp)

    ax.bar(labels[0], values[0], color='gray')
    ax.text(0, values[0]/2, f"{values[0]:,.0f}", ha='center', va='center', fontproperties=fp)

    ax.bar(labels[-1], values[-1], color='gray')
    ax.text(len(labels)-1, values[-1]/2, f"{values[-1]:,.0f}", ha='center', va='center', fontproperties=fp)

    ax.set_title("キャッシュフロー滝チャート（百万円）", fontproperties=fp)
    ax.set_ylabel("金額", fontproperties=fp)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontproperties=fp)
    plt.yticks(fontproperties=fp)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
