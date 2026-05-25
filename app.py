from flask import Flask, render_template, request
import os
import time
from detector import analyze_logs
from ai  import explain_threat

app = Flask(__name__)

# upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ensure folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        file = request.files["logfile"]

        if file.filename == "":
            return "No file selected"

        # unique filename (avoid overwrite issues)
        filename = str(int(time.time())) + "_" + file.filename
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        file.save(filepath)

        # read logs
        with open(filepath, "r") as f:
            logs = f.readlines()

        # STEP 1: Rule-based detection
        threats = analyze_logs(logs)

        # STEP 2: AI analysis (Gemini/OpenAI)
        try:
            ai_report = explain_threat(threats)
        except Exception as e:
            # fallback if AI fails (VERY IMPORTANT for hackathon demo)
            ai_report = f"""
AI temporarily unavailable.

Fallback Security Summary:
- Threats detected using rule engine
- System identified suspicious patterns
- Recommend manual review

Error: {str(e)}
"""

        # STATS for dashboard
        total_logs = len(logs)
        total_threats = len(threats)

        critical = len([t for t in threats if t["severity"] == "CRITICAL"])
        high = len([t for t in threats if t["severity"] == "HIGH"])
        medium = len([t for t in threats if t["severity"] == "MEDIUM"])

        return render_template(
            "dashboard.html",
            threats=threats,
            ai_report=ai_report,
            total_logs=total_logs,
            total_threats=total_threats,
            critical=critical,
            high=high,
            medium=medium
        )

    except Exception as e:
        return f"Something went wrong: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)