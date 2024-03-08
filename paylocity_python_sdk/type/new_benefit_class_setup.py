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


class RequiredNewBenefitClassSetup(TypedDict):
    # Date when Benefit Class takes effect. Common formats are MM-DD-CCYY, CCYY-MM-DD.
    benefitClassSetupEffectiveDate: date

class OptionalNewBenefitClassSetup(TypedDict, total=False):
    # Benefit Class code. Values are configured in Paylocity Payroll/HR solution Company > Setup > Benefits > Classes.<br  />Max length: 30
    benefitClass: str

    # Salary used to configure benefits.<br  />Decimal(12,2)
    benefitSalary: typing.Union[int, float]

    # Date when Benefit Salary takes effect. Common formats are MM-DD-CCYY, CCYY-MM-DD.
    benefitSalaryEffectiveDate: date

    # Applicable only for ACA Enhanced clients and Benefit Classes with ACA Employment Type of Full Time.
    doNotApplyAdministrativePeriod: bool

    # Applicable only for ACA Enhanced clients and Benefit Classes with ACA Employment Type of Full Time.
    measureACAEligibility: bool

class NewBenefitClassSetup(RequiredNewBenefitClassSetup, OptionalNewBenefitClassSetup):
    pass