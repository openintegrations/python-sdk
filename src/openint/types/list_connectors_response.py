# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ListConnectorsResponse",
    "ListConnectorsResponseItem",
    "ListConnectorsResponseItemIntegration",
    "ListConnectorsResponseItemSchemas",
    "ListConnectorsResponseItemScope",
]


class ListConnectorsResponseItemIntegration(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ListConnectorsResponseItemSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ListConnectorsResponseItemScope(BaseModel):
    scope: str

    description: Optional[str] = None

    display_name: Optional[str] = None


class ListConnectorsResponseItem(BaseModel):
    name: str

    display_name: Optional[str] = None

    integrations: Optional[List[ListConnectorsResponseItemIntegration]] = None

    logo_url: Optional[str] = None

    openint_scopes: Optional[List[str]] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ListConnectorsResponseItemSchemas] = None

    scopes: Optional[List[ListConnectorsResponseItemScope]] = None

    stage: Optional[Literal["alpha", "beta", "ga", "hidden"]] = None


ListConnectorsResponse: TypeAlias = List[ListConnectorsResponseItem]
