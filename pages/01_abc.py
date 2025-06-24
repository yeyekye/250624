import streamlit as st

st.set_page_config(page_title="관광서비스과 진학 길라잡이", layout="wide")

st.title("🎓 관광서비스과 진학 길라잡이")
st.write("관광서비스과 고3 학생을 위한 대학 및 학과 정보 안내 웹앱입니다.")

# -----------------------
# 데이터 입력
# -----------------------
data = [
    {"대학명": "한국관광대학교", "학과명": "호텔관광학과", "지역": "경기", "유형": "호텔", "특징": "호텔 실습 특화, 인턴십 연계"},
    {"대학명": "계원예술대학교", "학과명": "커피바리스타학과", "지역": "경기", "유형": "바리스타", "특징": "바리스타 실기 중심, 자격증 취득 지도"},
    {"대학명": "동서울대학교", "학과명": "항공서비스학과", "지역": "서울", "유형": "항공", "특징": "항공사 승무원 채용 연계"},
    {"대학명": "대전과학기술대학교", "학과명": "관광서비스과", "지역": "대전", "유형": "관광", "특징": "현장실습 중심, 관광통역지도사 준비"},
    {"대학명": "제주관광대학교", "학과명": "관광경영과", "지역": "제주", "유형": "관광", "특징": "관광지 실습, 해외 인턴 기회"},
    {"대학명": "부산여자대학교", "학과명": "커피바리스타학과", "지역": "부산", "유형": "바리스타", "특징": "여성 전문 바리스타 양성"},
    {"대학명": "송호대학교", "학과명": "항공서비스과", "지역": "강원", "유형": "항공", "특징": "외국어 교육 특화"},
]

# -----------------------
# 필터 선택
# -----------------------
regions = sorted(set([d["지역"] for d in data]))
types = sorted(set([d["유형"] for d in data]))

st.sidebar.header("🔍 조건 검색")
selected_region = st.sidebar.selectbox("지역 선택", ["전체"] + regions)
selected_type = st.sidebar.selectbox("학과 유형", ["전체"] + types)

# -----------------------
# 필터링
# -----------------------
filtered = []
for item in data:
    if (selected_region == "전체" or item["지역"] == selected_region) and \
       (selected_type == "전체" or item["유형"] == selected_type):
        filtered.append(item)

# -----------------------
# 결과 출력
# -----------------------
st.subheader("📚 추천 학과 목록")

if not filtered:
    st.warning("선택한 조건에 맞는 학과가 없습니다.")
else:
    for school in filtered:
        with st.container():
            st.markdown(f"### {school['대학명']} - {school['학과명']}")
            st.markdown(f"- 📍 위치: {school['지역']}")
            st.markdown(f"- 🔖 학과 유형: {school['유형']}")
            st.markdown(f"- ✏️ 특징: {school['특징']}")
            st.markdown("---")
