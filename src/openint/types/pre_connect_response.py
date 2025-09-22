# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "PreConnectResponse",
    "ConnectorAcmeApikeyDiscriminatedConnectInput",
    "ConnectorAcmeOauth2DiscriminatedConnectInput",
    "ConnectorAcmeOauth2DiscriminatedConnectInputConnectInput",
    "ConnectorAsanaDiscriminatedConnectInput",
    "ConnectorAsanaDiscriminatedConnectInputConnectInput",
    "ConnectorBigqueryDiscriminatedConnectInput",
    "ConnectorBigqueryDiscriminatedConnectInputConnectInput",
    "ConnectorBoxDiscriminatedConnectInput",
    "ConnectorBoxDiscriminatedConnectInputConnectInput",
    "ConnectorCalendlyDiscriminatedConnectInput",
    "ConnectorCalendlyDiscriminatedConnectInputConnectInput",
    "ConnectorConfluenceDiscriminatedConnectInput",
    "ConnectorConfluenceDiscriminatedConnectInputConnectInput",
    "ConnectorDatabricksDiscriminatedConnectInput",
    "ConnectorDatabricksDiscriminatedConnectInputConnectInput",
    "ConnectorDiscordDiscriminatedConnectInput",
    "ConnectorDiscordDiscriminatedConnectInputConnectInput",
    "ConnectorDropboxDiscriminatedConnectInput",
    "ConnectorDropboxDiscriminatedConnectInputConnectInput",
    "ConnectorFigmaDiscriminatedConnectInput",
    "ConnectorFigmaDiscriminatedConnectInputConnectInput",
    "ConnectorGitHubDiscriminatedConnectInput",
    "ConnectorGitHubDiscriminatedConnectInputConnectInput",
    "ConnectorGoogleCalendarDiscriminatedConnectInput",
    "ConnectorGoogleCalendarDiscriminatedConnectInputConnectInput",
    "ConnectorGoogleDocsDiscriminatedConnectInput",
    "ConnectorGoogleDocsDiscriminatedConnectInputConnectInput",
    "ConnectorGoogleDriveDiscriminatedConnectInput",
    "ConnectorGoogleDriveDiscriminatedConnectInputConnectInput",
    "ConnectorGoogleMailDiscriminatedConnectInput",
    "ConnectorGoogleMailDiscriminatedConnectInputConnectInput",
    "ConnectorGoogleSheetDiscriminatedConnectInput",
    "ConnectorGoogleSheetDiscriminatedConnectInputConnectInput",
    "ConnectorHubspotDiscriminatedConnectInput",
    "ConnectorHubspotDiscriminatedConnectInputConnectInput",
    "ConnectorInstagramDiscriminatedConnectInput",
    "ConnectorInstagramDiscriminatedConnectInputConnectInput",
    "ConnectorJiraDiscriminatedConnectInput",
    "ConnectorJiraDiscriminatedConnectInputConnectInput",
    "ConnectorLinearDiscriminatedConnectInput",
    "ConnectorLinearDiscriminatedConnectInputConnectInput",
    "ConnectorMondayDiscriminatedConnectInput",
    "ConnectorMondayDiscriminatedConnectInputConnectInput",
    "ConnectorNotionDiscriminatedConnectInput",
    "ConnectorNotionDiscriminatedConnectInputConnectInput",
    "ConnectorOnedriveDiscriminatedConnectInput",
    "ConnectorOnedriveDiscriminatedConnectInputConnectInput",
    "ConnectorOutlookDiscriminatedConnectInput",
    "ConnectorOutlookDiscriminatedConnectInputConnectInput",
    "ConnectorResendDiscriminatedConnectInput",
    "ConnectorSalesforceDiscriminatedConnectInput",
    "ConnectorSalesforceDiscriminatedConnectInputConnectInput",
    "ConnectorSendgridDiscriminatedConnectInput",
    "ConnectorSharepointDiscriminatedConnectInput",
    "ConnectorSharepointDiscriminatedConnectInputConnectInput",
    "ConnectorSlackDeployedAgentDiscriminatedConnectInput",
    "ConnectorSlackDeployedAgentDiscriminatedConnectInputConnectInput",
    "ConnectorSlackDiscriminatedConnectInput",
    "ConnectorSlackDiscriminatedConnectInputConnectInput",
    "ConnectorSnowflakeDiscriminatedConnectInput",
    "ConnectorSnowflakeDiscriminatedConnectInputConnectInput",
    "ConnectorSpotifyDiscriminatedConnectInput",
    "ConnectorSpotifyDiscriminatedConnectInputConnectInput",
    "ConnectorYoutubeDiscriminatedConnectInput",
    "ConnectorYoutubeDiscriminatedConnectInputConnectInput",
    "ConnectorZendeskDiscriminatedConnectInput",
    "ConnectorZendeskDiscriminatedConnectInputConnectInput",
    "ConnectorZoomDiscriminatedConnectInput",
    "ConnectorZoomDiscriminatedConnectInputConnectInput",
    "ConnectorApolloDiscriminatedConnectInput",
    "ConnectorPlaidDiscriminatedConnectInput",
    "ConnectorPlaidDiscriminatedConnectInputConnectInput",
    "ConnectorPlaidDiscriminatedConnectInputConnectInputLinkToken",
    "ConnectorPlaidDiscriminatedConnectInputConnectInputPublicToken",
    "ConnectorPostgresDiscriminatedConnectInput",
    "ConnectorSlackAgentDiscriminatedConnectInput",
    "ConnectorSlackAgentDiscriminatedConnectInputConnectInput",
    "ConnectorSlackAgentBuilderDiscriminatedConnectInput",
    "ConnectorSlackAgentBuilderDiscriminatedConnectInputConnectInput",
    "ConnectorStripeDiscriminatedConnectInput",
    "ConnectorStripeDiscriminatedConnectInputConnectInput",
    "ConnectorStripeAgentSandboxDiscriminatedConnectInput",
    "ConnectorStripeAgentSandboxDiscriminatedConnectInputConnectInput",
    "ConnectorTwilioDiscriminatedConnectInput",
    "ConnectorWorkatoDiscriminatedConnectInput",
]


class ConnectorAcmeApikeyDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["acme-apikey"]


class ConnectorAcmeOauth2DiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAcmeOauth2DiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAcmeOauth2DiscriminatedConnectInputConnectInput

    connector_name: Literal["acme-oauth2"]


class ConnectorAsanaDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAsanaDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAsanaDiscriminatedConnectInputConnectInput

    connector_name: Literal["asana"]


class ConnectorBigqueryDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBigqueryDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBigqueryDiscriminatedConnectInputConnectInput

    connector_name: Literal["bigquery"]


class ConnectorBoxDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBoxDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBoxDiscriminatedConnectInputConnectInput

    connector_name: Literal["box"]


class ConnectorCalendlyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorCalendlyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorCalendlyDiscriminatedConnectInputConnectInput

    connector_name: Literal["calendly"]


class ConnectorConfluenceDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorConfluenceDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorConfluenceDiscriminatedConnectInputConnectInput

    connector_name: Literal["confluence"]


class ConnectorDatabricksDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDatabricksDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDatabricksDiscriminatedConnectInputConnectInput

    connector_name: Literal["databricks"]


class ConnectorDiscordDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDiscordDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDiscordDiscriminatedConnectInputConnectInput

    connector_name: Literal["discord"]


class ConnectorDropboxDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDropboxDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDropboxDiscriminatedConnectInputConnectInput

    connector_name: Literal["dropbox"]


class ConnectorFigmaDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFigmaDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFigmaDiscriminatedConnectInputConnectInput

    connector_name: Literal["figma"]


class ConnectorGitHubDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGitHubDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGitHubDiscriminatedConnectInputConnectInput

    connector_name: Literal["github"]


class ConnectorGoogleCalendarDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGoogleCalendarDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGoogleCalendarDiscriminatedConnectInputConnectInput

    connector_name: Literal["google-calendar"]


class ConnectorGoogleDocsDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGoogleDocsDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGoogleDocsDiscriminatedConnectInputConnectInput

    connector_name: Literal["google-docs"]


class ConnectorGoogleDriveDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGoogleDriveDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGoogleDriveDiscriminatedConnectInputConnectInput

    connector_name: Literal["google-drive"]


class ConnectorGoogleMailDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGoogleMailDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGoogleMailDiscriminatedConnectInputConnectInput

    connector_name: Literal["google-mail"]


class ConnectorGoogleSheetDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGoogleSheetDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGoogleSheetDiscriminatedConnectInputConnectInput

    connector_name: Literal["google-sheet"]


class ConnectorHubspotDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorHubspotDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorHubspotDiscriminatedConnectInputConnectInput

    connector_name: Literal["hubspot"]


class ConnectorInstagramDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorInstagramDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorInstagramDiscriminatedConnectInputConnectInput

    connector_name: Literal["instagram"]


class ConnectorJiraDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorJiraDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorJiraDiscriminatedConnectInputConnectInput

    connector_name: Literal["jira"]


class ConnectorLinearDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorLinearDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorLinearDiscriminatedConnectInputConnectInput

    connector_name: Literal["linear"]


class ConnectorMondayDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorMondayDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorMondayDiscriminatedConnectInputConnectInput

    connector_name: Literal["monday"]


class ConnectorNotionDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorNotionDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorNotionDiscriminatedConnectInputConnectInput

    connector_name: Literal["notion"]


class ConnectorOnedriveDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorOnedriveDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOnedriveDiscriminatedConnectInputConnectInput

    connector_name: Literal["onedrive"]


class ConnectorOutlookDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorOutlookDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOutlookDiscriminatedConnectInputConnectInput

    connector_name: Literal["outlook"]


class ConnectorResendDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["resend"]


class ConnectorSalesforceDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSalesforceDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSalesforceDiscriminatedConnectInputConnectInput

    connector_name: Literal["salesforce"]


class ConnectorSendgridDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["sendgrid"]


class ConnectorSharepointDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSharepointDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSharepointDiscriminatedConnectInputConnectInput

    connector_name: Literal["sharepoint"]


class ConnectorSlackDeployedAgentDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSlackDeployedAgentDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSlackDeployedAgentDiscriminatedConnectInputConnectInput

    connector_name: Literal["slack-deployed-agent"]


class ConnectorSlackDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSlackDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSlackDiscriminatedConnectInputConnectInput

    connector_name: Literal["slack"]


class ConnectorSnowflakeDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSnowflakeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSnowflakeDiscriminatedConnectInputConnectInput

    connector_name: Literal["snowflake"]


class ConnectorSpotifyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSpotifyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSpotifyDiscriminatedConnectInputConnectInput

    connector_name: Literal["spotify"]


class ConnectorYoutubeDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorYoutubeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorYoutubeDiscriminatedConnectInputConnectInput

    connector_name: Literal["youtube"]


class ConnectorZendeskDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZendeskDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZendeskDiscriminatedConnectInputConnectInput

    connector_name: Literal["zendesk"]


class ConnectorZoomDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZoomDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZoomDiscriminatedConnectInputConnectInput

    connector_name: Literal["zoom"]


class ConnectorApolloDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["apollo"]


class ConnectorPlaidDiscriminatedConnectInputConnectInputLinkToken(BaseModel):
    link_token: str


class ConnectorPlaidDiscriminatedConnectInputConnectInputPublicToken(BaseModel):
    public_token: str


ConnectorPlaidDiscriminatedConnectInputConnectInput: TypeAlias = Union[
    ConnectorPlaidDiscriminatedConnectInputConnectInputLinkToken,
    ConnectorPlaidDiscriminatedConnectInputConnectInputPublicToken,
]


class ConnectorPlaidDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPlaidDiscriminatedConnectInputConnectInput

    connector_name: Literal["plaid"]


class ConnectorPostgresDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["postgres"]


class ConnectorSlackAgentDiscriminatedConnectInputConnectInput(BaseModel):
    configuration_url: str
    """Configuration URL - https://api.slack.com/apps/A1234567890/oauth..."""


class ConnectorSlackAgentDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSlackAgentDiscriminatedConnectInputConnectInput

    connector_name: Literal["slack-agent"]


class ConnectorSlackAgentBuilderDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSlackAgentBuilderDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSlackAgentBuilderDiscriminatedConnectInputConnectInput

    connector_name: Literal["slack-agent-builder"]


class ConnectorStripeDiscriminatedConnectInputConnectInput(BaseModel):
    mcp: str
    """MCP access token"""

    publishable: str
    """Stripe publishable key for the sandbox"""

    secret: str
    """Stripe secret key for the sandbox"""


class ConnectorStripeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorStripeDiscriminatedConnectInputConnectInput

    connector_name: Literal["stripe"]


class ConnectorStripeAgentSandboxDiscriminatedConnectInputConnectInput(BaseModel):
    mcp: str
    """MCP access token"""

    publishable: str
    """Stripe publishable key for the sandbox"""

    secret: str
    """Stripe secret key for the sandbox"""

    claim_url: Optional[str] = None
    """URL to claim/access the Stripe sandbox"""


class ConnectorStripeAgentSandboxDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorStripeAgentSandboxDiscriminatedConnectInputConnectInput

    connector_name: Literal["stripe-agent-sandbox"]


class ConnectorTwilioDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["twilio"]


class ConnectorWorkatoDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["workato"]


PreConnectResponse: TypeAlias = Annotated[
    Union[
        ConnectorAcmeApikeyDiscriminatedConnectInput,
        ConnectorAcmeOauth2DiscriminatedConnectInput,
        ConnectorAsanaDiscriminatedConnectInput,
        ConnectorBigqueryDiscriminatedConnectInput,
        ConnectorBoxDiscriminatedConnectInput,
        ConnectorCalendlyDiscriminatedConnectInput,
        ConnectorConfluenceDiscriminatedConnectInput,
        ConnectorDatabricksDiscriminatedConnectInput,
        ConnectorDiscordDiscriminatedConnectInput,
        ConnectorDropboxDiscriminatedConnectInput,
        ConnectorFigmaDiscriminatedConnectInput,
        ConnectorGitHubDiscriminatedConnectInput,
        ConnectorGoogleCalendarDiscriminatedConnectInput,
        ConnectorGoogleDocsDiscriminatedConnectInput,
        ConnectorGoogleDriveDiscriminatedConnectInput,
        ConnectorGoogleMailDiscriminatedConnectInput,
        ConnectorGoogleSheetDiscriminatedConnectInput,
        ConnectorHubspotDiscriminatedConnectInput,
        ConnectorInstagramDiscriminatedConnectInput,
        ConnectorJiraDiscriminatedConnectInput,
        ConnectorLinearDiscriminatedConnectInput,
        ConnectorMondayDiscriminatedConnectInput,
        ConnectorNotionDiscriminatedConnectInput,
        ConnectorOnedriveDiscriminatedConnectInput,
        ConnectorOutlookDiscriminatedConnectInput,
        ConnectorResendDiscriminatedConnectInput,
        ConnectorSalesforceDiscriminatedConnectInput,
        ConnectorSendgridDiscriminatedConnectInput,
        ConnectorSharepointDiscriminatedConnectInput,
        ConnectorSlackDeployedAgentDiscriminatedConnectInput,
        ConnectorSlackDiscriminatedConnectInput,
        ConnectorSnowflakeDiscriminatedConnectInput,
        ConnectorSpotifyDiscriminatedConnectInput,
        ConnectorYoutubeDiscriminatedConnectInput,
        ConnectorZendeskDiscriminatedConnectInput,
        ConnectorZoomDiscriminatedConnectInput,
        ConnectorApolloDiscriminatedConnectInput,
        ConnectorPlaidDiscriminatedConnectInput,
        ConnectorPostgresDiscriminatedConnectInput,
        ConnectorSlackAgentDiscriminatedConnectInput,
        ConnectorSlackAgentBuilderDiscriminatedConnectInput,
        ConnectorStripeDiscriminatedConnectInput,
        ConnectorStripeAgentSandboxDiscriminatedConnectInput,
        ConnectorTwilioDiscriminatedConnectInput,
        ConnectorWorkatoDiscriminatedConnectInput,
    ],
    PropertyInfo(discriminator="connector_name"),
]
