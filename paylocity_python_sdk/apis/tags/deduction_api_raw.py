# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from paylocity_python_sdk.paths.v1_deduction.post import AddOrUpdateDeductionRaw
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_deductions.get import GetAllDeductionsRaw
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_deductions_deduction_code.get import GetByCodeRaw
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_deductions_deduction_code_start_date.delete import RemoveDeductionByCodeAndStartDateRaw


class DeductionApiRaw(
    AddOrUpdateDeductionRaw,
    GetAllDeductionsRaw,
    GetByCodeRaw,
    RemoveDeductionByCodeAndStartDateRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
