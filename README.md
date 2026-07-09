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
