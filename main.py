{\rtf1\ansi\ansicpg932\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import streamlit as st\
import pandas as pd\
\
# 1. \uc0\u12487 \u12540 \u12479 \u12398 \u35501 \u12415 \u36796 \u12415 \
# \uc0\u21516 \u12376 \u12522 \u12509 \u12472 \u12488 \u12522 \u20869 \u12395 \u32622 \u12356 \u12383 CSV\u12501 \u12449 \u12452 \u12523 \u21517 \u12434 \u25351 \u23450 \u12375 \u12414 \u12377 \
df = pd.read_csv('nihonshi.csv')\
\
st.title("\uc0\u55356 \u57144  \u26085 \u26412 \u21490 \u19968 \u21839 \u19968 \u31572 \u12473 \u12497 \u12523 \u12479 \u22654 ")\
st.write("\uc0\u28450 \u23383 \u12391 \u27491 \u30906 \u12395 \u20837 \u21147 \u12375 \u12390 \u12367 \u12384 \u12373 \u12356 \u12290 \u12402 \u12425 \u12364 \u12394 \u12399 \u19981 \u27491 \u35299 \u12391 \u12377 \u65281 ")\
\
# \uc0\u12475 \u12483 \u12471 \u12519 \u12531 \u29366 \u24907 \u65288 \u12463 \u12452 \u12474 \u12398 \u36914 \u34892 \u29366 \u27841 \u65289 \u12434 \u20445 \u23384 \u12377 \u12427 \u20181 \u32068 \u12415 \
if 'index' not in st.session_state:\
    st.session_state.index = 0\
    st.session_state.score = 0\
    # \uc0\u26368 \u21021 \u12395 \u21839 \u38988 \u12434 \u12471 \u12515 \u12483 \u12501 \u12523 \
    st.session_state.questions = df.sample(frac=1).reset_index(drop=True)\
\
# \uc0\u12463 \u12452 \u12474 \u12364 \u12414 \u12384 \u27531 \u12387 \u12390 \u12356 \u12427 \u22580 \u21512 \
if st.session_state.index < len(st.session_state.questions):\
    row = st.session_state.questions.iloc[st.session_state.index]\
    \
    st.subheader(f"\uc0\u31532  \{st.session_state.index + 1\} \u21839 ")\
    st.info(f"\uc0\u26178 \u20195 \u65306 \{row.iloc[2]\}")\
    st.write(f"### \uc0\u21839 \u38988 \u65306 \{row.iloc[0]\}")\
\
    # \uc0\u20837 \u21147 \u12501 \u12457 \u12540 \u12512 \
    with st.form(key='quiz_form', clear_on_submit=True):\
        user_input = st.text_input("\uc0\u31572 \u12360 \u12434 \u28450 \u23383 \u12391 \u20837 \u21147 ")\
        submit_button = st.form_submit_button(label='\uc0\u22238 \u31572 \u12377 \u12427 ')\
\
    if submit_button:\
        correct_answer = str(row.iloc[1]).strip()\
        if user_input.strip() == correct_answer:\
            st.success("\uc0\u10024  \u27491 \u35299 \u65281 \u65281 ")\
            st.session_state.score += 1\
        else:\
            st.error(f"\uc0\u10060  \u19981 \u27491 \u35299 \u65281  \u27491 \u35299 \u12399 \u12300 \{correct_answer\}\u12301 \u12391 \u12375 \u12383 \u12290 ")\
        \
        st.session_state.index += 1\
        st.button("\uc0\u27425 \u12398 \u21839 \u38988 \u12408 ")\
\
# \uc0\u20840 \u21839 \u32066 \u20102 \u26178 \
else:\
    st.balloons()\
    st.write(f"## \uc0\u20840 \u21839 \u32066 \u20102 \u65281 \u12354 \u12394 \u12383 \u12398 \u27491 \u35299 \u25968 \u12399  \{st.session_state.score\} / \{len(st.session_state.questions)\} \u12391 \u12375 \u12383 \u12290 ")\
    if st.button("\uc0\u26368 \u21021 \u12363 \u12425 \u12420 \u12426 \u30452 \u12377 "):\
        st.session_state.index = 0\
        st.session_state.score = 0\
        st.rerun()}
