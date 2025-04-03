# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ClientListConnectorsParams"]


class ClientListConnectorsParams(TypedDict, total=False):
    expand: str
    """Comma separated list of fields to optionally expand.

    Available Options: `integrations`
    """
