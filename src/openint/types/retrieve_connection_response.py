# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "RetrieveConnectionResponse",
    "Item",
    "ItemPlaidConnection",
    "ItemPlaidConnectionSecrets",
    "ItemPlaidConnectionSettings",
    "ItemGreenhouseConnection",
    "ItemGreenhouseConnectionSecrets",
]


class ItemPlaidConnectionSecrets(BaseModel):
    access_token: str


class ItemPlaidConnectionSettings(BaseModel):
    item_id: str


class ItemPlaidConnection(BaseModel):
    connector_name: Literal["plaid"]

    secrets: ItemPlaidConnectionSecrets

    settings: ItemPlaidConnectionSettings

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class ItemGreenhouseConnectionSecrets(BaseModel):
    api_key: str


class ItemGreenhouseConnection(BaseModel):
    connector_name: Literal["greenhouse"]

    secrets: ItemGreenhouseConnectionSecrets

    settings: object

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


Item: TypeAlias = Union[ItemPlaidConnection, ItemGreenhouseConnection]


class RetrieveConnectionResponse(BaseModel):
    items: List[Item]
