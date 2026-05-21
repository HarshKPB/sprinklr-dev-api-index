---
title: "Source Agnostic - Close Conversation"
slug: source-agnostic-close-conversation
url: https://dev.sprinklr.com/source-agnostic-close-conversation
---

# Source Agnostic - Close Conversation

# POST Source Agnostic - Close Conversation

Source Agnostic close conversation API allows closing the conversation using the unique conversation Id that was earlier used to [import messages](https://dev.sprinklr.com/source-agnostic-send-message) on Sprinklr.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/source-agnostic/closeConversation?conversationId=`{conversationId}`

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

### Query Parameters

















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| conversationId | Required | The unique identifier for the conversation | String |

### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/closeConversation?conversationId=new_123’ \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'



**Dev Notes: **In case, you pass a new/unique conversationId that was not used earlier to send messages to Sprinklr using [this API](https://dev.sprinklr.com/source-agnostic-send-message), you will receive a 400 Bad Request.


### Example - Response





200 OK



**Dev Notes: **Response code 200 OK implies that the conversation has been successfully closed on Sprinklr’s end.

[](https://dev.sprinklr.com/source-agnostic-close-conversation) 

 

 
[Back to top](https://dev.sprinklr.com/source-agnostic-close-conversation)
