# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.connector_config_retrieve_response import ConnectorConfigRetrieveResponse

__all__ = ["ConnectorConfigResource", "AsyncConnectorConfigResource"]


class ConnectorConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openint-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openint-python#with_streaming_response
        """
        return ConnectorConfigResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorConfigRetrieveResponse:
        return self._get(
            "/connector-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorConfigRetrieveResponse,
        )


class AsyncConnectorConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openint-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openint-python#with_streaming_response
        """
        return AsyncConnectorConfigResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorConfigRetrieveResponse:
        return await self._get(
            "/connector-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorConfigRetrieveResponse,
        )


class ConnectorConfigResourceWithRawResponse:
    def __init__(self, connector_config: ConnectorConfigResource) -> None:
        self._connector_config = connector_config

        self.retrieve = to_raw_response_wrapper(
            connector_config.retrieve,
        )


class AsyncConnectorConfigResourceWithRawResponse:
    def __init__(self, connector_config: AsyncConnectorConfigResource) -> None:
        self._connector_config = connector_config

        self.retrieve = async_to_raw_response_wrapper(
            connector_config.retrieve,
        )


class ConnectorConfigResourceWithStreamingResponse:
    def __init__(self, connector_config: ConnectorConfigResource) -> None:
        self._connector_config = connector_config

        self.retrieve = to_streamed_response_wrapper(
            connector_config.retrieve,
        )


class AsyncConnectorConfigResourceWithStreamingResponse:
    def __init__(self, connector_config: AsyncConnectorConfigResource) -> None:
        self._connector_config = connector_config

        self.retrieve = async_to_streamed_response_wrapper(
            connector_config.retrieve,
        )
