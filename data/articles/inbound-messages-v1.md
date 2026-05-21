---
title: "Inbound Messages v1"
slug: inbound-messages-v1
url: https://dev.sprinklr.com/inbound-messages-v1
---

# Inbound Messages v1

#  Inbound Messages v1

This object returns information for a given message inbound to Sprinklr.





| Fields | Type | Description |
| --- | --- | --- |
| partnerId | Long | Unique Id for partner |
| clientId | Long | Unique Id for client |
| sourceId | Long | accountId or PS Id |
| accountId | Long | Unique Id for the channel account added in the system |
| sourceType | String | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} |
| snType | String | Channel Type for the message |
| snMsgId | String | Unique message Identifier received from channel |
| messageType | Long | An inbound message has a MessageType |
| messageSubType | Long | StreamType |
| universalMessageId | String | Unique internal universal Id of message |
| campaignId | Integer | Unique campaign within the client |
| campaignClientId | Integer | Client Id |
| clientAndCampaignId | String | clientId plus campaignId |
| permalink | String | Message Permalink, that provide message link on channel |
| message | String | Message text |
| senderProfile | Custom | AudienceProfile |
| receiverProfile | custom | AudienceProfile |
| isSenderFollower | boolean | Is sender a follower |
| createdTime | Long | (Unix time of record creation)* 1000 |
| modifiedTime | Long | (Unix time of record modification)* 1000 |
| snCreatedTime | Long | (Unix time of SN message creation)* 1000 |
| snCreatedTimeYearMonth | String | SN Message creation year and month |
| snModifiedTime | Long | (Unix time of SN message mofied)* 1000 |
| actionTime (this currently is only for Stream API) | Long | (Unix time of message action)* 1000, action = assignment for workflow and action = snCreatedTime for inbox column |
| snStats | Map { String , Long} | Object storing message statistics |
| mediaList | List { Media Object} | Object for Media attachment |
| workflowProperties | MessageWorkflowProperties | Terms and Description table "MessageWorkflowProperties" given below |
| location | Object | Location object |
| language | String | language |
| conversationId | String | Unique conversation Identifier |
| parentSnMsgId | String | Unique Message ID of parent message of a message on channel |
| parentMsgType | Integer | Message Type of parent message of message |
| deleted | Boolean | Is Message deleted |
| archived | Boolean | Is Message archived |
| brandPost | Boolean | Is message brandpost or fan post |
| parentBrandPost | Boolean | Is parent post brandpost or fan post |
| hasBrandComment | Boolean | Does message have brand comment |
| hasConversation | Boolean | Does message have a conversation |
| hasApplicationConversation | Boolean | True, if it is enabled |
| restrictedChildAssetsMap | Map { String , List (String) } | Map of associated child assets |
| hasBrandResponded | Boolean | Does the brand Account responded in the conversation |
| hasScheduledComment | Boolean | Does the Post have any Scheduled Comment |
| hasParentPost | Boolean | Does the Parent have any post |
| textEntities |  | Terms and Description table "Text ; Entities and Base Text Entity" given below |
| numberOfComments | Long | Count of Comments |
| sFCaseCreationEnabled | Boolean | True, if it is enabled |
| canCreateSFCase | Boolean | True, if it is enabled |
| sFTaskCreationEnabled | Boolean | True, if it is enabled |
| canCreateSFTask | Boolean | True, if it is enabled |
| title | String | Tittle of the post |
| favorite | Boolean | True, if it is enabled |
| conversationMessages | Data | Data : List ( InboundMessage ), for linkedin,sina_weibo |

### MessageWorkflowProperties





| Fields | Type | Description |
| --- | --- | --- |
| sentiment | Integer | Message Sentiment value |
| priority | String | Message Priority |
| status | String | Message Status |
| isSpam | Boolean | Is message marked spam |
| isProfane | Boolean | Is message marked profane |
| userAssignmentDetails | Object | User Assignment attributes |
| tags | List (String) | tags |
| clientQueues | List ( Object ) | List of client queue assignment objects |
| partnerQueues | List ( Object ) | List of partner queue assignment objects |
| notifyUserIds | List{Integer} | List of user ids to send notifications to when the message properties change |
| partnerCustomProperties | Map {String, List (String) } | A map of partner custom properties key, values pair that message is assigned to. |
| processingUserDetailsList | List (Object) |  |

### Text Entities







| Fields | Type | Description |
| --- | --- | --- |
| mentions | custom | The locations of the mentions in the message BaseTextEntity |
| hashTags | custom | The locations of the hashtags in the message BaseTextEntity |
| urls | custom | The location of the URLs in the BaseTextEntity |
| messageHighlightOffsets | custom | The key words in the message which matched the topic query. |
| titleHighlightOffsets | custom | The key words in the message which matched the topic query. |

### Base Text Entity

The base structure of the text entity.







| Fields | Type | Description |
| --- | --- | --- |
| start | int | The start index |
| end | int | The end index |
| value | String | The value entity |

[](https://dev.sprinklr.com/inbound-messages-v1) 

 

 
[Back to top](https://dev.sprinklr.com/inbound-messages-v1)
