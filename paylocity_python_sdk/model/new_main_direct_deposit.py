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


class NewMainDirectDeposit(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            accountType = schemas.StrSchema
            routingNumber = schemas.StrSchema
            accountNumber = schemas.StrSchema
            blockSpecial = schemas.BoolSchema
            nameOnAccount = schemas.StrSchema
            skipPreNote = schemas.BoolSchema
            preNoteDate = schemas.DateSchema
            __annotations__ = {
                "accountType": accountType,
                "routingNumber": routingNumber,
                "accountNumber": accountNumber,
                "blockSpecial": blockSpecial,
                "nameOnAccount": nameOnAccount,
                "skipPreNote": skipPreNote,
                "preNoteDate": preNoteDate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routingNumber"]) -> MetaOapg.properties.routingNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNumber"]) -> MetaOapg.properties.accountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockSpecial"]) -> MetaOapg.properties.blockSpecial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameOnAccount"]) -> MetaOapg.properties.nameOnAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skipPreNote"]) -> MetaOapg.properties.skipPreNote: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preNoteDate"]) -> MetaOapg.properties.preNoteDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountType", "routingNumber", "accountNumber", "blockSpecial", "nameOnAccount", "skipPreNote", "preNoteDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountType"]) -> typing.Union[MetaOapg.properties.accountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routingNumber"]) -> typing.Union[MetaOapg.properties.routingNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNumber"]) -> typing.Union[MetaOapg.properties.accountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockSpecial"]) -> typing.Union[MetaOapg.properties.blockSpecial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameOnAccount"]) -> typing.Union[MetaOapg.properties.nameOnAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skipPreNote"]) -> typing.Union[MetaOapg.properties.skipPreNote, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preNoteDate"]) -> typing.Union[MetaOapg.properties.preNoteDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountType", "routingNumber", "accountNumber", "blockSpecial", "nameOnAccount", "skipPreNote", "preNoteDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accountType: typing.Union[MetaOapg.properties.accountType, str, schemas.Unset] = schemas.unset,
        routingNumber: typing.Union[MetaOapg.properties.routingNumber, str, schemas.Unset] = schemas.unset,
        accountNumber: typing.Union[MetaOapg.properties.accountNumber, str, schemas.Unset] = schemas.unset,
        blockSpecial: typing.Union[MetaOapg.properties.blockSpecial, bool, schemas.Unset] = schemas.unset,
        nameOnAccount: typing.Union[MetaOapg.properties.nameOnAccount, str, schemas.Unset] = schemas.unset,
        skipPreNote: typing.Union[MetaOapg.properties.skipPreNote, bool, schemas.Unset] = schemas.unset,
        preNoteDate: typing.Union[MetaOapg.properties.preNoteDate, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewMainDirectDeposit':
        return super().__new__(
            cls,
            *args,
            accountType=accountType,
            routingNumber=routingNumber,
            accountNumber=accountNumber,
            blockSpecial=blockSpecial,
            nameOnAccount=nameOnAccount,
            skipPreNote=skipPreNote,
            preNoteDate=preNoteDate,
            _configuration=_configuration,
            **kwargs,
        )
