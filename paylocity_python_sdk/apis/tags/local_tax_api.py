# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_local_taxes.post import CreateOrUpdateLocalTaxes
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_local_taxes.get import GetAllTaxesForEmployee
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_local_taxes_tax_code.get import GetForTaxCode
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_local_taxes_tax_code.delete import RemoveForTaxCode
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_local_taxes_tax_code.put import UpdateForTaxCode
from paylocity_python_sdk.apis.tags.local_tax_api_raw import LocalTaxApiRaw


class LocalTaxApi(
    CreateOrUpdateLocalTaxes,
    GetAllTaxesForEmployee,
    GetForTaxCode,
    RemoveForTaxCode,
    UpdateForTaxCode,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LocalTaxApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LocalTaxApiRaw(api_client)
