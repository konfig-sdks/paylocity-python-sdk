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

from paylocity_python_sdk.type.employee_additional_direct_deposit import EmployeeAdditionalDirectDeposit
from paylocity_python_sdk.type.employee_additional_rate import EmployeeAdditionalRate
from paylocity_python_sdk.type.employee_custom_boolean_fields import EmployeeCustomBooleanFields
from paylocity_python_sdk.type.employee_custom_date_fields import EmployeeCustomDateFields
from paylocity_python_sdk.type.employee_custom_drop_down_fields import EmployeeCustomDropDownFields
from paylocity_python_sdk.type.employee_custom_number_fields import EmployeeCustomNumberFields
from paylocity_python_sdk.type.employee_custom_text_fields import EmployeeCustomTextFields
from paylocity_python_sdk.type.employee_emergency_contacts import EmployeeEmergencyContacts
from paylocity_python_sdk.type.employee_local_tax import EmployeeLocalTax

class RequiredEmployee(TypedDict):
    pass

class OptionalEmployee(TypedDict, total=False):
    additionalDirectDeposit: EmployeeAdditionalDirectDeposit

    additionalRate: EmployeeAdditionalRate

    #  Add or update setup values used for employee benefits integration, insurance plan settings, and ACA reporting.
    benefitSetup: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee birthdate. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
    birthDate: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Company FEIN as defined in Paylocity Payroll/HR solution, applicable with GET requests only.<br  /> Max length: 20
    companyFEIN: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Company name as defined in Paylocity Payroll/HR solution, applicable with GET requests only.<br  /> Max length: 50
    companyName: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee is paid in this currency. <br  />Max length: 30
    currency: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    customBooleanFields: EmployeeCustomBooleanFields

    customDateFields: EmployeeCustomDateFields

    customDropDownFields: EmployeeCustomDropDownFields

    customNumberFields: EmployeeCustomNumberFields

    customTextFields: EmployeeCustomTextFields

    # Add or update home department cost center, position, supervisor, reviewer, employment type, EEO class, pay settings, and union information.
    departmentPosition: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Indicates if employee has disability status.
    disabilityDescription: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    emergencyContacts: EmployeeEmergencyContacts

    # Leave blank to have Paylocity Payroll/HR solution automatically assign the next available employee ID.<br  />Max length: 10
    employeeId: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee ethnicity.<br  /> Max length: 10
    ethnicity: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update federal tax amount type (taxCalculationCode), amount or percentage, filing status, and exemptions.
    federalTax: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee first name. <br  />Max length: 40
    firstName: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee gender. Common values *M* (Male), *F* (Female). <br  />Max length: 1
    gender: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update employee's home address, personal phone numbers, and personal email.
    homeAddress: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Indicates if employee meets the highly compensated employee criteria.
    isHighlyCompensated: bool

    # Indicates if employee is a smoker.
    isSmoker: bool

    # Employee last name. <br  />Max length: 40
    lastName: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    localTax: EmployeeLocalTax

    # Add the main direct deposit account. After deposits are made to any additional direct deposit accounts, the remaining net check is deposited in the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with what is provided on the request. GET API will not return direct deposit data.
    mainDirectDeposit: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. <br  />Max length: 10
    maritalStatus: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee middle name.<br  /> Max length: 20
    middleName: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update non-primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, supplemental check (specialCheckCalc), and reciprocity code information.
    nonPrimaryStateTax: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Percentage of employee's ownership in the company, entered as a whole number. <br  /> Decimal (12,2)
    ownerPercent: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee preferred display name.<br  /> Max length: 20
    preferredName: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update hourly or salary pay rate, effective date, and pay frequency.
    primaryPayRate: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, and supplemental check (specialCheckCalc) information. Only one primary state is allowed. Sending an updated primary state will replace the current primary state.
    primaryStateTax: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Prior last name if applicable.<br  />Max length: 40
    priorLastName: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee preferred salutation. <br  />Max length: 10
    salutation: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee social security number. Leave it blank if valid social security number not available. <br  />Max length: 11
    ssn: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update employee status, change reason, effective date, and adjusted seniority date. Note that companies that are still in Implementation cannot hire future employees.
    status: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employee name suffix. Common values are *Jr, Sr, II*.<br  />Max length: 30
    suffix: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add tax form, 1099 exempt reasons and notes, and 943 agricultural employee information. Once the employee receives wages, this information cannot be updated. Add or update SUI tax state, retirement plan, and statutory information.
    taxSetup: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Indicates if employee is a veteran.
    veteranDescription: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update Web Time badge number and charge rate and synchronize Paylocity Payroll/HR solution and Web Time employee data.
    webTime: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update employee's work address, phone numbers, and email. Work Location drop down field is not included.
    workAddress: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Add or update I-9 work authorization information.
    workEligibility: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Employee(RequiredEmployee, OptionalEmployee):
    pass
