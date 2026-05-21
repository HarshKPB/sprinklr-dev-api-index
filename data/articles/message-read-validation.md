---
title: "Message Read Validation"
slug: message-read-validation
url: https://dev.sprinklr.com/message-read-validation
---

# Message Read Validation

# Message Read Validation



This API helps indicate that the message has been read by the end user.

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/{messageId}/messageRead

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.
















			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Path Parameters













| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| messageId | Required | Refers to the unique identifier for the message sent by the agent | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/6513d21819a98b52f41801df/messageRead' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \





### Example - Response



200 OK





**Dev Notes: **200 OK indicates that the API call has been executed successfully

[](https://dev.sprinklr.com/message-read-validation) 

 

 
[Back to top](https://dev.sprinklr.com/message-read-validation)
