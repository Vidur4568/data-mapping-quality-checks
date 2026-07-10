# Data Mapping Quality Checks

## Overview

This project demonstrates how Python can automate data quality validation during a data migration project. The application reads a multi-sheet Excel workbook containing source-to-target mappings and performs automated quality checks to identify incomplete or inconsistent mappings before migration.

The project was built using a fictional servicing data migration scenario to simulate a real-world business analyst or data analyst workflow.

---

## Features

- Reads a multi-sheet Excel workbook using pandas
- Summarizes workbook structure
- Detects missing source fields
- Detects missing target fields
- Detects missing transformation rules
- Detects missing SME owners
- Detects missing mapping status
- Detects duplicate source mappings
- Generates separate Excel reports for each issue
- Creates a summary report of all quality check results

---

## Case Study

Business Problem: 
During a data migration, organizations often manage thousands of source-to-target mappings across multiple systems. Reviewing these mappings manually is time-consuming and increases the risk of missing critical issues such as incomplete mappings, missing transformation rules, duplicated entries, or unassigned ownership. These errors can delay migrations, introduce data quality problems, and increase project costs.

Solution:
To address this challenge, I developed a Python-based data quality validation tool that automatically analyzes a multi-sheet business data mapping workbook. The application validates mapping completeness, identifies missing source and target fields, detects missing transformation rules, verifies mapping status and ownership, flags duplicate source mappings, and generates detailed Excel reports along with a summary report for quick review.

Outcome:
The application successfully automated the validation of the entire data mapping workbook and identified several data quality issues that would typically require manual review. Instead of searching through dozens of mapping records individually, users receive organized reports highlighting where problems exist, allowing teams to prioritize remediation before migration begins.

Business Impact:
Organizations can use this tool to improve the quality and consistency of their data migration process while reducing manual effort and review time. Automated validation helps identify issues earlier in the project lifecycle, supports stronger data governance practices, improves collaboration between business and technical teams, and reduces the risk of migrating incomplete or inaccurate data into production systems.

---

## Technologies Used

- Python
- pandas
- openpyxl
- Git
- GitHub
- Microsoft Excel

---

## Project Structure

```
data-mapping-quality-checks/
│
├── docs/
├── input/
├── output/
├── src/
│   ├── check_workbook.py
│   └── quality_checks.py
├── tests/
├── notebooks/
├── README.md
└── requirements.txt
```

---

## Quality Checks

The application automatically identifies:

- Missing source fields
- Missing target fields
- Missing transformation rules
- Missing mapping status
- Missing SME owners
- Duplicate source mappings

---

## Output

The application generates:

- missing_source_fields.xlsx
- missing_target_fields.xlsx
- missing_transformation_rules.xlsx
- missing_status.xlsx
- missing_sme_owner.xlsx
- duplicate_source_mappings.xlsx
- mapping_summary_report.xlsx

---

## Skills Demonstrated

- Data Mapping
- Data Quality Validation
- Python Automation
- Excel Processing
- pandas
- Git Version Control
- Business Analysis
- Data Migration Concepts

---

## Future Improvements

Potential future enhancements include:

- Data type validation
- Email validation
- Phone number validation
- Date format validation
- Lookup table validation
- Logging
- Dashboard reporting
- Database integration

---

## Author

Vidur Bhardwaj

Behavioral and Social Data Science  
The University of Texas at Austin
