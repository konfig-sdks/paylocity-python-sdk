# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from paylocity_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_EMPLOYEE = "/v1/employee"
    V1_COMPANY_COMPANY_ID_EMPLOYEE_EMPLOYEE_ID = "/v1/company/{companyId}/employee/{employeeId}"
    V1_UPDATEEMPLOYEE = "/v1/update-employee"
    V1_DEDUCTION = "/v1/deduction"
    V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_DEDUCTIONS_DEDUCTION_CODE_START_DATE = "/v1/companies/{companyId}/employees/{employeeId}/deductions/{deductionCode}/{startDate}"
    V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_DEDUCTIONS = "/v1/companies/{companyId}/employees/{employeeId}/deductions"
    V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_DEDUCTIONS_DEDUCTION_CODE = "/v1/companies/{companyId}/employees/{employeeId}/deductions/{deductionCode}"
    V1_COMPANIES_COMPANY_ID_ONBOARDING_EMPLOYEES = "/v1/companies/{companyId}/onboarding/employees"
    V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_LOCAL_TAXES_TAX_CODE = "/v1/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}"
    V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_LOCAL_TAXES = "/v1/companies/{companyId}/employees/{employeeId}/localTaxes"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_ADDITIONAL_RATES = "/v2/companies/{companyId}/employees/{employeeId}/additionalRates"
    V2_CREDENTIALS_SECRETS = "/v2/credentials/secrets"
    V2_COMPANIES_COMPANY_ID_CODES_CODE_RESOURCE = "/v2/companies/{companyId}/codes/{codeResource}"
    V2_COMPANIES_COMPANY_ID_OPENAPI = "/v2/companies/{companyId}/openapi"
    V2_COMPANIES_COMPANY_ID_CUSTOMFIELDS_CATEGORY = "/v2/companies/{companyId}/customfields/{category}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_DIRECT_DEPOSIT = "/v2/companies/{companyId}/employees/{employeeId}/directDeposit"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_EARNINGS = "/v2/companies/{companyId}/employees/{employeeId}/earnings"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_EARNINGS_EARNING_CODE_START_DATE = "/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_EARNINGS_EARNING_CODE = "/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_EMERGENCY_CONTACTS = "/v2/companies/{companyId}/employees/{employeeId}/emergencyContacts"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_BENEFIT_SETUP = "/v2/companies/{companyId}/employees/{employeeId}/benefitSetup"
    V2_WEBLINKSTAGING_COMPANIES_COMPANY_ID_EMPLOYEES_NEWEMPLOYEES = "/v2/weblinkstaging/companies/{companyId}/employees/newemployees"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES = "/v2/companies/{companyId}/employees"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID = "/v2/companies/{companyId}/employees/{employeeId}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_LOCAL_TAXES = "/v2/companies/{companyId}/employees/{employeeId}/localTaxes"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_LOCAL_TAXES_TAX_CODE = "/v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_NONPRIMARY_STATE_TAX = "/v2/companies/{companyId}/employees/{employeeId}/nonprimaryStateTax"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PAYSTATEMENT_DETAILS_YEAR_CHECK_DATE = "/v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}/{checkDate}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PAYSTATEMENT_DETAILS_YEAR = "/v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PAYSTATEMENT_SUMMARY_YEAR_CHECK_DATE = "/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PAYSTATEMENT_SUMMARY_YEAR = "/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PRIMARY_STATE_TAX = "/v2/companies/{companyId}/employees/{employeeId}/primaryStateTax"
    V2_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_SENSITIVEDATA = "/v2/companies/{companyId}/employees/{employeeId}/sensitivedata"
