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


class PayStatementSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The pay statement summary model
    """


    class MetaOapg:
        
        class properties:
            autoPay = schemas.BoolSchema
            beginDate = schemas.DictSchema
            checkDate = schemas.DictSchema
            checkNumber = schemas.IntSchema
            directDepositAmount = schemas.DictSchema
            endDate = schemas.DictSchema
            grossPay = schemas.DictSchema
            hours = schemas.DictSchema
            netCheck = schemas.DictSchema
            netPay = schemas.DictSchema
            overtimeDollars = schemas.DictSchema
            overtimeHours = schemas.DictSchema
            process = schemas.IntSchema
            regularDollars = schemas.DictSchema
            regularHours = schemas.DictSchema
            transactionNumber = schemas.IntSchema
            voucherNumber = schemas.IntSchema
            workersCompCode = schemas.DictSchema
            year = schemas.IntSchema
            __annotations__ = {
                "autoPay": autoPay,
                "beginDate": beginDate,
                "checkDate": checkDate,
                "checkNumber": checkNumber,
                "directDepositAmount": directDepositAmount,
                "endDate": endDate,
                "grossPay": grossPay,
                "hours": hours,
                "netCheck": netCheck,
                "netPay": netPay,
                "overtimeDollars": overtimeDollars,
                "overtimeHours": overtimeHours,
                "process": process,
                "regularDollars": regularDollars,
                "regularHours": regularHours,
                "transactionNumber": transactionNumber,
                "voucherNumber": voucherNumber,
                "workersCompCode": workersCompCode,
                "year": year,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoPay"]) -> MetaOapg.properties.autoPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beginDate"]) -> MetaOapg.properties.beginDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkDate"]) -> MetaOapg.properties.checkDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkNumber"]) -> MetaOapg.properties.checkNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directDepositAmount"]) -> MetaOapg.properties.directDepositAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grossPay"]) -> MetaOapg.properties.grossPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netCheck"]) -> MetaOapg.properties.netCheck: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netPay"]) -> MetaOapg.properties.netPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtimeDollars"]) -> MetaOapg.properties.overtimeDollars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtimeHours"]) -> MetaOapg.properties.overtimeHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["process"]) -> MetaOapg.properties.process: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regularDollars"]) -> MetaOapg.properties.regularDollars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regularHours"]) -> MetaOapg.properties.regularHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionNumber"]) -> MetaOapg.properties.transactionNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voucherNumber"]) -> MetaOapg.properties.voucherNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workersCompCode"]) -> MetaOapg.properties.workersCompCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["autoPay", "beginDate", "checkDate", "checkNumber", "directDepositAmount", "endDate", "grossPay", "hours", "netCheck", "netPay", "overtimeDollars", "overtimeHours", "process", "regularDollars", "regularHours", "transactionNumber", "voucherNumber", "workersCompCode", "year", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoPay"]) -> typing.Union[MetaOapg.properties.autoPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beginDate"]) -> typing.Union[MetaOapg.properties.beginDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkDate"]) -> typing.Union[MetaOapg.properties.checkDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkNumber"]) -> typing.Union[MetaOapg.properties.checkNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directDepositAmount"]) -> typing.Union[MetaOapg.properties.directDepositAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grossPay"]) -> typing.Union[MetaOapg.properties.grossPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> typing.Union[MetaOapg.properties.hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netCheck"]) -> typing.Union[MetaOapg.properties.netCheck, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netPay"]) -> typing.Union[MetaOapg.properties.netPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtimeDollars"]) -> typing.Union[MetaOapg.properties.overtimeDollars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtimeHours"]) -> typing.Union[MetaOapg.properties.overtimeHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["process"]) -> typing.Union[MetaOapg.properties.process, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regularDollars"]) -> typing.Union[MetaOapg.properties.regularDollars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regularHours"]) -> typing.Union[MetaOapg.properties.regularHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionNumber"]) -> typing.Union[MetaOapg.properties.transactionNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voucherNumber"]) -> typing.Union[MetaOapg.properties.voucherNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workersCompCode"]) -> typing.Union[MetaOapg.properties.workersCompCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> typing.Union[MetaOapg.properties.year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["autoPay", "beginDate", "checkDate", "checkNumber", "directDepositAmount", "endDate", "grossPay", "hours", "netCheck", "netPay", "overtimeDollars", "overtimeHours", "process", "regularDollars", "regularHours", "transactionNumber", "voucherNumber", "workersCompCode", "year", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        autoPay: typing.Union[MetaOapg.properties.autoPay, bool, schemas.Unset] = schemas.unset,
        beginDate: typing.Union[MetaOapg.properties.beginDate, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        checkDate: typing.Union[MetaOapg.properties.checkDate, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        checkNumber: typing.Union[MetaOapg.properties.checkNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        directDepositAmount: typing.Union[MetaOapg.properties.directDepositAmount, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        grossPay: typing.Union[MetaOapg.properties.grossPay, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        hours: typing.Union[MetaOapg.properties.hours, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        netCheck: typing.Union[MetaOapg.properties.netCheck, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        netPay: typing.Union[MetaOapg.properties.netPay, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        overtimeDollars: typing.Union[MetaOapg.properties.overtimeDollars, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        overtimeHours: typing.Union[MetaOapg.properties.overtimeHours, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        process: typing.Union[MetaOapg.properties.process, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        regularDollars: typing.Union[MetaOapg.properties.regularDollars, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        regularHours: typing.Union[MetaOapg.properties.regularHours, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        transactionNumber: typing.Union[MetaOapg.properties.transactionNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        voucherNumber: typing.Union[MetaOapg.properties.voucherNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        workersCompCode: typing.Union[MetaOapg.properties.workersCompCode, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        year: typing.Union[MetaOapg.properties.year, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayStatementSummary':
        return super().__new__(
            cls,
            *args,
            autoPay=autoPay,
            beginDate=beginDate,
            checkDate=checkDate,
            checkNumber=checkNumber,
            directDepositAmount=directDepositAmount,
            endDate=endDate,
            grossPay=grossPay,
            hours=hours,
            netCheck=netCheck,
            netPay=netPay,
            overtimeDollars=overtimeDollars,
            overtimeHours=overtimeHours,
            process=process,
            regularDollars=regularDollars,
            regularHours=regularHours,
            transactionNumber=transactionNumber,
            voucherNumber=voucherNumber,
            workersCompCode=workersCompCode,
            year=year,
            _configuration=_configuration,
            **kwargs,
        )
