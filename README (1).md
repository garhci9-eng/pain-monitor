# 🏥 무의식 환자 통증 모니터링 시스템
# Unconscious Patient Pain Monitoring System

> **"말 못하는 환자도 얼마나 아픈지 의료진이 알 수 있으면 좋겠다"**
> *"I wish medical staff could know how much pain a non-verbal patient is in."*

---

## 🌱 이 프로젝트의 시작 / Origin

이 프로젝트는 한국의 한 사람이 가진 작은 바람에서 시작됐습니다.

*"암이나 중증 질환으로 힘드신 분들이 많잖아요. 의식이 없어도 통증은 있을 텐데, 그게 수치로 보였으면 좋겠어요. 그분들이 조금이라도 덜 아팠으면 해서요."*

아이디어는 사람이 냈고, Claude AI가 첫 번째 버전을 함께 만들었습니다.
이제 이걸 실제로 작동하는 프로그램으로 만들어줄 분들이 필요합니다.

This project started from a simple wish by someone in Korea.

*"There are so many people suffering from cancer and serious illness. Even unconscious, they still feel pain. I wished medical staff could see that pain as a number. I just want them to hurt a little less."*

The idea came from a person. Claude AI helped build the first version.
Now it needs people who can turn it into something real.

---

## 💡 아이디어 / The Idea

기존 바이탈 모니터는 맥박, 혈압을 보여줍니다.
하지만 **"이 환자가 지금 얼마나 아픈가"** 는 환자가 말을 못 하면 알 수 없어요.

바이탈 데이터(맥박, 혈압, 호흡수, 발한, 얼굴 근육 긴장도 등)를 AI로 분석하면 통증 수치를 추정할 수 있습니다.

Existing monitors show heart rate and blood pressure — but not **"how much pain is this patient in right now."**
By analyzing vital signs with AI, pain can be estimated and shown to medical staff for faster, more accurate care.

---

## 🚀 실행 방법 / How to Run

### 1. 저장소 복사 / Clone
```bash
git clone https://github.com/YOUR_USERNAME/pain-monitor.git
cd pain-monitor
```

### 2. 패키지 설치 / Install
```bash
pip install -r requirements.txt
```

### 3. API 키 설정 / Set API Key
```bash
cp .env.example .env
# .env 파일을 열고 ANTHROPIC_API_KEY에 본인 키를 입력하세요
# Get your key at: https://console.anthropic.com
```

### 4. 실행 / Run
```bash
python app.py
```

### 5. 브라우저에서 접속 / Open Browser
```
http://localhost:5000
```

---

## 🤝 같이 만들어주세요 / Let's Build This Together

이 저장소는 **시작점**입니다. 다음 분들의 참여를 기다립니다:

- 👨‍⚕️ **의료진** — 실제 임상에서 어떤 데이터가 필요한지 알려주세요
- 👩‍💻 **개발자** — 더 정확하고 안정적인 시스템으로 만들어주세요
- 🔬 **연구자** — 통증 추정 알고리즘을 더 정확하게 만들어주세요
- 💬 **누구든** — Issues에 아이디어와 피드백을 남겨주세요

---

## 🔮 앞으로의 계획 / Roadmap

- [ ] 카메라 연동 — 얼굴 표정 자동 인식
- [ ] 실시간 바이탈 기기 연동
- [ ] 환자별 통증 추이 그래프
- [ ] 임상 데이터 기반 AI 정확도 향상
- [ ] 병원 시스템(EMR) 연동
- [ ] 모바일 앱 버전

---

## 📜 기여 인정 / Credits

- **아이디어 기여자 (50%)** — 이 프로젝트를 처음 구상한 사람. 익명이지만 이 프로젝트의 절반은 이분의 것입니다.
- **Claude AI by Anthropic (50%)** — 첫 번째 버전 구현을 도왔습니다.

**Idea Contributor (50%)** — The person who first envisioned this. They wish to remain anonymous, but half of this belongs to them.
**Claude AI by Anthropic (50%)** — Assisted in building the first version.

---

## 📄 라이선스 / License

**공익 목적 전용 / Public Benefit Only**

✅ 허용: 병원, 요양원, 의료 연구, 비영리 의료 서비스
❌ 금지: 상업적 판매, 영리 목적 사용

✅ Allowed: Hospitals, care facilities, medical research, non-profit healthcare
❌ Not allowed: Commercial sale, for-profit use

---

## ⚠️ 면책 사항 / Disclaimer

이 시스템은 **의료 보조 도구**입니다. 최종 판단은 반드시 의료진이 해야 합니다.
This is a **medical support tool**. All final decisions must be made by qualified medical professionals.

---

*이 프로젝트는 통증으로 힘드신 모든 환자분들을 위해 만들었습니다.*
*This project was made for every patient who suffers in silence.*
