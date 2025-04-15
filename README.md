# 📊 GPTs向け財務三表グラフ生成モジュール - gpts-financial-api

このリポジトリは、ChatGPTのカスタムGPT（GPTs）環境でPDFから抽出した財務データをもとにグラフを生成するための専用Pythonモジュールを提供します。

---

## ✅ ファイル構成（GPTs専用構成）

```
gpts-financial-api/
├── gpts_chart_generator.py   # 📈 財務グラフ描画関数（フォント処理含む）
├── sample_data/              # ✅ 任意：テスト用データ（BS/PL/CF）
├── fonts/                    # 任意：Notoフォントのバックアップ（DL不要）
├── README.md                 # このファイル
```

---

## 🧠 GPTsでの使い方

### ステップ1：ファイルをGPTsにアップロード

1. ChatGPTの `My GPTs` にアクセス → [https://chat.openai.com/gpts](https://chat.openai.com/gpts)
2. 編集画面で `Files` を開き、`gpts_chart_generator.py` をアップロード

---

### ステップ2：Instructionsに以下の内容を記述

#### ✅ 日本語版（そのままコピーOK）

```
ユーザーがPDFから抽出した財務数値（貸借対照表・損益計算書・キャッシュフロー）を入力したら、Python関数を使って対応するグラフを生成してください。
アップロードされた `gpts_chart_generator.py` に定義されている関数：

- `plot_balance_sheet_chart(...)` は貸借対照表のグラフを描画します
- `plot_profit_waterfall_chart(...)` は損益計算書の滝チャートを描画します
- `plot_cashflow_waterfall_chart(...)` はキャッシュフロー滝チャートを描画します

それぞれのグラフは `/tmp/output.png` に保存して返してください。出力画像はそのままユーザーに表示してください。
```

#### ✅ English version (for global use)
```
When the user provides financial data (balance sheet, income statement, or cash flow) extracted from a PDF, use the appropriate Python function from the uploaded `gpts_chart_generator.py` to generate the corresponding chart.

Functions included:
- `plot_balance_sheet_chart(...)`: generates balance sheet stacked bar chart
- `plot_profit_waterfall_chart(...)`: generates waterfall chart for profit and loss
- `plot_cashflow_waterfall_chart(...)`: generates waterfall chart for cash flow

Save the chart to `/tmp/output.png` and return the image as part of your response.
```

---

## ✅ 各関数の使い方（内部処理例）

```python
plot_balance_sheet_chart(
    [280890, 299094],
    [236616, 88882, 254486],
    "ウエルシア 2025年2月期 貸借対照表",
    "/tmp/bs_chart.png"
)

plot_profit_waterfall_chart(
    {
        "売上高": 1285005,
        "売上原価": -894648,
        "販管費": -353947,
        "営業外収益": 6134,
        "営業外費用": -1706,
        "特別利益": 154,
        "特別損失": -14714,
        "法人税等合計": -11938,
        "当期純利益": 14338
    },
    "損益計算書 滝チャート",
    "/tmp/pl_chart.png"
)

plot_cashflow_waterfall_chart(
    {
        "期首残高": 30065,
        "営業CF": 47845,
        "投資CF": -22736,
        "財務CF": -20774,
        "期末残高": 34404
    },
    "キャッシュフロー計算書 滝チャート",
    "/tmp/cf_chart.png"
)
```

---

## 🔤 フォントについて

- 日本語フォント `NotoSerifJP-Regular.ttf` を自動で `/tmp` にDLして適用（再アップロード不要）
- `FontProperties` による直接指定により、環境に依存せず日本語が確実に表示されます

---

## 📌 備考

- `japanize_matplotlib` は不要です（フォント直接指定方式）
- GPTsは毎回環境がリセットされるため、フォントは都度DLされます（自動処理）

---

## 📮 ライセンス

このプロジェクトは MIT ライセンスで公開されています。

---

## ✉ お問い合わせ

本リポジトリに関する質問・改良提案などがあれば issue または pull request にてご連絡ください。

