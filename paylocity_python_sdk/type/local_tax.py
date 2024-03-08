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


class RequiredLocalTax(TypedDict):
    pass

class OptionalLocalTax(TypedDict, total=False):
    # Local tax exemptions value.<br  />Decimal (12,2)
    exemptions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Local tax exemptions 2 value.<br  />Decimal (12,2)
    exemptions2: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee local tax filing status. Must match specific local tax setup. <br  /> Max length: 50
    filingStatus: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Resident PSD (political subdivision code) applicable in PA. Must match Company setup.<br  /> Max length: 9
    residentPSD: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Local tax code.<br  />Max length: 50
    taxCode: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Work location PSD. Must match Company setup. <br  /> Max length: 9
    workPSD: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class LocalTax(RequiredLocalTax, OptionalLocalTax):
    pass
