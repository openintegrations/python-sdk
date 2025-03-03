# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openint import Openint, AsyncOpenint
from tests.utils import assert_matches_type
from openint.types import ConnectorConfigRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectorConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Openint) -> None:
        connector_config = client.connector_config.retrieve()
        assert_matches_type(ConnectorConfigRetrieveResponse, connector_config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Openint) -> None:
        response = client.connector_config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector_config = response.parse()
        assert_matches_type(ConnectorConfigRetrieveResponse, connector_config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Openint) -> None:
        with client.connector_config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector_config = response.parse()
            assert_matches_type(ConnectorConfigRetrieveResponse, connector_config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnectorConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenint) -> None:
        connector_config = await async_client.connector_config.retrieve()
        assert_matches_type(ConnectorConfigRetrieveResponse, connector_config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenint) -> None:
        response = await async_client.connector_config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector_config = await response.parse()
        assert_matches_type(ConnectorConfigRetrieveResponse, connector_config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenint) -> None:
        async with async_client.connector_config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector_config = await response.parse()
            assert_matches_type(ConnectorConfigRetrieveResponse, connector_config, path=["response"])

        assert cast(Any, response.is_closed) is True
