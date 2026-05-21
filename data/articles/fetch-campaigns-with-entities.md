---
title: "Fetch Campaigns with Entities"
slug: fetch-campaigns-with-entities
url: https://dev.sprinklr.com/fetch-campaigns-with-entities
---

# Fetch Campaigns with Entities

#   POST Fetch Campaigns with Entities
 

This API retrieves details of a campaign along with its associated entities, such as ad sets and ads.


**Related Knowledge Base Article: **[Campaign Management](https://www.sprinklr.com/help/categories/campaign-management/63e380f553842c2a03a26862)


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/get/campaignWithEntities

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |


### Request Parameters
















[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-campaigns-with-entities#account_userid)





      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| accountUserId | Required | String | Id of the ad account userSee |
| adEntityIds | Required | String | Campaign ID to fetch details for. Format: {CHANNEL}_{ID}(for example, FACEBOOK_120213190680540130). |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request



 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/get/campaignWithEntities' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "accountUserId": "2773246777472780",
    "adEntityIds": "FACEBOOK_120226736198520434"
}'



## Example - Response





{
    "data": {
        "adEntities": [
            {
                "id": "FACEBOOK_120226736198520434",
                "name": "Automation_Fb_Leads_Forms_New_Obj 2025-07-02 14:13:59.814",
                "channelId": "120226736198520434",
                "channelType": "FACEBOOK",
                "adObjective": "OUTCOME_LEADS",
                "status": "PAUSED",
                "startTime": 1751487279000,
                "apiAdSetRequests": [
                    {
                        "name": "Automation_Fb_Leads_Forms_New_Obj 2025-07-02 14:13:59.814-Auto_india",
                        "channelId": "120226736203310434",
                        "id": "FACEBOOK_120226736203310434",
                        "startTime": 1751487279000,
                        "adObjective": "OUTCOME_LEADS",
                        "campaignGroupId": "120226736198520434",
                        "status": "DRAFT",
                        "publisherPlatforms": [
                            "FACEBOOK",
                            "INSTAGRAM"
                        ],
                        "positions": [
                            "INSTAGRAM_SEARCH_RESULTS",
                            "INSTAGRAM_EXPLORE",
                            "FEED",
                            "INSTAGRAM_FEED",
                            "FACEBOOK_BIZ_DISCO_FEED",
                            "FACEBOOK_REELS",
                            "INSTREAM_VIDEO",
                            "SUGGESTED_VIDEO",
                            "INSTAGRAM_STORIES",
                            "INSTAGRAM_PROFILE_FEED",
                            "FACEBOOK_REELS_OVERLAY",
                            "FACEBOOK_SEARCH",
                            "FACEBOOK_PROFILE_FEED",
                            "FACEBOOK_STORIES",
                            "INSTAGRAM_REELS",
                            "INSTAGRAM_EXPLORE_HOME",
                            "FACEBOOK_NOTIFICATION_MOBILE"
                        ],
                        "devicePlatforms": [
                            "BOTH"
                        ],
                        "adPlacementType": "AUTOMATIC",
                        "chargeBy": "IMPRESSIONS",
                        "optimiseFor": "LEAD",
                        "apiAttributionSpecs": [
                            {
                                "eventType": "CLICK_THROUGH",
                                "windowDays": 1
                            }
                        ],
                        "destinationType": "ON_AD",
                        "promotedObjectType": "PAGE",
                        "promotedObjectId": "107730485680116",
                        "targeting": {
                            "targetingValues": {
                                "GENDER": [
                                    {
                                        "key": "0",
                                        "label": "All"
                                    }
                                ],
                                "PLATFORM_VERSION": [
                                    {
                                        "key": "iOS 2.0",
                                        "label": "iOS 2.0"
                                    }
                                ],
                                "COUNTRY": [
                                    {
                                        "key": "country_india",
                                        "label": "India",
                                        "subText": "",
                                        "parentKey": "IN"
                                    }
                                ],
                                "MIN_AGE": [
                                    {
                                        "key": "23",
                                        "label": "23"
                                    }
                                ],
                                "LOCATION_TYPES": [
                                    {
                                        "key": "home",
                                        "label": "home"
                                    },
                                    {
                                        "key": "recent",
                                        "label": "recent"
                                    }
                                ],
                                "MAX_PLATFORM_VERSION": [
                                    {
                                        "key": "iOS 14.4",
                                        "label": "iOS 14.4"
                                    }
                                ],
                                "ACCOUNT_LEVEL_EXCLUDED_PUBLISHER_LIST_IDS": [
                                    {
                                        "key": "211116878196294",
                                        "label": "Blocklist2"
                                    }
                                ],
                                "PLATFORM": [
                                    {
                                        "key": "iOS",
                                        "label": "iOS"
                                    }
                                ],
                                "MAX_AGE": [
                                    {
                                        "key": "65",
                                        "label": "65+"
                                    }
                                ]
                            },
                            "flexibleTargetingList": [
                                {
                                    "INTERESTS": [
                                        {
                                            "key": "6003057392644",
                                            "label": "Gaming (video games)"
                                        }
                                    ]
                                }
                            ],
                            "exclusions": {
                                "WORK_EMPLOYERS": [
                                    {
                                        "key": "148646721874",
                                        "label": "Sprinklr"
                                    }
                                ]
                            }
                        },
                        "frequency": [],
                        "apiAdVariantRequests": [
                            {
                                "channelId": "120226736209590434",
                                "id": "FACEBOOK_120226736209590434",
                                "name": "Automation_Fb_Leads_Forms_New_Obj 2025-07-02 14:13:59.814-Auto_india_001",
                                "creativeObject": {
                                    "postType": "LINK",
                                    "isDarkPost": true,
                                    "pageId": "107730485680116",
                                    "secondaryPageId": "17841457848453443",
                                    "postChannelId": "107730485680116_623540827440280",
                                    "title": "latest products for sale",
                                    "linkUrl": "http://fb.me/",
                                    "imageUrl": "https://storage.googleapis.com/spr-qa6-cdn-secure/PAID/66000000/c1c577a8-e72f-4407-a76e-8525b8031789-879294258/image.jpg",
                                    "callToAction": "GET_QUOTE",
                                    "destinationObject": {
                                        "type": "WEBSITE",
                                        "url": "http://fb.me/"
                                    },
                                    "forceSingleLink": false,
                                    "multiAdvertiserAd": false
                                },
                                "trackingPixelChannelIds": [],
                                "campaignGroupId": "120226736198520434",
                                "channelCampaignId": "120226736203310434"
                            }
                        ],
                        "adBrandSafetyContentFilterLevels": [
                            "AN_STANDARD",
                            "FEED_STANDARD",
                            "FACEBOOK_STANDARD"
                        ],
                        "isDynamicCreative": false
                    }
                ],
                "lifeTimeBudget": 15000.0
            }
        ],
        "errors": []
    },
    "errors": []
}



## Response Parameters





































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. | Object |
|  | adEntities | List of campaign details.See the adEntities table below. | Array of Objects |
|  | errors | List of errors, if any, within the data object. | Array |
| errors |  | List of errors, if any, at the root level. | Array |

### adEntities Object
























































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the paid initiative. | String |
| name | Name of the paid initiative. | String |
| channelId | Identifier for the ad account or platform-specific channel. | String |
| channelType | Advertising platform/channel type (For example, FACEBOOK). | String |
| adObjective | Advertising objective enum (For example, OUTCOME_TRAFFIC). | AdObjective |
| status | Current status of the initiative (For example, ARCHIVED, DRAFT). | String |
| startTime | Start time of the campaign (epoch timestamp). | Long |
| apiAdSetRequests | List of API Ad Set requests associated with the initiative. | Array of Objects |
| lifeTimeBudget | Total budget allocated for the Ad Campaign over its entire duration. | Number |

### Ad Set Schema



































































































































| Parameter | Description | Type |
| --- | --- | --- |
| name | Name of the Ad Set. | String |
| channelId | Identifier for the Ad channel. | String |
| id | Unique identifier for the Ad Set. | String |
| startTime | Start time of the campaign (epoch timestamp). | String |
| endTime | End time of the campaign (epoch timestamp). | String |
| adObjective | Objective of the Ad Set (such as Brand Awareness, Conversions). | String |
| campaignGroupId | ID of the campaign group. | String |
| status | Current status of the Ad Set, such as DRAFT, PAUSED, ACTIVE, COMPLETED. | String |
| publisherPlatforms | Platforms where the Ad will be published, such as FACEBOOK, INSTAGRAM, MESSENGER. | Object |
| positions | Positions within platforms where the ad can appear, such as FEED, INSTANT_ARTICLE. | Object |
| devicePlatforms | Devices on which the Ad will be shown, such as mobile, desktop. | Object |
| adPlacementType | Type of ad placement. It is AUTOMATIC by default. | String |
| pacingType | Strategy for pacing Ad delivery, such as STANDARD or ACCELERATED. | String |
| dailyBudget | Daily budget allocated for the Ad Set. | Integer |
| bidStrategy | Strategy used for bidding, such as cost cap or target ROAS. | String |
| chargeBy | Defines what the advertiser is charged for, such as IMPRESSIONS or CLICKS. | String |
| optimiseFor | Optimization goal for the Ad Set. | String |
| apiAttributionSpecs | Attribution specifications for tracking conversions. | Array of Objects |
| promotedObjectType | Type of object being promoted, such as PRODUCT, PAGE, or SERVICE. | String |
| promotedObjectId | Identifier of the promoted object. | String |
| targeting | Targeting parameters for the Ad Set. | Array of Objects |
| frequency | Frequency capping settings for ad delivery. | Array |
| adBrandSafetyContentFilterLevels | Levels of brand safety content filtering. | Array of Strings |
| isDynamicCreative | Indicates if dynamic creative optimization is enabled. | Boolean |

[](https://dev.sprinklr.com/fetch-campaigns-with-entities) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-campaigns-with-entities)
