# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ClientListConnectionsParams"]


class ClientListConnectionsParams(TypedDict, total=False):
    connection_ids: SequenceNotStr[str]

    connector_config_id: str
    """The id of the connector config, starts with `ccfg_`"""

    connector_names: List[
        Literal[
            "acme-apikey",
            "acme-oauth2",
            "apollo",
            "asana",
            "bigquery",
            "box",
            "calendly",
            "confluence",
            "databricks",
            "discord",
            "dropbox",
            "figma",
            "github",
            "google-calendar",
            "google-docs",
            "google-drive",
            "google-mail",
            "google-sheet",
            "hubspot",
            "instagram",
            "jira",
            "linear",
            "monday",
            "notion",
            "onedrive",
            "outlook",
            "plaid",
            "postgres",
            "resend",
            "salesforce",
            "sendgrid",
            "sharepoint",
            "slack",
            "slack-agent",
            "slack-agent-builder",
            "slack-deployed-agent",
            "snowflake",
            "spotify",
            "stripe",
            "stripe-agent-sandbox",
            "twilio",
            "workato",
            "youtube",
            "zendesk",
            "zoom",
        ]
    ]

    customer_id: str
    """The id of the customer in your application.

    Ensure it is unique for that customer.
    """

    expand: List[Literal["connector"]]
    """Expand the response with additional optionals"""

    include_secrets: bool

    limit: int
    """Limit the number of items returned"""

    offset: int
    """Offset the items returned"""

    refresh_policy: Literal["none", "force", "auto"]
    """
    Controls credential refresh: none (never), force (always), or auto (when
    expired, default)
    """

    repl_id: str

    search_query: str
