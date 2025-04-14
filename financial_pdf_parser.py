import fitz
import re
from typing import Dict

def extract_structured_financial_data(pdf_path: str) -> Dict:
    """PDFから構造化データを抽出（強化版）"""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    
    # 正規表現パターンの最適化
    patterns = {
        "流動資産合計": r"流動資産合計\s*([\d,]+)",
        "固定資産合計": r"固定資産合計\s*([\d,]+)",
        "流動負債合計": r"流動負債合計\s*([\d,]+)",
        "固定負債合計": r"固定負債合計\s*([\d,]+)",
        "純資産合計": r"純資産合計\s*([\d,]+)",
        "営業利益": r"営業利益\s*([\d,]+)",
        "当期純利益": r"当期純利益\s*([\d,]+)"
    }
    
    result = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            value = int(match.group(1).replace(",", ""))
            result[key] = value
        else:
            raise ValueError(f"{key} の値を抽出できませんでした")
    
    return {
        "balance_sheet": {
            "資産": {
                "流動資産": result["流動資産合計"],
                "固定資産": result["固定資産合計"]
            },
            "負債・純資産": {
                "流動負債": result["流動負債合計"],
                "固定負債": result["固定負債合計"],
                "純資産": result["純資産合計"]
            }
        },
        "profit_statement": {
            "営業利益": result["営業利益"],
            "当期純利益": result["当期純利益"]
        }
    }
