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

from paylocity_python_sdk.model.employee_get_employee_data404_response import EmployeeGetEmployeeData404Response as EmployeeGetEmployeeData404ResponseSchema
from paylocity_python_sdk.model.employee_get_employee_data_response import EmployeeGetEmployeeDataResponse as EmployeeGetEmployeeDataResponseSchema
from paylocity_python_sdk.model.employee_get_employee_data500_response import EmployeeGetEmployeeData500Response as EmployeeGetEmployeeData500ResponseSchema

from paylocity_python_sdk.type.employee_get_employee_data404_response import EmployeeGetEmployeeData404Response
from paylocity_python_sdk.type.employee_get_employee_data_response import EmployeeGetEmployeeDataResponse
from paylocity_python_sdk.type.employee_get_employee_data500_response import EmployeeGetEmployeeData500Response

from ...api_client import Dictionary
from paylocity_python_sdk.pydantic.employee_get_employee_data500_response import EmployeeGetEmployeeData500Response as EmployeeGetEmployeeData500ResponsePydantic
from paylocity_python_sdk.pydantic.employee_get_employee_data404_response import EmployeeGetEmployeeData404Response as EmployeeGetEmployeeData404ResponsePydantic
from paylocity_python_sdk.pydantic.employee_get_employee_data_response import EmployeeGetEmployeeDataResponse as EmployeeGetEmployeeDataResponsePydantic

from . import path

# Path params
CompanyIdSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyId': typing.Union[CompanyIdSchema, str, ],
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
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
_auth = [
    'paylocity_auth',
]
SchemaFor200ResponseBodyApplicationJson = EmployeeGetEmployeeDataResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeeGetEmployeeDataResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeeGetEmployeeDataResponse


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
SchemaFor404ResponseBodyApplicationJson = EmployeeGetEmployeeData404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: EmployeeGetEmployeeData404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: EmployeeGetEmployeeData404Response


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
SchemaFor500ResponseBodyApplicationJson = EmployeeGetEmployeeData500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: EmployeeGetEmployeeData500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: EmployeeGetEmployeeData500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_employee_data_mapped_args(
        self,
        company_id: str,
        employee_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if company_id is not None:
            _path_params["companyId"] = company_id
        if employee_id is not None:
            _path_params["employeeId"] = employee_id
        args.path = _path_params
        return args

    async def _aget_employee_data_oapg(
        self,
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
        Get employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v2/companies/{companyId}/employees/{employeeId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _get_employee_data_oapg(
        self,
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
        Get employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v2/companies/{companyId}/employees/{employeeId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class GetEmployeeDataRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_employee_data(
        self,
        company_id: str,
        employee_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_employee_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
        )
        return await self._aget_employee_data_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_employee_data(
        self,
        company_id: str,
        employee_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_employee_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
        )
        return self._get_employee_data_oapg(
            path_params=args.path,
        )

class GetEmployeeData(BaseApi):

    async def aget_employee_data(
        self,
        company_id: str,
        employee_id: str,
        validate: bool = False,
        **kwargs,
    ) -> EmployeeGetEmployeeDataResponsePydantic:
        raw_response = await self.raw.aget_employee_data(
            company_id=company_id,
            employee_id=employee_id,
            **kwargs,
        )
        if validate:
            return RootModel[EmployeeGetEmployeeDataResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(EmployeeGetEmployeeDataResponsePydantic, raw_response.body)
    
    
    def get_employee_data(
        self,
        company_id: str,
        employee_id: str,
        validate: bool = False,
    ) -> EmployeeGetEmployeeDataResponsePydantic:
        raw_response = self.raw.get_employee_data(
            company_id=company_id,
            employee_id=employee_id,
        )
        if validate:
            return RootModel[EmployeeGetEmployeeDataResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(EmployeeGetEmployeeDataResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: str,
        employee_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_employee_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
        )
        return await self._aget_employee_data_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_id: str,
        employee_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_employee_data_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
        )
        return self._get_employee_data_oapg(
            path_params=args.path,
        )

