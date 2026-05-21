---
title: "Close Conversation API"
slug: close-conversation-api
url: https://dev.sprinklr.com/close-conversation-api
---

# Close Conversation API

# Close Conversation API



This API allows closing an existing conversation within the live chat application

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/closeConversation

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Query Parameters












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| conversationId | Required | Refers to the unique identifier for the conversation you want to close | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/closeConversation?conversationId=6512d36980feaa5b29b846c5' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \





### Example - Response



200 OK





**Dev Notes: **200 OK indicates that the API call has been executed successfully

	[](https://dev.sprinklr.com/close-conversation-api)

[Back to top](https://dev.sprinklr.com/close-conversation-api)
