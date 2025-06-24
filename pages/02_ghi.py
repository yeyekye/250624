import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import yfinance as yf
import plotly.graph_objs as go

st.set_page_config(page_title="관광서비스과 대학 지도", layout="wide")

st.title("🗺️ 관광서비스과 진학 대학 위치 지도")
st.write("지도에서 관광서비스 관련 학과가 개설된 대학의 위치를 확인하고, 주식 시장 차트도 확인해보세요!")

# -------------------------
# 대학 위치 데이터
# -------------------------
college_data = pd.DataFrame({
    "대학명": [
        "한국관광대학교", "계원예술대학교", "동서울대학교",
        "대전과학기술대학교", "제주관광대학교", "부산여자대학교", "송호대학교"
    ],
    "학과명": [
        "호텔관광학과", "커피바리스타학과", "항공서비스학과",
        "관광서비스과", "관광경영과", "커피바리스타학과", "항공서비스과"
    ],
    "위도": [
        37.2025, 37.3921, 37.4823,
        36.3367, 33.4510, 35.1455, 37.3867
    ],
    "경도": [
        127.3893, 127.1266, 127.1187,
        127.4238, 126.5715, 129.0345, 128.0416
    ]
})

# -------------------------
# 지도 생성 (folium)
# -------------------------
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

for _, row in college_data.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=f'{row["대학명"]} - {row["학과명"]}',
        tooltip=row["대학명"],
        icon=folium.Icon(color="blue", icon="graduation-cap", prefix='fa')
    ).add_to(m)

# Streamlit에 folium 지도 삽입
st.subheader("🎓 전국 관광서비스과 관련 대학 위치")
st_data = st_folium(m, width=1000, height=500)

# -------------------------
# 보너스: yfinance + plotly 차트
# -------------------------
st.subheader("📈 샘플 주식 차트 (교육 목적)")

symbol = st.selectbox("관심 있는 종목을 선택하세요:", ["AAPL", "GOOGL", "TSLA", "AMZN"])
stock_data = yf.download(symbol, period="1mo")

fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["Close"], mode="lines", name="Close"))
fig.update_layout(title=f"{symbol} 주가 (최근 1개월)", xaxis_title="날짜", yaxis_title="가격")

st.plotly_chart(fig, use_container_width=True)
