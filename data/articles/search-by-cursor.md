---
title: "Search by Cursor"
slug: search-by-cursor
url: https://dev.sprinklr.com/search-by-cursor
---

# Search by Cursor

# GET Search by Cursor

You can fetch the next set of available data with this API call.

## API Endpoint

https://api3.sprinklr.com`/{env}`api/v2/search/`{entityType}?id={id}`

**Dev Note: ** The above {id} is the one you receive in the response as “cursor” from the Search by Entity API.

```

"cursor": "https://api3.sprinklr.com/{env}/api/v2/search/{entityType}?id={cursorId}"

```

**Note: **Before using this API call, you should use the Search by Entity API to receive the Cursor in the response.



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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | The type of entity you are searching for | String |

### Query Parameters













``



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| cursorId | Required | The cursor id you received as response in the Search by Entity API post call. Example: "cursor": "id=5dd2699aaf47f50001d3299d" | String |

**Dev Notes: **The cursor id is only valid for **`five minutes`**. In case the cursor id expires, you'll have to regenerate a new one using [search by entity](https://dev.sprinklr.com/search-by-entity) API call.

## Example - Request

 Copy Code


curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/search/SAM?id=5dd2699aaf47f50001d3299d \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'

## Example - Response

{
    "data": {
        "results": [
            {
                "id": "5d737a16b205370001806b71",
                "name": "title",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/title-295a17e7-13c7-476d-8d39-93a3293b5588-2136884405.jpg",
                    "title": "title",
                    "description": "title",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 3.0,
                    "LINKEDIN_COMPANY_POST_IMPRESSIONS_COUNT": 0.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 0.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1567850697272,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d739b1fb2053700018d05fc",
                "name": "title",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/title-12b10539-e181-4155-b9b5-8a6f7166e233-2136884405.jpg",
                    "title": "title",
                    "description": "title",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11",
                    "partnerCustomProperties": {
                        "spr_campaign_goal": [],
                        "wh_bu_hsm_lan_code": [],
                        "wh_bu_hsm_element": [],
                        "5be003f4e4b023619df4ed48": [],
                        "wh_bu_hsm_lan_pol": [],
                        "wh_bu_hsm_namespace": [],
                        "5bf6ac70e4b0d3d98bda7bb4": [],
                        "5d63b63ac7a0e3224c156ec5": [
                            "Temp1"
                        ]
                    }
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 3.0,
                    "LINKEDIN_COMPANY_POST_IMPRESSIONS_COUNT": 0.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 0.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1567858992072,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "GLOBAL"
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d75dac786213d1e6ac5dd4c",
                "name": "4 images validation https://t.co/Jybz6ykWdv",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_ED-98db7c79-7562-4c1c-b4f4-94a1dd5dde0d-1093256239.jpg",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "TWITTER_VIDEO_VIEWS": 0.0,
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 7.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 7.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "TWITTER_TOTAL_ENGAGEMENTS": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568006588322,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d75dac786213d1e6ac5dd4b",
                "name": "4 images validation https://t.co/Jybz6ykWdv",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_ED-ed1db36f-eba2-40d2-ba83-e46315372abd-1381699108.jpg",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "TWITTER_VIDEO_VIEWS": 0.0,
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 7.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 7.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "TWITTER_TOTAL_ENGAGEMENTS": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568006588322,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d75ed01642f3d466b925e95",
                "name": "Set message from here with custom text fbpage1568009435199",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___testproxy-qa4.sprinklr-b5bfa80d-665b-4da1-9e85-daa7c2620f82-2099336475.jpg",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_FB_IMPRESSIONS_VIRAL_UNIQUE": 0.0,
                    "POST_FB_IMPRESSIONS_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_ORGANIC_UNIQUE": 0.0,
                    "POST_FB_NEGATIVE_FEEDBACK": 0.0,
                    "POST_FB_IMPRESSIONS_FAN_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_AUTOPLAYED": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_UNIQUE": 0.0,
                    "POST_FB_CONSUMPTIONS_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_UNIQUE": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_ORGANIC": 0.0,
                    "POST_FB_NEGATIVE_FEEDBACK_UNIQUE": 0.0,
                    "POST_FB_IMPRESSIONS_FAN_PAID_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_AUTOPLAYED": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_CLICKED_TO_PLAY": 0.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_FB_VIDEO_VIEWS_ORGANIC": 0.0,
                    "POST_FB_VIDEO_VIEW_TIME": 0.0,
                    "POST_COMMENT_COUNT": 1.0,
                    "POST_FB_IMPRESSIONS_VIRAL": 0.0,
                    "POST_FB_IMPRESSIONS_PAID_UNIQUE": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_AUTOPLAYED": 0.0,
                    "POST_FB_CONSUMPTIONS": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_PAID": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S": 0.0,
                    "POST_FB_STORYTELLERS": 1.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_ORGANIC_UNIQUE": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_PAID_UNIQUE": 0.0,
                    "POST_FB_IMPRESSIONS_ORGANIC": 0.0,
                    "POST_FB_IMPRESSIONS_FAN": 0.0,
                    "POST_FB_STORIES": 1.0,
                    "POST_FB_VIDEO_VIEWS": 0.0,
                    "POST_FB_ENGAGED_USERS": 1.0,
                    "POST_FB_IMPRESSIONS_ORGANIC_UNIQUE": 0.0,
                    "POST_REACH_COUNT": 0.0,
                    "POST_FB_VIDEO_LENGTH": 0.0,
                    "POST_FB_IMPRESSIONS": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_ORGANIC": 0.0,
                    "POST_FB_VIDEO_VIEWS_SOUND_ON": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_CLICKED_TO_PLAY": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S": 0.0,
                    "TOTAL_ENGAGEMENT": 1.0,
                    "POST_FB_VIDEO_VIEWS_10S_SOUND_ON": 0.0,
                    "POST_FB_IMPRESSIONS_FAN_UNIQUE": 0.0,
                    "ENGAGEMENT_METRICS": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_CLICKED_TO_PLAY": 0.0,
                    "POST_FB_VIDEO_VIEWS_PAID_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_ORGANIC": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_PAID": 0.0,
                    "POST_FB_VIDEO_AVG_TIME_WATCHED": 0.0,
                    "POST_FB_VIDEO_VIEW_TIME_ORGANIC": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568011263000,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d75ed01642f3d466b925e94",
                "name": "Set message from here with custom text fbpage1568009435199",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___scontent.xx.fbcdn.net_-2f183a09-f398-499a-9024-7ff3608cb429-669878853.jpg",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_FB_IMPRESSIONS_VIRAL_UNIQUE": 0.0,
                    "POST_FB_IMPRESSIONS_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_ORGANIC_UNIQUE": 0.0,
                    "POST_FB_NEGATIVE_FEEDBACK": 0.0,
                    "POST_FB_IMPRESSIONS_FAN_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_AUTOPLAYED": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_UNIQUE": 0.0,
                    "POST_FB_CONSUMPTIONS_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_UNIQUE": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_ORGANIC": 0.0,
                    "POST_FB_NEGATIVE_FEEDBACK_UNIQUE": 0.0,
                    "POST_FB_IMPRESSIONS_FAN_PAID_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_AUTOPLAYED": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_CLICKED_TO_PLAY": 0.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_FB_VIDEO_VIEWS_ORGANIC": 0.0,
                    "POST_FB_VIDEO_VIEW_TIME": 0.0,
                    "POST_COMMENT_COUNT": 1.0,
                    "POST_FB_IMPRESSIONS_VIRAL": 0.0,
                    "POST_FB_IMPRESSIONS_PAID_UNIQUE": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_AUTOPLAYED": 0.0,
                    "POST_FB_CONSUMPTIONS": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_PAID": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S": 0.0,
                    "POST_FB_STORYTELLERS": 1.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_ORGANIC_UNIQUE": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_PAID_UNIQUE": 0.0,
                    "POST_FB_IMPRESSIONS_ORGANIC": 0.0,
                    "POST_FB_IMPRESSIONS_FAN": 0.0,
                    "POST_FB_STORIES": 1.0,
                    "POST_FB_VIDEO_VIEWS": 0.0,
                    "POST_FB_ENGAGED_USERS": 1.0,
                    "POST_FB_IMPRESSIONS_ORGANIC_UNIQUE": 0.0,
                    "POST_REACH_COUNT": 0.0,
                    "POST_FB_VIDEO_LENGTH": 0.0,
                    "POST_FB_IMPRESSIONS": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_ORGANIC": 0.0,
                    "POST_FB_VIDEO_VIEWS_SOUND_ON": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_CLICKED_TO_PLAY": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S": 0.0,
                    "TOTAL_ENGAGEMENT": 1.0,
                    "POST_FB_VIDEO_VIEWS_10S_SOUND_ON": 0.0,
                    "POST_FB_IMPRESSIONS_FAN_UNIQUE": 0.0,
                    "ENGAGEMENT_METRICS": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_30S_PAID": 0.0,
                    "POST_FB_VIDEO_VIEWS_CLICKED_TO_PLAY": 0.0,
                    "POST_FB_VIDEO_VIEWS_PAID_UNIQUE": 0.0,
                    "POST_FB_VIDEO_VIEWS_10S_ORGANIC": 0.0,
                    "POST_FB_VIDEO_COMPLETE_VIEWS_PAID": 0.0,
                    "POST_FB_VIDEO_AVG_TIME_WATCHED": 0.0,
                    "POST_FB_VIDEO_VIEW_TIME_ORGANIC": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568011263000,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d74f263642f3d3916469611",
                "name": "Photo Post",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___testproxy-qa4.sprinklr-9600cde9-5238-47be-984e-7c46c985d925-238016306.jpg",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 34.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 1.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1567946631000,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d75dac786213d1e6ac5dd49",
                "name": "4 images validation https://t.co/Jybz6ykWdv",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_ED-f76d565c-de69-46e2-8d18-05ba94f8e13a-1231817257.png",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "TWITTER_VIDEO_VIEWS": 0.0,
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 7.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 7.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "TWITTER_TOTAL_ENGAGEMENTS": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568006588322,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d74f2aa18a1581797dbe29a",
                "name": "Twitter Photo Post https://t.co/Vp0YvrSo4D",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_ED-f210ed1d-2347-49e2-a058-a2482d43ccc0-303592129.jpg",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "TWITTER_VIDEO_VIEWS": 0.0,
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 1.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 1.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "TWITTER_TOTAL_ENGAGEMENTS": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1567947180412,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d739d8d86213d3b138a58b7",
                "name": "title",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/title-31fa81ca-802d-4675-941a-ac09bc7eb143-2136878701.png",
                    "title": "title",
                    "description": "title",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 3.0,
                    "LINKEDIN_COMPANY_POST_IMPRESSIONS_COUNT": 4.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 4.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1567859535562,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            }
        ],
        "cursor": "id=5dd27b88af47f50001d32a0f"
    },
    "errors": []
}



**Dev Note: ** You will receive another cursor if more data is available to fetch. You can use the id given in cursor to make another Get call.

## Response Parameters

[Click here](https://dev.sprinklr.com/create-asset) to check the response definitions of **SAM**.



********

| Parameter | Description | Type |
| --- | --- | --- |
| cursor | The cursor you get in the response will be used again in the Search by Cursor api to fetch next set of data. | String |

[](https://dev.sprinklr.com/search-by-cursor) 

 

 
[Back to top](https://dev.sprinklr.com/search-by-cursor)
