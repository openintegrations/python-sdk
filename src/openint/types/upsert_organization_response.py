# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["UpsertOrganizationResponse"]


class UpsertOrganizationResponse(BaseModel):
    id: str

    api_key: str

    created: bool
