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


class RequiredNonPrimaryStateTax(TypedDict):
    pass

class OptionalNonPrimaryStateTax(TypedDict, total=False):
    # State tax code.<br  /> Max length: 50
    amount: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Box 4(b) on form W4 (year 2020 or later): Deductions amount. <br  />Decimal (12,2)
    deductionsAmount: typing.Union[int, float]

    # Box 3 on form W4 (year 2020 or later): Total dependents amount. <br  />Decimal (12,2)
    dependentsAmount: typing.Union[int, float]

    # State tax exemptions value.<br  />Decimal (12,2)
    exemptions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # State tax exemptions 2 value.<br  />Decimal (12,2)
    exemptions2: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee state tax filing status. Common values are *S* (Single), *M* (Married).<br  />Max length: 50
    filingStatus: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Box 2(c) on form W4 (year 2020 or later): Multiple Jobs or Spouse Works. <br  />Boolean
    higherRate: bool

    # Box 4(a) on form W4 (year 2020 or later): Other income amount. <br  />Decimal (12,2)
    otherIncomeAmount: typing.Union[int, float]

    # State Tax percentage. <br  />Decimal (12,2)
    percentage: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Non-primary state tax reciprocity code.<br  /> Max length: 50
    reciprocityCode: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Supplemental check calculation code. Common values are *Blocked* (Taxes blocked on Supplemental checks), *Supp* (Use supplemental Tax Rate-Code). <br  />Max length: 10
    specialCheckCalc: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). <br  />Max length: 10
    taxCalculationCode: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # State tax code.<br  /> Max length: 50
    taxCode: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The state W4 form year <br  />Integer
    w4FormYear: int

class NonPrimaryStateTax(RequiredNonPrimaryStateTax, OptionalNonPrimaryStateTax):
    pass