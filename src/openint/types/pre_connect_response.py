# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "PreConnectResponse",
    "ConnectorAcceloDiscriminatedConnectInput",
    "ConnectorAcceloDiscriminatedConnectInputConnectInput",
    "ConnectorAcmeApikeyDiscriminatedConnectInput",
    "ConnectorAcmeOauth2DiscriminatedConnectInput",
    "ConnectorAcmeOauth2DiscriminatedConnectInputConnectInput",
    "ConnectorAdobeDiscriminatedConnectInput",
    "ConnectorAdobeDiscriminatedConnectInputConnectInput",
    "ConnectorAdyenDiscriminatedConnectInput",
    "ConnectorAdyenDiscriminatedConnectInputConnectInput",
    "ConnectorAircallDiscriminatedConnectInput",
    "ConnectorAircallDiscriminatedConnectInputConnectInput",
    "ConnectorAmazonDiscriminatedConnectInput",
    "ConnectorAmazonDiscriminatedConnectInputConnectInput",
    "ConnectorApaleoDiscriminatedConnectInput",
    "ConnectorApaleoDiscriminatedConnectInputConnectInput",
    "ConnectorAsanaDiscriminatedConnectInput",
    "ConnectorAsanaDiscriminatedConnectInputConnectInput",
    "ConnectorAttioDiscriminatedConnectInput",
    "ConnectorAttioDiscriminatedConnectInputConnectInput",
    "ConnectorAuth0DiscriminatedConnectInput",
    "ConnectorAuth0DiscriminatedConnectInputConnectInput",
    "ConnectorAutodeskDiscriminatedConnectInput",
    "ConnectorAutodeskDiscriminatedConnectInputConnectInput",
    "ConnectorAwsDiscriminatedConnectInput",
    "ConnectorAwsDiscriminatedConnectInputConnectInput",
    "ConnectorBamboohrDiscriminatedConnectInput",
    "ConnectorBamboohrDiscriminatedConnectInputConnectInput",
    "ConnectorBasecampDiscriminatedConnectInput",
    "ConnectorBasecampDiscriminatedConnectInputConnectInput",
    "ConnectorBattlenetDiscriminatedConnectInput",
    "ConnectorBattlenetDiscriminatedConnectInputConnectInput",
    "ConnectorBigcommerceDiscriminatedConnectInput",
    "ConnectorBigcommerceDiscriminatedConnectInputConnectInput",
    "ConnectorBitbucketDiscriminatedConnectInput",
    "ConnectorBitbucketDiscriminatedConnectInputConnectInput",
    "ConnectorBitlyDiscriminatedConnectInput",
    "ConnectorBitlyDiscriminatedConnectInputConnectInput",
    "ConnectorBlackbaudDiscriminatedConnectInput",
    "ConnectorBlackbaudDiscriminatedConnectInputConnectInput",
    "ConnectorBoldsignDiscriminatedConnectInput",
    "ConnectorBoldsignDiscriminatedConnectInputConnectInput",
    "ConnectorBoxDiscriminatedConnectInput",
    "ConnectorBoxDiscriminatedConnectInputConnectInput",
    "ConnectorBraintreeDiscriminatedConnectInput",
    "ConnectorBraintreeDiscriminatedConnectInputConnectInput",
    "ConnectorCalendlyDiscriminatedConnectInput",
    "ConnectorCalendlyDiscriminatedConnectInputConnectInput",
    "ConnectorClickupDiscriminatedConnectInput",
    "ConnectorClickupDiscriminatedConnectInputConnectInput",
    "ConnectorCloseDiscriminatedConnectInput",
    "ConnectorCloseDiscriminatedConnectInputConnectInput",
    "ConnectorConfluenceDiscriminatedConnectInput",
    "ConnectorConfluenceDiscriminatedConnectInputConnectInput",
    "ConnectorContentfulDiscriminatedConnectInput",
    "ConnectorContentfulDiscriminatedConnectInputConnectInput",
    "ConnectorContentstackDiscriminatedConnectInput",
    "ConnectorContentstackDiscriminatedConnectInputConnectInput",
    "ConnectorCopperDiscriminatedConnectInput",
    "ConnectorCopperDiscriminatedConnectInputConnectInput",
    "ConnectorCorosDiscriminatedConnectInput",
    "ConnectorCorosDiscriminatedConnectInputConnectInput",
    "ConnectorDatevDiscriminatedConnectInput",
    "ConnectorDatevDiscriminatedConnectInputConnectInput",
    "ConnectorDeelDiscriminatedConnectInput",
    "ConnectorDeelDiscriminatedConnectInputConnectInput",
    "ConnectorDialpadDiscriminatedConnectInput",
    "ConnectorDialpadDiscriminatedConnectInputConnectInput",
    "ConnectorDigitaloceanDiscriminatedConnectInput",
    "ConnectorDigitaloceanDiscriminatedConnectInputConnectInput",
    "ConnectorDiscordDiscriminatedConnectInput",
    "ConnectorDiscordDiscriminatedConnectInputConnectInput",
    "ConnectorDocusignDiscriminatedConnectInput",
    "ConnectorDocusignDiscriminatedConnectInputConnectInput",
    "ConnectorDropboxDiscriminatedConnectInput",
    "ConnectorDropboxDiscriminatedConnectInputConnectInput",
    "ConnectorEbayDiscriminatedConnectInput",
    "ConnectorEbayDiscriminatedConnectInputConnectInput",
    "ConnectorEgnyteDiscriminatedConnectInput",
    "ConnectorEgnyteDiscriminatedConnectInputConnectInput",
    "ConnectorEnvoyDiscriminatedConnectInput",
    "ConnectorEnvoyDiscriminatedConnectInputConnectInput",
    "ConnectorEventbriteDiscriminatedConnectInput",
    "ConnectorEventbriteDiscriminatedConnectInputConnectInput",
    "ConnectorExistDiscriminatedConnectInput",
    "ConnectorExistDiscriminatedConnectInputConnectInput",
    "ConnectorFacebookDiscriminatedConnectInput",
    "ConnectorFacebookDiscriminatedConnectInputConnectInput",
    "ConnectorFactorialDiscriminatedConnectInput",
    "ConnectorFactorialDiscriminatedConnectInputConnectInput",
    "ConnectorFigmaDiscriminatedConnectInput",
    "ConnectorFigmaDiscriminatedConnectInputConnectInput",
    "ConnectorFitbitDiscriminatedConnectInput",
    "ConnectorFitbitDiscriminatedConnectInputConnectInput",
    "ConnectorFortnoxDiscriminatedConnectInput",
    "ConnectorFortnoxDiscriminatedConnectInputConnectInput",
    "ConnectorFreshbooksDiscriminatedConnectInput",
    "ConnectorFreshbooksDiscriminatedConnectInputConnectInput",
    "ConnectorFrontDiscriminatedConnectInput",
    "ConnectorFrontDiscriminatedConnectInputConnectInput",
    "ConnectorGitHubDiscriminatedConnectInput",
    "ConnectorGitHubDiscriminatedConnectInputConnectInput",
    "ConnectorGitlabDiscriminatedConnectInput",
    "ConnectorGitlabDiscriminatedConnectInputConnectInput",
    "ConnectorGongDiscriminatedConnectInput",
    "ConnectorGongDiscriminatedConnectInputConnectInput",
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
    "ConnectorGorgiasDiscriminatedConnectInput",
    "ConnectorGorgiasDiscriminatedConnectInputConnectInput",
    "ConnectorGrainDiscriminatedConnectInput",
    "ConnectorGrainDiscriminatedConnectInputConnectInput",
    "ConnectorGumroadDiscriminatedConnectInput",
    "ConnectorGumroadDiscriminatedConnectInputConnectInput",
    "ConnectorGustoDiscriminatedConnectInput",
    "ConnectorGustoDiscriminatedConnectInputConnectInput",
    "ConnectorHarvestDiscriminatedConnectInput",
    "ConnectorHarvestDiscriminatedConnectInputConnectInput",
    "ConnectorHighlevelDiscriminatedConnectInput",
    "ConnectorHighlevelDiscriminatedConnectInputConnectInput",
    "ConnectorHubspotDiscriminatedConnectInput",
    "ConnectorHubspotDiscriminatedConnectInputConnectInput",
    "ConnectorInstagramDiscriminatedConnectInput",
    "ConnectorInstagramDiscriminatedConnectInputConnectInput",
    "ConnectorIntercomDiscriminatedConnectInput",
    "ConnectorIntercomDiscriminatedConnectInputConnectInput",
    "ConnectorJiraDiscriminatedConnectInput",
    "ConnectorJiraDiscriminatedConnectInputConnectInput",
    "ConnectorKeapDiscriminatedConnectInput",
    "ConnectorKeapDiscriminatedConnectInputConnectInput",
    "ConnectorLeverDiscriminatedConnectInput",
    "ConnectorLeverDiscriminatedConnectInputConnectInput",
    "ConnectorLinearDiscriminatedConnectInput",
    "ConnectorLinearDiscriminatedConnectInputConnectInput",
    "ConnectorLinkedinDiscriminatedConnectInput",
    "ConnectorLinkedinDiscriminatedConnectInputConnectInput",
    "ConnectorLinkhutDiscriminatedConnectInput",
    "ConnectorLinkhutDiscriminatedConnectInputConnectInput",
    "ConnectorMailchimpDiscriminatedConnectInput",
    "ConnectorMailchimpDiscriminatedConnectInputConnectInput",
    "ConnectorMiroDiscriminatedConnectInput",
    "ConnectorMiroDiscriminatedConnectInputConnectInput",
    "ConnectorMondayDiscriminatedConnectInput",
    "ConnectorMondayDiscriminatedConnectInputConnectInput",
    "ConnectorMuralDiscriminatedConnectInput",
    "ConnectorMuralDiscriminatedConnectInputConnectInput",
    "ConnectorNamelyDiscriminatedConnectInput",
    "ConnectorNamelyDiscriminatedConnectInputConnectInput",
    "ConnectorNationbuilderDiscriminatedConnectInput",
    "ConnectorNationbuilderDiscriminatedConnectInputConnectInput",
    "ConnectorNetsuiteDiscriminatedConnectInput",
    "ConnectorNetsuiteDiscriminatedConnectInputConnectInput",
    "ConnectorNotionDiscriminatedConnectInput",
    "ConnectorNotionDiscriminatedConnectInputConnectInput",
    "ConnectorOdooDiscriminatedConnectInput",
    "ConnectorOdooDiscriminatedConnectInputConnectInput",
    "ConnectorOktaDiscriminatedConnectInput",
    "ConnectorOktaDiscriminatedConnectInputConnectInput",
    "ConnectorOsuDiscriminatedConnectInput",
    "ConnectorOsuDiscriminatedConnectInputConnectInput",
    "ConnectorOuraDiscriminatedConnectInput",
    "ConnectorOuraDiscriminatedConnectInputConnectInput",
    "ConnectorOutreachDiscriminatedConnectInput",
    "ConnectorOutreachDiscriminatedConnectInputConnectInput",
    "ConnectorPagerdutyDiscriminatedConnectInput",
    "ConnectorPagerdutyDiscriminatedConnectInputConnectInput",
    "ConnectorPandadocDiscriminatedConnectInput",
    "ConnectorPandadocDiscriminatedConnectInputConnectInput",
    "ConnectorPayfitDiscriminatedConnectInput",
    "ConnectorPayfitDiscriminatedConnectInputConnectInput",
    "ConnectorPaypalDiscriminatedConnectInput",
    "ConnectorPaypalDiscriminatedConnectInputConnectInput",
    "ConnectorPennylaneDiscriminatedConnectInput",
    "ConnectorPennylaneDiscriminatedConnectInputConnectInput",
    "ConnectorPinterestDiscriminatedConnectInput",
    "ConnectorPinterestDiscriminatedConnectInputConnectInput",
    "ConnectorPipedriveDiscriminatedConnectInput",
    "ConnectorPipedriveDiscriminatedConnectInputConnectInput",
    "ConnectorPodiumDiscriminatedConnectInput",
    "ConnectorPodiumDiscriminatedConnectInputConnectInput",
    "ConnectorProductboardDiscriminatedConnectInput",
    "ConnectorProductboardDiscriminatedConnectInputConnectInput",
    "ConnectorQualtricsDiscriminatedConnectInput",
    "ConnectorQualtricsDiscriminatedConnectInputConnectInput",
    "ConnectorQuickbooksDiscriminatedConnectInput",
    "ConnectorQuickbooksDiscriminatedConnectInputConnectInput",
    "ConnectorRedditDiscriminatedConnectInput",
    "ConnectorRedditDiscriminatedConnectInputConnectInput",
    "ConnectorSageDiscriminatedConnectInput",
    "ConnectorSageDiscriminatedConnectInputConnectInput",
    "ConnectorSalesforceDiscriminatedConnectInput",
    "ConnectorSalesforceDiscriminatedConnectInputConnectInput",
    "ConnectorSalesloftDiscriminatedConnectInput",
    "ConnectorSalesloftDiscriminatedConnectInputConnectInput",
    "ConnectorSegmentDiscriminatedConnectInput",
    "ConnectorSegmentDiscriminatedConnectInputConnectInput",
    "ConnectorServicem8DiscriminatedConnectInput",
    "ConnectorServicem8DiscriminatedConnectInputConnectInput",
    "ConnectorServicenowDiscriminatedConnectInput",
    "ConnectorServicenowDiscriminatedConnectInputConnectInput",
    "ConnectorSharepointDiscriminatedConnectInput",
    "ConnectorSharepointDiscriminatedConnectInputConnectInput",
    "ConnectorShopifyDiscriminatedConnectInput",
    "ConnectorShopifyDiscriminatedConnectInputConnectInput",
    "ConnectorSignnowDiscriminatedConnectInput",
    "ConnectorSignnowDiscriminatedConnectInputConnectInput",
    "ConnectorSlackDiscriminatedConnectInput",
    "ConnectorSlackDiscriminatedConnectInputConnectInput",
    "ConnectorSmartsheetDiscriminatedConnectInput",
    "ConnectorSmartsheetDiscriminatedConnectInputConnectInput",
    "ConnectorSnowflakeDiscriminatedConnectInput",
    "ConnectorSnowflakeDiscriminatedConnectInputConnectInput",
    "ConnectorSpotifyDiscriminatedConnectInput",
    "ConnectorSpotifyDiscriminatedConnectInputConnectInput",
    "ConnectorSquarespaceDiscriminatedConnectInput",
    "ConnectorSquarespaceDiscriminatedConnectInputConnectInput",
    "ConnectorSquareupDiscriminatedConnectInput",
    "ConnectorSquareupDiscriminatedConnectInputConnectInput",
    "ConnectorStackexchangeDiscriminatedConnectInput",
    "ConnectorStackexchangeDiscriminatedConnectInputConnectInput",
    "ConnectorStravaDiscriminatedConnectInput",
    "ConnectorStravaDiscriminatedConnectInputConnectInput",
    "ConnectorTeamworkDiscriminatedConnectInput",
    "ConnectorTeamworkDiscriminatedConnectInputConnectInput",
    "ConnectorTicktickDiscriminatedConnectInput",
    "ConnectorTicktickDiscriminatedConnectInputConnectInput",
    "ConnectorTimelyDiscriminatedConnectInput",
    "ConnectorTimelyDiscriminatedConnectInputConnectInput",
    "ConnectorTodoistDiscriminatedConnectInput",
    "ConnectorTodoistDiscriminatedConnectInputConnectInput",
    "ConnectorTremendousDiscriminatedConnectInput",
    "ConnectorTremendousDiscriminatedConnectInputConnectInput",
    "ConnectorTsheetsteamDiscriminatedConnectInput",
    "ConnectorTsheetsteamDiscriminatedConnectInputConnectInput",
    "ConnectorTumblrDiscriminatedConnectInput",
    "ConnectorTumblrDiscriminatedConnectInputConnectInput",
    "ConnectorTwinfieldDiscriminatedConnectInput",
    "ConnectorTwinfieldDiscriminatedConnectInputConnectInput",
    "ConnectorTwitchDiscriminatedConnectInput",
    "ConnectorTwitchDiscriminatedConnectInputConnectInput",
    "ConnectorTwitterDiscriminatedConnectInput",
    "ConnectorTwitterDiscriminatedConnectInputConnectInput",
    "ConnectorTypeformDiscriminatedConnectInput",
    "ConnectorTypeformDiscriminatedConnectInputConnectInput",
    "ConnectorUberDiscriminatedConnectInput",
    "ConnectorUberDiscriminatedConnectInputConnectInput",
    "ConnectorVimeoDiscriminatedConnectInput",
    "ConnectorVimeoDiscriminatedConnectInputConnectInput",
    "ConnectorWakatimeDiscriminatedConnectInput",
    "ConnectorWakatimeDiscriminatedConnectInputConnectInput",
    "ConnectorWealthboxDiscriminatedConnectInput",
    "ConnectorWealthboxDiscriminatedConnectInputConnectInput",
    "ConnectorWebflowDiscriminatedConnectInput",
    "ConnectorWebflowDiscriminatedConnectInputConnectInput",
    "ConnectorWhoopDiscriminatedConnectInput",
    "ConnectorWhoopDiscriminatedConnectInputConnectInput",
    "ConnectorWordpressDiscriminatedConnectInput",
    "ConnectorWordpressDiscriminatedConnectInputConnectInput",
    "ConnectorWrikeDiscriminatedConnectInput",
    "ConnectorWrikeDiscriminatedConnectInputConnectInput",
    "ConnectorXeroDiscriminatedConnectInput",
    "ConnectorXeroDiscriminatedConnectInputConnectInput",
    "ConnectorYahooDiscriminatedConnectInput",
    "ConnectorYahooDiscriminatedConnectInputConnectInput",
    "ConnectorYandexDiscriminatedConnectInput",
    "ConnectorYandexDiscriminatedConnectInputConnectInput",
    "ConnectorZapierDiscriminatedConnectInput",
    "ConnectorZapierDiscriminatedConnectInputConnectInput",
    "ConnectorZendeskDiscriminatedConnectInput",
    "ConnectorZendeskDiscriminatedConnectInputConnectInput",
    "ConnectorZenefitsDiscriminatedConnectInput",
    "ConnectorZenefitsDiscriminatedConnectInputConnectInput",
    "ConnectorZohoDeskDiscriminatedConnectInput",
    "ConnectorZohoDeskDiscriminatedConnectInputConnectInput",
    "ConnectorZohoDiscriminatedConnectInput",
    "ConnectorZohoDiscriminatedConnectInputConnectInput",
    "ConnectorZoomDiscriminatedConnectInput",
    "ConnectorZoomDiscriminatedConnectInputConnectInput",
    "ConnectorAirtableDiscriminatedConnectInput",
    "ConnectorApolloDiscriminatedConnectInput",
    "ConnectorBrexDiscriminatedConnectInput",
    "ConnectorCodaDiscriminatedConnectInput",
    "ConnectorFinchDiscriminatedConnectInput",
    "ConnectorFinchDiscriminatedConnectInputConnectInput",
    "ConnectorFirebaseDiscriminatedConnectInput",
    "ConnectorForeceiptDiscriminatedConnectInput",
    "ConnectorForeceiptDiscriminatedConnectInputConnectInput",
    "ConnectorGreenhouseDiscriminatedConnectInput",
    "ConnectorHeronDiscriminatedConnectInput",
    "ConnectorLunchmoneyDiscriminatedConnectInput",
    "ConnectorMercuryDiscriminatedConnectInput",
    "ConnectorMergeDiscriminatedConnectInput",
    "ConnectorMergeDiscriminatedConnectInputConnectInput",
    "ConnectorMootaDiscriminatedConnectInput",
    "ConnectorOnebrickDiscriminatedConnectInput",
    "ConnectorOnebrickDiscriminatedConnectInputConnectInput",
    "ConnectorOpenledgerDiscriminatedConnectInput",
    "ConnectorPlaidDiscriminatedConnectInput",
    "ConnectorPlaidDiscriminatedConnectInputConnectInput",
    "ConnectorPlaidDiscriminatedConnectInputConnectInputLinkToken",
    "ConnectorPlaidDiscriminatedConnectInputConnectInputPublicToken",
    "ConnectorPostgresDiscriminatedConnectInput",
    "ConnectorRampDiscriminatedConnectInput",
    "ConnectorRampDiscriminatedConnectInputConnectInput",
    "ConnectorSaltedgeDiscriminatedConnectInput",
    "ConnectorSharepointOnpremDiscriminatedConnectInput",
    "ConnectorSlackAgentDiscriminatedConnectInput",
    "ConnectorSlackAgentDiscriminatedConnectInputConnectInput",
    "ConnectorSplitwiseDiscriminatedConnectInput",
    "ConnectorStripeDiscriminatedConnectInput",
    "ConnectorTellerDiscriminatedConnectInput",
    "ConnectorTellerDiscriminatedConnectInputConnectInput",
    "ConnectorTogglDiscriminatedConnectInput",
    "ConnectorTogglDiscriminatedConnectInputConnectInput",
    "ConnectorTwentyDiscriminatedConnectInput",
    "ConnectorVenmoDiscriminatedConnectInput",
    "ConnectorWiseDiscriminatedConnectInput",
    "ConnectorWiseDiscriminatedConnectInputConnectInput",
    "ConnectorYodleeDiscriminatedConnectInput",
    "ConnectorYodleeDiscriminatedConnectInputConnectInput",
    "ConnectorYodleeDiscriminatedConnectInputConnectInputAccessToken",
]


class ConnectorAcceloDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAcceloDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAcceloDiscriminatedConnectInputConnectInput

    connector_name: Literal["accelo"]


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


class ConnectorAdobeDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAdobeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAdobeDiscriminatedConnectInputConnectInput

    connector_name: Literal["adobe"]


class ConnectorAdyenDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAdyenDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAdyenDiscriminatedConnectInputConnectInput

    connector_name: Literal["adyen"]


class ConnectorAircallDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAircallDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAircallDiscriminatedConnectInputConnectInput

    connector_name: Literal["aircall"]


class ConnectorAmazonDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAmazonDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAmazonDiscriminatedConnectInputConnectInput

    connector_name: Literal["amazon"]


class ConnectorApaleoDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorApaleoDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorApaleoDiscriminatedConnectInputConnectInput

    connector_name: Literal["apaleo"]


class ConnectorAsanaDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAsanaDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAsanaDiscriminatedConnectInputConnectInput

    connector_name: Literal["asana"]


class ConnectorAttioDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAttioDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAttioDiscriminatedConnectInputConnectInput

    connector_name: Literal["attio"]


class ConnectorAuth0DiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAuth0DiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAuth0DiscriminatedConnectInputConnectInput

    connector_name: Literal["auth0"]


class ConnectorAutodeskDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAutodeskDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAutodeskDiscriminatedConnectInputConnectInput

    connector_name: Literal["autodesk"]


class ConnectorAwsDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorAwsDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorAwsDiscriminatedConnectInputConnectInput

    connector_name: Literal["aws"]


class ConnectorBamboohrDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBamboohrDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBamboohrDiscriminatedConnectInputConnectInput

    connector_name: Literal["bamboohr"]


class ConnectorBasecampDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBasecampDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBasecampDiscriminatedConnectInputConnectInput

    connector_name: Literal["basecamp"]


class ConnectorBattlenetDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBattlenetDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBattlenetDiscriminatedConnectInputConnectInput

    connector_name: Literal["battlenet"]


class ConnectorBigcommerceDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBigcommerceDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBigcommerceDiscriminatedConnectInputConnectInput

    connector_name: Literal["bigcommerce"]


class ConnectorBitbucketDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBitbucketDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBitbucketDiscriminatedConnectInputConnectInput

    connector_name: Literal["bitbucket"]


class ConnectorBitlyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBitlyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBitlyDiscriminatedConnectInputConnectInput

    connector_name: Literal["bitly"]


class ConnectorBlackbaudDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBlackbaudDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBlackbaudDiscriminatedConnectInputConnectInput

    connector_name: Literal["blackbaud"]


class ConnectorBoldsignDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBoldsignDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBoldsignDiscriminatedConnectInputConnectInput

    connector_name: Literal["boldsign"]


class ConnectorBoxDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBoxDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBoxDiscriminatedConnectInputConnectInput

    connector_name: Literal["box"]


class ConnectorBraintreeDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorBraintreeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorBraintreeDiscriminatedConnectInputConnectInput

    connector_name: Literal["braintree"]


class ConnectorCalendlyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorCalendlyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorCalendlyDiscriminatedConnectInputConnectInput

    connector_name: Literal["calendly"]


class ConnectorClickupDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorClickupDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorClickupDiscriminatedConnectInputConnectInput

    connector_name: Literal["clickup"]


class ConnectorCloseDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorCloseDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorCloseDiscriminatedConnectInputConnectInput

    connector_name: Literal["close"]


class ConnectorConfluenceDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorConfluenceDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorConfluenceDiscriminatedConnectInputConnectInput

    connector_name: Literal["confluence"]


class ConnectorContentfulDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorContentfulDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorContentfulDiscriminatedConnectInputConnectInput

    connector_name: Literal["contentful"]


class ConnectorContentstackDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorContentstackDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorContentstackDiscriminatedConnectInputConnectInput

    connector_name: Literal["contentstack"]


class ConnectorCopperDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorCopperDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorCopperDiscriminatedConnectInputConnectInput

    connector_name: Literal["copper"]


class ConnectorCorosDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorCorosDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorCorosDiscriminatedConnectInputConnectInput

    connector_name: Literal["coros"]


class ConnectorDatevDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDatevDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDatevDiscriminatedConnectInputConnectInput

    connector_name: Literal["datev"]


class ConnectorDeelDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDeelDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDeelDiscriminatedConnectInputConnectInput

    connector_name: Literal["deel"]


class ConnectorDialpadDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDialpadDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDialpadDiscriminatedConnectInputConnectInput

    connector_name: Literal["dialpad"]


class ConnectorDigitaloceanDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDigitaloceanDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDigitaloceanDiscriminatedConnectInputConnectInput

    connector_name: Literal["digitalocean"]


class ConnectorDiscordDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDiscordDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDiscordDiscriminatedConnectInputConnectInput

    connector_name: Literal["discord"]


class ConnectorDocusignDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDocusignDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDocusignDiscriminatedConnectInputConnectInput

    connector_name: Literal["docusign"]


class ConnectorDropboxDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorDropboxDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorDropboxDiscriminatedConnectInputConnectInput

    connector_name: Literal["dropbox"]


class ConnectorEbayDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorEbayDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorEbayDiscriminatedConnectInputConnectInput

    connector_name: Literal["ebay"]


class ConnectorEgnyteDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorEgnyteDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorEgnyteDiscriminatedConnectInputConnectInput

    connector_name: Literal["egnyte"]


class ConnectorEnvoyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorEnvoyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorEnvoyDiscriminatedConnectInputConnectInput

    connector_name: Literal["envoy"]


class ConnectorEventbriteDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorEventbriteDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorEventbriteDiscriminatedConnectInputConnectInput

    connector_name: Literal["eventbrite"]


class ConnectorExistDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorExistDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorExistDiscriminatedConnectInputConnectInput

    connector_name: Literal["exist"]


class ConnectorFacebookDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFacebookDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFacebookDiscriminatedConnectInputConnectInput

    connector_name: Literal["facebook"]


class ConnectorFactorialDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFactorialDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFactorialDiscriminatedConnectInputConnectInput

    connector_name: Literal["factorial"]


class ConnectorFigmaDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFigmaDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFigmaDiscriminatedConnectInputConnectInput

    connector_name: Literal["figma"]


class ConnectorFitbitDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFitbitDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFitbitDiscriminatedConnectInputConnectInput

    connector_name: Literal["fitbit"]


class ConnectorFortnoxDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFortnoxDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFortnoxDiscriminatedConnectInputConnectInput

    connector_name: Literal["fortnox"]


class ConnectorFreshbooksDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFreshbooksDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFreshbooksDiscriminatedConnectInputConnectInput

    connector_name: Literal["freshbooks"]


class ConnectorFrontDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorFrontDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFrontDiscriminatedConnectInputConnectInput

    connector_name: Literal["front"]


class ConnectorGitHubDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGitHubDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGitHubDiscriminatedConnectInputConnectInput

    connector_name: Literal["github"]


class ConnectorGitlabDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGitlabDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGitlabDiscriminatedConnectInputConnectInput

    connector_name: Literal["gitlab"]


class ConnectorGongDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGongDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGongDiscriminatedConnectInputConnectInput

    connector_name: Literal["gong"]


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


class ConnectorGorgiasDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGorgiasDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGorgiasDiscriminatedConnectInputConnectInput

    connector_name: Literal["gorgias"]


class ConnectorGrainDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGrainDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGrainDiscriminatedConnectInputConnectInput

    connector_name: Literal["grain"]


class ConnectorGumroadDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGumroadDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGumroadDiscriminatedConnectInputConnectInput

    connector_name: Literal["gumroad"]


class ConnectorGustoDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorGustoDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorGustoDiscriminatedConnectInputConnectInput

    connector_name: Literal["gusto"]


class ConnectorHarvestDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorHarvestDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorHarvestDiscriminatedConnectInputConnectInput

    connector_name: Literal["harvest"]


class ConnectorHighlevelDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorHighlevelDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorHighlevelDiscriminatedConnectInputConnectInput

    connector_name: Literal["highlevel"]


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


class ConnectorIntercomDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorIntercomDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorIntercomDiscriminatedConnectInputConnectInput

    connector_name: Literal["intercom"]


class ConnectorJiraDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorJiraDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorJiraDiscriminatedConnectInputConnectInput

    connector_name: Literal["jira"]


class ConnectorKeapDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorKeapDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorKeapDiscriminatedConnectInputConnectInput

    connector_name: Literal["keap"]


class ConnectorLeverDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorLeverDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorLeverDiscriminatedConnectInputConnectInput

    connector_name: Literal["lever"]


class ConnectorLinearDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorLinearDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorLinearDiscriminatedConnectInputConnectInput

    connector_name: Literal["linear"]


class ConnectorLinkedinDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorLinkedinDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorLinkedinDiscriminatedConnectInputConnectInput

    connector_name: Literal["linkedin"]


class ConnectorLinkhutDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorLinkhutDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorLinkhutDiscriminatedConnectInputConnectInput

    connector_name: Literal["linkhut"]


class ConnectorMailchimpDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorMailchimpDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorMailchimpDiscriminatedConnectInputConnectInput

    connector_name: Literal["mailchimp"]


class ConnectorMiroDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorMiroDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorMiroDiscriminatedConnectInputConnectInput

    connector_name: Literal["miro"]


class ConnectorMondayDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorMondayDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorMondayDiscriminatedConnectInputConnectInput

    connector_name: Literal["monday"]


class ConnectorMuralDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorMuralDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorMuralDiscriminatedConnectInputConnectInput

    connector_name: Literal["mural"]


class ConnectorNamelyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorNamelyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorNamelyDiscriminatedConnectInputConnectInput

    connector_name: Literal["namely"]


class ConnectorNationbuilderDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorNationbuilderDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorNationbuilderDiscriminatedConnectInputConnectInput

    connector_name: Literal["nationbuilder"]


class ConnectorNetsuiteDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorNetsuiteDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorNetsuiteDiscriminatedConnectInputConnectInput

    connector_name: Literal["netsuite"]


class ConnectorNotionDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorNotionDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorNotionDiscriminatedConnectInputConnectInput

    connector_name: Literal["notion"]


class ConnectorOdooDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorOdooDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOdooDiscriminatedConnectInputConnectInput

    connector_name: Literal["odoo"]


class ConnectorOktaDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorOktaDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOktaDiscriminatedConnectInputConnectInput

    connector_name: Literal["okta"]


class ConnectorOsuDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorOsuDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOsuDiscriminatedConnectInputConnectInput

    connector_name: Literal["osu"]


class ConnectorOuraDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorOuraDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOuraDiscriminatedConnectInputConnectInput

    connector_name: Literal["oura"]


class ConnectorOutreachDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorOutreachDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOutreachDiscriminatedConnectInputConnectInput

    connector_name: Literal["outreach"]


class ConnectorPagerdutyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPagerdutyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPagerdutyDiscriminatedConnectInputConnectInput

    connector_name: Literal["pagerduty"]


class ConnectorPandadocDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPandadocDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPandadocDiscriminatedConnectInputConnectInput

    connector_name: Literal["pandadoc"]


class ConnectorPayfitDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPayfitDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPayfitDiscriminatedConnectInputConnectInput

    connector_name: Literal["payfit"]


class ConnectorPaypalDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPaypalDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPaypalDiscriminatedConnectInputConnectInput

    connector_name: Literal["paypal"]


class ConnectorPennylaneDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPennylaneDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPennylaneDiscriminatedConnectInputConnectInput

    connector_name: Literal["pennylane"]


class ConnectorPinterestDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPinterestDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPinterestDiscriminatedConnectInputConnectInput

    connector_name: Literal["pinterest"]


class ConnectorPipedriveDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPipedriveDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPipedriveDiscriminatedConnectInputConnectInput

    connector_name: Literal["pipedrive"]


class ConnectorPodiumDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorPodiumDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorPodiumDiscriminatedConnectInputConnectInput

    connector_name: Literal["podium"]


class ConnectorProductboardDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorProductboardDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorProductboardDiscriminatedConnectInputConnectInput

    connector_name: Literal["productboard"]


class ConnectorQualtricsDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorQualtricsDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorQualtricsDiscriminatedConnectInputConnectInput

    connector_name: Literal["qualtrics"]


class ConnectorQuickbooksDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorQuickbooksDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorQuickbooksDiscriminatedConnectInputConnectInput

    connector_name: Literal["quickbooks"]


class ConnectorRedditDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorRedditDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorRedditDiscriminatedConnectInputConnectInput

    connector_name: Literal["reddit"]


class ConnectorSageDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSageDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSageDiscriminatedConnectInputConnectInput

    connector_name: Literal["sage"]


class ConnectorSalesforceDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSalesforceDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSalesforceDiscriminatedConnectInputConnectInput

    connector_name: Literal["salesforce"]


class ConnectorSalesloftDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSalesloftDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSalesloftDiscriminatedConnectInputConnectInput

    connector_name: Literal["salesloft"]


class ConnectorSegmentDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSegmentDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSegmentDiscriminatedConnectInputConnectInput

    connector_name: Literal["segment"]


class ConnectorServicem8DiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorServicem8DiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorServicem8DiscriminatedConnectInputConnectInput

    connector_name: Literal["servicem8"]


class ConnectorServicenowDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorServicenowDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorServicenowDiscriminatedConnectInputConnectInput

    connector_name: Literal["servicenow"]


class ConnectorSharepointDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSharepointDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSharepointDiscriminatedConnectInputConnectInput

    connector_name: Literal["sharepoint"]


class ConnectorShopifyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorShopifyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorShopifyDiscriminatedConnectInputConnectInput

    connector_name: Literal["shopify"]


class ConnectorSignnowDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSignnowDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSignnowDiscriminatedConnectInputConnectInput

    connector_name: Literal["signnow"]


class ConnectorSlackDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSlackDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSlackDiscriminatedConnectInputConnectInput

    connector_name: Literal["slack"]


class ConnectorSmartsheetDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSmartsheetDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSmartsheetDiscriminatedConnectInputConnectInput

    connector_name: Literal["smartsheet"]


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


class ConnectorSquarespaceDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSquarespaceDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSquarespaceDiscriminatedConnectInputConnectInput

    connector_name: Literal["squarespace"]


class ConnectorSquareupDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorSquareupDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSquareupDiscriminatedConnectInputConnectInput

    connector_name: Literal["squareup"]


class ConnectorStackexchangeDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorStackexchangeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorStackexchangeDiscriminatedConnectInputConnectInput

    connector_name: Literal["stackexchange"]


class ConnectorStravaDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorStravaDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorStravaDiscriminatedConnectInputConnectInput

    connector_name: Literal["strava"]


class ConnectorTeamworkDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTeamworkDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTeamworkDiscriminatedConnectInputConnectInput

    connector_name: Literal["teamwork"]


class ConnectorTicktickDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTicktickDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTicktickDiscriminatedConnectInputConnectInput

    connector_name: Literal["ticktick"]


class ConnectorTimelyDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTimelyDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTimelyDiscriminatedConnectInputConnectInput

    connector_name: Literal["timely"]


class ConnectorTodoistDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTodoistDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTodoistDiscriminatedConnectInputConnectInput

    connector_name: Literal["todoist"]


class ConnectorTremendousDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTremendousDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTremendousDiscriminatedConnectInputConnectInput

    connector_name: Literal["tremendous"]


class ConnectorTsheetsteamDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTsheetsteamDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTsheetsteamDiscriminatedConnectInputConnectInput

    connector_name: Literal["tsheetsteam"]


class ConnectorTumblrDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTumblrDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTumblrDiscriminatedConnectInputConnectInput

    connector_name: Literal["tumblr"]


class ConnectorTwinfieldDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTwinfieldDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTwinfieldDiscriminatedConnectInputConnectInput

    connector_name: Literal["twinfield"]


class ConnectorTwitchDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTwitchDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTwitchDiscriminatedConnectInputConnectInput

    connector_name: Literal["twitch"]


class ConnectorTwitterDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTwitterDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTwitterDiscriminatedConnectInputConnectInput

    connector_name: Literal["twitter"]


class ConnectorTypeformDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorTypeformDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTypeformDiscriminatedConnectInputConnectInput

    connector_name: Literal["typeform"]


class ConnectorUberDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorUberDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorUberDiscriminatedConnectInputConnectInput

    connector_name: Literal["uber"]


class ConnectorVimeoDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorVimeoDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorVimeoDiscriminatedConnectInputConnectInput

    connector_name: Literal["vimeo"]


class ConnectorWakatimeDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorWakatimeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorWakatimeDiscriminatedConnectInputConnectInput

    connector_name: Literal["wakatime"]


class ConnectorWealthboxDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorWealthboxDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorWealthboxDiscriminatedConnectInputConnectInput

    connector_name: Literal["wealthbox"]


class ConnectorWebflowDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorWebflowDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorWebflowDiscriminatedConnectInputConnectInput

    connector_name: Literal["webflow"]


class ConnectorWhoopDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorWhoopDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorWhoopDiscriminatedConnectInputConnectInput

    connector_name: Literal["whoop"]


class ConnectorWordpressDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorWordpressDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorWordpressDiscriminatedConnectInputConnectInput

    connector_name: Literal["wordpress"]


class ConnectorWrikeDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorWrikeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorWrikeDiscriminatedConnectInputConnectInput

    connector_name: Literal["wrike"]


class ConnectorXeroDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorXeroDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorXeroDiscriminatedConnectInputConnectInput

    connector_name: Literal["xero"]


class ConnectorYahooDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorYahooDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorYahooDiscriminatedConnectInputConnectInput

    connector_name: Literal["yahoo"]


class ConnectorYandexDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorYandexDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorYandexDiscriminatedConnectInputConnectInput

    connector_name: Literal["yandex"]


class ConnectorZapierDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZapierDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZapierDiscriminatedConnectInputConnectInput

    connector_name: Literal["zapier"]


class ConnectorZendeskDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZendeskDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZendeskDiscriminatedConnectInputConnectInput

    connector_name: Literal["zendesk"]


class ConnectorZenefitsDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZenefitsDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZenefitsDiscriminatedConnectInputConnectInput

    connector_name: Literal["zenefits"]


class ConnectorZohoDeskDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZohoDeskDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZohoDeskDiscriminatedConnectInputConnectInput

    connector_name: Literal["zoho-desk"]


class ConnectorZohoDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZohoDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZohoDiscriminatedConnectInputConnectInput

    connector_name: Literal["zoho"]


class ConnectorZoomDiscriminatedConnectInputConnectInput(BaseModel):
    authorization_url: str
    """URL to take user to for approval"""

    code_verifier: Optional[str] = None
    """Code verifier for PKCE"""


class ConnectorZoomDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorZoomDiscriminatedConnectInputConnectInput

    connector_name: Literal["zoom"]


class ConnectorAirtableDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["airtable"]


class ConnectorApolloDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["apollo"]


class ConnectorBrexDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["brex"]


class ConnectorCodaDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["coda"]


class ConnectorFinchDiscriminatedConnectInputConnectInput(BaseModel):
    client_id: str

    products: List[
        Literal["company", "directory", "individual", "ssn", "employment", "payment", "pay_statement", "benefits"]
    ]


class ConnectorFinchDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorFinchDiscriminatedConnectInputConnectInput

    connector_name: Literal["finch"]


class ConnectorFirebaseDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["firebase"]


class ConnectorForeceiptDiscriminatedConnectInputConnectInput(BaseModel):
    env_name: Literal["staging", "production"] = FieldInfo(alias="envName")

    api_id: Optional[object] = FieldInfo(alias="_id", default=None)

    credentials: Optional[object] = None


class ConnectorForeceiptDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorForeceiptDiscriminatedConnectInputConnectInput

    connector_name: Literal["foreceipt"]


class ConnectorGreenhouseDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["greenhouse"]


class ConnectorHeronDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["heron"]


class ConnectorLunchmoneyDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["lunchmoney"]


class ConnectorMercuryDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["mercury"]


class ConnectorMergeDiscriminatedConnectInputConnectInput(BaseModel):
    link_token: str


class ConnectorMergeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorMergeDiscriminatedConnectInputConnectInput

    connector_name: Literal["merge"]


class ConnectorMootaDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["moota"]


class ConnectorOnebrickDiscriminatedConnectInputConnectInput(BaseModel):
    public_token: Optional[str] = FieldInfo(alias="publicToken", default=None)

    redirect_url: Optional[str] = None


class ConnectorOnebrickDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorOnebrickDiscriminatedConnectInputConnectInput

    connector_name: Literal["onebrick"]


class ConnectorOpenledgerDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["openledger"]


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


class ConnectorRampDiscriminatedConnectInputConnectInput(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)


class ConnectorRampDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorRampDiscriminatedConnectInputConnectInput

    connector_name: Literal["ramp"]


class ConnectorSaltedgeDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["saltedge"]


class ConnectorSharepointOnpremDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["sharepoint-onprem"]


class ConnectorSlackAgentDiscriminatedConnectInputConnectInput(BaseModel):
    configuration_url: str
    """Configuration URL - https://api.slack.com/apps/A1234567890/oauth..."""


class ConnectorSlackAgentDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorSlackAgentDiscriminatedConnectInputConnectInput

    connector_name: Literal["slack-agent"]


class ConnectorSplitwiseDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["splitwise"]


class ConnectorStripeDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["stripe"]


class ConnectorTellerDiscriminatedConnectInputConnectInput(BaseModel):
    application_id: str = FieldInfo(alias="applicationId")

    user_token: Optional[str] = FieldInfo(alias="userToken", default=None)


class ConnectorTellerDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTellerDiscriminatedConnectInputConnectInput

    connector_name: Literal["teller"]


class ConnectorTogglDiscriminatedConnectInputConnectInput(BaseModel):
    api_token: str = FieldInfo(alias="apiToken")


class ConnectorTogglDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorTogglDiscriminatedConnectInputConnectInput

    connector_name: Literal["toggl"]


class ConnectorTwentyDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["twenty"]


class ConnectorVenmoDiscriminatedConnectInput(BaseModel):
    connect_input: object

    connector_name: Literal["venmo"]


