import streamlit as st
import pandas as pd
import numpy as np

# ── 여기서부터 자유롭게 수정하세요 ───────────────

st.title("나의 첫 번째 Streamlit 앱")   # ← 제목을 바꿔보세요

# ── 사이드바 ──────────────────────────────────
st.sidebar.title("설정")

chart_type = st.sidebar.radio(
    "차트 유형",
    ["꺾은선 그래프", "막대 그래프", "면적 그래프"]   # ← 유형을 바꿔보세요
)

n = st.sidebar.slider(
    "데이터 개수",
    min_value=50,    # ← 최솟값을 50으로 변경하였습니다.
    max_value=500,   # ← 최댓값을 500으로 변경하였습니다.
    value=100        # 초기 설정값도 100으로 상향 조정하였습니다.
)

# ── 메인 화면 ─────────────────────────────────
st.write("여기에 앱 설명을 적어보세요.")   # ← 설명을 바꿔보세요

data = pd.DataFrame(
    np.random.randn(n, 3),
    columns=['A', 'B', 'C']   # ← 컬럼 이름을 바꿔보세요
)

if chart_type == "꺾은선 그래프":
    st.line_chart(data)
elif chart_type == "막대 그래프":
    st.bar_chart(data)
else:
    st.area_chart(data)

st.dataframe(data.head(5))

# ── 여기까지 ──────────────────────────────────



# 바꾼 것: 사이드바의 데이터 개수를 조절하는 슬라이더 요소의 min_value를 50, max_value를 500, value를 100으로 변경하였다. 
# 이유: 소규모 데이터보다는 다소 규모가 있는 데이터 세트의 변동 추이를 보다 명확하게 조망하고, 무작위 분포의 시각적 패턴을 심도 있게 분석하기 위하여 데이터 생성의 허용 범위를 대폭 확장하였다.
