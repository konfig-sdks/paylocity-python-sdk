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


class CustomFieldDefinition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            category = schemas.StrSchema
            defaultValue = schemas.StrSchema
            isRequired = schemas.BoolSchema
            label = schemas.StrSchema
            type = schemas.StrSchema
        
            @staticmethod
            def values() -> typing.Type['CustomFieldDefinitionValues']:
                return CustomFieldDefinitionValues
            __annotations__ = {
                "category": category,
                "defaultValue": defaultValue,
                "isRequired": isRequired,
                "label": label,
                "type": type,
                "values": values,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultValue"]) -> MetaOapg.properties.defaultValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isRequired"]) -> MetaOapg.properties.isRequired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values"]) -> 'CustomFieldDefinitionValues': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["category", "defaultValue", "isRequired", "label", "type", "values", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultValue"]) -> typing.Union[MetaOapg.properties.defaultValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isRequired"]) -> typing.Union[MetaOapg.properties.isRequired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> typing.Union['CustomFieldDefinitionValues', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["category", "defaultValue", "isRequired", "label", "type", "values", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        defaultValue: typing.Union[MetaOapg.properties.defaultValue, str, schemas.Unset] = schemas.unset,
        isRequired: typing.Union[MetaOapg.properties.isRequired, bool, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        values: typing.Union['CustomFieldDefinitionValues', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldDefinition':
        return super().__new__(
            cls,
            *args,
            category=category,
            defaultValue=defaultValue,
            isRequired=isRequired,
            label=label,
            type=type,
            values=values,
            _configuration=_configuration,
            **kwargs,
        )

from paylocity_python_sdk.model.custom_field_definition_values import CustomFieldDefinitionValues