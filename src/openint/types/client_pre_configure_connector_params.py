# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClientPreConfigureConnectorParams"]


class ClientPreConfigureConnectorParams(TypedDict, total=False):
    connector_name: Required[
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
