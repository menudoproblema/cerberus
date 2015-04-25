"""
This module contains the error messages issued by the Cerberus Validator.
The test suite uses this module as well.
"""
defaults = {
    'schema_missing': "validation schema missing",
    'schema_format': "'%s' is not a schema, must be a dict",
    'schema_type': "type of field '%s' must be either 'list' or 'dict'",
    'document_missing': "document is missing",
    'document_format': "'%s' is not a document, must be a dict",
    'unknown_rule': "unknown rule '%s' for field '%s'",
    'definition_format': "schema definition for field '%s' must be a dict",
    'unknown_field': "unknown field",
    'required_field': "required field",
    'unknown_type': "unrecognized data-type '%s'",
    'bad_type': "must be of %s type",
    'min_length': "min length is %d",
    'max_length': "max length is %d",
    'unallowed_values': "unallowed values %s",
    'unallowed_value': "unallowed value %s",
    'items_list': "length of list should be %d",
    'readonly_field': "field is read-only",
    'max_value': "max value is %d",
    'min_value': "min value is %d",
    'empty_not_allowed': "empty values not allowed",
    'not_nullable': "null value not allowed",
    'regex': "value does not match regex '%s'",
    'dependencies_field': "field '%s' is required",
    'dependencies_field_value': "field '%s' is required with values: %s",
}
