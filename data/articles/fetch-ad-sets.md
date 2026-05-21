---
title: "Fetch Ad Sets"
slug: fetch-ad-sets
url: https://dev.sprinklr.com/fetch-ad-sets
---

# Fetch Ad Sets

#   POST Fetch Ad Sets
 

This API allows you to fetch a paginated list of ad sets for a given account.


**Related Knowledge Base Article: **[Ad Sets](https://www.sprinklr.com/help/articles/sprinklr-marketing-glossary/ad-set/641497412680c35a78bc5172)


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/get/adSets

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














[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-ad-sets#account_userid)



| Parameter | Required/Optional | Description |
| --- | --- | --- |
| accountUserId | Required | Id of the ad account userSee |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/get/adSets' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "accountUserId": "394232028806869"
}'



## Example - Response





{
  "data": {
    "adEntities": [
      {
        "name": "API big man-Gender: All; Max Age: 65+; Min Age: 18; Location Types: home,recent; Countries: India; User Operating System: iOS",
        "channelId": "120229205994710569",
        "id": "6825e21b6f84cf7f95c9ae96",
        "startTime": 1747313185000,
        "adObjective": "OUTCOME_APP_PROMOTION",
        "campaignGroupId": "120229205990560569",
        "status": "DRAFT",
        "publisherPlatforms": [
          "AUDIENCE_NETWORK",
          "MESSENGER",
          "FACEBOOK",
          "INSTAGRAM"
        ],
        "positions": [
          "FACEBOOK_REELS_OVERLAY",
          "FACEBOOK_STORIES",
          "INSTAGRAM_REELS",
          "INSTAGRAM_PROFILE_FEED",
          "MESSENGER_STORY",
          "INSTREAM_VIDEO",
          "FACEBOOK_PROFILE_FEED",
          "INSTAGRAM_EXPLORE_HOME",
          "REWARDED_VIDEO",
          "INSTAGRAM_PROFILE_REELS",
          "INSTAGRAM_EXPLORE",
          "INSTAGRAM_SEARCH_RESULTS",
          "FACEBOOK_BIZ_DISCO_FEED",
          "MARKETPLACE",
          "SUGGESTED_VIDEO",
          "CLASSIC",
          "FEED",
          "FACEBOOK_REELS",
          "FACEBOOK_SEARCH",
          "INSTAGRAM_FEED",
          "HOME",
          "INSTAGRAM_STORIES"
        ],
        "devicePlatforms": ["MOBILE"],
        "adPlacementType": "MANUAL",
        "pacingType": "STANDARD",
        "dailyBudget": 300.0,
        "bidStrategy": "LOWEST_COST",
        "chargeBy": "IMPRESSIONS",
        "optimiseFor": "APP_INSTALL",
        "apiAttributionSpecs": [
          {
            "eventType": "CLICK_THROUGH",
            "windowDays": 1
          }
        ],
        "promotedObjectType": "APPLICATION",
        "promotedObjectId": "493673020768393",
        "url": "http://itunes.apple.com/app/id1369693945",
        "targeting": {
          "targetingValues": {
            "COUNTRY": [
              {
                "key": "country_india",
                "label": "India",
                "subText": "",
                "parentKey": "IN"
              }
            ],
            "PLATFORM": [
              {
                "key": "iOS",
                "label": "iOS"
              }
            ],
            "GENDER": [
              {
                "key": "0",
                "label": "All"
              }
            ],
            "MAX_AGE": [
              {
                "key": "65",
                "label": "65+"
              }
            ],
            "PLATFORM_VERSION": [
              {
                "key": "iOS 2.0",
                "label": "iOS 2.0"
              }
            ],
            "MAX_PLATFORM_VERSION": [
              {
                "key": "iOS 14.4",
                "label": "iOS 14.4"
              }
            ],
            "MIN_AGE": [
              {
                "key": "18",
                "label": "18"
              }
            ],
            "APP_INSTALL_STATE": [
              {
                "key": "not_installed",
                "label": "Unchecked"
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
            "ACCOUNT_LEVEL_EXCLUDED_PUBLISHER_LIST_IDS": [
              {
                "key": "211116878196294",
                "label": "Blocklist2"
              },
              {
                "key": "1171530283545811",
                "label": "Blocklist1"
              },
              {
                "key": "6717669128263069",
                "label": "Blocklist 3"
              }
            ]
          }
        },
        "frequency": [],
        "adBrandSafetyContentFilterLevels": [
          "AN_STANDARD",
          "FEED_STANDARD",
          "FACEBOOK_STANDARD"
        ],
        "isDynamicCreative": false
      },
      {
        "name": "sd-sd",
        "id": "6819e4dcee4f7a0d6b60776c",
        "startTime": 1746527435422,
        "adObjective": "OUTCOME_AWARENESS",
        "status": "DRAFT",
        "publisherPlatforms": [
          "INSTAGRAM",
          "MESSENGER",
          "AUDIENCE_NETWORK",
          "FACEBOOK"
        ],
        "positions": [
          "INSTAGRAM_REELS",
          "INSTAGRAM_EXPLORE_HOME",
          "INSTAGRAM_SEARCH_RESULTS",
          "FACEBOOK_PROFILE_FEED",
          "INSTAGRAM_FEED",
          "INSTAGRAM_EXPLORE",
          "FACEBOOK_BIZ_DISCO_FEED",
          "FACEBOOK_SEARCH",
          "AUDIENCE_NETWORK_INSTREAM_VIDEO",
          "FEED",
          "FACEBOOK_REELS",
          "FACEBOOK_REELS_OVERLAY",
          "INSTREAM_VIDEO",
          "SUGGESTED_VIDEO",
          "INSTAGRAM_STORIES",
          "MESSENGER_STORY",
          "INSTAGRAM_PROFILE_FEED",
          "MARKETPLACE",
          "INSTAGRAM_PROFILE_REELS",
          "FACEBOOK_STORIES"
        ],
        "devicePlatforms": ["BOTH"],
        "adPlacementType": "AUTOMATIC",
        "pacingType": "STANDARD",
        "dailyBudget": 34.0,
        "bidStrategy": "LOWEST_COST",
        "chargeBy": "IMPRESSIONS",
        "optimiseFor": "AD_RECALL_LIFT",
        "promotedObjectType": "PAGE",
        "promotedObjectId": "105538155871626",
        "targeting": {
          "targetingValues": {
            "COUNTRY_GROUP": [
              {
                "key": "worldwide",
                "label": "worldwide"
              }
            ],
            "GENDER": [
              {
                "key": "0",
                "label": "All"
              }
            ],
            "MAX_AGE": [
              {
                "key": "65",
                "label": "65+"
              }
            ],
            "LOCATION_INTEREST_TARGETING": [
              {
                "key": "LOCATION_INTEREST_TARGETING",
                "label": "Checked"
              }
            ],
            "MIN_AGE": [
              {
                "key": "18",
                "label": "18"
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
            "ACCOUNT_LEVEL_EXCLUDED_PUBLISHER_LIST_IDS": [
              {
                "key": "211116878196294",
                "label": "Blocklist2"
              },
              {
                "key": "1171530283545811",
                "label": "Blocklist1"
              },
              {
                "key": "6717669128263069",
                "label": "Blocklist 3"
              }
            ]
          },
          "flexibleTargetingList": []
        },
        "frequency": [],
        "adBrandSafetyContentFilterLevels": [
          "AN_STANDARD",
          "FEED_STANDARD",
          "FACEBOOK_STANDARD"
        ],
        "isDynamicCreative": false
      }
    ],
    "errors": []
  },
  "errors": []
}




### Response Parameters



































































































































| Parameter | Description | Type |
| --- | --- | --- |
| name | Name of the ad set. | String |
| channelId | Campaign Id or Channel Id. | String |
| id | Id of the ad set. | String |
| startTime | Start time of the ad set in epoch milliseconds. | Long |
| adObjective | Objective of the ad campaign (for example, brand awareness, conversions). | String |
| campaignGroupId | Id of the campaign group the ad set belongs to. | String |
| status | Current status of the ad set (default: DRAFT, ACTIVE, PAUSED). | String |
| publisherPlatforms | Platforms where the ad will be published (for example, FACEBOOK, INSTAGRAM, MESSENGER). | List |
| positions | Positions within platforms where the ad can appear (for example, FEED, INSTANT_ARTICLE). | List |
| devicePlatforms | Devices on which the ad will be shown (for example, MOBILE). | List |
| adPlacementType | Type of ad placement (default: AUTOMATIC, MANUAL). | String |
| pacingType | Strategy for pacing ad delivery (for example, STANDARD). | String |
| dailyBudget | Daily budget allocated for the ad set. | Double |
| bidStrategy | Strategy used for bidding (for example, LOWEST_COST). | String |
| chargeBy | Defines what the advertiser is charged for (for example, IMPRESSIONS). | String |
| optimiseFor | Optimization goal for the ad set (for example, APP_INSTALL). | String |
| apiAttributionSpecs | Attribution specifications for tracking conversions (see separate table below). | List |
| promotedObjectType | Type of object being promoted (PAGE, OFFER, PIXEL, APPLICATION, PRODUCT_CATALOG, etc.). | String |
| promotedObjectId | Identifier of the promoted object. | String |
| url | Object Store URL. | String |
| targeting | Targeting parameters for the ad set (see separate table below for targetingValues). | TargetingRequest |
| frequency | Frequency capping settings for ad delivery (empty in this example). | List |
| adBrandSafetyContentFilterLevels | Levels of brand safety content filtering (for example, AN_STANDARD). | Set |
| isDynamicCreative | Indicates if dynamic creative optimization is enabled. | Boolean |

### apiAttributionSpecs





















| Parameter | Description | Type |
| --- | --- | --- |
| eventType | Type of attribution event (for example, CLICK_THROUGH). | String |
| windowDays | Number of days for the attribution window. | Integer |

### targetingValues


















































































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| COUNTRY |  |  |  |
|  | key | Country code key (for example, country_india). | String |
|  | label | Country name (for example, India). | String |
|  | subText | Additional info (often empty). | String |
|  | parentKey | Parent country code (for example, IN). | String |
| PLATFORM |  |  |  |
|  | key | Platform key (for example, iOS). | String |
|  | label | Platform label (for example, iOS). | String |
| GENDER |  |  |  |
|  | key | Gender key (for example, 0 for All). | String |
|  | label | Gender label (for example, All). | String |
| MAX_AGE |  |  |  |
|  | key | Maximum age key (for example, 65). | String |
|  | label | Maximum age label (for example, 65+). | String |
| MIN_AGE |  |  |  |
|  | key | Minimum age key (for example, 18). | String |
|  | label | Minimum age label (for example, 18). | String |
| PLATFORM_VERSION |  |  |  |
|  | key | Platform version key (for example, iOS 2.0). | String |
|  | label | Platform version label (for example, iOS 2.0). | String |
| MAX_PLATFORM_VERSION |  |  |  |
|  | key | Max platform version key (for example, iOS 14.4). | String |
|  | label | Max platform version label (for example, iOS 14.4). | String |
| APP_INSTALL_STATE |  |  |  |
|  | key | App install state key (for example, not_installed). | String |
|  | label | App install state label (for example, Unchecked). | String |
| LOCATION_TYPES |  |  |  |
|  | key | Location type key (for example, home, recent). | String |
|  | label | Location type label (for example, home, recent). | String |
| ACCOUNT_LEVEL_EXCLUDED_PUBLISHER_LIST_IDS |  |  |  |
|  | key | Blocklist Id key (for example, 211116878196294). | String |
|  | label | Blocklist label (for example, Blocklist2). | String |

[](https://dev.sprinklr.com/fetch-ad-sets) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-ad-sets)
