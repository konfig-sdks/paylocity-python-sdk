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


class PrimaryPayRate(BaseModel):
    # If set to *True*, employee will be paid automatically using deafultHours. 
    auto_pay: typing.Optional[bool] = Field(None, alias='autoPay')

    # Employee base rate, used for Hourly employees. <br  />Decimal (12,2)
    base_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseRate')

    # Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. <br  />Decimal (12,2)
    default_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='defaultHours')

    # The date the employee’s pay rate takes effect. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
    effective_date: typing.Optional[date] = Field(None, alias='effectiveDate')

    # Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. <br  />Max length: 5
    pay_frequency: typing.Optional[str] = Field(None, alias='payFrequency')

    # Employee pay grade. Must match Company setup. <br  /> Max length: 10
    pay_grade: typing.Optional[str] = Field(None, alias='payGrade')

    # Employee pay type (rate code). Valid values are *Hourly* or *Salary*. <br  />Max length: 10
    pay_type: typing.Optional[str] = Field(None, alias='payType')

    # Employee base rate frequency used with payType Hourly. Common values are *Hour, Week*. Default is Hour. <br  />Max length: 10
    rate_per: typing.Optional[str] = Field(None, alias='ratePer')

    # Primary Pay Rate change reason. Must match Company setup.<br  />Max length: 15
    reason: typing.Optional[str] = Field(None, alias='reason')

    # Employee gross salary per pay period used with payType Salary.<br  />Decimal (12,2)
    salary: typing.Optional[typing.Union[int, float]] = Field(None, alias='salary')
    class Config:
        arbitrary_types_allowed = True