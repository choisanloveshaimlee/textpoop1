import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# 1. 기본 설정 및 함수 정의
# -----------------------------------------------------------

st.set_page_config(layout="wide")
st.title("📈 이차함수 그래프의 표준형 학습 앱: $y=a(x-p)^2+q$")
st.markdown("이 앱을 통해 이차함수 표준형에서 $p$와 $q$ 값이 그래프에 미치는 영향을 시각적으로 학습해 보세요.")
st.markdown("---")

# 이차함수 그래프를 그리는 함수
def plot_parabola(a, p, q, title):
    # x 범위 설정
    x = np.linspace(-10, 10, 400)
    # y 값 계산: y = a(x-p)^2 + q
    y = a * (x - p)**2 + q

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, label=f'$y={a}(x-{p})^2 + {q}$')

    # 꼭짓점 표시
    ax.plot(p, q, 'ro') # 'ro'는 빨간색 원
    ax.text(p + 0.2, q + 0.5, f'꼭짓점 ({p}, {q})', color='red')

    # 축 설정
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title(title, fontsize=16)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    
    # y=ax^2 기준 그래프 (비교를 위해)
    y_base = a * x**2
    ax.plot(x, y_base, 'b--', alpha=0.5, label=f'기준: $y={a}x^2$')
    
    plt.close(fig) # 메모리 효율을 위해 닫기
    return fig

# -----------------------------------------------------------
# 2. y = a(x-p)² 분석 (x축 평행이동)
# -----------------------------------------------------------

st.header("1️⃣ $y=a(x-p)^2$ 분석: **x축 평행이동**")
st.markdown("$\mathbf{a}$를 고정($a=2$)하고 $\mathbf{p}$ 값을 변경하며 그래프가 **좌우**로 움직이는 것을 관찰하세요.")

# 'a' 값 고정 (a=2), 'q' 값 고정 (q=0)
a_val_p = 2
p_val = st.slider("x축 평행이동 값 $p$", -5.0, 5.0, 0.0, 0.5, key='p_slider')
q_val_p = 0 

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"현재 그래프: $y={a_val_p}(x-{p_val})^2$")
    fig_p = plot_parabola(a_val_p, p_val, q_val_p, f'p 변화: $y={a_val_p}(x-{p_val})^2$')
    st.pyplot(fig_p)

with col2:
    st.warning("⚠️ **주의!** 식에서 $x-p$일 때 꼭짓점 $x$좌표는 $+p$입니다.")
    st.info(f"""
    **🔍 관찰 결과:**
    * 꼭짓점의 좌표는 $(\mathbf{{p}}, 0)$입니다.
    * $y=2x^2$의 그래프를 **x축 방향으로** $\mathbf{{p}}$ 만큼 평행이동한 것입니다.
    """)

st.markdown("---")

# -----------------------------------------------------------
# 3. y = ax²+q 분석 (y축 평행이동)
# -----------------------------------------------------------

st.header("2️⃣ $y=ax^2+q$ 분석: **y축 평행이동**")
st.markdown("$\mathbf{a}$를 고정($a=2$)하고 $\mathbf{q}$ 값을 변경하며 그래프가 **상하**로 움직이는 것을 관찰하세요.")

# 'a' 값 고정 (a=2), 'p' 값 고정 (p=0)
a_val_q = 2
p_val_q = 0 
q_val = st.slider("y축 평행이동 값 $q$", -5.0, 5.0, 0.0, 0.5, key='q_slider')

col3, col4 = st.columns(2)

with col3:
    st.subheader(f"현재 그래프: $y={a_val_q}x^2 + {q_val}$")
    fig_q = plot_parabola(a_val_q, p_val_q, q_val, f'q 변화: $y={a_val_q}x^2 + {q_val}$')
    st.pyplot(fig_q)

with col4:
    st.info(f"""
    **🔍 관찰 결과:**
    * 꼭짓점의 좌표는 $(0, \mathbf{{q}})$입니다.
    * $y=2x^2$의 그래프를 **y축 방향으로** $\mathbf{{q}}$ 만큼 평행이동한 것입니다.
    """)

st.markdown("---")

# -----------------------------------------------------------
# 4. y = a(x-p)²+q 통합 분석
# -----------------------------------------------------------

st.header("3️⃣ 표준형 $y=a(x-p)^2+q$ **통합 관찰**")
st.markdown("$\mathbf{p}$ 값과 $\mathbf{q}$ 값을 동시에 변경하여 평행이동의 결과를 확인하고 **꼭짓점**을 파악해 보세요.")

# 'a' 값 선택
a_val_all = st.selectbox("그래프의 폭과 방향 $\mathbf{a}$ 값", [1, -1, 0.5, -0.5, 2, -2], index=4)

col_all_1, col_all_2, col_all_3 = st.columns(3)
with col_all_1:
    p_val_all = st.slider("x축 평행이동 $p$", -5.0, 5.0, 1.0, 0.5, key='p_all_slider')
with col_all_2:
    q_val_all = st.slider("y축 평행이동 $q$", -5.0, 5.0, 2.0, 0.5, key='q_all_slider')
with col_all_3:
    st.metric("꼭짓점 좌표", f"({p_val_all}, {q_val_all})", help="꼭짓점은 (p, q)입니다.")


st.subheader(f"최종 그래프: $y={a_val_all}(x-{p_val_all})^2 + {q_val_all}$")
fig_all = plot_parabola(a_val_all, p_val_all, q_val_all, f'통합: $y={a_val_all}(x-{p_val_all})^2 + {q_val_all}$')
st.pyplot(fig_all)

# 오류가 났던 f-string 부분을 일반 문자열로 수정했습니다.
st.success("""
**🎉 최종 정리:**
* 표준형 $\mathbf{y=a(x-p)^2+q}$ 는 $\mathbf{y=ax^2}$ 그래프를 **x축으로 $\mathbf{p}$만큼, y축으로 $\mathbf{q}$만큼** 평행이동한 것입니다.
* 그래프의 꼭짓점의 좌표는 $(\mathbf{p}, \mathbf{q})$ 입니다.
""")

st.markdown("---")

# -----------------------------------------------------------
# 5. 개념 확인 퀴즈
# -----------------------------------------------------------

st.header("4️⃣ 개념 확인 퀴즈")
st.subheader("아래 이차함수의 **꼭짓점 좌표**는 무엇일까요?")

quiz_q = "$y=-3(x+2)^2+5$"
quiz_ans = "(-2, 5)"

st.markdown(f"**문제:** {quiz_q}")
user_answer = st.text_input("정답 입력 (예: (p, q))", key='quiz_input')

if st.button("정답 확인하기"):
    # 입력된 문자열 정리 (공백, 괄호 제거)
    clean_user_ans = user_answer.replace(" ", "").replace("(", "").replace(")", "")
    clean_correct_ans = quiz_ans.replace(" ", "").replace("(", "").replace(")", "")

    if clean_user_ans == clean_correct_ans:
        st.balloons()
        st.success("✅ **정답입니다!** $x+2$는 $x-(-2)$이므로 $p=-2, q=5$입니다.")
    else:
        st.error("❌ **오답입니다.** 식을 $y=a(x-p)^2+q$ 형태로 변형하여 꼭짓점 $(\mathbf{p}, \mathbf{q})$를 다시 확인해 보세요. ($x+2 = x-(-2)$)")
