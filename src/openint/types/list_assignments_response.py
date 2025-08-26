# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ListAssignmentsResponse"]


class ListAssignmentsResponse(BaseModel):
    id: str
    """The id of the connection, starts with `conn_`"""

    assignments: List[str]
