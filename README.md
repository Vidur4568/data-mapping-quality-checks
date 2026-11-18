# Data Mapping Quality Checks

A Python tool that automates data quality validation on source-to-target mapping workbooks, catching incomplete or inconsistent mappings before a data migration begins.

## Overview

During a data migration, teams track how every source field maps to a target field, along with transformation rules, owners, and status. Reviewing those mappings by hand is slow and easy to get wrong.

This tool reads a multi-sheet Excel mapping workbook with pandas, runs six automated quality checks, and writes a separate Excel report for each issue type plus a summary report. It was built around a fictional servicing data migration scenario that mirrors a real business analyst or data analyst workflow.

## At a Glance

| | |
|---|---|
| Quality checks automated | 6 |
| Excel reports generated | 7 (6 issue reports + 1 summary) |
| Source-to-target records validated | 37 |
| Mapping workbook | 15 sheets |

## Quality Checks

| Check | What it flags |
|---|---|
| Missing source fields | Mappings with no source field defined |
| Missing target fields | Mappings with no target field defined |
| Missing transformation rules | Mappings with no rule describing how data is transformed |
| Missing mapping status | Mappings with no status recorded |
| Missing SME owners | Mappings with no subject matter expert assigned |
| Duplicate source mappings | The same source field mapped more than once |

The tool also summarizes the workbook structure so you can see what it is validating before the checks run.

## Output

Each run produces these Excel files:

- `missing_source_fields.xlsx`
- `missing_target_fields.xlsx`
- `missing_transformation_rules.xlsx`
- `missing_status.xlsx`
- `missing_sme_owner.xlsx`
- `duplicate_source_mappings.xlsx`
- `mapping_summary_report.xlsx`, a summary of the results of all checks

Issues are grouped by type, so a team can see where the problems are and prioritize fixes before migration starts.

## Project Structure

```text
data-mapping-quality-checks/
├── src/
│   ├── check_workbook.py     # Summarizes the workbook structure
│   └── quality_checks.py     # Runs the quality checks and writes the reports
├── requirements.txt
└── README.md
```

## How to Run

```bash
git clone https://github.com/Vidur4568/data-mapping-quality-checks.git
cd data-mapping-quality-checks
pip install -r requirements.txt
python src/check_workbook.py
python src/quality_checks.py
```

## Technologies

Python, pandas, openpyxl, Microsoft Excel, Git, GitHub

## Future Improvements

- Data type, email, phone number, and date format validation
- Lookup table validation
- Logging
- Dashboard reporting
- Database integration

## Author

Vidur Bhardwaj, Behavioral and Social Data Science, The University of Texas at Austin
