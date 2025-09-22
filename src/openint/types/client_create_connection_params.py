# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ClientCreateConnectionParams",
    "Data",
    "DataConnectorAcmeApikeyDiscriminatedConnectionSettings",
    "DataConnectorAcmeApikeyDiscriminatedConnectionSettingsSettings",
    "DataConnectorAcmeOauth2DiscriminatedConnectionSettings",
    "DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettings",
    "DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorAsanaDiscriminatedConnectionSettings",
    "DataConnectorAsanaDiscriminatedConnectionSettingsSettings",
    "DataConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorBigqueryDiscriminatedConnectionSettings",
    "DataConnectorBigqueryDiscriminatedConnectionSettingsSettings",
    "DataConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorBoxDiscriminatedConnectionSettings",
    "DataConnectorBoxDiscriminatedConnectionSettingsSettings",
    "DataConnectorBoxDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorBoxDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorCalendlyDiscriminatedConnectionSettings",
    "DataConnectorCalendlyDiscriminatedConnectionSettingsSettings",
    "DataConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorConfluenceDiscriminatedConnectionSettings",
    "DataConnectorConfluenceDiscriminatedConnectionSettingsSettings",
    "DataConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorDatabricksDiscriminatedConnectionSettings",
    "DataConnectorDatabricksDiscriminatedConnectionSettingsSettings",
    "DataConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorDiscordDiscriminatedConnectionSettings",
    "DataConnectorDiscordDiscriminatedConnectionSettingsSettings",
    "DataConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorDropboxDiscriminatedConnectionSettings",
    "DataConnectorDropboxDiscriminatedConnectionSettingsSettings",
    "DataConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorFigmaDiscriminatedConnectionSettings",
    "DataConnectorFigmaDiscriminatedConnectionSettingsSettings",
    "DataConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorGitHubDiscriminatedConnectionSettings",
    "DataConnectorGitHubDiscriminatedConnectionSettingsSettings",
    "DataConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorGoogleCalendarDiscriminatedConnectionSettings",
    "DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettings",
    "DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorGoogleDocsDiscriminatedConnectionSettings",
    "DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettings",
    "DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorGoogleDriveDiscriminatedConnectionSettings",
    "DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettings",
    "DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorGoogleMailDiscriminatedConnectionSettings",
    "DataConnectorGoogleMailDiscriminatedConnectionSettingsSettings",
    "DataConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorGoogleSheetDiscriminatedConnectionSettings",
    "DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettings",
    "DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorHubspotDiscriminatedConnectionSettings",
    "DataConnectorHubspotDiscriminatedConnectionSettingsSettings",
    "DataConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorInstagramDiscriminatedConnectionSettings",
    "DataConnectorInstagramDiscriminatedConnectionSettingsSettings",
    "DataConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorJiraDiscriminatedConnectionSettings",
    "DataConnectorJiraDiscriminatedConnectionSettingsSettings",
    "DataConnectorJiraDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorJiraDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorLinearDiscriminatedConnectionSettings",
    "DataConnectorLinearDiscriminatedConnectionSettingsSettings",
    "DataConnectorLinearDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorLinearDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorMondayDiscriminatedConnectionSettings",
    "DataConnectorMondayDiscriminatedConnectionSettingsSettings",
    "DataConnectorMondayDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorMondayDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorNotionDiscriminatedConnectionSettings",
    "DataConnectorNotionDiscriminatedConnectionSettingsSettings",
    "DataConnectorNotionDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorNotionDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorOnedriveDiscriminatedConnectionSettings",
    "DataConnectorOnedriveDiscriminatedConnectionSettingsSettings",
    "DataConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorOutlookDiscriminatedConnectionSettings",
    "DataConnectorOutlookDiscriminatedConnectionSettingsSettings",
    "DataConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorResendDiscriminatedConnectionSettings",
    "DataConnectorResendDiscriminatedConnectionSettingsSettings",
    "DataConnectorSalesforceDiscriminatedConnectionSettings",
    "DataConnectorSalesforceDiscriminatedConnectionSettingsSettings",
    "DataConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorSendgridDiscriminatedConnectionSettings",
    "DataConnectorSendgridDiscriminatedConnectionSettingsSettings",
    "DataConnectorSharepointDiscriminatedConnectionSettings",
    "DataConnectorSharepointDiscriminatedConnectionSettingsSettings",
    "DataConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorSlackDeployedAgentDiscriminatedConnectionSettings",
    "DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettings",
    "DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorSlackDiscriminatedConnectionSettings",
    "DataConnectorSlackDiscriminatedConnectionSettingsSettings",
    "DataConnectorSlackDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorSlackDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorSnowflakeDiscriminatedConnectionSettings",
    "DataConnectorSnowflakeDiscriminatedConnectionSettingsSettings",
    "DataConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorSpotifyDiscriminatedConnectionSettings",
    "DataConnectorSpotifyDiscriminatedConnectionSettingsSettings",
    "DataConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorYoutubeDiscriminatedConnectionSettings",
    "DataConnectorYoutubeDiscriminatedConnectionSettingsSettings",
    "DataConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorZendeskDiscriminatedConnectionSettings",
    "DataConnectorZendeskDiscriminatedConnectionSettingsSettings",
    "DataConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorZoomDiscriminatedConnectionSettings",
    "DataConnectorZoomDiscriminatedConnectionSettingsSettings",
    "DataConnectorZoomDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorZoomDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorApolloDiscriminatedConnectionSettings",
    "DataConnectorApolloDiscriminatedConnectionSettingsSettings",
    "DataConnectorPlaidDiscriminatedConnectionSettings",
    "DataConnectorPlaidDiscriminatedConnectionSettingsSettings",
    "DataConnectorPostgresDiscriminatedConnectionSettings",
    "DataConnectorPostgresDiscriminatedConnectionSettingsSettings",
    "DataConnectorSlackAgentDiscriminatedConnectionSettings",
    "DataConnectorSlackAgentDiscriminatedConnectionSettingsSettings",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettings",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettings",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuth",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilder",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuth",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuthCredentials",
    "DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderApp",
    "DataConnectorStripeDiscriminatedConnectionSettings",
    "DataConnectorStripeDiscriminatedConnectionSettingsSettings",
    "DataConnectorStripeAgentSandboxDiscriminatedConnectionSettings",
    "DataConnectorStripeAgentSandboxDiscriminatedConnectionSettingsSettings",
    "DataConnectorTwilioDiscriminatedConnectionSettings",
    "DataConnectorTwilioDiscriminatedConnectionSettingsSettings",
    "DataConnectorWorkatoDiscriminatedConnectionSettings",
    "DataConnectorWorkatoDiscriminatedConnectionSettingsSettings",
]


