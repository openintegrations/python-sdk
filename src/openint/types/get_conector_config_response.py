# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .connector import Connector
from .integration import Integration

__all__ = [
    "GetConectorConfigResponse",
    "ConnectorAcmeApikeyDiscriminatedConnectorConfig",
    "ConnectorAcmeOauth2DiscriminatedConnectorConfig",
    "ConnectorAcmeOauth2DiscriminatedConnectorConfigConfig",
    "ConnectorAcmeOauth2DiscriminatedConnectorConfigConfigOAuth",
    "ConnectorAsanaDiscriminatedConnectorConfig",
    "ConnectorAsanaDiscriminatedConnectorConfigConfig",
    "ConnectorAsanaDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorBigqueryDiscriminatedConnectorConfig",
    "ConnectorBigqueryDiscriminatedConnectorConfigConfig",
    "ConnectorBigqueryDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorBoxDiscriminatedConnectorConfig",
    "ConnectorBoxDiscriminatedConnectorConfigConfig",
    "ConnectorBoxDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorCalendlyDiscriminatedConnectorConfig",
    "ConnectorCalendlyDiscriminatedConnectorConfigConfig",
    "ConnectorCalendlyDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorConfluenceDiscriminatedConnectorConfig",
    "ConnectorConfluenceDiscriminatedConnectorConfigConfig",
    "ConnectorConfluenceDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorDatabricksDiscriminatedConnectorConfig",
    "ConnectorDatabricksDiscriminatedConnectorConfigConfig",
    "ConnectorDatabricksDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorDiscordDiscriminatedConnectorConfig",
    "ConnectorDiscordDiscriminatedConnectorConfigConfig",
    "ConnectorDiscordDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorDropboxDiscriminatedConnectorConfig",
    "ConnectorDropboxDiscriminatedConnectorConfigConfig",
    "ConnectorDropboxDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorFigmaDiscriminatedConnectorConfig",
    "ConnectorFigmaDiscriminatedConnectorConfigConfig",
    "ConnectorFigmaDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorGitHubDiscriminatedConnectorConfig",
    "ConnectorGitHubDiscriminatedConnectorConfigConfig",
    "ConnectorGitHubDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorGoogleCalendarDiscriminatedConnectorConfig",
    "ConnectorGoogleCalendarDiscriminatedConnectorConfigConfig",
    "ConnectorGoogleCalendarDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorGoogleDocsDiscriminatedConnectorConfig",
    "ConnectorGoogleDocsDiscriminatedConnectorConfigConfig",
    "ConnectorGoogleDocsDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorGoogleDriveDiscriminatedConnectorConfig",
    "ConnectorGoogleDriveDiscriminatedConnectorConfigConfig",
    "ConnectorGoogleDriveDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorGoogleMailDiscriminatedConnectorConfig",
    "ConnectorGoogleMailDiscriminatedConnectorConfigConfig",
    "ConnectorGoogleMailDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorGoogleSheetDiscriminatedConnectorConfig",
    "ConnectorGoogleSheetDiscriminatedConnectorConfigConfig",
    "ConnectorGoogleSheetDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorHubspotDiscriminatedConnectorConfig",
    "ConnectorHubspotDiscriminatedConnectorConfigConfig",
    "ConnectorHubspotDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorInstagramDiscriminatedConnectorConfig",
    "ConnectorInstagramDiscriminatedConnectorConfigConfig",
    "ConnectorInstagramDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorJiraDiscriminatedConnectorConfig",
    "ConnectorJiraDiscriminatedConnectorConfigConfig",
    "ConnectorJiraDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorLinearDiscriminatedConnectorConfig",
    "ConnectorLinearDiscriminatedConnectorConfigConfig",
    "ConnectorLinearDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorMondayDiscriminatedConnectorConfig",
    "ConnectorMondayDiscriminatedConnectorConfigConfig",
    "ConnectorMondayDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorNotionDiscriminatedConnectorConfig",
    "ConnectorNotionDiscriminatedConnectorConfigConfig",
    "ConnectorNotionDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorOnedriveDiscriminatedConnectorConfig",
    "ConnectorOnedriveDiscriminatedConnectorConfigConfig",
    "ConnectorOnedriveDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorOutlookDiscriminatedConnectorConfig",
    "ConnectorOutlookDiscriminatedConnectorConfigConfig",
    "ConnectorOutlookDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorResendDiscriminatedConnectorConfig",
    "ConnectorSalesforceDiscriminatedConnectorConfig",
    "ConnectorSalesforceDiscriminatedConnectorConfigConfig",
    "ConnectorSalesforceDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorSendgridDiscriminatedConnectorConfig",
    "ConnectorSharepointDiscriminatedConnectorConfig",
    "ConnectorSharepointDiscriminatedConnectorConfigConfig",
    "ConnectorSharepointDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorSlackDeployedAgentDiscriminatedConnectorConfig",
    "ConnectorSlackDeployedAgentDiscriminatedConnectorConfigConfig",
    "ConnectorSlackDeployedAgentDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorSlackDiscriminatedConnectorConfig",
    "ConnectorSlackDiscriminatedConnectorConfigConfig",
    "ConnectorSlackDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorSnowflakeDiscriminatedConnectorConfig",
    "ConnectorSnowflakeDiscriminatedConnectorConfigConfig",
    "ConnectorSnowflakeDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorSpotifyDiscriminatedConnectorConfig",
    "ConnectorSpotifyDiscriminatedConnectorConfigConfig",
    "ConnectorSpotifyDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorYoutubeDiscriminatedConnectorConfig",
    "ConnectorYoutubeDiscriminatedConnectorConfigConfig",
    "ConnectorYoutubeDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorZendeskDiscriminatedConnectorConfig",
    "ConnectorZendeskDiscriminatedConnectorConfigConfig",
    "ConnectorZendeskDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorZoomDiscriminatedConnectorConfig",
    "ConnectorZoomDiscriminatedConnectorConfigConfig",
    "ConnectorZoomDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorApolloDiscriminatedConnectorConfig",
    "ConnectorPlaidDiscriminatedConnectorConfig",
    "ConnectorPlaidDiscriminatedConnectorConfigConfig",
    "ConnectorPlaidDiscriminatedConnectorConfigConfigCredentials",
    "ConnectorPostgresDiscriminatedConnectorConfig",
    "ConnectorSlackAgentDiscriminatedConnectorConfig",
    "ConnectorSlackAgentDiscriminatedConnectorConfigConfig",
    "ConnectorSlackAgentBuilderDiscriminatedConnectorConfig",
    "ConnectorSlackAgentBuilderDiscriminatedConnectorConfigConfig",
    "ConnectorSlackAgentBuilderDiscriminatedConnectorConfigConfigOAuth",
    "ConnectorStripeDiscriminatedConnectorConfig",
    "ConnectorStripeAgentSandboxDiscriminatedConnectorConfig",
    "ConnectorTwilioDiscriminatedConnectorConfig",
    "ConnectorWorkatoDiscriminatedConnectorConfig",
]


