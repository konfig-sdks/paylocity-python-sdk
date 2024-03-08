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

from paylocity_python_sdk.pydantic.error_options import ErrorOptions

class Error(BaseModel):
    # The name of the field, or property in the request message that contains an error.
    field: typing.Optional[str] = Field(None, alias='field')

    # The error message.
    message: typing.Optional[str] = Field(None, alias='message')

    options: typing.Optional[ErrorOptions] = Field(None, alias='options')

    # The JSON path of the field, or property, that contains an error in the request message.
    path: typing.Optional[str] = Field(None, alias='path')
    class Config:
        arbitrary_types_allowed = True