# Functions for checking whcih rows need reviewing in the data mapping workbook

def check_missing_source_field(mapping):
    return mapping[mapping["Source Field"].isna()]

def check_missing_target_field(mapping):
    return mapping[mapping["Target Field"].isna()]

def check_missing_transformation_rule(mapping):
    return mapping[mapping["Transformation Rule ID"].isna()]

def check_missing_status(mapping):
    return mapping[mapping["Mapping Status"].isna()]

def check_missing_owner(mapping):
    return mapping[mapping["SME Owner"].isna()]

def check_duplicate_source_mappings(mapping):
    return mapping[
        mapping.duplicated(
            subset=["Source Table/Object", "Source Field"],
            keep=False
        )
    ]