import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot_profit_waterfall_chart(title, revenue, cogs, sg_and_a, op_income,
                                non_op_income, non_op_expenses, ordinary_income,
                                special_gains, special_losses, pre_tax_income,
                                income_taxes, net_income, output_path):

    items = [
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

    cum_values = [0]
    for i in range(1, len(values)):
        cum_values.append(cum_values[-1] + values[i - 1])

    colors = ['#4caf50' if v >= 0 else '#f44336' for v in values]

    fig, ax = plt.subplots(figsize=(12, 6))
    for i, (label, val, base) in enumerate(zip(items, values, cum_values)):
        ax.bar(label, val, bottom=base, color=colors[i])
        y = base + val if val > 0 else base
        ax.text(i, y, f"{val:,}", ha='center', va='bottom' if val > 0 else 'top', fontsize=10)

    ax.set_title(title, fontsize=16)
    ax.axhline(0, color='black', linewidth=0.8)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
