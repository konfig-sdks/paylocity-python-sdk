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


class RequiredClientCredentialsResponse(TypedDict):
    pass

class OptionalClientCredentialsResponse(TypedDict, total=False):
    # The client's secret
    clientSecret: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The client's secret expiration date
    clientSecretExpirationDate: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class ClientCredentialsResponse(RequiredClientCredentialsResponse, OptionalClientCredentialsResponse):
    pass