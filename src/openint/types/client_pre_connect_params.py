# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ClientPreConnectParams",
    "DiscriminatedData",
    "DiscriminatedDataConnectorAcmeApikeyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBigqueryDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBoxDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDatabricksDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorJiraDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorJiraDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorLinearDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMondayDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorNotionDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOnedriveDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOutlookDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorResendDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSendgridDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSlackDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorYoutubeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorZoomDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorApolloDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPostgresDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSlackAgentDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorStripeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTwilioDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWorkatoDiscriminatedPreConnectInput",
    "Options",
]


class ClientPreConnectParams(TypedDict, total=False):
    connector_config_id: Required[str]
    """
    Must correspond to data.connector_name. Technically id should imply
    connector_name already but there is no way to specify a discriminated union with
    id alone.
    """

    discriminated_data: DiscriminatedData

    options: Options


class DiscriminatedDataConnectorAcmeApikeyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["acme-apikey"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["acme-oauth2"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["asana"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorBigqueryDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["bigquery"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorBoxDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["box"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["calendly"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    site_url: Required[str]
    """Your Atlassian site URL (e.g., https://your-domain.atlassian.net).

    You can find this in your browser when logged into Confluence.
    """


class DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["confluence"]]

    pre_connect_input: Required[DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDatabricksDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["databricks"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["discord"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["dropbox"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["figma"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["github"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-calendar"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-docs"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-drive"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-mail"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-sheet"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["hubspot"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["instagram"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorJiraDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    site_url: Required[str]
    """Your Atlassian site URL (e.g., https://your-domain.atlassian.net).

    You can find this in your browser when logged into Jira.
    """


class DiscriminatedDataConnectorJiraDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["jira"]]

    pre_connect_input: Required[DiscriminatedDataConnectorJiraDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorLinearDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["linear"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorMondayDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["monday"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorNotionDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["notion"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorOnedriveDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["onedrive"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorOutlookDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["outlook"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorResendDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["resend"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["salesforce"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSendgridDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["sendgrid"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["sharepoint"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["slack-deployed-agent"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSlackDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["slack"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["snowflake"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["spotify"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorYoutubeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["youtube"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    subdomain: Required[str]
    """Your Zendesk subdomain.

    This is the first part of your Zendesk URL. For example, if your Zendesk URL is
    https://acme.zendesk.com, then your subdomain is "acme".
    """


class DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zendesk"]]

    pre_connect_input: Required[DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorZoomDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zoom"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorApolloDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["apollo"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    language: Literal["en", "fr", "es", "nl", "de"]

    sandbox_public_token_create: Annotated[bool, PropertyInfo(alias="sandboxPublicTokenCreate")]


class DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["plaid"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPostgresDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["postgres"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSlackAgentDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["slack-agent"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["slack-agent-builder"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorStripeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["stripe"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    email: Required[str]
    """Email address of the user for sandbox prefill"""

    country: str
    """Country code for sandbox prefill"""


class DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["stripe-agent-sandbox"]]

    pre_connect_input: Required[DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTwilioDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["twilio"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorWorkatoDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["workato"]]

    pre_connect_input: Required[object]


DiscriminatedData: TypeAlias = Union[
    DiscriminatedDataConnectorAcmeApikeyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBigqueryDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBoxDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDatabricksDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorJiraDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorLinearDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMondayDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorNotionDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOnedriveDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOutlookDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorResendDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSendgridDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSlackDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorYoutubeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZoomDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorApolloDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPostgresDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSlackAgentDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorStripeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTwilioDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWorkatoDiscriminatedPreConnectInput,
]


class Options(TypedDict, total=False):
    connection_external_id: Annotated[Union[str, float, None], PropertyInfo(alias="connectionExternalId")]

    integration_external_id: Annotated[Union[str, float, None], PropertyInfo(alias="integrationExternalId")]
