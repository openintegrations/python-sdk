# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PostConnectResponse",
    "ConnectorAcmeApikeyDiscriminatedConnectionSettings",
    "ConnectorAcmeApikeyDiscriminatedConnectionSettingsSettings",
    "ConnectorAcmeOauth2DiscriminatedConnectionSettings",
    "ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettings",
    "ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorAsanaDiscriminatedConnectionSettings",
    "ConnectorAsanaDiscriminatedConnectionSettingsSettings",
    "ConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorBigqueryDiscriminatedConnectionSettings",
    "ConnectorBigqueryDiscriminatedConnectionSettingsSettings",
    "ConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorBoxDiscriminatedConnectionSettings",
    "ConnectorBoxDiscriminatedConnectionSettingsSettings",
    "ConnectorBoxDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorBoxDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorCalendlyDiscriminatedConnectionSettings",
    "ConnectorCalendlyDiscriminatedConnectionSettingsSettings",
    "ConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorConfluenceDiscriminatedConnectionSettings",
    "ConnectorConfluenceDiscriminatedConnectionSettingsSettings",
    "ConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorDatabricksDiscriminatedConnectionSettings",
    "ConnectorDatabricksDiscriminatedConnectionSettingsSettings",
    "ConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorDiscordDiscriminatedConnectionSettings",
    "ConnectorDiscordDiscriminatedConnectionSettingsSettings",
    "ConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorDropboxDiscriminatedConnectionSettings",
    "ConnectorDropboxDiscriminatedConnectionSettingsSettings",
    "ConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorFigmaDiscriminatedConnectionSettings",
    "ConnectorFigmaDiscriminatedConnectionSettingsSettings",
    "ConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorGitHubDiscriminatedConnectionSettings",
    "ConnectorGitHubDiscriminatedConnectionSettingsSettings",
    "ConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorGoogleCalendarDiscriminatedConnectionSettings",
    "ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettings",
    "ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorGoogleDocsDiscriminatedConnectionSettings",
    "ConnectorGoogleDocsDiscriminatedConnectionSettingsSettings",
    "ConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorGoogleDriveDiscriminatedConnectionSettings",
    "ConnectorGoogleDriveDiscriminatedConnectionSettingsSettings",
    "ConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorGoogleMailDiscriminatedConnectionSettings",
    "ConnectorGoogleMailDiscriminatedConnectionSettingsSettings",
    "ConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorGoogleSheetDiscriminatedConnectionSettings",
    "ConnectorGoogleSheetDiscriminatedConnectionSettingsSettings",
    "ConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorHubspotDiscriminatedConnectionSettings",
    "ConnectorHubspotDiscriminatedConnectionSettingsSettings",
    "ConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorInstagramDiscriminatedConnectionSettings",
    "ConnectorInstagramDiscriminatedConnectionSettingsSettings",
    "ConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorJiraDiscriminatedConnectionSettings",
    "ConnectorJiraDiscriminatedConnectionSettingsSettings",
    "ConnectorJiraDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorJiraDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorLinearDiscriminatedConnectionSettings",
    "ConnectorLinearDiscriminatedConnectionSettingsSettings",
    "ConnectorLinearDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorLinearDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorMondayDiscriminatedConnectionSettings",
    "ConnectorMondayDiscriminatedConnectionSettingsSettings",
    "ConnectorMondayDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorMondayDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorNotionDiscriminatedConnectionSettings",
    "ConnectorNotionDiscriminatedConnectionSettingsSettings",
    "ConnectorNotionDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorNotionDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorOnedriveDiscriminatedConnectionSettings",
    "ConnectorOnedriveDiscriminatedConnectionSettingsSettings",
    "ConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorOutlookDiscriminatedConnectionSettings",
    "ConnectorOutlookDiscriminatedConnectionSettingsSettings",
    "ConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorResendDiscriminatedConnectionSettings",
    "ConnectorResendDiscriminatedConnectionSettingsSettings",
    "ConnectorSalesforceDiscriminatedConnectionSettings",
    "ConnectorSalesforceDiscriminatedConnectionSettingsSettings",
    "ConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorSendgridDiscriminatedConnectionSettings",
    "ConnectorSendgridDiscriminatedConnectionSettingsSettings",
    "ConnectorSharepointDiscriminatedConnectionSettings",
    "ConnectorSharepointDiscriminatedConnectionSettingsSettings",
    "ConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorSlackDeployedAgentDiscriminatedConnectionSettings",
    "ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettings",
    "ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorSlackDiscriminatedConnectionSettings",
    "ConnectorSlackDiscriminatedConnectionSettingsSettings",
    "ConnectorSlackDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorSlackDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorSnowflakeDiscriminatedConnectionSettings",
    "ConnectorSnowflakeDiscriminatedConnectionSettingsSettings",
    "ConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorSpotifyDiscriminatedConnectionSettings",
    "ConnectorSpotifyDiscriminatedConnectionSettingsSettings",
    "ConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorYoutubeDiscriminatedConnectionSettings",
    "ConnectorYoutubeDiscriminatedConnectionSettingsSettings",
    "ConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorZendeskDiscriminatedConnectionSettings",
    "ConnectorZendeskDiscriminatedConnectionSettingsSettings",
    "ConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorZoomDiscriminatedConnectionSettings",
    "ConnectorZoomDiscriminatedConnectionSettingsSettings",
    "ConnectorZoomDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorZoomDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorApolloDiscriminatedConnectionSettings",
    "ConnectorApolloDiscriminatedConnectionSettingsSettings",
    "ConnectorPlaidDiscriminatedConnectionSettings",
    "ConnectorPlaidDiscriminatedConnectionSettingsSettings",
    "ConnectorPostgresDiscriminatedConnectionSettings",
    "ConnectorPostgresDiscriminatedConnectionSettingsSettings",
    "ConnectorSlackAgentDiscriminatedConnectionSettings",
    "ConnectorSlackAgentDiscriminatedConnectionSettingsSettings",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettings",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettings",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuth",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilder",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuth",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuthCredentials",
    "ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderApp",
    "ConnectorStripeDiscriminatedConnectionSettings",
    "ConnectorStripeDiscriminatedConnectionSettingsSettings",
    "ConnectorStripeAgentSandboxDiscriminatedConnectionSettings",
    "ConnectorStripeAgentSandboxDiscriminatedConnectionSettingsSettings",
    "ConnectorTwilioDiscriminatedConnectionSettings",
    "ConnectorTwilioDiscriminatedConnectionSettingsSettings",
    "ConnectorWorkatoDiscriminatedConnectionSettings",
    "ConnectorWorkatoDiscriminatedConnectionSettingsSettings",
]


