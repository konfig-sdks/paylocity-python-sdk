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


class NewLocalTax(BaseModel):
    # Local tax code.<br  />Max length: 50
    t_code: typing.Optional[str] = Field(None, alias='tCode')

    # Local tax exemptions value.<br  />Decimal (12,2)
    exemptions: typing.Optional[typing.Union[int, float]] = Field(None, alias='exemptions')

    # Local tax exemptions 2 value.<br  />Decimal (12,2)
    exemptions2: typing.Optional[typing.Union[int, float]] = Field(None, alias='exemptions2')

    # Employee local tax filing status. Must match specific local tax setup. <br  /> Max length: 50
    filing_status: typing.Optional[str] = Field(None, alias='filingStatus')

    # Resident PSD (political subdivision code) applicable in PA. Must match Company setup.<br  /> Max length: 9
    resident_p_s_d: typing.Optional[str] = Field(None, alias='residentPSD')

    # Work location PSD. Must match Company setup. <br  /> Max length: 9
    work_p_s_d: typing.Optional[str] = Field(None, alias='workPSD')
    class Config:
        arbitrary_types_allowed = True
