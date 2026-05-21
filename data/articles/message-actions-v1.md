---
title: "Message Actions v1"
slug: message-actions-v1
url: https://dev.sprinklr.com/message-actions-v1
---

# Message Actions v1

# POST Message Actions v1

You can use this API to perform different actions on Messages like ` HIDE, UNHIDE, LIKE, UNLIKE, FAVORITE, UNFAVORITE, DELETE` and many more specific to native channel type

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/message/action

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters




















































































| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| universalMessageKey |  | Required | The universal message object containing message details. |  |
|  | snType | Required | The social network type. e.g. TWITTER | String |
|  | msgType | Required | The socail message type like Post or Reply etc. | String |
|  | snMsgId | Required | The social network message Id. | String |
|  | sourceId | Required | The sourceId/accountId existing in Sprinklr on which fan replied or from which the brand posted. | String |
|  | sourceType | Required | The source type of the message. | String |
|  | snCreatedTime | Optional | The message created time. | Epoch |
| channelType |  | Required | The social network type. e.g. TWITTER | String |
| accountId |  | Required | The accountId of the account within Sprinklr on which fan replied or from which the brand posted. | Long |
| action |  | Required | The action that needs to be performed on message. | String |

## SN-Message Actions










			``



| snType | Actions |
| --- | --- |
| TWITTER | HIDE, UNHIDE, LIKE, UNLIKE, FAVORITE, UNFAVORITE, DELETE |

## Example: Hide Twitter Replies




 Copy Code



curl -X POST \
  https://api2.sprinklr.com/{env}/api/v1/message/action \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
-d '{
    "universalMessageKey": {
        "snType": "TWITTER",
        "msgType": "7",
        "snMsgId": "1307965381303123969",
        "sourceId": "228770",
        "sourceType": "ACCOUNT",
        "snCreatedTime": 0
    },
    "channelType": "TWITTER",
    "accountId": 228770,
    "action": "HIDE"
}'

## Example - Response




204 No Content

## Example: Delete Tweet




 Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v1/message/action \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
-d '{
    "universalMessageKey": {
        "snType": "TWITTER",
        "msgType": "2",
        "snMsgId": "1307965381303123919",
        "sourceId": "228770",
        "sourceType": "ACCOUNT",
        "snCreatedTime": 0
    },
    "channelType": "TWITTER",
    "accountId": 228770,
    "action": "DELETE"
}'

## Example - Response




204 No Content

[](https://dev.sprinklr.com/message-actions-v1)
