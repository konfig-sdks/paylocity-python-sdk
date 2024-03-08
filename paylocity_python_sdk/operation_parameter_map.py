operation_parameter_map = {
    '/v2/companies/{companyId}/employees/{employeeId}/additionalRates-PUT': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'changeReason'
            },
            {
                'name': 'costCenter1'
            },
            {
                'name': 'costCenter2'
            },
            {
                'name': 'costCenter3'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'endCheckDate'
            },
            {
                'name': 'job'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'rateCode'
            },
            {
                'name': 'rateNotes'
            },
            {
                'name': 'ratePer'
            },
            {
                'name': 'shift'
            },
        ]
    },
    '/v2/credentials/secrets-POST': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/v2/companies/{companyId}/codes/{codeResource}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'codeResource'
            },
        ]
    },
    '/v2/companies/{companyId}/openapi-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/v2/companies/{companyId}/customfields/{category}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'category'
            },
        ]
    },
    '/v1/deduction-POST': {
        'parameters': [
            {
                'name': 'deduction'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/deductions-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/deductions/{deductionCode}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'deductionCode'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/deductions/{deductionCode}/{startDate}-DELETE': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'deductionCode'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/directDeposit-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/earnings-PUT': {
        'parameters': [
            {
                'name': 'earningCode'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'agency'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'annualMaximum'
            },
            {
                'name': 'calculationCode'
            },
            {
                'name': 'costCenter1'
            },
            {
                'name': 'costCenter2'
            },
            {
                'name': 'costCenter3'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'goal'
            },
            {
                'name': 'hoursOrUnits'
            },
            {
                'name': 'isSelfInsured'
            },
            {
                'name': 'jobCode'
            },
            {
                'name': 'miscellaneousInfo'
            },
            {
                'name': 'paidTowardsGoal'
            },
            {
                'name': 'payPeriodMaximum'
            },
            {
                'name': 'payPeriodMinimum'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'rateCode'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate}-DELETE': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'earningCode'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/earnings-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'earningCode'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'earningCode'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/emergencyContacts-PUT': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
            {
                'name': 'county'
            },
            {
                'name': 'email'
            },
            {
                'name': 'homePhone'
            },
            {
                'name': 'mobilePhone'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'pager'
            },
            {
                'name': 'primaryPhone'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'relationship'
            },
            {
                'name': 'state'
            },
            {
                'name': 'syncEmployeeInfo'
            },
            {
                'name': 'workExtension'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'zip'
            },
        ]
    },
    '/v2/companies/{companyId}/employees-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'additionalDirectDeposit'
            },
            {
                'name': 'additionalRate'
            },
            {
                'name': 'benefitSetup'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'companyFEIN'
            },
            {
                'name': 'companyName'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'customBooleanFields'
            },
            {
                'name': 'customDateFields'
            },
            {
                'name': 'customDropDownFields'
            },
            {
                'name': 'customNumberFields'
            },
            {
                'name': 'customTextFields'
            },
            {
                'name': 'departmentPosition'
            },
            {
                'name': 'disabilityDescription'
            },
            {
                'name': 'emergencyContacts'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'ethnicity'
            },
            {
                'name': 'federalTax'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'homeAddress'
            },
            {
                'name': 'isHighlyCompensated'
            },
            {
                'name': 'isSmoker'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'localTax'
            },
            {
                'name': 'mainDirectDeposit'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'nonPrimaryStateTax'
            },
            {
                'name': 'ownerPercent'
            },
            {
                'name': 'preferredName'
            },
            {
                'name': 'primaryPayRate'
            },
            {
                'name': 'primaryStateTax'
            },
            {
                'name': 'priorLastName'
            },
            {
                'name': 'salutation'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'status'
            },
            {
                'name': 'suffix'
            },
            {
                'name': 'taxSetup'
            },
            {
                'name': 'veteranDescription'
            },
            {
                'name': 'webTime'
            },
            {
                'name': 'workAddress'
            },
            {
                'name': 'workEligibility'
            },
        ]
    },
    '/v2/companies/{companyId}/employees-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'pagesize'
            },
            {
                'name': 'pagenumber'
            },
            {
                'name': 'includetotalcount'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}-PATCH': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'additionalDirectDeposit'
            },
            {
                'name': 'additionalRate'
            },
            {
                'name': 'benefitSetup'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'companyFEIN'
            },
            {
                'name': 'companyName'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'customBooleanFields'
            },
            {
                'name': 'customDateFields'
            },
            {
                'name': 'customDropDownFields'
            },
            {
                'name': 'customNumberFields'
            },
            {
                'name': 'customTextFields'
            },
            {
                'name': 'departmentPosition'
            },
            {
                'name': 'disabilityDescription'
            },
            {
                'name': 'emergencyContacts'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'ethnicity'
            },
            {
                'name': 'federalTax'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'homeAddress'
            },
            {
                'name': 'isHighlyCompensated'
            },
            {
                'name': 'isSmoker'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'localTax'
            },
            {
                'name': 'mainDirectDeposit'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'nonPrimaryStateTax'
            },
            {
                'name': 'ownerPercent'
            },
            {
                'name': 'preferredName'
            },
            {
                'name': 'primaryPayRate'
            },
            {
                'name': 'primaryStateTax'
            },
            {
                'name': 'priorLastName'
            },
            {
                'name': 'salutation'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'status'
            },
            {
                'name': 'suffix'
            },
            {
                'name': 'taxSetup'
            },
            {
                'name': 'veteranDescription'
            },
            {
                'name': 'webTime'
            },
            {
                'name': 'workAddress'
            },
            {
                'name': 'workEligibility'
            },
        ]
    },
    '/v1/employee-POST': {
        'parameters': [
            {
                'name': 'newEmployee'
            },
        ]
    },
    '/v1/company/{companyId}/employee/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v1/update-employee-POST': {
        'parameters': [
            {
                'name': 'updateEmployee'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/benefitSetup-PUT': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'benefitClass'
            },
            {
                'name': 'benefitClassEffectiveDate'
            },
            {
                'name': 'benefitSalary'
            },
            {
                'name': 'benefitSalaryEffectiveDate'
            },
            {
                'name': 'doNotApplyAdministrativePeriod'
            },
            {
                'name': 'isMeasureAcaEligibility'
            },
        ]
    },
    '/v2/weblinkstaging/companies/{companyId}/employees/newemployees-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'additionalDirectDeposit'
            },
            {
                'name': 'benefitSetup'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'customBooleanFields'
            },
            {
                'name': 'customDateFields'
            },
            {
                'name': 'customDropDownFields'
            },
            {
                'name': 'customNumberFields'
            },
            {
                'name': 'customTextFields'
            },
            {
                'name': 'departmentPosition'
            },
            {
                'name': 'disabilityDescription'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'ethnicity'
            },
            {
                'name': 'federalTax'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'fitwExemptReason'
            },
            {
                'name': 'futaExemptReason'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'homeAddress'
            },
            {
                'name': 'isEmployee943'
            },
            {
                'name': 'isSmoker'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'localTax'
            },
            {
                'name': 'mainDirectDeposit'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'medExemptReason'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'nonPrimaryStateTax'
            },
            {
                'name': 'preferredName'
            },
            {
                'name': 'primaryPayRate'
            },
            {
                'name': 'primaryStateTax'
            },
            {
                'name': 'priorLastName'
            },
            {
                'name': 'salutation'
            },
            {
                'name': 'sitwExemptReason'
            },
            {
                'name': 'ssExemptReason'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'status'
            },
            {
                'name': 'suffix'
            },
            {
                'name': 'suiExemptReason'
            },
            {
                'name': 'suiState'
            },
            {
                'name': 'taxDistributionCode1099R'
            },
            {
                'name': 'taxForm'
            },
            {
                'name': 'veteranDescription'
            },
            {
                'name': 'webTime'
            },
            {
                'name': 'workAddress'
            },
            {
                'name': 'workEligibility'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/localTaxes-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'exemptions'
            },
            {
                'name': 'exemptions2'
            },
            {
                'name': 'filingStatus'
            },
            {
                'name': 'residentPSD'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'workPSD'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/localTaxes-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'taxCode'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}-DELETE': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'taxCode'
            },
        ]
    },
    '/v1/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}-PUT': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'exemptions'
            },
            {
                'name': 'exemptions2'
            },
            {
                'name': 'filingStatus'
            },
            {
                'name': 'residentPSD'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'workPSD'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/localTaxes-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'exemptions'
            },
            {
                'name': 'exemptions2'
            },
            {
                'name': 'filingStatus'
            },
            {
                'name': 'residentPSD'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'workPSD'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}-DELETE': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'taxCode'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/localTaxes-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'taxCode'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/nonprimaryStateTax-PUT': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'deductionsAmount'
            },
            {
                'name': 'dependentsAmount'
            },
            {
                'name': 'exemptions'
            },
            {
                'name': 'exemptions2'
            },
            {
                'name': 'filingStatus'
            },
            {
                'name': 'higherRate'
            },
            {
                'name': 'otherIncomeAmount'
            },
            {
                'name': 'percentage'
            },
            {
                'name': 'reciprocityCode'
            },
            {
                'name': 'specialCheckCalc'
            },
            {
                'name': 'taxCalculationCode'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'w4FormYear'
            },
        ]
    },
    '/v1/companies/{companyId}/onboarding/employees-POST': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'autoPayType'
            },
            {
                'name': 'baseRate'
            },
            {
                'name': 'city'
            },
            {
                'name': 'costCenter1'
            },
            {
                'name': 'costCenter2'
            },
            {
                'name': 'costCenter3'
            },
            {
                'name': 'defaultHours'
            },
            {
                'name': 'employeeStatus'
            },
            {
                'name': 'employmentType'
            },
            {
                'name': 'federalFilingStatus'
            },
            {
                'name': 'sex'
            },
            {
                'name': 'hireDate'
            },
            {
                'name': 'homePhone'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'personalMobilePhone'
            },
            {
                'name': 'payFrequency'
            },
            {
                'name': 'personalEmailAddress'
            },
            {
                'name': 'payType'
            },
            {
                'name': 'ratePer'
            },
            {
                'name': 'salary'
            },
            {
                'name': 'state'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'stateFilingStatus'
            },
            {
                'name': 'suiState'
            },
            {
                'name': 'taxForm'
            },
            {
                'name': 'taxState'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'workEmailAddress'
            },
            {
                'name': 'zip'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'year'
            },
            {
                'name': 'pagesize'
            },
            {
                'name': 'pagenumber'
            },
            {
                'name': 'includetotalcount'
            },
            {
                'name': 'codegroup'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}/{checkDate}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'year'
            },
            {
                'name': 'checkDate'
            },
            {
                'name': 'pagesize'
            },
            {
                'name': 'pagenumber'
            },
            {
                'name': 'includetotalcount'
            },
            {
                'name': 'codegroup'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'year'
            },
            {
                'name': 'pagesize'
            },
            {
                'name': 'pagenumber'
            },
            {
                'name': 'includetotalcount'
            },
            {
                'name': 'codegroup'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'year'
            },
            {
                'name': 'checkDate'
            },
            {
                'name': 'pagesize'
            },
            {
                'name': 'pagenumber'
            },
            {
                'name': 'includetotalcount'
            },
            {
                'name': 'codegroup'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/primaryStateTax-PUT': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'deductionsAmount'
            },
            {
                'name': 'dependentsAmount'
            },
            {
                'name': 'exemptions'
            },
            {
                'name': 'exemptions2'
            },
            {
                'name': 'filingStatus'
            },
            {
                'name': 'higherRate'
            },
            {
                'name': 'otherIncomeAmount'
            },
            {
                'name': 'percentage'
            },
            {
                'name': 'specialCheckCalc'
            },
            {
                'name': 'taxCalculationCode'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'w4FormYear'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/sensitivedata-PUT': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'disability'
            },
            {
                'name': 'ethnicity'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'veteran'
            },
        ]
    },
    '/v2/companies/{companyId}/employees/{employeeId}/sensitivedata-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
};