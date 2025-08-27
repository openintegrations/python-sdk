# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ClientConnectorRpcParams"]


class ClientConnectorRpcParams(TypedDict, total=False):
    connector_config_id: Required[str]
    """The id of the connector config, starts with `ccfg_`"""

    input: Required[Dict[str, object]]
