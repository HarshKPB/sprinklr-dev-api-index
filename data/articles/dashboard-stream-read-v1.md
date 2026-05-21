---
title: "Dashboard Stream Read v1"
slug: dashboard-stream-read-v1
url: https://dev.sprinklr.com/dashboard-stream-read-v1
---

# Dashboard Stream Read v1

#
  GET Dashboard Stream Read


Using this API, you can fetch the existing message(s) within the given column stream Id.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/stream/{stream id}/feed


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

## Path Parameters



[Read Dashboard API](https://dev.sprinklr.com/fetch-engagement-dashboard-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| streamId | Required | Stream Id of the column to fetch data.You can fetch the stream Id by referring to the . | String |

## Query Parameters







````

****

****

********

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| start | Required | The start offset to tell the client where to begin pulling data. The default is 0. To pull multiple batches of messages, use the start and row paramaters to iterate through the messages. Example: Pull #1: GET /api/v1/stream/{stream id}/feed?start=0&rows=21 Example: Pull #2: GET /api/v1/stream/{stream id}/feed?start=1&rows=21 | String |
| rows | Required | The number of rows to be fetched starting from the start. The default is 21 rows. | Integer |
| sinceDate | Optional | Used to return messages with an actionTime greater than this value. The attribute actionTime shows when a message entered Sprinklr. The messages are returned in DESCENDING order of the actionTime. The recent messages are shown first. To get the latest messages, you can use sinceDate without untilDate. | Integer |
| untilDate | Optional | Used to return messages with an actionTime less than this value. The attribute actionTime shows when a message entered Sprinklr. The messages are returned in DESCENDING order of the actionTime. The recent messages are shown first. | Integer |
| sort | Optional | Refers to the sorting information that you want to apply on the response.Supported values: snCreatedTime, snModifiedTimeNote: It is required to define the order in which the response will be arranged, i.e., ascending or descendingThe syntax for defining sort field would be: sort=snCreatedTime asc (for ascending), sort=snCreatedTime desc (for descending) | String |

**Dev Notes: **
You can use `sinceDate` & `untilDate` to get the data between certain dates.

**Example:**
`https://api2.sprinklr.com/api/v1/stream/5c348717e4b0230512940b46/feed?start=0&rows=10&sinceDate=1583231387000&untilDate=1583233343000&sort=snCreatedTime`

## Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/stream/598dd97ee4b0ec5110f2d803/feed?sort=snCreatedTime&rows=10&start=0' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'









{
        "favorite": false,
        "promotedOnly": false,
        "fromVerifiedProfile": false,
        "authorKlout": "60",
        "generator": "Twitter Ads Composer",
        "feedbackDM": false,
        "partnerId": 787,
        "clientId": 7019,
        "sourceId": -1,
        "accountId": 999998,
        "sourceType": "LISTENING",
        "snType": "TWITTER",
        "snMsgId": "1126122676341202945",
        "messageType": 2,
        "messageSubType": 46,
        "universalMessageId": "TWITTER_2_1126122676341202945",
        "permalink": "https://twitter.com/show/status/1126122676341202945",
        "message": "Can #DC capitalise on their form to beat 2018 finalists #SRH?\nEnjoy the actions of the playoffs with your friends! Watch #DCvSRH LIVE and invite, chat and play with your friends on Hotstar, jahaan #KoiYaarNahiFar.\n\n#VIVOIPL #VIVOIPL2019",
        "textEntities": {
            "message": [
                {
                    "indices": [
                        4,
                        7
                    ],
                    "hashtag": "DC",
                    "copiableEntity": false
                },
                {
                    "indices": [
                        56,
                        60
                    ],
                    "hashtag": "SRH",
                    "copiableEntity": false
                },
                {
                    "indices": [
                        121,
                        128
                    ],
                    "hashtag": "DCvSRH",
                    "copiableEntity": false
                },
                {
                    "indices": [
                        197,
                        212
                    ],
                    "hashtag": "KoiYaarNahiFar",
                    "copiableEntity": false
                },
                {
                    "indices": [
                        215,
                        223
                    ],
                    "hashtag": "VIVOIPL",
                    "copiableEntity": false
                },
                {
                    "indices": [
                        224,
                        236
                    ],
                    "hashtag": "VIVOIPL2019",
                    "copiableEntity": false
                }
            ]
        },
        "highLightEntities": {},
        "senderProfile": {
            "snType": "TWITTER",
            "age": 0,
            "snId": "2817066926",
            "name": "Hotstar",
            "screenName": "hotstartweets",
            "bio": "Your favourite destination for shows, movies and sports. Need help? Reach out to our support team at @hotstar_helps.",
            "subType": "",
            "following": 246,
            "followers": 196118,
            "favCount": 1290,
            "statusCount": 18785,
            "permalink": "https://twitter.com/hotstartweets",
            "createdTime": "1411048038000",
            "profileImgUrl": "https://pbs.twimg.com/profile_images/974277012419371009/K9jmigAK_normal.jpg",
            "verified": true,
            "profileWorkflowProperties": {
                "tags": [],
                "comments": [],
                "notifyUserIds": [],
                "partnerProfileLists": [
                    1168
                ],
                "clientProfileLists": [],
                "partnerCustomProperties": {
                    "57473e79e4b001e1b0c5e051": [
                        "Not Working"
                    ],
                    "58fc99dde4b0fbea49e7ed5b": [
                        "en"
                    ],
                    "5a2e3c69e4b04020caed0c21": [
                        "no"
                    ]
                },
                "clientCustomProperties": {},
                "spaceCustomProperties": {},
                "userCustomProperties": {},
                "clientTags": []
            },
            "universalProfileId": "56a8c171e4b0d76b9fde6f66",
            "participationIndex": 0.0,
            "influencerIndex": 60.0,
            "spamIndex": 0.0,
            "accountsFollowedByUser": [],
            "accountsFollowingUser": [],
            "accountsUnFollowingUser": [],
            "accountsUnFollowedByUser": [],
            "accountsBlockingUser": [],
            "accountsSuspendingUser": [],
            "profileTags": [],
            "urlEntities": {
                "bio": [
                    {
                        "url": "https://t.co/ILe7524DDO",
                        "display_url": "hotstar.com",
                        "expanded_url": "http://www.hotstar.com"
                    }
                ]
            },
            "textEntities": {
                "bio": [
                    {
                        "indices": [
                            101,
                            115
                        ],
                        "screenName": "hotstar_helps",
                        "copiableEntity": false
                    },
                    {
                        "indices": [
                            0,
                            23
                        ],
                        "url": "https://t.co/ILe7524DDO",
                        "copiableEntity": false
                    }
                ]
            }
        },
        "receiverProfile": {
            "age": 0,
            "following": 0,
            "followers": 0,
            "favCount": 0,
            "statusCount": 0,
            "profileWorkflowProperties": {
                "tags": [],
                "comments": [],
                "notifyUserIds": [],
                "partnerProfileLists": [],
                "clientProfileLists": [],
                "partnerCustomProperties": {},
                "clientCustomProperties": {},
                "spaceCustomProperties": {},
                "userCustomProperties": {},
                "clientTags": []
            },
            "participationIndex": 0.0,
            "influencerIndex": 0.0,
            "spamIndex": 0.0,
            "accountsFollowedByUser": [],
            "accountsFollowingUser": [],
            "accountsUnFollowingUser": [],
            "accountsUnFollowedByUser": [],
            "accountsBlockingUser": [],
            "accountsSuspendingUser": []
        },
        "isSenderFollower": false,
        "createdTime": 1557323566364,
        "modifiedTime": 1557911786468,
        "snCreatedTime": 1557323543044,
        "snCreatedTimeYearMonth": "2019_05",
        "snModifiedTime": 1557323543044,
        "actionTime": 1557323543044,
        "snStats": {
            "nEFR": 3904,
            "reC": 175152,
            "nr": 3,
            "erEng": 3,
            "nF": 175152,
            "conLen": 236,
            "iFsC": 60,
            "nL": 0
        },
        "mediaList": [],
        "workflowProperties": {
            "sentiment": 2,
            "isSpam": false,
            "isProfane": false,
            "tags": [],
            "partnerQueues": [],
            "contentLists": [],
            "partnerCustomProperties": {},
            "processingUserDetailsList": [],
            "read": false
        },
        "language": "en",
        "conversationId": "1126122676341202945",
        "parentMsgType": 0,
        "deleted": false,
        "archived": false,
        "brandPost": false,
        "parentBrandPost": false,
        "hasBrandComment": false,
        "hasScheduledComment": false,
        "hasParentPost": false,
        "hasApplicationConversation": false,
        "rootUniversalMessageId": "TWITTER_2_1126122676341202945",
        "isSharedPost": false,
        "hasConversation": false,
        "colorCode": "green",
        "colorDescription": "20 days - 30 days range",
        "influencerScore": "60",
        "dataSource": "gFireOrig",
        "defaultActionTime": 1557323543044,
        "additionalInformation": {
            "intel": {
                "source": "TWITTER",
                "assetTitle": "##JJNew",
                "assetType": "COMMERCE_PRODUCT",
                "assetId": "5a6eb184e4b0d788e0921baf"
            },
            "eS": [
                {
                    "title": "Person",
                    "pol": "neutral",
                    "sc": 1.0,
                    "labels": [
                        "live"
                    ]
                }
            ]
        },
        "hasChildren": false,
        "userActions": [],
        "detectedSurveyMessage": false
    }







### Response Parameters







[Channel Type](https://dev.sprinklr.com/channels-v1)

[MessageType](https://dev.sprinklr.com/)

[StreamType](https://dev.sprinklr.com/listening-streams-v1)

[Channel Type](https://dev.sprinklr.com/channels-v1)

[](https://dev.sprinklr.com/message-v1)

| Parameter | Sub Parameter | Key: Values | Description | Type |
| --- | --- | --- | --- | --- |
| favorite |  |  | If True, favorite selected. | Boolean |
| promotedOnly |  |  | If True, Its promoted. | Boolean |
| fromVerifiedProfile |  |  | Is the profile verified or not. | Boolean |
| feedbackDM |  |  | Is direct feedback message allowed or not. | Boolean |
| partnerId |  |  | Unique Id of the Partner. | String |
| clientId |  |  | Unique client Id in Partner. | String |
| sourceId |  |  | Id of the source type. accountId or PS Id. | Long |
| accountId |  |  | Unique Id for the channel account added in the system. | Long |
| sourceType |  |  | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING}. | String |
| snType |  |  | for the message. | String |
| snMsgId |  |  | Unique message Identifier received from channel. | String |
| messageType |  |  | An inbound message has a . | Long |
| messageSubType |  |  | . | Long |
| universalMessageId |  |  | Unique internal universal Id of message. | String |
| permalink |  |  | Message Permalink, that provide message link on channel. | String |
| message |  |  | Message text. | String |
| textEntities |  |  |  |  |
|  | message |  | Text message. | String |
|  |  | hashtag | The locations of the hashtags in the message BaseTextEntity. | Custom |
|  |  | mentions | The locations of the mentions in the message BaseTextEntity. | Custom |
|  |  | urls | The location of the URLs in the BaseTextEntity. | Custom |
| highLightEntities |  |  | The key words in the message which matched the topic query. | Custom |
| senderProfile |  |  | The profile of the message sender. AudienceProfile. | Custom |
|  | snType |  | for the message. | String |
|  | age |  | Age of the sender. | Integer |
|  | snId |  | Sender Id. | String |
|  | name |  | Name of the sender. | Custom |
|  | screenName |  | Screen Name where message appeared. | Custom |
|  | bio |  | Description about the sender space. Why they use it. | String, Long |
|  | following |  | Social following by sender. | Integer |
|  | followers |  | Fllowers of the sender profile. | Integer |
|  | favCount |  | Favorite count of sender profile. | Integer |
|  | statusCount |  | Status count of sender profile. How many status update sender posted. | Integer |
|  | permalink |  | Profile Permalink, that provide profile link on channel. | String |
|  | createdTime |  | Creation time of sender profile. | Long |
|  | profileImgUrl |  | Link to image used as a DP on sender profile. | Image |
|  | verified |  | Sender profile verified otr not. | Boolean |
|  | profileWorkflowProperties |  | Metrics of workflow properties. | Map<String, Long> |
| receiverProfile |  |  | The profile of the message receiver. AudienceProfile. | Custom |
|  | age |  | Age of the message receiver. | String |
|  | following |  | Social following by receiver. | Integer |
|  | followers |  | Fllowers of the receiver profile. | Integer |
|  | favCount |  | Favorite count of receiver profile. | Integer |
|  | statusCount |  | Status count of receiver profile. How many status update receiver posted. | Integer |
|  | profileWorkflowProperties |  | Metrics of workflow properties. | Map<String, Long> |
| snStats |  |  | Object storing message statistics. | Map<String, Long> |
| mediaList |  |  | Object for Media attachment. | List<Media Object> |
| workflowProperties |  |  | Workflow properties of message. | MessageWorkflowProperties |
|  | language |  | Language used in message. | String |
|  | conversationId |  | Unique conversation Identifier. | String |
|  | parentMsgType |  | Message Typeof parent message of message. | Integer |
|  | deleted |  | Is message deleted. | Boolean |
|  | archived |  | Is message archived. | Boolean |
|  | brandPost |  | Is message brandpost or fan post. | Boolean |
|  | parentBrandPost |  | Is parent post brandpost or fan post. | Boolean |
|  | hasBrandComment |  | Does message have brand comments. | Boolean |
|  | hasScheduledComment |  | Does the Post have any Scheduled Comments. | Boolean |
|  | hasParentPost |  | Does the Parent have any post. | Boolean |
|  | hasApplicationConversation |  | True, if it is enabled. | Boolean |
|  | isSharedPost |  | True, if it is enabled. | Boolean |
|  | hasConversation |  | Does message have a conversation. | Boolean |
| additionalInformation |  |  | Addition information about stream. |  |
|  | intel |  |  |  |
|  |  | source | Message native source. | String |
|  |  | assetTitle | Tittle of the aseet. | String |
|  |  | assetType | Type of asset. | String |
|  |  | assetId | Id of the asset. | String |
|  | hasChildren |  | Does it has clildren messages. | Boolean |
| userActions |  |  | Actions taken by user. | list |
|  | detectedSurveyMessage |  | If True, it is enabled. | Boolean |

	[](https://dev.sprinklr.com/dashboard-stream-read-v1)






[Back to top](https://dev.sprinklr.com/dashboard-stream-read-v1)
