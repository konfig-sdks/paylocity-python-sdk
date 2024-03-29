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


class NewFedTax(BaseModel):
    # Tax amount. <br  />Decimal (12,2)
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Federal tax exemptions value. <br  />Decimal (12,2)
    exemptions: typing.Optional[typing.Union[int, float]] = Field(None, alias='exemptions')

    # Employee federal filing status. Common values are *S* (Single), *M* (Married).<br  />Max length: 50
    filing_status: typing.Optional[str] = Field(None, alias='filingStatus')

    # Tax percentage. <br  />Decimal (12,2)
    percentage: typing.Optional[typing.Union[int, float]] = Field(None, alias='percentage')

    # Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). <br  />Max length: 10
    tax_calc_code: typing.Optional[str] = Field(None, alias='taxCalcCode')

    # Tax code. <br  /> Max length: 50
    t_code: typing.Optional[str] = Field(None, alias='tCode')
    class Config:
        arbitrary_types_allowed = True
