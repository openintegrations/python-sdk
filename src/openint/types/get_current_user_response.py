# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GetCurrentUserResponse", "Role", "UnionMember1", "UnionMember2", "UnionMember3"]


class Role(BaseModel):
    role: Literal["anon"]


class UnionMember1(BaseModel):
    customer_id: str = FieldInfo(alias="customerId")

    org_id: str = FieldInfo(alias="orgId")

    role: Literal["customer"]


class UnionMember2(BaseModel):
    role: Literal["user"]

    user_id: str = FieldInfo(alias="userId")

    extra: Optional[Dict[str, object]] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)


class UnionMember3(BaseModel):
    org_id: str = FieldInfo(alias="orgId")

    role: Literal["org"]

    extra: Optional[Dict[str, object]] = None


GetCurrentUserResponse: TypeAlias = Union[Role, UnionMember1, UnionMember2, UnionMember3, Role]
