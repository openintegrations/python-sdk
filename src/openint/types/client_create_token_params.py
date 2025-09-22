# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ClientCreateTokenParams", "ConnectOptions"]


class ClientCreateTokenParams(TypedDict, total=False):
    connect_options: ConnectOptions

    validity_in_seconds: float
    """
    How long the publishable token and magic link url will be valid for (in seconds)
    before it expires. By default it will be valid for 30 days unless otherwise
    specified.
    """


class ConnectOptions(TypedDict, total=False):
    auto_connect: Literal[
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
    """
    Automatically trigger connection flow for the specified connector when the page
    loads. Only works when view is "add" and the connector is available.
    """

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
    """The names of the connectors to show in the connect page.

    If not provided, all connectors will be shown
    """

    debug: bool
    """Whether to enable debug mode"""

    hide_navigation: bool
    """Whether to hide the navigation bar.

    This is useful for hardcoding to a particular view.
    """

    is_embedded: bool
    """Whether to enable embedded mode.

    Embedded mode hides the side bar with extra context for the end user (customer)
    on the organization
    """

    return_url: str
    """
    Optional URL to return customers after adding a connection or if they press the
    Return To Organization button
    """

    theme: Literal["light", "dark"]
    """The theme to use for the connect page. Defaults to light if not specified."""

    view: Literal["add", "manage"]
    """The default view to show when the magic link is opened.

    If omitted, by default it will smartly load the right view based on whether the
    user has connections or not
    """
