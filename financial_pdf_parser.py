import fitz
import re
from typing import Dict

def extract_structured_financial_data(pdf_path: str) -> Dict:
    """PDFから構造化データを抽出（強化版）"""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    
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
    
    # データ構造化
    return {
        "balance_sheet": {
            "資産": {
                "流動資産": result.get("流動資産合計", 0),
                "固定資産": result.get("固定資産合計", 0)
            },
            "負債・純資産": {
                "流動負債": result.get("流動負債合計", 0),
                "固定負債": result.get("固定負債合計", 0),
                "純資産": result.get("純資産合計", 0)
            }
        },
        "profit_statement": {
            "営業利益": result.get("営業利益", 0),
            "当期純利益": result.get("当期純利益", 0)
        }
    }
