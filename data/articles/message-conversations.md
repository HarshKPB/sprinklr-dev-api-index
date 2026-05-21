---
title: "Message Conversations"
slug: message-conversations
url: https://dev.sprinklr.com/message-conversations
---

# Message Conversations

#
  POST Message Conversations




This API call will help extract all the conversation details related to a particular message.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/message/conversations

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
| Content-Type | multipart/form-data; boundary=<calculated when request is sent> | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

**Dev Notes: **[Profile conversations](https://dev.sprinklr.com/fetch-profile-conversations) API provides details regarding all the messages that exist for a particular profile. Whereas, message conversations API provides all the details w.r.t. a particular message.

###  Request Parameters


























        [type of message](https://dev.sprinklr.com/message-v1)



















****









| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| messageId | Required | Unique message Id related to the message | String |
| parentSnMsgId | Optional | The unique parent message Identifier received from channel | String |
| msgTypes | Optional | The | String |
| sinceDate | Optional | The date in milliseconds since  when you want to pull message conversations | Long [Unix Epoch] |
| untilDate | Optional | The date in milliseconds till  when you want to pull message conversations | Long [Unix Epoch] |
| start | Optional | The start offset that determines where to begin pulling data from.The default is 0. | Integer |
| rows | Optional | The number of rows you want in the response. The default value is 21 if not passed. | Integer |

**Dev Notes: **`messageId`= **sourceType** (ACCOUNT, PERSISTENT_SEARCH, LISTENING) + “_”+ **sourceId** + “_” + **channelCreatedTime** + “_” + “**[channelType](https://dev.sprinklr.com/channels-v1)**” + “_” + ” **[messageType](https://dev.sprinklr.com/message-v1)**“ +”_” + **channelMessageId**

### Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/message/conversations' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
    "messageId": "ACCOUNT_1000070103_1649437654240_TWITTER_5_1647140850_902522372057571430",
    "parentSnMsgId":"1647140850_902522372057571430",
    "msgTypes":5,
    "sinceDate":1581172111000,
    "untilDate":1649826760000,
    "start":0,
    "rows":1
}'






### Example - Response





{
    "data": [
        {
            "draftId": 2090566610,
            "sourceType": "ACCOUNT",
            "sourceId": 1000070103,
            "content": {
                "title": "",
                "text": ""
            },
            "channelMessageId": "1512652734423512131",
            "channelType": "TWITTER",
            "accountType": "TWITTER",
            "channelCreatedTime": 1649479490272,
            "senderProfile": {
                "channelType": "TWITTER",
                "channelId": "1647140850",
                "permalink": "https://pbs.twimg.com/profile_images/412497031899074560/Sy27IH1Q_normal.jpeg",
                "followers": -1,
                "following": -1,
                "unSubscribed": false,
                "deleted": false,
                "snCreatedTime": 0,
                "snModifiedTime": 0,
                "statusCount": -1
            },
            "language": "en",
            "messageId": "ACCOUNT_1000070103_1649479490272_TWITTER_5_1512652734423512131",
            "postId": 2090464351,
            "brandPost": true,
            "createdTime": 1649479490555,
            "modifiedTime": 1649479827376,
            "textEntities": {},
            "insights": {},
            "workflow": {
                "modifiedTime": 1649479827376,
                "customProperties": {},
                "queues": [
                    {
                        "queueId": 17,
                        "assignmentTime": 1649479490743
                    }
                ],
                "spaceWorkflows": [],
                "campaignId": "1000004201_762"
            },
            "enrichments": {},
            "parentMessageId": "ACCOUNT_1000070103_1649437883290_TWITTER_5_1512478222092582025",
            "autoImported": false,
            "autoResponse": false,
            "apiStatus": "Removed fields because of resyndication policy"
        }
    ],
    "errors": []
}







**Dev Notes:**The API response depends on the channel where the message exists

###  Response Parameters

























































            [type of channel](https://dev.sprinklr.com/channels-v1)








































****


























































































































| Parameters | Sub-Parameters | Description | Type |
| --- | --- | --- | --- |
| draftId |  | The draft Id of the message | Integer |
| sourceType |  | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
| sourceId |  | accountId or PS Id | String |
| content |  | Object containing message details | Object |
|  | title | The title of the message (if any) | String |
|  | text | The text of the message | String |
|  | attachment | Refers to the object containing the attachments present on the message (if any) Refer to the table below for the attachment object details | Object |
|  | isRichText | If true, the context is a rich text format | Boolean |
| channelMessageId |  | Id of the message on Native | String |
| channelType |  | The  where the message exists | String |
| accountType |  | The type of account where the message exists | String |
| channelCreatedTime |  | Time the message was created in native | Epoch |
| senderProfile |  | Refers to the object containing the sender profile detailsRefer to the table below for senderProfile object details | Array |
| receiverProfile |  | Refers to the object containing the receiver profile detailsRefer to the table below for receiverProfile object details | Array |
| mentionedProfiles |  | Array that stores information about the mentionedProfilesRefer to the table below for mentionedProfiles array details | Array |
| language |  | The language used in the native channelExample: “en” for EnglishRefer to the table below for commonly used language codes | String |
| messageId |  | Refers to the unique identifier for the message sent by the sender | String |
| postId |  | Post Id of the message | String |
| brandPost |  | If true, the message has been sent by the brand | Boolean |
| createdTime |  | Time at which the message was created | Epoch |
| modifiedTime |  | The time at which the message was modified | Epoch |
| textEntities |  | Provides metadata and any additional details related to a message | Object |
| Insights |  | Refers to the object containing the message insights such as:POST_REACH_COUNT, POST_COMMENT_COUNT | Object |
| workflow |  | workflow properties related to the message | Object |
|  | modifiedTime | The time at which the message was modified | Epoch |
|  | customProperties | Custom properties related to the message | Object |
|  | queues | The queue in which the message has been added. Refer to the table below for the queue array details | Array |
|  | spaceWorkflows | SpaceWorkflows are the workflow properties that are specific to a space (Earlier known as client). This has attributes like client queues and client custom fields. | Object |
|  | campaignId | The campaign under which the message is published | String |
| enrichments |  | List of enrichment metadata derived for a userRefer to the table below for enrichments object description | Object |
| conversationMessageId |  | Refers to the unique identifier for the conversation | String |
| parentMessageId |  | Unique universal Id of the message | String |
| autoImported |  | If True, thenthe message was not published by sprinklr. It has been imported | Boolean |
| autoResponse |  | If true, thenthe message was auto published via bot or via rule | Boolean |
| apiStatus |  | Describes the status of the API | String |

### attachment Object Description Table










| Parameters | Description | Type |
| --- | --- | --- |
| url | Refers to the URL of the attachment | String |
| title | Refers to the title of the attachment | String |
| previewUrl | Refers to the preview Url link of the attachment | String |
| type | Refers to the type of the attachment such as IMAGE, VIDEO, AUDIO, DOC | String |

### Commonly Used Language Codes










| Language | Code |
| --- | --- |
| English (US) | en |
| Deutsch (German) | d |
| Español (Spanish) | es |
| Français (France) | fr |
| Italiano (Italian) | it |
| Português (Brasil) | pt |
| Русский (Russian) | ru |
| (Arabic) | ar |
| (Chinese) | zh |

### Sender Profile/Receiver/Mentioned Profile Parameter Description Table

































































| Parameters | Description | Type |
| --- | --- | --- |
| name | Refers to the name associated with the user profile | String |
| channelType | The type of channel where the profile exists | String |
| channelId | Channel Id associated with the profile on the native | String |
| avatarUrl | Refers to the avatar Url associated with the profile picture | String |
| profileImageUrl | Refers to the display picture Url of the profile as available on the native channel | String |
| permalink | Profile URL on the native channel | URL |
| followers | Number of followers for the respective profile | Integer |
| following | Number of people the user is following | Integer |
| username | Refers to the username of the user as mentioned on the native channel | String |
| unSubscribed | If true, the profile has been unsubscribed | Boolean |
| deleted | If true, the profile is deleted on the native | Boolean |
| snCreatedTime | Refers to the profile creation time on native | Epoch |
| snModifiedTime | Refers to the profile modified time on native | Epoch |
| statusCount | The number of statuses published from the profile | Integer |
| accountSpecificInfos | Refers to the object containing the meta data associated with the accountRefer to the table below for accountSpecificInfos object details | Object |
| additional | Refers to the object containing the additional details associated with the profile | Object |

## Queues Array Description Table










| Parameters | Description | Type |
| --- | --- | --- |
| queueId | Refers to the unique identifier for the queue where the message has been added | Integer |
| assignmentTime | Refers to the time at which the message was added to the given queue | Epoch (milliseconds) |

## Enrichments Object Description Table











| Parameters | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| sentiment |  | Refers to the sentiment of the message, i.e., positive, negative, or neutral | Integer |
| flaggedWords |  | Refers to the object containing the flagged words | Object |
|  | allFlaggedWords | Refers to the list of all the flagged words | List [String] |
|  | imageFlaggedWords | Refers to the list of flagged words present in the images | List [String] |
|  | messageFlaggedWords | Refers to the list of flagged words present in the message | List [String] |
|  | videoFlaggedWords | Refers to the list of flagged words present in the video | List [String] |

## Account Specific Infos Object Description Table










| Parameters | Description | Type |
| --- | --- | --- |
| accountId | Refers to the unique identifier for the brand's social account existing within Sprinklr | Integer |
| lastBrandEngagedTime | Refers to the time at which the brand last replied on the message | Epoch (milliseconds) |
| lastFanEngagedTime | Refers to the time at which the customer last replied on the message | Epoch (milliseconds) |
| activeUser | If true, the user has a active social account | Boolean |

[](https://dev.sprinklr.com/message-conversations)




[Back to top](https://dev.sprinklr.com/message-conversations)
