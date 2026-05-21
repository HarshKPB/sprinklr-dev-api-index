---
title: "Message Action"
slug: message-action
url: https://dev.sprinklr.com/message-action
---

# Message Action

#
 POST Message Action



This API call will help perform different actions on messages such as `HIDE`, `UNHIDE`, `LIKE`, `UNLIKE`, `FAVORITE`, `UNFAVORITE`, `DELETE`, `APPROVE`, `REJECT`, etc. These actions are specific to native channel types.

**Dev Notes: **The mentioned actions are channel specific, i.e., not all actions will work for all channels.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/message/action

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

###  Request Parameters














``````````````














| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Action | Required | Can choose from a list of actions such as HIDE, UNHIDE, LIKE, UNLIKE, FAVORITE, UNFAVORITE, DELETE based on ChannelType | String |
| MessageId | Required | The Id of the message you want to perform action on | String |
| AccountId | Required | The Id of the account you want to perform the action from | Long |

**Dev Notes: **`messageId`= sourceType + “_”+ sourceId + “_” + ChannelCreatedTime + “_” + “[ChannelType](https://dev.sprinklr.com/channels-v1)” + “_” + ” [MessageType](https://dev.sprinklr.com/message-v1)“ +”_” + channelMessageId.

### Example: UNLIKE Twitter Replies















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/message/action' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
   "action": "UNLIKE",
   "messageId": "ACCOUNT_1000069102_1646154630069_TWITTER_7_1498707259974909953",
   "accountId": 1000069102
}'






### Example - Response





204 No Content







### Example: DELETE Twitter Replies















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/message/action' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"action": "DELETE",
"messageId": "ACCOUNT_1000069102_1646154630069_TWITTER_7_1498707259974909953",
"accountId": 1000069102
}'






## Example - Response





204 No Content






	[](https://dev.sprinklr.com/message-action)




[Back to top](https://dev.sprinklr.com/message-action)
