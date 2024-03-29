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


class Deduction(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            agency = schemas.StrSchema
            annualMaximum = schemas.NumberSchema
            calcCode = schemas.StrSchema
            caseNo = schemas.StrSchema
            costCenter1 = schemas.StrSchema
            costCenter2 = schemas.StrSchema
            costCenter3 = schemas.StrSchema
            dcode = schemas.StrSchema
            effectiveDate = schemas.DateSchema
            endDate = schemas.DateSchema
            fipsCode = schemas.StrSchema
            frequency = schemas.StrSchema
            goal = schemas.NumberSchema
            isSelfInsuredPlan = schemas.BoolSchema
            loanFirstPaymentDate401K = schemas.DateSchema
            loanIssueDate401K = schemas.DateSchema
            loanNumber = schemas.StrSchema
            maximum = schemas.NumberSchema
            medicalSupport = schemas.BoolSchema
            minimum = schemas.NumberSchema
            miscInfo = schemas.StrSchema
            paidTowardsGoal = schemas.NumberSchema
            priority = schemas.IntSchema
            rate = schemas.NumberSchema
            reportTerminated = schemas.BoolSchema
            startDate = schemas.DateSchema
            stateAbbrev = schemas.StrSchema
            __annotations__ = {
                "agency": agency,
                "annualMaximum": annualMaximum,
                "calcCode": calcCode,
                "caseNo": caseNo,
                "costCenter1": costCenter1,
                "costCenter2": costCenter2,
                "costCenter3": costCenter3,
                "dcode": dcode,
                "effectiveDate": effectiveDate,
                "endDate": endDate,
                "fipsCode": fipsCode,
                "frequency": frequency,
                "goal": goal,
                "isSelfInsuredPlan": isSelfInsuredPlan,
                "loanFirstPaymentDate401K": loanFirstPaymentDate401K,
                "loanIssueDate401K": loanIssueDate401K,
                "loanNumber": loanNumber,
                "maximum": maximum,
                "medicalSupport": medicalSupport,
                "minimum": minimum,
                "miscInfo": miscInfo,
                "paidTowardsGoal": paidTowardsGoal,
                "priority": priority,
                "rate": rate,
                "reportTerminated": reportTerminated,
                "startDate": startDate,
                "stateAbbrev": stateAbbrev,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agency"]) -> MetaOapg.properties.agency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualMaximum"]) -> MetaOapg.properties.annualMaximum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calcCode"]) -> MetaOapg.properties.calcCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseNo"]) -> MetaOapg.properties.caseNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCenter1"]) -> MetaOapg.properties.costCenter1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCenter2"]) -> MetaOapg.properties.costCenter2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCenter3"]) -> MetaOapg.properties.costCenter3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dcode"]) -> MetaOapg.properties.dcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveDate"]) -> MetaOapg.properties.effectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fipsCode"]) -> MetaOapg.properties.fipsCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal"]) -> MetaOapg.properties.goal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSelfInsuredPlan"]) -> MetaOapg.properties.isSelfInsuredPlan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanFirstPaymentDate401K"]) -> MetaOapg.properties.loanFirstPaymentDate401K: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanIssueDate401K"]) -> MetaOapg.properties.loanIssueDate401K: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanNumber"]) -> MetaOapg.properties.loanNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximum"]) -> MetaOapg.properties.maximum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["medicalSupport"]) -> MetaOapg.properties.medicalSupport: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum"]) -> MetaOapg.properties.minimum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["miscInfo"]) -> MetaOapg.properties.miscInfo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paidTowardsGoal"]) -> MetaOapg.properties.paidTowardsGoal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportTerminated"]) -> MetaOapg.properties.reportTerminated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateAbbrev"]) -> MetaOapg.properties.stateAbbrev: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agency", "annualMaximum", "calcCode", "caseNo", "costCenter1", "costCenter2", "costCenter3", "dcode", "effectiveDate", "endDate", "fipsCode", "frequency", "goal", "isSelfInsuredPlan", "loanFirstPaymentDate401K", "loanIssueDate401K", "loanNumber", "maximum", "medicalSupport", "minimum", "miscInfo", "paidTowardsGoal", "priority", "rate", "reportTerminated", "startDate", "stateAbbrev", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agency"]) -> typing.Union[MetaOapg.properties.agency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualMaximum"]) -> typing.Union[MetaOapg.properties.annualMaximum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calcCode"]) -> typing.Union[MetaOapg.properties.calcCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseNo"]) -> typing.Union[MetaOapg.properties.caseNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCenter1"]) -> typing.Union[MetaOapg.properties.costCenter1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCenter2"]) -> typing.Union[MetaOapg.properties.costCenter2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCenter3"]) -> typing.Union[MetaOapg.properties.costCenter3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dcode"]) -> typing.Union[MetaOapg.properties.dcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveDate"]) -> typing.Union[MetaOapg.properties.effectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fipsCode"]) -> typing.Union[MetaOapg.properties.fipsCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union[MetaOapg.properties.frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal"]) -> typing.Union[MetaOapg.properties.goal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSelfInsuredPlan"]) -> typing.Union[MetaOapg.properties.isSelfInsuredPlan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanFirstPaymentDate401K"]) -> typing.Union[MetaOapg.properties.loanFirstPaymentDate401K, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanIssueDate401K"]) -> typing.Union[MetaOapg.properties.loanIssueDate401K, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanNumber"]) -> typing.Union[MetaOapg.properties.loanNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximum"]) -> typing.Union[MetaOapg.properties.maximum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["medicalSupport"]) -> typing.Union[MetaOapg.properties.medicalSupport, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum"]) -> typing.Union[MetaOapg.properties.minimum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["miscInfo"]) -> typing.Union[MetaOapg.properties.miscInfo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paidTowardsGoal"]) -> typing.Union[MetaOapg.properties.paidTowardsGoal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> typing.Union[MetaOapg.properties.rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportTerminated"]) -> typing.Union[MetaOapg.properties.reportTerminated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateAbbrev"]) -> typing.Union[MetaOapg.properties.stateAbbrev, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agency", "annualMaximum", "calcCode", "caseNo", "costCenter1", "costCenter2", "costCenter3", "dcode", "effectiveDate", "endDate", "fipsCode", "frequency", "goal", "isSelfInsuredPlan", "loanFirstPaymentDate401K", "loanIssueDate401K", "loanNumber", "maximum", "medicalSupport", "minimum", "miscInfo", "paidTowardsGoal", "priority", "rate", "reportTerminated", "startDate", "stateAbbrev", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agency: typing.Union[MetaOapg.properties.agency, str, schemas.Unset] = schemas.unset,
        annualMaximum: typing.Union[MetaOapg.properties.annualMaximum, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        calcCode: typing.Union[MetaOapg.properties.calcCode, str, schemas.Unset] = schemas.unset,
        caseNo: typing.Union[MetaOapg.properties.caseNo, str, schemas.Unset] = schemas.unset,
        costCenter1: typing.Union[MetaOapg.properties.costCenter1, str, schemas.Unset] = schemas.unset,
        costCenter2: typing.Union[MetaOapg.properties.costCenter2, str, schemas.Unset] = schemas.unset,
        costCenter3: typing.Union[MetaOapg.properties.costCenter3, str, schemas.Unset] = schemas.unset,
        dcode: typing.Union[MetaOapg.properties.dcode, str, schemas.Unset] = schemas.unset,
        effectiveDate: typing.Union[MetaOapg.properties.effectiveDate, str, date, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        fipsCode: typing.Union[MetaOapg.properties.fipsCode, str, schemas.Unset] = schemas.unset,
        frequency: typing.Union[MetaOapg.properties.frequency, str, schemas.Unset] = schemas.unset,
        goal: typing.Union[MetaOapg.properties.goal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isSelfInsuredPlan: typing.Union[MetaOapg.properties.isSelfInsuredPlan, bool, schemas.Unset] = schemas.unset,
        loanFirstPaymentDate401K: typing.Union[MetaOapg.properties.loanFirstPaymentDate401K, str, date, schemas.Unset] = schemas.unset,
        loanIssueDate401K: typing.Union[MetaOapg.properties.loanIssueDate401K, str, date, schemas.Unset] = schemas.unset,
        loanNumber: typing.Union[MetaOapg.properties.loanNumber, str, schemas.Unset] = schemas.unset,
        maximum: typing.Union[MetaOapg.properties.maximum, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        medicalSupport: typing.Union[MetaOapg.properties.medicalSupport, bool, schemas.Unset] = schemas.unset,
        minimum: typing.Union[MetaOapg.properties.minimum, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        miscInfo: typing.Union[MetaOapg.properties.miscInfo, str, schemas.Unset] = schemas.unset,
        paidTowardsGoal: typing.Union[MetaOapg.properties.paidTowardsGoal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        reportTerminated: typing.Union[MetaOapg.properties.reportTerminated, bool, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        stateAbbrev: typing.Union[MetaOapg.properties.stateAbbrev, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Deduction':
        return super().__new__(
            cls,
            *args,
            agency=agency,
            annualMaximum=annualMaximum,
            calcCode=calcCode,
            caseNo=caseNo,
            costCenter1=costCenter1,
            costCenter2=costCenter2,
            costCenter3=costCenter3,
            dcode=dcode,
            effectiveDate=effectiveDate,
            endDate=endDate,
            fipsCode=fipsCode,
            frequency=frequency,
            goal=goal,
            isSelfInsuredPlan=isSelfInsuredPlan,
            loanFirstPaymentDate401K=loanFirstPaymentDate401K,
            loanIssueDate401K=loanIssueDate401K,
            loanNumber=loanNumber,
            maximum=maximum,
            medicalSupport=medicalSupport,
            minimum=minimum,
            miscInfo=miscInfo,
            paidTowardsGoal=paidTowardsGoal,
            priority=priority,
            rate=rate,
            reportTerminated=reportTerminated,
            startDate=startDate,
            stateAbbrev=stateAbbrev,
            _configuration=_configuration,
            **kwargs,
        )
