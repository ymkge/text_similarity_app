# テキスト類似度計算アプリ

## 概要

このアプリケーションは、入力された2つの日本語テキストの類似度を計算し、表示するツールです。
計算結果は、Googleスプレッドシートに保存することも可能です。

類似度の計算には、文字列の形状を比較するJaro-Winkler類似度アルゴリズムを用いており、表記の揺れ（例：「ヴァ」と「バ」）に強い判定が可能です。また、比較前にテキストはNFKC形式で正規化されます。

## 主な技術

- Python
- Streamlit
- Jellyfish
- gspread
- google-auth-oauthlib
- pandas

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

### 3. Google Cloud Platformの認証情報設定

このアプリはGoogleスプレッドシートに計算結果を保存するため、Google Cloud Platformのサービスアカウント認証情報が必要です。

1.  Google Cloudコンソールでサービスアカウントを作成し、キー（JSONファイル）をダウンロードします。
2.  `.streamlit/secrets.toml.sample` をコピーして、`.streamlit/secrets.toml` ファイルを作成し、以下の内容を記述します。

    ```toml
    # .streamlit/secrets.toml

    # Google Cloud Platform service account credentials
    [gcp_service_account]
    type = "service_account"
    project_id = "your_project_id"
    private_key_id = "your_private_key_id"
    private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
    client_email = "your_client_email"
    client_id = "your_client_id"
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
    client_x509_cert_url = "your_client_x509_cert_url"

    # Google Spreadsheet ID
    spreadsheet_id = "your_spreadsheet_id"
    ```

    - `[gcp_service_account]`セクションには、ダウンロードしたサービスアカウントのJSONファイルの内容をコピーしてください。**特に`private_key`は改行を`
`に置き換える必要があります。**
    - `spreadsheet_id`には、保存先となるGoogleスプレッドシートのIDを指定してください。

### 4. アプリケーションの起動

```bash
streamlit run app.py
```

ブラウザで表示されたURLにアクセスし、アプリを使用します。

## 使い方

1.  2つのテキストエリアに比較したい文字列を入力します。
2.  「類似度を計算」ボタンをクリックすると、類似度が0から1の範囲で表示されます。
3.  「Googleスプレッドシートに保存」ボタンをクリックすると、入力した2つのテキストと計算された類似度が、指定したスプレッドシートの新しい行に追記されます。