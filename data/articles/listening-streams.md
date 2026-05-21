---
title: "Listening Streams"
slug: listening-streams
url: https://dev.sprinklr.com/listening-streams
---

# Listening Streams

#
  POST Listening Streams



This endpoint returns the message stream associated with each message, containing the required information. It returns StreamWidgetResponse.

## API Endpoint

 https://api3.sprinklr.com/{env}/api/v2/listening/query/stream


	**Note**: If you do not have Listening Stream enabled you will receive the following error in the response body:




{
  "message": "Streaming in listening is not enabled for you. Please contact support",
  "data": { }
}







**Note: **

You cannot fetch more than 10000 messages in a same timestamp.

You cannot fetch more than 1000 messages in one request.

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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


## Request Parameters















































****








****


























































| Parameters | Sub-Params | Required | Description | Type |
| --- | --- | --- | --- | --- |
| sinceTime |  | Optional | start time of the time range in milliseconds | Long |
| untilTime |  | Optional | end time of the time range in milliseconds | Long |
| timeField |  | Optional | Set the type of time range (sinceTime + untilTill) to use. It takes either 				"SYSTEM_CREATED_TIME": The time message is created on Sprinklr 				"SN_CREATED_TIME": The time message is created on social network (default) | String |
| timezoneOffset |  | Optional | The timezone UTC offset in milliseconds. Default offset set to 0 for UTC based time. e.g.  EST timezone -5 UTC it will be -(5*60*60*1000) | Long |
| details |  | Required | Object defining the details for the widget. | Object |
|  | widgetType | Required | Refers to the type of the widgetExample: STREAM | String |
| filters |  | Optional | List<WidgetFilter> | The filters applied to the widget. |
|  | dimension |  | Refers to the dimension of the message stream | String |
|  | filterValues |  | Refers to the list of ids for the given dimensionExample: For TOPIC dimension, the filterValues would be the list of topic Ids | List[String] |
| metric |  | Optional | The metric type for the widget; MENTIONS (default), REACH | String |
| trendAggregationPeriod |  | Optional | The trend aggregate period; applicable for TREND and GROUPED_TREND Widget  				{HOUR, DAY, WEEK, MONTH, QUARTER, YEAR} | String |
| start |  | Optional | starting page number; default=0; applicable for only STREAM Widget | Integer |
| rows |  | Optional | max number of items in the page; default=20; applicable for only STREAM | Integer |
| echoRequest |  | Optional | flag to state whete to get back request in response object. | Boolean |
| tag |  | Optional | A state parameter. It can be used as version attached with the response. It will remain unchanged from api and will be returned as it is. | String |
| sortKey |  | Optional | It can take 3 values -  				‘SYSTEM_CREATED_TIME’ - system created time 				‘CREATED_TIME’ - social network created time 				‘MODIFIED_TIME’ - modified time 				It sorts the response messages based upon the specified field. by default it sorts the response message based upon CREATED_TIME | String |
| messageFormatOptions |  | Optional | Comma delimit format values = {strip_html, text strip_url, include_original} 				strip_html - Strip html from the message text 				strip_url - Strip Urls from the message text 				include_original - Include the original text as well in the field "originalText" | String |


### Example - Request















Copy Code


 curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/listening/query/stream' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "sinceTime": "1731061980000",
    "untilTime": "1731065580000",
    "details": {
        "widgetType": "STREAM"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "670ea8ee45b02d1899afed71"
            ]
        }
    ],
    "metric": "MENTIONS",
    "timezoneOffset": 14400000,
    "rows": 1,
    "start": 1
}'






### Example - Response





