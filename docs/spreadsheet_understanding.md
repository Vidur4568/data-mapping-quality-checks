# Spreadsheet Understanding

## Project Overview

The purpose of this workbook is to simulate a real-world data migration project. It documents how data moves from a legacy servicing system into a modern servicing platform while maintaining data quality, traceability, and business definitions.

## Worksheet Summary

### README
Provides an overview of the workbook, its purpose, and instructions for using each worksheet.

### Dashboard
Displays a high-level summary of the migration project, including progress and quality metrics.

### Source System Inventory
Lists all source systems involved in the migration, including system names, owners, interfaces, and descriptions.

### Source Data Dictionary
Documents every source field, including field names, data types, business definitions, and sample values.

### Target Data Dictionary
Documents the destination fields that will exist in the new platform along with their definitions and expected data types.

### Business Glossary
Defines common business terms used throughout the migration to ensure consistent terminology across business and technical teams.

### Critical Data Elements
Identifies high-priority fields that require additional validation because they have financial, operational, or regulatory importance.

### Source-to-Target Mapping
Serves as the core mapping document by linking every source field to its corresponding target field while documenting transformation logic and ownership.

### Transformation Rules
Documents the business logic required to convert source values into the format expected by the target system.

### Code Lookup Crosswalk
Maps legacy codes and values to their standardized target equivalents.

### Data Quality Rules
Defines validation rules used to identify incomplete, invalid, or inconsistent data before migration.

### Reconciliation Rules
Defines how migrated data will be verified after migration to ensure completeness and accuracy.

### Issues & Decisions Log
Tracks open issues, project decisions, owners, priorities, and current status.

### Signoff Tracker
Records business and technical approvals required before migration activities can proceed.

### Lists
Stores controlled values used for drop-down menus and standardized entries throughout the workbook.

## Python Automation

This project uses Python and pandas to:

- Read every worksheet in the workbook.
- Perform automated quality checks on the Source-to-Target Mapping worksheet.
- Detect missing values and duplicate mappings.
- Generate Excel reports containing identified issues.
- Create a summary report showing the number of issues found for each quality check.