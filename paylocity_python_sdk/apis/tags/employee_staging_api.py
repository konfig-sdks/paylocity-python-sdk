# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from paylocity_python_sdk.paths.v2_weblinkstaging_companies_company_id_employees_newemployees.post import AddNewEmployeeToWebLink
from paylocity_python_sdk.apis.tags.employee_staging_api_raw import EmployeeStagingApiRaw


class EmployeeStagingApi(
    AddNewEmployeeToWebLink,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EmployeeStagingApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EmployeeStagingApiRaw(api_client)
