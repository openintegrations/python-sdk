# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ClientListConnectionsParams"]


class ClientListConnectionsParams(TypedDict, total=False):
    connector_config_id: str

    connector_name: Literal[
        "aircall",
        "airtable",
        "apollo",
        "beancount",
        "brex",
        "coda",
        "confluence",
        "discord",
        "finch",
        "firebase",
        "foreceipt",
        "github",
        "gong",
        "google",
        "greenhouse",
        "heron",
        "hubspot",
        "intercom",
        "jira",
        "kustomer",
        "lever",
        "linear",
        "lunchmoney",
        "merge",
        "microsoft",
        "moota",
        "onebrick",
        "outreach",
        "pipedrive",
        "plaid",
        "qbo",
        "ramp",
        "salesforce",
        "salesloft",
        "saltedge",
        "slack",
        "splitwise",
        "stripe",
        "teller",
        "toggl",
        "twenty",
        "wise",
        "xero",
        "yodlee",
        "zohodesk",
        "googledrive",
    ]
    """The name of the connector"""

    customer_id: str

    expand: List[Literal["connector"]]

    include_secrets: Literal["none", "basic", "all"]
    """Controls secret inclusion: none (default), basic (auth only), or all secrets"""

    limit: int

    offset: int
