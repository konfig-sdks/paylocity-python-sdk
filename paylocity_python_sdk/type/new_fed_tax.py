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


class RequiredNewFedTax(TypedDict):
    pass

class OptionalNewFedTax(TypedDict, total=False):
    # Tax amount. <br  />Decimal (12,2)
    amount: typing.Union[int, float]

    # Federal tax exemptions value. <br  />Decimal (12,2)
    exemptions: typing.Union[int, float]

    # Employee federal filing status. Common values are *S* (Single), *M* (Married).<br  />Max length: 50
    filingStatus: str

    # Tax percentage. <br  />Decimal (12,2)
    percentage: typing.Union[int, float]

    # Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). <br  />Max length: 10
    taxCalcCode: str

    # Tax code. <br  /> Max length: 50
    tCode: str

class NewFedTax(RequiredNewFedTax, OptionalNewFedTax):
    pass
