---
title: "Conversation Read v1"
slug: conversation-read-v1
url: https://dev.sprinklr.com/conversation-read-v1
---

# Conversation Read v1

# POST Conversation Read v1

Using this API, you can fetch message conversation details of the Post with different source type and channels.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/conversations/new/message-details

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

## Request Body Parameters





[Channel Type](https://dev.sprinklr.com/channels-v1)

[MessageType](https://dev.sprinklr.com/messages-v1)

[](https://dev.sprinklr.com/messages-v1)

| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| conversationId | Required | Its a unique id which combines all the associated message related to a post. | String |
| snMsgId | Required | Unique message Identifier received from channel. | String |
| sntype | Required | for the message. | String |
| sourceType | Required | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING, BENCHMARKING, AUDIENCE, AUDIENCE_STUDY}. | String |
| sourceId | Optional | accountId or PS Id. | Long |
| messageType | Required | Sprinklr supported message types messages are either inbound (from a channel) or outbound (posts to a channel). |  |
| parentLevelsToFetch | Optional | Parent level in integer to fetch the message. Default value = 2. | Integer |
| siblingsToFetch | Optional | Number of sibling of specific message to fetch. Default value = 4. | Integer |
| parentMsgType | Optional | Message Typeof parent message of message. | Integer |

## Example




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/conversations/new/message-details' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
   "conversationId":"1129005705577603072",
   "snMsgId":"1129005705577603072",
   "snType":"TWITTER",
   "sourceType":"LISTENING",
   "sourceId":-1,
   "messageType":4,
   "msgType":4,
   "parentLevelsToFetch":1,
   "siblingsToFetch":5,
   "parentMsgType":0,
   "sortOrder":"ASC"
}'

## Response:

You will get the response as per the request payload.

[](https://dev.sprinklr.com/conversation-read-v1)
