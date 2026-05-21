---
title: "Read Message by ID"
slug: read-message-by-id
url: https://dev.sprinklr.com/read-message-by-id
---

# Read Message by ID

#
  GET Read Message by ID



Using this API, you can fetch the content of the message for the given message Id. The message can either be on a post, reply, direct message, or on a case.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/message/byMessageId

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

### Query Parameters



****

- [Read Case by Case Number API](https://dev.sprinklr.com/read-case-by-case-number)
- [Fetch Case Associated Messages API](https://dev.sprinklr.com/case-associated-messages)
- [Read Message by Message Id API](https://dev.sprinklr.com/read-message-by-id)[Read Bulk Messages API](https://dev.sprinklr.com/read-messages-bulk)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| messageId | Required | Refers to the unique identifier for the message.How to Retrieve Message Id Associated with a Case?Use  to fetch the case Id  associated to the caseUse  to retrieve all the message Ids associated with the caseUse  to retrieve the message content. Alternatively, you can also use  to fetch all the messages associated with the case for the given message Ids | String |

**Dev Notes: **`messageId`= **sourceType** (ACCOUNT, PERSISTENT_SEARCH, LISTENING) + “_”+ **sourceId** + “_” + **channelCreatedTime** + “_” + “**[channelType](https://dev.sprinklr.com/channels-v1)**” + “_” + ” **[messageType](https://dev.sprinklr.com/message)**“ +”_” + **channelMessageId**

## Example 1 - Fetch Reply















Copy Code



curl -X GET \
'https://api3.sprinklr.com/{env}/api/v2/message/byMessageId?messageId=ACCOUNT_600039042_1649218507139_TWITTER_7_1511558084136687456' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
    "data": {
        "sourceType": "ACCOUNT",
        "sourceId": 600039042,
        "content": {
            "text": "@bdee @shaun",
            "richText": "@bdee @shaun"
        },
        "channelMessageId": "1511558084136687456",
        "channelType": "TWITTER",
        "accountType": "TWITTER",
        "channelCreatedTime": 1649218505306,
        "senderProfile": {
            "name": "Raq",
            "channelType": "TWITTER",
            "channelId": "1062932421388132786",
            "permalink": "https://twitter.com/Raq1",
            "avatarUrl": "https://abz.twimg.com/sticky/default_profile_images/default_profile.png",
            "bio": "",
            "followers": 2,
            "following": 38,
            "username": "Raq1",
            "verified": false,
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 0,
            "snModifiedTime": 0,
            "statusCount": 94
        },
        "receiverProfile": {
            "name": "bdee",
            "channelType": "TWITTER",
            "channelId": "859271786",
            "permalink": "https://twitter.com/bdee",
            "avatarUrl": "https://pbs.twimg.com/profile_images/478429801032597501/ihdJNAtu.jpeg",
            "bio": "Programming, Hacking, Security Vulnerability, Distributed and Cloud Computing, Massive Parallel Computing, Natural Language Processing, Artificial Intelligence",
            "followers": 107,
            "following": 86,
            "username": "bdee",
            "verified": false,
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 0,
            "snModifiedTime": 0,
            "statusCount": 14553
        },
        "mentionedProfiles": [
            {
                "name": "bdee",
                "channelType": "TWITTER",
                "channelId": "859271786",
                "followers": 0,
                "following": 0,
                "username": "bdee",
                "deleted": false,
                "snCreatedTime": 0,
                "snModifiedTime": 0,
                "statusCount": 0
            },
            {
                "name": "Himan",
                "channelType": "TWITTER",
                "channelId": "1422199331818409876",
                "followers": 0,
                "following": 0,
                "username": "himansays",
                "deleted": false,
                "snCreatedTime": 0,
                "snModifiedTime": 0,
                "statusCount": 0
            }
        ],
        "permalink": "https://twitter.com/Himansays/status/1511558084136687456",
        "language": "fr",
        "messageId": "ACCOUNT_600039042_1649218505306_TWITTER_7_1511558084136687456",
        "postId": 600000006735621,
        "brandPost": false,
        "createdTime": 1649218507139,
        "modifiedTime": 1649218507567,
        "textEntities": {
            "message": [
                {
                    "indices": [
                        0,
                        11
                    ],
                    "screenName": "bdee"
                },
                {
                    "indices": [
                        12,
                        26
                    ],
                    "screenName": "himan"
                }
            ]
        },
        "location": {
            "lat": 0.0,
            "lon": 0.0
        },
        "insights": {
            "POST_REACH_COUNT": 2.0
        },
        "workflow": {
            "modifiedTime": 1649218507879,
            "customProperties": {},
            "queues": [
                {
                    "queueId": 101416,
                    "assignmentTime": 1649218507840
                }
            ],
            "spaceWorkflows": [],
            "campaignId": "2_11"
        },
        "enrichments": {
            "sentiment": 0
        },
        "conversationId": "1443895480526598150",
        "parentMessageId": "ACCOUNT_600039042_1634191118951_TWITTER_7_1448528657438359564",
        "autoImported": true,
        "autoResponse": false
    },
    "errors": []
}







**Dev Notes: **`parentMessageId`= sourceType + “_”+ AccountId + “_” + createdTime + “_” + “[ChannelType](https://dev.sprinklr.com/channels-v1)” + “_” + ” [MessageType](https://dev.sprinklr.com/message)“ +”_” + parentSnMsgId

Also, `ParentMessageId`is only applicable for replies and comments and not to DMs (Direct Messages).

## Example 2 - Fetch Call Recording















Copy Code



curl -X GET \
'https://api3.sprinklr.com/{env}/api/v2/message/byMessageId?messageId=ACCOUNT_1000105495_1684304685007_SPRINKLR_VOICE_382_6464732fc4dad52567e0eed8' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
    "data": {
        "sourceType": "ACCOUNT",
        "sourceId": 1000105495,
        "content": {
            "text": "",
            "attachment": {
                "commands": [
                    {
                        "recordingDuration": 133344.0,
                        "recordingUrl": "https://s3.amazonaws.com/spr-uploads-pz/VOICE/app_1000105495_TW/17/05/2023/CONV_RECORD_1684304799371_3282864545560506599.mp3",
                        "contentType": "audio/mp3",
                        "encryptedRecording": false,
                        "downloadDisabled": false,
                        "botRecording": false,
                        "recordingId": "0000018828618a34e4b0ed4e9f9f92dc_1684304665160",
                        "type": "RECORDED_CALL"
                    }
                ],
                "type": "VOICE"
            }
        },
        "channelMessageId": "000001882863aa05e4b0ed4e9f9f92e4",
        "channelType": "SPRINKLR_VOICE",
        "accountType": "SPRINKLR_VOICE",
        "channelCreatedTime": 1684304800261,
        "senderProfile": {
            "name": "RM Twilio app",
            "channelType": "SPRINKLR_VOICE",
            "channelId": "60c3900467beee23512c84ee",
            "followers": 0,
            "following": 0,
            "username": "RM Twilio app",
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 0,
            "snModifiedTime": 1684912875039,
            "statusCount": 0,
            "accountSpecificInfos": [],
            "additional": {}
        },
        "receiverProfile": {
            "name": "+918085076029",
            "channelType": "SPRINKLR_VOICE",
            "channelId": "+918085076029",
            "followers": 0,
            "following": 0,
            "username": "+918085076029",
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 0,
            "snModifiedTime": 1684304661046,
            "statusCount": 0,
            "accountSpecificInfos": [],
            "additional": {
                "PHONE_NO": [
                    "8085076029"
                ],
                "COUNTRY_CODE": [
                    "+91"
                ]
            }
        },
        "messageId": "ACCOUNT_1000105495_1684304800261_SPRINKLR_VOICE_384_000001882863aa05e4b0ed4e9f9f92e4",
        "brandPost": true,
        "createdTime": 1684304800425,
        "modifiedTime": 1684304800425,
        "textEntities": {},
        "insights": {},
        "workflow": {},
        "enrichments": {
            "sentiment": 0,
            "flaggedWords": {
                "allFlaggedWords": [],
                "imageFlaggedWords": [],
                "messageFlaggedWords": [],
                "videoFlaggedWords": []
            }
        },
        "conversationId": "0000018828618a34e4b0ed4e9f9f92dc",
        "autoImported": false,
        "autoResponse": false
    },
    "errors": []
}







## Example 3 - Fetch Call Transcript















Copy Code



curl -X GET \
'https://api3.sprinklr.com/{env}/api/v2/message/byMessageId?messageId=ACCOUNT_1000105495_1684304685007_SPRINKLR_VOICE_382_6464732fc4dad52567e0eed8' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
    "data": {
        "sourceType": "ACCOUNT",
        "sourceId": 1000105495,
        "content": {
            "text": "I.",
            "attachment": {
                "commands": [
                    {
                        "startTime": 19847,
                        "endTime": 21567,
                        "duration": 1720,
                        "interactionId": "6464732fc4dad52567e0eed8",
                        "callStartTime": 1684304673307,
                        "recordingOffset": 8147,
                        "lastPacketReceivedTime": 1684304686839,
                        "vadResponseTime": 1684304687057,
                        "asrResponseTime": 1684304687394,
                        "convEventReceivedTime": 1684304687508,
                        "recordingId": "0000018828618a34e4b0ed4e9f9f92dc_1684304665160",
                        "type": "TRANSCRIPT"
                    }
                ],
                "type": "VOICE"
            }
        },
        "channelMessageId": "6464732fc4dad52567e0eed8",
        "channelType": "SPRINKLR_VOICE",
        "accountType": "SPRINKLR_VOICE",
        "channelCreatedTime": 1684304685007,
        "senderProfile": {
            "name": "+918085076029",
            "channelType": "SPRINKLR_VOICE",
            "channelId": "+918085076029",
            "followers": 0,
            "following": 0,
            "username": "+918085076029",
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 0,
            "snModifiedTime": 1684304661046,
            "statusCount": 0,
            "accountSpecificInfos": [],
            "additional": {
                "PHONE_NO": [
                    "8085076029"
                ],
                "COUNTRY_CODE": [
                    "+91"
                ]
            }
        },
        "receiverProfile": {
            "name": "RM Twilio app",
            "channelType": "SPRINKLR_VOICE",
            "channelId": "60c3900467beee23512c84ee",
            "followers": 0,
            "following": 0,
            "username": "RM Twilio app",
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 0,
            "snModifiedTime": 1684931145134,
            "statusCount": 0,
            "accountSpecificInfos": [],
            "additional": {}
        },
        "language": "hr",
        "messageId": "ACCOUNT_1000105495_1684304685007_SPRINKLR_VOICE_382_6464732fc4dad52567e0eed8",
        "brandPost": false,
        "createdTime": 1684304687715,
        "modifiedTime": 1684304687715,
        "textEntities": {},
        "insights": {},
        "workflow": {
            "modifiedTime": 1684304692599,
            "customProperties": {
                "spr_im_predicted_csat_rating": [
                    "54"
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
        "conversationId": "0000018828618a34e4b0ed4e9f9f92dc",
        "autoImported": false,
        "autoResponse": false
    },
    "errors": []
}







### Response Parameters















            ``````






















****








****













        [type of channel](https://dev.sprinklr.com/channels-v1)






        [account type](https://dev.sprinklr.com/bootstrap-api-v1)














































``







































































































































































































| Parameters | Sub-Params | Sub-Params | Description | Type |
| --- | --- | --- | --- | --- |
| sourceType |  |  | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
| sourceId |  |  | accountId or PS Id | Long |
| content |  |  | Object containing message details | Object |
|  | text |  | The text of the message         Includes: [replying To Profile Id] and [message] | String |
|  | richtext |  | The text in reply to a post         Includes: [replying To Profile Id]] and [message] | String |
| channelMessageId |  |  | The unique identifier for the channel | Integer |
| channelType |  |  | The  used to publish/send message | String |
| AccountType |  |  | The  where the message exists | String |
| channelcreatedTime |  |  | The time at which the conversation was created (in seconds) | Integer |
| senderProfile |  |  | The profile from where the reply is being sent         Refer to the table below for more information on senderProfile object | Object |
| ReceiverProfile |  |  | The profile to which the reply is being sent         Refer to the table below for more information on receiverProfile object | Object |
| MentionedProfiles |  |  | Shows up only if a profile is mentioned in the conversation         Refer to the table below for more information on mentionedProfile object | Array |
| permalink |  |  | The URI of the conversation thread | String |
| language |  |  | The language of the conversation         Example: en for english | String |
| messageId |  |  | The Id of the message the action is performed on | String |
| postId |  |  | The Id of the post | Integer |
| brandPost |  |  | Determines whether the post is made from a brand/company account or not | boolean |
| createdTime |  |  | The time at which the post was created (in seconds) | Integer |
| modifiedTime |  |  | The time at which the post was modified (in seconds) | Integer |
| textEntities |  |  | Provides metadata and any additional details related to a post | Object |
|  | message |  | Array of text entities included in the post | Array |
|  |  | Indices | The character positions from where the entity is mentioned | list |
|  |  | screenName | The screen name of mentioned profiles | String |
| location |  |  | The location from where the post was published | Object |
|  | lat |  | The latitude coordinates of the location | String |
|  | lon |  | The longitude coordinates of the location | String |
| insights |  |  | Object containing information about post insights such aits reach and comment count | Object |
|  | POST_REACH_COUNT |  | The reach of the post since it was published | String |
| workflow |  |  | Object containing details of the post such as campaign Id | Object |
|  | modifiedTime |  | The time at which the post was modified | Integer |
|  | customProperties |  | Client and partner custom properties for the post | list |
|  | queues |  | Array of queues in which the message has been added | Array |
|  |  | queueId | The Id of the queue | Integer |
|  |  | assignmentTime | The time at which the queue was created | Integer |
|  | spaceWorkflows |  | The space related workflow properties | Object |
|  | campiagnId |  | The campaign under which the post was published | String |
| enrichments |  |  | List of enrichment metadata derived for a user | Object |
|  | sentiment |  | The sentiment score of the post | String |
| conversationId |  |  | Each of the replies has a conversation Id, which matches to the original post Id | Integer |
| ParentMessageId |  |  | Unique universal Id of the post | String |
| autoImported |  |  | Determines whether the data associated with the post is auto imported or not | Boolean |
| autoResponse |  |  | Determines whether the account has auto response enabled or not | Boolean |

### Sender and Receiver Profile Parameters
















            [Channel type](https://dev.sprinklr.com/channels-v1)
































































| Parameter | Description | Type |
| --- | --- | --- |
| Name | Name of the sender/receiver | String |
| channelType | where the post is published | String |
| channelId | The Id associated with the channel type | Integer |
| permalink | The profile image of the sender/receiver | String |
| bio | The profile bio of the sender/receiver | String |
| followers | The number of followers of sender/receiver | Integer |
| following | The number of people following sender/receiver | Integer |
| username | The username of the sender/receiver | String |
| verified | Determines whether the account is verified or not | String |
| unsubscribed | Determines whether the account is unsubscribed to receive post updates or not | String |
| Deleted | Determines whether the post has been deleted or not | String |
| snCreatedTime | The time at which the sent/received post was created | Integer |
| snModifiedTime | The time at which the sent’/received post was modified | Integer |
| statusCount | The number of statuses published by sender/receiver | Integer |

### Mentioned Profiles Array Parameters





























































| Parameter | Description | Type |
| --- | --- | --- |
| Name | The name of the mentioned profile in the post or the comments | String |
| channelType | The channel type used to publish the post | String |
| channelId | The Id associated with the channel type | Integer |
| followers | The number of followers of the mentioned profile | Integer |
| following | The number of people followed by the mentioned profile | Integer |
| username | The username of the mentioned profile | String |
| deleted | Determines whether the comment mentioning the profile has been deleted or not | String |
| snCreatedTime | The time at which the profile was mentioned (in seconds) | Integer |
| snModifiedTime | The time at which the comment with the mention was last modified | Integer |
| statusCount | The number of statuses published by the mentioned profile | Integer |

	[](https://dev.sprinklr.com/read-message-by-id)




[Back to top](https://dev.sprinklr.com/read-message-by-id)
