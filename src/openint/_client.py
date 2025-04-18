# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, List, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import (
    client_create_token_params,
    client_get_connection_params,
    client_list_connectors_params,
    client_list_connections_params,
    client_create_connection_params,
    client_create_magic_link_params,
    client_list_connection_configs_params,
)
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from .pagination import SyncOffsetPagination, AsyncOffsetPagination
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    AsyncPaginator,
    make_request_options,
)
from .types.create_token_response import CreateTokenResponse
from .types.get_connection_response import GetConnectionResponse
from .types.list_connectors_response import ListConnectorsResponse
from .types.check_connection_response import CheckConnectionResponse
from .types.get_current_user_response import GetCurrentUserResponse
from .types.list_connections_response import ListConnectionsResponse
from .types.create_connection_response import CreateConnectionResponse
from .types.create_magic_link_response import CreateMagicLinkResponse
from .types.delete_connection_response import DeleteConnectionResponse
from .types.list_connection_configs_response import ListConnectionConfigsResponse

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Openint", "AsyncOpenint", "Client", "AsyncClient"]


class Openint(SyncAPIClient):
    with_raw_response: OpenintWithRawResponse
    with_streaming_response: OpenintWithStreamedResponse

    # client options
    api_key: str | None
    customer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        customer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Openint client instance.

        This automatically infers the `api_key` argument from the `OPENINT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("OPENINT_API_KEY")
        self.api_key = api_key

        self.customer_token = customer_token

        if base_url is None:
            base_url = os.environ.get("OPENINT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openint.dev/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.with_raw_response = OpenintWithRawResponse(self)
        self.with_streaming_response = OpenintWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._customer_token}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _customer_token(self) -> dict[str, str]:
        customer_token = self.customer_token
        if customer_token is None:
            return {}
        return {"Authorization": f"Bearer {customer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.customer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or customer_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        customer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            customer_token=customer_token or self.customer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def check_connection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckConnectionResponse:
        """
        Verify that a connection is healthy

        Args:
          id: The id of the connection, starts with `conn_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self.post(
            f"/connection/{id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckConnectionResponse,
        )

    def create_connection(
        self,
        *,
        connector_config_id: str,
        customer_id: str,
        data: client_create_connection_params.Data,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateConnectionResponse:
        """
        Import an existing connection after validation

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          data: Connector specific data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CreateConnectionResponse,
            self.post(
                "/connection",
                body=maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "customer_id": customer_id,
                        "data": data,
                        "metadata": metadata,
                    },
                    client_create_connection_params.ClientCreateConnectionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, CreateConnectionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def create_magic_link(
        self,
        customer_id: str,
        *,
        client_options: client_create_magic_link_params.ClientOptions | NotGiven = NOT_GIVEN,
        validity_in_seconds: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateMagicLinkResponse:
        """
        Create a magic link that is ready to be shared with customers who want to use
        Connect

        Args:
          client_options: Search params to configure the connect page. Not signed as part of JWT and
              therefore can be modified by client

          validity_in_seconds: How long the magic link will be valid for (in seconds) before it expires

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self.post(
            f"/customer/{customer_id}/magic-link",
            body=maybe_transform(
                {
                    "client_options": client_options,
                    "validity_in_seconds": validity_in_seconds,
                },
                client_create_magic_link_params.ClientCreateMagicLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateMagicLinkResponse,
        )

    def create_token(
        self,
        customer_id: str,
        *,
        validity_in_seconds: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateTokenResponse:
        """Create a @Connect authentication token for a customer.

        This token can be used to
        embed @Connect in your application via the `@openint/connect` npm package.

        Args:
          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          validity_in_seconds: How long the token will be valid for (in seconds) before it expires

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self.post(
            f"/customer/{customer_id}/token",
            body=maybe_transform(
                {"validity_in_seconds": validity_in_seconds}, client_create_token_params.ClientCreateTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTokenResponse,
        )

    def delete_connection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeleteConnectionResponse:
        """
        Delete a connection

        Args:
          id: The id of the connection, starts with `conn_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self.delete(
            f"/connection/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteConnectionResponse,
        )

    def get_connection(
        self,
        id: str,
        *,
        expand: List[Literal["connector"]] | NotGiven = NOT_GIVEN,
        include_secrets: Literal["none", "basic", "all"] | NotGiven = NOT_GIVEN,
        refresh_policy: Literal["none", "force", "auto"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetConnectionResponse:
        """
        Get details of a specific connection, including credentials

        Args:
          id: The id of the connection, starts with `conn_`

          include_secrets: Controls secret inclusion: none (default), basic (auth only), or all secrets

          refresh_policy: Controls credential refresh: none (never), force (always), or auto (when
              expired, default)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            GetConnectionResponse,
            self.get(
                f"/connection/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "expand": expand,
                            "include_secrets": include_secrets,
                            "refresh_policy": refresh_policy,
                        },
                        client_get_connection_params.ClientGetConnectionParams,
                    ),
                ),
                cast_to=cast(
                    Any, GetConnectionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetCurrentUserResponse:
        """Get information about the current authenticated user"""
        return self.get(
            "/viewer",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetCurrentUserResponse,
        )

    def list_connection_configs(
        self,
        *,
        connector_name: Literal[
            "aircall",
            "airtable",
            "apollo",
            "brex",
            "coda",
            "confluence",
            "discord",
            "dummy-oauth2",
            "facebook",
            "finch",
            "firebase",
            "foreceipt",
            "github",
            "gong",
            "googlecalendar",
            "googledocs",
            "googledrive",
            "googlemail",
            "googlesheet",
            "greenhouse",
            "heron",
            "hubspot",
            "instagram",
            "intercom",
            "jira",
            "kustomer",
            "lever",
            "linear",
            "linkedin",
            "lunchmoney",
            "mercury",
            "merge",
            "microsoft",
            "moota",
            "notion",
            "onebrick",
            "outreach",
            "pipedrive",
            "plaid",
            "postgres",
            "quickbooks",
            "ramp",
            "reddit",
            "salesforce",
            "salesloft",
            "saltedge",
            "sharepointonline",
            "slack",
            "splitwise",
            "stripe",
            "teller",
            "toggl",
            "twenty",
            "twitter",
            "venmo",
            "wise",
            "xero",
            "yodlee",
            "zohodesk",
        ]
        | NotGiven = NOT_GIVEN,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPagination[ListConnectionConfigsResponse]:
        """
        List the connectors that are configured in your account and available for your
        customers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/connector-config",
            page=SyncOffsetPagination[ListConnectionConfigsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_name": connector_name,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                    },
                    client_list_connection_configs_params.ClientListConnectionConfigsParams,
                ),
            ),
            model=cast(
                Any, ListConnectionConfigsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def list_connections(
        self,
        *,
        connector_config_id: str | NotGiven = NOT_GIVEN,
        connector_name: Literal[
            "aircall",
            "airtable",
            "apollo",
            "brex",
            "coda",
            "confluence",
            "discord",
            "dummy-oauth2",
            "facebook",
            "finch",
            "firebase",
            "foreceipt",
            "github",
            "gong",
            "googlecalendar",
            "googledocs",
            "googledrive",
            "googlemail",
            "googlesheet",
            "greenhouse",
            "heron",
            "hubspot",
            "instagram",
            "intercom",
            "jira",
            "kustomer",
            "lever",
            "linear",
            "linkedin",
            "lunchmoney",
            "mercury",
            "merge",
            "microsoft",
            "moota",
            "notion",
            "onebrick",
            "outreach",
            "pipedrive",
            "plaid",
            "postgres",
            "quickbooks",
            "ramp",
            "reddit",
            "salesforce",
            "salesloft",
            "saltedge",
            "sharepointonline",
            "slack",
            "splitwise",
            "stripe",
            "teller",
            "toggl",
            "twenty",
            "twitter",
            "venmo",
            "wise",
            "xero",
            "yodlee",
            "zohodesk",
        ]
        | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["connector"]] | NotGiven = NOT_GIVEN,
        include_secrets: Literal["none", "basic", "all"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPagination[ListConnectionsResponse]:
        """List all connections with optional filtering.

        Does not retrieve secrets or
        perform any connection healthcheck. For that use `getConnection` or
        `checkConnectionHealth`.

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          include_secrets: Controls secret inclusion: none (default), basic (auth only), or all secrets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/connection",
            page=SyncOffsetPagination[ListConnectionsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "connector_name": connector_name,
                        "customer_id": customer_id,
                        "expand": expand,
                        "include_secrets": include_secrets,
                        "limit": limit,
                        "offset": offset,
                    },
                    client_list_connections_params.ClientListConnectionsParams,
                ),
            ),
            model=cast(Any, ListConnectionsResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def list_connectors(
        self,
        *,
        expand: List[Literal["schemas"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListConnectorsResponse:
        """
        List all connectors to understand what integrations are available to configure

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get(
            "/connector",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, client_list_connectors_params.ClientListConnectorsParams),
            ),
            cast_to=ListConnectorsResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOpenint(AsyncAPIClient):
    with_raw_response: AsyncOpenintWithRawResponse
    with_streaming_response: AsyncOpenintWithStreamedResponse

    # client options
    api_key: str | None
    customer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        customer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOpenint client instance.

        This automatically infers the `api_key` argument from the `OPENINT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("OPENINT_API_KEY")
        self.api_key = api_key

        self.customer_token = customer_token

        if base_url is None:
            base_url = os.environ.get("OPENINT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openint.dev/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.with_raw_response = AsyncOpenintWithRawResponse(self)
        self.with_streaming_response = AsyncOpenintWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._customer_token}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _customer_token(self) -> dict[str, str]:
        customer_token = self.customer_token
        if customer_token is None:
            return {}
        return {"Authorization": f"Bearer {customer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.customer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or customer_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        customer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            customer_token=customer_token or self.customer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def check_connection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckConnectionResponse:
        """
        Verify that a connection is healthy

        Args:
          id: The id of the connection, starts with `conn_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self.post(
            f"/connection/{id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckConnectionResponse,
        )

    async def create_connection(
        self,
        *,
        connector_config_id: str,
        customer_id: str,
        data: client_create_connection_params.Data,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateConnectionResponse:
        """
        Import an existing connection after validation

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          data: Connector specific data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CreateConnectionResponse,
            await self.post(
                "/connection",
                body=await async_maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "customer_id": customer_id,
                        "data": data,
                        "metadata": metadata,
                    },
                    client_create_connection_params.ClientCreateConnectionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, CreateConnectionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def create_magic_link(
        self,
        customer_id: str,
        *,
        client_options: client_create_magic_link_params.ClientOptions | NotGiven = NOT_GIVEN,
        validity_in_seconds: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateMagicLinkResponse:
        """
        Create a magic link that is ready to be shared with customers who want to use
        Connect

        Args:
          client_options: Search params to configure the connect page. Not signed as part of JWT and
              therefore can be modified by client

          validity_in_seconds: How long the magic link will be valid for (in seconds) before it expires

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self.post(
            f"/customer/{customer_id}/magic-link",
            body=await async_maybe_transform(
                {
                    "client_options": client_options,
                    "validity_in_seconds": validity_in_seconds,
                },
                client_create_magic_link_params.ClientCreateMagicLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateMagicLinkResponse,
        )

    async def create_token(
        self,
        customer_id: str,
        *,
        validity_in_seconds: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateTokenResponse:
        """Create a @Connect authentication token for a customer.

        This token can be used to
        embed @Connect in your application via the `@openint/connect` npm package.

        Args:
          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          validity_in_seconds: How long the token will be valid for (in seconds) before it expires

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self.post(
            f"/customer/{customer_id}/token",
            body=await async_maybe_transform(
                {"validity_in_seconds": validity_in_seconds}, client_create_token_params.ClientCreateTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTokenResponse,
        )

    async def delete_connection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeleteConnectionResponse:
        """
        Delete a connection

        Args:
          id: The id of the connection, starts with `conn_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self.delete(
            f"/connection/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteConnectionResponse,
        )

    async def get_connection(
        self,
        id: str,
        *,
        expand: List[Literal["connector"]] | NotGiven = NOT_GIVEN,
        include_secrets: Literal["none", "basic", "all"] | NotGiven = NOT_GIVEN,
        refresh_policy: Literal["none", "force", "auto"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetConnectionResponse:
        """
        Get details of a specific connection, including credentials

        Args:
          id: The id of the connection, starts with `conn_`

          include_secrets: Controls secret inclusion: none (default), basic (auth only), or all secrets

          refresh_policy: Controls credential refresh: none (never), force (always), or auto (when
              expired, default)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            GetConnectionResponse,
            await self.get(
                f"/connection/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "expand": expand,
                            "include_secrets": include_secrets,
                            "refresh_policy": refresh_policy,
                        },
                        client_get_connection_params.ClientGetConnectionParams,
                    ),
                ),
                cast_to=cast(
                    Any, GetConnectionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetCurrentUserResponse:
        """Get information about the current authenticated user"""
        return await self.get(
            "/viewer",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetCurrentUserResponse,
        )

    def list_connection_configs(
        self,
        *,
        connector_name: Literal[
            "aircall",
            "airtable",
            "apollo",
            "brex",
            "coda",
            "confluence",
            "discord",
            "dummy-oauth2",
            "facebook",
            "finch",
            "firebase",
            "foreceipt",
            "github",
            "gong",
            "googlecalendar",
            "googledocs",
            "googledrive",
            "googlemail",
            "googlesheet",
            "greenhouse",
            "heron",
            "hubspot",
            "instagram",
            "intercom",
            "jira",
            "kustomer",
            "lever",
            "linear",
            "linkedin",
            "lunchmoney",
            "mercury",
            "merge",
            "microsoft",
            "moota",
            "notion",
            "onebrick",
            "outreach",
            "pipedrive",
            "plaid",
            "postgres",
            "quickbooks",
            "ramp",
            "reddit",
            "salesforce",
            "salesloft",
            "saltedge",
            "sharepointonline",
            "slack",
            "splitwise",
            "stripe",
            "teller",
            "toggl",
            "twenty",
            "twitter",
            "venmo",
            "wise",
            "xero",
            "yodlee",
            "zohodesk",
        ]
        | NotGiven = NOT_GIVEN,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ListConnectionConfigsResponse, AsyncOffsetPagination[ListConnectionConfigsResponse]]:
        """
        List the connectors that are configured in your account and available for your
        customers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/connector-config",
            page=AsyncOffsetPagination[ListConnectionConfigsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_name": connector_name,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                    },
                    client_list_connection_configs_params.ClientListConnectionConfigsParams,
                ),
            ),
            model=cast(
                Any, ListConnectionConfigsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def list_connections(
        self,
        *,
        connector_config_id: str | NotGiven = NOT_GIVEN,
        connector_name: Literal[
            "aircall",
            "airtable",
            "apollo",
            "brex",
            "coda",
            "confluence",
            "discord",
            "dummy-oauth2",
            "facebook",
            "finch",
            "firebase",
            "foreceipt",
            "github",
            "gong",
            "googlecalendar",
            "googledocs",
            "googledrive",
            "googlemail",
            "googlesheet",
            "greenhouse",
            "heron",
            "hubspot",
            "instagram",
            "intercom",
            "jira",
            "kustomer",
            "lever",
            "linear",
            "linkedin",
            "lunchmoney",
            "mercury",
            "merge",
            "microsoft",
            "moota",
            "notion",
            "onebrick",
            "outreach",
            "pipedrive",
            "plaid",
            "postgres",
            "quickbooks",
            "ramp",
            "reddit",
            "salesforce",
            "salesloft",
            "saltedge",
            "sharepointonline",
            "slack",
            "splitwise",
            "stripe",
            "teller",
            "toggl",
            "twenty",
            "twitter",
            "venmo",
            "wise",
            "xero",
            "yodlee",
            "zohodesk",
        ]
        | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["connector"]] | NotGiven = NOT_GIVEN,
        include_secrets: Literal["none", "basic", "all"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ListConnectionsResponse, AsyncOffsetPagination[ListConnectionsResponse]]:
        """List all connections with optional filtering.

        Does not retrieve secrets or
        perform any connection healthcheck. For that use `getConnection` or
        `checkConnectionHealth`.

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          include_secrets: Controls secret inclusion: none (default), basic (auth only), or all secrets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/connection",
            page=AsyncOffsetPagination[ListConnectionsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "connector_name": connector_name,
                        "customer_id": customer_id,
                        "expand": expand,
                        "include_secrets": include_secrets,
                        "limit": limit,
                        "offset": offset,
                    },
                    client_list_connections_params.ClientListConnectionsParams,
                ),
            ),
            model=cast(Any, ListConnectionsResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def list_connectors(
        self,
        *,
        expand: List[Literal["schemas"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListConnectorsResponse:
        """
        List all connectors to understand what integrations are available to configure

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.get(
            "/connector",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, client_list_connectors_params.ClientListConnectorsParams
                ),
            ),
            cast_to=ListConnectorsResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OpenintWithRawResponse:
    def __init__(self, client: Openint) -> None:
        self.check_connection = to_raw_response_wrapper(
            client.check_connection,
        )
        self.create_connection = to_raw_response_wrapper(
            client.create_connection,
        )
        self.create_magic_link = to_raw_response_wrapper(
            client.create_magic_link,
        )
        self.create_token = to_raw_response_wrapper(
            client.create_token,
        )
        self.delete_connection = to_raw_response_wrapper(
            client.delete_connection,
        )
        self.get_connection = to_raw_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = to_raw_response_wrapper(
            client.get_current_user,
        )
        self.list_connection_configs = to_raw_response_wrapper(
            client.list_connection_configs,
        )
        self.list_connections = to_raw_response_wrapper(
            client.list_connections,
        )
        self.list_connectors = to_raw_response_wrapper(
            client.list_connectors,
        )


class AsyncOpenintWithRawResponse:
    def __init__(self, client: AsyncOpenint) -> None:
        self.check_connection = async_to_raw_response_wrapper(
            client.check_connection,
        )
        self.create_connection = async_to_raw_response_wrapper(
            client.create_connection,
        )
        self.create_magic_link = async_to_raw_response_wrapper(
            client.create_magic_link,
        )
        self.create_token = async_to_raw_response_wrapper(
            client.create_token,
        )
        self.delete_connection = async_to_raw_response_wrapper(
            client.delete_connection,
        )
        self.get_connection = async_to_raw_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = async_to_raw_response_wrapper(
            client.get_current_user,
        )
        self.list_connection_configs = async_to_raw_response_wrapper(
            client.list_connection_configs,
        )
        self.list_connections = async_to_raw_response_wrapper(
            client.list_connections,
        )
        self.list_connectors = async_to_raw_response_wrapper(
            client.list_connectors,
        )


class OpenintWithStreamedResponse:
    def __init__(self, client: Openint) -> None:
        self.check_connection = to_streamed_response_wrapper(
            client.check_connection,
        )
        self.create_connection = to_streamed_response_wrapper(
            client.create_connection,
        )
        self.create_magic_link = to_streamed_response_wrapper(
            client.create_magic_link,
        )
        self.create_token = to_streamed_response_wrapper(
            client.create_token,
        )
        self.delete_connection = to_streamed_response_wrapper(
            client.delete_connection,
        )
        self.get_connection = to_streamed_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = to_streamed_response_wrapper(
            client.get_current_user,
        )
        self.list_connection_configs = to_streamed_response_wrapper(
            client.list_connection_configs,
        )
        self.list_connections = to_streamed_response_wrapper(
            client.list_connections,
        )
        self.list_connectors = to_streamed_response_wrapper(
            client.list_connectors,
        )


class AsyncOpenintWithStreamedResponse:
    def __init__(self, client: AsyncOpenint) -> None:
        self.check_connection = async_to_streamed_response_wrapper(
            client.check_connection,
        )
        self.create_connection = async_to_streamed_response_wrapper(
            client.create_connection,
        )
        self.create_magic_link = async_to_streamed_response_wrapper(
            client.create_magic_link,
        )
        self.create_token = async_to_streamed_response_wrapper(
            client.create_token,
        )
        self.delete_connection = async_to_streamed_response_wrapper(
            client.delete_connection,
        )
        self.get_connection = async_to_streamed_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = async_to_streamed_response_wrapper(
            client.get_current_user,
        )
        self.list_connection_configs = async_to_streamed_response_wrapper(
            client.list_connection_configs,
        )
        self.list_connections = async_to_streamed_response_wrapper(
            client.list_connections,
        )
        self.list_connectors = async_to_streamed_response_wrapper(
            client.list_connectors,
        )


Client = Openint

AsyncClient = AsyncOpenint
