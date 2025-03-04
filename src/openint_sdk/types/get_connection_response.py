# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GetConnectionResponse", "Item"]


class Item(BaseModel):
    id: str

    connector_config_id: Optional[str] = None


class GetConnectionResponse(BaseModel):
    items: List[Item]
