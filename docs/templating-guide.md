# Templating Guide

This guide explains how to create custom report section templates for security-report-bot.

## Overview

Report templates allow per-team customization of the generated security report output.
Templates use a simple variable substitution syntax and support conditional blocks.

## Template Syntax

### Variable Substitution

Use `{{ variable_name }}` to insert dynamic values:

```
Report generated: {{ report_date }}
Team: {{ team_name }}
Total findings: {{ finding_count }}
```

### Conditional Blocks

```
{% if severity == "CRITICAL" %}
  ⚠️  Immediate action required
{% endif %}
```

## Available Variables

| Variable | Description |
|---|---|
| `report_date` | ISO 8601 date of report generation |
| `team_name` | Target team name from config |
| `finding_count` | Total number of findings |
| `critical_count` | Number of CRITICAL severity findings |
| `high_count` | Number of HIGH severity findings |
| `scanner_name` | Name of the source scanner |
| `repo` | Source repository name |

## Example Template

```markdown
# Security Report — {{ team_name }}

**Date:** {{ report_date }}
**Scanner:** {{ scanner_name }}
**Repository:** {{ repo }}

## Summary

| Severity | Count |
|---|---|
| Critical | {{ critical_count }} |
| High | {{ high_count }} |
| Total | {{ finding_count }} |

{% if critical_count > 0 %}
## ⚠️ Critical Findings Require Immediate Attention
{% endif %}
```

## Configuration

Register your template in `config.yaml`:

```yaml
report:
  template: templates/my-team-report.md
  delivery:
    - slack
    - email
```

## Notes

- Templates are rendered server-side before delivery
- HTML templates are supported for email delivery
- Slack templates are auto-converted to Block Kit format
