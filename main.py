import streamlit as st
import pandas as pd
import json

# タイトルの設定
st.title('CSV to JSON Converter')

# ファイルアップロードのウィジェット
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # CSVファイルを読み込む
    df = pd.read_csv(uploaded_file)

    # DataFrameをJSONに変換
    json_str = df.to_json(orient='records', lines=False, force_ascii=False)

    # JSONを整形して表示
    parsed_json = json.loads(json_str)
    pretty_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
    
    # 結果の表示
    st.text_area("Converted JSON", pretty_json, height=300)

    # JSONファイルとしてダウンロード可能にする
    st.download_button(label="Download JSON",
                       data=pretty_json,
                       file_name="converted.json",
                       mime="application/json")
