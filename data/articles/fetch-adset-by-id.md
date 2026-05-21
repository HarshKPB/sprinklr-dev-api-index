---
title: "Fetch AdSet by Id"
slug: fetch-adset-by-id
url: https://dev.sprinklr.com/fetch-adset-by-id
---

# Fetch AdSet by Id

#   POST Fetch AdSet by Id
 

This API retrieves AdSet details for the specified ad set ID from a given advertising account.


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/get/adSetByIds

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
















[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-adset-by-id#account_userid)









| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| accountUserId | Required | String | Id of the ad account userSee |
| adEntityIds | Required | String | Ad set ID to fetch details for. |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request



 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/get/adSetByIds' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "accountUserId": "394232028806869",
    "adEntityIds": "6656fb5f3694ba2ba6d79c52"
}'



## Example - Response





{
    "data": {
        "adEntities": [
            {
                "name": "carousel_retry_2905-Gender: Male; Max Age: 65+; Min Age: 18; Location Types: home,recent; Countries: United States; Language: English (UK),Armenian,English (US); User Operating System: Android",
                "channelId": "120207878240970434",
                "id": "6656fb5f3694ba2ba6d79c52",
                "startTime": 1717017318000,
                "endTime": 1717145118000,
                "adObjective": "OUTCOME_TRAFFIC",
                "campaignGroupId": "120207878230630434",
                "status": "DRAFT",
                "publisherPlatforms": [
                    "AUDIENCE_NETWORK",
                    "FACEBOOK",
                    "INSTAGRAM",
                    "MESSENGER"
                ],
                "positions": [
                    "INSTAGRAM_STORIES",
                    "INSTAGRAM_EXPLORE",
                    "REWARDED_VIDEO",
                    "FEED",
                    "RIGHT_HAND_COLUMN",
                    "SUGGESTED_VIDEO",
                    "MESSENGER_STORY",
                    "MARKETPLACE",
                    "INSTAGRAM_REELS",
                    "FACEBOOK_SEARCH",
                    "FACEBOOK_BIZ_DISCO_FEED",
                    "HOME",
                    "INSTAGRAM_FEED",
                    "FACEBOOK_STORIES",
                    "FACEBOOK_REELS",
                    "INSTAGRAM_EXPLORE_HOME",
                    "FACEBOOK_REELS_OVERLAY",
                    "INSTAGRAM_SEARCH_RESULTS",
                    "INSTREAM_VIDEO",
                    "INSTAGRAM_PROFILE_FEED",
                    "CLASSIC"
                ],
                "devicePlatforms": [
                    "BOTH"
                ],
                "adPlacementType": "AUTOMATIC",
                "pacingType": "STANDARD",
                "lifeTimeBudget": 500.0,
                "bidStrategy": "LOWEST_COST",
                "chargeBy": "IMPRESSIONS",
                "optimiseFor": "LINK_CLICK",
                "apiAttributionSpecs": [
                    {
                        "eventType": "CLICK_THROUGH",
                        "windowDays": 1
                    }
                ],
                "destinationType": "WEBSITE_MESSENGER",
                "promotedObjectType": "PAGE",
                "promotedObjectId": "103016439108141",
                "targeting": {
                    "targetingValues": {
                        "MIN_AGE": [
                            {
                                "key": "18",
                                "label": "18"
                            }
                        ],
                        "COUNTRY": [
                            {
                                "key": "country_united states",
                                "label": "United States",
                                "subText": "",
                                "parentKey": "US"
                            }
                        ],
                        "LOCALES": [
                            {
                                "key": "24",
                                "label": "English (UK)"
                            },
                            {
                                "key": "68",
                                "label": "Armenian"
                            },
                            {
                                "key": "6",
                                "label": "English (US)"
                            }
                        ],
                        "MAX_AGE": [
                            {
                                "key": "65",
                                "label": "65+"
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
                        "PLATFORM": [
                            {
                                "key": "Android",
                                "label": "Android"
                            }
                        ],
                        "GENDER": [
                            {
                                "key": "1",
                                "label": "Male"
                            }
                        ],
                        "ACCOUNT_LEVEL_EXCLUDED_PUBLISHER_LIST_IDS": [
                            {
                                "key": "211116878196294",
                                "label": "Blocklist2"
                            }
                        ]
                    }
                },
                "frequency": [],
                "adBrandSafetyContentFilterLevels": [
                    "AN_STANDARD",
                    "FACEBOOK_STANDARD"
                ],
                "isDynamicCreative": false
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
|  | adEntities | List of AdSet details.See the adEntities table below. | Array of Objects |
|  | errors | List of errors, if any, within the data object. | Array |
| errors |  | List of errors, if any, at the root level. | Array |

#### adEntities Object





































| Parameter | Type | Description |
| --- | --- | --- |
| id | string | Unique identifier of the ad set. |
| name | string | Name of the ad set. |
| channelId | string | Channel identifier. |
| channelType | string | Advertising channel type (e.g., FACEBOOK). |
| adObjective | string | Objective of the ad set. |
| campaignGroupId | string | Associated campaign identifier. |
| status | string | Current ad set status. |
| startTime | integer | Start time (epoch milliseconds). |
| endTime | integer | End time (epoch milliseconds). |
| publisherPlatforms | array of strings | Platforms where the ad set is published. |
| positions | array of strings | Eligible ad placements. |
| devicePlatforms | array of strings | Supported device platforms. |
| adPlacementType | string | Placement selection type (e.g., AUTOMATIC). |
| pacingType | string | Budget pacing strategy. |
| lifeTimeBudget | number | Lifetime budget. |
| bidStrategy | string | Bid strategy (e.g., LOWEST_COST). |
| chargeBy | string | Billing event (e.g., IMPRESSIONS). |
| optimiseFor | string | Optimization goal (e.g., LINK_CLICK). |
| apiAttributionSpecs | array of objects | Attribution specification entries. |
| destinationType | string | Destination type (e.g., WEBSITE_MESSENGER). |
| promotedObjectType | string | Type of promoted object (e.g., PAGE). |
| promotedObjectId | string | Identifier of promoted object. |
| targeting | object | Audience targeting configuration. |
| frequency | array | Frequency control settings. |
| adBrandSafetyContentFilterLevels | array of strings | Brand safety filter levels. |
| isDynamicCreative | boolean | Indicates if dynamic creative is enabled. |

#### apiAttributionSpecs Object













| Parameter | Type | Description |
| --- | --- | --- |
| eventType | string | Attribution event type (e.g., CLICK_THROUGH). |
| windowDays | number | Attribution window in days. |

#### targeting Object












| Parameter | Type | Description |
| --- | --- | --- |
| targetingValues | object | Dictionary of targeting attributes keyed by attribute name. |

### targetingValues — Item Structure (Examples)



































































































































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

[](https://dev.sprinklr.com/fetch-adset-by-id) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-adset-by-id)
