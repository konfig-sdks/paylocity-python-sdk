# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import paylocity_python_sdk
from paylocity_python_sdk.paths.v2_companies_company_id_employees_employee_id_earnings_earning_code_start_date import get
from paylocity_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2CompaniesCompanyIdEmployeesEmployeeIdEarningsEarningCodeStartDate(ApiTestMixin, unittest.TestCase):
    """
    V2CompaniesCompanyIdEmployeesEmployeeIdEarningsEarningCodeStartDate unit test stubs
        Get Earning by Earning Code and Start Date
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
