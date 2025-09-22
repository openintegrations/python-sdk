# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Integration"]


class Integration(BaseModel):
    id: str

    connector_name: Literal[
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

    created_at: str

    external: Union[str, float, bool, Dict[str, object], List[object], None] = None

    name: str

    standard: Union[str, float, bool, Dict[str, object], List[object], None] = None

    updated_at: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None
