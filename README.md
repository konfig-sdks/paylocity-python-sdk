<div align="center">

[![Visit Paylocity](./header.png)](https://developer.paylocity.com)

# Paylocity<a id="paylocity"></a>

For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`paylocity.additional_rates.update_employee_additional_rates`](#paylocityadditional_ratesupdate_employee_additional_rates)
  * [`paylocity.client_credentials.obtain_new_client_secret`](#paylocityclient_credentialsobtain_new_client_secret)
  * [`paylocity.company_codes.get_all_by_resource`](#paylocitycompany_codesget_all_by_resource)
  * [`paylocity.company_specific_schema.get_open_api_doc`](#paylocitycompany_specific_schemaget_open_api_doc)
  * [`paylocity.custom_fields.get_all_by_category`](#paylocitycustom_fieldsget_all_by_category)
  * [`paylocity.deduction.add_or_update_deduction`](#paylocitydeductionadd_or_update_deduction)
  * [`paylocity.deduction.get_all_deductions`](#paylocitydeductionget_all_deductions)
  * [`paylocity.deduction.get_by_code`](#paylocitydeductionget_by_code)
  * [`paylocity.deduction.remove_deduction_by_code_and_start_date`](#paylocitydeductionremove_deduction_by_code_and_start_date)
  * [`paylocity.direct_deposit.get_all_direct_deposits`](#paylocitydirect_depositget_all_direct_deposits)
  * [`paylocity.earnings.add_or_update_earning`](#paylocityearningsadd_or_update_earning)
  * [`paylocity.earnings.delete_by_code_and_start`](#paylocityearningsdelete_by_code_and_start)
  * [`paylocity.earnings.get_all`](#paylocityearningsget_all)
  * [`paylocity.earnings.get_by_code_and_start`](#paylocityearningsget_by_code_and_start)
  * [`paylocity.earnings.get_by_earning_code`](#paylocityearningsget_by_earning_code)
  * [`paylocity.emergency_contacts.add_or_update`](#paylocityemergency_contactsadd_or_update)
  * [`paylocity.employee.add_to_paylocity`](#paylocityemployeeadd_to_paylocity)
  * [`paylocity.employee.get_all_employees`](#paylocityemployeeget_all_employees)
  * [`paylocity.employee.get_employee_data`](#paylocityemployeeget_employee_data)
  * [`paylocity.employee.update_employee_data`](#paylocityemployeeupdate_employee_data)
  * [`paylocity.employee_(v1).create_new_employee_record`](#paylocityemployee_v1create_new_employee_record)
  * [`paylocity.employee_(v1).get_employee_data`](#paylocityemployee_v1get_employee_data)
  * [`paylocity.employee_(v1).update_employee_data_to_paylocity`](#paylocityemployee_v1update_employee_data_to_paylocity)
  * [`paylocity.employee_benefit_setup.add_or_update_benefit_setup`](#paylocityemployee_benefit_setupadd_or_update_benefit_setup)
  * [`paylocity.employee_staging.add_new_employee_to_web_link`](#paylocityemployee_stagingadd_new_employee_to_web_link)
  * [`paylocity.local_tax.create_or_update_local_taxes`](#paylocitylocal_taxcreate_or_update_local_taxes)
  * [`paylocity.local_tax.get_all_taxes_for_employee`](#paylocitylocal_taxget_all_taxes_for_employee)
  * [`paylocity.local_tax.get_for_tax_code`](#paylocitylocal_taxget_for_tax_code)
  * [`paylocity.local_tax.remove_for_tax_code`](#paylocitylocal_taxremove_for_tax_code)
  * [`paylocity.local_tax.update_for_tax_code`](#paylocitylocal_taxupdate_for_tax_code)
  * [`paylocity.local_taxes.add_new_tax`](#paylocitylocal_taxesadd_new_tax)
  * [`paylocity.local_taxes.delete_by_tax_code`](#paylocitylocal_taxesdelete_by_tax_code)
  * [`paylocity.local_taxes.get_all_for_employee`](#paylocitylocal_taxesget_all_for_employee)
  * [`paylocity.local_taxes.get_by_tax_code`](#paylocitylocal_taxesget_by_tax_code)
  * [`paylocity.non_primary_state_tax.add_or_update_state_tax`](#paylocitynon_primary_state_taxadd_or_update_state_tax)
  * [`paylocity.onboarding.add_employee_to_onboarding`](#paylocityonboardingadd_employee_to_onboarding)
  * [`paylocity.pay_statements.get_details_by_year`](#paylocitypay_statementsget_details_by_year)
  * [`paylocity.pay_statements.get_details_by_year_and_check_date`](#paylocitypay_statementsget_details_by_year_and_check_date)
  * [`paylocity.pay_statements.get_summary_by_year`](#paylocitypay_statementsget_summary_by_year)
  * [`paylocity.pay_statements.get_summary_data`](#paylocitypay_statementsget_summary_data)
  * [`paylocity.primary_state_tax.add_or_update_tax`](#paylocityprimary_state_taxadd_or_update_tax)
  * [`paylocity.sensitive_data.add_or_update_employee_sensitive_data`](#paylocitysensitive_dataadd_or_update_employee_sensitive_data)
  * [`paylocity.sensitive_data.get_employee_sensitive_data`](#paylocitysensitive_dataget_employee_sensitive_data)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Paylocity&serviceName=Weblink&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from paylocity_python_sdk import Paylocity, ApiException

paylocity = Paylocity(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Add/update additional rates
    paylocity.additional_rates.update_employee_additional_rates(
        company_id="companyId_example",
        employee_id="employeeId_example",
        change_reason={},
        cost_center1={},
        cost_center2={},
        cost_center3={},
        effective_date={},
        end_check_date={},
        job={},
        rate={},
        rate_code={},
        rate_notes={},
        rate_per={},
        shift={},
    )
except ApiException as e:
    print("Exception when calling AdditionalRatesApi.update_employee_additional_rates: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from paylocity_python_sdk import Paylocity, ApiException

paylocity = Paylocity(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Add/update additional rates
        await paylocity.additional_rates.aupdate_employee_additional_rates(
            company_id="companyId_example",
            employee_id="employeeId_example",
            change_reason={},
            cost_center1={},
            cost_center2={},
            cost_center3={},
            effective_date={},
            end_check_date={},
            job={},
            rate={},
            rate_code={},
            rate_notes={},
            rate_per={},
            shift={},
        )
    except ApiException as e:
        print("Exception when calling AdditionalRatesApi.update_employee_additional_rates: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from paylocity_python_sdk import Paylocity, ApiException

paylocity = Paylocity(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Add/update additional rates
    update_employee_additional_rates_response = paylocity.additional_rates.raw.update_employee_additional_rates(
        company_id="companyId_example",
        employee_id="employeeId_example",
        change_reason={},
        cost_center1={},
        cost_center2={},
        cost_center3={},
        effective_date={},
        end_check_date={},
        job={},
        rate={},
        rate_code={},
        rate_notes={},
        rate_per={},
        shift={},
    )
    pprint(update_employee_additional_rates_response.headers)
    pprint(update_employee_additional_rates_response.status)
    pprint(update_employee_additional_rates_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AdditionalRatesApi.update_employee_additional_rates: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `paylocity.additional_rates.update_employee_additional_rates`<a id="paylocityadditional_ratesupdate_employee_additional_rates"></a>

Sends new or updated employee additional rates information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.additional_rates.update_employee_additional_rates(
    company_id="companyId_example",
    employee_id="employeeId_example",
    change_reason={},
    cost_center1={},
    cost_center2={},
    cost_center3={},
    effective_date={},
    end_check_date={},
    job={},
    rate={},
    rate_code={},
    rate_notes={},
    rate_per={},
    shift={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### change_reason: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="change_reason-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required. If populated, must match one of the system coded values available in the Additional Rates Change Reason drop down.<br />

##### cost_center1: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="cost_center1-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 1 drop down. This cell must be in a text format.<br />

##### cost_center2: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="cost_center2-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 2 drop down. This cell must be in a text format.<br />

##### cost_center3: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="cost_center3-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 3 drop down. This cell must be in a text format.<br />

##### effective_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="effective_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.<br />

##### end_check_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="end_check_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required. Must match one of the system coded check dates available in the Additional Rates End Check Date drop down. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.<br />

##### job: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="job-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required. If populated, must match one of the system coded values available in the Additional Rates Job drop down.<br />

##### rate: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="rate-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Enter dollar amount that corresponds to the Per selection.<br />

##### rate_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="rate_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. If populated, must match one of the system coded values available in the Additional Rates Rate Code drop down.<br />

##### rate_notes: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="rate_notes-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required.<br  />Max length: 4000<br />

##### rate_per: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="rate_per-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Valid values are HOUR or WEEK.<br />

##### shift: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="shift-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Not required. If populated, must match one of the system coded values available in the Additional Rates Shift drop down.<br />

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AdditionalRate`](./paylocity_python_sdk/type/additional_rate.py)
Additional Rate Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/additionalRates` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.client_credentials.obtain_new_client_secret`<a id="paylocityclient_credentialsobtain_new_client_secret"></a>

Obtain new client secret for Paylocity-issued client id. See Weblink Authentication section for details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
obtain_new_client_secret_response = paylocity.client_credentials.obtain_new_client_secret(
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

A value sent with the 'ACTION NEEDED: Web Link API Credentials Expiring Soon.' email notification.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddClientSecret`](./paylocity_python_sdk/type/add_client_secret.py)
Add Client Secret Model

#### 🔄 Return<a id="🔄-return"></a>

[`ClientCredentialsObtainNewClientSecretResponse`](./paylocity_python_sdk/pydantic/client_credentials_obtain_new_client_secret_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/credentials/secrets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.company_codes.get_all_by_resource`<a id="paylocitycompany_codesget_all_by_resource"></a>

Get All Company Codes for the selected company and resource.
\
> 🚧 Maintenance Mode
> 
> _This API is in a limited support mode and certain resources will be moved to a sunset status in the next 18-24 months._
> 
> The [Company Level Information API](ref:get_apihub-payroll-v1-companies-companyid-jobs) should be used when possible in place of Company Codes resource of this API

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_by_resource_response = paylocity.company_codes.get_all_by_resource(
    company_id="companyId_example",
    code_resource="codeResource_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### code_resource: `str`<a id="code_resource-str"></a>

Type of Company Code. Common values costcenter1, costcenter2, costcenter3, deductions, earnings, taxes, paygrade, positions.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyCodesGetAllByResourceResponse`](./paylocity_python_sdk/pydantic/company_codes_get_all_by_resource_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/codes/{codeResource}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.company_specific_schema.get_open_api_doc`<a id="paylocitycompany_specific_schemaget_open_api_doc"></a>

The company-specific Open API endpoint allows the client to GET an Open API document for the Paylocity API that is customized with company-specific resource schemas. These customized resource schemas define certain properties as enumerations of pre-defined values that correspond to the company's setup with Paylocity Payroll/HR solution. The customized schemas also indicate which properties are required by the company within Paylocity Payroll/HR solution.<br  />To learn more about Open API, click [here](https://www.openapis.org/)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.company_specific_schema.get_open_api_doc(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/openapi` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.custom_fields.get_all_by_category`<a id="paylocitycustom_fieldsget_all_by_category"></a>

Get All Custom Fields for the selected company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_by_category_response = paylocity.custom_fields.get_all_by_category(
    company_id="companyId_example",
    category="category_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### category: `str`<a id="category-str"></a>

Custom Fields Category

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsGetAllByCategoryResponse`](./paylocity_python_sdk/pydantic/custom_fields_get_all_by_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/customfields/{category}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.deduction.add_or_update_deduction`<a id="paylocitydeductionadd_or_update_deduction"></a>

Add/Update Deduction API sends new or updated employee deduction information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.deduction.add_or_update_deduction(
    deduction={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### deduction: [`AddUpdateDeduction`](./paylocity_python_sdk/type/add_update_deduction.py)<a id="deduction-addupdatedeductionpaylocity_python_sdktypeadd_update_deductionpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeductionAddOrUpdateDeductionRequest`](./paylocity_python_sdk/type/deduction_add_or_update_deduction_request.py)
Deduction

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/deduction` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.deduction.get_all_deductions`<a id="paylocitydeductionget_all_deductions"></a>

Get All Deductions returns all deductions for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_deductions_response = paylocity.deduction.get_all_deductions(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`DeductionGetAllDeductionsResponse`](./paylocity_python_sdk/pydantic/deduction_get_all_deductions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/deductions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.deduction.get_by_code`<a id="paylocitydeductionget_by_code"></a>

Get Deduction for Deduction Code returns records for a specific deduction for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_code_response = paylocity.deduction.get_by_code(
    company_id="companyId_example",
    employee_id="employeeId_example",
    deduction_code="deductionCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### deduction_code: `str`<a id="deduction_code-str"></a>

Deduction Code

#### 🔄 Return<a id="🔄-return"></a>

[`Deduction`](./paylocity_python_sdk/pydantic/deduction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/deductions/{deductionCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.deduction.remove_deduction_by_code_and_start_date`<a id="paylocitydeductionremove_deduction_by_code_and_start_date"></a>

Delete Deduction API deletes an incorrect deduction from Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.deduction.remove_deduction_by_code_and_start_date(
    company_id="companyId_example",
    employee_id="employeeId_example",
    deduction_code="deductionCode_example",
    start_date="startDate_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### deduction_code: `str`<a id="deduction_code-str"></a>

Deduction Code

##### start_date: `str`<a id="start_date-str"></a>

Start Date

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/deductions/{deductionCode}/{startDate}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.direct_deposit.get_all_direct_deposits`<a id="paylocitydirect_depositget_all_direct_deposits"></a>

Get All Direct Deposit returns main direct deposit and all additional direct depositsfor the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_direct_deposits_response = paylocity.direct_deposit.get_all_direct_deposits(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositGetAllDirectDepositsResponse`](./paylocity_python_sdk/pydantic/direct_deposit_get_all_direct_deposits_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/directDeposit` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.earnings.add_or_update_earning`<a id="paylocityearningsadd_or_update_earning"></a>

Add/Update Earning API sends new or updated employee earnings information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.earnings.add_or_update_earning(
    earning_code={},
    start_date={},
    company_id="companyId_example",
    employee_id="employeeId_example",
    agency={},
    amount={},
    annual_maximum={},
    calculation_code={},
    cost_center1={},
    cost_center2={},
    cost_center3={},
    effective_date={},
    end_date={},
    frequency={},
    goal={},
    hours_or_units={},
    is_self_insured={},
    job_code={},
    miscellaneous_info={},
    paid_towards_goal={},
    pay_period_maximum={},
    pay_period_minimum={},
    rate={},
    rate_code={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### earning_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="earning_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Earning code. Must match Company setup. <br  />Max length: 10

##### start_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="start_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Start date of an earning based on payroll calendar. Common formats are MM-DD-CCYY, CCYY-MM-DD.

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### agency: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="agency-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Third-party agency associated with earning. Must match Company setup.<br  />Max length: 10

##### amount: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="amount-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Value that matches CalculationCode to add to gross wages. For percentage (%), enter whole number (10 = 10%).  <br  />Decimal(12,2)

##### annual_maximum: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="annual_maximum-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Year to Date dollar amount not to be exceeded for an earning in the calendar year. Used only with company driven maximums. <br  />Decimal(12,2)

##### calculation_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="calculation_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Defines how earnings are calculated. Common values are *% (percentage of gross), flat (flat dollar amount)*. Defaulted to the Company setup calcCode for earning. <br  />Max length: 20

##### cost_center1: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="cost_center1-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Cost Center associated with earning. Must match Company setup.<br  /> Max length: 10

##### cost_center2: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="cost_center2-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Cost Center associated with earning. Must match Company setup.<br  /> Max length: 10

##### cost_center3: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="cost_center3-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Cost Center associated with earning. Must match Company setup.<br  /> Max length: 10

##### effective_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="effective_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Date earning is active. Defaulted to run date or check date based on Company setup. Common formats are MM-DD-CCYY, CCYY-MM-DD.

##### end_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="end_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Stop date of an earning. Common formats are MM-DD-CCYY, CCYY-MM-DD.

##### frequency: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="frequency-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Needed if earning is applied differently from the payroll frequency (one time earning for example).<br  /> Max length: 5

##### goal: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="goal-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Dollar amount. The employee earning will stop when the goal amount is reached.<br  /> Decimal(12,2)

##### hours_or_units: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="hours_or_units-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The value is used in conjunction with the Rate field. When entering Group Term Life Insurance (GTL), it should contain the full amount of the group term life insurance policy. <br  /> Decimal(12,2)

##### is_self_insured: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="is_self_insured-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Used for ACA. If not entered, defaulted to Company earning setup.

##### job_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="job_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Job code associated with earnings. Must match Company setup.<br  /> Max length: 20

##### miscellaneous_info: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="miscellaneous_info-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Information to print on the check stub if agency is set up for this earning. <br  />Max length: 50

##### paid_towards_goal: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="paid_towards_goal-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Amount already paid to employee toward goal. <br  /> Decimal(12,2)

##### pay_period_maximum: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="pay_period_maximum-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Maximum amount of the earning on a single paycheck. <br  /> Decimal(12,2)

##### pay_period_minimum: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="pay_period_minimum-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Minimum amount of the earning on a single paycheck. <br  /> Decimal(12,2)

##### rate: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="rate-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Rate is used in conjunction with the hoursOrUnits field. <br  /> Decimal(12,2)

##### rate_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="rate_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Rate Code applies to additional pay rates entered for an employee. Must match Company setup. <br  /> Max length: 10

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Earning`](./paylocity_python_sdk/type/earning.py)
Earning Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/earnings` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.earnings.delete_by_code_and_start`<a id="paylocityearningsdelete_by_code_and_start"></a>

Delete Earning by Earning Code and Start Date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.earnings.delete_by_code_and_start(
    company_id="companyId_example",
    employee_id="employeeId_example",
    earning_code="earningCode_example",
    start_date="startDate_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### earning_code: `str`<a id="earning_code-str"></a>

Earning Code

##### start_date: `str`<a id="start_date-str"></a>

Start Date

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.earnings.get_all`<a id="paylocityearningsget_all"></a>

Get All Earnings returns all earnings for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = paylocity.earnings.get_all(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`EarningsGetAllResponse`](./paylocity_python_sdk/pydantic/earnings_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/earnings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.earnings.get_by_code_and_start`<a id="paylocityearningsget_by_code_and_start"></a>

Get Earnings returns the single earning with the provided earning code and start date for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_code_and_start_response = paylocity.earnings.get_by_code_and_start(
    company_id="companyId_example",
    employee_id="employeeId_example",
    earning_code="earningCode_example",
    start_date="startDate_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### earning_code: `str`<a id="earning_code-str"></a>

Earning Code

##### start_date: `str`<a id="start_date-str"></a>

Start Date

#### 🔄 Return<a id="🔄-return"></a>

[`Earning`](./paylocity_python_sdk/pydantic/earning.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.earnings.get_by_earning_code`<a id="paylocityearningsget_by_earning_code"></a>

Get Earnings returns all earnings with the provided earning code for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_earning_code_response = paylocity.earnings.get_by_earning_code(
    company_id="companyId_example",
    employee_id="employeeId_example",
    earning_code="earningCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### earning_code: `str`<a id="earning_code-str"></a>

Earning Code

#### 🔄 Return<a id="🔄-return"></a>

[`EarningsGetByEarningCodeResponse`](./paylocity_python_sdk/pydantic/earnings_get_by_earning_code_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.emergency_contacts.add_or_update`<a id="paylocityemergency_contactsadd_or_update"></a>

Sends new or updated employee emergency contacts directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.emergency_contacts.add_or_update(
    first_name={},
    last_name={},
    company_id="companyId_example",
    employee_id="employeeId_example",
    address1={},
    address2={},
    city={},
    country={},
    county={},
    email={},
    home_phone={},
    mobile_phone={},
    notes={},
    pager={},
    primary_phone={},
    priority={},
    relationship={},
    state={},
    sync_employee_info=True,
    work_extension={},
    work_phone={},
    zip={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="first_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Contact first name. <br  />Max length: 40

##### last_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="last_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Contact last name. <br  />Max length: 40

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### address1: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="address1-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

1st address line.

##### address2: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="address2-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

2nd address line.

##### city: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="city-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

City.

##### country: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="country-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

County.

##### county: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="county-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Country.  Must be a valid 3 character country code.  Common values are *USA* (United States), *CAN* (Canada).

##### email: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="email-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contact email.  Must be valid email address format.

##### home_phone: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="home_phone-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contact Home Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.

##### mobile_phone: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="mobile_phone-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contact Mobile Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.

##### notes: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="notes-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Notes. <br  />Max length: 1000

##### pager: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="pager-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contact Pager.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.

##### primary_phone: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="primary_phone-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Contact primary phone type.  Must match Company setup.  Valid  values are H (Home), M (Mobile), P (Pager), W (Work)

##### priority: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="priority-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Contact priority. Valid values are *P* (Primary) or *S* (Secondary).

##### relationship: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="relationship-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Required. Contact relationship.  Must match Company setup.  Common values are Spouse, Mother, Father.

##### state: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="state-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State or Province.  If U.S. address, must be valid 2 character state code.  Common values are *IL* (Illinois), *CA* (California).

##### sync_employee_info: `bool`<a id="sync_employee_info-bool"></a>

Valid values are *true* or *false*.

##### work_extension: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="work_extension-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Work Extension.

##### work_phone: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="work_phone-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contact Work Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.

##### zip: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="zip-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Postal code.  If U.S. address, must be a valid zip code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmergencyContact`](./paylocity_python_sdk/type/emergency_contact.py)
Emergency Contact Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/emergencyContacts` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee.add_to_paylocity`<a id="paylocityemployeeadd_to_paylocity"></a>

New Employee API sends new employee data directly to Paylocity Payroll/HR solution. Companies who use the New Hire Template in Paylocity Payroll/HR solution may require additional fields when hiring employees. New Employee API Requests will honor these required fields.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_paylocity_response = paylocity.employee.add_to_paylocity(
    company_id="companyId_example",
    additional_direct_deposit=[
        {}
    ],
    additional_rate=[
        {}
    ],
    benefit_setup={},
    birth_date={},
    company_fein={},
    company_name={},
    currency={},
    custom_boolean_fields=[
        {}
    ],
    custom_date_fields=[
        {}
    ],
    custom_drop_down_fields=[
        {}
    ],
    custom_number_fields=[
        {}
    ],
    custom_text_fields=[
        {}
    ],
    department_position={},
    disability_description={},
    emergency_contacts=[
        {}
    ],
    employee_id={},
    ethnicity={},
    federal_tax={},
    first_name={},
    gender={},
    home_address={},
    is_highly_compensated=True,
    is_smoker=True,
    last_name={},
    local_tax=[
        {}
    ],
    main_direct_deposit={},
    marital_status={},
    middle_name={},
    non_primary_state_tax={},
    owner_percent={},
    preferred_name={},
    primary_pay_rate={},
    primary_state_tax={},
    prior_last_name={},
    salutation={},
    ssn={},
    status={},
    suffix={},
    tax_setup={},
    veteran_description={},
    web_time={},
    work_address={},
    work_eligibility={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### additional_direct_deposit: [`EmployeeAdditionalDirectDeposit`](./paylocity_python_sdk/type/employee_additional_direct_deposit.py)<a id="additional_direct_deposit-employeeadditionaldirectdepositpaylocity_python_sdktypeemployee_additional_direct_depositpy"></a>

##### additional_rate: [`EmployeeAdditionalRate`](./paylocity_python_sdk/type/employee_additional_rate.py)<a id="additional_rate-employeeadditionalratepaylocity_python_sdktypeemployee_additional_ratepy"></a>

##### benefit_setup: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="benefit_setup-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

 Add or update setup values used for employee benefits integration, insurance plan settings, and ACA reporting.

##### birth_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="birth_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee birthdate. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.

##### company_fein: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="company_fein-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Company FEIN as defined in Paylocity Payroll/HR solution, applicable with GET requests only.<br  /> Max length: 20

##### company_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="company_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Company name as defined in Paylocity Payroll/HR solution, applicable with GET requests only.<br  /> Max length: 50

##### currency: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="currency-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee is paid in this currency. <br  />Max length: 30

##### custom_boolean_fields: [`EmployeeCustomBooleanFields`](./paylocity_python_sdk/type/employee_custom_boolean_fields.py)<a id="custom_boolean_fields-employeecustombooleanfieldspaylocity_python_sdktypeemployee_custom_boolean_fieldspy"></a>

##### custom_date_fields: [`EmployeeCustomDateFields`](./paylocity_python_sdk/type/employee_custom_date_fields.py)<a id="custom_date_fields-employeecustomdatefieldspaylocity_python_sdktypeemployee_custom_date_fieldspy"></a>

##### custom_drop_down_fields: [`EmployeeCustomDropDownFields`](./paylocity_python_sdk/type/employee_custom_drop_down_fields.py)<a id="custom_drop_down_fields-employeecustomdropdownfieldspaylocity_python_sdktypeemployee_custom_drop_down_fieldspy"></a>

##### custom_number_fields: [`EmployeeCustomNumberFields`](./paylocity_python_sdk/type/employee_custom_number_fields.py)<a id="custom_number_fields-employeecustomnumberfieldspaylocity_python_sdktypeemployee_custom_number_fieldspy"></a>

##### custom_text_fields: [`EmployeeCustomTextFields`](./paylocity_python_sdk/type/employee_custom_text_fields.py)<a id="custom_text_fields-employeecustomtextfieldspaylocity_python_sdktypeemployee_custom_text_fieldspy"></a>

##### department_position: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="department_position-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update home department cost center, position, supervisor, reviewer, employment type, EEO class, pay settings, and union information.

##### disability_description: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="disability_description-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Indicates if employee has disability status.

##### emergency_contacts: [`EmployeeEmergencyContacts`](./paylocity_python_sdk/type/employee_emergency_contacts.py)<a id="emergency_contacts-employeeemergencycontactspaylocity_python_sdktypeemployee_emergency_contactspy"></a>

##### employee_id: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="employee_id-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Leave blank to have Paylocity Payroll/HR solution automatically assign the next available employee ID.<br  />Max length: 10

##### ethnicity: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="ethnicity-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee ethnicity.<br  /> Max length: 10

##### federal_tax: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="federal_tax-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update federal tax amount type (taxCalculationCode), amount or percentage, filing status, and exemptions.

##### first_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="first_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee first name. <br  />Max length: 40

##### gender: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="gender-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee gender. Common values *M* (Male), *F* (Female). <br  />Max length: 1

##### home_address: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="home_address-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update employee's home address, personal phone numbers, and personal email.

##### is_highly_compensated: `bool`<a id="is_highly_compensated-bool"></a>

Indicates if employee meets the highly compensated employee criteria.

##### is_smoker: `bool`<a id="is_smoker-bool"></a>

Indicates if employee is a smoker.

##### last_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="last_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee last name. <br  />Max length: 40

##### local_tax: [`EmployeeLocalTax`](./paylocity_python_sdk/type/employee_local_tax.py)<a id="local_tax-employeelocaltaxpaylocity_python_sdktypeemployee_local_taxpy"></a>

##### main_direct_deposit: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="main_direct_deposit-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add the main direct deposit account. After deposits are made to any additional direct deposit accounts, the remaining net check is deposited in the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with what is provided on the request. GET API will not return direct deposit data.

##### marital_status: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="marital_status-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. <br  />Max length: 10

##### middle_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="middle_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee middle name.<br  /> Max length: 20

##### non_primary_state_tax: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="non_primary_state_tax-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update non-primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, supplemental check (specialCheckCalc), and reciprocity code information.

##### owner_percent: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="owner_percent-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Percentage of employee's ownership in the company, entered as a whole number. <br  /> Decimal (12,2)

##### preferred_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="preferred_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee preferred display name.<br  /> Max length: 20

##### primary_pay_rate: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="primary_pay_rate-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update hourly or salary pay rate, effective date, and pay frequency.

##### primary_state_tax: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="primary_state_tax-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, and supplemental check (specialCheckCalc) information. Only one primary state is allowed. Sending an updated primary state will replace the current primary state.

##### prior_last_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prior_last_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prior last name if applicable.<br  />Max length: 40

##### salutation: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="salutation-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee preferred salutation. <br  />Max length: 10

##### ssn: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="ssn-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee social security number. Leave it blank if valid social security number not available. <br  />Max length: 11

##### status: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="status-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update employee status, change reason, effective date, and adjusted seniority date. Note that companies that are still in Implementation cannot hire future employees.

##### suffix: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="suffix-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee name suffix. Common values are *Jr, Sr, II*.<br  />Max length: 30

##### tax_setup: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_setup-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add tax form, 1099 exempt reasons and notes, and 943 agricultural employee information. Once the employee receives wages, this information cannot be updated. Add or update SUI tax state, retirement plan, and statutory information.

##### veteran_description: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="veteran_description-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Indicates if employee is a veteran.

##### web_time: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="web_time-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update Web Time badge number and charge rate and synchronize Paylocity Payroll/HR solution and Web Time employee data.

##### work_address: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="work_address-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update employee's work address, phone numbers, and email. Work Location drop down field is not included.

##### work_eligibility: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="work_eligibility-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update I-9 work authorization information.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Employee`](./paylocity_python_sdk/type/employee.py)
Employee Model

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddToPaylocityResponse`](./paylocity_python_sdk/pydantic/employee_add_to_paylocity_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee.get_all_employees`<a id="paylocityemployeeget_all_employees"></a>

Get All Employees API will return employee data currently available in Paylocity Payroll/HR solution.
\
> 🚧 Maintenance Mode
> 
> _This API is in a limited support mode and certain resources will be moved to a sunset status in the next 18-24 months._
> 
> The [Employee Demographic API](ref:get_corehr-v1-companies-companyid-employees) should be used when possible in place of the Employee resources of this API

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_employees_response = paylocity.employee.get_all_employees(
    company_id="companyId_example",
    pagesize=1,
    pagenumber=1,
    includetotalcount=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### pagesize: `int`<a id="pagesize-int"></a>

Number of records per page. Default value is 25.

##### pagenumber: `int`<a id="pagenumber-int"></a>

Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.

##### includetotalcount: `bool`<a id="includetotalcount-bool"></a>

Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetAllEmployeesResponse`](./paylocity_python_sdk/pydantic/employee_get_all_employees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee.get_employee_data`<a id="paylocityemployeeget_employee_data"></a>

Get Employee API will return employee data currently available in Paylocity Payroll/HR solution.
\
> 🚧 Maintenance Mode
> 
> _This API is in a limited support mode and certain resources will be moved to a sunset status in the next 18-24 months._
> 
> The [Employee Demographic API](ref:get_corehr-v1-companies-companyid-employees-employeeid) should be used when possible in place of the Employee resources of this API

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_data_response = paylocity.employee.get_employee_data(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGetEmployeeDataResponse`](./paylocity_python_sdk/pydantic/employee_get_employee_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee.update_employee_data`<a id="paylocityemployeeupdate_employee_data"></a>

Update Employee API will update existing employee data in WebPay.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.employee.update_employee_data(
    company_id="companyId_example",
    employee_id="employeeId_example",
    additional_direct_deposit=[
        {}
    ],
    additional_rate=[
        {}
    ],
    benefit_setup={},
    birth_date={},
    company_fein={},
    company_name={},
    currency={},
    custom_boolean_fields=[
        {}
    ],
    custom_date_fields=[
        {}
    ],
    custom_drop_down_fields=[
        {}
    ],
    custom_number_fields=[
        {}
    ],
    custom_text_fields=[
        {}
    ],
    department_position={},
    disability_description={},
    emergency_contacts=[
        {}
    ],
    employee_id={},
    ethnicity={},
    federal_tax={},
    first_name={},
    gender={},
    home_address={},
    is_highly_compensated=True,
    is_smoker=True,
    last_name={},
    local_tax=[
        {}
    ],
    main_direct_deposit={},
    marital_status={},
    middle_name={},
    non_primary_state_tax={},
    owner_percent={},
    preferred_name={},
    primary_pay_rate={},
    primary_state_tax={},
    prior_last_name={},
    salutation={},
    ssn={},
    status={},
    suffix={},
    tax_setup={},
    veteran_description={},
    web_time={},
    work_address={},
    work_eligibility={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### requestBody: [`Employee`](./paylocity_python_sdk/type/employee.py)<a id="requestbody-employeepaylocity_python_sdktypeemployeepy"></a>

Employee Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee_(v1).create_new_employee_record`<a id="paylocityemployee_v1create_new_employee_record"></a>

This resource allows for the creation of a new employee record for a specified companyID.  Additional field objects may need to be added for companies that use the New Hire Template in the Paylocity HCM solution when hiring employees and have additional required fields.
 
> 🚧 Maintenance Mode
> 
> _This resource version is in a limited support mode and should not be used for new integrations.  Please use the latest version._


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.employee_(v1).create_new_employee_record(
    new_employee={
        "company_number": "company_number_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_employee: [`NewEmployee`](./paylocity_python_sdk/type/new_employee.py)<a id="new_employee-newemployeepaylocity_python_sdktypenew_employeepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeV1CreateNewEmployeeRecordRequest`](./paylocity_python_sdk/type/employee_v1_create_new_employee_record_request.py)
New Employee

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employee` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee_(v1).get_employee_data`<a id="paylocityemployee_v1get_employee_data"></a>

Get Employee API will return employee data currently available in Paylocity Payroll/HR solution.
 
> 🚧 Maintenance Mode
> 
> _This resource version is in a limited support mode and should not be used for new integrations.  Please use the latest version._


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_data_response = paylocity.employee_(v1).get_employee_data(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeV1`](./paylocity_python_sdk/pydantic/employee_v1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company/{companyId}/employee/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee_(v1).update_employee_data_to_paylocity`<a id="paylocityemployee_v1update_employee_data_to_paylocity"></a>

Update Employee API sends updates to employee data to Paylocity Payroll/HR solution.
 
> 🚧 Maintenance Mode
> 
> _This resource version is in a limited support mode and should not be used for new integrations.  Please use the latest version._


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.employee_(v1).update_employee_data_to_paylocity(
    update_employee={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### update_employee: [`UpdateEmployee`](./paylocity_python_sdk/type/update_employee.py)<a id="update_employee-updateemployeepaylocity_python_sdktypeupdate_employeepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeV1UpdateEmployeeDataToPaylocityRequest`](./paylocity_python_sdk/type/employee_v1_update_employee_data_to_paylocity_request.py)
UpdateEmployee

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/update-employee` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee_benefit_setup.add_or_update_benefit_setup`<a id="paylocityemployee_benefit_setupadd_or_update_benefit_setup"></a>

Sends new or updated employee benefit setup information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.employee_benefit_setup.add_or_update_benefit_setup(
    company_id="companyId_example",
    employee_id="employeeId_example",
    benefit_class={},
    benefit_class_effective_date={},
    benefit_salary={},
    benefit_salary_effective_date={},
    do_not_apply_administrative_period={},
    is_measure_aca_eligibility={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### benefit_class: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="benefit_class-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Benefit Class code. Values are configured in Paylocity Payroll/HR solution Company > Setup > Benefits > Classes.<br  />Max length: 30

##### benefit_class_effective_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="benefit_class_effective_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Date when Benefit Class takes effect. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.

##### benefit_salary: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="benefit_salary-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Salary used to configure benefits.<br  />Decimal(12,2)

##### benefit_salary_effective_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="benefit_salary_effective_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Date when Benefit Salary takes effect. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.

##### do_not_apply_administrative_period: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="do_not_apply_administrative_period-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Applicable only for HR Enhanced clients and Benefit Classes with ACA Employment Type of Full Time.

##### is_measure_aca_eligibility: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="is_measure_aca_eligibility-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Only valid for HR Enhanced clients and Benefit Classes that are ACA Employment Type of Full Time.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BenefitSetup`](./paylocity_python_sdk/type/benefit_setup.py)
BenefitSetup Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/benefitSetup` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.employee_staging.add_new_employee_to_web_link`<a id="paylocityemployee_stagingadd_new_employee_to_web_link"></a>

Add new employee to Web Link will send partially completed or potentially erroneous new hire record to Web Link, where it can be corrected and competed by company administrator or authorized Paylocity Service Bureau employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_employee_to_web_link_response = paylocity.employee_staging.add_new_employee_to_web_link(
    company_id="companyId_example",
    additional_direct_deposit=[
        {}
    ],
    benefit_setup=[
        {}
    ],
    birth_date={},
    custom_boolean_fields=[
        {}
    ],
    custom_date_fields=[
        {}
    ],
    custom_drop_down_fields=[
        {}
    ],
    custom_number_fields=[
        {}
    ],
    custom_text_fields=[
        {}
    ],
    department_position=[
        {}
    ],
    disability_description={},
    employee_id={},
    ethnicity={},
    federal_tax=[
        {}
    ],
    first_name={},
    fitw_exempt_reason={},
    futa_exempt_reason={},
    gender={},
    home_address=[
        {}
    ],
    is_employee943={},
    is_smoker={},
    last_name={},
    local_tax=[
        {}
    ],
    main_direct_deposit=[
        {}
    ],
    marital_status={},
    med_exempt_reason={},
    middle_name={},
    non_primary_state_tax=[
        {}
    ],
    preferred_name={},
    primary_pay_rate=[
        {}
    ],
    primary_state_tax=[
        {}
    ],
    prior_last_name={},
    salutation={},
    sitw_exempt_reason={},
    ss_exempt_reason={},
    ssn={},
    status=[
        {}
    ],
    suffix={},
    sui_exempt_reason={},
    sui_state={},
    tax_distribution_code1099_r={},
    tax_form={},
    veteran_description={},
    web_time={},
    work_address=[
        {}
    ],
    work_eligibility=[
        {}
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### additional_direct_deposit: [`StagedEmployeeAdditionalDirectDeposit`](./paylocity_python_sdk/type/staged_employee_additional_direct_deposit.py)<a id="additional_direct_deposit-stagedemployeeadditionaldirectdepositpaylocity_python_sdktypestaged_employee_additional_direct_depositpy"></a>

##### benefit_setup: [`StagedEmployeeBenefitSetup`](./paylocity_python_sdk/type/staged_employee_benefit_setup.py)<a id="benefit_setup-stagedemployeebenefitsetuppaylocity_python_sdktypestaged_employee_benefit_setuppy"></a>

##### birth_date: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="birth_date-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee birthdate. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.

##### custom_boolean_fields: [`StagedEmployeeCustomBooleanFields`](./paylocity_python_sdk/type/staged_employee_custom_boolean_fields.py)<a id="custom_boolean_fields-stagedemployeecustombooleanfieldspaylocity_python_sdktypestaged_employee_custom_boolean_fieldspy"></a>

##### custom_date_fields: [`StagedEmployeeCustomDateFields`](./paylocity_python_sdk/type/staged_employee_custom_date_fields.py)<a id="custom_date_fields-stagedemployeecustomdatefieldspaylocity_python_sdktypestaged_employee_custom_date_fieldspy"></a>

##### custom_drop_down_fields: [`StagedEmployeeCustomDropDownFields`](./paylocity_python_sdk/type/staged_employee_custom_drop_down_fields.py)<a id="custom_drop_down_fields-stagedemployeecustomdropdownfieldspaylocity_python_sdktypestaged_employee_custom_drop_down_fieldspy"></a>

##### custom_number_fields: [`StagedEmployeeCustomNumberFields`](./paylocity_python_sdk/type/staged_employee_custom_number_fields.py)<a id="custom_number_fields-stagedemployeecustomnumberfieldspaylocity_python_sdktypestaged_employee_custom_number_fieldspy"></a>

##### custom_text_fields: [`StagedEmployeeCustomTextFields`](./paylocity_python_sdk/type/staged_employee_custom_text_fields.py)<a id="custom_text_fields-stagedemployeecustomtextfieldspaylocity_python_sdktypestaged_employee_custom_text_fieldspy"></a>

##### department_position: [`StagedEmployeeDepartmentPosition`](./paylocity_python_sdk/type/staged_employee_department_position.py)<a id="department_position-stagedemployeedepartmentpositionpaylocity_python_sdktypestaged_employee_department_positionpy"></a>

##### disability_description: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="disability_description-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Indicates if employee has disability status.

##### employee_id: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="employee_id-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Leave blank to have Paylocity Payroll/HR solution automatically assign the next available employee ID.<br  /> Max length: 10

##### ethnicity: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="ethnicity-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee ethnicity.<br  /> Max length: 10

##### federal_tax: [`StagedEmployeeFederalTax`](./paylocity_python_sdk/type/staged_employee_federal_tax.py)<a id="federal_tax-stagedemployeefederaltaxpaylocity_python_sdktypestaged_employee_federal_taxpy"></a>

##### first_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="first_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee first name. <br  />Max length: 40

##### fitw_exempt_reason: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="fitw_exempt_reason-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Reason code for FITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30

##### futa_exempt_reason: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="futa_exempt_reason-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Reason code for FUTA exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).<br  /> Max length: 30

##### gender: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="gender-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee gender. Common values *M* (Male), *F* (Female). <br  />Max length: 1

##### home_address: [`StagedEmployeeHomeAddress`](./paylocity_python_sdk/type/staged_employee_home_address.py)<a id="home_address-stagedemployeehomeaddresspaylocity_python_sdktypestaged_employee_home_addresspy"></a>

##### is_employee943: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="is_employee943-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Indicates if employee in agriculture or farming.

##### is_smoker: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="is_smoker-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Indicates if employee is a smoker.

##### last_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="last_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee last name. <br  />Max length: 40

##### local_tax: [`StagedEmployeeLocalTax`](./paylocity_python_sdk/type/staged_employee_local_tax.py)<a id="local_tax-stagedemployeelocaltaxpaylocity_python_sdktypestaged_employee_local_taxpy"></a>

##### main_direct_deposit: [`StagedEmployeeMainDirectDeposit`](./paylocity_python_sdk/type/staged_employee_main_direct_deposit.py)<a id="main_direct_deposit-stagedemployeemaindirectdepositpaylocity_python_sdktypestaged_employee_main_direct_depositpy"></a>

##### marital_status: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="marital_status-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. <br  />Max length: 10

##### med_exempt_reason: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="med_exempt_reason-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Reason code for Medicare exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).<br  /> Max length: 30

##### middle_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="middle_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee middle name.<br  /> Max length: 20

##### non_primary_state_tax: [`StagedEmployeeNonPrimaryStateTax`](./paylocity_python_sdk/type/staged_employee_non_primary_state_tax.py)<a id="non_primary_state_tax-stagedemployeenonprimarystatetaxpaylocity_python_sdktypestaged_employee_non_primary_state_taxpy"></a>

##### preferred_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="preferred_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee preferred display name.<br  /> Max length: 20

##### primary_pay_rate: [`StagedEmployeePrimaryPayRate`](./paylocity_python_sdk/type/staged_employee_primary_pay_rate.py)<a id="primary_pay_rate-stagedemployeeprimarypayratepaylocity_python_sdktypestaged_employee_primary_pay_ratepy"></a>

##### primary_state_tax: [`StagedEmployeePrimaryStateTax`](./paylocity_python_sdk/type/staged_employee_primary_state_tax.py)<a id="primary_state_tax-stagedemployeeprimarystatetaxpaylocity_python_sdktypestaged_employee_primary_state_taxpy"></a>

##### prior_last_name: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prior_last_name-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prior last name if applicable.<br  />Max length: 40

##### salutation: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="salutation-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee preferred salutation. <br  />Max length: 10

##### sitw_exempt_reason: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="sitw_exempt_reason-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Reason code for SITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30

##### ss_exempt_reason: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="ss_exempt_reason-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Reason code for Social Security exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30

##### ssn: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="ssn-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee social security number. Leave it blank if valid social security number not available. <br  />Max length: 11

##### status: [`StagedEmployeeStatus`](./paylocity_python_sdk/type/staged_employee_status.py)<a id="status-stagedemployeestatuspaylocity_python_sdktypestaged_employee_statuspy"></a>

##### suffix: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="suffix-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee name suffix. Common values are *Jr, Sr, II*.<br  />Max length: 30

##### sui_exempt_reason: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="sui_exempt_reason-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Reason code for SUI exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30

##### sui_state: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="sui_state-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee SUI (State Unemployment Insurance) state. <br  />Max length: 2

##### tax_distribution_code1099_r: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_distribution_code1099_r-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee 1099R distribution code. Common values are *7* (Normal Distribution), *F* (Charitable Gift Annuity). <br  />Max length: 1

##### tax_form: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_form-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee tax form for reporting income. Valid values are *W2, 1099M, 1099R*. Default is W2. <br  />Max length: 15

##### veteran_description: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="veteran_description-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Indicates if employee is a veteran.

##### web_time: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="web_time-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add Web Time badge number and charge rate and synchronize Paylocity Payroll/HR solution and Web Time employee data.

##### work_address: [`StagedEmployeeWorkAddress`](./paylocity_python_sdk/type/staged_employee_work_address.py)<a id="work_address-stagedemployeeworkaddresspaylocity_python_sdktypestaged_employee_work_addresspy"></a>

##### work_eligibility: [`StagedEmployeeWorkEligibility`](./paylocity_python_sdk/type/staged_employee_work_eligibility.py)<a id="work_eligibility-stagedemployeeworkeligibilitypaylocity_python_sdktypestaged_employee_work_eligibilitypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StagedEmployee`](./paylocity_python_sdk/type/staged_employee.py)
StagedEmployee Model

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeStagingAddNewEmployeeToWebLinkResponse`](./paylocity_python_sdk/pydantic/employee_staging_add_new_employee_to_web_link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/weblinkstaging/companies/{companyId}/employees/newemployees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_tax.create_or_update_local_taxes`<a id="paylocitylocal_taxcreate_or_update_local_taxes"></a>

Add Local Tax sends new local tax information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.local_tax.create_or_update_local_taxes(
    company_id="companyId_example",
    employee_id="employeeId_example",
    exemptions={},
    exemptions2={},
    filing_status={},
    resident_psd={},
    tax_code={},
    work_psd={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### exemptions: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Local tax exemptions value.<br  />Decimal (12,2)

##### exemptions2: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions2-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Local tax exemptions 2 value.<br  />Decimal (12,2)

##### filing_status: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="filing_status-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee local tax filing status. Must match specific local tax setup. <br  /> Max length: 50

##### resident_psd: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="resident_psd-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Resident PSD (political subdivision code) applicable in PA. Must match Company setup.<br  /> Max length: 9

##### tax_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Local tax code.<br  />Max length: 50

##### work_psd: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="work_psd-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Work location PSD. Must match Company setup. <br  /> Max length: 9

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocalTax`](./paylocity_python_sdk/type/local_tax.py)
localTax Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/localTaxes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_tax.get_all_taxes_for_employee`<a id="paylocitylocal_taxget_all_taxes_for_employee"></a>

Get All Local Taxes returns all local tax information for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_taxes_for_employee_response = paylocity.local_tax.get_all_taxes_for_employee(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`LocalTaxGetAllTaxesForEmployeeResponse`](./paylocity_python_sdk/pydantic/local_tax_get_all_taxes_for_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/localTaxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_tax.get_for_tax_code`<a id="paylocitylocal_taxget_for_tax_code"></a>

Get Local Tax for Tax Code returns local tax information for the specific tax code for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_for_tax_code_response = paylocity.local_tax.get_for_tax_code(
    company_id="companyId_example",
    employee_id="employeeId_example",
    tax_code="taxCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### tax_code: `str`<a id="tax_code-str"></a>

Tax Code

#### 🔄 Return<a id="🔄-return"></a>

[`LocalTax`](./paylocity_python_sdk/pydantic/local_tax.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_tax.remove_for_tax_code`<a id="paylocitylocal_taxremove_for_tax_code"></a>

Delete Local Tax for Tax Code deletes the local tax code from Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.local_tax.remove_for_tax_code(
    company_id="companyId_example",
    employee_id="employeeId_example",
    tax_code="taxCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### tax_code: `str`<a id="tax_code-str"></a>

Tax Code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_tax.update_for_tax_code`<a id="paylocitylocal_taxupdate_for_tax_code"></a>

Update Local Tax sends updated local tax code information for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.local_tax.update_for_tax_code(
    company_id="companyId_example",
    employee_id="employeeId_example",
    tax_code="taxCode_example",
    exemptions={},
    exemptions2={},
    filing_status={},
    resident_psd={},
    tax_code={},
    work_psd={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### tax_code: `str`<a id="tax_code-str"></a>

Tax Code

##### requestBody: [`LocalTax`](./paylocity_python_sdk/type/local_tax.py)<a id="requestbody-localtaxpaylocity_python_sdktypelocal_taxpy"></a>

localTax Model (Note: taxCode can be included in the localTax model but will be ignored)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_taxes.add_new_tax`<a id="paylocitylocal_taxesadd_new_tax"></a>

Sends new employee local tax information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.local_taxes.add_new_tax(
    company_id="companyId_example",
    employee_id="employeeId_example",
    exemptions={},
    exemptions2={},
    filing_status={},
    resident_psd={},
    tax_code={},
    work_psd={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### exemptions: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Local tax exemptions value.<br  />Decimal (12,2)

##### exemptions2: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions2-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Local tax exemptions 2 value.<br  />Decimal (12,2)

##### filing_status: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="filing_status-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee local tax filing status. Must match specific local tax setup. <br  /> Max length: 50

##### resident_psd: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="resident_psd-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Resident PSD (political subdivision code) applicable in PA. Must match Company setup.<br  /> Max length: 9

##### tax_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Local tax code.<br  />Max length: 50

##### work_psd: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="work_psd-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Work location PSD. Must match Company setup. <br  /> Max length: 9

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocalTax`](./paylocity_python_sdk/type/local_tax.py)
LocalTax Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/localTaxes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_taxes.delete_by_tax_code`<a id="paylocitylocal_taxesdelete_by_tax_code"></a>

Delete local tax by tax code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.local_taxes.delete_by_tax_code(
    company_id="companyId_example",
    employee_id="employeeId_example",
    tax_code="taxCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### tax_code: `str`<a id="tax_code-str"></a>

Tax Code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_taxes.get_all_for_employee`<a id="paylocitylocal_taxesget_all_for_employee"></a>

Returns all local taxes for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_employee_response = paylocity.local_taxes.get_all_for_employee(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`LocalTaxesGetAllForEmployeeResponse`](./paylocity_python_sdk/pydantic/local_taxes_get_all_for_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/localTaxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.local_taxes.get_by_tax_code`<a id="paylocitylocal_taxesget_by_tax_code"></a>

Returns all local taxes with the provided tax code for the selected employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_tax_code_response = paylocity.local_taxes.get_by_tax_code(
    company_id="companyId_example",
    employee_id="employeeId_example",
    tax_code="taxCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### tax_code: `str`<a id="tax_code-str"></a>

Tax Code

#### 🔄 Return<a id="🔄-return"></a>

[`LocalTaxesGetByTaxCodeResponse`](./paylocity_python_sdk/pydantic/local_taxes_get_by_tax_code_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.non_primary_state_tax.add_or_update_state_tax`<a id="paylocitynon_primary_state_taxadd_or_update_state_tax"></a>

Sends new or updated employee non-primary state tax information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.non_primary_state_tax.add_or_update_state_tax(
    company_id="companyId_example",
    employee_id="employeeId_example",
    amount={},
    deductions_amount=3.14,
    dependents_amount=3.14,
    exemptions={},
    exemptions2={},
    filing_status={},
    higher_rate=True,
    other_income_amount=3.14,
    percentage={},
    reciprocity_code={},
    special_check_calc={},
    tax_calculation_code={},
    tax_code={},
    w4_form_year=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### amount: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="amount-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax code.<br  /> Max length: 50

##### deductions_amount: `Union[int, float]`<a id="deductions_amount-unionint-float"></a>

Box 4(b) on form W4 (year 2020 or later): Deductions amount. <br  />Decimal (12,2)

##### dependents_amount: `Union[int, float]`<a id="dependents_amount-unionint-float"></a>

Box 3 on form W4 (year 2020 or later): Total dependents amount. <br  />Decimal (12,2)

##### exemptions: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax exemptions value.<br  />Decimal (12,2)

##### exemptions2: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions2-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax exemptions 2 value.<br  />Decimal (12,2)

##### filing_status: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="filing_status-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee state tax filing status. Common values are *S* (Single), *M* (Married).<br  />Max length: 50

##### higher_rate: `bool`<a id="higher_rate-bool"></a>

Box 2(c) on form W4 (year 2020 or later): Multiple Jobs or Spouse Works. <br  />Boolean

##### other_income_amount: `Union[int, float]`<a id="other_income_amount-unionint-float"></a>

Box 4(a) on form W4 (year 2020 or later): Other income amount. <br  />Decimal (12,2)

##### percentage: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="percentage-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State Tax percentage. <br  />Decimal (12,2)

##### reciprocity_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="reciprocity_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Non-primary state tax reciprocity code.<br  /> Max length: 50

##### special_check_calc: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="special_check_calc-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Supplemental check calculation code. Common values are *Blocked* (Taxes blocked on Supplemental checks), *Supp* (Use supplemental Tax Rate-Code). <br  />Max length: 10

##### tax_calculation_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_calculation_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). <br  />Max length: 10

##### tax_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax code.<br  /> Max length: 50

##### w4_form_year: `int`<a id="w4_form_year-int"></a>

The state W4 form year <br  />Integer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NonPrimaryStateTax`](./paylocity_python_sdk/type/non_primary_state_tax.py)
Non-Primary State Tax Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/nonprimaryStateTax` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.onboarding.add_employee_to_onboarding`<a id="paylocityonboardingadd_employee_to_onboarding"></a>

Onboarding API sends employee data into Paylocity Onboarding to help ensure an easy and accurate hiring process for subsequent completion into Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.onboarding.add_employee_to_onboarding(
    first_name="string_example",
    last_name="string_example",
    company_id="companyId_example",
    employee_id="string_example",
    address1="string_example",
    address2="string_example",
    auto_pay_type="string_example",
    base_rate=3.14,
    city="string_example",
    cost_center1="string_example",
    cost_center2="string_example",
    cost_center3="string_example",
    default_hours=3.14,
    employee_status="string_example",
    employment_type="string_example",
    federal_filing_status="string_example",
    sex="string_example",
    hire_date="string_example",
    home_phone="string_example",
    marital_status="string_example",
    personal_mobile_phone="string_example",
    pay_frequency="string_example",
    personal_email_address="string_example",
    pay_type="string_example",
    rate_per="string_example",
    salary=3.14,
    state="string_example",
    ssn="string_example",
    state_filing_status="string_example",
    sui_state="string_example",
    tax_form="string_example",
    tax_state="string_example",
    user_name="string_example",
    work_email_address="string_example",
    zip="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

Employee first name. <br  />Max length: 40

##### last_name: `str`<a id="last_name-str"></a>

Employee last name. <br  />Max length: 40

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

(optional) The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### address1: `str`<a id="address1-str"></a>

Employee home 1st address line. <br  />Max length: 40

##### address2: `str`<a id="address2-str"></a>

Employee home 2nd address line. <br  />Max length: 40

##### auto_pay_type: `str`<a id="auto_pay_type-str"></a>

Valid values are *N, D, S. (N- employee won't automatically receive a salary or hours during payroll, D - employee will be automatically paid in defaultHours during payroll, S - employee will be automatically paid Salary amount during payroll)*. <br  />Max length: 3

##### base_rate: `Union[int, float]`<a id="base_rate-unionint-float"></a>

Employee base rate, used for Hourly employees. <br  />Decimal (12,2)

##### city: `str`<a id="city-str"></a>

Employee home city. <br  />Max length: 40

##### cost_center1: `str`<a id="cost_center1-str"></a>

Employer defined location, like *branch, division, department, etc.* Must match Company setup. <br  />Max length: 10

##### cost_center2: `str`<a id="cost_center2-str"></a>

Employer defined location, like *branch, division, department, etc.* Must match Company setup. <br  />Max length: 10

##### cost_center3: `str`<a id="cost_center3-str"></a>

Employer defined location, like *branch, division, department, etc.* Must match Company setup. <br  />Max length: 10

##### default_hours: `Union[int, float]`<a id="default_hours-unionint-float"></a>

Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. <br  />Decimal (12,2)

##### employee_status: `str`<a id="employee_status-str"></a>

Employee current work status. Common values are *A (Active), L (Leave of Absence), T (Terminated)*. <br  />Max length: 20

##### employment_type: `str`<a id="employment_type-str"></a>

Employee current employment type. Common values RFT *(Regular Full Time), RPT (Regular Part Time), SNL (Seasonal), TFT (Temporary Full Time), TPT (Temporary Part Time)*. <br  />Max length: 10

##### federal_filing_status: `str`<a id="federal_filing_status-str"></a>

Employee federal filing status. Common values *M (Married), S (Single)*. <br  />Max length: 10

##### sex: `str`<a id="sex-str"></a>

Employee gender. Common values *M (Male), F (Female)*. <br  />Max length: 1

##### hire_date: `str`<a id="hire_date-str"></a>

Employee hired date. Common formats are MM-DD-CCYY, CCYY-MM-DD

##### home_phone: `str`<a id="home_phone-str"></a>

Employee home phone number. <br  />Max length: 12

##### marital_status: `str`<a id="marital_status-str"></a>

Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. <br  />Max length: 10

##### personal_mobile_phone: `str`<a id="personal_mobile_phone-str"></a>

Employee personal mobile phone number. <br  />Max length: 12

##### pay_frequency: `str`<a id="pay_frequency-str"></a>

Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. <br  />Max length: 5

##### personal_email_address: `str`<a id="personal_email_address-str"></a>

Employee personal email address. <br  />Max length: 50

##### pay_type: `str`<a id="pay_type-str"></a>

Employee pay type. Valid values are *Hourly or Salary*. <br  />Max length: 10

##### rate_per: `str`<a id="rate_per-str"></a>

Employee base rate frequency used with payType Hourly. Common values are *Hour or Week*. Default is Hour <br  />Max length: 10

##### salary: `Union[int, float]`<a id="salary-unionint-float"></a>

Employee gross salary per pay period used with payType Salary. <br  />Decimal (12,2)

##### state: `str`<a id="state-str"></a>

Employee home state. <br  />Max length: 2

##### ssn: `str`<a id="ssn-str"></a>

Employee social security number. Leave it blank if valid social security number not available. <br  />Max length: 11

##### state_filing_status: `str`<a id="state_filing_status-str"></a>

Employee state filing status. Common values are *M (Married), S (Single)*. <br  />Max length: 50

##### sui_state: `str`<a id="sui_state-str"></a>

Employee SUI (State Unemployment Insurance) state. <br  />Max length: 2

##### tax_form: `str`<a id="tax_form-str"></a>

Employee tax form for reporting income. Valid values are *W2, 1099M, 1099R*. Default is W2. <br  />Max length: 15

##### tax_state: `str`<a id="tax_state-str"></a>

Employee primary tax state. <br  />Max Length: 2

##### user_name: `str`<a id="user_name-str"></a>

Required. Employer assigned username to log into Onboarding. Duplicate usernames are not allowed. <br  />Must be between 3 and 20 characters and cannot have special characters other than . (period) and _ (underscore)

##### work_email_address: `str`<a id="work_email_address-str"></a>

Employee work email. <br  />Max length: 50

##### zip: `str`<a id="zip-str"></a>

Employee home zip code. <br  />Max length: 10

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Onboarding`](./paylocity_python_sdk/type/onboarding.py)
onboarding Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{companyId}/onboarding/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.pay_statements.get_details_by_year`<a id="paylocitypay_statementsget_details_by_year"></a>

Get pay statement details API will return employee pay statement details data currently available in Paylocity Payroll/HR solution for the specified year.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_year_response = paylocity.pay_statements.get_details_by_year(
    company_id="companyId_example",
    employee_id="employeeId_example",
    year="year_example",
    pagesize=1,
    pagenumber=1,
    includetotalcount=True,
    codegroup="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### year: `str`<a id="year-str"></a>

The year for which to retrieve pay statement data

##### pagesize: `int`<a id="pagesize-int"></a>

Number of records per page. Default value is 25.

##### pagenumber: `int`<a id="pagenumber-int"></a>

Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.

##### includetotalcount: `bool`<a id="includetotalcount-bool"></a>

Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.

##### codegroup: `str`<a id="codegroup-str"></a>

Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.

#### 🔄 Return<a id="🔄-return"></a>

[`PayStatementsGetDetailsByYearResponse`](./paylocity_python_sdk/pydantic/pay_statements_get_details_by_year_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.pay_statements.get_details_by_year_and_check_date`<a id="paylocitypay_statementsget_details_by_year_and_check_date"></a>

Get pay statement details API will return employee pay statement detail data currently available in Paylocity Payroll/HR solution for the specified year and check date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_year_and_check_date_response = paylocity.pay_statements.get_details_by_year_and_check_date(
    company_id="companyId_example",
    employee_id="employeeId_example",
    year="year_example",
    check_date="checkDate_example",
    pagesize=1,
    pagenumber=1,
    includetotalcount=True,
    codegroup="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### year: `str`<a id="year-str"></a>

The year for which to retrieve pay statement data

##### check_date: `str`<a id="check_date-str"></a>

The check date for which to retrieve pay statement data

##### pagesize: `int`<a id="pagesize-int"></a>

Number of records per page. Default value is 25.

##### pagenumber: `int`<a id="pagenumber-int"></a>

Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.

##### includetotalcount: `bool`<a id="includetotalcount-bool"></a>

Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.

##### codegroup: `str`<a id="codegroup-str"></a>

Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.

#### 🔄 Return<a id="🔄-return"></a>

[`PayStatementsGetDetailsByYearAndCheckDateResponse`](./paylocity_python_sdk/pydantic/pay_statements_get_details_by_year_and_check_date_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}/{checkDate}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.pay_statements.get_summary_by_year`<a id="paylocitypay_statementsget_summary_by_year"></a>

Get pay statement summary API will return employee pay statement summary data currently available in Paylocity Payroll/HR solution for the specified year.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_summary_by_year_response = paylocity.pay_statements.get_summary_by_year(
    company_id="companyId_example",
    employee_id="employeeId_example",
    year="year_example",
    pagesize=1,
    pagenumber=1,
    includetotalcount=True,
    codegroup="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### year: `str`<a id="year-str"></a>

The year for which to retrieve pay statement data

##### pagesize: `int`<a id="pagesize-int"></a>

Number of records per page. Default value is 25.

##### pagenumber: `int`<a id="pagenumber-int"></a>

Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.

##### includetotalcount: `bool`<a id="includetotalcount-bool"></a>

Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.

##### codegroup: `str`<a id="codegroup-str"></a>

Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.

#### 🔄 Return<a id="🔄-return"></a>

[`PayStatementsGetSummaryByYearResponse`](./paylocity_python_sdk/pydantic/pay_statements_get_summary_by_year_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.pay_statements.get_summary_data`<a id="paylocitypay_statementsget_summary_data"></a>

Get pay statement summary API will return employee pay statement summary data currently available in Paylocity Payroll/HR solution for the specified year and check date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_summary_data_response = paylocity.pay_statements.get_summary_data(
    company_id="companyId_example",
    employee_id="employeeId_example",
    year="year_example",
    check_date="checkDate_example",
    pagesize=1,
    pagenumber=1,
    includetotalcount=True,
    codegroup="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### year: `str`<a id="year-str"></a>

The year for which to retrieve pay statement data

##### check_date: `str`<a id="check_date-str"></a>

The check date for which to retrieve pay statement data

##### pagesize: `int`<a id="pagesize-int"></a>

Number of records per page. Default value is 25.

##### pagenumber: `int`<a id="pagenumber-int"></a>

Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.

##### includetotalcount: `bool`<a id="includetotalcount-bool"></a>

Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.

##### codegroup: `str`<a id="codegroup-str"></a>

Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.

#### 🔄 Return<a id="🔄-return"></a>

[`PayStatementsGetSummaryDataResponse`](./paylocity_python_sdk/pydantic/pay_statements_get_summary_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.primary_state_tax.add_or_update_tax`<a id="paylocityprimary_state_taxadd_or_update_tax"></a>

Sends new or updated employee primary state tax information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.primary_state_tax.add_or_update_tax(
    company_id="companyId_example",
    employee_id="employeeId_example",
    amount={},
    deductions_amount=3.14,
    dependents_amount=3.14,
    exemptions={},
    exemptions2={},
    filing_status={},
    higher_rate=True,
    other_income_amount=3.14,
    percentage={},
    special_check_calc={},
    tax_calculation_code={},
    tax_code={},
    w4_form_year=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### amount: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="amount-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax code.<br  /> Max length: 50

##### deductions_amount: `Union[int, float]`<a id="deductions_amount-unionint-float"></a>

Box 4(b) on form W4 (year 2020 or later): Deductions amount. <br  />Decimal (12,2)

##### dependents_amount: `Union[int, float]`<a id="dependents_amount-unionint-float"></a>

Box 3 on form W4 (year 2020 or later): Total dependents amount. <br  />Decimal (12,2)

##### exemptions: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax exemptions value.<br  />Decimal (12,2)

##### exemptions2: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="exemptions2-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax exemptions 2 value.<br  />Decimal (12,2)

##### filing_status: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="filing_status-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employee state tax filing status. Common values are *S* (Single), *M* (Married).<br  />Max length: 50

##### higher_rate: `bool`<a id="higher_rate-bool"></a>

Box 2(c) on form W4 (year 2020 or later): Multiple Jobs or Spouse Works. <br  />Boolean

##### other_income_amount: `Union[int, float]`<a id="other_income_amount-unionint-float"></a>

Box 4(a) on form W4 (year 2020 or later): Other income amount. <br  />Decimal (12,2)

##### percentage: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="percentage-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State Tax percentage. <br  />Decimal (12,2)

##### special_check_calc: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="special_check_calc-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Supplemental check calculation code. Common values are *Blocked* (Taxes blocked on Supplemental checks), *Supp* (Use supplemental Tax Rate-Code). <br  />Max length: 10

##### tax_calculation_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_calculation_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). <br  />Max length: 10

##### tax_code: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="tax_code-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

State tax code.<br  /> Max length: 50

##### w4_form_year: `int`<a id="w4_form_year-int"></a>

The state W4 form year <br  />Integer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StateTax`](./paylocity_python_sdk/type/state_tax.py)
Primary State Tax Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/primaryStateTax` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.sensitive_data.add_or_update_employee_sensitive_data`<a id="paylocitysensitive_dataadd_or_update_employee_sensitive_data"></a>

Sends new or updated employee sensitive data information directly to Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paylocity.sensitive_data.add_or_update_employee_sensitive_data(
    company_id="companyId_example",
    employee_id="employeeId_example",
    disability={},
    ethnicity={},
    gender={},
    veteran={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

##### disability: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="disability-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update disability data.

##### ethnicity: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="ethnicity-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update ethnicity data.

##### gender: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="gender-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update gender data.

##### veteran: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="veteran-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Add or update veteran data.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SensitiveData`](./paylocity_python_sdk/type/sensitive_data.py)
Sensitive Data Model

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/sensitivedata` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paylocity.sensitive_data.get_employee_sensitive_data`<a id="paylocitysensitive_dataget_employee_sensitive_data"></a>

Gets employee sensitive data information directly from Paylocity Payroll/HR solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_sensitive_data_response = paylocity.sensitive_data.get_employee_sensitive_data(
    company_id="companyId_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Paylocity Company Identifier. This is the unique value provided by Paylocity to each specific Payroll Entity.                  **Allowable Values:**                  9 char max

##### employee_id: `str`<a id="employee_id-str"></a>

The Paylocity Employee ID. This is a unique value per Paylocity Company ID.  **Allowable Values:**  10 char max

#### 🔄 Return<a id="🔄-return"></a>

[`SensitiveDataGetEmployeeSensitiveDataResponse`](./paylocity_python_sdk/pydantic/sensitive_data_get_employee_sensitive_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{companyId}/employees/{employeeId}/sensitivedata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
