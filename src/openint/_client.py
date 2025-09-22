# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, List, Mapping, Optional, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import (
    client_list_events_params,
    client_pre_connect_params,
    client_create_token_params,
    client_post_connect_params,
    client_connector_rpc_params,
    client_get_connection_params,
    client_list_customers_params,
    client_list_connectors_params,
    client_upsert_customer_params,
    client_list_connections_params,
    client_create_connection_params,
    client_get_conector_config_params,
    client_upsert_organization_params,
    client_list_connector_configs_params,
    client_list_connnector_configs_params,
    client_pre_configure_connector_params,
    client_create_connnector_config_params,
    client_upsert_connnector_config_params,
)
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    SequenceNotStr,
    omit,
    not_given,
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
from .types.list_events_response import ListEventsResponse
from .types.pre_connect_response import PreConnectResponse
from .types.create_token_response import CreateTokenResponse
from .types.post_connect_response import PostConnectResponse
from .types.connector_rpc_response import ConnectorRpcResponse
from .types.list_customers_response import ListCustomersResponse
from .types.list_connectors_response import ListConnectorsResponse
from .types.upsert_customer_response import UpsertCustomerResponse
from .types.check_connection_response import CheckConnectionResponse
from .types.get_current_user_response import GetCurrentUserResponse
from .types.list_assignments_response import ListAssignmentsResponse
from .types.assign_connection_response import AssignConnectionResponse
from .types.delete_assignment_response import DeleteAssignmentResponse
from .types.delete_connection_response import DeleteConnectionResponse
from .types.get_conector_config_response import GetConectorConfigResponse
from .types.upsert_organization_response import UpsertOrganizationResponse
from .types.list_connector_configs_response import ListConnectorConfigsResponse
from .types.delete_connector_config_response import DeleteConnectorConfigResponse
from .types.list_connnector_configs_response import ListConnnectorConfigsResponse
from .types.pre_configure_connector_response import PreConfigureConnectorResponse
from .types.create_connnector_config_response import CreateConnnectorConfigResponse
from .types.upsert_connnector_config_response import UpsertConnnectorConfigResponse

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Openint", "AsyncOpenint", "Client", "AsyncClient"]


