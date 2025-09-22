# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ClientListConnnectorConfigsParams"]


class ClientListConnnectorConfigsParams(TypedDict, total=False):
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

    expand: List[Literal["connector", "connector.schemas", "connection_count"]]

    include_disabled: bool
    """Include disabled connector configs in the response.

    By default, disabled configs are filtered out.
    """

    limit: int
    """Limit the number of items returned"""

    offset: int
    """Offset the items returned"""

    search_query: Optional[str]
