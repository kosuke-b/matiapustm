import streamlit as st
import google.generativeai as genai

# --- スタイル設定: ネイビー背景、白文字、ピンクアクセント ---
st.markdown("""
<style>
html, body, .stApp {
  background-color: #0d1b2a !important;
  color: #ffffff !important;
}
.stButton>button {
  background-color: #fe5a99 !important;
  color: #ffffff !important;
  border-radius: 8px !important;
  padding: 12px 24px !important;
  font-weight: bold !important;
  border: none !important;
}
.stTextArea textarea {
  background-color: #1f2a44 !important;
  color: #ffffff !important;
  border: 2px solid #fe5a99 !important;
  border-radius: 8px !important;
}
.stRadio > div {
  background-color: #1f2a44 !important;
  color: #ffffff !important;
  border: 2px solid #fe5a99 !important;
  border-radius: 8px !important;
  padding: 8px 12px !important;
}
.stRadio label {
  color: #ffffff !important;
}
h1, h2, h3, label {
  color: #ffffff !important;
}
hr {
  border: 1px solid #fe5a99 !important;
}
</style>
""", unsafe_allow_html=True)

# --- APIキー設定 ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 返信生成関数 ---
def generate_reply_from_profile(profile_text):
    prompt = f"""
マッチングアプリで以下の相手のプロフィールを元に最初に送るメッセージを作成してください。

条件:
・各メッセージは3行以内で絵文字を入れない。
・自然で程よいテンション。
・ネガティブな話題、自分語り、質問攻めを避ける。
・最新トレンドを入れる。
・オープンエンドな質問で締める。

プロフィール:
{profile_text}

返信文:
1:
2:
3:
4:
5:
"""
    response = model.generate_content(prompt)
    return response.text

def generate_reply_from_conversation(conversation_text):
    prompt = f"""
マッチングアプリで以下のやり取りを踏まえて次に送る返信メッセージを作成してください。

条件:
・各メッセージは3行以内で絵文字を入れない。
・自然で程よいテンション。
・ネガティブな話題、自分語り、質問攻めを避ける。
・最新トレンドを入れる。
・共感を示しオープンエンドな質問で締める。

やり取り:
{conversation_text}

返信文:
1:
2:
3:
4:
5:
"""
    response = model.generate_content(prompt)
    return response.text

# --- タイトルと説明 ---
st.markdown("<h1 style='text-align:center;'>マッチングアプリ返信文AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>プロフィールまたはやり取り内容を入力して、サンプル返信文を5パターン生成します。</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- モード選択 ---
mode = st.radio("モードを選択", ("プロフィールから生成", "やり取りから生成"), horizontal=True)

# --- 入力エリア ---
user_input = st.text_area(
    "ここにプロフィール文ややり取りの内容を入力してください", height=200
)

# --- 生成ボタン ---
if st.button("返信文生成"):
    with st.spinner('生成中...'):
        if mode == "プロフィールから生成":
            result = generate_reply_from_profile(user_input)
        else:
            result = generate_reply_from_conversation(user_input)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3>返信文サンプル</h3>", unsafe_allow_html=True)
    st.code(result)
