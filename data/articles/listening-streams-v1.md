---
title: "Listening Streams v1"
slug: listening-streams-v1
url: https://dev.sprinklr.com/listening-streams-v1
---

# Listening Streams v1

#
  POST Listening Streams



This endpoint returns the message stream associated with each message, containing the required information. It returns StreamWidgetResponse.

## API Endpoint

 https://api3.sprinklr.com/{env}/api/v1/listening/query/stream

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
  'https://api3.sprinklr.com/{env}/api/v1/listening/query/stream' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "sinceTime": "1544418000000",
    "untilTime": "1547152918520",
    "details": {
        "widgetType": "STREAM"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        }
    ],
    "metric": "MENTIONS",
    "timezoneOffset": 14400000,
    "rows": 100,
    "start": 1
}'






### Example - Response





{
    "status": "SUCCESS",
    "response": {
        "data": [
            {
                "favorite": false,
                "promotedOnly": false,
                "fromVerifiedProfile": false,
                "authorKlout": "10",
                "generator": "Sprinklr",
                "feedbackDM": false,
                "partnerId": 1090,
                "clientId": 5547,
                "sourceId": -1,
                "accountId": 999998,
                "sourceType": "LISTENING",
                "snType": "TWITTER",
                "snMsgId": "1082653160588693506",
                "messageType": 2,
                "messageSubType": 247,
                "universalMessageId": "TWITTER_2_1082653160588693506",
                "permalink": "https://twitter.com/show/status/1082653160588693506",
                "message": "#Dataviz of the day: Want a Doctorate? Eat More Cheese! Or, Not... https://t.co/qw1WcApXfv\n\n#statistics #JMP https://t.co/WjCkTduSF4",
                "textEntities":
	 {
                    "message": [
                        {
                            "indices": [
                                0,
                                8
                            ],
                            "hashtag": "Dataviz"
                        },
                        {
                            "indices": [
                                92,
                                103
                            ],
                            "hashtag": "statistics"
                        },
                        {
                            "indices": [
                                104,
                                108
                            ],
                            "hashtag": "JMP"
                        },
                        {
                            "indices": [
                                67,
                                90
                            ],
                            "url": "https://t.co/qw1WcApXfv"
                        },
                        {
                            "indices": [
                                109,
                                132
                            ],
                            "url": "https://t.co/WjCkTduSF4"
                        }
                    ]
                },
                "urlEntities": {
                    "message": [
                        {
                            "url": "https://t.co/qw1WcApXfv",
                            "expandedUrl": "https://public.jmp.com/packages/Want-a-Doctorate-Eat-More-Cheese-Or-Not/js-p/5c01fd17acf2c90f041dfac7?utm_source=TWITTER&utm_medium=social_sprinklr&utm_content=2069392323&utm_campaign=pub&linkId=62063256",
                            "displayUrl": "j.mp/2VINZBg"
                        }
                    ]
                },
                "senderProfile": {
                    "snType": "TWITTER",
                    "age": 0,
                    "location": "Cary, NC",
                    "snId": "966365508168765444",
                    "name": "JMP Public",
                    "screenName": "JMP_Public",
                    "bio": "JMP Public is the platform for sharing interactive @JMP_software #visualizations & #dashboards with the world. #dataviz #dataanalysis",
                    "subType": "",
                    "following": 2,
                    "followers": 6,
                    "favCount": 0,
                    "statusCount": 5,
                    "permalink": "https://twitter.com/JMP_Public",
                    "createdTime": "1519234466000",
                    "profileImgUrl": "http://pbs.twimg.com/profile_images/1080538130049126401/bTuuZWSw_normal.jpg",
                    "verified": false,
                    "profileWorkflowProperties": {
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
                    "universalProfileId": "5c34bb04e4b0f0df482ce2a0",
                    "participationIndex": 0,
                    "influencerIndex": 0,
                    "spamIndex": 0,
                    "accountsFollowedByUser": [],
                    "accountsFollowingUser": [],
                    "accountsUnFollowingUser": [],
                    "accountsUnFollowedByUser": [],
                    "accountsBlockingUser": [],
                    "accountsSuspendingUser": []
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
                    "participationIndex": 0,
                    "influencerIndex": 0,
                    "spamIndex": 0,
                    "accountsFollowedByUser": [],
                    "accountsFollowingUser": [],
                    "accountsUnFollowingUser": [],
                    "accountsUnFollowedByUser": [],
                    "accountsBlockingUser": [],
                    "accountsSuspendingUser": []
                },
                "isSenderFollower": false,
                "createdTime": 1546959620372,
                "modifiedTime": 1546959620372,
                "snCreatedTime": 1546959602864,
                "snCreatedTimeYearMonth": "2019_01",
                "snModifiedTime": 1546959602864,
                "actionTime": 1546959602864,
                "snStats": {
                    "reC": 2178,
                    "nF": 6,
                    "conLen": 132,
                    "iFsC": 10,
                    "fC": 5,
                    "nR": 2
                },
                "mediaList": [
                    {
                        "id": "1082653157719789568",
                        "type": "PHOTO",
                        "picture": "https://pbs.twimg.com/media/DwZbT5DX0AAoZxr.jpg",
                        "source": "https://t.co/WjCkTduSF4"
                    }
                ],
                "workflowProperties": {
                    "sentiment": -2,
                    "isSpam": false,
                    "isProfane": false,
                    "read": false
                },
	  "location": {
                    "text": "Cary, North Carolina, United States",
                    "lat": 35.79154,
                    "lon": -78.78112,
                    "additional": {
                        "country": "United States",
                        "stateCode": "NC",
                        "state": "North Carolina",
                        "code": "US",
                        "city": "Cary"
                    }
                },
	 "language": "en",
                "conversationId": "1082653160588693506",
                "parentMsgType": 0,
                "deleted": false,
                "archived": false,
                "brandPost": false,
                "parentBrandPost": false,
                "hasBrandComment": false,
                "hasScheduledComment": false,
                "hasParentPost": false,
                "hasApplicationConversation": false,
                "rootUniversalMessageId": "TWITTER_2_1082653160588693506",
                "isSharedPost": false,
                "hasConversation": false,
                "influencerScore": "10",
                "topicIds": [
                    "5b3a6fdde4b02dbcb7facd66"
                ],
	  "dataSource": "gFireOrig",
                "additionalInformation": {},
                "hasChildren": false,
                "userActions": []
            },
        "hasMore": true
    }
}







### Response Parameters














































































			[Channel Type](https://dev.sprinklr.com/channels-v1)













			[MessageType](https://dev.sprinklr.com/message-v1)





















































































			[Channel Type](https://dev.sprinklr.com/channels-v1)





























































































































































































			[](https://developer.sprinklr.com/docs/read/messages)









































































			``
































































| Parameter | Sub Parameter | Sub Parameter Object | Description | Type |
| --- | --- | --- | --- | --- |
| favorite |  |  | If True, favorite selected | Boolean |
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
| messageSubType |  |  | StreamType | Long |
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
| additionalInformation |  |  | Addition information about stream.The information contain the product insight details and will appear in response only if the Product Insight is enabled |  |
|  | intel |  |  |  |
|  |  | source | Message native source. | String |
|  |  | assetTitle | Tittle of the asset. | String |
|  |  | assetType | Type of asset. | String |
|  |  | assetId | Id of the asset. | String |
|  | hasChildren |  | Does it has children messages. | Boolean |
| userActions |  |  | Actions taken by user. | list |
|  | detectedSurveyMessage |  | If True, it is enabled. | Boolean |

[](https://dev.sprinklr.com/listening-streams-v1)






[Back to top](https://dev.sprinklr.com/listening-streams-v1)
