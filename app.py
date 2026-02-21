from flask import Flask, render_template, request, jsonify
import anthropic
import os

app = Flask(__name__)

# Anthropic 클라이언트 설정
# .env 파일에 ANTHROPIC_API_KEY를 설정하거나 환경변수로 넣어주세요
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """당신은 중환자실 통증 평가 AI 보조 시스템입니다.
무의식 환자의 바이탈 사인을 분석하여 통증 수치(0~10)를 추정하고 의료진을 위한 치료 계획을 제시합니다.
반드시 다음 JSON 형식으로만 응답하세요:
{
  "painScore": 숫자(0-10),
  "confidence": "높음/중간/낮음",
  "assessment": "통증 평가 요약 (2-3문장)",
  "treatmentPlan": "의료진을 위한 구체적 치료 계획 (단계별로)",
  "urgency": "낮음/중간/높음/긴급"
}"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    user_message = f"""무의식 환자 바이탈 데이터:
- 맥박: {data.get('heartRate', 'N/A')}회/분
- 혈압: {data.get('systolic', 'N/A')}/{data.get('diastolic', 'N/A')} mmHg
- 호흡수: {data.get('respRate', 'N/A')}회/분
- 산소포화도: {data.get('spo2', 'N/A')}%
- 체온: {data.get('temp', 'N/A')}°C
- 발한: {data.get('sweating', 'N/A')}
- 얼굴 근육 긴장도: {data.get('facialTension', 'N/A')}

이 데이터를 바탕으로 통증 수치를 추정하고 치료 계획을 제시해주세요."""

    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}]
        )

        import json
        text = message.content[0].text
        clean = text.replace("```json", "").replace("```", "").strip()
        result = json.loads(clean)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🏥 무의식 환자 통증 모니터링 시스템 시작")
    print("브라우저에서 http://localhost:5000 으로 접속하세요")
    app.run(debug=True, port=5000)
