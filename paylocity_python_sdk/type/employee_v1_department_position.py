# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredEmployeeV1DepartmentPosition(TypedDict):
    pass

class OptionalEmployeeV1DepartmentPosition(TypedDict, total=False):
    # Employer defined location, like *branch, division, department*, etc. Must match Company setup. <br  />Max length: 10
    costCenter1: str

    # Employer defined location, like *branch, division, department*, etc. Must match Company setup. <br  />Max length: 10
    costCenter2: str

    # Employer defined location, like *branch, division, department*, etc. Must match Company setup. <br  />Max length: 10
    costCenter3: str

    # Employee current employment type. Common values *RFT (Regular Full Time), RPT (Regular Part Time), SNL (Seasonal), TFT (Temporary Full Time), TPT (Temporary Part Time)*. <br  />Max length: 10
    employeeType: str

    # Values are configured in Company > Setup > HR > EEO Classes.<br  /> Max length: 10
    equalEmploymentOpportunityClass: str

    # Employee current job title. <br  />Max length: 50
    jobTitle: str

    # Employee pay group. Must match Company setup. <br  /> Max length: 20
    payGroup: str

class EmployeeV1DepartmentPosition(RequiredEmployeeV1DepartmentPosition, OptionalEmployeeV1DepartmentPosition):
    pass