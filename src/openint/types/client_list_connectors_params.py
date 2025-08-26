# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ClientListConnectorsParams"]


class ClientListConnectorsParams(TypedDict, total=False):
    connector_name: str

    expand: List[Literal["schemas"]]

    limit: int
    """Limit the number of items returned"""

    offset: int
    """Offset the items returned"""
