---
title: "Fetch Default Placements"
slug: fetch-default-placements
url: https://dev.sprinklr.com/fetch-default-placements
---

# Fetch Default Placements

#  POST Fetch Default Placements

Use this endpoint to retrieve the default ad placements available for a given ad account, and ad objective. The response categorizes placements by device type: DESKTOP, MOBILE, and BOTH. This is typically used during ad setup to determine which placements are supported by the platform for a campaign based on its configuration.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/default/placements

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

## Request Body Parameters




















      ````





      ````















| Field | Type | Required | Description |
| --- | --- | --- | --- |
| accountUserId | string | Yes | Unique identifier of the user associated with the ad account. |
| adBuyingType | enum | No | The buying type for the campaign (e.g., AUCTION, RESERVED). |
| adObjective | enum | Yes | The objective of the ad campaign (e.g., OUTCOME_TRAFFIC, LEADS). |
| destinationType | enum | No | The destination type. |
| optimizationGoal | enum | No | The optimization goal. |

## Steps to Retrieve `accountUserId`


- In Sprinklr, click the **New Page (+)** icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the Accounts page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the **User ID** column. This value corresponds to the `accountUserId`.

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/default/placements' \
--header 'Authorization: Bearer {Token}’ \
--header 'Key: {Api_Key}’ \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "accountUserId": "394232028806869",
    "adBuyingType": "AUCTION",
    "adObjective": "OUTCOME_TRAFFIC"
}'

## Example - Response


{
    "data": {
        "placements": {
            "DESKTOP": [
                "FEED",
                "INSTREAM_VIDEO",
                "FACEBOOK_SEARCH",
                "FACEBOOK_BIZ_DISCO_FEED",
                "FACEBOOK_PROFILE_FEED"
            ],
            "BOTH": [
                "FEED",
                "INSTREAM_VIDEO",
                "SUGGESTED_VIDEO",
                "FACEBOOK_STORIES",
                "FACEBOOK_SEARCH",
                "FACEBOOK_REELS",
                "FACEBOOK_REELS_OVERLAY",
                "FACEBOOK_BIZ_DISCO_FEED",
                "FACEBOOK_PROFILE_FEED",
                "INSTAGRAM_FEED",
                "INSTAGRAM_EXPLORE",
                "INSTAGRAM_STORIES",
                "INSTAGRAM_REELS",
                "INSTAGRAM_PROFILE_FEED",
                "INSTAGRAM_EXPLORE_HOME",
                "INSTAGRAM_SEARCH_RESULTS",
                "INSTAGRAM_PROFILE_REELS",
                "HOME",
                "MESSENGER_STORY"
            ],
            "MOBILE": [
                "FEED",
                "INSTREAM_VIDEO",
                "SUGGESTED_VIDEO",
                "FACEBOOK_STORIES",
                "FACEBOOK_SEARCH",
                "FACEBOOK_REELS",
                "FACEBOOK_REELS_OVERLAY",
                "FACEBOOK_BIZ_DISCO_FEED",
                "FACEBOOK_PROFILE_FEED",
                "INSTAGRAM_FEED",
                "INSTAGRAM_EXPLORE",
                "INSTAGRAM_STORIES",
                "INSTAGRAM_REELS",
                "INSTAGRAM_PROFILE_FEED",
                "INSTAGRAM_EXPLORE_HOME",
                "INSTAGRAM_SEARCH_RESULTS",
                "INSTAGRAM_PROFILE_REELS",
                "HOME",
                "MESSENGER_STORY"
            ]
        }
    },
    "errors": []
}

### Response Schema






























| Field | Sub Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | object | Contains the list of response entities. |
|  | placements | object | Contains lists of supported placements by device type. |
| errors |  | array | List of errors, if any. |

#### placements Object


























| Parameter | Type | Description |
| --- | --- | --- |
| DESKTOP | array of strings | Supported placements for desktop devices. |
| MOBILE | array of strings | Supported placements for mobile devices. |
| BOTH | array of strings | Placements available on both desktop and mobile. |

[](https://dev.sprinklr.com/fetch-default-placements)

[Back to top](https://dev.sprinklr.com/fetch-default-placements)
