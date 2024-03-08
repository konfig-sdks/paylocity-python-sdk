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

from paylocity_python_sdk.type.new_additional_direct_deposit import NewAdditionalDirectDeposit
from paylocity_python_sdk.type.new_benefit_class_setup import NewBenefitClassSetup
from paylocity_python_sdk.type.new_fed_tax import NewFedTax
from paylocity_python_sdk.type.new_local_tax import NewLocalTax
from paylocity_python_sdk.type.new_main_direct_deposit import NewMainDirectDeposit
from paylocity_python_sdk.type.new_state_tax import NewStateTax
from paylocity_python_sdk.type.new_work_eligibility import NewWorkEligibility

class RequiredNewEmployee(TypedDict):
    # Paylocity assigned company number.<br  /> Max length: 9
    companyNumber: str

class OptionalNewEmployee(TypedDict, total=False):
    # Employee current job title.<br  />Max length: 50
    title: str

    # Employee home 1st address line. <br  />Max length: 40
    address1: str

    # Employee home 2nd address line. <br  />Max length: 40
    address2: str

    # Adjusted seniority date. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
    adjSeniorityDate: date

    # Employee annual salary. <br  />Decimal (12,2)
    annualSalary: typing.Union[int, float]

    # *True* to have Paylocity Payroll/HR solution automatically assign the next available employee ID.<br  />*False* when providing a value in the employeeId field.
    autoGenerateEmployeeId: bool

    # If set to *True*, employee will be paid automatically using deafultHours.
    autoPay: bool

    # Valid values are *N, D, S*. (N- employee won't automatically receive a salary or hours during payroll, D - employee will be automatically paid in defaultHours during payroll, S - employee will be automatically paid Salary
    autoPayType: str

    # Employee base rate, used for Hourly employees. <br  />Decimal (12,2)
    baseRate: typing.Union[int, float]

    # Employee birthdate. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
    birthDate: date

    # Employee home city. <br  />Max length: 40
    city: str

    # Employee clock badge number. Deafults to employeeId. <br  />Max length: 10
    clockBadge: str

    # Employer defined location, like *branch, division, department*, etc. Must match Company setup. <br  />Max length: 10
    costCenter1: str

    # Employer defined location, like *branch, division, department*, etc. Must match Company setup. <br  />Max length: 10
    costCenter2: str

    # Employer defined location, like *branch, division, department*, etc. Must match Company setup. <br  />Max length: 10
    costCenter3: str

    # Employee country. <br  /> Max length: 30
    country: str

    # Employee county.<br  /> Max length: 30 
    county: str

    # Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. <br  />Decimal (12,2)
    defaultHours: typing.Union[int, float]

    # Indicates if employee has disability status.
    disability: bool

    # Indicates if employee eligible for rehire.
    eligibleForRehire: bool

    # Indicates if employee in agriculture or farming.
    employee943: bool

    # Leave blank to have Paylocity Payroll/HR solution automatically assign the next available employee ID.<br  /> Max length: 10
    employeeId: str

    # Employee current work status. Common values are *A* (Active), *L* (Leave of Absence), *T* (Terminated). <br  />Max length: 20
    employeeStatus: str

    # Employee current employment type. Common values *RFT (Regular Full Time), RPT (Regular Part Time), SNL (Seasonal), TFT (Temporary Full Time), TPT (Temporary Part Time)*. <br  />Max length: 10
    employmentType: str

    # Values are configured in Company > Setup > HR > EEO Classes.<br  /> Max length: 10
    equalEmploymentOpportunityClass: str

    # Employee ethnicity.<br  /> Max length: 10
    ethnicity: str

    # Employee first name. <br  />Max length: 40
    firstName: str

    # Indicates if employee exempt from federal income tax.
    fitwExempt: bool

    # Notes for FITW exempt.<br  /> Max length: 250
    fitwExemptNotes: str

    # Reason code for FITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
    fitwExemptReason: str

    # Indicates if employee is exempt from Federal Unemployment Tax Act.
    futaExempt: bool

    # FUTA exempt note. <br  /> Max length: 250
    futaExemptNotes: str

    # Reason code for FUTA exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).<br  /> Max length: 30
    futaExemptReason: str

    # Employee hired date. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
    hireDate: date

    # Employee home phone number.<br  />Max length: 12
    homePhone: str

    # Indicates if employee is a supervisor or reviewer.
    isSupervisorReviewer: bool

    # Employee last name. <br  />Max length: 40
    lastName: str

    # Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. <br  />Max length: 10
    maritalStatus: str

    # Indicates if employee is Medicare exempt.
    medExempt: bool

    # Notes for Medicare exempt.
    medExemptNotes: str

    # Reason code for Medicare exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).<br  /> Max length: 30
    medExemptReason: str

    # Employee middle name.<br  /> Max length: 20
    middleName: str

    # Indicates if employee is exempt from minimum wage.
    minimumWageExempt: bool

    # Employee preferred display name.<br  /> Max length: 20
    nickname: str

    # Indicates override to the default Job Title. Use the title field to enter Employee job title.
    overrideTitle: bool

    # Indicates if employee is exempt from overtime.
    overtimeExempt: bool

    # Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. <br  />Max length: 5
    payFrequency: str

    # Employee pay grade. Must match Company setup. <br  /> Max length: 10
    payGrade: str

    # Employee pay group. Must match Company setup. <br  /> Max length: 20
    payGroup: str

    # Pay rate notes regarding employee.<br  /> Max length: 250
    payRateNote: str

    # Indicates if employee is eligible for pension.
    pension: bool

    # Employee personal email address. <br  />Max length: 50
    personalEmailAddress: str

    # Employee personal mobile phone number. <br  />Max length: 12
    personalMobilePhone: str

    # Employee position code. Must match Company setup.<br  />Max length: 20
    positionCode: str

    # Primary Pay Rate EffectiveDate
    primaryPayRateEffectiveDate: date

    # Prior last name if applicable.<br  />Max length: 40
    priorLastName: str

    # Employee rate (pay type) code.  Valid values are *Hourly* or *Salary*. <br  />Max length: 10
    rateCode: str

    # Employee base rate frequency used with payType Hourly. Common values are *Hour, Week*. Default is Hour. <br  />Max length: 10
    ratePer: str

    # Company number of reviewer. <br  />Max length: 9
    reviewerCo: str

    # Employee id of the reviewer. <br  />Max length: 10
    reviewerId: str

    # Employee gross salary per pay period used with payType Salary.<br  />Decimal (12,2)
    salary: typing.Union[int, float]

    # Employee preferred salutation. <br  />Max length: 10
    salutation: str

    # Employee gender. Common values *M* (Male), *F* (Female). <br  />Max length: 1
    sex: str

    # Employee work shift.<br  />Max length: 255
    shift: str

    # Indicates if employee exempt from state income tax.
    sitwExempt: bool

    # Notes for SITW exempt.<br  /> Max length: 250
    sitwExemptNotes: str

    # Reason code for SITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
    sitwExemptReason: str

    # Indicates if employee is a smoker.
    smoker: bool

    # Indicates if employee is exempt from Social Security taxes.
    ssExempt: bool

    # Notes for Socal Security exemptions.<br  /> Max length: 250
    ssExemptNotes: str

    # Reason code for Social Security exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
    ssExemptReason: str

    # Employee social security number. Leave it blank if valid social security number not available. <br  />Max length: 11
    ssn: str

    # Employee home state. <br  />Max length: 2
    state: str

    # Indicates if employee is statutory.
    statutory: bool

    # Employee name suffix. Common values are *Jr, Sr, II*.<br  />Max length: 30
    suffix: str

    # Indicates if employee is exempt from state unemployment insurance.
    suiExempt: bool

    # Notes for SUI exempt.<br  /> Max length: 250
    suiExemptNotes: str

    # Reason code for SUI exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
    suiExemptReason: str

    # Employee SUI (State Unemployment Insurance) state. <br  />Max length: 2
    suiState: str

    # Supervisor's company number. Defaults to employee company number.<br  />Max length: 9
    supervisorCo: str

    # EmployeeId of the supervisor. <br  />Max length: 10
    supervisorID: str

    # Emplopyee 1099R distribution code. Common values are *7* (Normal Distribution), *F* (Charitable Gift Annuity). <br  />Max length: 1
    taxDistributionCode1099R: str

    # Employee tax form for reporting income. Valid values are *W2, 1099M, 1099R*. Default is W2. <br  />Max length: 15
    taxForm: str

    # Indicates if employee receives tips.
    tipped: str

    # Employee union code. Must match Company setup. <br  />Max length: 10
    unionCode: str

    # Employee union affiliation effective date. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
    unionDate: date

    # Indicates if union dues are collected.
    unionDues: bool

    # Indicates if initiations fees are collected.
    unionInitFees: bool

    # Employee union position. Must match Company setup. <br  />Max length: 30
    unionPosition: str

    # Indicates if employee is a veteran.
    veteran: bool

    # Indicates if employee is exempt from Washington state Liability Insurance.
    waliExempt: bool

    # Notes for WALI exemption.
    waliExemptNotes: str

    # Reason code for WALI exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
    waliExemptReason: str

    # Employee work 1st address line.<br  /> Max length: 40
    workAddress1: str

    # Employee work 2nd address line. <br  /> Max length: 40
    workAddress2: str

    # Employee work city.<br  /> Max length: 40
    workCity: str

    # Employee work country.<br  /> Max length: 30
    workCountry: str

    # Employee work county.<br  /> Max length: 30
    workCounty: str

    # Employee work email. <br  />Max length: 50
    workEmailAddress: str

    # Employee worker compensation code. Must match Company setup.<br  /> Max length: 10
    workersComp: str

    # Employee work phone extension number.<br  /> Max length: 10
    workExt: str

    # Employee work location. <br  /> Max length: 50
    workLocation: str

    # Employee physical mail box location.<br  /> Max length: 10
    workMailStop: str

    # Employee work mobile phone number.<br  /> Max length: 12
    workMobilePhone: str

    # Employee work pager number.<br  /> Max length: 20
    workPager: str

    # Employee work phone number.<br  /> Max length: 12
    workPhone: str

    # Employee work state.<br  /> Max length: 2
    workState: str

    # Employee work zip code.<br  /> Max length: 10
    workZip: str

    # Employee home zip code. <br  />Max length: 10
    zip: str

    # If set to *True*, employee will be synced with Web Time.
    syncWebTimeRecord: bool

    newBenefitClassSetup: typing.List[NewBenefitClassSetup]

    newMainDirectDeposit: typing.List[NewMainDirectDeposit]

    newAdditionalDirectDeposit: typing.List[NewAdditionalDirectDeposit]

    newFedTax: typing.List[NewFedTax]

    newLocalTax: typing.List[NewLocalTax]

    newStateTax: typing.List[NewStateTax]

    newWorkEligibility: typing.List[NewWorkEligibility]

class NewEmployee(RequiredNewEmployee, OptionalNewEmployee):
    pass
