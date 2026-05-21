---
title: "Update Ad Campaigns and Ad Sets"
slug: update-ad-campaigns-and-ad-sets
url: https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets
---

# Update Ad Campaigns and Ad Sets

#   POST Update Campaigns, Ad Sets & Ads
 

This API allows you to update ad campaigns and their associated ad sets on advertising platforms (in this case, Facebook).


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/create/updateAds

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





















****







****

- [Facebook Ad Objectives](https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets#fb_ad_objective)
- [LinkedIn Ad Objectives](https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets#linkedinAdObjectives)
- [X Ad Objectives](https://dev.sprinklr.com/update-ad-campaigns-and-ad-setsn#xAdObjectives)
























[apiAdSetRequests](https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets#api_ad_set_requests)




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Unique identifier of the ad campaign | String |
| channelType | Optional | Advertising platform/channel type.Supported Values: FACEBOOK, LINKEDIN, TWITTER | String |
| adObjective | Optional | The objective of the advertisement campaign.Supported Values: | String |
| dailyBudget | Optional | Daily budget allocated for the ad set. | Double |
| changeTypes | Optional | List of fields being updated (for example, ["NAME", "DAILY_BUDGET"]) | Array |
| name | Optional | Name of the ad campaign | String |
| apiAdSetRequests | Optional | List of ad sets associated with this campaign, each with detailed configuration.See the  table below. | Array |

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

The following table lists the supported ad objectives for LinkedIn (value for `adObjective` parameter).






































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

The following table lists the supported ad objectives for X (value for `adObjective` parameter).










































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





















****
****







****
****







****[Facebook Ad Positions](https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets#fb_ad_positions)







****







****







****































****







****













****



















[targetingValues Object](https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets#targeting_values)




| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Unique identifier of the ad set. | String |
| adPlacementType |  | Type of ad placement.Supported Values: AUTOMATIC, MANUALDefault: AUTOMATIC | String |
| devicePlatforms |  | Devices where the ad will be shown.Supported Values: MOBILE, DESKTOP, BOTHRecommended: BOTH | Array |
| positions |  | Specific positions within platforms where ads will be shown.Supported Values: | Array |
| changeTypes |  | Fields updated for this ad set.Supported Values: NAME, DAILY_BUDGET, BID_AMOUNT | Array |
| publisherPlatforms |  | Platforms where the ads will be published.Supported Values: FACEBOOK, INSTAGRAM, MESSENGER, AUDIENCE_NETWORK | Array |
| pacingType |  | Pacing strategy for ad delivery.Supported Values: STANDARD, ACCELERATED | String |
| name |  | Name of the ad set. | String |
| startTime |  | Start time of the ad set in epoch milliseconds. | Long |
| endTime |  | End time of the ad set in epoch milliseconds. | Long |
| bidAmount |  | Bid amount for the ad set. | Number |
| bidStrategy |  | Bid strategy usedSupported Values: LOWEST_COST, LOWEST_COST_WITH_BID_CAP, COST_CAP | String |
| chargeBy |  | Charging methodSupported Values: IMPRESSIONS, CLICKS, CONVERSIONS | String |
| dailyBudget |  | Daily budget for the ad set. | Number |
| optimiseFor |  | Optimization goal.Supported Values: REACH, APP_INSTALL, LINK_CLICKS, CONVERSIONS | String |
| targeting |  | Object containing target audience criteria. | Object |
|  | name | Name or label for the targeting configuration. | String |
|  | targetingValues | Defines the criteria used to target the audience. This includes filters such as gender, age, location, platform.See the  table below | Object |

### targetingValues Object



































































































































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

### Facebook Ad Positions







































| Position Enum | Display Name |
| --- | --- |
| FEED | Facebook Feed |
| INSTANT_ARTICLE | Instant Articles |
| INSTREAM_VIDEO | Facebook In-Stream Videos |
| RIGHT_HAND_COLUMN | Facebook right column |
| SUGGESTED_VIDEO | Facebook Video Feeds |
| MARKETPLACE | Facebook Marketplace |
| FACEBOOK_STORIES | Facebook Stories |
| FACEBOOK_SEARCH | Facebook Search Results |
| INSTAGRAM_FEED | Instagram Feed |
| INSTAGRAM_EXPLORE | Instagram Explore |
| INSTAGRAM_STORIES | Instagram Stories |
| CLASSIC | Audience Network native, banner and interstitial |
| AUDIENCE_NETWORK_INSTREAM_VIDEO | Audience Network In-Stream Videos |
| REWARDED_VIDEO | Audience Network rewarded videos |
| SPONSORED_MESSAGES | Messenger sponsored messages |
| MESSENGER_STORY | Messenger Stories |
| INSTAGRAM_IGTV | Instagram TV |
| INSTAGRAM_REELS | Instagram Reels |
| FACEBOOK_REELS | Facebook Reels |
| FACEBOOK_REELS_OVERLAY | Ads on Facebook Reels |
| FACEBOOK_BIZ_DISCO_FEED | Facebook Business Explore |
| INSTAGRAM_PROFILE_FEED | Instagram Profile Feed |
| INSTAGRAM_EXPLORE_HOME | Instagram Explore Home |
| INSTAGRAM_SEARCH_RESULTS | Instagram search results |
| INSTAGRAM_REELS_OVERLAY | Ads on Instagram Reels |
| WHATSAPP_MARKETING_MESSAGE | WhatsApp Marketing Messages |
| FACEBOOK_PROFILE_FEED | Facebook Profile Feed |
| INSTAGRAM_PROFILE_REELS | Instagram Profile Reels |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/create/updateAds' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "id": "FACEBOOK_120226311356960434",
    "channelType": "FACEBOOK",
    "adObjective": "OUTCOME_TRAFFIC",
    "dailyBudget": 1260,
    "changeTypes": [
        "NAME",
        "DAILY_BUDGET"
    ],
    "name": "Updated from API - Traffic",
    "apiAdSetRequests": [
        {
            "id": "685beaa08439065289f856a6",
            "adPlacementType": "MANUAL",
            "devicePlatforms": [
                "BOTH"
            ],
            "positions": [
                "FEED",
                "INSTAGRAM_FEED",
                "FACEBOOK_STORIES",
                "INSTAGRAM_STORIES",
                "INSTAGRAM_REELS",
                "FACEBOOK_REELS"
            ],
            "changeTypes": [
                "DAILY_BUDGET",
                "BID_AMOUNT",
                "BID_STRATEGY",
                "OPTIMIZE_FOR",
                "CHARGE_BY",
                "END_DATE",
                "START_DATE",
                "PUBLISHER_PLATFORMS",
                "AD_POSITIONS",
                "DEVICE_PLATFORMS",
                "AD_PLACEMENT_TYPE"
            ],
            "publisherPlatforms": [
                "FACEBOOK",
                "INSTAGRAM"
            ],
            "pacingType": "STANDARD",
            "name": "New AdSet",
            "endTime": 1748608464000,
            "startTime": 1748003664000,
            "bidAmount": 300,
            "bidStrategy": "LOWEST_COST_WITH_BID_CAP",
            "chargeBy": "IMPRESSIONS",
            "dailyBudget": 1300,
            "optimiseFor": "REACH",
            "targeting": {
                "name": "New AdSet - From API - updated again",
                "targetingValues":  {
                        "GENDER": [
                            {
                                "key": "0",
                                "label": "All"
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
                                "key": "30",
                                "label": "30"
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
                    }
            }
        }
    ]
}'



## Example - Response





{
    "data": {
        "requestId": "689b32d58409b804ecebb71d",
        "errorList": [],
        "errorsMap": {}
    },
    "errors": []
}



### Response Parameters










































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data | Object |
|  | requestId | Unique ID associated with the request | String |
|  | errorList | List of errors related to the request (if any) | Array |
|  | errorsMap | Map of field-level errors | Object |
| errors |  | Top-level list of errors (if any) | Array |

[](https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets) 

 

 
[Back to top](https://dev.sprinklr.com/update-ad-campaigns-and-ad-sets)
