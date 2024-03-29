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


class NewFedTax(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            amount = schemas.NumberSchema
            exemptions = schemas.NumberSchema
            filingStatus = schemas.StrSchema
            percentage = schemas.NumberSchema
            taxCalcCode = schemas.StrSchema
            tCode = schemas.StrSchema
            __annotations__ = {
                "amount": amount,
                "exemptions": exemptions,
                "filingStatus": filingStatus,
                "percentage": percentage,
                "taxCalcCode": taxCalcCode,
                "tCode": tCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exemptions"]) -> MetaOapg.properties.exemptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filingStatus"]) -> MetaOapg.properties.filingStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percentage"]) -> MetaOapg.properties.percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalcCode"]) -> MetaOapg.properties.taxCalcCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tCode"]) -> MetaOapg.properties.tCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "exemptions", "filingStatus", "percentage", "taxCalcCode", "tCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exemptions"]) -> typing.Union[MetaOapg.properties.exemptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filingStatus"]) -> typing.Union[MetaOapg.properties.filingStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percentage"]) -> typing.Union[MetaOapg.properties.percentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalcCode"]) -> typing.Union[MetaOapg.properties.taxCalcCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tCode"]) -> typing.Union[MetaOapg.properties.tCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "exemptions", "filingStatus", "percentage", "taxCalcCode", "tCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        exemptions: typing.Union[MetaOapg.properties.exemptions, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        filingStatus: typing.Union[MetaOapg.properties.filingStatus, str, schemas.Unset] = schemas.unset,
        percentage: typing.Union[MetaOapg.properties.percentage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        taxCalcCode: typing.Union[MetaOapg.properties.taxCalcCode, str, schemas.Unset] = schemas.unset,
        tCode: typing.Union[MetaOapg.properties.tCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewFedTax':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            exemptions=exemptions,
            filingStatus=filingStatus,
            percentage=percentage,
            taxCalcCode=taxCalcCode,
            tCode=tCode,
            _configuration=_configuration,
            **kwargs,
        )
