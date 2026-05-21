"""
security-report-bot
--------------------
Reads a JSON findings file and auto-generates a formatted
security assessment PDF report. Great for audit deliverables.

Install: pip install fpdf2
"""

from fpdf import FPDF
from datetime import datetime
import json
import sys
import os

SAMPLE_FINDINGS = {
    "client": "Acme Corp",
    "assessment_date": "2024-03-01",
    "assessor": "Michael N.",
    "findings": [
        {"id": "FIND-001", "severity": "CRITICAL", "title": "Unpatched RCE Vulnerability (CVE-2024-1234)",
         "description": "Apache 2.4.51 on web01 is vulnerable to remote code execution.",
         "remediation": "Upgrade Apache to 2.4.58 or later immediately."},
        {"id": "FIND-002", "severity": "HIGH", "title": "Overprivileged IAM Roles in AWS",
         "description": "Three IAM roles have AdministratorAccess. Least privilege not enforced.",
         "remediation": "Audit and restrict IAM roles per team function."},
        {"id": "FIND-003", "severity": "MEDIUM", "title": "Missing MFA on Admin Accounts",
         "description": "4 of 12 admin accounts do not have MFA enabled.",
         "remediation": "Enforce MFA for all admin accounts via IAM policy."},
        {"id": "FIND-004", "severity": "LOW", "title": "Verbose Error Messages in Web App",
         "description": "Stack traces exposed in HTTP 500 responses.",
         "remediation": "Return generic error messages in production."},
    ],
}

SEVERITY_COLORS = {
    "CRITICAL": (200, 0, 0),
    "HIGH": (220, 80, 0),
    "MEDIUM": (200, 150, 0),
    "LOW": (0, 120, 0),
}


class SecurityReportPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(31, 56, 100)
        self.cell(0, 10, "SECURITY ASSESSMENT REPORT", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(31, 56, 100)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"CONFIDENTIAL - Page {self.page_no()}", align="C")


def generate_report(data: dict, output_file: str = "security_report.pdf") -> None:
    pdf = SecurityReportPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)

    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(31, 56, 100)
    pdf.cell(0, 12, data["client"], new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 7, f"Assessment Date: {data['assessment_date']}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Assessor: {data['assessor']}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Report Generated: {datetime.now().strftime('%Y-%m-%d')}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(31, 56, 100)
    pdf.cell(0, 8, "Findings Detail", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    for finding in data["findings"]:
        r, g, b = SEVERITY_COLORS.get(finding["severity"], (100, 100, 100))
        pdf.set_fill_color(r, g, b)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(28, 7, f" {finding['severity']}", fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 7, f"  {finding['id']}: {finding['title']}", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 6, f"Description: {finding['description']}", new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 100, 0)
        pdf.multi_cell(0, 6, f"Remediation: {finding['remediation']}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(4)

    pdf.output(output_file)
    print(f"Report saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1]) as f:
            data = json.load(f)
    else:
        print("No findings file provided - using sample data.")
        data = SAMPLE_FINDINGS
    generate_report(data)
