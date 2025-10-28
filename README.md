# テキスト類似度計算アプリ
<img width="766" height="518" alt="スクリーンショット 2025-09-25 19 13 27" src="https://github.com/user-attachments/assets/28de1ed5-f186-4dd5-9eb1-53cb7e188a03" />

## 概要

このアプリケーションは、入力された2つの日本語テキストの類似度を計算し、表示するツールです。

類似度の計算には、文字列の形状を比較するJaro-Winkler類似度アルゴリズムを用いており、表記の揺れ（例：「ヴァ」と「バ」）に強い判定が可能です。また、比較前にテキストはNFKC形式で正規化されます。

## 主な技術

- Python
- Streamlit
- Jellyfish

## セットアップと実行方法

### 1. リポジリのクローン

```bash
git clone <repository_url>
cd text_similarity_app
```

### 2. 必要なライブラリのインストール

```bash
pip install -r requirements.txt
```

### 3. アプリケーションの起動

```bash
streamlit run app.py
```

ブラウザで表示されたURLにアクセスし、アプリを使用します。

## 使い方

1.  2つのテキストエリアに比較したい文字列を入力します。
2.  「類似度を計算」ボタンをクリックすると、類似度が0から1の範囲で表示されます。

## 処理フロー

```mermaid
graph TD
    A[開始] --> B[テキスト1とテキスト2を入力];
    B --> C{「類似度を計算」ボタンをクリック};
    C --> D{テキストが両方入力されているか？};
    D -- No --> E[警告メッセージを表示];
    D -- Yes --> F[テキストをNFKC形式で正規化];
    F --> G[Jaro-Winkler類似度を計算];
    G --> H[類似度スコアとプログレスバーを表示];
    H --> I[終了];
    E --> I;
```