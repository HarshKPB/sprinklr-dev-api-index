---
title: "Start Typing API"
slug: start-typing-api
url: https://dev.sprinklr.com/start-typing-api
---

# Start Typing API

# Start Typing API



This API helps indicate that the customer is typing and replying to a case. The agent can see the "three dots" that implies that the user is typing.

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/{conversationId}/startTyping

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Path Parameters











| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| conversationId | Required | Refers to the unique identifier for the conversation that the sender initiated | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/653a34fa4b4051546cb90516/startTyping' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \





## Example - Response



200 OK





**Dev Notes: **200 OK indicates that the API call has been executed successfully

	[](https://dev.sprinklr.com/start-typing-api)

[Back to top](https://dev.sprinklr.com/start-typing-api)
