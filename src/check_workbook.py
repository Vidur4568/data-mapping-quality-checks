import pandas as pd

# Import the quality check functions from the quality_checks.py
from quality_checks import (
    check_missing_source_field,
    check_missing_target_field,
    check_missing_transformation_rule,
    check_missing_status,
    check_missing_owner,
    check_duplicate_source_mappings
)
# File path to the workbook
workbook_path = "input/sample_data_mapping_workbook.xlsx"

# Open workbook toaccess all worksheet names
workbook = pd.ExcelFile(workbook_path)

try:
    # Print a header 
    print("=" * 60)
    print("DATA MAPPING WORKBOOK SUMMARY")
    print("=" * 60)

    # Loop through every worksheet in the workbook
    for sheet in workbook.sheet_names:
        df = pd.read_excel(workbook_path, sheet_name=sheet)
        
        # Display the worksheet name, number of rows, and number of columns
        print(f"\nWorksheet: {sheet}")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")
    # Print a success message after successfully loading the workbook
    print("\nWorkbook loaded successfully!")
# Display a message if workbook is not found 
except FileNotFoundError:
    print("Workbook not found.")
# Catch any other errors and siplay the error message
except Exception as e:
    print("Error:", e)

print("\n" + "=" * 60)
print("SOURCE TO TARGET MAPPING QUALITY CHECKS")
print("=" * 60)

# Read the Source to Target Mapping worksheet into a DataFrame
mapping = pd.read_excel(
    workbook_path,
    sheet_name="Source-to-Target Mapping",
    header=3
)

# Remove completely blank rows
mapping = mapping.dropna(how="all")


# Run each quality check function
missing_source = check_missing_source_field(mapping)
missing_target = check_missing_target_field(mapping)
missing_transformation = check_missing_transformation_rule(mapping)
missing_status = check_missing_status(mapping)
missing_owner = check_missing_owner(mapping)
duplicate_source_mappings = check_duplicate_source_mappings(mapping)

# Save rows with missing source fields
missing_source.to_excel(
    "output/missing_source_fields.xlsx",
    index=False
)

# Save rows with missing target fields
missing_target.to_excel(
    "output/missing_target_fields.xlsx",
    index=False
)

# Save rows with missing transformation rules
missing_transformation.to_excel(
    "output/missing_transformation_rules.xlsx",
    index=False
)

# Save rows with missing mapping status
missing_status.to_excel(
    "output/missing_status.xlsx",
    index=False
)

# Save rows with missing SME owners
missing_owner.to_excel(
    "output/missing_owner.xlsx",
    index=False
)

# Save duplicate source mappings
duplicate_source_mappings.to_excel(
    "output/duplicate_source_mappings.xlsx",
    index=False
)

summary = pd.DataFrame({
    "Quality Check": [
        "Missing Source Fields",
        "Missing Target Fields",
        "Missing Transformation Rules",
        "Missing Status",
        "Missing SME Owner",
        "Duplicate Source Mappings"
    ],
    "Issues Found": [
        len(missing_source),
        len(missing_target),
        len(missing_transformation),
        len(missing_status),
        len(missing_owner),
        len(duplicate_source_mappings)
    ]
})

# Save the summary report
summary.to_excel(
    "output/mapping_summary_report.xlsx",
    index=False
)

print("Summary report saved!")

# Print a confirmation message after all reports have been successfully saved
print("\nQuality check reports saved to the output folder!")

# Display the number of issues found for each check
print("Missing source fields:" , len(missing_source))
print("Missing target fields:" , len(missing_target))
print("Missing transformation rules:" , len(missing_transformation))
print("Missing status fields:" , len(missing_status))
print("Missing owner fields:" , len(missing_owner))
print("Duplicate source mappings:" , len(duplicate_source_mappings))