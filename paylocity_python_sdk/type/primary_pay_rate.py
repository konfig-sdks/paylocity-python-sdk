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


class RequiredPrimaryPayRate(TypedDict):
    pass

class OptionalPrimaryPayRate(TypedDict, total=False):
    # If set to *True*, employee will be paid automatically using deafultHours. 
    autoPay: bool

    # Employee base rate, used for Hourly employees. <br  />Decimal (12,2)
    baseRate: typing.Union[int, float]

    # Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. <br  />Decimal (12,2)
    defaultHours: typing.Union[int, float]

    # The date the employee’s pay rate takes effect. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
    effectiveDate: date

    # Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. <br  />Max length: 5
    payFrequency: str

    # Employee pay grade. Must match Company setup. <br  /> Max length: 10
    payGrade: str

    # Employee pay type (rate code). Valid values are *Hourly* or *Salary*. <br  />Max length: 10
    payType: str

    # Employee base rate frequency used with payType Hourly. Common values are *Hour, Week*. Default is Hour. <br  />Max length: 10
    ratePer: str

    # Primary Pay Rate change reason. Must match Company setup.<br  />Max length: 15
    reason: str

    # Employee gross salary per pay period used with payType Salary.<br  />Decimal (12,2)
    salary: typing.Union[int, float]

class PrimaryPayRate(RequiredPrimaryPayRate, OptionalPrimaryPayRate):
    pass
