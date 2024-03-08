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
from paylocity_python_sdk.paths.v1_companies_company_id_employees_employee_id_deductions_deduction_code_start_date import delete
from paylocity_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1CompaniesCompanyIdEmployeesEmployeeIdDeductionsDeductionCodeStartDate(ApiTestMixin, unittest.TestCase):
    """
    V1CompaniesCompanyIdEmployeesEmployeeIdDeductionsDeductionCodeStartDate unit test stubs
        Delete deduction for deduction code / start date
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204


if __name__ == '__main__':
    unittest.main()
