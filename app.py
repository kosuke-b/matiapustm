import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

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

st.title("マッチングアプリ返信文生成AIツール")

mode = st.radio("モードを選択", ("プロフィールから生成", "やり取りから生成"))

user_input = st.text_area("ここにプロフィールまたはやり取りを入力してください:", height=150)

if st.button("返信文生成"):
    if mode == "プロフィールから生成":
        replies = generate_reply_from_profile(user_input)
    else:
        replies = generate_reply_from_conversation(user_input)

    st.subheader("返信文サンプル")
    st.write(replies)
