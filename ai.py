import os
from google import genai

# BEST PRACTICE: use environment variable (instead of hardcoding key)
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key="AIzaSyDWAVC5G3LSAa_LD1K8jwgi-nVc7D2IyTA")


def explain_threat(threats):
    try:
        if not threats:
            return "No threats detected. System is secure."

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are a senior cybersecurity analyst.

Analyze these security threats from a monitoring system:

{threats}

Provide output in this format:

1. What happened
2. Severity (Low/Medium/High/Critical)
3. Why it is dangerous
4. Recommended actions
5. Short summary for executives
"""
        )

        return response.text

    except Exception as e:
        return f"""
AI Analysis Failed (Fallback Mode)

System still working using rule-based detection.

Error: {str(e)}

Recommendation:
- Check API key
- Verify internet connection
- Continue using detected threats from engine
"""