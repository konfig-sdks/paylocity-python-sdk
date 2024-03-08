# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from paylocity_python_sdk.paths.v2_companies_company_id_employees_employee_id_earnings.put import AddOrUpdateEarning
from paylocity_python_sdk.paths.v2_companies_company_id_employees_employee_id_earnings_earning_code_start_date.delete import DeleteByCodeAndStart
from paylocity_python_sdk.paths.v2_companies_company_id_employees_employee_id_earnings.get import GetAll
from paylocity_python_sdk.paths.v2_companies_company_id_employees_employee_id_earnings_earning_code_start_date.get import GetByCodeAndStart
from paylocity_python_sdk.paths.v2_companies_company_id_employees_employee_id_earnings_earning_code.get import GetByEarningCode
from paylocity_python_sdk.apis.tags.earnings_api_raw import EarningsApiRaw


class EarningsApi(
    AddOrUpdateEarning,
    DeleteByCodeAndStart,
    GetAll,
    GetByCodeAndStart,
    GetByEarningCode,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EarningsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EarningsApiRaw(api_client)