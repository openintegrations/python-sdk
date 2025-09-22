# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ClientPostConnectParams",
    "DiscriminatedData",
    "DiscriminatedDataConnectorAcmeApikeyDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorAcmeApikeyDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorAcmeOauth2DiscriminatedConnectOutput",
    "DiscriminatedDataConnectorAcmeOauth2DiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorAsanaDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorAsanaDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorBigqueryDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorBigqueryDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorBoxDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorBoxDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorCalendlyDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorCalendlyDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorConfluenceDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorConfluenceDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorDatabricksDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorDatabricksDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorDiscordDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorDiscordDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorDropboxDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorDropboxDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorFigmaDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorFigmaDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorGitHubDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorGitHubDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorGoogleCalendarDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorGoogleCalendarDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorGoogleDocsDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorGoogleDocsDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorGoogleDriveDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorGoogleDriveDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorGoogleMailDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorGoogleMailDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorGoogleSheetDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorGoogleSheetDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorHubspotDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorHubspotDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorInstagramDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorInstagramDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorJiraDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorJiraDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorLinearDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorLinearDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorMondayDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorMondayDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorNotionDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorNotionDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorOnedriveDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorOnedriveDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorOutlookDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorOutlookDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorResendDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorResendDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSalesforceDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSalesforceDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSendgridDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSendgridDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSharepointDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSharepointDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSlackDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSlackDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSnowflakeDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSnowflakeDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSpotifyDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSpotifyDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorYoutubeDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorYoutubeDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorZendeskDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorZendeskDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorZoomDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorZoomDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorApolloDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorApolloDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorPlaidDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorPlaidDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorPostgresDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorPostgresDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSlackAgentDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSlackAgentDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorStripeDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorStripeDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorTwilioDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorTwilioDiscriminatedConnectOutputConnectOutput",
    "DiscriminatedDataConnectorWorkatoDiscriminatedConnectOutput",
    "DiscriminatedDataConnectorWorkatoDiscriminatedConnectOutputConnectOutput",
    "Options",
]


class ClientPostConnectParams(TypedDict, total=False):
    connector_config_id: Required[str]
    """
    Must correspond to data.connector_name. Technically id should imply
    connector_name already but there is no way to specify a discriminated union with
    id alone.
    """

    discriminated_data: Required[DiscriminatedData]

    options: Required[Options]


class DiscriminatedDataConnectorAcmeApikeyDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    api_key: Required[str]


class DiscriminatedDataConnectorAcmeApikeyDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorAcmeApikeyDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["acme-apikey"]]


class DiscriminatedDataConnectorAcmeOauth2DiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorAcmeOauth2DiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorAcmeOauth2DiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["acme-oauth2"]]


class DiscriminatedDataConnectorAsanaDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorAsanaDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorAsanaDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["asana"]]


class DiscriminatedDataConnectorBigqueryDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorBigqueryDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorBigqueryDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["bigquery"]]


class DiscriminatedDataConnectorBoxDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorBoxDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorBoxDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["box"]]


class DiscriminatedDataConnectorCalendlyDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorCalendlyDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorCalendlyDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["calendly"]]


class DiscriminatedDataConnectorConfluenceDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorConfluenceDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorConfluenceDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["confluence"]]


class DiscriminatedDataConnectorDatabricksDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorDatabricksDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorDatabricksDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["databricks"]]


class DiscriminatedDataConnectorDiscordDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorDiscordDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorDiscordDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["discord"]]


class DiscriminatedDataConnectorDropboxDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorDropboxDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorDropboxDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["dropbox"]]


class DiscriminatedDataConnectorFigmaDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorFigmaDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorFigmaDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["figma"]]


class DiscriminatedDataConnectorGitHubDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorGitHubDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorGitHubDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["github"]]


class DiscriminatedDataConnectorGoogleCalendarDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorGoogleCalendarDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorGoogleCalendarDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["google-calendar"]]


class DiscriminatedDataConnectorGoogleDocsDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorGoogleDocsDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorGoogleDocsDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["google-docs"]]


class DiscriminatedDataConnectorGoogleDriveDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorGoogleDriveDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorGoogleDriveDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["google-drive"]]


class DiscriminatedDataConnectorGoogleMailDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorGoogleMailDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorGoogleMailDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["google-mail"]]


class DiscriminatedDataConnectorGoogleSheetDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorGoogleSheetDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorGoogleSheetDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["google-sheet"]]


class DiscriminatedDataConnectorHubspotDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorHubspotDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorHubspotDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["hubspot"]]


class DiscriminatedDataConnectorInstagramDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorInstagramDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorInstagramDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["instagram"]]


class DiscriminatedDataConnectorJiraDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorJiraDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorJiraDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["jira"]]


class DiscriminatedDataConnectorLinearDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorLinearDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorLinearDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["linear"]]


class DiscriminatedDataConnectorMondayDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorMondayDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorMondayDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["monday"]]


class DiscriminatedDataConnectorNotionDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorNotionDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorNotionDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["notion"]]


class DiscriminatedDataConnectorOnedriveDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorOnedriveDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorOnedriveDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["onedrive"]]


class DiscriminatedDataConnectorOutlookDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorOutlookDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorOutlookDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["outlook"]]


class DiscriminatedDataConnectorResendDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    api_key: Required[str]


class DiscriminatedDataConnectorResendDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorResendDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["resend"]]


class DiscriminatedDataConnectorSalesforceDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorSalesforceDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSalesforceDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["salesforce"]]


class DiscriminatedDataConnectorSendgridDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    api_key: Required[str]


class DiscriminatedDataConnectorSendgridDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSendgridDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["sendgrid"]]


class DiscriminatedDataConnectorSharepointDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorSharepointDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSharepointDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["sharepoint"]]


class DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["slack-deployed-agent"]]


class DiscriminatedDataConnectorSlackDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorSlackDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSlackDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["slack"]]


class DiscriminatedDataConnectorSnowflakeDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorSnowflakeDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSnowflakeDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["snowflake"]]


class DiscriminatedDataConnectorSpotifyDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorSpotifyDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSpotifyDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["spotify"]]


class DiscriminatedDataConnectorYoutubeDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorYoutubeDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorYoutubeDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["youtube"]]


class DiscriminatedDataConnectorZendeskDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorZendeskDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorZendeskDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["zendesk"]]


class DiscriminatedDataConnectorZoomDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorZoomDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorZoomDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["zoom"]]


class DiscriminatedDataConnectorApolloDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    api_key: Required[str]


class DiscriminatedDataConnectorApolloDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorApolloDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["apollo"]]


class DiscriminatedDataConnectorPlaidDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    public_token: Required[str]

    meta: object


class DiscriminatedDataConnectorPlaidDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorPlaidDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["plaid"]]


class DiscriminatedDataConnectorPostgresDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    database_url: str


class DiscriminatedDataConnectorPostgresDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorPostgresDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["postgres"]]


class DiscriminatedDataConnectorSlackAgentDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    access_token: Required[str]
    """Bot OAuth token - xoxb-..."""


class DiscriminatedDataConnectorSlackAgentDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSlackAgentDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["slack-agent"]]


class DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    code: Required[str]
    """OAuth2 authorization code used for token exchange"""

    state: Required[str]
    """OAuth2 state"""

    client_id: str
    """Custom client ID to use for token exchange"""

    client_secret: str
    """Custom client secret to use for token exchange"""

    code_verifier: str
    """Code verifier for PKCE from the connect input"""


class DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["slack-agent-builder"]]


class DiscriminatedDataConnectorStripeDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    mcp: Required[str]
    """MCP access token"""

    publishable: Required[str]
    """Stripe publishable key for production"""

    secret: Required[str]
    """Stripe secret key for production"""


class DiscriminatedDataConnectorStripeDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorStripeDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["stripe"]]


class DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    claim_url: Required[str]
    """URL to claim/access the Stripe sandbox"""

    mcp: Required[str]
    """MCP access token"""

    publishable: Required[str]
    """Stripe publishable key for the sandbox"""

    secret: Required[str]
    """Stripe secret key for the sandbox"""


class DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["stripe-agent-sandbox"]]


class DiscriminatedDataConnectorTwilioDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    account_sid: Required[str]

    api_key: Required[str]

    api_key_secret: Required[str]


class DiscriminatedDataConnectorTwilioDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorTwilioDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["twilio"]]


