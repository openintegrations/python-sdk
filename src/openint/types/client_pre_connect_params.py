# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ClientPreConnectParams",
    "DiscriminatedData",
    "DiscriminatedDataConnectorAcceloDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAcceloDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAcmeApikeyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAdobeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAdobeDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAdyenDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAdyenDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAircallDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAircallDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAmazonDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAmazonDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorApaleoDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorApaleoDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAttioDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAttioDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAuth0DiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAuth0DiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAutodeskDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAutodeskDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAwsDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorAwsDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBamboohrDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBamboohrDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBasecampDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBasecampDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBattlenetDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBattlenetDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBigcommerceDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBigcommerceDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBitbucketDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBitbucketDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBitlyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBitlyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBlackbaudDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBlackbaudDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBoldsignDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBoldsignDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBoxDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBoxDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorBraintreeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBraintreeDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorClickupDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorClickupDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorCloseDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorCloseDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorContentfulDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorContentfulDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorContentstackDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorContentstackDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorCopperDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorCopperDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorCorosDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorCorosDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDatevDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDatevDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDeelDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDeelDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDialpadDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDialpadDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDigitaloceanDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDigitaloceanDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDocusignDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDocusignDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorEbayDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorEbayDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorEgnyteDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorEgnyteDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorEnvoyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorEnvoyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorEventbriteDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorEventbriteDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorExistDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorExistDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFacebookDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFacebookDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFactorialDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFactorialDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFitbitDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFitbitDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFortnoxDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFortnoxDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFreshbooksDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFreshbooksDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFrontDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFrontDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGitlabDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGitlabDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGongDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGongDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGorgiasDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGorgiasDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGrainDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGrainDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGumroadDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGumroadDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorGustoDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGustoDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorHarvestDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorHarvestDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorHighlevelDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorHighlevelDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorIntercomDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorIntercomDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorJiraDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorJiraDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorKeapDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorKeapDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorLeverDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorLeverDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorLinearDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorLinearDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorLinkedinDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorLinkedinDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorLinkhutDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorLinkhutDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorMailchimpDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMailchimpDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorMiroDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMiroDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorMondayDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMondayDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorMuralDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMuralDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorNamelyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorNamelyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorNationbuilderDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorNationbuilderDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorNetsuiteDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorNetsuiteDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorNotionDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorNotionDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorOdooDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOdooDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorOktaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOktaDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorOsuDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOsuDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorOuraDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOuraDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorOutreachDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOutreachDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPagerdutyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPagerdutyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPandadocDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPandadocDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPayfitDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPayfitDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPaypalDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPaypalDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPennylaneDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPennylaneDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPinterestDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPinterestDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPipedriveDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPipedriveDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPodiumDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPodiumDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorProductboardDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorProductboardDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorQualtricsDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorQualtricsDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorQuickbooksDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorQuickbooksDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorRedditDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorRedditDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSageDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSageDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSalesloftDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSalesloftDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSegmentDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSegmentDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorServicem8DiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorServicem8DiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorServicenowDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorServicenowDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorShopifyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorShopifyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSignnowDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSignnowDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSlackDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSlackDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSmartsheetDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSmartsheetDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSquarespaceDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSquarespaceDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorSquareupDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSquareupDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorStackexchangeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorStackexchangeDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorStravaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorStravaDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTeamworkDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTeamworkDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTicktickDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTicktickDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTimelyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTimelyDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTodoistDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTodoistDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTremendousDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTremendousDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTsheetsteamDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTsheetsteamDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTumblrDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTumblrDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTwinfieldDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTwinfieldDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTwitchDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTwitchDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTwitterDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTwitterDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorTypeformDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTypeformDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorUberDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorUberDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorVimeoDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorVimeoDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorWakatimeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWakatimeDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorWealthboxDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWealthboxDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorWebflowDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWebflowDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorWhoopDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWhoopDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorWordpressDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWordpressDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorWrikeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWrikeDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorXeroDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorXeroDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorYahooDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorYahooDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorYandexDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorYandexDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorZapierDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZapierDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorZenefitsDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZenefitsDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorZohoDeskDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZohoDeskDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorZohoDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZohoDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorZoomDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorZoomDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorAirtableDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorApolloDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorBrexDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorCodaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFinchDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorFinchDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorFirebaseDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorForeceiptDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorGreenhouseDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorHeronDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorLunchmoneyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMercuryDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMergeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorMergeDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorMootaDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOnebrickDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorOpenledgerDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInputPreConnectInput",
    "DiscriminatedDataConnectorPostgresDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorRampDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSaltedgeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSharepointOnpremDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSlackAgentDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorSplitwiseDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorStripeDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTellerDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTogglDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorTwentyDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorVenmoDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorWiseDiscriminatedPreConnectInput",
    "DiscriminatedDataConnectorYodleeDiscriminatedPreConnectInput",
    "Options",
]