{
    "data": {
        "result": [
            {
                "sourceType": "LISTENING",
                "sourceId": -1,
                "content": {
                    "text": "😂🫵🏻💯🔥\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n....Our hashtag:- #viratabdfan #virat #viratlovers\n\n#viratkohli #viratabdfanpage18 #abdevilliers #abd\n\n#anushkasharma #rcb #rcbarmy\n\n#royalchallengersbangalore #rcblovers #rcbstatus #ipl\n\n#kingkohli #ipl2023 #iplauction #india\n\n#indiancricketteam #marathi #marathipost #msdhoni\n\n#mahirat #marathistatus #maxwell #fafduplessis\n\n#cricket #cricketlovers♥️🏏",
                    "attachment": {
                        "url": "https://instagram.fpnq10-1.fna.fbcdn.net/o1/v/t16/f1/m86/B94BA9ADFC9F69E3316E9F9BE89E1A9A_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNsaXBzLnVua25vd24tQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=instagram.fpnq10-1.fna.fbcdn.net&_nc_cat=102&vs=574795864914640_4121054925&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9COTRCQTlBREZDOUY2OUUzMzE2RTlGOUJFODlFMUE5QV92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dCZ1Z4aHRQR3I3d0NHVURBR1ltSEM4Q1dZVlVicV9FQUFBRhUCAsgBACgAGAAbAYgHdXNlX29pbAExFQAAJoSqt5nTyOE%2FFQIoAkMzLBdAI%2FfO2RaHKxgSZGFzaF9iYXNlbGluZV8xX3YxEQB1AAA%3D&ccb=9-4&oh=00_AYCRp-QEnzZakw-XHemCFqZoQFcvALJif6eI5ZtlypzNvA&oe=672FD060&_nc_sid=1d576d",
                        "type": "VIDEO"
                    },
                    "isRichText": false
                },
                "channelMessageId": "18021575324538004",
                "channelType": "INSTAGRAM",
                "channelCreatedTime": 1731065571000,
                "senderProfile": {
                    "name": "Instagram User",
                    "channelType": "INSTAGRAM",
                    "channelId": "9052e1e9352583c51ae9f6adebb1000f",
                    "followers": 0,
                    "following": 0,
                    "username": "Instagram User",
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0,
                    "statusCount": 0,
                    "accountSpecificInfos": []
                },
                "receiverProfile": {
                    "followers": 0,
                    "following": 0,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0,
                    "statusCount": 0,
                    "accountSpecificInfos": []
                },
                "permalink": "https://www.instagram.com/reel/DCG9wrxMuQZ/",
                "language": "en",
                "messageId": "LISTENING_-1_1731065571000_INSTAGRAM_36_18021575324538004",
                "brandPost": false,
                "createdTime": 1731065951571,
                "modifiedTime": 1731065951571,
                "textEntities": {
                    "message": [
                        {
                            "indices": [
                                59,
                                71
                            ],
                            "hashtag": "viratabdfan"
                        },
                        {
                            "indices": [
                                72,
                                78
                            ],
                            "hashtag": "virat"
                        },
                        {
                            "indices": [
                                79,
                                91
                            ],
                            "hashtag": "viratlovers"
                        },
                        {
                            "indices": [
                                93,
                                104
                            ],
                            "hashtag": "viratkohli"
                        },
                        {
                            "indices": [
                                105,
                                123
                            ],
                            "hashtag": "viratabdfanpage18"
                        },
                        {
                            "indices": [
                                124,
                                137
                            ],
                            "hashtag": "abdevilliers"
                        },
                        {
                            "indices": [
                                138,
                                142
                            ],
                            "hashtag": "abd"
                        },
                        {
                            "indices": [
                                144,
                                158
                            ],
                            "hashtag": "anushkasharma"
                        },
                        {
                            "indices": [
                                159,
                                163
                            ],
                            "hashtag": "rcb"
                        },
                        {
                            "indices": [
                                164,
                                172
                            ],
                            "hashtag": "rcbarmy"
                        },
                        {
                            "indices": [
                                174,
                                200
                            ],
                            "hashtag": "royalchallengersbangalore"
                        },
                        {
                            "indices": [
                                201,
                                211
                            ],
                            "hashtag": "rcblovers"
                        },
                        {
                            "indices": [
                                212,
                                222
                            ],
                            "hashtag": "rcbstatus"
                        },
                        {
                            "indices": [
                                223,
                                227
                            ],
                            "hashtag": "ipl"
                        },
                        {
                            "indices": [
                                229,
                                239
                            ],
                            "hashtag": "kingkohli"
                        },
                        {
                            "indices": [
                                240,
                                248
                            ],
                            "hashtag": "ipl2023"
                        },
                        {
                            "indices": [
                                249,
                                260
                            ],
                            "hashtag": "iplauction"
                        },
                        {
                            "indices": [
                                261,
                                267
                            ],
                            "hashtag": "india"
                        },
                        {
                            "indices": [
                                269,
                                287
                            ],
                            "hashtag": "indiancricketteam"
                        },
                        {
                            "indices": [
                                288,
                                296
                            ],
                            "hashtag": "marathi"
                        },
                        {
                            "indices": [
                                297,
                                309
                            ],
                            "hashtag": "marathipost"
                        },
                        {
                            "indices": [
                                310,
                                318
                            ],
                            "hashtag": "msdhoni"
                        },
                        {
                            "indices": [
                                320,
                                328
                            ],
                            "hashtag": "mahirat"
                        },
                        {
                            "indices": [
                                329,
                                343
                            ],
                            "hashtag": "marathistatus"
                        },
                        {
                            "indices": [
                                344,
                                352
                            ],
                            "hashtag": "maxwell"
                        },
                        {
                            "indices": [
                                353,
                                366
                            ],
                            "hashtag": "fafduplessis"
                        },
                        {
                            "indices": [
                                368,
                                376
                            ],
                            "hashtag": "cricket"
                        },
                        {
                            "indices": [
                                377,
                                391
                            ],
                            "hashtag": "cricketlovers"
                        }
                    ]
                },
                "location": {
                    "text": "Unknown",
                    "lat": 0.0,
                    "lon": 0.0,
                    "additional": {
                        "code": "UN"
                    }
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 0.0,
                    "POST_REACH_COUNT": 0.0,
                    "POST_LIKE_COUNT": 8.0
                },
                "workflow": {},
                "enrichments": {},
                "conversationId": "18021575324538004",
                "autoImported": false,
                "autoResponse": false
            }
        ],
        "hasMore": true
    },
    "errors": []
}







