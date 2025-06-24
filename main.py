import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# 파일 업로드
uploaded_file = st.file_uploader("📂 엑셀 파일 업로드", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name="특강 계획 전체(학과별)", skiprows=1)
    df = df.rename(columns={
        df.columns[2]: "구분",
        df.columns[3]: "주제",
        df.columns[4]: "일시",
        df.columns[5]: "강사",
        df.columns[6]: "대상",
        df.columns[7]: "장소"
    })

    # 날짜 파싱
    df["날짜"] = pd.to_datetime(df["일시"].str.extract(r'(\d{4}\. *\d{1,2}\. *\d{1,2})')[0].str.replace(' ', ''), format="%Y.%m.%d", errors='coerce')

    today = datetime.now(pytz.timezone("Asia/Seoul")).date()

    st.title("📘 2025학년도 1학기 전문가 및 선배 특강")
    targets = sorted(df["대상"].dropna().unique())
    tabs = st.tabs(targets)

    def highlight_past(row):
        return ['background-color: #f0f0f0' if pd.notnull(row["날짜"]) and row["날짜"].date() < today else '' for _ in row]

    for i, target in enumerate(targets):
        with tabs[i]:
            st.subheader(f"🎯 대상: {target}")
            sub_df = df[df["대상"] == target].copy()
            sub_df = sub_df.sort_values("날짜")

            expert = sub_df[sub_df["구분"] == "전문가특강"]
            alumni = sub_df[sub_df["구분"] == "선배특강"]

            if not expert.empty:
                st.markdown("### 👨‍🏫 전문가 특강")
                st.dataframe(expert.style.apply(highlight_past, axis=1), use_container_width=True)
            else:
                st.info("전문가 특강 없음")

            if not alumni.empty:
                st.markdown("### 👩‍🎓 선배 특강")
                st.dataframe(alumni.style.apply(highlight_past, axis=1), use_container_width=True)
            else:
                st.info("선배 특강 없음")

    st.markdown("---")
    st.markdown("## 📄 원본 데이터")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("왼쪽에서 엑셀 파일을 업로드해주세요.")
