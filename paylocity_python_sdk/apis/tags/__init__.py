# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from paylocity_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    LOCAL_TAX = "Local Tax"
    EARNINGS = "Earnings"
    DEDUCTION = "Deduction"
    EMPLOYEE = "Employee"
    LOCAL_TAXES = "Local Taxes"
    PAY_STATEMENTS = "PayStatements"
    EMPLOYEE_V1 = "Employee (v1)"
    SENSITIVE_DATA = "Sensitive Data"
    ONBOARDING = "Onboarding"
    ADDITIONAL_RATES = "Additional Rates"
    CLIENT_CREDENTIALS = "Client Credentials"
    COMPANY_CODES = "Company Codes"
    COMPANYSPECIFIC_SCHEMA = "Company-Specific Schema"
    CUSTOM_FIELDS = "Custom Fields"
    DIRECT_DEPOSIT = "Direct Deposit"
    EMERGENCY_CONTACTS = "Emergency Contacts"
    EMPLOYEE_BENEFIT_SETUP = "Employee Benefit Setup"
    EMPLOYEE_STAGING = "Employee Staging"
    NONPRIMARY_STATE_TAX = "Non-Primary State Tax"
    PRIMARY_STATE_TAX = "Primary State Tax"
