import streamlit as st
from google import genai
import os

# --- 1. Gemini API 설정 ---
# Streamlit Cloud의 비밀 저장소에서 키를 가져오는 방식입니다.
# 로컬에서 실행할 때는 secrets.toml 파일이 필요하지만, 클라우드에서는 설정 화면에서 입력합니다.
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=GEMINI_API_KEY)

# --- 2. 앱 화면 구성 (GUI) ---
st.set_page_config(page_title="건물 정보 가이드 (Gemini)", page_icon="🏢")

st.title("🏢 건물 정보 돋보기 (Gemini 버전)")
st.subheader("궁금한 건물의 정보를 즉시 확인하세요!")

col1, col2 = st.columns(2)
with col1:
    city = st.text_input("도시 입력", placeholder="예: 서울, 파리")
with col2:
    building_name = st.text_input("건물 이름 입력", placeholder="예: 63빌딩, 에펠탑")

if st.button("정보 가져오기"):
    if not city or not building_name:
        st.warning("도시와 건물 이름을 모두 입력해 주세요.")
    elif not GEMINI_API_KEY:
        st.error("API 키가 설정되지 않았습니다. 코드를 확인해 주세요.")
    else:
        with st.spinner('Gemini AI가 정보를 분석 중입니다...'):
            try:
                # --- 3. Gemini 모델 요청 (최신 SDK 문법) ---
                user_prompt = f"도시: {city}, 건물 이름: {building_name}"
                
                # 최신 SDK에서는 client.models.generate_content를 사용합니다.
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt,
                    config={
                        'system_instruction': (
                            "너는 전문 건축 가이드야. 사용자가 도시와 건물을 입력하면 해당 건물을 설명해줘. "
                            "반드시 '한국어'로 친절하게 답변해야 해. "
                            "답변 구조: 1.요약, 2.상세정보(완공/설계/양식), 3.건축적 특징, 4.역사적 의의, 5.방문 팁"
                        )
                    }
                )

                # --- 4. 결과 출력 ---
                st.markdown("---")
                st.markdown(f"### 📍 {building_name} ({city})")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")