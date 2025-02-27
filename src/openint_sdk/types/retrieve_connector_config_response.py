# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "RetrieveConnectorConfigResponse",
    "Item",
    "ItemPlaidConnectorConfig",
    "ItemPlaidConnectorConfigConfig",
    "ItemPlaidConnectorConfigSecrets",
    "ItemGreenhouseConnectorConfig",
]


class ItemPlaidConnectorConfigConfig(BaseModel):
    client_name: str

    products: List[Literal["transactions", "balances"]]


class ItemPlaidConnectorConfigSecrets(BaseModel):
    client_id: str

    client_secret: str


class ItemPlaidConnectorConfig(BaseModel):
    config: ItemPlaidConnectorConfigConfig

    connector_name: Literal["plaid"]

    secrets: ItemPlaidConnectorConfigSecrets

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    org_id: Optional[str] = None

    updated_at: Optional[datetime] = None


class ItemGreenhouseConnectorConfig(BaseModel):
    config: object

    connector_name: Literal["greenhouse"]

    secrets: object

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    org_id: Optional[str] = None

    updated_at: Optional[datetime] = None


Item: TypeAlias = Union[ItemPlaidConnectorConfig, ItemGreenhouseConnectorConfig]


class RetrieveConnectorConfigResponse(BaseModel):
    items: List[Item]
