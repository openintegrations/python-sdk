# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openint_sdk import Openint, AsyncOpenint
from tests.utils import assert_matches_type
from openint_sdk.types import CheckHealthResponse, GetConnectionResponse, GetConnectionConfigResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_health(self, client: Openint) -> None:
        client_ = client.check_health()
        assert_matches_type(CheckHealthResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_health(self, client: Openint) -> None:
        response = client.with_raw_response.check_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(CheckHealthResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_health(self, client: Openint) -> None:
        with client.with_streaming_response.check_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(CheckHealthResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_connection(self, client: Openint) -> None:
        client_ = client.get_connection()
        assert_matches_type(GetConnectionResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_connection(self, client: Openint) -> None:
        response = client.with_raw_response.get_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GetConnectionResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_connection(self, client: Openint) -> None:
        with client.with_streaming_response.get_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GetConnectionResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_connection_config(self, client: Openint) -> None:
        client_ = client.get_connection_config()
        assert_matches_type(GetConnectionConfigResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_connection_config(self, client: Openint) -> None:
        response = client.with_raw_response.get_connection_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GetConnectionConfigResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_connection_config(self, client: Openint) -> None:
        with client.with_streaming_response.get_connection_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GetConnectionConfigResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_health(self, async_client: AsyncOpenint) -> None:
        client = await async_client.check_health()
        assert_matches_type(CheckHealthResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_health(self, async_client: AsyncOpenint) -> None:
        response = await async_client.with_raw_response.check_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(CheckHealthResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_health(self, async_client: AsyncOpenint) -> None:
        async with async_client.with_streaming_response.check_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(CheckHealthResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_connection(self, async_client: AsyncOpenint) -> None:
        client = await async_client.get_connection()
        assert_matches_type(GetConnectionResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_connection(self, async_client: AsyncOpenint) -> None:
        response = await async_client.with_raw_response.get_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GetConnectionResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_connection(self, async_client: AsyncOpenint) -> None:
        async with async_client.with_streaming_response.get_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GetConnectionResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_connection_config(self, async_client: AsyncOpenint) -> None:
        client = await async_client.get_connection_config()
        assert_matches_type(GetConnectionConfigResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_connection_config(self, async_client: AsyncOpenint) -> None:
        response = await async_client.with_raw_response.get_connection_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GetConnectionConfigResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_connection_config(self, async_client: AsyncOpenint) -> None:
        async with async_client.with_streaming_response.get_connection_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GetConnectionConfigResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
