# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DeleteConnectorConfigResponse"]


class DeleteConnectorConfigResponse(BaseModel):
    id: str
    """The id of the connector config, starts with `ccfg_`"""
