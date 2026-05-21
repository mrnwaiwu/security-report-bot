# security-report-bot

Python automation that reads a JSON security findings file and generates a clean, formatted PDF assessment report — ready to send to a client or leadership.

## Setup
```bash
pip install fpdf2
python report_bot.py                   # uses built-in sample data
python report_bot.py my_findings.json  # use your own findings file
```

## Findings JSON format
```json
{
  "client": "Acme Corp",
  "assessment_date": "2024-03-01",
  "assessor": "Your Name",
  "findings": [
    {
      "id": "FIND-001",
      "severity": "CRITICAL",
      "title": "...",
      "description": "...",
      "remediation": "..."
    }
  ]
}
```

## Tech Stack
Python · fpdf2 · JSON
