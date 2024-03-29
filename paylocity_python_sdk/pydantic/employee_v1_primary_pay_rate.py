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
from pydantic import BaseModel, Field, RootModel


class EmployeeV1PrimaryPayRate(BaseModel):
    # Employee annual salary. <br  />Decimal (12,2)
    annual_salary: typing.Optional[typing.Union[int, float]] = Field(None, alias='annualSalary')

    # Employee base rate, used for Hourly employees. <br  />Decimal (12,2)
    base_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseRate')

    # Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. <br  />Decimal (12,2)
    default_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='defaultHours')

    # Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. <br  />Max length: 5
    pay_frequency: typing.Optional[str] = Field(None, alias='payFrequency')

    # Employee pay type (rate code). Valid values are *Hourly* or *Salary*. <br  />Max length: 10
    pay_type: typing.Optional[str] = Field(None, alias='payType')

    # The date the employee’s pay rate takes effect. (MM-DD-CCYY)
    primary_pay_rate_effective_date: typing.Optional[str] = Field(None, alias='primaryPayRateEffectiveDate')

    # Employee gross salary per pay period used with payType Salary.<br  />Decimal (12,2)
    salary: typing.Optional[typing.Union[int, float]] = Field(None, alias='salary')
    class Config:
        arbitrary_types_allowed = True
