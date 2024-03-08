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


class Onboarding(BaseModel):
    # Employee first name. <br  />Max length: 40
    first_name: str = Field(alias='firstName')

    # Employee last name. <br  />Max length: 40
    last_name: str = Field(alias='lastName')

    # (optional) The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max
    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    # Employee home 1st address line. <br  />Max length: 40
    address1: typing.Optional[str] = Field(None, alias='address1')

    # Employee home 2nd address line. <br  />Max length: 40
    address2: typing.Optional[str] = Field(None, alias='address2')

    # Valid values are *N, D, S. (N- employee won't automatically receive a salary or hours during payroll, D - employee will be automatically paid in defaultHours during payroll, S - employee will be automatically paid Salary amount during payroll)*. <br  />Max length: 3
    auto_pay_type: typing.Optional[str] = Field(None, alias='autoPayType')

    # Employee base rate, used for Hourly employees. <br  />Decimal (12,2)
    base_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseRate')

    # Employee home city. <br  />Max length: 40
    city: typing.Optional[str] = Field(None, alias='city')

    # Employer defined location, like *branch, division, department, etc.* Must match Company setup. <br  />Max length: 10
    cost_center1: typing.Optional[str] = Field(None, alias='costCenter1')

    # Employer defined location, like *branch, division, department, etc.* Must match Company setup. <br  />Max length: 10
    cost_center2: typing.Optional[str] = Field(None, alias='costCenter2')

    # Employer defined location, like *branch, division, department, etc.* Must match Company setup. <br  />Max length: 10
    cost_center3: typing.Optional[str] = Field(None, alias='costCenter3')

    # Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. <br  />Decimal (12,2)
    default_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='defaultHours')

    # Employee current work status. Common values are *A (Active), L (Leave of Absence), T (Terminated)*. <br  />Max length: 20
    employee_status: typing.Optional[str] = Field(None, alias='employeeStatus')

    # Employee current employment type. Common values RFT *(Regular Full Time), RPT (Regular Part Time), SNL (Seasonal), TFT (Temporary Full Time), TPT (Temporary Part Time)*. <br  />Max length: 10
    employment_type: typing.Optional[str] = Field(None, alias='employmentType')

    # Employee federal filing status. Common values *M (Married), S (Single)*. <br  />Max length: 10
    federal_filing_status: typing.Optional[str] = Field(None, alias='federalFilingStatus')

    # Employee gender. Common values *M (Male), F (Female)*. <br  />Max length: 1
    sex: typing.Optional[str] = Field(None, alias='sex')

    # Employee hired date. Common formats are MM-DD-CCYY, CCYY-MM-DD
    hire_date: typing.Optional[str] = Field(None, alias='hireDate')

    # Employee home phone number. <br  />Max length: 12
    home_phone: typing.Optional[str] = Field(None, alias='homePhone')

    # Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. <br  />Max length: 10
    marital_status: typing.Optional[str] = Field(None, alias='maritalStatus')

    # Employee personal mobile phone number. <br  />Max length: 12
    personal_mobile_phone: typing.Optional[str] = Field(None, alias='personalMobilePhone')

    # Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. <br  />Max length: 5
    pay_frequency: typing.Optional[str] = Field(None, alias='payFrequency')

    # Employee personal email address. <br  />Max length: 50
    personal_email_address: typing.Optional[str] = Field(None, alias='personalEmailAddress')

    # Employee pay type. Valid values are *Hourly or Salary*. <br  />Max length: 10
    pay_type: typing.Optional[str] = Field(None, alias='payType')

    # Employee base rate frequency used with payType Hourly. Common values are *Hour or Week*. Default is Hour <br  />Max length: 10
    rate_per: typing.Optional[str] = Field(None, alias='ratePer')

    # Employee gross salary per pay period used with payType Salary. <br  />Decimal (12,2)
    salary: typing.Optional[typing.Union[int, float]] = Field(None, alias='salary')

    # Employee home state. <br  />Max length: 2
    state: typing.Optional[str] = Field(None, alias='state')

    # Employee social security number. Leave it blank if valid social security number not available. <br  />Max length: 11
    ssn: typing.Optional[str] = Field(None, alias='ssn')

    # Employee state filing status. Common values are *M (Married), S (Single)*. <br  />Max length: 50
    state_filing_status: typing.Optional[str] = Field(None, alias='stateFilingStatus')

    # Employee SUI (State Unemployment Insurance) state. <br  />Max length: 2
    sui_state: typing.Optional[str] = Field(None, alias='suiState')

    # Employee tax form for reporting income. Valid values are *W2, 1099M, 1099R*. Default is W2. <br  />Max length: 15
    tax_form: typing.Optional[str] = Field(None, alias='taxForm')

    # Employee primary tax state. <br  />Max Length: 2
    tax_state: typing.Optional[str] = Field(None, alias='taxState')

    # Required. Employer assigned username to log into Onboarding. Duplicate usernames are not allowed. <br  />Must be between 3 and 20 characters and cannot have special characters other than . (period) and _ (underscore)
    user_name: typing.Optional[str] = Field(None, alias='userName')

    # Employee work email. <br  />Max length: 50
    work_email_address: typing.Optional[str] = Field(None, alias='workEmailAddress')

    # Employee home zip code. <br  />Max length: 10
    zip: typing.Optional[str] = Field(None, alias='zip')
    class Config:
        arbitrary_types_allowed = True
