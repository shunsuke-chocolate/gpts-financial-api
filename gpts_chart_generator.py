import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# フォントパス（GPTsにKnowledgeとしてアップロードしたもの）
FONT_PATH = "/mnt/data/NotoSerifJP-Regular.ttf"

def plot_profit_waterfall_chart(
    title: str,
    revenue: int,
    cogs: int,
    sg_and_a: int,
    op_income: int,
    non_op_income: int,
    non_op_expenses: int,
    ordinary_income: int,
    special_gains: int,
    special_losses: int,
    pre_tax_income: int,
    income_taxes: int,
    net_income: int,
    output_path: str = "/tmp/output.png"
):
    # 日本語フォントを読み込む
    jp_font = FontProperties(fname=FONT_PATH)

    # ラベルと値の定義
    labels = [
        "売上高", "売上原価", "販管費", "営業利益",
        "営業外収益", "営業外費用", "経常利益",
        "特別利益", "特別損失", "税引前当期純利益",
        "法人税等", "当期純利益"
    ]
    values = [
        revenue, -cogs, -sg_and_a, op_income,
        non_op_income, -non_op_expenses, ordinary_income,
        special_gains, -special_losses, pre_tax_income,
        -income_taxes, net_income
    ]

    # 累積位置を計算
    cum_values = [0]
    for i in range(1, len(values)):
        cum_values.append(cum_values[-1] + values[i - 1])

    # 棒の色（プラスは緑、マイナスは赤）
    colors = ['#4caf50' if v >= 0 else '#f44336' for v in values]

    # グラフ描画
    fig, ax = plt.subplots(figsize=(12, 6))
    for i in range(len(labels)):
        ax.bar(labels[i], values[i], bottom=cum_values[i], color=colors[i])
        ax.text(i, cum_values[i] + values[i] / 2, f"{values[i]:,}", 
                ha='center', va='center', fontproperties=jp_font, fontsize=10)

    # タイトルと装飾
    ax.set_title(title, fontproperties=jp_font, fontsize=14)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.set_ylabel("金額（百万円）", fontproperties=jp_font)
    plt.xticks(rotation=45, fontproperties=jp_font)
    plt.yticks(fontproperties=jp_font)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    # ファイル出力
    plt.savefig(output_path)
    plt.close()
