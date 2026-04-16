import streamlit as st
import pandas as pd

# データの読み込み
df = pd.read_csv('nihonshi.csv')

st.title("日本史一問一答")
st.write("漢字で正確に入力してください。ひらがなは不正解になります")

# セッション状態の初期化
if 'index' not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.questions = df.sample(frac=1).reset_index(drop=True)

# クイズが残っている場合
if st.session_state.index < len(st.session_state.questions):
    row = st.session_state.questions.iloc[st.session_state.index]
    
    st.subheader(f"第 {st.session_state.index + 1} 問 / 全 {len(st.session_state.questions)} 問")
    # CSVの3列目に時代があれば表示（なければ飛ばす）
    if len(row) >= 3:
        st.info(f"時代：{row.iloc[2]}")
    
    st.write(f"### 問題：{row.iloc[0]}")

    with st.form(key='quiz_form', clear_on_submit=True):
        user_input = st.text_input("答えを入力してください")
        submit_button = st.form_submit_button(label='解答する')

    if submit_button:
        correct_answer = str(row.iloc[1]).strip()
        if user_input.strip() == correct_answer:
            st.success("✨ 正解！！")
            st.session_state.score += 1
        else:
            st.error(f"❌ ぶー！ 正解は「{correct_answer}」でした。")
        
        st.session_state.index += 1
        st.button("次の問題へ")

# 全問終了時
else:
    st.balloons()
    st.write(f"## 全問終了！正解数は {st.session_state.score} / {len(st.session_state.questions)} です。")
    if st.button("最初からやり直す"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.rerun()
