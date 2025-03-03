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
from ..types.connection_retrieve_response import ConnectionRetrieveResponse

__all__ = ["ConnectionResource", "AsyncConnectionResource"]


class ConnectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openint-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openint-python#with_streaming_response
        """
        return ConnectionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionRetrieveResponse:
        return self._get(
            "/connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveResponse,
        )


class AsyncConnectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openint-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openint-python#with_streaming_response
        """
        return AsyncConnectionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionRetrieveResponse:
        return await self._get(
            "/connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveResponse,
        )


class ConnectionResourceWithRawResponse:
    def __init__(self, connection: ConnectionResource) -> None:
        self._connection = connection

        self.retrieve = to_raw_response_wrapper(
            connection.retrieve,
        )


class AsyncConnectionResourceWithRawResponse:
    def __init__(self, connection: AsyncConnectionResource) -> None:
        self._connection = connection

        self.retrieve = async_to_raw_response_wrapper(
            connection.retrieve,
        )


class ConnectionResourceWithStreamingResponse:
    def __init__(self, connection: ConnectionResource) -> None:
        self._connection = connection

        self.retrieve = to_streamed_response_wrapper(
            connection.retrieve,
        )


class AsyncConnectionResourceWithStreamingResponse:
    def __init__(self, connection: AsyncConnectionResource) -> None:
        self._connection = connection

        self.retrieve = async_to_streamed_response_wrapper(
            connection.retrieve,
        )