class ClientCreateConnectionParams(TypedDict, total=False):
    connector_config_id: Required[str]
    """The id of the connector config, starts with `ccfg_`"""

    data: Required[Data]
    """Connector specific data"""

    check_connection: bool
    """Perform a synchronous connection check before creating it."""

    customer_id: str
    """The id of the customer in your application.

    Ensure it is unique for that customer.
    """

    metadata: Dict[str, object]


class DataConnectorAcmeApikeyDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    api_key: Required[str]


class DataConnectorAcmeApikeyDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["acme-apikey"]]

    settings: DataConnectorAcmeApikeyDiscriminatedConnectionSettingsSettings


class DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorAcmeOauth2DiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["acme-oauth2"]]

    settings: DataConnectorAcmeOauth2DiscriminatedConnectionSettingsSettings


class DataConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorAsanaDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorAsanaDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorAsanaDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["asana"]]

    settings: DataConnectorAsanaDiscriminatedConnectionSettingsSettings


class DataConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorBigqueryDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorBigqueryDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorBigqueryDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["bigquery"]]

    settings: DataConnectorBigqueryDiscriminatedConnectionSettingsSettings


class DataConnectorBoxDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorBoxDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorBoxDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorBoxDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorBoxDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorBoxDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["box"]]

    settings: DataConnectorBoxDiscriminatedConnectionSettingsSettings


class DataConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorCalendlyDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorCalendlyDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorCalendlyDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["calendly"]]

    settings: DataConnectorCalendlyDiscriminatedConnectionSettingsSettings


class DataConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorConfluenceDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorConfluenceDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorConfluenceDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["confluence"]]

    settings: DataConnectorConfluenceDiscriminatedConnectionSettingsSettings


class DataConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorDatabricksDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    databricks_instance: Required[str]
    """
    The Databricks workspace instance name (e.g., "your-workspace" for
    your-workspace.cloud.databricks.com)
    """

    oauth: Required[DataConnectorDatabricksDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorDatabricksDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["databricks"]]

    settings: DataConnectorDatabricksDiscriminatedConnectionSettingsSettings


class DataConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorDiscordDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorDiscordDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorDiscordDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["discord"]]

    settings: DataConnectorDiscordDiscriminatedConnectionSettingsSettings


class DataConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorDropboxDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorDropboxDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorDropboxDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["dropbox"]]

    settings: DataConnectorDropboxDiscriminatedConnectionSettingsSettings


class DataConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorFigmaDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorFigmaDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorFigmaDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["figma"]]

    settings: DataConnectorFigmaDiscriminatedConnectionSettingsSettings


class DataConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorGitHubDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorGitHubDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorGitHubDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["github"]]

    settings: DataConnectorGitHubDiscriminatedConnectionSettingsSettings


class DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorGoogleCalendarDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["google-calendar"]]

    settings: DataConnectorGoogleCalendarDiscriminatedConnectionSettingsSettings


class DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorGoogleDocsDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["google-docs"]]

    settings: DataConnectorGoogleDocsDiscriminatedConnectionSettingsSettings


class DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorGoogleDriveDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["google-drive"]]

    settings: DataConnectorGoogleDriveDiscriminatedConnectionSettingsSettings


class DataConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorGoogleMailDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorGoogleMailDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorGoogleMailDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["google-mail"]]

    settings: DataConnectorGoogleMailDiscriminatedConnectionSettingsSettings


class DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorGoogleSheetDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["google-sheet"]]

    settings: DataConnectorGoogleSheetDiscriminatedConnectionSettingsSettings


class DataConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorHubspotDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorHubspotDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorHubspotDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["hubspot"]]

    settings: DataConnectorHubspotDiscriminatedConnectionSettingsSettings


class DataConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorInstagramDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorInstagramDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorInstagramDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["instagram"]]

    settings: DataConnectorInstagramDiscriminatedConnectionSettingsSettings


class DataConnectorJiraDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorJiraDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorJiraDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorJiraDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorJiraDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorJiraDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["jira"]]

    settings: DataConnectorJiraDiscriminatedConnectionSettingsSettings


class DataConnectorLinearDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorLinearDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorLinearDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorLinearDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorLinearDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorLinearDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["linear"]]

    settings: DataConnectorLinearDiscriminatedConnectionSettingsSettings


class DataConnectorMondayDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorMondayDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorMondayDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorMondayDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorMondayDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorMondayDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["monday"]]

    settings: DataConnectorMondayDiscriminatedConnectionSettingsSettings


class DataConnectorNotionDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorNotionDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorNotionDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorNotionDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorNotionDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorNotionDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["notion"]]

    settings: DataConnectorNotionDiscriminatedConnectionSettingsSettings


class DataConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorOnedriveDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorOnedriveDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorOnedriveDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["onedrive"]]

    settings: DataConnectorOnedriveDiscriminatedConnectionSettingsSettings


class DataConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorOutlookDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorOutlookDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorOutlookDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["outlook"]]

    settings: DataConnectorOutlookDiscriminatedConnectionSettingsSettings


class DataConnectorResendDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    api_key: Required[str]


class DataConnectorResendDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["resend"]]

    settings: DataConnectorResendDiscriminatedConnectionSettingsSettings


class DataConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSalesforceDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    instance_url: Required[str]
    """The instance URL of your Salesforce account (e.g., example)"""

    oauth: Required[DataConnectorSalesforceDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorSalesforceDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["salesforce"]]

    settings: DataConnectorSalesforceDiscriminatedConnectionSettingsSettings


class DataConnectorSendgridDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    api_key: Required[str]


class DataConnectorSendgridDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["sendgrid"]]

    settings: DataConnectorSendgridDiscriminatedConnectionSettingsSettings


class DataConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSharepointDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorSharepointDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorSharepointDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["sharepoint"]]

    settings: DataConnectorSharepointDiscriminatedConnectionSettingsSettings


class DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorSlackDeployedAgentDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["slack-deployed-agent"]]

    settings: DataConnectorSlackDeployedAgentDiscriminatedConnectionSettingsSettings


class DataConnectorSlackDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSlackDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSlackDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSlackDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorSlackDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorSlackDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["slack"]]

    settings: DataConnectorSlackDiscriminatedConnectionSettingsSettings


class DataConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSnowflakeDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorSnowflakeDiscriminatedConnectionSettingsSettingsOAuth]

    snowflake_account_url: Required[str]
    """The domain of your Snowflake account (e.g., https://example-subdomain)"""

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorSnowflakeDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["snowflake"]]

    settings: DataConnectorSnowflakeDiscriminatedConnectionSettingsSettings


class DataConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSpotifyDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorSpotifyDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorSpotifyDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["spotify"]]

    settings: DataConnectorSpotifyDiscriminatedConnectionSettingsSettings


class DataConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorYoutubeDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorYoutubeDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorYoutubeDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["youtube"]]

    settings: DataConnectorYoutubeDiscriminatedConnectionSettingsSettings


class DataConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorZendeskDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorZendeskDiscriminatedConnectionSettingsSettingsOAuth]

    subdomain: Required[str]
    """The subdomain of your Zendesk account (e.g., https://domain.zendesk.com)"""

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorZendeskDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["zendesk"]]

    settings: DataConnectorZendeskDiscriminatedConnectionSettingsSettings


class DataConnectorZoomDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorZoomDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorZoomDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorZoomDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorZoomDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """


class DataConnectorZoomDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["zoom"]]

    settings: DataConnectorZoomDiscriminatedConnectionSettingsSettings


class DataConnectorApolloDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    api_key: Required[str]


class DataConnectorApolloDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["apollo"]]

    settings: DataConnectorApolloDiscriminatedConnectionSettingsSettings


class DataConnectorPlaidDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="accessToken")]]

    institution: object

    item: object

    item_id: Annotated[Optional[str], PropertyInfo(alias="itemId")]

    status: object

    webhook_item_error: Annotated[None, PropertyInfo(alias="webhookItemError")]


class DataConnectorPlaidDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["plaid"]]

    settings: DataConnectorPlaidDiscriminatedConnectionSettingsSettings


class DataConnectorPostgresDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    database_url: str


class DataConnectorPostgresDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["postgres"]]

    settings: DataConnectorPostgresDiscriminatedConnectionSettingsSettings


class DataConnectorSlackAgentDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[str]
    """Bot OAuth token - xoxb-..."""


class DataConnectorSlackAgentDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["slack-agent"]]

    settings: DataConnectorSlackAgentDiscriminatedConnectionSettingsSettings


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuthCredentials(
    TypedDict, total=False
):
    access_token: Required[str]

    client_id: str
    """Client ID used for the connection"""

    expires_at: str

    expires_in: float

    raw: Dict[str, object]

    refresh_token: str

    scope: str

    token_type: str


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuth(TypedDict, total=False):
    created_at: str

    credentials: DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""

    last_fetched_at: str

    metadata: Optional[Dict[str, object]]

    updated_at: str


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderApp(TypedDict, total=False):
    app_id: Required[str]
    """The Slack app ID"""

    client_id: Required[str]
    """The client ID for the app"""

    client_secret: Required[str]
    """The client secret for the app"""

    oauth_url: Required[str]
    """The OAuth authorization URL for the app"""

    signing_secret: Required[str]
    """The signing secret for the app"""

    verification_token: Required[str]
    """The verification token for the app"""


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilder(TypedDict, total=False):
    oauth: Required[DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderOAuth]

    app: DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilderApp
    """Slack app configuration created by the agent builder"""


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsOAuth]

    access_token: str
    """Same as oauth.credentials.access_token, but more convenient to access.

    Optional for backward compatibility until we remove the oauth field
    """

    agent_builder: DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettingsAgentBuilder

    event_subscription_url: str
    """URL for Slack event subscriptions"""


class DataConnectorSlackAgentBuilderDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["slack-agent-builder"]]

    settings: DataConnectorSlackAgentBuilderDiscriminatedConnectionSettingsSettings


class DataConnectorStripeDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    mcp: Required[str]
    """MCP access token"""

    publishable: Required[str]
    """Stripe publishable key for production"""

    secret: Required[str]
    """Stripe secret key for production"""


class DataConnectorStripeDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["stripe"]]

    settings: DataConnectorStripeDiscriminatedConnectionSettingsSettings


class DataConnectorStripeAgentSandboxDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    claim_url: Required[str]
    """URL to claim/access the Stripe sandbox"""

    mcp: Required[str]
    """MCP access token"""

    publishable: Required[str]
    """Stripe publishable key for the sandbox"""

    secret: Required[str]
    """Stripe secret key for the sandbox"""


class DataConnectorStripeAgentSandboxDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["stripe-agent-sandbox"]]

    settings: DataConnectorStripeAgentSandboxDiscriminatedConnectionSettingsSettings


class DataConnectorTwilioDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    account_sid: Required[str]

    api_key: Required[str]

    api_key_secret: Required[str]


class DataConnectorTwilioDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["twilio"]]

    settings: DataConnectorTwilioDiscriminatedConnectionSettingsSettings


class DataConnectorWorkatoDiscriminatedConnectionSettingsSettings(TypedDict, total=False):
    workato_api_host: Required[str]

    workato_api_token: Required[str]

    workato_account_id: str


class DataConnectorWorkatoDiscriminatedConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["workato"]]

    settings: DataConnectorWorkatoDiscriminatedConnectionSettingsSettings


Data: TypeAlias = Union[
    DataConnectorAcmeApikeyDiscriminatedConnectionSettings,
    DataConnectorAcmeOauth2DiscriminatedConnectionSettings,
    DataConnectorAsanaDiscriminatedConnectionSettings,
    DataConnectorBigqueryDiscriminatedConnectionSettings,
    DataConnectorBoxDiscriminatedConnectionSettings,
    DataConnectorCalendlyDiscriminatedConnectionSettings,
    DataConnectorConfluenceDiscriminatedConnectionSettings,
    DataConnectorDatabricksDiscriminatedConnectionSettings,
    DataConnectorDiscordDiscriminatedConnectionSettings,
    DataConnectorDropboxDiscriminatedConnectionSettings,
    DataConnectorFigmaDiscriminatedConnectionSettings,
    DataConnectorGitHubDiscriminatedConnectionSettings,
    DataConnectorGoogleCalendarDiscriminatedConnectionSettings,
    DataConnectorGoogleDocsDiscriminatedConnectionSettings,
    DataConnectorGoogleDriveDiscriminatedConnectionSettings,
    DataConnectorGoogleMailDiscriminatedConnectionSettings,
    DataConnectorGoogleSheetDiscriminatedConnectionSettings,
    DataConnectorHubspotDiscriminatedConnectionSettings,
    DataConnectorInstagramDiscriminatedConnectionSettings,
    DataConnectorJiraDiscriminatedConnectionSettings,
    DataConnectorLinearDiscriminatedConnectionSettings,
    DataConnectorMondayDiscriminatedConnectionSettings,
    DataConnectorNotionDiscriminatedConnectionSettings,
    DataConnectorOnedriveDiscriminatedConnectionSettings,
    DataConnectorOutlookDiscriminatedConnectionSettings,
    DataConnectorResendDiscriminatedConnectionSettings,
    DataConnectorSalesforceDiscriminatedConnectionSettings,
    DataConnectorSendgridDiscriminatedConnectionSettings,
    DataConnectorSharepointDiscriminatedConnectionSettings,
    DataConnectorSlackDeployedAgentDiscriminatedConnectionSettings,
    DataConnectorSlackDiscriminatedConnectionSettings,
    DataConnectorSnowflakeDiscriminatedConnectionSettings,
    DataConnectorSpotifyDiscriminatedConnectionSettings,
    DataConnectorYoutubeDiscriminatedConnectionSettings,
    DataConnectorZendeskDiscriminatedConnectionSettings,
    DataConnectorZoomDiscriminatedConnectionSettings,
    DataConnectorApolloDiscriminatedConnectionSettings,
    DataConnectorPlaidDiscriminatedConnectionSettings,
    DataConnectorPostgresDiscriminatedConnectionSettings,
    DataConnectorSlackAgentDiscriminatedConnectionSettings,
    DataConnectorSlackAgentBuilderDiscriminatedConnectionSettings,
    DataConnectorStripeDiscriminatedConnectionSettings,
    DataConnectorStripeAgentSandboxDiscriminatedConnectionSettings,
    DataConnectorTwilioDiscriminatedConnectionSettings,
    DataConnectorWorkatoDiscriminatedConnectionSettings,
]
