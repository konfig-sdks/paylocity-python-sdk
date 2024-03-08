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

from paylocity_python_sdk.type.direct_deposit_additional_direct_deposit import DirectDepositAdditionalDirectDeposit

class RequiredDirectDeposit(TypedDict):
    pass

class OptionalDirectDeposit(TypedDict, total=False):
    additionalDirectDeposit: DirectDepositAdditionalDirectDeposit

    # The main Direct Deposit account.
    mainDirectDeposit: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class DirectDeposit(RequiredDirectDeposit, OptionalDirectDeposit):
    pass