class ClientPreConnectParams(TypedDict, total=False):
    connector_config_id: Required[str]
    """
    Must correspond to data.connector_name. Technically id should imply
    connector_name already but there is no way to specify a discriminated union with
    id alone.
    """

    discriminated_data: Required[DiscriminatedData]

    options: Required[Options]


class DiscriminatedDataConnectorAcceloDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAcceloDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["accelo"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAcceloDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAcmeApikeyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["acme-apikey"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["acme-oauth2"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAdobeDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAdobeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["adobe"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAdobeDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAdyenDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAdyenDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["adyen"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAdyenDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAircallDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAircallDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["aircall"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAircallDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAmazonDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAmazonDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["amazon"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAmazonDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorApaleoDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorApaleoDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["apaleo"]]

    pre_connect_input: Required[DiscriminatedDataConnectorApaleoDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["asana"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAttioDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAttioDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["attio"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAttioDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAuth0DiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAuth0DiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["auth0"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAuth0DiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAutodeskDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAutodeskDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["autodesk"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAutodeskDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAwsDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorAwsDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["aws"]]

    pre_connect_input: Required[DiscriminatedDataConnectorAwsDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBamboohrDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBamboohrDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["bamboohr"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBamboohrDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBasecampDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBasecampDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["basecamp"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBasecampDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBattlenetDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBattlenetDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["battlenet"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBattlenetDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBigcommerceDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBigcommerceDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["bigcommerce"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBigcommerceDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBitbucketDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBitbucketDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["bitbucket"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBitbucketDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBitlyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBitlyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["bitly"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBitlyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBlackbaudDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBlackbaudDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["blackbaud"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBlackbaudDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBoldsignDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBoldsignDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["boldsign"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBoldsignDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBoxDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBoxDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["box"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBoxDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorBraintreeDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorBraintreeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["braintree"]]

    pre_connect_input: Required[DiscriminatedDataConnectorBraintreeDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["calendly"]]

    pre_connect_input: Required[DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorClickupDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorClickupDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["clickup"]]

    pre_connect_input: Required[DiscriminatedDataConnectorClickupDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorCloseDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorCloseDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["close"]]

    pre_connect_input: Required[DiscriminatedDataConnectorCloseDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["confluence"]]

    pre_connect_input: Required[DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorContentfulDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorContentfulDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["contentful"]]

    pre_connect_input: Required[DiscriminatedDataConnectorContentfulDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorContentstackDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorContentstackDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["contentstack"]]

    pre_connect_input: Required[DiscriminatedDataConnectorContentstackDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorCopperDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorCopperDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["copper"]]

    pre_connect_input: Required[DiscriminatedDataConnectorCopperDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorCorosDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorCorosDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["coros"]]

    pre_connect_input: Required[DiscriminatedDataConnectorCorosDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDatevDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorDatevDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["datev"]]

    pre_connect_input: Required[DiscriminatedDataConnectorDatevDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDeelDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorDeelDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["deel"]]

    pre_connect_input: Required[DiscriminatedDataConnectorDeelDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDialpadDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorDialpadDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["dialpad"]]

    pre_connect_input: Required[DiscriminatedDataConnectorDialpadDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDigitaloceanDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorDigitaloceanDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["digitalocean"]]

    pre_connect_input: Required[DiscriminatedDataConnectorDigitaloceanDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["discord"]]

    pre_connect_input: Required[DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDocusignDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorDocusignDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["docusign"]]

    pre_connect_input: Required[DiscriminatedDataConnectorDocusignDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["dropbox"]]

    pre_connect_input: Required[DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorEbayDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorEbayDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["ebay"]]

    pre_connect_input: Required[DiscriminatedDataConnectorEbayDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorEgnyteDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorEgnyteDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["egnyte"]]

    pre_connect_input: Required[DiscriminatedDataConnectorEgnyteDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorEnvoyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorEnvoyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["envoy"]]

    pre_connect_input: Required[DiscriminatedDataConnectorEnvoyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorEventbriteDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorEventbriteDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["eventbrite"]]

    pre_connect_input: Required[DiscriminatedDataConnectorEventbriteDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorExistDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorExistDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["exist"]]

    pre_connect_input: Required[DiscriminatedDataConnectorExistDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFacebookDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorFacebookDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["facebook"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFacebookDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFactorialDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorFactorialDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["factorial"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFactorialDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["figma"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFitbitDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorFitbitDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["fitbit"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFitbitDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFortnoxDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorFortnoxDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["fortnox"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFortnoxDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFreshbooksDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorFreshbooksDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["freshbooks"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFreshbooksDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFrontDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorFrontDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["front"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFrontDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["github"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGitlabDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGitlabDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["gitlab"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGitlabDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGongDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGongDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["gong"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGongDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-calendar"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-docs"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-drive"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-mail"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["google-sheet"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGorgiasDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGorgiasDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["gorgias"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGorgiasDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGrainDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGrainDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["grain"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGrainDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGumroadDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGumroadDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["gumroad"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGumroadDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorGustoDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorGustoDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["gusto"]]

    pre_connect_input: Required[DiscriminatedDataConnectorGustoDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorHarvestDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorHarvestDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["harvest"]]

    pre_connect_input: Required[DiscriminatedDataConnectorHarvestDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorHighlevelDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorHighlevelDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["highlevel"]]

    pre_connect_input: Required[DiscriminatedDataConnectorHighlevelDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["hubspot"]]

    pre_connect_input: Required[DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["instagram"]]

    pre_connect_input: Required[DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorIntercomDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorIntercomDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["intercom"]]

    pre_connect_input: Required[DiscriminatedDataConnectorIntercomDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorJiraDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorJiraDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["jira"]]

    pre_connect_input: Required[DiscriminatedDataConnectorJiraDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorKeapDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorKeapDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["keap"]]

    pre_connect_input: Required[DiscriminatedDataConnectorKeapDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorLeverDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorLeverDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["lever"]]

    pre_connect_input: Required[DiscriminatedDataConnectorLeverDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorLinearDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorLinearDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["linear"]]

    pre_connect_input: Required[DiscriminatedDataConnectorLinearDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorLinkedinDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorLinkedinDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["linkedin"]]

    pre_connect_input: Required[DiscriminatedDataConnectorLinkedinDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorLinkhutDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorLinkhutDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["linkhut"]]

    pre_connect_input: Required[DiscriminatedDataConnectorLinkhutDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorMailchimpDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorMailchimpDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["mailchimp"]]

    pre_connect_input: Required[DiscriminatedDataConnectorMailchimpDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorMiroDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorMiroDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["miro"]]

    pre_connect_input: Required[DiscriminatedDataConnectorMiroDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorMondayDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorMondayDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["monday"]]

    pre_connect_input: Required[DiscriminatedDataConnectorMondayDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorMuralDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorMuralDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["mural"]]

    pre_connect_input: Required[DiscriminatedDataConnectorMuralDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorNamelyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorNamelyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["namely"]]

    pre_connect_input: Required[DiscriminatedDataConnectorNamelyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorNationbuilderDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorNationbuilderDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["nationbuilder"]]

    pre_connect_input: Required[DiscriminatedDataConnectorNationbuilderDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorNetsuiteDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorNetsuiteDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["netsuite"]]

    pre_connect_input: Required[DiscriminatedDataConnectorNetsuiteDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorNotionDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorNotionDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["notion"]]

    pre_connect_input: Required[DiscriminatedDataConnectorNotionDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorOdooDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorOdooDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["odoo"]]

    pre_connect_input: Required[DiscriminatedDataConnectorOdooDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorOktaDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorOktaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["okta"]]

    pre_connect_input: Required[DiscriminatedDataConnectorOktaDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorOsuDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorOsuDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["osu"]]

    pre_connect_input: Required[DiscriminatedDataConnectorOsuDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorOuraDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorOuraDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["oura"]]

    pre_connect_input: Required[DiscriminatedDataConnectorOuraDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorOutreachDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorOutreachDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["outreach"]]

    pre_connect_input: Required[DiscriminatedDataConnectorOutreachDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPagerdutyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPagerdutyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["pagerduty"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPagerdutyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPandadocDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPandadocDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["pandadoc"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPandadocDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPayfitDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPayfitDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["payfit"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPayfitDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPaypalDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPaypalDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["paypal"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPaypalDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPennylaneDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPennylaneDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["pennylane"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPennylaneDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPinterestDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPinterestDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["pinterest"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPinterestDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPipedriveDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPipedriveDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["pipedrive"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPipedriveDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorPodiumDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorPodiumDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["podium"]]

    pre_connect_input: Required[DiscriminatedDataConnectorPodiumDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorProductboardDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorProductboardDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["productboard"]]

    pre_connect_input: Required[DiscriminatedDataConnectorProductboardDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorQualtricsDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorQualtricsDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["qualtrics"]]

    pre_connect_input: Required[DiscriminatedDataConnectorQualtricsDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorQuickbooksDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorQuickbooksDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["quickbooks"]]

    pre_connect_input: Required[DiscriminatedDataConnectorQuickbooksDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorRedditDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorRedditDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["reddit"]]

    pre_connect_input: Required[DiscriminatedDataConnectorRedditDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSageDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSageDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["sage"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSageDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["salesforce"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSalesloftDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSalesloftDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["salesloft"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSalesloftDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSegmentDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSegmentDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["segment"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSegmentDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorServicem8DiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorServicem8DiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["servicem8"]]

    pre_connect_input: Required[DiscriminatedDataConnectorServicem8DiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorServicenowDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorServicenowDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["servicenow"]]

    pre_connect_input: Required[DiscriminatedDataConnectorServicenowDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["sharepoint"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorShopifyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorShopifyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["shopify"]]

    pre_connect_input: Required[DiscriminatedDataConnectorShopifyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSignnowDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSignnowDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["signnow"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSignnowDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSlackDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSlackDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["slack"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSlackDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSmartsheetDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSmartsheetDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["smartsheet"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSmartsheetDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["snowflake"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["spotify"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSquarespaceDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSquarespaceDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["squarespace"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSquarespaceDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorSquareupDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorSquareupDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["squareup"]]

    pre_connect_input: Required[DiscriminatedDataConnectorSquareupDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorStackexchangeDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorStackexchangeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["stackexchange"]]

    pre_connect_input: Required[DiscriminatedDataConnectorStackexchangeDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorStravaDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorStravaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["strava"]]

    pre_connect_input: Required[DiscriminatedDataConnectorStravaDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTeamworkDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTeamworkDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["teamwork"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTeamworkDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTicktickDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTicktickDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["ticktick"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTicktickDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTimelyDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTimelyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["timely"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTimelyDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTodoistDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTodoistDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["todoist"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTodoistDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTremendousDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTremendousDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["tremendous"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTremendousDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTsheetsteamDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTsheetsteamDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["tsheetsteam"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTsheetsteamDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTumblrDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTumblrDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["tumblr"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTumblrDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTwinfieldDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTwinfieldDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["twinfield"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTwinfieldDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTwitchDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTwitchDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["twitch"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTwitchDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTwitterDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTwitterDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["twitter"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTwitterDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorTypeformDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorTypeformDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["typeform"]]

    pre_connect_input: Required[DiscriminatedDataConnectorTypeformDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorUberDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorUberDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["uber"]]

    pre_connect_input: Required[DiscriminatedDataConnectorUberDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorVimeoDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorVimeoDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["vimeo"]]

    pre_connect_input: Required[DiscriminatedDataConnectorVimeoDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorWakatimeDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorWakatimeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["wakatime"]]

    pre_connect_input: Required[DiscriminatedDataConnectorWakatimeDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorWealthboxDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorWealthboxDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["wealthbox"]]

    pre_connect_input: Required[DiscriminatedDataConnectorWealthboxDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorWebflowDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorWebflowDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["webflow"]]

    pre_connect_input: Required[DiscriminatedDataConnectorWebflowDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorWhoopDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorWhoopDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["whoop"]]

    pre_connect_input: Required[DiscriminatedDataConnectorWhoopDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorWordpressDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorWordpressDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["wordpress"]]

    pre_connect_input: Required[DiscriminatedDataConnectorWordpressDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorWrikeDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorWrikeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["wrike"]]

    pre_connect_input: Required[DiscriminatedDataConnectorWrikeDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorXeroDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorXeroDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["xero"]]

    pre_connect_input: Required[DiscriminatedDataConnectorXeroDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorYahooDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorYahooDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["yahoo"]]

    pre_connect_input: Required[DiscriminatedDataConnectorYahooDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorYandexDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorYandexDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["yandex"]]

    pre_connect_input: Required[DiscriminatedDataConnectorYandexDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorZapierDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorZapierDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zapier"]]

    pre_connect_input: Required[DiscriminatedDataConnectorZapierDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zendesk"]]

    pre_connect_input: Required[DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorZenefitsDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorZenefitsDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zenefits"]]

    pre_connect_input: Required[DiscriminatedDataConnectorZenefitsDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorZohoDeskDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorZohoDeskDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zoho-desk"]]

    pre_connect_input: Required[DiscriminatedDataConnectorZohoDeskDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorZohoDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorZohoDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zoho"]]

    pre_connect_input: Required[DiscriminatedDataConnectorZohoDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorZoomDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    connection_id: str
    """In case of re-connecting, id of the existing connection"""


class DiscriminatedDataConnectorZoomDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["zoom"]]

    pre_connect_input: Required[DiscriminatedDataConnectorZoomDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorAirtableDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["airtable"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorApolloDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["apollo"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorBrexDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["brex"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorCodaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["coda"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorFinchDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    state: str


class DiscriminatedDataConnectorFinchDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["finch"]]

    pre_connect_input: Required[DiscriminatedDataConnectorFinchDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorFirebaseDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["firebase"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorForeceiptDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["foreceipt"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorGreenhouseDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["greenhouse"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorHeronDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["heron"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorLunchmoneyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["lunchmoney"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorMercuryDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["mercury"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorMergeDiscriminatedPreConnectInputPreConnectInput(TypedDict, total=False):
    categories: Required[Iterable[object]]

    customer_email_address: str

    customer_organization_name: str


class DiscriminatedDataConnectorMergeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["merge"]]

    pre_connect_input: Required[DiscriminatedDataConnectorMergeDiscriminatedPreConnectInputPreConnectInput]


class DiscriminatedDataConnectorMootaDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["moota"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorOnebrickDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["onebrick"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorOpenledgerDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["openledger"]]

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


class DiscriminatedDataConnectorRampDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["ramp"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSaltedgeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["saltedge"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSharepointOnpremDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["sharepoint-onprem"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSlackAgentDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["slack-agent"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorSplitwiseDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["splitwise"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorStripeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["stripe"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorTellerDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["teller"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorTogglDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["toggl"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorTwentyDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["twenty"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorVenmoDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["venmo"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorWiseDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["wise"]]

    pre_connect_input: Required[object]


class DiscriminatedDataConnectorYodleeDiscriminatedPreConnectInput(TypedDict, total=False):
    connector_name: Required[Literal["yodlee"]]

    pre_connect_input: Required[object]


DiscriminatedData: TypeAlias = Union[
    DiscriminatedDataConnectorAcceloDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAcmeApikeyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAcmeOauth2DiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAdobeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAdyenDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAircallDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAmazonDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorApaleoDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAsanaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAttioDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAuth0DiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAutodeskDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAwsDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBamboohrDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBasecampDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBattlenetDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBigcommerceDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBitbucketDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBitlyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBlackbaudDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBoldsignDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBoxDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBraintreeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorCalendlyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorClickupDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorCloseDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorConfluenceDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorContentfulDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorContentstackDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorCopperDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorCorosDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDatevDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDeelDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDialpadDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDigitaloceanDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDiscordDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDocusignDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorDropboxDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorEbayDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorEgnyteDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorEnvoyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorEventbriteDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorExistDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFacebookDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFactorialDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFigmaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFitbitDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFortnoxDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFreshbooksDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFrontDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGitHubDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGitlabDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGongDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleCalendarDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleDocsDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleDriveDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleMailDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGoogleSheetDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGorgiasDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGrainDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGumroadDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGustoDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorHarvestDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorHighlevelDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorHubspotDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorInstagramDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorIntercomDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorJiraDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorKeapDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorLeverDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorLinearDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorLinkedinDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorLinkhutDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMailchimpDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMiroDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMondayDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMuralDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorNamelyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorNationbuilderDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorNetsuiteDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorNotionDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOdooDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOktaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOsuDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOuraDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOutreachDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPagerdutyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPandadocDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPayfitDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPaypalDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPennylaneDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPinterestDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPipedriveDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPodiumDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorProductboardDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorQualtricsDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorQuickbooksDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorRedditDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSageDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSalesforceDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSalesloftDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSegmentDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorServicem8DiscriminatedPreConnectInput,
    DiscriminatedDataConnectorServicenowDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSharepointDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorShopifyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSignnowDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSlackDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSmartsheetDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSnowflakeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSpotifyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSquarespaceDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSquareupDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorStackexchangeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorStravaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTeamworkDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTicktickDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTimelyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTodoistDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTremendousDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTsheetsteamDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTumblrDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTwinfieldDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTwitchDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTwitterDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTypeformDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorUberDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorVimeoDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWakatimeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWealthboxDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWebflowDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWhoopDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWordpressDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWrikeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorXeroDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorYahooDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorYandexDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZapierDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZendeskDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZenefitsDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZohoDeskDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZohoDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorZoomDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorAirtableDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorApolloDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorBrexDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorCodaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFinchDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorFirebaseDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorForeceiptDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorGreenhouseDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorHeronDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorLunchmoneyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMercuryDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMergeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorMootaDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOnebrickDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorOpenledgerDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPlaidDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorPostgresDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorRampDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSaltedgeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSharepointOnpremDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSlackAgentDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorSplitwiseDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorStripeDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTellerDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTogglDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorTwentyDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorVenmoDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorWiseDiscriminatedPreConnectInput,
    DiscriminatedDataConnectorYodleeDiscriminatedPreConnectInput,
]


class Options(TypedDict, total=False):
    connection_external_id: Annotated[Union[str, float, None], PropertyInfo(alias="connectionExternalId")]

    integration_external_id: Annotated[Union[str, float, None], PropertyInfo(alias="integrationExternalId")]
