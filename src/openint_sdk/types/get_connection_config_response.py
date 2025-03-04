# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["GetConnectionConfigResponse", "Item"]


class Item(BaseModel):
    id: str

    org_id: str


class GetConnectionConfigResponse(BaseModel):
    items: List[Item]
