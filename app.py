import streamlit as st
import google.generativeai as genai

# --- カスタムCSSでネイビー×ピンクのスタイル ---
st.markdown("""
    <style>
    body {
        background-color: #0e1a2b;
    }
    .main {
        background-color: #172445;
        color: #f4f6fa;
    }
    .st-bx, .st-c6, .st-c8 {
        background: #172445 !important;
    }
    .stButton>button {
        background-color: #fe5a99;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        padding: 0.5em 2em;
    }
    .st-bb, .stTextArea textarea {
        background-color: #1c2940 !important;
        color: #f4f6fa !important;
    }
    .stRadio > div { 
        background: #243056;
        color: #f4f6fa;
        border-radius: 8px;
        padding: 8px 0 8px 8px;
    }
    .st-dx {
        color: #fe5a99 !important;
    }
    .explanation {
        background: rgba(254,90,153,0.09);
        border-left: 5px solid #fe5a99;
        padding: 18px 20px 16px 20px;
        margin-bottom: 20px;
        border-radius: 10px;
        color: #f4f6fa;
    }
    </style>
""", unsafe_allow_html=True)

# --- API設定 ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- ユーザーガイド ---
st.markdown("""
<div class='explanation'>
<b style="font-size:1.2em;color:#fe5a99;">▶️ 使い方ガイド</b><br>
1. <b>モード</b>を選択（プロフィール or やり取り）<br>
2. <b>テキストボックス</b>にプロフィール文ややり取りの内容を貼り付け<br>
3. <b style="color:#fe5a99;">「返信文生成」</b>ボタンをクリック！<br>
<br>
<b>✔️ コツ</b>：内容はなるべく詳細に、趣味・仕事・最近の話題なども書くとAIが自然な返信例を提案してくれます。
</div>
""", unsafe_allow_html=True)

# --- タイトル ---
st.markdown(
    "<h1 style='color:#fe5a99;font-weight:800;font-size:2.3em;letter-spacing:2px;'>マッチングアプリ返信文AI</h1>", 
    unsafe_allow_html=True
)

# --- モード選択 ---
mode = st.radio(
    "モードを選択",
    ("プロフィールから生成", "やり取りから生成"),
    horizontal=True,
    index=0
)

# --- 入力エリア ---
user_input = st.text_area(
    "ここにプロフィール文ややり取りの内容を入力してください（例：趣味、仕事、最近ハマってるもの など）", 
    height=150,
    key="input_area"
)

# --- ボタン＆結果 ---
col1, col2, col3 = st.columns([2,1,2])
with col2:
    submit = st.button("返信文生成", use_container_width=True)

if submit:
    with st.spinner("AIが返信文を作成中..."):
        if mode == "プロフィールから生成":
            replies = generate_reply_from_profile(user_input)
        else:
            replies = generate_reply_from_conversation(user_input)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#fe5a99;'>返信文サンプル</h3>", unsafe_allow_html=True)
    st.code(replies, language="markdown")
