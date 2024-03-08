# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from paylocity_python_sdk.paths.v2_companies_company_id_employees_employee_id_primary_state_tax.put import AddOrUpdateTax
from paylocity_python_sdk.apis.tags.primary_state_tax_api_raw import PrimaryStateTaxApiRaw


class PrimaryStateTaxApi(
    AddOrUpdateTax,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PrimaryStateTaxApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PrimaryStateTaxApiRaw(api_client)