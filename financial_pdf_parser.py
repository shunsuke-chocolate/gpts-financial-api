import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_structured_financial_data(text):
    # これはシンプルなキーワードマッチング例です。必要に応じて正規表現や形態素解析へ切替可。
    keywords = {
        "固定資産合計": None,
        "流動資産合計": None,
        "固定負債合計": None,
        "流動負債合計": None,
        "純資産合計": None,
        "営業活動によるキャッシュ・フロー": None,
        "投資活動によるキャッシュ・フロー": None,
        "財務活動によるキャッシュ・フロー": None,
        "現金及び現金同等物の期首残高": None,
        "現金及び現金同等物の期末残高": None,
    }
    for line in text.splitlines():
        for key in keywords:
            if key in line:
                num = "".join(filter(str.isdigit, line.replace(",", "")))
                if num:
                    keywords[key] = int(num)
    return keywords
