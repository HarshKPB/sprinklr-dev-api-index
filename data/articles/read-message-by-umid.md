---
title: "Read Message by UMID"
slug: read-message-by-umid
url: https://dev.sprinklr.com/read-message-by-umid
---

# Read Message by UMID

#
  GET Read Message by UMID


Using this API, you can fetch message details using UMID (Universal Message Id).

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/message

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

### Query Parameter

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Refers to the universal message Id associated with the message. When viewing on the Sprinklr platform, you can view this UMID within the "Properties" section of the message details pane | String |

## Example - Request




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/message?id=TWITTER_2_1790374689384051060' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example - Response




{
    "data": {
        "sourceType": "ACCOUNT",
        "sourceId": 600049002,
        "content": {
            "title": "TELL ME THEY DIDNT JUST SAY THAT ",
            "text": "
We’re live pal.
",
            "attachment": {
                "url": "https://v.redd.it/099a9xy2qyyc1/DASH_720.mp4?source=fallback",
                "previewUrl": "url",
                "type": "VIDEO"
            },
            "isRichText": false
        },
        "channelMessageId": "1cm6oxn",
        "channelType": "REDDIT",
        "accountType": "SUBREDDIT",
        "channelCreatedTime": 1715069514000,
        "senderProfile": {
            "name": "Late_Cookie_7797",
            "channelType": "REDDIT",
            "channelId": "Late_Cookie_7797",
            "permalink": "https://www.reddit.com/user/Late_Cookie_7797",
            "followers": 0,
            "following": 0,
            "username": "Late_Cookie_7797",
            "verified": true,
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 1679646101000,
            "snModifiedTime": 1679646101000,
            "statusCount": 0,
            "accountSpecificInfos": [],
            "additional": {
                "id": [
                    "d4xoyux5"
                ]
            },
            "url": "https://www.reddit.com/user/Late_Cookie_7797"
        },
        "permalink": "https://www.reddit.com/r/HolUp/comments/1cm6oxn/tell_me_they_didnt_just_say_that/",
        "language": "en",
        "messageId": "ACCOUNT_600049002_1715069514000_REDDIT_267_1cm6oxn",
        "brandPost": false,
        "createdTime": 1715069609506,
        "modifiedTime": 1715119864466,
        "textEntities": {},
        "insights": {
            "POST_COMMENT_COUNT": 2.0
        },
        "workflow": {
            "modifiedTime": 1715702412954,
            "customProperties": {
                "_c_652e7ef8e85ac50718f5d9e1": [
                    "HolUp"
                ]
            },
            "queues": [],
            "spaceWorkflows": []
        },
        "enrichments": {
            "sentiment": 0,
            "flaggedWords": {
                "allFlaggedWords": [],
                "imageFlaggedWords": [],
                "messageFlaggedWords": [],
                "videoFlaggedWords": []
            }
        },
        "conversationId": "1cm6oxn",
        "autoImported": false,
        "autoResponse": false
    },
    "errors": []
}





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

[](https://dev.sprinklr.com/read-message-by-umid)




[Back to top](https://dev.sprinklr.com/read-message-by-umid)
