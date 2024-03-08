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


class Onboarding(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "firstName",
            "lastName",
        }
        
        class properties:
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            employeeId = schemas.StrSchema
            address1 = schemas.StrSchema
            address2 = schemas.StrSchema
            autoPayType = schemas.StrSchema
            baseRate = schemas.NumberSchema
            city = schemas.StrSchema
            costCenter1 = schemas.StrSchema
            costCenter2 = schemas.StrSchema
            costCenter3 = schemas.StrSchema
            defaultHours = schemas.NumberSchema
            employeeStatus = schemas.StrSchema
            employmentType = schemas.StrSchema
            federalFilingStatus = schemas.StrSchema
            sex = schemas.StrSchema
            hireDate = schemas.StrSchema
            homePhone = schemas.StrSchema
            maritalStatus = schemas.StrSchema
            personalMobilePhone = schemas.StrSchema
            payFrequency = schemas.StrSchema
            personalEmailAddress = schemas.StrSchema
            payType = schemas.StrSchema
            ratePer = schemas.StrSchema
            salary = schemas.NumberSchema
            state = schemas.StrSchema
            ssn = schemas.StrSchema
            stateFilingStatus = schemas.StrSchema
            suiState = schemas.StrSchema
            taxForm = schemas.StrSchema
            taxState = schemas.StrSchema
            userName = schemas.StrSchema
            workEmailAddress = schemas.StrSchema
            zip = schemas.StrSchema
            __annotations__ = {
                "firstName": firstName,
                "lastName": lastName,
                "employeeId": employeeId,
                "address1": address1,
                "address2": address2,
                "autoPayType": autoPayType,
                "baseRate": baseRate,
                "city": city,
                "costCenter1": costCenter1,
                "costCenter2": costCenter2,
                "costCenter3": costCenter3,
                "defaultHours": defaultHours,
                "employeeStatus": employeeStatus,
                "employmentType": employmentType,
                "federalFilingStatus": federalFilingStatus,
                "sex": sex,
                "hireDate": hireDate,
                "homePhone": homePhone,
                "maritalStatus": maritalStatus,
                "personalMobilePhone": personalMobilePhone,
                "payFrequency": payFrequency,
                "personalEmailAddress": personalEmailAddress,
                "payType": payType,
                "ratePer": ratePer,
                "salary": salary,
                "state": state,
                "ssn": ssn,
                "stateFilingStatus": stateFilingStatus,
                "suiState": suiState,
                "taxForm": taxForm,
                "taxState": taxState,
                "userName": userName,
                "workEmailAddress": workEmailAddress,
                "zip": zip,
            }
    
    firstName: MetaOapg.properties.firstName
    lastName: MetaOapg.properties.lastName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address1"]) -> MetaOapg.properties.address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address2"]) -> MetaOapg.properties.address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoPayType"]) -> MetaOapg.properties.autoPayType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseRate"]) -> MetaOapg.properties.baseRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCenter1"]) -> MetaOapg.properties.costCenter1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCenter2"]) -> MetaOapg.properties.costCenter2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCenter3"]) -> MetaOapg.properties.costCenter3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultHours"]) -> MetaOapg.properties.defaultHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeStatus"]) -> MetaOapg.properties.employeeStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employmentType"]) -> MetaOapg.properties.employmentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["federalFilingStatus"]) -> MetaOapg.properties.federalFilingStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sex"]) -> MetaOapg.properties.sex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hireDate"]) -> MetaOapg.properties.hireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["homePhone"]) -> MetaOapg.properties.homePhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maritalStatus"]) -> MetaOapg.properties.maritalStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalMobilePhone"]) -> MetaOapg.properties.personalMobilePhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payFrequency"]) -> MetaOapg.properties.payFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalEmailAddress"]) -> MetaOapg.properties.personalEmailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payType"]) -> MetaOapg.properties.payType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratePer"]) -> MetaOapg.properties.ratePer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary"]) -> MetaOapg.properties.salary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateFilingStatus"]) -> MetaOapg.properties.stateFilingStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suiState"]) -> MetaOapg.properties.suiState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxForm"]) -> MetaOapg.properties.taxForm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxState"]) -> MetaOapg.properties.taxState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workEmailAddress"]) -> MetaOapg.properties.workEmailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "employeeId", "address1", "address2", "autoPayType", "baseRate", "city", "costCenter1", "costCenter2", "costCenter3", "defaultHours", "employeeStatus", "employmentType", "federalFilingStatus", "sex", "hireDate", "homePhone", "maritalStatus", "personalMobilePhone", "payFrequency", "personalEmailAddress", "payType", "ratePer", "salary", "state", "ssn", "stateFilingStatus", "suiState", "taxForm", "taxState", "userName", "workEmailAddress", "zip", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address1"]) -> typing.Union[MetaOapg.properties.address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address2"]) -> typing.Union[MetaOapg.properties.address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoPayType"]) -> typing.Union[MetaOapg.properties.autoPayType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseRate"]) -> typing.Union[MetaOapg.properties.baseRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCenter1"]) -> typing.Union[MetaOapg.properties.costCenter1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCenter2"]) -> typing.Union[MetaOapg.properties.costCenter2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCenter3"]) -> typing.Union[MetaOapg.properties.costCenter3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultHours"]) -> typing.Union[MetaOapg.properties.defaultHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeStatus"]) -> typing.Union[MetaOapg.properties.employeeStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employmentType"]) -> typing.Union[MetaOapg.properties.employmentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["federalFilingStatus"]) -> typing.Union[MetaOapg.properties.federalFilingStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sex"]) -> typing.Union[MetaOapg.properties.sex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hireDate"]) -> typing.Union[MetaOapg.properties.hireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["homePhone"]) -> typing.Union[MetaOapg.properties.homePhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maritalStatus"]) -> typing.Union[MetaOapg.properties.maritalStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalMobilePhone"]) -> typing.Union[MetaOapg.properties.personalMobilePhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payFrequency"]) -> typing.Union[MetaOapg.properties.payFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalEmailAddress"]) -> typing.Union[MetaOapg.properties.personalEmailAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payType"]) -> typing.Union[MetaOapg.properties.payType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratePer"]) -> typing.Union[MetaOapg.properties.ratePer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary"]) -> typing.Union[MetaOapg.properties.salary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssn"]) -> typing.Union[MetaOapg.properties.ssn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateFilingStatus"]) -> typing.Union[MetaOapg.properties.stateFilingStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suiState"]) -> typing.Union[MetaOapg.properties.suiState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxForm"]) -> typing.Union[MetaOapg.properties.taxForm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxState"]) -> typing.Union[MetaOapg.properties.taxState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> typing.Union[MetaOapg.properties.userName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workEmailAddress"]) -> typing.Union[MetaOapg.properties.workEmailAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> typing.Union[MetaOapg.properties.zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "employeeId", "address1", "address2", "autoPayType", "baseRate", "city", "costCenter1", "costCenter2", "costCenter3", "defaultHours", "employeeStatus", "employmentType", "federalFilingStatus", "sex", "hireDate", "homePhone", "maritalStatus", "personalMobilePhone", "payFrequency", "personalEmailAddress", "payType", "ratePer", "salary", "state", "ssn", "stateFilingStatus", "suiState", "taxForm", "taxState", "userName", "workEmailAddress", "zip", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        address1: typing.Union[MetaOapg.properties.address1, str, schemas.Unset] = schemas.unset,
        address2: typing.Union[MetaOapg.properties.address2, str, schemas.Unset] = schemas.unset,
        autoPayType: typing.Union[MetaOapg.properties.autoPayType, str, schemas.Unset] = schemas.unset,
        baseRate: typing.Union[MetaOapg.properties.baseRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        costCenter1: typing.Union[MetaOapg.properties.costCenter1, str, schemas.Unset] = schemas.unset,
        costCenter2: typing.Union[MetaOapg.properties.costCenter2, str, schemas.Unset] = schemas.unset,
        costCenter3: typing.Union[MetaOapg.properties.costCenter3, str, schemas.Unset] = schemas.unset,
        defaultHours: typing.Union[MetaOapg.properties.defaultHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        employeeStatus: typing.Union[MetaOapg.properties.employeeStatus, str, schemas.Unset] = schemas.unset,
        employmentType: typing.Union[MetaOapg.properties.employmentType, str, schemas.Unset] = schemas.unset,
        federalFilingStatus: typing.Union[MetaOapg.properties.federalFilingStatus, str, schemas.Unset] = schemas.unset,
        sex: typing.Union[MetaOapg.properties.sex, str, schemas.Unset] = schemas.unset,
        hireDate: typing.Union[MetaOapg.properties.hireDate, str, schemas.Unset] = schemas.unset,
        homePhone: typing.Union[MetaOapg.properties.homePhone, str, schemas.Unset] = schemas.unset,
        maritalStatus: typing.Union[MetaOapg.properties.maritalStatus, str, schemas.Unset] = schemas.unset,
        personalMobilePhone: typing.Union[MetaOapg.properties.personalMobilePhone, str, schemas.Unset] = schemas.unset,
        payFrequency: typing.Union[MetaOapg.properties.payFrequency, str, schemas.Unset] = schemas.unset,
        personalEmailAddress: typing.Union[MetaOapg.properties.personalEmailAddress, str, schemas.Unset] = schemas.unset,
        payType: typing.Union[MetaOapg.properties.payType, str, schemas.Unset] = schemas.unset,
        ratePer: typing.Union[MetaOapg.properties.ratePer, str, schemas.Unset] = schemas.unset,
        salary: typing.Union[MetaOapg.properties.salary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        ssn: typing.Union[MetaOapg.properties.ssn, str, schemas.Unset] = schemas.unset,
        stateFilingStatus: typing.Union[MetaOapg.properties.stateFilingStatus, str, schemas.Unset] = schemas.unset,
        suiState: typing.Union[MetaOapg.properties.suiState, str, schemas.Unset] = schemas.unset,
        taxForm: typing.Union[MetaOapg.properties.taxForm, str, schemas.Unset] = schemas.unset,
        taxState: typing.Union[MetaOapg.properties.taxState, str, schemas.Unset] = schemas.unset,
        userName: typing.Union[MetaOapg.properties.userName, str, schemas.Unset] = schemas.unset,
        workEmailAddress: typing.Union[MetaOapg.properties.workEmailAddress, str, schemas.Unset] = schemas.unset,
        zip: typing.Union[MetaOapg.properties.zip, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Onboarding':
        return super().__new__(
            cls,
            *args,
            firstName=firstName,
            lastName=lastName,
            employeeId=employeeId,
            address1=address1,
            address2=address2,
            autoPayType=autoPayType,
            baseRate=baseRate,
            city=city,
            costCenter1=costCenter1,
            costCenter2=costCenter2,
            costCenter3=costCenter3,
            defaultHours=defaultHours,
            employeeStatus=employeeStatus,
            employmentType=employmentType,
            federalFilingStatus=federalFilingStatus,
            sex=sex,
            hireDate=hireDate,
            homePhone=homePhone,
            maritalStatus=maritalStatus,
            personalMobilePhone=personalMobilePhone,
            payFrequency=payFrequency,
            personalEmailAddress=personalEmailAddress,
            payType=payType,
            ratePer=ratePer,
            salary=salary,
            state=state,
            ssn=ssn,
            stateFilingStatus=stateFilingStatus,
            suiState=suiState,
            taxForm=taxForm,
            taxState=taxState,
            userName=userName,
            workEmailAddress=workEmailAddress,
            zip=zip,
            _configuration=_configuration,
            **kwargs,
        )
