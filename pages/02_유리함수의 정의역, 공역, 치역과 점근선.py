import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 사용자 입력
function_str = st.text_input("유리함수의 식을 입력하세요 (예: 1/(x-3) + 2)")

if function_str:
    # 예시: y = 1/(x-3) + 2 (p=3, q=2)
    p = 3
    q = 2

    st.subheader("개념 정리")
    st.markdown("유리함수 $y = \\frac{k}{x-p} + q$ 에 대하여:")
    st.markdown(f"* **정의역**: 분모가 0이 아닌 실수 전체 $\\Rightarrow x \\neq p$")
    st.markdown(f"* **치역**: $y$ 점근선이 아닌 실수 전체 $\\Rightarrow y \\neq q$")
    st.markdown(f"* **점근선**: $x=p$, $y=q$")

    st.subheader("결과 분석")
    st.markdown(f"입력하신 함수 $f(x)$에 대하여:")
    st.write(f"**정의역**: $\\{{x \\mid x \\neq {p}, x \\in R \\}}\$")
    st.write(f"**치역**: $\\{{y \\mid y \\neq {q}, y \\in R \\}}\$")
    st.write(f"**점근선**: $x={p}$, $y={q}$")

    # 그래프 시각화 (예시)
    st.subheader("그래프")
    fig, ax = plt.subplots()

    # 점근선
    ax.axvline(p, color='gray', linestyle='--', label=f'x={p} (점근선)')
    ax.axhline(q, color='gray', linestyle=':', label=f'y={q} (점근선)')
    
    # ... 그래프 그리는 로직 추가 (x!=p 영역 분리하여 그리기)
    
    st.pyplot(fig)