class ConnectorAcmeApikeyDiscriminatedConnectionSettingsSettings(BaseModel):
    api_key: str


class ConnectorAcmeApikeyDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["acme-apikey"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorAcmeApikeyDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorAcmeOauth2DiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["acme-oauth2"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorAcmeOauth2DiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorAsanaDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorAsanaDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["asana"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorAsanaDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorBigqueryDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorBigqueryDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["bigquery"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorBigqueryDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorBoxDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorBoxDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorBoxDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorBoxDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorBoxDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorBoxDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["box"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorBoxDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorCalendlyDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorCalendlyDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["calendly"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorCalendlyDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorConfluenceDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorConfluenceDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["confluence"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorConfluenceDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorDatabricksDiscriminatedConnectionSettingsSettings(BaseModel):
    databricks_instance: str
    """
    The Databricks workspace instance name (e.g., "your-workspace" for
    your-workspace.cloud.databricks.com)
    """

    oauth: ConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorDatabricksDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["databricks"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorDatabricksDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorDiscordDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorDiscordDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["discord"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorDiscordDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorDropboxDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorDropboxDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["dropbox"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorDropboxDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorFigmaDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorFigmaDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["figma"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorFigmaDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorGitHubDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorGitHubDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["github"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorGitHubDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorGoogleCalendarDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["google-calendar"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorGoogleCalendarDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorGoogleDocsDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorGoogleDocsDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["google-docs"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorGoogleDocsDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorGoogleDriveDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorGoogleDriveDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["google-drive"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorGoogleDriveDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorGoogleMailDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorGoogleMailDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["google-mail"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorGoogleMailDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorGoogleSheetDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorGoogleSheetDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["google-sheet"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorGoogleSheetDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorHubspotDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorHubspotDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["hubspot"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorHubspotDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorInstagramDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorInstagramDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["instagram"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorInstagramDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorJiraDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorJiraDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorJiraDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorJiraDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorJiraDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorJiraDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["jira"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorJiraDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorLinearDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorLinearDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorLinearDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorLinearDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorLinearDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorLinearDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["linear"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorLinearDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorMondayDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorMondayDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorMondayDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorMondayDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorMondayDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorMondayDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["monday"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorMondayDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorNotionDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorNotionDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorNotionDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorNotionDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorNotionDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorNotionDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["notion"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorNotionDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorOnedriveDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorOnedriveDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["onedrive"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorOnedriveDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorOutlookDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorOutlookDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["outlook"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorOutlookDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorResendDiscriminatedConnectionSettingsSettings(BaseModel):
    api_key: str


class ConnectorResendDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["resend"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorResendDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSalesforceDiscriminatedConnectionSettingsSettings(BaseModel):
    instance_url: str
    """The instance URL of your Salesforce account (e.g., example)"""

    oauth: ConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorSalesforceDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["salesforce"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSalesforceDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSendgridDiscriminatedConnectionSettingsSettings(BaseModel):
    api_key: str


class ConnectorSendgridDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["sendgrid"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSendgridDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSharepointDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorSharepointDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["sharepoint"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSharepointDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorSlackDeployedAgentDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["slack-deployed-agent"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSlackDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorSlackDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSlackDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorSlackDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorSlackDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["slack"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSlackDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSnowflakeDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuth

    snowflake_account_url: str
    """The domain of your Snowflake account (e.g., https://example-subdomain)"""

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorSnowflakeDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["snowflake"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSnowflakeDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSpotifyDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorSpotifyDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["spotify"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSpotifyDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorYoutubeDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorYoutubeDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["youtube"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorYoutubeDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorZendeskDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuth

    subdomain: str
    """The subdomain of your Zendesk account (e.g., https://domain.zendesk.com)"""

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorZendeskDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["zendesk"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorZendeskDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorZoomDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorZoomDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorZoomDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorZoomDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorZoomDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class ConnectorZoomDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["zoom"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorZoomDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorApolloDiscriminatedConnectionSettingsSettings(BaseModel):
    api_key: str


class ConnectorApolloDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["apollo"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorApolloDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorPlaidDiscriminatedConnectionSettingsSettings(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    institution: Optional[object] = None

    item: Optional[object] = None

    item_id: Optional[str] = FieldInfo(alias="itemId", default=None)

    status: Optional[object] = None

    webhook_item_error: None = FieldInfo(alias="webhookItemError", default=None)


class ConnectorPlaidDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["plaid"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorPlaidDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorPostgresDiscriminatedConnectionSettingsSettings(BaseModel):
    database_url: Optional[str] = None


class ConnectorPostgresDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["postgres"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorPostgresDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackAgentDiscriminatedConnectionSettingsSettings(BaseModel):
    access_token: str
    """Bot OAuth token - xoxb-..."""


class ConnectorSlackAgentDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["slack-agent"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSlackAgentDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuthCredentials(BaseModel):
    access_token: str

    client_id: Optional[str] = None
    """Client ID used for the connection"""

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    raw: Optional[Dict[str, object]] = None

    refresh_token: Optional[str] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuth(BaseModel):
    created_at: Optional[str] = None

    credentials: Optional[
        ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuthCredentials
    ] = None
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderApp(BaseModel):
    app_id: str
    """The Slack app ID"""

    client_id: str
    """The client ID for the app"""

    client_secret: str
    """The client secret for the app"""

    oauth_url: str
    """The OAuth authorization URL for the app"""

    signing_secret: str
    """The signing secret for the app"""

    verification_token: str
    """The verification token for the app"""


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilder(BaseModel):
    oauth: ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuth

    app: Optional[ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderApp] = None
    """Slack app configuration created by the agent builder"""


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettings(BaseModel):
    oauth: ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuth

    access_token: Optional[str] = None
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """

    agent_builder: Optional[ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilder] = None

    event_subscription_url: Optional[str] = None
    """URL for Slack event subscriptions"""


class ConnectorSlackAgentBuilderDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["slack-agent-builder"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorStripeDiscriminatedConnectionSettingsSettings(BaseModel):
    mcp: str
    """MCP access token"""

    publishable: str
    """Stripe publishable key for production"""

    secret: str
    """Stripe secret key for production"""


class ConnectorStripeDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["stripe"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorStripeDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorStripeAgentSandboxDiscriminatedConnectionSettingsSettings(BaseModel):
    claim_url: str
    """URL to claim/access the Stripe sandbox"""

    mcp: str
    """MCP access token"""

    publishable: str
    """Stripe publishable key for the sandbox"""

    secret: str
    """Stripe secret key for the sandbox"""


class ConnectorStripeAgentSandboxDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["stripe-agent-sandbox"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorStripeAgentSandboxDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorTwilioDiscriminatedConnectionSettingsSettings(BaseModel):
    account_sid: str

    api_key: str

    api_key_secret: str


class ConnectorTwilioDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["twilio"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorTwilioDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorWorkatoDiscriminatedConnectionSettingsSettings(BaseModel):
    workato_api_host: str

    workato_api_token: str

    workato_account_id: Optional[str] = None


class ConnectorWorkatoDiscriminatedConnectionSettings(BaseModel):
    connector_name: Literal["workato"]

    id: Optional[str] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    settings: Optional[ConnectorWorkatoDiscriminatedConnectionSettingsSettings] = None

    status: Optional[Literal["healthy", "disconnected", "error", "manual", "unknown"]] = None

    status_message: Optional[str] = None

    updated_at: Optional[str] = None


PostConnectResponse: TypeAlias = Union[
    ConnectorAcmeApikeyDiscriminatedConnectionSettings,
    ConnectorAcmeOauth2DiscriminatedConnectionSettings,
    ConnectorAsanaDiscriminatedConnectionSettings,
    ConnectorBigqueryDiscriminatedConnectionSettings,
    ConnectorBoxDiscriminatedConnectionSettings,
    ConnectorCalendlyDiscriminatedConnectionSettings,
    ConnectorConfluenceDiscriminatedConnectionSettings,
    ConnectorDatabricksDiscriminatedConnectionSettings,
    ConnectorDiscordDiscriminatedConnectionSettings,
    ConnectorDropboxDiscriminatedConnectionSettings,
    ConnectorFigmaDiscriminatedConnectionSettings,
    ConnectorGitHubDiscriminatedConnectionSettings,
    ConnectorGoogleCalendarDiscriminatedConnectionSettings,
    ConnectorGoogleDocsDiscriminatedConnectionSettings,
    ConnectorGoogleDriveDiscriminatedConnectionSettings,
    ConnectorGoogleMailDiscriminatedConnectionSettings,
    ConnectorGoogleSheetDiscriminatedConnectionSettings,
    ConnectorHubspotDiscriminatedConnectionSettings,
    ConnectorInstagramDiscriminatedConnectionSettings,
    ConnectorJiraDiscriminatedConnectionSettings,
    ConnectorLinearDiscriminatedConnectionSettings,
    ConnectorMondayDiscriminatedConnectionSettings,
    ConnectorNotionDiscriminatedConnectionSettings,
    ConnectorOnedriveDiscriminatedConnectionSettings,
    ConnectorOutlookDiscriminatedConnectionSettings,
    ConnectorResendDiscriminatedConnectionSettings,
    ConnectorSalesforceDiscriminatedConnectionSettings,
    ConnectorSendgridDiscriminatedConnectionSettings,
    ConnectorSharepointDiscriminatedConnectionSettings,
    ConnectorSlackDeployedAgentDiscriminatedConnectionSettings,
    ConnectorSlackDiscriminatedConnectionSettings,
    ConnectorSnowflakeDiscriminatedConnectionSettings,
    ConnectorSpotifyDiscriminatedConnectionSettings,
    ConnectorYoutubeDiscriminatedConnectionSettings,
    ConnectorZendeskDiscriminatedConnectionSettings,
    ConnectorZoomDiscriminatedConnectionSettings,
    ConnectorApolloDiscriminatedConnectionSettings,
    ConnectorPlaidDiscriminatedConnectionSettings,
    ConnectorPostgresDiscriminatedConnectionSettings,
    ConnectorSlackAgentDiscriminatedConnectionSettings,
    ConnectorSlackAgentBuilderDiscriminatedConnectionSettings,
    ConnectorStripeDiscriminatedConnectionSettings,
    ConnectorStripeAgentSandboxDiscriminatedConnectionSettings,
    ConnectorTwilioDiscriminatedConnectionSettings,
    ConnectorWorkatoDiscriminatedConnectionSettings,
]
