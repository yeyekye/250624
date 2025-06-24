import streamlit as st

# 페이지 제목
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠")

st.title("🎯 MBTI 기반 직업 추천기")
st.caption("당신의 성격 유형에 어울리는 직업을 찾아보세요!")

# MBTI 정보 사전
mbti_data = {
    "INTJ": {
        "description": "전략가 🧠 – 창의적이며 논리적인 해결사. 큰 그림을 보며 미래를 설계합니다.",
        "jobs": {
            "전략 컨설턴트": "기업의 문제를 해결하고 방향을 제시하는 전략 전문가 💼",
            "데이터 과학자": "데이터에서 인사이트를 도출하는 분석가 📊",
            "시스템 분석가": "IT 시스템을 효율적으로 설계하고 분석하는 전문가 💻"
        }
    },
    "ENFP": {
        "description": "활동가 🌈 – 열정적이고 창의적인 낙천주의자. 사람들과의 소통을 즐깁니다.",
        "jobs": {
            "브랜드 매니저": "브랜드 이미지를 만들고 관리하는 마케팅 전문가 🛍️",
            "광고 기획자": "창의적인 광고를 기획하고 캠페인을 이끄는 사람 📺",
            "창작자 (크리에이터)": "자신만의 콘텐츠를 만들고 세상과 소통하는 사람 🎨"
        }
    },
    "ISTJ": {
        "description": "현실주의자 📘 – 책임감 있고 신뢰할 수 있는 조직의 핵심.",
        "jobs": {
            "회계사": "숫자를 다루며 정확성을 추구하는 재무 전문가 📑",
            "공무원": "국가를 위해 일하며 안정적인 삶을 지향하는 직업 🏛️",
            "법률 보조원": "법률 전문가를 보조하며 실무를 처리하는 사람 ⚖️"
        }
    },
    "INFP": {
        "description": "중재자 💖 – 이상주의자이며 감성이 풍부한 사람.",
        "jobs": {
            "작가": "세상과 감정을 글로 표현하는 창조적 예술가 ✍️",
            "교육자": "학생들을 성장시키고 영감을 주는 선생님 🍎",
            "예술가": "자신의 감정을 다양한 방식으로 표현하는 창작자 🎨"
        }
    },
    # 원하면 여기 나머지 유형도 추가할 수 있음
}

# 사용자가 선택할 수 있는 MBTI 목록
mbti_types = list(mbti_data.keys())
selected_mbti = st.selectbox("🧬 당신의 MBTI 유형을 선택하세요:", mbti_types)

# 결과 출력
if selected_mbti:
    st.markdown("---")
    info = mbti_data[selected_mbti]
    st.subheader(f"🧾 {selected_mbti} 유형 설명")
    st.info(info["description"])

    st.subheader("🔍 추천 직업 리스트")
    for job, desc in info["jobs"].items():
        st.write(f"**✅ {job}**  \n{desc}")
    
    st.success("당신에게 딱 맞는 직업을 발견했나요? 🌟")
    st.balloons()  # 풍선 효과 🎈
