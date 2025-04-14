import matplotlib.pyplot as plt
import pandas as pd
import os
from typing import Dict, List
from matplotlib import font_manager as fm

def validate_font(font_path: str) -> str:
    """フォントパスの検証とフォールバック処理"""
    if os.path.isfile(font_path):
        return font_path
    default_path = "./NotoSerifJP-Regular.ttf"
    if os.path.isfile(default_path):
        return default_path
    raise FileNotFoundError(f"フォントファイルが見つかりません: {font_path}")

def plot_bs_vertical_grouped_stacked(
    bs_data: Dict[str, Dict[str, float]],
    years: List[str],
    font_path: str = "./NotoSerifJP-Regular.ttf",
    title: str = ""
) -> str:
    """貸借対照表グラフ生成（検証済み）"""
    # データ検証
    required_sections = ["資産", "負債・純資産"]
    for section in required_sections:
        if section not in bs_data:
            raise ValueError(f"必須セクション不足: {section}")

    # フォント設定
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

# 他のグラフ関数も同様に強化
