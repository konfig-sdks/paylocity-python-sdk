import typing_extensions

from paylocity_python_sdk.apis.tags import TagValues
from paylocity_python_sdk.apis.tags.local_tax_api import LocalTaxApi
from paylocity_python_sdk.apis.tags.earnings_api import EarningsApi
from paylocity_python_sdk.apis.tags.deduction_api import DeductionApi
from paylocity_python_sdk.apis.tags.employee_api import EmployeeApi
from paylocity_python_sdk.apis.tags.local_taxes_api import LocalTaxesApi
from paylocity_python_sdk.apis.tags.pay_statements_api import PayStatementsApi
from paylocity_python_sdk.apis.tags.employee_v1_api import EmployeeV1Api
from paylocity_python_sdk.apis.tags.sensitive_data_api import SensitiveDataApi
from paylocity_python_sdk.apis.tags.onboarding_api import OnboardingApi
from paylocity_python_sdk.apis.tags.additional_rates_api import AdditionalRatesApi
from paylocity_python_sdk.apis.tags.client_credentials_api import ClientCredentialsApi
from paylocity_python_sdk.apis.tags.company_codes_api import CompanyCodesApi
from paylocity_python_sdk.apis.tags.company_specific_schema_api import CompanySpecificSchemaApi
from paylocity_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from paylocity_python_sdk.apis.tags.direct_deposit_api import DirectDepositApi
from paylocity_python_sdk.apis.tags.emergency_contacts_api import EmergencyContactsApi
from paylocity_python_sdk.apis.tags.employee_benefit_setup_api import EmployeeBenefitSetupApi
from paylocity_python_sdk.apis.tags.employee_staging_api import EmployeeStagingApi
from paylocity_python_sdk.apis.tags.non_primary_state_tax_api import NonPrimaryStateTaxApi
from paylocity_python_sdk.apis.tags.primary_state_tax_api import PrimaryStateTaxApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.LOCAL_TAX: LocalTaxApi,
        TagValues.EARNINGS: EarningsApi,
        TagValues.DEDUCTION: DeductionApi,
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.LOCAL_TAXES: LocalTaxesApi,
        TagValues.PAY_STATEMENTS: PayStatementsApi,
        TagValues.EMPLOYEE_V1: EmployeeV1Api,
        TagValues.SENSITIVE_DATA: SensitiveDataApi,
        TagValues.ONBOARDING: OnboardingApi,
        TagValues.ADDITIONAL_RATES: AdditionalRatesApi,
        TagValues.CLIENT_CREDENTIALS: ClientCredentialsApi,
        TagValues.COMPANY_CODES: CompanyCodesApi,
        TagValues.COMPANYSPECIFIC_SCHEMA: CompanySpecificSchemaApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.DIRECT_DEPOSIT: DirectDepositApi,
        TagValues.EMERGENCY_CONTACTS: EmergencyContactsApi,
        TagValues.EMPLOYEE_BENEFIT_SETUP: EmployeeBenefitSetupApi,
        TagValues.EMPLOYEE_STAGING: EmployeeStagingApi,
        TagValues.NONPRIMARY_STATE_TAX: NonPrimaryStateTaxApi,
        TagValues.PRIMARY_STATE_TAX: PrimaryStateTaxApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.LOCAL_TAX: LocalTaxApi,
        TagValues.EARNINGS: EarningsApi,
        TagValues.DEDUCTION: DeductionApi,
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.LOCAL_TAXES: LocalTaxesApi,
        TagValues.PAY_STATEMENTS: PayStatementsApi,
        TagValues.EMPLOYEE_V1: EmployeeV1Api,
        TagValues.SENSITIVE_DATA: SensitiveDataApi,
        TagValues.ONBOARDING: OnboardingApi,
        TagValues.ADDITIONAL_RATES: AdditionalRatesApi,
        TagValues.CLIENT_CREDENTIALS: ClientCredentialsApi,
        TagValues.COMPANY_CODES: CompanyCodesApi,
        TagValues.COMPANYSPECIFIC_SCHEMA: CompanySpecificSchemaApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.DIRECT_DEPOSIT: DirectDepositApi,
        TagValues.EMERGENCY_CONTACTS: EmergencyContactsApi,
        TagValues.EMPLOYEE_BENEFIT_SETUP: EmployeeBenefitSetupApi,
        TagValues.EMPLOYEE_STAGING: EmployeeStagingApi,
        TagValues.NONPRIMARY_STATE_TAX: NonPrimaryStateTaxApi,
        TagValues.PRIMARY_STATE_TAX: PrimaryStateTaxApi,
    }
)