class ConnectorAcmeApikeyDiscriminatedConnectorConfig(BaseModel):
    config: object
    """Base configuration for api key connector"""

    connector_name: Literal["acme-apikey"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorAcmeOauth2DiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorAcmeOauth2DiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorAcmeOauth2DiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorAcmeOauth2DiscriminatedConnectorConfig(BaseModel):
    config: ConnectorAcmeOauth2DiscriminatedConnectorConfigConfig

    connector_name: Literal["acme-oauth2"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorAsanaDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorAsanaDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorAsanaDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorAsanaDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorAsanaDiscriminatedConnectorConfigConfig

    connector_name: Literal["asana"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorBigqueryDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorBigqueryDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorBigqueryDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorBigqueryDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorBigqueryDiscriminatedConnectorConfigConfig

    connector_name: Literal["bigquery"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorBoxDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorBoxDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorBoxDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorBoxDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorBoxDiscriminatedConnectorConfigConfig

    connector_name: Literal["box"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorCalendlyDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorCalendlyDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorCalendlyDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorCalendlyDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorCalendlyDiscriminatedConnectorConfigConfig

    connector_name: Literal["calendly"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorConfluenceDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorConfluenceDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorConfluenceDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorConfluenceDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorConfluenceDiscriminatedConnectorConfigConfig

    connector_name: Literal["confluence"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorDatabricksDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorDatabricksDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorDatabricksDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorDatabricksDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorDatabricksDiscriminatedConnectorConfigConfig

    connector_name: Literal["databricks"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorDiscordDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorDiscordDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorDiscordDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorDiscordDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorDiscordDiscriminatedConnectorConfigConfig

    connector_name: Literal["discord"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorDropboxDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorDropboxDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorDropboxDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorDropboxDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorDropboxDiscriminatedConnectorConfigConfig

    connector_name: Literal["dropbox"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorFigmaDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorFigmaDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorFigmaDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorFigmaDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorFigmaDiscriminatedConnectorConfigConfig

    connector_name: Literal["figma"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGitHubDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorGitHubDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorGitHubDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorGitHubDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorGitHubDiscriminatedConnectorConfigConfig

    connector_name: Literal["github"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleCalendarDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorGoogleCalendarDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorGoogleCalendarDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorGoogleCalendarDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorGoogleCalendarDiscriminatedConnectorConfigConfig

    connector_name: Literal["google-calendar"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleDocsDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorGoogleDocsDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorGoogleDocsDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorGoogleDocsDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorGoogleDocsDiscriminatedConnectorConfigConfig

    connector_name: Literal["google-docs"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleDriveDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorGoogleDriveDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorGoogleDriveDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorGoogleDriveDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorGoogleDriveDiscriminatedConnectorConfigConfig

    connector_name: Literal["google-drive"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleMailDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorGoogleMailDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorGoogleMailDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorGoogleMailDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorGoogleMailDiscriminatedConnectorConfigConfig

    connector_name: Literal["google-mail"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorGoogleSheetDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorGoogleSheetDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorGoogleSheetDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorGoogleSheetDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorGoogleSheetDiscriminatedConnectorConfigConfig

    connector_name: Literal["google-sheet"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorHubspotDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorHubspotDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorHubspotDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorHubspotDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorHubspotDiscriminatedConnectorConfigConfig

    connector_name: Literal["hubspot"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorInstagramDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorInstagramDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorInstagramDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorInstagramDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorInstagramDiscriminatedConnectorConfigConfig

    connector_name: Literal["instagram"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorJiraDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorJiraDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorJiraDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorJiraDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorJiraDiscriminatedConnectorConfigConfig

    connector_name: Literal["jira"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorLinearDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorLinearDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorLinearDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorLinearDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorLinearDiscriminatedConnectorConfigConfig

    connector_name: Literal["linear"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorMondayDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorMondayDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorMondayDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorMondayDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorMondayDiscriminatedConnectorConfigConfig

    connector_name: Literal["monday"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorNotionDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorNotionDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorNotionDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorNotionDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorNotionDiscriminatedConnectorConfigConfig

    connector_name: Literal["notion"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorOnedriveDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorOnedriveDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorOnedriveDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorOnedriveDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorOnedriveDiscriminatedConnectorConfigConfig

    connector_name: Literal["onedrive"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorOutlookDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorOutlookDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorOutlookDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorOutlookDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorOutlookDiscriminatedConnectorConfigConfig

    connector_name: Literal["outlook"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorResendDiscriminatedConnectorConfig(BaseModel):
    config: object
    """Base configuration for api key connector"""

    connector_name: Literal["resend"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSalesforceDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorSalesforceDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorSalesforceDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorSalesforceDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSalesforceDiscriminatedConnectorConfigConfig

    connector_name: Literal["salesforce"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSendgridDiscriminatedConnectorConfig(BaseModel):
    config: object
    """Base configuration for api key connector"""

    connector_name: Literal["sendgrid"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSharepointDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorSharepointDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorSharepointDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorSharepointDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSharepointDiscriminatedConnectorConfigConfig

    connector_name: Literal["sharepoint"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackDeployedAgentDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorSlackDeployedAgentDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorSlackDeployedAgentDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorSlackDeployedAgentDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSlackDeployedAgentDiscriminatedConnectorConfigConfig

    connector_name: Literal["slack-deployed-agent"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorSlackDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorSlackDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorSlackDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSlackDiscriminatedConnectorConfigConfig

    connector_name: Literal["slack"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSnowflakeDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorSnowflakeDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorSnowflakeDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorSnowflakeDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSnowflakeDiscriminatedConnectorConfigConfig

    connector_name: Literal["snowflake"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSpotifyDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorSpotifyDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorSpotifyDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorSpotifyDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSpotifyDiscriminatedConnectorConfigConfig

    connector_name: Literal["spotify"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorYoutubeDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorYoutubeDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorYoutubeDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorYoutubeDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorYoutubeDiscriminatedConnectorConfigConfig

    connector_name: Literal["youtube"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorZendeskDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorZendeskDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorZendeskDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorZendeskDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorZendeskDiscriminatedConnectorConfigConfig

    connector_name: Literal["zendesk"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorZoomDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorZoomDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorZoomDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorZoomDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorZoomDiscriminatedConnectorConfigConfig

    connector_name: Literal["zoom"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorApolloDiscriminatedConnectorConfig(BaseModel):
    config: object

    connector_name: Literal["apollo"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorPlaidDiscriminatedConnectorConfigConfigCredentials(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")


class ConnectorPlaidDiscriminatedConnectorConfigConfig(BaseModel):
    client_name: str = FieldInfo(alias="clientName")
    """
    The name of your application, as it should be displayed in Link. Maximum length
    of 30 characters. If a value longer than 30 characters is provided, Link will
    display "This Application" instead.
    """

    country_codes: List[
        Literal["US", "GB", "ES", "NL", "FR", "IE", "CA", "DE", "IT", "PL", "DK", "NO", "SE", "EE", "LT", "LV"]
    ] = FieldInfo(alias="countryCodes")

    env_name: Literal["sandbox", "development", "production"] = FieldInfo(alias="envName")

    language: Literal["en", "fr", "es", "nl", "de"]

    products: List[
        Literal[
            "assets",
            "auth",
            "balance",
            "identity",
            "investments",
            "liabilities",
            "payment_initiation",
            "identity_verification",
            "transactions",
            "credit_details",
            "income",
            "income_verification",
            "deposit_switch",
            "standing_orders",
            "transfer",
            "employment",
            "recurring_transactions",
        ]
    ]

    credentials: Optional[ConnectorPlaidDiscriminatedConnectorConfigConfigCredentials] = None


class ConnectorPlaidDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorPlaidDiscriminatedConnectorConfigConfig

    connector_name: Literal["plaid"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorPostgresDiscriminatedConnectorConfig(BaseModel):
    config: object

    connector_name: Literal["postgres"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackAgentDiscriminatedConnectorConfigConfig(BaseModel):
    challenge_code: str
    """Previous challenge code - e.g. challenge_slack_abc123xyz"""

    challenge_response: str
    """USER_PASTED_TOKEN - SLACK_ONETIME_CHALLENGE_CODE"""

    app_description: Optional[str] = None
    """App description - Replit integration app for Slack workspace"""

    app_id: Optional[str] = None
    """App ID - A1234567890"""

    app_name: Optional[str] = None
    """App name - Replit Agent App"""

    client_id: Optional[str] = None
    """Client ID - 1234567890.1234567890"""

    client_secret: Optional[str] = None
    """Client secret - abc123..."""

    event_subscription_url: Optional[str] = None
    """Initial event subscription URL"""

    initial_oauth_url: Optional[str] = None
    """Initial OAuth URL - https://slack.com/oauth/v2/authorize?..."""

    service_token: Optional[str] = None
    """Service token - xoxb-..."""

    signing_secret: Optional[str] = None
    """Signing secret - abc123..."""

    verification_token: Optional[str] = None
    """Verification token - xyz123..."""


class ConnectorSlackAgentDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSlackAgentDiscriminatedConnectorConfigConfig

    connector_name: Literal["slack-agent"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorSlackAgentBuilderDiscriminatedConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    redirect_uri: Optional[str] = None
    """Custom redirect URI"""

    scopes: Optional[List[str]] = None


class ConnectorSlackAgentBuilderDiscriminatedConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorSlackAgentBuilderDiscriminatedConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorSlackAgentBuilderDiscriminatedConnectorConfig(BaseModel):
    config: ConnectorSlackAgentBuilderDiscriminatedConnectorConfigConfig

    connector_name: Literal["slack-agent-builder"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorStripeDiscriminatedConnectorConfig(BaseModel):
    config: object

    connector_name: Literal["stripe"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorStripeAgentSandboxDiscriminatedConnectorConfig(BaseModel):
    config: object

    connector_name: Literal["stripe-agent-sandbox"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorTwilioDiscriminatedConnectorConfig(BaseModel):
    config: object

    connector_name: Literal["twilio"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorWorkatoDiscriminatedConnectorConfig(BaseModel):
    config: object

    connector_name: Literal["workato"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[Connector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, Integration]] = None

    metadata: Optional[Dict[str, object]] = None
    """
    JSON object can can be used to associate arbitrary metadata to avoid needing a
    separate 1-1 table just for simple key values in your application. During
    updates this object will be shallowly merged
    """

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


GetConectorConfigResponse: TypeAlias = Union[
    ConnectorAcmeApikeyDiscriminatedConnectorConfig,
    ConnectorAcmeOauth2DiscriminatedConnectorConfig,
    ConnectorAsanaDiscriminatedConnectorConfig,
    ConnectorBigqueryDiscriminatedConnectorConfig,
    ConnectorBoxDiscriminatedConnectorConfig,
    ConnectorCalendlyDiscriminatedConnectorConfig,
    ConnectorConfluenceDiscriminatedConnectorConfig,
    ConnectorDatabricksDiscriminatedConnectorConfig,
    ConnectorDiscordDiscriminatedConnectorConfig,
    ConnectorDropboxDiscriminatedConnectorConfig,
    ConnectorFigmaDiscriminatedConnectorConfig,
    ConnectorGitHubDiscriminatedConnectorConfig,
    ConnectorGoogleCalendarDiscriminatedConnectorConfig,
    ConnectorGoogleDocsDiscriminatedConnectorConfig,
    ConnectorGoogleDriveDiscriminatedConnectorConfig,
    ConnectorGoogleMailDiscriminatedConnectorConfig,
    ConnectorGoogleSheetDiscriminatedConnectorConfig,
    ConnectorHubspotDiscriminatedConnectorConfig,
    ConnectorInstagramDiscriminatedConnectorConfig,
    ConnectorJiraDiscriminatedConnectorConfig,
    ConnectorLinearDiscriminatedConnectorConfig,
    ConnectorMondayDiscriminatedConnectorConfig,
    ConnectorNotionDiscriminatedConnectorConfig,
    ConnectorOnedriveDiscriminatedConnectorConfig,
    ConnectorOutlookDiscriminatedConnectorConfig,
    ConnectorResendDiscriminatedConnectorConfig,
    ConnectorSalesforceDiscriminatedConnectorConfig,
    ConnectorSendgridDiscriminatedConnectorConfig,
    ConnectorSharepointDiscriminatedConnectorConfig,
    ConnectorSlackDeployedAgentDiscriminatedConnectorConfig,
    ConnectorSlackDiscriminatedConnectorConfig,
    ConnectorSnowflakeDiscriminatedConnectorConfig,
    ConnectorSpotifyDiscriminatedConnectorConfig,
    ConnectorYoutubeDiscriminatedConnectorConfig,
    ConnectorZendeskDiscriminatedConnectorConfig,
    ConnectorZoomDiscriminatedConnectorConfig,
    ConnectorApolloDiscriminatedConnectorConfig,
    ConnectorPlaidDiscriminatedConnectorConfig,
    ConnectorPostgresDiscriminatedConnectorConfig,
    ConnectorSlackAgentDiscriminatedConnectorConfig,
    ConnectorSlackAgentBuilderDiscriminatedConnectorConfig,
    ConnectorStripeDiscriminatedConnectorConfig,
    ConnectorStripeAgentSandboxDiscriminatedConnectorConfig,
    ConnectorTwilioDiscriminatedConnectorConfig,
    ConnectorWorkatoDiscriminatedConnectorConfig,
]
