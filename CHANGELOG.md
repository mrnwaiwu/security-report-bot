# Changelog

All notable changes to this project will be documented in this file.

## 2026-06-05 - Minor improvements

- Added support for multi-channel delivery (Slack + email) in a single report run
- Improved finding deduplication logic to handle cross-scanner overlaps
- Added configurable severity threshold filter (e.g. only report CRITICAL and HIGH)
- Fixed timestamp formatting in report headers for non-UTC timezones

## 2026-06-01 - Minor improvements

- Added PDF export option for generated security reports
- Improved deduplication of findings with identical CVE identifiers
- Fixed Slack message truncation for reports with large finding counts
- Added --dry-run flag to preview report output without sending

## 2026-05-29 - Minor improvements

- Added summary section to weekly security digest reports
- Improved Markdown formatting for report output
- Fixed edge case where empty finding lists caused report generation to fail
- Added configurable report title and footer fields

## 2026-05-01 - Initial release

- Automated security report generation from scanner output
- Slack and email delivery integrations
- Supports SARIF and JSON input formats
- Severity-bucketed findings table in output
