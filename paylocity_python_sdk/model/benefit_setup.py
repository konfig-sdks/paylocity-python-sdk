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


class BenefitSetup(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The benefit setup model
    """


    class MetaOapg:
        
        class properties:
            benefitClass = schemas.DictSchema
            benefitClassEffectiveDate = schemas.DictSchema
            benefitSalary = schemas.DictSchema
            benefitSalaryEffectiveDate = schemas.DictSchema
            doNotApplyAdministrativePeriod = schemas.DictSchema
            isMeasureAcaEligibility = schemas.DictSchema
            __annotations__ = {
                "benefitClass": benefitClass,
                "benefitClassEffectiveDate": benefitClassEffectiveDate,
                "benefitSalary": benefitSalary,
                "benefitSalaryEffectiveDate": benefitSalaryEffectiveDate,
                "doNotApplyAdministrativePeriod": doNotApplyAdministrativePeriod,
                "isMeasureAcaEligibility": isMeasureAcaEligibility,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefitClass"]) -> MetaOapg.properties.benefitClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefitClassEffectiveDate"]) -> MetaOapg.properties.benefitClassEffectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefitSalary"]) -> MetaOapg.properties.benefitSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefitSalaryEffectiveDate"]) -> MetaOapg.properties.benefitSalaryEffectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["doNotApplyAdministrativePeriod"]) -> MetaOapg.properties.doNotApplyAdministrativePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isMeasureAcaEligibility"]) -> MetaOapg.properties.isMeasureAcaEligibility: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["benefitClass", "benefitClassEffectiveDate", "benefitSalary", "benefitSalaryEffectiveDate", "doNotApplyAdministrativePeriod", "isMeasureAcaEligibility", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefitClass"]) -> typing.Union[MetaOapg.properties.benefitClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefitClassEffectiveDate"]) -> typing.Union[MetaOapg.properties.benefitClassEffectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefitSalary"]) -> typing.Union[MetaOapg.properties.benefitSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefitSalaryEffectiveDate"]) -> typing.Union[MetaOapg.properties.benefitSalaryEffectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["doNotApplyAdministrativePeriod"]) -> typing.Union[MetaOapg.properties.doNotApplyAdministrativePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isMeasureAcaEligibility"]) -> typing.Union[MetaOapg.properties.isMeasureAcaEligibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["benefitClass", "benefitClassEffectiveDate", "benefitSalary", "benefitSalaryEffectiveDate", "doNotApplyAdministrativePeriod", "isMeasureAcaEligibility", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        benefitClass: typing.Union[MetaOapg.properties.benefitClass, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        benefitClassEffectiveDate: typing.Union[MetaOapg.properties.benefitClassEffectiveDate, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        benefitSalary: typing.Union[MetaOapg.properties.benefitSalary, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        benefitSalaryEffectiveDate: typing.Union[MetaOapg.properties.benefitSalaryEffectiveDate, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        doNotApplyAdministrativePeriod: typing.Union[MetaOapg.properties.doNotApplyAdministrativePeriod, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        isMeasureAcaEligibility: typing.Union[MetaOapg.properties.isMeasureAcaEligibility, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BenefitSetup':
        return super().__new__(
            cls,
            *args,
            benefitClass=benefitClass,
            benefitClassEffectiveDate=benefitClassEffectiveDate,
            benefitSalary=benefitSalary,
            benefitSalaryEffectiveDate=benefitSalaryEffectiveDate,
            doNotApplyAdministrativePeriod=doNotApplyAdministrativePeriod,
            isMeasureAcaEligibility=isMeasureAcaEligibility,
            _configuration=_configuration,
            **kwargs,
        )