### Response Parameters


































































































































- ****
- ****
- ****


































































| Parameter | Sub Parameter | Sub Sub Parameter | Type | Description |
| --- | --- | --- | --- | --- |
| data |  |  | Object | This is the primary container in the API response that encapsulates the payload returned by the API. |
|  | result |  | Array | List of message results. |
|  |  | sourceType | String | Source of the message (e.g., LISTENING). |
|  |  | sourceId | Integer | Source identifier (-1 in this case). |
|  |  | content | Object | Encapsulates the core details of a message, including its textual and media components. |
|  |  | channelMessageId | String | Unique ID of the message on the channel. |
|  |  | channelType | String | The social media platform (e.g., INSTAGRAM). |
|  |  | channelCreatedTime | Long | Timestamp of message creation (in milliseconds). |
|  |  | senderProfile | Object | Provides details about the user who sent the message. |
|  |  | receiverProfile | Object | Contains details about the recipient of the message. |
|  |  | permalink | String | URL to the original Instagram post. |
|  |  | language | String | Detected language of the message. |
|  |  | messageId | String | Unique identifier for the message. |
|  |  | brandPost | Boolean | Indicates if the post is brand-related. |
|  |  | createdTime | Long | Timestamp when the message was created. |
|  |  | modifiedTime | Long | Timestamp when the message was last modified. |
|  |  | textEntities | Object | Provides structured details about specific elements within the message text, such as hashtags, mentions, or links.                   Includes:                                      message (array): A list of identified entities within the message text.                     indices (array of integers): The start and end positions of the entity within the text.                     hashtag (string, optional): The hashtag extracted from the message (e.g., #viratkohli). |
|  |  | location | Object | Provides geographical information associated with the message. |
|  |  | insights | Object | Provides key engagement metrics related to the message or post. |
|  |  | workflow | Object | Workflow-related information (if any). |
|  |  | enrichments | Object | Additional enrichments (if available). |
|  |  | conversationId | String | ID of the conversation thread. |
|  |  | autoImported | Boolean | Indicates if the message was auto-imported. |
|  |  | autoResponse | Boolean | Indicates if the message received an auto-response. |
|  | hasMore |  | Boolean | Indicates if there are more results to fetch. |
| errors |  |  | Array | List of errors (if any). |

[](https://dev.sprinklr.com/listening-streams-v1)




[Back to top](https://dev.sprinklr.com/listening-streams)
