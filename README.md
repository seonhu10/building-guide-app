# 🏢 Building Guide App

도시와 건물 이름을 입력하면 AI가 그 건물을 한국어로 설명해주는 Streamlit 앱.

## Versions

| 파일 | 모델 | 비고 |
|---|---|---|
| `building-guide-app-v1.py` | Google Gemini 2.5 Flash | 초기 버전 |
| `building-guide-app-v2.py` | Anthropic Claude (Sonnet/Haiku/Opus 선택) | **현재 추천** ✨ |

## v2 새 기능

- 🎯 **모델 선택** — Sonnet (균형) / Haiku (빠름) / Opus (최고)
- ⚡ **스트리밍 응답** — 답변이 실시간으로 나타남
- 📥 **마크다운 다운로드** — 결과를 파일로 저장
- 🕘 **검색 히스토리** — 최근 10개 자동 표시
- 🛡️ **입력 검증 강화**
- 📋 **구조화된 답변** — 요약/상세/특징/의의/팁 5섹션

## Setup

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. API 키 설정

`.streamlit/secrets.toml` 파일 생성 (이 파일은 git에 안 올라감):

```toml
GEMINI_API_KEY = "your-gemini-key"      # v1용
ANTHROPIC_API_KEY = "your-claude-key"   # v2용
```

또는 Streamlit Cloud 배포 시 Settings → Secrets에서 입력.

**예시 파일:** `.streamlit/secrets.toml.example` 참고.

### 3. 실행

```bash
# v2 (Claude — 추천)
streamlit run building-guide-app-v2.py

# v1 (Gemini — 레거시)
streamlit run building-guide-app-v1.py
```

## 보안 주의

- ❌ API 키를 코드나 git에 절대 포함하지 마세요.
- ✅ `.gitignore`로 `.streamlit/secrets.toml`, `.env` 차단됨.
- ✅ 키는 환경변수 또는 Streamlit secrets로만 주입.

## License

Personal project.
