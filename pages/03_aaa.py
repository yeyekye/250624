import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="전국 관광서비스과 대학 지도", layout="wide")

# 제목
st.title("🗺️ 전국 관광서비스과 진학 대학 위치 지도")
st.markdown("관광서비스과 관련 학과가 개설된 전국 대학의 위치를 지도에서 확인해보세요.")

# 대학 데이터
college_data = pd.DataFrame({
    "대학명": [
        "한국관광대학교", "계원예술대학교", "동서울대학교",
        "대전과학기술대학교", "제주관광대학교", "부산여자대학교", "송호대학교",
        "전주기전대학", "경기과학기술대학교", "인하공업전문대학"
    ],
    "학과명": [
        "호텔관광학과", "커피바리스타학과", "항공서비스학과",
        "관광서비스과", "관광경영과", "커피바리스타학과", "항공서비스과",
        "관광과", "항공서비스과", "호텔관광과"
    ],
    "위도": [
        37.2025, 37.3921, 37.4823,
        36.3367, 33.4510, 35.1455, 37.3867,
        35.8032, 37.2681, 37.4505
    ],
    "경도": [
        127.3893, 127.1266, 127.1187,
        127.4238, 126.5715, 129.0345, 128.0416,
        127.1326, 127.0068, 126.6578
    ]
})

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 대학 위치 마커 추가
for _, row in college_data.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=f"<b>{row['대학명']}</b><br>{row['학과명']}",
        tooltip=row["대학명"],
        icon=folium.Icon(color="blue", icon="graduation-cap", prefix="fa")
    ).add_to(m)

# Streamlit에 지도 표시
st_data = st_folium(m, width=1000, height=600)

# 표 형태로도 데이터 제공
st.subheader("📋 대학 정보 보기")
st.dataframe(college_data, use_container_width=True)
