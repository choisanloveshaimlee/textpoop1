import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Poly, fraction, parse_expr

# SymPy를 이용해 일반형을 분석하고 p, q, k를 계산하는 함수
def analyze_rational_function(func_str):
    """
    유리함수 문자열을 분석하여 p, q, k 값을 반환합니다.
    p: 수직 점근선 (분모가 0이 되는 x값)
    q: 수평 점근선 (x가 무한대로 갈 때 y값)
    k: 그래프의 모양과 위치를 결정하는 상수
    """
    x = symbols('x')
    
    try:
        # 문자열을 SymPy 표현식으로 파싱합니다.
        # 예: "(2*x+1)/(x-3)"
        f_x = parse_expr(func_str, evaluate=False)
        
        # 분자(num)와 분모(den)를 추출합니다.
        num, den = fraction(f_x)
        
        # 분자, 분모를 x에 대한 다항식 객체로 변환합니다.
        poly_num = Poly(num, x)
        poly_den = Poly(den, x)
        
        # 계수 추출: (ax+b) / (cx+d)
        # SymPy Poly 객체는 차수가 높은 항부터 계수를 저장합니다.
        if poly_num.degree() == 1:
            a = poly_num.coeffs()[0] if len(poly_num.coeffs()) > 1 else 0
            b = poly_num.coeffs()[1] if len(poly_num.coeffs()) > 1 else poly_num.coeffs()[0]
        else: # 분자 차수가 0
            a = 0
            b = poly_num.coeffs()[0]
            
        if poly_den.degree() == 1:
            c = poly_den.coeffs()[0]
            d = poly_den.coeffs()[1]
        else: # 분모 차수가 0 (다항함수가 됨)
            st.error("오류: 분모가 상수이거나 x에 대한 일차식이 아닙니다.")
            return None, None, None

        # 분모가 0이 되는 경우 (c=0)
        if c == 0:
            st.error("오류: 분모의 x 계수가 0입니다. 이는 분수함수가 아닙니다.")
            return None, None, None
            
        # ----------------------------------
        # p, q, k 공식 적용
        # y = k/(x-p) + q
        # ----------------------------------
        
        # 수직 점근선: x = p = -d/c
        p = -d / c
        
        # 수평 점근선: y = q = a/c
        q = a / c
        
        # 상수 k: k = (bc - ad) / c^2
        k = (b * c - a * d) / (c * c)

        return float(p), float(q), float(k)
    
    except Exception as e:
        st.error(f"함수 분석 중 오류가 발생했습니다. 입력 형식을 확인해 주세요. (예: (2*x+1)/(x-3))")
        st.exception(e)
        return None, None, None

# -------------------------------------------------------------
# Streamlit 앱 본체 시작
# -------------------------------------------------------------

st.set_page_config(layout="wide")
st.title("📊 유리함수 개념 학습 및 시각화")
st.markdown("---")

# ---------------------------------
# 1. 사용자 입력
# ---------------------------------
st.sidebar.header("함수 입력")
func_input = st.sidebar.text_input(
    "유리함수의 식을 입력하세요 (일반형)",
    value="(2*x+1)/(x-3)"
)

# ---------------------------------
# 2. 분석 및 결과 표시
# ---------------------------------

if func_input:
    p, q, k = analyze_rational_function(func_input)
    
    if p is not None:
        
        st.header("🔍 함수 분석 결과")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📚 표준형 변환")
            st.latex(f"y = \\frac{{ax+b}}{{cx+d}} \\quad \\rightarrow \\quad y = \\frac{{k}}{{x - p}} + q")
            st.markdown(f"**입력 함수**: $y = {func_input}$")
            
            # 표준형 결과 표시 (k가 0에 매우 가까우면 표시하지 않음)
            if abs(k) < 1e-9:
                st.latex(f"y = {q}")
                st.warning("경고: k 값이 0에 매우 가깝습니다. 이는 분수함수가 아닌 직선입니다.")
            else:
                st.latex(f"y = \\frac{{{k:.3f}}}{{x - ({p:.3f})}} + {q:.3f}")
        
        with col2:
            st.subheader("📍 점근선 (Asymptote)")
            st.markdown("점근선은 그래프가 한없이 가까워지지만 만나지 않는 직선입니다.")
            st.markdown(f"**수직 점근선** ($x=p$): $\\mathbf{{x = {p:.3f}}}$")
            st.markdown(f"**수평 점근선** ($y=q$): $\\mathbf{{y = {q:.3f}}}$")
            st.markdown(f"**점근선의 교점**: $\\mathbf{{({p:.3f}, {q:.3f})}}$")

        st.markdown("---")
        
        st.header("集合 정의역, 치역, 공역")
        st.markdown("---")
        
        col3, col4, col5 = st.columns(3)
        
        with col3:
            st.subheader("정의역 (Domain)")
            st.markdown("함수가 정의될 수 있는 $x$ 값의 집합입니다. (분모 $\\neq 0$)")
            st.latex(f"D = \\mathbf{{\\{{x \\mid x \\neq {p:.3f}, x \\in R \\}}}}")
            
        with col4:
            st.subheader("치역 (Range)")
            st.markdown("$x$에 대응되는 $y$ 값의 집합입니다. ($y \\neq$ 수평 점근선)")
            st.latex(f"R = \\mathbf{{\\{{y \\mid y \\neq {q:.3f}, y \\in R \\}}}}")

        with col5:
            st.subheader("공역 (Codomain)")
            st.markdown("함수의 값이 될 수 있는 전체 $y$ 값의 집합입니다. (특별 언급 없으면 실수 전체)")
            st.latex("\\mathbf{R \\quad (실수 전체의 집합)}")

        st.markdown("---")
        
        # ---------------------------------
        # 3. 그래프 시각화
        # ---------------------------------
        st.header("📈 그래프 시각화")

        fig, ax = plt.subplots(figsize=(10, 6))

        # x 값 범위 설정 (점근선 주변은 제외)
        min_x, max_x = p - 10, p + 10
        
        x_range1 = np.linspace(min_x, p - 0.01, 500)
        x_range2 = np.linspace(p + 0.01, max_x, 500)

        # 함수 정의 (표준형 기준)
        def rational_func(x, k, p, q):
            return k / (x - p) + q

        # 그래프 그리기
        ax.plot(x_range1, rational_func(x_range1, k, p, q), color='C0')
        ax.plot(x_range2, rational_func(x_range2, k, p, q), color='C0', label=f'Function')

        # 점근선 표시
        ax.axvline(p, color='red', linestyle='--', linewidth=1.5, label=f'x={p:.2f} (수직 점근선)')
        ax.axhline(q, color='blue', linestyle='--', linewidth=1.5, label=f'y={q:.2f} (수평 점근선)')
        ax.plot(p, q, 'o', color='green', markersize=5, label='점근선 교점')

        # 설정
        ax.set_title(f"유리함수 그래프", fontsize=16)
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_ylim(q - 10, q + 10)
        ax.set_xlim(min_x, max_x)
        ax.legend()
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        st.pyplot(fig)

