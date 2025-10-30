# streamlit_lotto_app.py
# Lotto 번호 추천 + 최신 당첨번호 비교 (대한민국 로또 6/45)
# 실행: pip install streamlit requests beautifulsoup4
#       streamlit run streamlit_lotto_app.py

import streamlit as st
import random
import requests
import re
from typing import List, Tuple, Dict

st.set_page_config(page_title="로또 번호 추첨기", layout="centered")

st.title("🇰🇷 로또(6/45) 번호 추첨기 — Streamlit 앱")
st.markdown("원하는 세트 수만큼 1~45 사이의 숫자 6개를 추천해줍니다. 또한 최신 회차 당첨번호와 비교할 수 있습니다.")

# ------------------- 유틸리티 함수 -------------------
