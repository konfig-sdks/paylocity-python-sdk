# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from paylocity_python_sdk import schemas  # noqa: F401


class ErrorsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            Path = schemas.StrSchema
            field = schemas.StrSchema
            message = schemas.StrSchema
        
            @staticmethod
            def options() -> typing.Type['ErrorsItemOptions']:
                return ErrorsItemOptions
            __annotations__ = {
                "Path": Path,
                "field": field,
                "message": message,
                "options": options,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Path"]) -> MetaOapg.properties.Path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field"]) -> MetaOapg.properties.field: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'ErrorsItemOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Path", "field", "message", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Path"]) -> typing.Union[MetaOapg.properties.Path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field"]) -> typing.Union[MetaOapg.properties.field, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['ErrorsItemOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Path", "field", "message", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Path: typing.Union[MetaOapg.properties.Path, str, schemas.Unset] = schemas.unset,
        field: typing.Union[MetaOapg.properties.field, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        options: typing.Union['ErrorsItemOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ErrorsItem':
        return super().__new__(
            cls,
            *args,
            Path=Path,
            field=field,
            message=message,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from paylocity_python_sdk.model.errors_item_options import ErrorsItemOptions
