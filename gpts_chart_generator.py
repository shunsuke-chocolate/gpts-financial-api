# gpts_chart_generator.py (GPTs対応・フォント明示指定版)
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter
import urllib.request
import os

# ✅ フォント準備関数
FONT_URL = "https://raw.githubusercontent.com/shunsuke-chocolate/gpts-financial-api/main/NotoSerifJP-Regular.ttf"
FONT_PATH = "/tmp/NotoSerifJP-Regular.ttf"

def get_font():
    if not os.path.exists(FONT_PATH):
        urllib.request.urlretrieve(FONT_URL, FONT_PATH)
    return FontProperties(fname=FONT_PATH)

# ✅ 金額フォーマット
formatter = FuncFormatter(lambda x, _: f"{int(x):,}")

# ✅ 貸借対照表グラフ作成

def plot_balance_sheet_chart(bs_assets, bs_liabilities_equity, title, output_path):
    fp = get_font()
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar("資産", bs_assets[0], label="流動資産", color="#4C72B0")
    ax.bar("資産", bs_assets[1], bottom=bs_assets[0], label="固定資産", color="#55A868")

    ax.bar("負債・純資産", bs_liabilities_equity[0], label="流動負債", color="#C44E52")
    ax.bar("負債・純資産", bs_liabilities_equity[1], bottom=bs_liabilities_equity[0], label="固定負債", color="#8172B2")
    bottom_total = bs_liabilities_equity[0] + bs_liabilities_equity[1]
    ax.bar("負債・純資産", bs_liabilities_equity[2], bottom=bottom_total, label="純資産", color="#64B5CD")

    ax.set_title(title, fontproperties=fp, fontsize=14)
    ax.set_ylabel("金額（百万円）", fontproperties=fp)
    ax.legend(prop=fp)
    ax.yaxis.set_major_formatter(formatter)
    ax.set_xticklabels(["資産", "負債・純資産"], fontproperties=fp)
    plt.yticks(fontproperties=fp)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# ✅ 損益計算書 滝チャート作成

def plot_profit_waterfall_chart(pl_data: dict, title, output_path):
    fp = get_font()
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
        ax.text(i, bottom + val / 2, f"{val:,.0f}", ha='center', va='center', fontproperties=fp, fontsize=10)

    ax.set_title(title, fontproperties=fp, fontsize=14)
    ax.set_ylabel("金額（百万円）", fontproperties=fp)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontproperties=fp, rotation=45)
    ax.yaxis.set_major_formatter(formatter)
    plt.yticks(fontproperties=fp)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# ✅ キャッシュフロー 滝チャート作成

def plot_cashflow_waterfall_chart(cf_data: dict, title, output_path):
    fp = get_font()
    labels = list(cf_data.keys())
    values = list(cf_data.values())

    cumulative = [values[0]]
    for v in values[1:-1]:
        cumulative.append(cumulative[-1] + v)
    cumulative = cumulative[:-1]

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (label, val, bottom) in enumerate(zip(labels[1:], values[1:-1], cumulative)):
        ax.bar(label, val, bottom=bottom, color='blue' if val >= 0 else 'orange')
        ax.text(i+1, bottom + val / 2, f"{val:,.0f}", ha='center', va='center', fontproperties=fp)

    ax.bar(labels[0], values[0], color='gray')
    ax.text(0, values[0]/2, f"{values[0]:,.0f}", ha='center', va='center', fontproperties=fp)

    ax.bar(labels[-1], values[-1], color='gray')
    ax.text(len(labels)-1, values[-1]/2, f"{values[-1]:,.0f}", ha='center', va='center', fontproperties=fp)

    ax.set_title(title, fontproperties=fp)
    ax.set_ylabel("金額（百万円）", fontproperties=fp)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontproperties=fp)
    ax.yaxis.set_major_formatter(formatter)
    plt.yticks(fontproperties=fp)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
