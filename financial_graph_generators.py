import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib import font_manager as fm

def validate_font(font_path: str) -> str:
    """フォントパスの検証とフォールバック処理"""
    font_paths = [
        font_path,
        "./NotoSerifJP-Regular.ttf",
        "/usr/share/fonts/opentype/noto/NotoSerifJP-Regular.otf",
        "/System/Library/Fonts/Supplemental/NotoSerifJP-Regular.otf"
    ]
    
    for fp in font_paths:
        if os.path.isfile(fp):
            return fp
    raise FileNotFoundError(f"有効なフォントファイルが見つかりません: {font_paths}")

def plot_bs_vertical_grouped_stacked(
    bs_data: Dict[str, Dict[str, float]],
    years: List[str],
    font_path: str = "./NotoSerifJP-Regular.ttf",
    title: str = ""
) -> str:
    # フォント検証
    valid_font = validate_font(font_path)
    font_prop = fm.FontProperties(fname=valid_font)
    
    # データ加工
    df_assets = pd.DataFrame(bs_data["資産"], index=years)
    df_liabilities = pd.DataFrame(bs_data["負債・純資産"], index=years)
    
    # 可視化
    fig, ax = plt.subplots(figsize=(12, 7))
    df_assets.plot(kind='bar', stacked=True, ax=ax, position=0, width=0.4)
    df_liabilities.plot(kind='bar', stacked=True, ax=ax, position=1, width=0.4)
    
    # 書式設定
    ax.set_title(title, fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    plt.xticks(rotation=0, fontproperties=font_prop)
    plt.legend(prop=font_prop)
    
    # 出力
    output_path = "bs_vertical_grouped_stacked.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    return output_path

def plot_profit_step_only(
    df_middle: Dict[str, Dict[str, float]],
    font_path: str = "./NotoSerifJP-Regular.ttf"
) -> str:
    # フォント検証
    valid_font = validate_font(font_path)
    font_prop = fm.FontProperties(fname=valid_font)
    
    # データ加工
    values = [df_middle[k]["当期"] for k in df_middle]
    labels = list(df_middle.keys())
    
    # 可視化
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, values)
    
    # 書式設定
    ax.set_title("利益ステップグラフ", fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.tight_layout()
    
    # 出力
    output_path = "profit_step_only.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    return output_path

def plot_cf_waterfall_labeled(
    cf_values: List[Dict[str, float]],
    font_path: str = "./NotoSerifJP-Regular.ttf",
    title: str = ""
) -> str:
    # フォント検証
    valid_font = validate_font(font_path)
    font_prop = fm.FontProperties(fname=valid_font)
    
    # データ加工
    labels = [item["label"] for item in cf_values]
    amounts = [item["amount"] for item in cf_values]
    
    # 可視化
    fig, ax = plt.subplots(figsize=(12, 7))
    cumulative = 0
    for i, (label, amount) in enumerate(zip(labels, amounts)):
        color = "green" if amount >= 0 else "red"
        ax.bar(label, amount, bottom=cumulative, color=color)
        cumulative += amount
    
    # 書式設定
    ax.set_title(title, fontproperties=font_prop)
    ax.set_ylabel("金額（百万円）", fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.tight_layout()
    
    # 出力
    output_path = "cf_waterfall_labeled.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    return output_path
