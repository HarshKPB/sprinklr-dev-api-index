---
title: "Inbound Column Stream"
slug: inbound-column-stream
url: https://dev.sprinklr.com/inbound-column-stream
---

# Inbound Column Stream

#
  POST Inbound Column Stream




You can use the api to fetch stream data for inbound columns available in engagement dashboards with Sprinklr Modern Engagement.

Note: In the response of this API call, if there is more data then you will receive a cursor as `"nextPageCursor": "602cc4ngh67dg345tnb703fe"`which can be used in the [Stream Cursor API](https://dev.sprinklr.com/stream-cursor-api) to fetch the next set of data.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/stream/{streamId}/feed

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

### Path Parameter



[Read Dashboard API](https://dev.sprinklr.com/fetch-engagement-dashboard-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| streamId | Required | Stream Id of the inbound column to fetch data.You can fetch the stream Id using | String |

## Request Parameters







| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| start | Required | The start offset to tell the client where to begin pulling data.The default is 0. | Integer |
| rows | Required | The number of rows to be fetched, starting from the start. | Integer |
| sortField | Required | Key on the basis of which you want to sort the data. | String |
| sortOrder | Optional | Short in ascending or descending order.i.e. ASC and DESC. | String |

### Supported sortField







``

| sortField | Description |
| --- | --- |
| CHANNEL_CREATED_TIME | For INBOX,     COMMENTS,     REPLIES,     POSTS,     PRIVATE_MESSAGES,     EVENTS,     SHARES,     GROUP_POSTS,     GROUP_COMMENTS,     GROUP_REPLIES,     FB_INSTA_AD_POST,     FB_INSTA_AD_COMMENT,     FB_INSTA_AD_REPLY,     CHANNEL_SEARCH,     SEARCH,     SEARCH_WITH_FILTERS,     RECEIVED_DIRECT_MESSAGES,     MENTIONS,     RETWEETS,     MY_TWEETS,     SENT_DIRECT_MESSAGES,     TIMELINE,     FILTERED_TIMELINE,     FAV_TWEETS,     LISTS,     INSTAGRAM_MEDIA,     INSTAGRAM_MEDIA_COMMENT,     INSTAGRAM_STORY,     INSTAGRAM_MENTION,     INSTAGRAM_COMMENT_MENTION,     INSTAGRAM_MEDIA_TAG,     DIRECT_MESSAGES, TIK_TOK VIDEO POSTS |

## Example - Request















Copy Code


 curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/stream/{streamId}/feed' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "start" : 0,
    "rows" :2,
    "sortField" : "CHANNEL_CREATED_TIME",
    "sortOrder" : "ASC"
    }'






## Example - Response





{
    "data": {
        "entities": [
{
                "sourceType": "ACCOUNT",
                "sourceId": 134567,
                "content": {
                    "text": "this is a gp"
                },
                "channelMessageId": "1693299830886884_2748473155369541",
                "channelType": "FACEBOOK",
                "accountType": "FBPAGE",
                "channelCreatedTime": 1610558220000,
                "senderProfile": {
                    "name": "Hookah Bar",
                    "channelType": "FACEBOOK",
                    "channelId": "1693299830886884",
                    "permalink": " ",
                    "followers": 0,
                    "username": "Hookah Bar",
                    "verified": false,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "receiverProfile": {
                    "name": "Hookah Bar",
                    "channelType": "FACEBOOK",
                    "channelId": "1693299830886884",
                    "permalink": " ",
                    "followers": 0,
                    "username": "Hookah Bar",
                    "verified": false,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "permalink": "https://www.facebook.com/1693299830886884/posts/2748473155369541/",
                "language": "en",
                "messageId": "FACEBOOK_15_1693299830886884_2748473155369541",
                "postId": 4401573146,
                "brandPost": true,
                "createdTime": 1610558225191,
                "modifiedTime": 1610558225184,
                "textEntities": {},
                "insights": {
                    "POST_FB_IMPRESSIONS": 2.0
                },
                "workflow": {
                    "modifiedTime": 1610558225184,
                    "customProperties": {},
                    "queues": [],
                    "spaceWorkflows": [],
                    "campaignId": "4706_623"
                },
                "enrichments": {},
                "conversationId": "1693299830886884_2748473155369541",
                "autoImported": false
            },
            {
                "sourceType": "ACCOUNT",
                "sourceId": 123457,
                "content": {
                    "text": "testing",
                    "attachment": {
                        "disableManualResponse": false,
                        "reSubmittable": false,
                        "type": "CAROUSEL"
                    }
                },
                "channelMessageId": "1693299830886884_2729446573938866",
                "channelType": "FACEBOOK",
                "accountType": "FBPAGE",
                "channelCreatedTime": 1608284228000,
                "senderProfile": {
                    "name": "Hookah Bar",
                    "channelType": "FACEBOOK",
                    "channelId": "1693299830886884",
                    "permalink": " ",
                    "followers": 0,
                    "username": "Hookah Bar",
                    "verified": false,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "receiverProfile": {
                    "name": "Hookah Bar",
                    "channelType": "FACEBOOK",
                    "channelId": "1693299830886884",
                    "permalink": " ",
                    "followers": 0,
                    "username": "Hookah Bar",
                    "verified": false,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "permalink": "https://www.facebook.com/1693299830886884/posts/2729446573938866/",
                "language": "fi",
                "messageId": "FACEBOOK_15_1693299830886884_2729446573938866",
                "postId": 4330698915,
                "brandPost": true,
                "createdTime": 1608284234139,
                "modifiedTime": 1608284234324,
                "textEntities": {},
                "insights": {
                    "POST_FB_IMPRESSIONS": 1.0
                },
                "workflow": {
                    "modifiedTime": 1608284234324,
                    "customProperties": {},
                    "queues": [],
                    "spaceWorkflows": [],
                    "campaignId": "4706_750"
                },
                "enrichments": {},
                "conversationId": "1693299830886884_2729446573938866",
                "autoImported": false
            },
         ],
"hasMore": true,
        "nextPageCursor": "602cc4ccefbf6645tnb703fe"
    },
    "errors": []
}







## Response Parameters

 [Click here](https://dev.sprinklr.com/read-message-by-id) to check the response definitions of **MESSAGE**.



********

| Parameter | Description | Type |
| --- | --- | --- |
| nextPageCursor | The nextPageCursor you get in the response will be used in the Stream Cursor API to fetch next set of data. | String |

[](https://dev.sprinklr.com/inbound-column-stream)




[Back to top](https://dev.sprinklr.com/inbound-column-stream)