class DiscriminatedDataConnectorWorkatoDiscriminatedConnectOutputConnectOutput(TypedDict, total=False):
    workato_api_host: Required[str]

    workato_api_token: Required[str]

    workato_account_id: str


class DiscriminatedDataConnectorWorkatoDiscriminatedConnectOutput(TypedDict, total=False):
    connect_output: Required[DiscriminatedDataConnectorWorkatoDiscriminatedConnectOutputConnectOutput]

    connector_name: Required[Literal["workato"]]


DiscriminatedData: TypeAlias = Union[
    DiscriminatedDataConnectorAcmeApikeyDiscriminatedConnectOutput,
    DiscriminatedDataConnectorAcmeOauth2DiscriminatedConnectOutput,
    DiscriminatedDataConnectorAsanaDiscriminatedConnectOutput,
    DiscriminatedDataConnectorBigqueryDiscriminatedConnectOutput,
    DiscriminatedDataConnectorBoxDiscriminatedConnectOutput,
    DiscriminatedDataConnectorCalendlyDiscriminatedConnectOutput,
    DiscriminatedDataConnectorConfluenceDiscriminatedConnectOutput,
    DiscriminatedDataConnectorDatabricksDiscriminatedConnectOutput,
    DiscriminatedDataConnectorDiscordDiscriminatedConnectOutput,
    DiscriminatedDataConnectorDropboxDiscriminatedConnectOutput,
    DiscriminatedDataConnectorFigmaDiscriminatedConnectOutput,
    DiscriminatedDataConnectorGitHubDiscriminatedConnectOutput,
    DiscriminatedDataConnectorGoogleCalendarDiscriminatedConnectOutput,
    DiscriminatedDataConnectorGoogleDocsDiscriminatedConnectOutput,
    DiscriminatedDataConnectorGoogleDriveDiscriminatedConnectOutput,
    DiscriminatedDataConnectorGoogleMailDiscriminatedConnectOutput,
    DiscriminatedDataConnectorGoogleSheetDiscriminatedConnectOutput,
    DiscriminatedDataConnectorHubspotDiscriminatedConnectOutput,
    DiscriminatedDataConnectorInstagramDiscriminatedConnectOutput,
    DiscriminatedDataConnectorJiraDiscriminatedConnectOutput,
    DiscriminatedDataConnectorLinearDiscriminatedConnectOutput,
    DiscriminatedDataConnectorMondayDiscriminatedConnectOutput,
    DiscriminatedDataConnectorNotionDiscriminatedConnectOutput,
    DiscriminatedDataConnectorOnedriveDiscriminatedConnectOutput,
    DiscriminatedDataConnectorOutlookDiscriminatedConnectOutput,
    DiscriminatedDataConnectorResendDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSalesforceDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSendgridDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSharepointDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSlackDeployedAgentDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSlackDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSnowflakeDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSpotifyDiscriminatedConnectOutput,
    DiscriminatedDataConnectorYoutubeDiscriminatedConnectOutput,
    DiscriminatedDataConnectorZendeskDiscriminatedConnectOutput,
    DiscriminatedDataConnectorZoomDiscriminatedConnectOutput,
    DiscriminatedDataConnectorApolloDiscriminatedConnectOutput,
    DiscriminatedDataConnectorPlaidDiscriminatedConnectOutput,
    DiscriminatedDataConnectorPostgresDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSlackAgentDiscriminatedConnectOutput,
    DiscriminatedDataConnectorSlackAgentBuilderDiscriminatedConnectOutput,
    DiscriminatedDataConnectorStripeDiscriminatedConnectOutput,
    DiscriminatedDataConnectorStripeAgentSandboxDiscriminatedConnectOutput,
    DiscriminatedDataConnectorTwilioDiscriminatedConnectOutput,
    DiscriminatedDataConnectorWorkatoDiscriminatedConnectOutput,
]


class Options(TypedDict, total=False):
    connection_external_id: Annotated[Union[str, float, None], PropertyInfo(alias="connectionExternalId")]

    integration_external_id: Annotated[Union[str, float, None], PropertyInfo(alias="integrationExternalId")]

    integration_id: Annotated[Optional[str], PropertyInfo(alias="integrationId")]
    """Must start with 'int\\__'"""

    sync_in_band: Annotated[Optional[bool], PropertyInfo(alias="syncInBand")]
