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


class RequiredErrorOptionsItem(TypedDict):
    pass

class OptionalErrorOptionsItem(TypedDict, total=False):
    # The description of the option.
    description: str

    # The code associated with this option.
    code: str

class ErrorOptionsItem(RequiredErrorOptionsItem, OptionalErrorOptionsItem):
    pass
