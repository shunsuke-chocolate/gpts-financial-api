import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def generate_balance_sheet_graph(font_path, output_path):
    fp = FontProperties(fname=font_path)
    assets = {"流動資産": 280890, "固定資産": 299094}
    liabilities = {"流動負債": 236616, "固定負債": 88882, "純資産": 254486}

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar("資産", assets["流動資産"], label="流動資産")
    ax.bar("資産", assets["固定資産"], bottom=assets["流動資産"], label="固定資産")

    ax.bar("負債・純資産", liabilities["流動負債"], label="流動負債")
    bottom = liabilities["流動負債"]
    ax.bar("負債・純資産", liabilities["固定負債"], bottom=bottom, label="固定負債")
    bottom += liabilities["固定負債"]
    ax.bar("負債・純資産", liabilities["純資産"], bottom=bottom, label="純資産")

    ax.set_title("貸借対照表", fontproperties=fp)
    ax.set_ylabel("金額（百万円）", fontproperties=fp)
    ax.legend(prop=fp)
    plt.xticks(fontproperties=fp)
    plt.yticks(fontproperties=fp)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def generate_profit_step_chart(font_path, output_path):
    fp = FontProperties(fname=font_path)
    steps = {
        "売上総利益": 5000,
        "営業利益": 3000,
        "経常利益": 2000,
        "税引前当期純利益": 1500,
        "当期純利益": 1000
    }

    fig, ax = plt.subplots(figsize=(8, 6))
    x = list(steps.keys())
    y = [steps[x[0]]]
    for i in range(1, len(x)):
        y.append(steps[x[i]] - steps[x[i-1]])
    cumulative = [steps[x[0]]]
    for i in range(1, len(y)):
        cumulative.append(cumulative[i-1] + y[i])

    colors = ["green" if val >= 0 else "red" for val in y]
    base = [0] + cumulative[:-1]
    ax.bar(x, y, bottom=base, color=colors)
    ax.set_title("損益計算書 ステップチャート", fontproperties=fp)
    ax.set_ylabel("金額（百万円）", fontproperties=fp)
    plt.xticks(fontproperties=fp, rotation=45)
    plt.yticks(fontproperties=fp)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def generate_cashflow_waterfall_chart(font_path, output_path):
    fp = FontProperties(fname=font_path)
    flows = {
        "期首残高": 3000,
        "営業CF": 1500,
        "投資CF": -1000,
        "財務CF": -500
    }
    flows["期末残高"] = sum(flows.values())

    fig, ax = plt.subplots(figsize=(8, 6))
    keys = list(flows.keys())
    values = [flows[key] for key in keys]
    base = [0]
    for i in range(1, len(values)):
        base.append(base[i-1] + values[i-1])

    colors = ["gray", "blue", "orange", "green", "gray"]
    ax.bar(keys, values, bottom=base, color=colors)
    ax.set_title("キャッシュフロー計算書", fontproperties=fp)
    ax.set_ylabel("金額（百万円）", fontproperties=fp)
    plt.xticks(fontproperties=fp, rotation=45)
    plt.yticks(fontproperties=fp)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