class Openint(SyncAPIClient):
    with_raw_response: OpenintWithRawResponse
    with_streaming_response: OpenintWithStreamedResponse

    # client options
    token: str | None

    def __init__(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

        This automatically infers the `token` argument from the `OPENINT_API_KEY` environment variable if it is not provided.
        """
        if token is None:
            token = os.environ.get("OPENINT_API_KEY")
        self.token = token

        if base_url is None:
            base_url = os.environ.get("OPENINT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openint.dev"

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
        token = self.token
        if token is None:
            return {}
        return {"Authorization": f"Bearer {token}"}

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
        if self.token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            token=token or self.token,
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

    def assign_connection(
        self,
        repl_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssignConnectionResponse:
        """
        Assign a connection to a customer

        Args:
          id: The id of the connection, starts with `conn_`

          repl_id: The repl ID to assign to this connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not repl_id:
            raise ValueError(f"Expected a non-empty value for `repl_id` but received {repl_id!r}")
        return self.put(
            f"/v2/connection/{id}/assignment/{repl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssignConnectionResponse,
        )

    def check_connection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v1/connection/{id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckConnectionResponse,
        )

    def connector_rpc(
        self,
        function_name: str,
        *,
        connector_config_id: str,
        input: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorRpcResponse:
        """
        Execute RPC function on connector

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          function_name: RPC function name to execute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_config_id:
            raise ValueError(
                f"Expected a non-empty value for `connector_config_id` but received {connector_config_id!r}"
            )
        if not function_name:
            raise ValueError(f"Expected a non-empty value for `function_name` but received {function_name!r}")
        return self.post(
            f"/v2/connector-config/{connector_config_id}/rpc/{function_name}",
            body=maybe_transform({"input": input}, client_connector_rpc_params.ClientConnectorRpcParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorRpcResponse,
        )

    def create_connection(
        self,
        *,
        connector_config_id: str,
        data: client_create_connection_params.Data,
        check_connection: bool | Omit = omit,
        customer_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Import an existing connection after validation

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          data: Connector specific data

          check_connection: Perform a synchronous connection check before creating it.

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v2/connection",
            body=maybe_transform(
                {
                    "connector_config_id": connector_config_id,
                    "data": data,
                    "check_connection": check_connection,
                    "customer_id": customer_id,
                    "metadata": metadata,
                },
                client_create_connection_params.ClientCreateConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_connnector_config(
        self,
        *,
        connector_name: str,
        config: Optional[Dict[str, object]] | Omit = omit,
        disabled: Optional[bool] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateConnnectorConfigResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CreateConnnectorConfigResponse,
            self.post(
                "/v2/connector-config",
                body=maybe_transform(
                    {
                        "connector_name": connector_name,
                        "config": config,
                        "disabled": disabled,
                        "display_name": display_name,
                        "metadata": metadata,
                    },
                    client_create_connnector_config_params.ClientCreateConnnectorConfigParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, CreateConnnectorConfigResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def create_token(
        self,
        customer_id: str,
        *,
        connect_options: client_create_token_params.ConnectOptions | Omit = omit,
        validity_in_seconds: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateTokenResponse:
        """Create a @Connect authentication token for a customer.

        This token can be used to
        embed @Connect in your application via the `@openint/connect` npm package.

        Args:
          customer_id: The unique ID of the customer to create the token for

          validity_in_seconds: How long the publishable token and magic link url will be valid for (in seconds)
              before it expires. By default it will be valid for 30 days unless otherwise
              specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self.post(
            f"/v1/customer/{customer_id}/token",
            body=maybe_transform(
                {
                    "connect_options": connect_options,
                    "validity_in_seconds": validity_in_seconds,
                },
                client_create_token_params.ClientCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTokenResponse,
        )

    def delete_assignment(
        self,
        repl_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteAssignmentResponse:
        """
        Remove a repl assignment from a connection

        Args:
          id: The id of the connection, starts with `conn_`

          repl_id: The repl ID to remove from this connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not repl_id:
            raise ValueError(f"Expected a non-empty value for `repl_id` but received {repl_id!r}")
        return self.delete(
            f"/v2/connection/{id}/assignment/{repl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteAssignmentResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/connection/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteConnectionResponse,
        )

    def delete_connector_config(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteConnectorConfigResponse:
        """
        Args:
          id: The id of the connector config, starts with `ccfg_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self.delete(
            f"/v2/connector-config/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteConnectorConfigResponse,
        )

    def get_conector_config(
        self,
        id: str,
        *,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetConectorConfigResponse:
        """
        Args:
          id: The id of the connector config, starts with `ccfg_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            GetConectorConfigResponse,
            self.get(
                f"/v2/connector-config/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"expand": expand}, client_get_conector_config_params.ClientGetConectorConfigParams
                    ),
                ),
                cast_to=cast(
                    Any, GetConectorConfigResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get_connection(
        self,
        id: str,
        *,
        expand: List[Literal["connector"]] | Omit = omit,
        include_secrets: bool | Omit = omit,
        refresh_policy: Literal["none", "force", "auto"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get details of a specific connection, including credentials

        Args:
          id: The id of the connection, starts with `conn_`

          refresh_policy: Controls credential refresh: none (never), force (always), or auto (when
              expired, default)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self.get(
            f"/v2/connection/{id}",
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
            cast_to=object,
        )

    def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetCurrentUserResponse:
        """Get information about the current authenticated user"""
        return self.get(
            "/v1/viewer",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetCurrentUserResponse,
        )

    def list_assignments(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListAssignmentsResponse:
        """
        Get the list of assignments for a specific connection

        Args:
          id: The id of the connection, starts with `conn_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self.get(
            f"/v2/connection/{id}/assignment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListAssignmentsResponse,
        )

    def list_connections(
        self,
        *,
        connection_ids: SequenceNotStr[str] | Omit = omit,
        connector_config_id: str | Omit = omit,
        connector_names: List[
            Literal[
                "acme-apikey",
                "acme-oauth2",
                "apollo",
                "asana",
                "bigquery",
                "box",
                "calendly",
                "confluence",
                "databricks",
                "discord",
                "dropbox",
                "figma",
                "github",
                "google-calendar",
                "google-docs",
                "google-drive",
                "google-mail",
                "google-sheet",
                "hubspot",
                "instagram",
                "jira",
                "linear",
                "monday",
                "notion",
                "onedrive",
                "outlook",
                "plaid",
                "postgres",
                "resend",
                "salesforce",
                "sendgrid",
                "sharepoint",
                "slack",
                "slack-agent",
                "slack-agent-builder",
                "slack-deployed-agent",
                "snowflake",
                "spotify",
                "stripe",
                "stripe-agent-sandbox",
                "twilio",
                "workato",
                "youtube",
                "zendesk",
                "zoom",
            ]
        ]
        | Omit = omit,
        customer_id: str | Omit = omit,
        expand: List[Literal["connector"]] | Omit = omit,
        include_secrets: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        refresh_policy: Literal["none", "force", "auto"] | Omit = omit,
        repl_id: str | Omit = omit,
        search_query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[object]:
        """List all connections with optional filtering.

        Does not retrieve secrets or
        perform any connection healthcheck. For that use `getConnection` or
        `checkConnectionHealth`.

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          expand: Expand the response with additional optionals

          limit: Limit the number of items returned

          offset: Offset the items returned

          refresh_policy: Controls credential refresh: none (never), force (always), or auto (when
              expired, default)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connection",
            page=SyncOffsetPagination[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_ids": connection_ids,
                        "connector_config_id": connector_config_id,
                        "connector_names": connector_names,
                        "customer_id": customer_id,
                        "expand": expand,
                        "include_secrets": include_secrets,
                        "limit": limit,
                        "offset": offset,
                        "refresh_policy": refresh_policy,
                        "repl_id": repl_id,
                        "search_query": search_query,
                    },
                    client_list_connections_params.ClientListConnectionsParams,
                ),
            ),
            model=object,
        )

    def list_connector_configs(
        self,
        *,
        connector_names: List[
            Literal[
                "acme-apikey",
                "acme-oauth2",
                "apollo",
                "asana",
                "bigquery",
                "box",
                "calendly",
                "confluence",
                "databricks",
                "discord",
                "dropbox",
                "figma",
                "github",
                "google-calendar",
                "google-docs",
                "google-drive",
                "google-mail",
                "google-sheet",
                "hubspot",
                "instagram",
                "jira",
                "linear",
                "monday",
                "notion",
                "onedrive",
                "outlook",
                "plaid",
                "postgres",
                "resend",
                "salesforce",
                "sendgrid",
                "sharepoint",
                "slack",
                "slack-agent",
                "slack-agent-builder",
                "slack-deployed-agent",
                "snowflake",
                "spotify",
                "stripe",
                "stripe-agent-sandbox",
                "twilio",
                "workato",
                "youtube",
                "zendesk",
                "zoom",
            ]
        ]
        | Omit = omit,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | Omit = omit,
        include_disabled: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ListConnectorConfigsResponse]:
        """
        List Configured Connectors

        Args:
          include_disabled: Include disabled connector configs in the response. By default, disabled configs
              are filtered out.

          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connector-config",
            page=SyncOffsetPagination[ListConnectorConfigsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_names": connector_names,
                        "expand": expand,
                        "include_disabled": include_disabled,
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                    },
                    client_list_connector_configs_params.ClientListConnectorConfigsParams,
                ),
            ),
            model=cast(
                Any, ListConnectorConfigsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def list_connectors(
        self,
        *,
        connector_name: str | Omit = omit,
        expand: List[Literal["schemas"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ListConnectorsResponse]:
        """
        List all connectors to understand what integrations are available to configure

        Args:
          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connector",
            page=SyncOffsetPagination[ListConnectorsResponse],
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
                    client_list_connectors_params.ClientListConnectorsParams,
                ),
            ),
            model=ListConnectorsResponse,
        )

    def list_connnector_configs(
        self,
        *,
        connector_names: List[
            Literal[
                "acme-apikey",
                "acme-oauth2",
                "apollo",
                "asana",
                "bigquery",
                "box",
                "calendly",
                "confluence",
                "databricks",
                "discord",
                "dropbox",
                "figma",
                "github",
                "google-calendar",
                "google-docs",
                "google-drive",
                "google-mail",
                "google-sheet",
                "hubspot",
                "instagram",
                "jira",
                "linear",
                "monday",
                "notion",
                "onedrive",
                "outlook",
                "plaid",
                "postgres",
                "resend",
                "salesforce",
                "sendgrid",
                "sharepoint",
                "slack",
                "slack-agent",
                "slack-agent-builder",
                "slack-deployed-agent",
                "snowflake",
                "spotify",
                "stripe",
                "stripe-agent-sandbox",
                "twilio",
                "workato",
                "youtube",
                "zendesk",
                "zoom",
            ]
        ]
        | Omit = omit,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | Omit = omit,
        include_disabled: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ListConnnectorConfigsResponse]:
        """
        List Configured Connectors

        Args:
          include_disabled: Include disabled connector configs in the response. By default, disabled configs
              are filtered out.

          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connector-config",
            page=SyncOffsetPagination[ListConnnectorConfigsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_names": connector_names,
                        "expand": expand,
                        "include_disabled": include_disabled,
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                    },
                    client_list_connnector_configs_params.ClientListConnnectorConfigsParams,
                ),
            ),
            model=cast(
                Any, ListConnnectorConfigsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def list_customers(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ListCustomersResponse]:
        """
        List all customers

        Args:
          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v1/customer",
            page=SyncOffsetPagination[ListCustomersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                    },
                    client_list_customers_params.ClientListCustomersParams,
                ),
            ),
            model=ListCustomersResponse,
        )

    def list_events(
        self,
        *,
        include_prompt: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: str | Omit = omit,
        since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ListEventsResponse]:
        """
        List all events for an organization

        Args:
          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v1/event",
            page=SyncOffsetPagination[ListEventsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_prompt": include_prompt,
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                        "since": since,
                    },
                    client_list_events_params.ClientListEventsParams,
                ),
            ),
            model=cast(Any, ListEventsResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def post_connect(
        self,
        *,
        connector_config_id: str,
        discriminated_data: client_post_connect_params.DiscriminatedData,
        options: client_post_connect_params.Options,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostConnectResponse:
        """Args:
          connector_config_id: Must correspond to data.connector_name.

        Technically id should imply
              connector_name already but there is no way to specify a discriminated union with
              id alone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            PostConnectResponse,
            self.post(
                "/v1/connect/post-connect",
                body=maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "discriminated_data": discriminated_data,
                        "options": options,
                    },
                    client_post_connect_params.ClientPostConnectParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PostConnectResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def pre_configure_connector(
        self,
        *,
        connector_name: Literal[
            "acme-apikey",
            "acme-oauth2",
            "apollo",
            "asana",
            "bigquery",
            "box",
            "calendly",
            "confluence",
            "databricks",
            "discord",
            "dropbox",
            "figma",
            "github",
            "google-calendar",
            "google-docs",
            "google-drive",
            "google-mail",
            "google-sheet",
            "hubspot",
            "instagram",
            "jira",
            "linear",
            "monday",
            "notion",
            "onedrive",
            "outlook",
            "plaid",
            "postgres",
            "resend",
            "salesforce",
            "sendgrid",
            "sharepoint",
            "slack",
            "slack-agent",
            "slack-agent-builder",
            "slack-deployed-agent",
            "snowflake",
            "spotify",
            "stripe",
            "stripe-agent-sandbox",
            "twilio",
            "workato",
            "youtube",
            "zendesk",
            "zoom",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreConfigureConnectorResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v2/connector-config/pre-configure",
            body=maybe_transform(
                {"connector_name": connector_name},
                client_pre_configure_connector_params.ClientPreConfigureConnectorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreConfigureConnectorResponse,
        )

    def pre_connect(
        self,
        *,
        connector_config_id: str,
        discriminated_data: client_pre_connect_params.DiscriminatedData | Omit = omit,
        options: client_pre_connect_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreConnectResponse:
        """Args:
          connector_config_id: Must correspond to data.connector_name.

        Technically id should imply
              connector_name already but there is no way to specify a discriminated union with
              id alone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            PreConnectResponse,
            self.post(
                "/v1/connect/pre-connect",
                body=maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "discriminated_data": discriminated_data,
                        "options": options,
                    },
                    client_pre_connect_params.ClientPreConnectParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PreConnectResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def upsert_connnector_config(
        self,
        id: str,
        *,
        config: Optional[Dict[str, object]] | Omit = omit,
        disabled: bool | Omit = omit,
        display_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpsertConnnectorConfigResponse:
        """
        Args:
          id: The id of the connector config, starts with `ccfg_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            UpsertConnnectorConfigResponse,
            self.put(
                f"/v2/connector-config/{id}",
                body=maybe_transform(
                    {
                        "config": config,
                        "disabled": disabled,
                        "display_name": display_name,
                    },
                    client_upsert_connnector_config_params.ClientUpsertConnnectorConfigParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, UpsertConnnectorConfigResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def upsert_customer(
        self,
        *,
        id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpsertCustomerResponse:
        """
        Create or update a customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.put(
            "/v1/customer",
            body=maybe_transform(
                {
                    "id": id,
                    "metadata": metadata,
                },
                client_upsert_customer_params.ClientUpsertCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpsertCustomerResponse,
        )

    def upsert_organization(
        self,
        org_id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpsertOrganizationResponse:
        """Upsert an organization by ID.

        Creates if it does not exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self.put(
            f"/v2/organization/{org_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                client_upsert_organization_params.ClientUpsertOrganizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpsertOrganizationResponse,
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
    token: str | None

    def __init__(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

        This automatically infers the `token` argument from the `OPENINT_API_KEY` environment variable if it is not provided.
        """
        if token is None:
            token = os.environ.get("OPENINT_API_KEY")
        self.token = token

        if base_url is None:
            base_url = os.environ.get("OPENINT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openint.dev"

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
        token = self.token
        if token is None:
            return {}
        return {"Authorization": f"Bearer {token}"}

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
        if self.token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            token=token or self.token,
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

    async def assign_connection(
        self,
        repl_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssignConnectionResponse:
        """
        Assign a connection to a customer

        Args:
          id: The id of the connection, starts with `conn_`

          repl_id: The repl ID to assign to this connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not repl_id:
            raise ValueError(f"Expected a non-empty value for `repl_id` but received {repl_id!r}")
        return await self.put(
            f"/v2/connection/{id}/assignment/{repl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssignConnectionResponse,
        )

    async def check_connection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v1/connection/{id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckConnectionResponse,
        )

    async def connector_rpc(
        self,
        function_name: str,
        *,
        connector_config_id: str,
        input: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorRpcResponse:
        """
        Execute RPC function on connector

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          function_name: RPC function name to execute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_config_id:
            raise ValueError(
                f"Expected a non-empty value for `connector_config_id` but received {connector_config_id!r}"
            )
        if not function_name:
            raise ValueError(f"Expected a non-empty value for `function_name` but received {function_name!r}")
        return await self.post(
            f"/v2/connector-config/{connector_config_id}/rpc/{function_name}",
            body=await async_maybe_transform({"input": input}, client_connector_rpc_params.ClientConnectorRpcParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorRpcResponse,
        )

    async def create_connection(
        self,
        *,
        connector_config_id: str,
        data: client_create_connection_params.Data,
        check_connection: bool | Omit = omit,
        customer_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Import an existing connection after validation

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          data: Connector specific data

          check_connection: Perform a synchronous connection check before creating it.

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v2/connection",
            body=await async_maybe_transform(
                {
                    "connector_config_id": connector_config_id,
                    "data": data,
                    "check_connection": check_connection,
                    "customer_id": customer_id,
                    "metadata": metadata,
                },
                client_create_connection_params.ClientCreateConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_connnector_config(
        self,
        *,
        connector_name: str,
        config: Optional[Dict[str, object]] | Omit = omit,
        disabled: Optional[bool] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateConnnectorConfigResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CreateConnnectorConfigResponse,
            await self.post(
                "/v2/connector-config",
                body=await async_maybe_transform(
                    {
                        "connector_name": connector_name,
                        "config": config,
                        "disabled": disabled,
                        "display_name": display_name,
                        "metadata": metadata,
                    },
                    client_create_connnector_config_params.ClientCreateConnnectorConfigParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, CreateConnnectorConfigResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def create_token(
        self,
        customer_id: str,
        *,
        connect_options: client_create_token_params.ConnectOptions | Omit = omit,
        validity_in_seconds: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateTokenResponse:
        """Create a @Connect authentication token for a customer.

        This token can be used to
        embed @Connect in your application via the `@openint/connect` npm package.

        Args:
          customer_id: The unique ID of the customer to create the token for

          validity_in_seconds: How long the publishable token and magic link url will be valid for (in seconds)
              before it expires. By default it will be valid for 30 days unless otherwise
              specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self.post(
            f"/v1/customer/{customer_id}/token",
            body=await async_maybe_transform(
                {
                    "connect_options": connect_options,
                    "validity_in_seconds": validity_in_seconds,
                },
                client_create_token_params.ClientCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTokenResponse,
        )

    async def delete_assignment(
        self,
        repl_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteAssignmentResponse:
        """
        Remove a repl assignment from a connection

        Args:
          id: The id of the connection, starts with `conn_`

          repl_id: The repl ID to remove from this connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not repl_id:
            raise ValueError(f"Expected a non-empty value for `repl_id` but received {repl_id!r}")
        return await self.delete(
            f"/v2/connection/{id}/assignment/{repl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteAssignmentResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/connection/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteConnectionResponse,
        )

    async def delete_connector_config(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteConnectorConfigResponse:
        """
        Args:
          id: The id of the connector config, starts with `ccfg_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self.delete(
            f"/v2/connector-config/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteConnectorConfigResponse,
        )

    async def get_conector_config(
        self,
        id: str,
        *,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetConectorConfigResponse:
        """
        Args:
          id: The id of the connector config, starts with `ccfg_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            GetConectorConfigResponse,
            await self.get(
                f"/v2/connector-config/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"expand": expand}, client_get_conector_config_params.ClientGetConectorConfigParams
                    ),
                ),
                cast_to=cast(
                    Any, GetConectorConfigResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get_connection(
        self,
        id: str,
        *,
        expand: List[Literal["connector"]] | Omit = omit,
        include_secrets: bool | Omit = omit,
        refresh_policy: Literal["none", "force", "auto"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get details of a specific connection, including credentials

        Args:
          id: The id of the connection, starts with `conn_`

          refresh_policy: Controls credential refresh: none (never), force (always), or auto (when
              expired, default)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self.get(
            f"/v2/connection/{id}",
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
            cast_to=object,
        )

    async def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetCurrentUserResponse:
        """Get information about the current authenticated user"""
        return await self.get(
            "/v1/viewer",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetCurrentUserResponse,
        )

    async def list_assignments(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListAssignmentsResponse:
        """
        Get the list of assignments for a specific connection

        Args:
          id: The id of the connection, starts with `conn_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self.get(
            f"/v2/connection/{id}/assignment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListAssignmentsResponse,
        )

    def list_connections(
        self,
        *,
        connection_ids: SequenceNotStr[str] | Omit = omit,
        connector_config_id: str | Omit = omit,
        connector_names: List[
            Literal[
                "acme-apikey",
                "acme-oauth2",
                "apollo",
                "asana",
                "bigquery",
                "box",
                "calendly",
                "confluence",
                "databricks",
                "discord",
                "dropbox",
                "figma",
                "github",
                "google-calendar",
                "google-docs",
                "google-drive",
                "google-mail",
                "google-sheet",
                "hubspot",
                "instagram",
                "jira",
                "linear",
                "monday",
                "notion",
                "onedrive",
                "outlook",
                "plaid",
                "postgres",
                "resend",
                "salesforce",
                "sendgrid",
                "sharepoint",
                "slack",
                "slack-agent",
                "slack-agent-builder",
                "slack-deployed-agent",
                "snowflake",
                "spotify",
                "stripe",
                "stripe-agent-sandbox",
                "twilio",
                "workato",
                "youtube",
                "zendesk",
                "zoom",
            ]
        ]
        | Omit = omit,
        customer_id: str | Omit = omit,
        expand: List[Literal["connector"]] | Omit = omit,
        include_secrets: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        refresh_policy: Literal["none", "force", "auto"] | Omit = omit,
        repl_id: str | Omit = omit,
        search_query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[object, AsyncOffsetPagination[object]]:
        """List all connections with optional filtering.

        Does not retrieve secrets or
        perform any connection healthcheck. For that use `getConnection` or
        `checkConnectionHealth`.

        Args:
          connector_config_id: The id of the connector config, starts with `ccfg_`

          customer_id: The id of the customer in your application. Ensure it is unique for that
              customer.

          expand: Expand the response with additional optionals

          limit: Limit the number of items returned

          offset: Offset the items returned

          refresh_policy: Controls credential refresh: none (never), force (always), or auto (when
              expired, default)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connection",
            page=AsyncOffsetPagination[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_ids": connection_ids,
                        "connector_config_id": connector_config_id,
                        "connector_names": connector_names,
                        "customer_id": customer_id,
                        "expand": expand,
                        "include_secrets": include_secrets,
                        "limit": limit,
                        "offset": offset,
                        "refresh_policy": refresh_policy,
                        "repl_id": repl_id,
                        "search_query": search_query,
                    },
                    client_list_connections_params.ClientListConnectionsParams,
                ),
            ),
            model=object,
        )

    def list_connector_configs(
        self,
        *,
        connector_names: List[
            Literal[
                "acme-apikey",
                "acme-oauth2",
                "apollo",
                "asana",
                "bigquery",
                "box",
                "calendly",
                "confluence",
                "databricks",
                "discord",
                "dropbox",
                "figma",
                "github",
                "google-calendar",
                "google-docs",
                "google-drive",
                "google-mail",
                "google-sheet",
                "hubspot",
                "instagram",
                "jira",
                "linear",
                "monday",
                "notion",
                "onedrive",
                "outlook",
                "plaid",
                "postgres",
                "resend",
                "salesforce",
                "sendgrid",
                "sharepoint",
                "slack",
                "slack-agent",
                "slack-agent-builder",
                "slack-deployed-agent",
                "snowflake",
                "spotify",
                "stripe",
                "stripe-agent-sandbox",
                "twilio",
                "workato",
                "youtube",
                "zendesk",
                "zoom",
            ]
        ]
        | Omit = omit,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | Omit = omit,
        include_disabled: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ListConnectorConfigsResponse, AsyncOffsetPagination[ListConnectorConfigsResponse]]:
        """
        List Configured Connectors

        Args:
          include_disabled: Include disabled connector configs in the response. By default, disabled configs
              are filtered out.

          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connector-config",
            page=AsyncOffsetPagination[ListConnectorConfigsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_names": connector_names,
                        "expand": expand,
                        "include_disabled": include_disabled,
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                    },
                    client_list_connector_configs_params.ClientListConnectorConfigsParams,
                ),
            ),
            model=cast(
                Any, ListConnectorConfigsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def list_connectors(
        self,
        *,
        connector_name: str | Omit = omit,
        expand: List[Literal["schemas"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ListConnectorsResponse, AsyncOffsetPagination[ListConnectorsResponse]]:
        """
        List all connectors to understand what integrations are available to configure

        Args:
          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connector",
            page=AsyncOffsetPagination[ListConnectorsResponse],
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
                    client_list_connectors_params.ClientListConnectorsParams,
                ),
            ),
            model=ListConnectorsResponse,
        )

    def list_connnector_configs(
        self,
        *,
        connector_names: List[
            Literal[
                "acme-apikey",
                "acme-oauth2",
                "apollo",
                "asana",
                "bigquery",
                "box",
                "calendly",
                "confluence",
                "databricks",
                "discord",
                "dropbox",
                "figma",
                "github",
                "google-calendar",
                "google-docs",
                "google-drive",
                "google-mail",
                "google-sheet",
                "hubspot",
                "instagram",
                "jira",
                "linear",
                "monday",
                "notion",
                "onedrive",
                "outlook",
                "plaid",
                "postgres",
                "resend",
                "salesforce",
                "sendgrid",
                "sharepoint",
                "slack",
                "slack-agent",
                "slack-agent-builder",
                "slack-deployed-agent",
                "snowflake",
                "spotify",
                "stripe",
                "stripe-agent-sandbox",
                "twilio",
                "workato",
                "youtube",
                "zendesk",
                "zoom",
            ]
        ]
        | Omit = omit,
        expand: List[Literal["connector", "connector.schemas", "connection_count"]] | Omit = omit,
        include_disabled: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ListConnnectorConfigsResponse, AsyncOffsetPagination[ListConnnectorConfigsResponse]]:
        """
        List Configured Connectors

        Args:
          include_disabled: Include disabled connector configs in the response. By default, disabled configs
              are filtered out.

          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v2/connector-config",
            page=AsyncOffsetPagination[ListConnnectorConfigsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connector_names": connector_names,
                        "expand": expand,
                        "include_disabled": include_disabled,
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                    },
                    client_list_connnector_configs_params.ClientListConnnectorConfigsParams,
                ),
            ),
            model=cast(
                Any, ListConnnectorConfigsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def list_customers(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ListCustomersResponse, AsyncOffsetPagination[ListCustomersResponse]]:
        """
        List all customers

        Args:
          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v1/customer",
            page=AsyncOffsetPagination[ListCustomersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                    },
                    client_list_customers_params.ClientListCustomersParams,
                ),
            ),
            model=ListCustomersResponse,
        )

    def list_events(
        self,
        *,
        include_prompt: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: str | Omit = omit,
        since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ListEventsResponse, AsyncOffsetPagination[ListEventsResponse]]:
        """
        List all events for an organization

        Args:
          limit: Limit the number of items returned

          offset: Offset the items returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v1/event",
            page=AsyncOffsetPagination[ListEventsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_prompt": include_prompt,
                        "limit": limit,
                        "offset": offset,
                        "search_query": search_query,
                        "since": since,
                    },
                    client_list_events_params.ClientListEventsParams,
                ),
            ),
            model=cast(Any, ListEventsResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def post_connect(
        self,
        *,
        connector_config_id: str,
        discriminated_data: client_post_connect_params.DiscriminatedData,
        options: client_post_connect_params.Options,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostConnectResponse:
        """Args:
          connector_config_id: Must correspond to data.connector_name.

        Technically id should imply
              connector_name already but there is no way to specify a discriminated union with
              id alone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            PostConnectResponse,
            await self.post(
                "/v1/connect/post-connect",
                body=await async_maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "discriminated_data": discriminated_data,
                        "options": options,
                    },
                    client_post_connect_params.ClientPostConnectParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PostConnectResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def pre_configure_connector(
        self,
        *,
        connector_name: Literal[
            "acme-apikey",
            "acme-oauth2",
            "apollo",
            "asana",
            "bigquery",
            "box",
            "calendly",
            "confluence",
            "databricks",
            "discord",
            "dropbox",
            "figma",
            "github",
            "google-calendar",
            "google-docs",
            "google-drive",
            "google-mail",
            "google-sheet",
            "hubspot",
            "instagram",
            "jira",
            "linear",
            "monday",
            "notion",
            "onedrive",
            "outlook",
            "plaid",
            "postgres",
            "resend",
            "salesforce",
            "sendgrid",
            "sharepoint",
            "slack",
            "slack-agent",
            "slack-agent-builder",
            "slack-deployed-agent",
            "snowflake",
            "spotify",
            "stripe",
            "stripe-agent-sandbox",
            "twilio",
            "workato",
            "youtube",
            "zendesk",
            "zoom",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreConfigureConnectorResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v2/connector-config/pre-configure",
            body=await async_maybe_transform(
                {"connector_name": connector_name},
                client_pre_configure_connector_params.ClientPreConfigureConnectorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreConfigureConnectorResponse,
        )

    async def pre_connect(
        self,
        *,
        connector_config_id: str,
        discriminated_data: client_pre_connect_params.DiscriminatedData | Omit = omit,
        options: client_pre_connect_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreConnectResponse:
        """Args:
          connector_config_id: Must correspond to data.connector_name.

        Technically id should imply
              connector_name already but there is no way to specify a discriminated union with
              id alone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            PreConnectResponse,
            await self.post(
                "/v1/connect/pre-connect",
                body=await async_maybe_transform(
                    {
                        "connector_config_id": connector_config_id,
                        "discriminated_data": discriminated_data,
                        "options": options,
                    },
                    client_pre_connect_params.ClientPreConnectParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PreConnectResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def upsert_connnector_config(
        self,
        id: str,
        *,
        config: Optional[Dict[str, object]] | Omit = omit,
        disabled: bool | Omit = omit,
        display_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpsertConnnectorConfigResponse:
        """
        Args:
          id: The id of the connector config, starts with `ccfg_`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            UpsertConnnectorConfigResponse,
            await self.put(
                f"/v2/connector-config/{id}",
                body=await async_maybe_transform(
                    {
                        "config": config,
                        "disabled": disabled,
                        "display_name": display_name,
                    },
                    client_upsert_connnector_config_params.ClientUpsertConnnectorConfigParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, UpsertConnnectorConfigResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def upsert_customer(
        self,
        *,
        id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpsertCustomerResponse:
        """
        Create or update a customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.put(
            "/v1/customer",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "metadata": metadata,
                },
                client_upsert_customer_params.ClientUpsertCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpsertCustomerResponse,
        )

    async def upsert_organization(
        self,
        org_id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpsertOrganizationResponse:
        """Upsert an organization by ID.

        Creates if it does not exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self.put(
            f"/v2/organization/{org_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                client_upsert_organization_params.ClientUpsertOrganizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpsertOrganizationResponse,
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
        self.assign_connection = to_raw_response_wrapper(
            client.assign_connection,
        )
        self.check_connection = to_raw_response_wrapper(
            client.check_connection,
        )
        self.connector_rpc = to_raw_response_wrapper(
            client.connector_rpc,
        )
        self.create_connection = to_raw_response_wrapper(
            client.create_connection,
        )
        self.create_connnector_config = to_raw_response_wrapper(
            client.create_connnector_config,
        )
        self.create_token = to_raw_response_wrapper(
            client.create_token,
        )
        self.delete_assignment = to_raw_response_wrapper(
            client.delete_assignment,
        )
        self.delete_connection = to_raw_response_wrapper(
            client.delete_connection,
        )
        self.delete_connector_config = to_raw_response_wrapper(
            client.delete_connector_config,
        )
        self.get_conector_config = to_raw_response_wrapper(
            client.get_conector_config,
        )
        self.get_connection = to_raw_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = to_raw_response_wrapper(
            client.get_current_user,
        )
        self.list_assignments = to_raw_response_wrapper(
            client.list_assignments,
        )
        self.list_connections = to_raw_response_wrapper(
            client.list_connections,
        )
        self.list_connector_configs = to_raw_response_wrapper(
            client.list_connector_configs,
        )
        self.list_connectors = to_raw_response_wrapper(
            client.list_connectors,
        )
        self.list_connnector_configs = to_raw_response_wrapper(
            client.list_connnector_configs,
        )
        self.list_customers = to_raw_response_wrapper(
            client.list_customers,
        )
        self.list_events = to_raw_response_wrapper(
            client.list_events,
        )
        self.post_connect = to_raw_response_wrapper(
            client.post_connect,
        )
        self.pre_configure_connector = to_raw_response_wrapper(
            client.pre_configure_connector,
        )
        self.pre_connect = to_raw_response_wrapper(
            client.pre_connect,
        )
        self.upsert_connnector_config = to_raw_response_wrapper(
            client.upsert_connnector_config,
        )
        self.upsert_customer = to_raw_response_wrapper(
            client.upsert_customer,
        )
        self.upsert_organization = to_raw_response_wrapper(
            client.upsert_organization,
        )


class AsyncOpenintWithRawResponse:
    def __init__(self, client: AsyncOpenint) -> None:
        self.assign_connection = async_to_raw_response_wrapper(
            client.assign_connection,
        )
        self.check_connection = async_to_raw_response_wrapper(
            client.check_connection,
        )
        self.connector_rpc = async_to_raw_response_wrapper(
            client.connector_rpc,
        )
        self.create_connection = async_to_raw_response_wrapper(
            client.create_connection,
        )
        self.create_connnector_config = async_to_raw_response_wrapper(
            client.create_connnector_config,
        )
        self.create_token = async_to_raw_response_wrapper(
            client.create_token,
        )
        self.delete_assignment = async_to_raw_response_wrapper(
            client.delete_assignment,
        )
        self.delete_connection = async_to_raw_response_wrapper(
            client.delete_connection,
        )
        self.delete_connector_config = async_to_raw_response_wrapper(
            client.delete_connector_config,
        )
        self.get_conector_config = async_to_raw_response_wrapper(
            client.get_conector_config,
        )
        self.get_connection = async_to_raw_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = async_to_raw_response_wrapper(
            client.get_current_user,
        )
        self.list_assignments = async_to_raw_response_wrapper(
            client.list_assignments,
        )
        self.list_connections = async_to_raw_response_wrapper(
            client.list_connections,
        )
        self.list_connector_configs = async_to_raw_response_wrapper(
            client.list_connector_configs,
        )
        self.list_connectors = async_to_raw_response_wrapper(
            client.list_connectors,
        )
        self.list_connnector_configs = async_to_raw_response_wrapper(
            client.list_connnector_configs,
        )
        self.list_customers = async_to_raw_response_wrapper(
            client.list_customers,
        )
        self.list_events = async_to_raw_response_wrapper(
            client.list_events,
        )
        self.post_connect = async_to_raw_response_wrapper(
            client.post_connect,
        )
        self.pre_configure_connector = async_to_raw_response_wrapper(
            client.pre_configure_connector,
        )
        self.pre_connect = async_to_raw_response_wrapper(
            client.pre_connect,
        )
        self.upsert_connnector_config = async_to_raw_response_wrapper(
            client.upsert_connnector_config,
        )
        self.upsert_customer = async_to_raw_response_wrapper(
            client.upsert_customer,
        )
        self.upsert_organization = async_to_raw_response_wrapper(
            client.upsert_organization,
        )


class OpenintWithStreamedResponse:
    def __init__(self, client: Openint) -> None:
        self.assign_connection = to_streamed_response_wrapper(
            client.assign_connection,
        )
        self.check_connection = to_streamed_response_wrapper(
            client.check_connection,
        )
        self.connector_rpc = to_streamed_response_wrapper(
            client.connector_rpc,
        )
        self.create_connection = to_streamed_response_wrapper(
            client.create_connection,
        )
        self.create_connnector_config = to_streamed_response_wrapper(
            client.create_connnector_config,
        )
        self.create_token = to_streamed_response_wrapper(
            client.create_token,
        )
        self.delete_assignment = to_streamed_response_wrapper(
            client.delete_assignment,
        )
        self.delete_connection = to_streamed_response_wrapper(
            client.delete_connection,
        )
        self.delete_connector_config = to_streamed_response_wrapper(
            client.delete_connector_config,
        )
        self.get_conector_config = to_streamed_response_wrapper(
            client.get_conector_config,
        )
        self.get_connection = to_streamed_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = to_streamed_response_wrapper(
            client.get_current_user,
        )
        self.list_assignments = to_streamed_response_wrapper(
            client.list_assignments,
        )
        self.list_connections = to_streamed_response_wrapper(
            client.list_connections,
        )
        self.list_connector_configs = to_streamed_response_wrapper(
            client.list_connector_configs,
        )
        self.list_connectors = to_streamed_response_wrapper(
            client.list_connectors,
        )
        self.list_connnector_configs = to_streamed_response_wrapper(
            client.list_connnector_configs,
        )
        self.list_customers = to_streamed_response_wrapper(
            client.list_customers,
        )
        self.list_events = to_streamed_response_wrapper(
            client.list_events,
        )
        self.post_connect = to_streamed_response_wrapper(
            client.post_connect,
        )
        self.pre_configure_connector = to_streamed_response_wrapper(
            client.pre_configure_connector,
        )
        self.pre_connect = to_streamed_response_wrapper(
            client.pre_connect,
        )
        self.upsert_connnector_config = to_streamed_response_wrapper(
            client.upsert_connnector_config,
        )
        self.upsert_customer = to_streamed_response_wrapper(
            client.upsert_customer,
        )
        self.upsert_organization = to_streamed_response_wrapper(
            client.upsert_organization,
        )


class AsyncOpenintWithStreamedResponse:
    def __init__(self, client: AsyncOpenint) -> None:
        self.assign_connection = async_to_streamed_response_wrapper(
            client.assign_connection,
        )
        self.check_connection = async_to_streamed_response_wrapper(
            client.check_connection,
        )
        self.connector_rpc = async_to_streamed_response_wrapper(
            client.connector_rpc,
        )
        self.create_connection = async_to_streamed_response_wrapper(
            client.create_connection,
        )
        self.create_connnector_config = async_to_streamed_response_wrapper(
            client.create_connnector_config,
        )
        self.create_token = async_to_streamed_response_wrapper(
            client.create_token,
        )
        self.delete_assignment = async_to_streamed_response_wrapper(
            client.delete_assignment,
        )
        self.delete_connection = async_to_streamed_response_wrapper(
            client.delete_connection,
        )
        self.delete_connector_config = async_to_streamed_response_wrapper(
            client.delete_connector_config,
        )
        self.get_conector_config = async_to_streamed_response_wrapper(
            client.get_conector_config,
        )
        self.get_connection = async_to_streamed_response_wrapper(
            client.get_connection,
        )
        self.get_current_user = async_to_streamed_response_wrapper(
            client.get_current_user,
        )
        self.list_assignments = async_to_streamed_response_wrapper(
            client.list_assignments,
        )
        self.list_connections = async_to_streamed_response_wrapper(
            client.list_connections,
        )
        self.list_connector_configs = async_to_streamed_response_wrapper(
            client.list_connector_configs,
        )
        self.list_connectors = async_to_streamed_response_wrapper(
            client.list_connectors,
        )
        self.list_connnector_configs = async_to_streamed_response_wrapper(
            client.list_connnector_configs,
        )
        self.list_customers = async_to_streamed_response_wrapper(
            client.list_customers,
        )
        self.list_events = async_to_streamed_response_wrapper(
            client.list_events,
        )
        self.post_connect = async_to_streamed_response_wrapper(
            client.post_connect,
        )
        self.pre_configure_connector = async_to_streamed_response_wrapper(
            client.pre_configure_connector,
        )
        self.pre_connect = async_to_streamed_response_wrapper(
            client.pre_connect,
        )
        self.upsert_connnector_config = async_to_streamed_response_wrapper(
            client.upsert_connnector_config,
        )
        self.upsert_customer = async_to_streamed_response_wrapper(
            client.upsert_customer,
        )
        self.upsert_organization = async_to_streamed_response_wrapper(
            client.upsert_organization,
        )


Client = Openint

AsyncClient = AsyncOpenint
