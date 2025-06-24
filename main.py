import streamlit as st
import pandas as pd

# CSV 파일 읽기 (EUC-KR 인코딩)
file_path = '202505_202505_연령별인구현황_월간.csv'
df = pd.read_csv(file_path, encoding='euc-kr')

st.title("2025년 5월 기준 연령별 인구 현황 분석")
st.write("출처: 통계청 / 단위: 명")

# 필요한 열만 추출: '행정구역', '총인구수', '연령별 인구'
# 열 이름 중 '2025년05월_계_'로 시작하는 열만 추출 (연령 열)
age_columns = [col for col in df.columns if col.startswith("2025년05월_계_")]
df_age = df[['행정구역별(1)'] + ['2025년05월_계_총인구수'] + age_columns].copy()

# 컬럼명 정리
df_age = df_age.rename(columns={'행정구역별(1)': '행정구역', '2025년05월_계_총인구수': '총인구수'})

# 연령 숫자만 남기기
rename_dict = {col: col.replace("2025년05월_계_", "") for col in age_columns}
df_age = df_age.rename(columns=rename_dict)

# 상위 5개 행정구역 선택 (총인구수 기준)
df_top5 = df_age.sort_values(by='총인구수', ascending=False).head(5)

# 연령 컬럼만 추출 (가로: 연령, 세로: 인구수)
age_only_cols = list(rename_dict.values())

# 선 그래프용 데이터 준비
st.subheader("상위 5개 행정구역의 연령별 인구 분포")
for i in range(len(df_top5)):
    region = df_top5.iloc[i]['행정구역']
    region_data = df_top5.iloc[i][age_only_cols].astype(int)
    
    st.write(f"📍 {region}")
    st.line_chart(region_data.T, use_container_width=True)

# 원본 데이터 보여주기
st.subheader("📄 원본 데이터 (요약)")
st.dataframe(df_top5.reset_index(drop=True))
