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

from paylocity_python_sdk.type.new_employee import NewEmployee

class RequiredEmployeeV1CreateNewEmployeeRecordRequest(TypedDict):
    pass

class OptionalEmployeeV1CreateNewEmployeeRecordRequest(TypedDict, total=False):
    newEmployee: NewEmployee

class EmployeeV1CreateNewEmployeeRecordRequest(RequiredEmployeeV1CreateNewEmployeeRecordRequest, OptionalEmployeeV1CreateNewEmployeeRecordRequest):
    pass
