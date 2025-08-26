# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AssignConnectionResponse"]


class AssignConnectionResponse(BaseModel):
    id: str
    """The id of the connection, starts with `conn_`"""

    assignments: Optional[List[str]] = None