class ConnectorWiseDiscriminatedConnectInputConnectInput(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    env_name: Literal["sandbox", "live"] = FieldInfo(alias="envName")

    redirect_uri: str = FieldInfo(alias="redirectUri")


class ConnectorWiseDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorWiseDiscriminatedConnectInputConnectInput

    connector_name: Literal["wise"]


class ConnectorYodleeDiscriminatedConnectInputConnectInputAccessToken(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    expires_in: float = FieldInfo(alias="expiresIn")

    issued_at: str = FieldInfo(alias="issuedAt")


class ConnectorYodleeDiscriminatedConnectInputConnectInput(BaseModel):
    access_token: ConnectorYodleeDiscriminatedConnectInputConnectInputAccessToken = FieldInfo(alias="accessToken")

    env_name: Literal["sandbox", "development", "production"] = FieldInfo(alias="envName")


class ConnectorYodleeDiscriminatedConnectInput(BaseModel):
    connect_input: ConnectorYodleeDiscriminatedConnectInputConnectInput

    connector_name: Literal["yodlee"]


PreConnectResponse: TypeAlias = Annotated[
    Union[
        ConnectorAcceloDiscriminatedConnectInput,
        ConnectorAcmeApikeyDiscriminatedConnectInput,
        ConnectorAcmeOauth2DiscriminatedConnectInput,
        ConnectorAdobeDiscriminatedConnectInput,
        ConnectorAdyenDiscriminatedConnectInput,
        ConnectorAircallDiscriminatedConnectInput,
        ConnectorAmazonDiscriminatedConnectInput,
        ConnectorApaleoDiscriminatedConnectInput,
        ConnectorAsanaDiscriminatedConnectInput,
        ConnectorAttioDiscriminatedConnectInput,
        ConnectorAuth0DiscriminatedConnectInput,
        ConnectorAutodeskDiscriminatedConnectInput,
        ConnectorAwsDiscriminatedConnectInput,
        ConnectorBamboohrDiscriminatedConnectInput,
        ConnectorBasecampDiscriminatedConnectInput,
        ConnectorBattlenetDiscriminatedConnectInput,
        ConnectorBigcommerceDiscriminatedConnectInput,
        ConnectorBitbucketDiscriminatedConnectInput,
        ConnectorBitlyDiscriminatedConnectInput,
        ConnectorBlackbaudDiscriminatedConnectInput,
        ConnectorBoldsignDiscriminatedConnectInput,
        ConnectorBoxDiscriminatedConnectInput,
        ConnectorBraintreeDiscriminatedConnectInput,
        ConnectorCalendlyDiscriminatedConnectInput,
        ConnectorClickupDiscriminatedConnectInput,
        ConnectorCloseDiscriminatedConnectInput,
        ConnectorConfluenceDiscriminatedConnectInput,
        ConnectorContentfulDiscriminatedConnectInput,
        ConnectorContentstackDiscriminatedConnectInput,
        ConnectorCopperDiscriminatedConnectInput,
        ConnectorCorosDiscriminatedConnectInput,
        ConnectorDatevDiscriminatedConnectInput,
        ConnectorDeelDiscriminatedConnectInput,
        ConnectorDialpadDiscriminatedConnectInput,
        ConnectorDigitaloceanDiscriminatedConnectInput,
        ConnectorDiscordDiscriminatedConnectInput,
        ConnectorDocusignDiscriminatedConnectInput,
        ConnectorDropboxDiscriminatedConnectInput,
        ConnectorEbayDiscriminatedConnectInput,
        ConnectorEgnyteDiscriminatedConnectInput,
        ConnectorEnvoyDiscriminatedConnectInput,
        ConnectorEventbriteDiscriminatedConnectInput,
        ConnectorExistDiscriminatedConnectInput,
        ConnectorFacebookDiscriminatedConnectInput,
        ConnectorFactorialDiscriminatedConnectInput,
        ConnectorFigmaDiscriminatedConnectInput,
        ConnectorFitbitDiscriminatedConnectInput,
        ConnectorFortnoxDiscriminatedConnectInput,
        ConnectorFreshbooksDiscriminatedConnectInput,
        ConnectorFrontDiscriminatedConnectInput,
        ConnectorGitHubDiscriminatedConnectInput,
        ConnectorGitlabDiscriminatedConnectInput,
        ConnectorGongDiscriminatedConnectInput,
        ConnectorGoogleCalendarDiscriminatedConnectInput,
        ConnectorGoogleDocsDiscriminatedConnectInput,
        ConnectorGoogleDriveDiscriminatedConnectInput,
        ConnectorGoogleMailDiscriminatedConnectInput,
        ConnectorGoogleSheetDiscriminatedConnectInput,
        ConnectorGorgiasDiscriminatedConnectInput,
        ConnectorGrainDiscriminatedConnectInput,
        ConnectorGumroadDiscriminatedConnectInput,
        ConnectorGustoDiscriminatedConnectInput,
        ConnectorHarvestDiscriminatedConnectInput,
        ConnectorHighlevelDiscriminatedConnectInput,
        ConnectorHubspotDiscriminatedConnectInput,
        ConnectorInstagramDiscriminatedConnectInput,
        ConnectorIntercomDiscriminatedConnectInput,
        ConnectorJiraDiscriminatedConnectInput,
        ConnectorKeapDiscriminatedConnectInput,
        ConnectorLeverDiscriminatedConnectInput,
        ConnectorLinearDiscriminatedConnectInput,
        ConnectorLinkedinDiscriminatedConnectInput,
        ConnectorLinkhutDiscriminatedConnectInput,
        ConnectorMailchimpDiscriminatedConnectInput,
        ConnectorMiroDiscriminatedConnectInput,
        ConnectorMondayDiscriminatedConnectInput,
        ConnectorMuralDiscriminatedConnectInput,
        ConnectorNamelyDiscriminatedConnectInput,
        ConnectorNationbuilderDiscriminatedConnectInput,
        ConnectorNetsuiteDiscriminatedConnectInput,
        ConnectorNotionDiscriminatedConnectInput,
        ConnectorOdooDiscriminatedConnectInput,
        ConnectorOktaDiscriminatedConnectInput,
        ConnectorOsuDiscriminatedConnectInput,
        ConnectorOuraDiscriminatedConnectInput,
        ConnectorOutreachDiscriminatedConnectInput,
        ConnectorPagerdutyDiscriminatedConnectInput,
        ConnectorPandadocDiscriminatedConnectInput,
        ConnectorPayfitDiscriminatedConnectInput,
        ConnectorPaypalDiscriminatedConnectInput,
        ConnectorPennylaneDiscriminatedConnectInput,
        ConnectorPinterestDiscriminatedConnectInput,
        ConnectorPipedriveDiscriminatedConnectInput,
        ConnectorPodiumDiscriminatedConnectInput,
        ConnectorProductboardDiscriminatedConnectInput,
        ConnectorQualtricsDiscriminatedConnectInput,
        ConnectorQuickbooksDiscriminatedConnectInput,
        ConnectorRedditDiscriminatedConnectInput,
        ConnectorSageDiscriminatedConnectInput,
        ConnectorSalesforceDiscriminatedConnectInput,
        ConnectorSalesloftDiscriminatedConnectInput,
        ConnectorSegmentDiscriminatedConnectInput,
        ConnectorServicem8DiscriminatedConnectInput,
        ConnectorServicenowDiscriminatedConnectInput,
        ConnectorSharepointDiscriminatedConnectInput,
        ConnectorShopifyDiscriminatedConnectInput,
        ConnectorSignnowDiscriminatedConnectInput,
        ConnectorSlackDiscriminatedConnectInput,
        ConnectorSmartsheetDiscriminatedConnectInput,
        ConnectorSnowflakeDiscriminatedConnectInput,
        ConnectorSpotifyDiscriminatedConnectInput,
        ConnectorSquarespaceDiscriminatedConnectInput,
        ConnectorSquareupDiscriminatedConnectInput,
        ConnectorStackexchangeDiscriminatedConnectInput,
        ConnectorStravaDiscriminatedConnectInput,
        ConnectorTeamworkDiscriminatedConnectInput,
        ConnectorTicktickDiscriminatedConnectInput,
        ConnectorTimelyDiscriminatedConnectInput,
        ConnectorTodoistDiscriminatedConnectInput,
        ConnectorTremendousDiscriminatedConnectInput,
        ConnectorTsheetsteamDiscriminatedConnectInput,
        ConnectorTumblrDiscriminatedConnectInput,
        ConnectorTwinfieldDiscriminatedConnectInput,
        ConnectorTwitchDiscriminatedConnectInput,
        ConnectorTwitterDiscriminatedConnectInput,
        ConnectorTypeformDiscriminatedConnectInput,
        ConnectorUberDiscriminatedConnectInput,
        ConnectorVimeoDiscriminatedConnectInput,
        ConnectorWakatimeDiscriminatedConnectInput,
        ConnectorWealthboxDiscriminatedConnectInput,
        ConnectorWebflowDiscriminatedConnectInput,
        ConnectorWhoopDiscriminatedConnectInput,
        ConnectorWordpressDiscriminatedConnectInput,
        ConnectorWrikeDiscriminatedConnectInput,
        ConnectorXeroDiscriminatedConnectInput,
        ConnectorYahooDiscriminatedConnectInput,
        ConnectorYandexDiscriminatedConnectInput,
        ConnectorZapierDiscriminatedConnectInput,
        ConnectorZendeskDiscriminatedConnectInput,
        ConnectorZenefitsDiscriminatedConnectInput,
        ConnectorZohoDeskDiscriminatedConnectInput,
        ConnectorZohoDiscriminatedConnectInput,
        ConnectorZoomDiscriminatedConnectInput,
        ConnectorAirtableDiscriminatedConnectInput,
        ConnectorApolloDiscriminatedConnectInput,
        ConnectorBrexDiscriminatedConnectInput,
        ConnectorCodaDiscriminatedConnectInput,
        ConnectorFinchDiscriminatedConnectInput,
        ConnectorFirebaseDiscriminatedConnectInput,
        ConnectorForeceiptDiscriminatedConnectInput,
        ConnectorGreenhouseDiscriminatedConnectInput,
        ConnectorHeronDiscriminatedConnectInput,
        ConnectorLunchmoneyDiscriminatedConnectInput,
        ConnectorMercuryDiscriminatedConnectInput,
        ConnectorMergeDiscriminatedConnectInput,
        ConnectorMootaDiscriminatedConnectInput,
        ConnectorOnebrickDiscriminatedConnectInput,
        ConnectorOpenledgerDiscriminatedConnectInput,
        ConnectorPlaidDiscriminatedConnectInput,
        ConnectorPostgresDiscriminatedConnectInput,
        ConnectorRampDiscriminatedConnectInput,
        ConnectorSaltedgeDiscriminatedConnectInput,
        ConnectorSharepointOnpremDiscriminatedConnectInput,
        ConnectorSlackAgentDiscriminatedConnectInput,
        ConnectorSplitwiseDiscriminatedConnectInput,
        ConnectorStripeDiscriminatedConnectInput,
        ConnectorTellerDiscriminatedConnectInput,
        ConnectorTogglDiscriminatedConnectInput,
        ConnectorTwentyDiscriminatedConnectInput,
        ConnectorVenmoDiscriminatedConnectInput,
        ConnectorWiseDiscriminatedConnectInput,
        ConnectorYodleeDiscriminatedConnectInput,
    ],
    PropertyInfo(discriminator="connector_name"),
]
