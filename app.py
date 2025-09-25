import streamlit as st
import jellyfish
import unicodedata

# Normalize text to NFKC
def normalize_text(text):
    return unicodedata.normalize('NFKC', text)

# Calculate Jaro-Winkler similarity
def calculate_similarity(text1, text2):
    normalized_text1 = normalize_text(text1)
    normalized_text2 = normalize_text(text2)
    return jellyfish.jaro_winkler_similarity(normalized_text1, normalized_text2)

# Main app
st.title("テキスト類似度計算アプリ")

text1 = st.text_area("テキスト1", "ここに1つ目のテキストを入力してください。")
text2 = st.text_area("テキスト2", "ここに2つ目のテキストを入力してください。")

if st.button("類似度を計算"):
    if text1 and text2:
        similarity = calculate_similarity(text1, text2)
        st.session_state.similarity = similarity
        st.session_state.text1 = text1
        st.session_state.text2 = text2
        st.write(f"テキスト間の類似度: {similarity:.4f}")
        st.progress(similarity)
    else:
        st.warning("両方のテキストエリアにテキストを入力してください。")