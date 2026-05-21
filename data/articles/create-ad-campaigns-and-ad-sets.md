---
title: "Create Ad Campaigns and Ad Sets"
slug: create-ad-campaigns-and-ad-sets
url: https://dev.sprinklr.com/create-ad-campaigns-and-ad-sets
---

# Create Ad Campaigns and Ad Sets

#   POST Create Campaigns, Ad Sets & Ads
 

This API allows you to create ad campaigns and their associated ad sets on advertising platforms (in this case, Facebook).


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/create/publishAds

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

### Request Body














































****

- [Facebook Ad Objectives](https://dev.sprinklr.com/create-ad-campaigns-and-ad-sets#fb_ad_objective)
- [LinkedIn Ad Objectives](https://dev.sprinklr.com/create-ad-campaigns-and-ad-sets#linkedinAdObjectives)
- [X Ad Objectives](https://dev.sprinklr.com/create-ad-campaigns-and-ad-sets#xAdObjectives)















| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| startTime | integer | Required | Ad start time in epoch milliseconds. |
| adAccountId | integer | Required | ID of the ad account where the ad will be created. |
| name | string | Required | Name of the campaign. |
| adCategories | array | Optional | Categories assigned to the ad (empty array if not applicable). |
| channelType | string | Required | Advertising platform (e.g., FACEBOOK). |
| adObjective | string | Required | The objective of the advertisement campaign.Supported Values: |
| status | string | Required | Initial campaign status (PAUSED or ACTIVE). |
| apiAdSetRequests | array of objects | Required | List of ad set configurations. |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

### Facebook Channel Ad Objectives

The following table lists the supported ad objectives for Facebook (value for `adObjective` parameter):


















































| Enum | Label |
| --- | --- |
| OUTCOME_AWARENESS | Facebook Awareness |
| OUTCOME_TRAFFIC | Facebook Traffic |
| OUTCOME_ENGAGEMENT | Facebook Engagement |
| OUTCOME_LEADS | Facebook Leads |
| OUTCOME_SALES | Facebook Sales |
| OUTCOME_APP_PROMOTION | Facebook App Promotion |
| MESSAGES | Facebook Messages |
| CONVERSIONS | Facebook Conversions |
| CATALOG_SALES | Facebook Catalog Sales |
| STORE_VISITS | Facebook Store Visits |


### LinkedIn Channel Ad Objectives

The following table lists the supported ad objectives for LinkedIn (value for adObjective parameter).






































| Ad Objective | Label |
| --- | --- |
| LINKEDIN_WEBSITE_VISIT | Website Visit |
| LINKEDIN_BRAND_AWARENESS | Brand Awareness |
| LINKEDIN_LEAD_GENERATION | Lead Generation |
| LINKEDIN_ENGAGEMENT | Engagement |
| LINKEDIN_VIDEO_VIEWS | Video Views |
| LINKEDIN_JOB_APPLICANT | Job Applicant |
| LINKEDIN_WEB_CONVERSION | Web Conversion |

### X (Twitter) Channel Ad Objectives

The following table lists the supported ad objectives for X (value for adObjective parameter).










































| Ad Objective | Label |
| --- | --- |
| PROMOTED_TWEETS | X Engagements |
| TWITTER_AWARENESS | X Reach |
| TWITTER_WEBSITE_CLICKS | X Website Traffic |
| PROMOTED_ACCOUNTS | X Followers |
| TWITTER_VIDEO_VIEWS | X Video Views |
| TWITTER_PREROLL_VIEWS | X Preroll Views |
| TWITTER_APP_INSTALLS | X App Installs |
| TWITTER_APP_ENGAGEMENTS | X App Re Engagements |

### apiAdSetRequests Object




































































































****````












      ****















| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| adPlacementType | string | Required | Placement setting type (MANUAL or AUTOMATIC). |
| devicePlatforms | array of strings | Required | Targeted device platforms (BOTH, MOBILE, DESKTOP). |
| positions | array of strings | Required | Placement positions (e.g., FEED, INSTAGRAM_STORIES). |
| publisherPlatforms | array of strings | Required | Supported platforms (FACEBOOK, INSTAGRAM, X, LINKEDIN). |
| pacingType | string | Required | Budget pacing type (STANDARD, ACCELERATED). |
| name | string | Required | Name of the ad set. |
| adObjective | string | Required | Ad set objective. |
| destinationType | string | Required | Destination type for the ad (e.g., ON_VIDEO). |
| startTime | integer | Required | Ad set start time in epoch milliseconds. |
| endTime | integer | Required | Ad set end time in epoch milliseconds. |
| adSetRotationType | string | Optional | Ad set rotation method (OPTIMIZED, EVEN). |
| bidAmount | number | Required | Bid amount in the account's currency. |
| bidStrategy | string | Required | Bid strategy (e.g., LOWEST_COST_WITH_BID_CAP). |
| chargeBy | string | Required | Billing method (IMPRESSIONS, CLICKS). |
| lifeTimeBudget | number | Required | Lifetime budget of the ad set.    Dev Note: You must specify at least one of the following fields:      lifeTimeBudget or dailyBudget. |
| dailyBudget | number | Required | Daily budget of the ad set. |
| optimiseFor | string | Required | Optimization goal. Supported Values: REACH, APP_INSTALL, LINK_CLICKS, CONVERSIONS, THRUPLAY |
| targeting | object | Required | Audience targeting details. |
| apiAdVariantRequests | array of objects | Optional | List of ad creative variants. |

### targeting Object


















| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| targetingValues | object | Optional | Dictionary of targeting attributes. Keys include MIN_AGE, MAX_AGE, GENDER, COUNTRY, etc. |

### targetingValues




































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| GENDER |  | Gender targeting | Object |
|  | key | Gender key (0 for All) | String |
|  | label | Gender label | String |
| COUNTRY |  | Country targeting | Object |
|  | key | Country code key | String |
|  | label | Country name | String |
|  | subText | Additional information | String |
|  | parentKey | Parent country code | String |
| MIN_AGE |  | Minimum age targeting | Object |
|  | key | Minimum age key | String |
|  | label | Minimum age label | String |
| LOCATION_TYPES |  | Location type targeting | Object |
|  | key | Location type key | String |
|  | label | Location type label | String |
| ACCOUNT_LEVEL_EXCLUDED_PUBLISHER_LIST_IDS |  | Excluded publisher lists | Object |
|  | key | Blocklist ID key | String |
|  | label | Blocklist label | String |
| PLATFORM |  | Platform targeting | Object |
|  | key | Platform key | String |
|  | label | Platform label | String |
| MAX_AGE |  | Maximum age targeting | Object |
|  | key | Maximum age key | String |
|  | label | Maximum age label | String |

### apiAdVariantRequests Object








































































































| Parameter | Sub-Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- | --- |
| name | - | string | Required | Name of the ad variant. |
| creativeObject | - | object | Required | Creative details for the ad. |
|  | name | string | Required | Creative name. |
|  | title | string | Optional | Ad headline. |
|  | description | string | Optional | Ad description. |
|  | linkDescription | string | Optional | Description shown with the link. |
|  | videoUrl | string | Optional | URL of the ad video. |
|  | imageUrl | string | Optional | URL of the ad image. |
|  | linkUrl | string | Optional | Destination URL for the ad. |
|  | displayLink | string | Optional | Display link for the ad. |
|  | callToAction | string | Optional | Call-to-action button text (e.g., SHOP_NOW). |
|  | pageId | string | Required | Primary Facebook page ID. |
|  | secondaryPageId | string | Optional | Secondary Facebook page ID, if applicable. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/create/publishAds' \
--header 'Authorization: Bearer {token}’ \
--header 'Key: {API_Key}’ \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "startTime": 1754983509000,
    "adAccountId":66001023,
    "name": "Shivi Test",
    "adCategories": [],
    "channelType": "FACEBOOK",
    "adObjective": "OUTCOME_ENGAGEMENT",
    "status": "PAUSED",
    "apiAdSetRequests": [
         {  "adPlacementType": "MANUAL",
            "devicePlatforms": ["BOTH"],
            "positions": [
                "FEED",
                "INSTAGRAM_FEED",
                "FACEBOOK_STORIES",
                "INSTAGRAM_STORIES",
                "INSTAGRAM_REELS",
                "FACEBOOK_REELS"
            ],
            "publisherPlatforms": ["FACEBOOK","INSTAGRAM"],
            "pacingType": "STANDARD",
            "name": "New AdSet",
            "adObjective": "OUTCOME_ENGAGEMENT",
            "destinationType": "ON_VIDEO",
            "startTime": 1754983509000,
            "endTime":  1756106709000,
            "adSetRotationType": "OPTIMIZED",
            "bidAmount": 4444,
            "bidStrategy": "LOWEST_COST_WITH_BID_CAP",
            "chargeBy": "IMPRESSIONS",
            "lifeTimeBudget": 12000,
            "optimiseFor": "THRUPLAY",
            "targeting": {
                "targetingValues": {
                    "MIN_AGE": [{"key": "18", "label": "18"}],
                    "MAX_AGE": [{"key": "65", "label": "65+"}],
                    "GENDER": [{"key": "0", "label": "All"}],
                    "COUNTRY": [
                        {
                            "key": "country_united states",
                            "label": "United States",
                            "parentKey": "US"
                        }
                    ]
                }
            },
            "apiAdVariantRequests": [
                {
                    "name": "New Ad",
                    "creativeObject": {
                        "name": "Creative MC",
                        "title": "New Products headline",
                        "description": "latest products for Text",
                        "linkDescription": "Link Description",
                        "videoUrl": "https://storage.googleapis.com/spr-qa6-cdn/EXPORT/66000000/ee5482be-6d2e-41dc-9bdd-50207f1b1430-1331818238/video.mp4",
                        "imageUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/13537cc1-74a0-49d8-858c-fa09e4588a8d-1679383746/preview_image_0-video.png",
                        "linkUrl": "https://www.acmesprinklr.com",
                        "displayLink": "www.acmesprinklr.com",
                        "callToAction": "SHOP_NOW",
                        "pageId": "133777779825243",
                        "secondaryPageId": "7798747846810883"
                    }
                }
            ]
        }
    ]
}'

## Example - Response


{
    "data": {
        "requestId": "689c5dd6a303306eda946d78",
        "paidInitiativeId": "689c5dd7a303306eda946d79",
        "adSetIds": [
            "689c5dd7a303306eda946d7a"
        ],
        "adIds": [
            "689c5dd7a303306eda946d7b"
        ],
        "errorList": [],
        "errorsMap": {}
    },
    "errors": []
}

### Response Schema




























































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | object | Contains the IDs of created entities and any related errors. |
|  | requestId | string | Unique request identifier. |
|  | paidInitiativeId | string | Unique ID of the created campaign. |
|  | adSetIds | array of strings | List of created ad set IDs. |
|  | adIds | array of strings | List of created ad IDs. |
|  | errorList | array | List of ad set or ad creation errors. |
|  | errorsMap | object | Key-value mapping of errors. |
| errors |  | array | List of root-level errors, if any. |

[](https://dev.sprinklr.com/create-ad-campaigns-and-ad-sets)

[Back to top](https://dev.sprinklr.com/create-ad-campaigns-and-ad-sets)
