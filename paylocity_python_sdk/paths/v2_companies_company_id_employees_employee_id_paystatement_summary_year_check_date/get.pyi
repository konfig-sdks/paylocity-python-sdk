# coding: utf-8

"""
    WebLink API

    For documentation about this API, please visit https://developer.paylocity.com/integrations/reference/weblink-overview

    The version of the OpenAPI document: v2
    Contact: webservices@paylocity.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from paylocity_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from paylocity_python_sdk.api_response import AsyncGeneratorResponse
from paylocity_python_sdk import api_client, exceptions
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

from paylocity_python_sdk.model.pay_statements_get_summary_data404_response import PayStatementsGetSummaryData404Response as PayStatementsGetSummaryData404ResponseSchema
from paylocity_python_sdk.model.pay_statements_get_summary_data500_response import PayStatementsGetSummaryData500Response as PayStatementsGetSummaryData500ResponseSchema
from paylocity_python_sdk.model.pay_statements_get_summary_data_response import PayStatementsGetSummaryDataResponse as PayStatementsGetSummaryDataResponseSchema

from paylocity_python_sdk.type.pay_statements_get_summary_data500_response import PayStatementsGetSummaryData500Response
from paylocity_python_sdk.type.pay_statements_get_summary_data_response import PayStatementsGetSummaryDataResponse
from paylocity_python_sdk.type.pay_statements_get_summary_data404_response import PayStatementsGetSummaryData404Response

from ...api_client import Dictionary
from paylocity_python_sdk.pydantic.pay_statements_get_summary_data404_response import PayStatementsGetSummaryData404Response as PayStatementsGetSummaryData404ResponsePydantic
from paylocity_python_sdk.pydantic.pay_statements_get_summary_data_response import PayStatementsGetSummaryDataResponse as PayStatementsGetSummaryDataResponsePydantic
from paylocity_python_sdk.pydantic.pay_statements_get_summary_data500_response import PayStatementsGetSummaryData500Response as PayStatementsGetSummaryData500ResponsePydantic

# Query params
PagesizeSchema = schemas.IntSchema
PagenumberSchema = schemas.IntSchema
IncludetotalcountSchema = schemas.BoolSchema
CodegroupSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'pagesize': typing.Union[PagesizeSchema, decimal.Decimal, int, ],
        'pagenumber': typing.Union[PagenumberSchema, decimal.Decimal, int, ],
        'includetotalcount': typing.Union[IncludetotalcountSchema, bool, ],
        'codegroup': typing.Union[CodegroupSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_pagesize = api_client.QueryParameter(
    name="pagesize",
    style=api_client.ParameterStyle.FORM,
    schema=PagesizeSchema,
    explode=True,
)
request_query_pagenumber = api_client.QueryParameter(
    name="pagenumber",
    style=api_client.ParameterStyle.FORM,
    schema=PagenumberSchema,
    explode=True,
)
request_query_includetotalcount = api_client.QueryParameter(
    name="includetotalcount",
    style=api_client.ParameterStyle.FORM,
    schema=IncludetotalcountSchema,
    explode=True,
)
request_query_codegroup = api_client.QueryParameter(
    name="codegroup",
    style=api_client.ParameterStyle.FORM,
    schema=CodegroupSchema,
    explode=True,
)
# Path params
CompanyIdSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
YearSchema = schemas.StrSchema
CheckDateSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyId': typing.Union[CompanyIdSchema, str, ],
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
        'year': typing.Union[YearSchema, str, ],
        'checkDate': typing.Union[CheckDateSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_company_id = api_client.PathParameter(
    name="companyId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
request_path_employee_id = api_client.PathParameter(
    name="employeeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EmployeeIdSchema,
    required=True,
)
request_path_year = api_client.PathParameter(
    name="year",
    style=api_client.ParameterStyle.SIMPLE,
    schema=YearSchema,
    required=True,
)
request_path_check_date = api_client.PathParameter(
    name="checkDate",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CheckDateSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = PayStatementsGetSummaryDataResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PayStatementsGetSummaryDataResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PayStatementsGetSummaryDataResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: 


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: 


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
SchemaFor404ResponseBodyApplicationJson = PayStatementsGetSummaryData404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: PayStatementsGetSummaryData404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: PayStatementsGetSummaryData404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: 


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
)
SchemaFor500ResponseBodyApplicationJson = PayStatementsGetSummaryData500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: PayStatementsGetSummaryData500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: PayStatementsGetSummaryData500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_summary_data_mapped_args(
        self,
        company_id: str,
        employee_id: str,
        year: str,
        check_date: str,
        pagesize: typing.Optional[int] = None,
        pagenumber: typing.Optional[int] = None,
        includetotalcount: typing.Optional[bool] = None,
        codegroup: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if pagesize is not None:
            _query_params["pagesize"] = pagesize
        if pagenumber is not None:
            _query_params["pagenumber"] = pagenumber
        if includetotalcount is not None:
            _query_params["includetotalcount"] = includetotalcount
        if codegroup is not None:
            _query_params["codegroup"] = codegroup
        if company_id is not None:
            _path_params["companyId"] = company_id
        if employee_id is not None:
            _path_params["employeeId"] = employee_id
        if year is not None:
            _path_params["year"] = year
        if check_date is not None:
            _path_params["checkDate"] = check_date
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_summary_data_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get employee pay statement summary data for the specified year and check date.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_employee_id,
            request_path_year,
            request_path_check_date,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pagesize,
            request_query_pagenumber,
            request_query_includetotalcount,
            request_query_codegroup,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_summary_data_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get employee pay statement summary data for the specified year and check date.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_employee_id,
            request_path_year,
            request_path_check_date,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pagesize,
            request_query_pagenumber,
            request_query_includetotalcount,
            request_query_codegroup,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetSummaryDataRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_summary_data(
        self,
        company_id: str,
        employee_id: str,
        year: str,
        check_date: str,
        pagesize: typing.Optional[int] = None,
        pagenumber: typing.Optional[int] = None,
        includetotalcount: typing.Optional[bool] = None,
        codegroup: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_summary_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            year=year,
            check_date=check_date,
            pagesize=pagesize,
            pagenumber=pagenumber,
            includetotalcount=includetotalcount,
            codegroup=codegroup,
        )
        return await self._aget_summary_data_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_summary_data(
        self,
        company_id: str,
        employee_id: str,
        year: str,
        check_date: str,
        pagesize: typing.Optional[int] = None,
        pagenumber: typing.Optional[int] = None,
        includetotalcount: typing.Optional[bool] = None,
        codegroup: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_summary_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            year=year,
            check_date=check_date,
            pagesize=pagesize,
            pagenumber=pagenumber,
            includetotalcount=includetotalcount,
            codegroup=codegroup,
        )
        return self._get_summary_data_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetSummaryData(BaseApi):

    async def aget_summary_data(
        self,
        company_id: str,
        employee_id: str,
        year: str,
        check_date: str,
        pagesize: typing.Optional[int] = None,
        pagenumber: typing.Optional[int] = None,
        includetotalcount: typing.Optional[bool] = None,
        codegroup: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PayStatementsGetSummaryDataResponsePydantic:
        raw_response = await self.raw.aget_summary_data(
            company_id=company_id,
            employee_id=employee_id,
            year=year,
            check_date=check_date,
            pagesize=pagesize,
            pagenumber=pagenumber,
            includetotalcount=includetotalcount,
            codegroup=codegroup,
            **kwargs,
        )
        if validate:
            return RootModel[PayStatementsGetSummaryDataResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PayStatementsGetSummaryDataResponsePydantic, raw_response.body)
    
    
    def get_summary_data(
        self,
        company_id: str,
        employee_id: str,
        year: str,
        check_date: str,
        pagesize: typing.Optional[int] = None,
        pagenumber: typing.Optional[int] = None,
        includetotalcount: typing.Optional[bool] = None,
        codegroup: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PayStatementsGetSummaryDataResponsePydantic:
        raw_response = self.raw.get_summary_data(
            company_id=company_id,
            employee_id=employee_id,
            year=year,
            check_date=check_date,
            pagesize=pagesize,
            pagenumber=pagenumber,
            includetotalcount=includetotalcount,
            codegroup=codegroup,
        )
        if validate:
            return RootModel[PayStatementsGetSummaryDataResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PayStatementsGetSummaryDataResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: str,
        employee_id: str,
        year: str,
        check_date: str,
        pagesize: typing.Optional[int] = None,
        pagenumber: typing.Optional[int] = None,
        includetotalcount: typing.Optional[bool] = None,
        codegroup: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_summary_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            year=year,
            check_date=check_date,
            pagesize=pagesize,
            pagenumber=pagenumber,
            includetotalcount=includetotalcount,
            codegroup=codegroup,
        )
        return await self._aget_summary_data_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_id: str,
        employee_id: str,
        year: str,
        check_date: str,
        pagesize: typing.Optional[int] = None,
        pagenumber: typing.Optional[int] = None,
        includetotalcount: typing.Optional[bool] = None,
        codegroup: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_summary_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            year=year,
            check_date=check_date,
            pagesize=pagesize,
            pagenumber=pagenumber,
            includetotalcount=includetotalcount,
            codegroup=codegroup,
        )
        return self._get_summary_data_oapg(
            query_params=args.query,
            path_params=args.path,
        )

