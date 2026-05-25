# AI Security Threat Monitoring Agent

## Overview

AI Security Threat Monitoring Agent is a cybersecurity monitoring system that analyzes security logs, detects suspicious activities, prioritizes critical threats, and provides AI-generated explanations in simple language.

The system helps security teams reduce alert fatigue by automatically identifying important threats from large volumes of security events.

---

## Problem Statement

Security teams receive thousands of alerts daily, making it difficult to identify genuine threats quickly.

This project addresses that problem by:

- Analyzing security logs
- Monitoring authentication events
- Detecting suspicious activities
- Prioritizing critical threats
- Generating AI-powered threat explanations
- Providing actionable security recommendations

---

## Features

### Security Log Analysis
- Upload log files for analysis
- Parse authentication and security events
- Process large sets of log entries

### Threat Detection
- Brute Force Attack Detection
- Privilege Escalation Detection
- Suspicious Login Activity Detection
- Authentication Failure Monitoring

### Threat Prioritization
Threats are categorized by severity:

- Critical
- High
- Medium
- Low

### AI Security Analysis
The system uses Google's Gemini AI model to:

- Explain detected threats
- Assess risk levels
- Recommend mitigation actions
- Generate executive summaries

### Dashboard
The dashboard displays:

- Total Logs Processed
- Total Threats Detected
- Critical Threat Count
- High-Risk Threat Count
- Detailed Threat Table
- AI Security Report

---

## Technology Stack

### Backend
- Python
- Flask

### AI Engine
- Google Gemini API

### Frontend
- HTML
- CSS

### Security Analysis
- Custom Rule-Based Detection Engine

---

## Project Structure

ai-security-agent/
│
├── app.py
├── detector.py
├── ai.py
│
├── uploads/
│
├── templates/
│ ├── index.html
│ └── dashboard.html
│
└── README.md

---

## Installation

### Clone Project

```bash
git clone <repository-url>
cd ai-security-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask
pip install google-genai
```

---

## Configure Gemini API

Set your Gemini API Key:

Windows:

```bash
setx GEMINI_API_KEY "YOUR_API_KEY"
```

Linux/Mac:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

---

## Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Workflow

1. Upload security log file
2. System analyzes logs
3. Threat detection engine identifies suspicious activities
4. Threats are prioritized by severity
5. Gemini AI generates explanations and recommendations
6. Results are displayed on the dashboard

---

## Example Threats Detected

### Brute Force Attack

Multiple failed login attempts from the same source followed by a successful login.

### Privilege Escalation

Unauthorized elevation of user permissions to administrator level.

### Suspicious Authentication Activity

Unusual authentication patterns and login anomalies.

---

## Future Improvements

- Real-time log monitoring
- SIEM integration
- Threat intelligence feeds
- Email and Slack alerts
- Advanced anomaly detection
- Cloud security monitoring
- Machine learning threat classification

---

## Author

Hackathon Project

AI Security Threat Monitoring Agent