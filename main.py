import streamlit as st

# MBTI 유형별 직업 추천 사전
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "시스템 분석가"],
    "INTP": ["연구 과학자", "프로그래머", "기술 작가"],
    "ENTJ": ["경영 컨설턴트", "프로젝트 매니저", "기업가"],
    "ENTP": ["마케팅 전략가", "벤처 창업가", "기획자"],

    "INFJ": ["상담사", "작가", "심리학자"],
    "INFP": ["예술가", "작사가", "교육자"],
    "ENFJ": ["홍보 전문가", "교육 컨설턴트", "인사 관리자"],
    "ENFP": ["광고 기획자", "브랜드 매니저", "창작자"],

    "ISTJ": ["회계사", "공무원", "법률 보조원"],
    "ISFJ": ["간호사", "사회복지사", "교사"],
    "ESTJ": ["경영 관리자", "군 장교", "운영 관리자"],
    "ESFJ": ["고객 서비스 관리자", "행정직", "이벤트 플래너"],

    "ISTP": ["엔지니어", "정비사", "보안 전문가"],
    "ISFP": ["디자이너", "요리사", "사진작가"],
    "ESTP": ["영업 전문가", "마케터", "스타트업 창업자"],
    "ESFP": ["연예인", "MC", "이벤트 기획자"]
}

# Streamlit UI
st.title("MBTI 기반 직업 추천기 🎯")

# MBTI 목록
mbti_types = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 직업 추천 출력
if selected_mbti:
    st.subheader(f"✅ {selected_mbti} 유형에게 추천하는 직업:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
