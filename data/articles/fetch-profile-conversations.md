---
title: "Fetch Profile Conversations"
slug: fetch-profile-conversations
url: https://dev.sprinklr.com/fetch-profile-conversations
---

# Fetch Profile Conversations

#
  POST Fetch Profile Conversations



This API call will help extract all the conversations related to an account, based on the respective channelType. For example, for Twitter, profile conversations could include posting a status, replying to a thread, sending a direct message, mentioning a profile in the comments section, etc.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/profile/conversations

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```







[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |

### Request Parameters






















			[Channel Type](https://dev.sprinklr.com/channels-v1)

****




































****








``


















| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| ProfileKey |  | Required | Object containing the channel details | Object |
|  | ChannelType | Required | of the profile.Example: Facebook, Twitter | String |
|  | ChannelId | Required | The unique Id of the channel on profile | String |
| SinceDate |  | Optional | The date since when you want the records | Integer |
| untilDate |  | Optional | The date till which you want the records | Integer |
| Sort |  | Optional | Object containing filters for response | Object |
|  | Key | Required | Refers to the type of results you want to see first 				For example: createdTime | String |
|  | Order | Optional | The order in which you want the results based on key parameter 				For example:ASC(ascending) | String |
| sourceType |  | Optional | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
| rows |  | Optional | The number of results you want in the response | Integer |

### Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/profile/conversations' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
   "profileKey": {
       "channelType": "TWITTER",
       "channelId": "859271732"
   },
   "sinceDate": "1583154891000",
   "untilDate": "1646226891000",
   "sort": {
       "key": "createdTime",
       "order": "ASC"
   },
   "sourceType": "ACCOUNT",
   "rows":"100"
}'






### Example - Response





{
               "draftId": 2016121530,
               "sourceType": "ACCOUNT",
               "sourceId": 1000068697,
               "content": {
                   "text": "@itest_2 update 1",
                   "richText": "@itest_2 update 1"
               },
               "channelMessageId": "1252594527199588354",
               "channelType": "TWITTER",
               "accountType": "TWITTER",
               "channelCreatedTime": 1587476782022,
               "senderProfile": {
                   "name": "Deep",
                   "channelType": "TWITTER",
                   "channelId": "859271732",
                   "permalink": "https://pbs.twimg.com/profile_images/478429801032597504/ihdJNAtu_normal.jpeg",
                   "bio": "Programming, Hacking, Security Vulnerability, Distributed and Cloud Computing, Massive Parallel Computing, Natural Language Processing, Artificial Intelligence",
                   "followers": 107,
                   "following": 88,
                   "username": "deep1",
                   "verified": false,
                   "unSubscribed": false,
                   "deleted": false,
                   "snCreatedTime": 0,
                   "snModifiedTime": 0,
                   "statusCount": 14550
               },
               "receiverProfile": {
                   "name": "Ish",
                   "channelType": "TWITTER",
                   "channelId": "2558964998",
                   "permalink": "https://pbs.twimg.com/profile_images/521948302422470660/IcZMwdMd_normal.jpeg",
                   "bio": "New places to go!",
                   "followers": 10,
                   "following": 20,
                   "username": "itest_2",
                   "verified": false,
                   "unSubscribed": false,
                   "deleted": false,
                   "snCreatedTime": 0,
                   "snModifiedTime": 0,
                   "statusCount": 2746
               },
               "mentionedProfiles": [
                   {
                       "name": "Ish",
                       "channelType": "TWITTER",
                       "channelId": "2558964998",
                       "followers": 0,
                       "following": 0,
                       "username": "itest_2",
                       "deleted": false,
                       "snCreatedTime": 0,
                       "snModifiedTime": 0,
                       "statusCount": 0
                   }
               ],
               "permalink": "https://twitter.com/deep1/status/1252594527199588354",
               "language": "en",
               "messageId": "ACCOUNT_1000068697_1587476782022_TWITTER_7_1252594527199588354",
               "postId": 2016121530,
               "brandPost": true,
               "createdTime": 1587476782932,
               "modifiedTime": 1587476783577,
               "textEntities": { },
                "location": {
                   "lat": 0.0,
                   "lon": 0.0
               },
               "insights": {
                   "POST_REACH_COUNT": 104.0
               },
               "workflow": {
                   "campaignId": "1000004679_2"
               },
               "enrichments": { },
               "conversationId": "1245676140502470660",
               "parentMessageId": "ACCOUNT_1000068697_1585827310096_TWITTER_4_1245676140502470660",
               "autoImported": true,
               "autoResponse": false
         }
       ],
       "hasMore": true,
       "unPublishedMessages": [
           {
               "id": 2078424949,
               "accountIds": [
                   1000067527
               ],
               "accountGroupIds": [],
               "inReplyToMessageId": "ACCOUNT_1000074730_1608571258499_TWITTER_4_1341071174248275970",
               "version": 11,
               "accountTypes": [
                   "TWITTER"
               ],
               "variantDetails": {
                   "variant": false,
                   "variantParentMessageId": "MESSAGE_2078424949",
                   "hasVariants": false
               },
               "content": {
                   "attachment": {
                       "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/1d458bf4-5f90-4e50-845e-3e40ba1315b2-183422575.jpg",
                       "title": "06.30.14 - Point of View-Firew.jpg",
                       "previewUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/8d7d3e27-7fff-4f27-95d0-83401de6c698-1075408478/06.30.14_-_Point_of_View-Firew_p.jpg",
                       "type": "IMAGE"
                   }
               },
               "channelOptions": [],
               "scheduleDate": 1608617680039,
               "taxonomy": {
                   "campaignId": "1000004679_1821",
                   "clientCustomProperties": {
                       "additionalProp1": [
                           "string"
                       ],
                       "additionalProp2": [
                           "string"
                       ],
                       "additionalProp3": [
                           "string"
                       ]
	      },
                   "partnerCustomProperties": {
                       additionalProp1": [
                           "string"
                       ],
                       "additionalProp2": [
                           "string"
                       ],
                       "additionalProp3": [
                           "string"
                       ]
	        },
                     "urlShortenerId": ""
               },
               "status": "DRAFT",
               "autoResponse": false,
               "createdTime": 1608617680039,
               "modifiedTime": 1637389544107,
               "authorId": 1000055246
           }
       ]
   },
   "errors": []
}








**Dev Notes: **`ParentMessageId` is only applicable for replies and comments and not to DMs (Direct Messages).

### Response Parameters







































****







****











			[type of channel](https://dev.sprinklr.com/channels-v1)














































``























































































































| Parameters | Sub-Parameters | Description | Type |
| --- | --- | --- | --- |
| DraftId |  | The Id of the post | Integer |
| sourceType |  | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
| SourceId |  | accountId or PS Id | Long |
| Content |  | Object containing post details | Object |
|  | text | The text in reply to post 				Includes: [replying To Profile Id] and [message] | String |
|  | richtext | The text in reply to a post 				Includes: [replying To Profile Id]] and [message] | String |
| channelMessageId |  | Id of the message on Native | Integer |
| channelType |  | The  for which the conversation is being recorded | String |
| AccountType |  | The type of the account for which the conversations are being recorded | String |
| channelcreatedTime |  | Time the message was created on native | Epoch |
| senderProfile |  | The profile from where the reply is being sent 				Refer to the table below for more information on senderProfile object | Object |
| ReceiverProfile |  | The profile to which the reply is being sent 				Refer to the table below for more information on receiverProfile object | Object |
| MentionedProfiles |  | Shows up only if one or more profiles are mentioned in the conversation 				Refer to the table below for more information on mentionedProfile object | Array |
| permalink |  | URL of the message on native | URL |
| language |  | The language of the conversation 				Example: en for english | String |
| messageId |  | Id of the message on Sprinklr’s platform | String |
| postId |  | The Id of the post | Integer |
| brandPost |  | Determines whether the post is a brand post or a fan post | boolean |
| createdTime |  | The time at which the post was created on Sprinklr's platform | Epoch |
| modifiedTime |  | The time at which the post was modified (in seconds) | Epoch |
| textEntities |  | Provides metadata and any additional details related to a post | Object |
| location |  | The location from where the post was published | Object |
|  | lat | The latitude coordinates of the location | String |
|  | lon | The longitude coordinates of the location | String |
| insights |  | Object containing information about post insights such as its reach and comment count | Object |
|  | POST_REACH_COUNT | The reach of the post since it was published | String |
|  | POST_COMMENT_COUNT | The comments received on the post since it was published | String |
| workflow |  | Describes the schema of partner level workflow in the message/case | Object |
|  | campaignId | The campaign under which the post was published | String |
| enrichments |  | List of enrichment metadata derived for a user | Object |
| conversationId |  | The conversation Id, generated on sprinklr w.r.t. a conversation | Integer |
| ParentMessageId |  | Id that uniquely identifies the parent message on Sprinklr | String |
| autoImported |  | If true, then the message was not published from Sprinklr’s platform. Instead, it has been imported | Boolean |
| autoResponse |  | Determines whether the message was auto published via bot or via rule | Boolean |

### Sender and Receiver Profile Parameters
















			[Channel type](https://dev.sprinklr.com/channels-v1)
































































| Parameter | Description | Type |
| --- | --- | --- |
| Name | Name of the sender/receiver | String |
| channelType | where the post is published | String |
| channelId | The Id associated with the channel type | Integer |
| permalink | The profile image URL of the sender/receiver | URL |
| bio | The profile bio of the sender/receiver | String |
| followers | The number of followers of sender/receiver | Integer |
| following | The number of people following sender/receiver | Integer |
| username | The username of the sender/receiver | String |
| verified | Determines whether the account is verified or not | String |
| unsubscribed | Determines whether the account is unsubscribed to receive post updates or not | String |
| Deleted | Determines whether the post has been deleted or not | String |
| snCreatedTime | Profile creation time on Native | Epoch |
| snModifiedTime | Profile modification time on Native | Epoch |
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
| snCreatedTime | Profile creation time on Native | Epoch |
| snModifiedTime | Profile modification time on Native | Epoch |
| statusCount | The number of statuses published by the mentioned profile | Integer |

For any unpublished message that has been scheduled for later, the response parameters include:

### hasMore Parameters





















| Parameters | Description | Type |
| --- | --- | --- |
| hasMore | Determines whether there are more conversations available for the respective profile | Boolean |
| unpublishedMessages | Details about any unpublished message | Array |

### unpublishedMessage Array Parameters




















































****










































































































****
































| Parameters | Sub-Parameters | Sub-Params | Description | Type |
| --- | --- | --- | --- | --- |
| Id |  |  | Post Id | Integer |
| accountIds |  |  | array of account ids where you want to send the message | Integer |
| accountGroupIds |  |  | The Ids of the dedicated groups where the message is sent | Integer |
| inReplyToMessageId |  |  | The messageId on which the reply is being sent | String |
| version |  |  | Current version of the message | Integer |
| accountTypes |  |  | The type of account being used.Example: Twitter | String |
| variantDetails |  |  | Determines whether there is another variant of the unpublished message | Object |
| content |  |  | The content associated with the unpublished message | Object |
|  | attachment |  | The attachment object containing attachments associated with the message | Object |
|  |  | url | The URL of the attachment | String |
|  |  | title | The title of the post (if any) | String |
|  |  | previewUrl | The preview URl of the message | String |
|  |  | type | The type of attachment | String |
| ChannelOptions |  |  | Channel specific options (if any) | String |
| scheduleDate |  |  | Scheduled date for publishing the message | Integer |
| taxonomy |  |  | Object containing taxonomy details | Object |
|  | campaignId |  | Campaign Id to associate the message with | String |
|  | clientCustomProperties |  | Client custom properties for the post | list |
|  | partnerCustomProperties |  | Partner custom properties for the post | list |
|  | urlShortnerId |  | URL shortener identifier to apply to the post | String |
| status |  |  | The current status of the messageExample: DRAFT | String |
| autoResponse |  |  | Determines whether the message was auto published via bot or via rule | Boolean |
| createdTime |  |  | The time at which the post was created on Sprinklr's platform | Epoch |
| modifiedTime |  |  | The time at which the message was modified | Epoch |
| authorId |  |  | The unique Id of the user sending the message | Integer |

[](https://dev.sprinklr.com/fetch-profile-conversations)




[Back to top](https://dev.sprinklr.com/fetch-profile-conversations)
