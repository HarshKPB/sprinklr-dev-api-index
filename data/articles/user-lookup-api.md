---
title: "user-lookup-api"
slug: user-lookup-api
url: https://dev.sprinklr.com/user-lookup-api
---

# user-lookup-api

# User Lookup API

This API allows searching profile information about end users who sent the messages on the live chat application

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/userLookup

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters (Array)












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sender | Required | Refers to the unique identifier for the sender who sent the message on the live chat application | String |
| conversationId | Required | Refers to the unique identifier for the conversation that the sender initiated | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1//conversation/userLookup' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '[
    {
        "sender": "P_1000199492",
        "conversationId": "6513d09e80feaa5b29bb82e4"
    },
    {
        "sender": "A_65113c865395ae2da5646b4b",
        "conversationId": "6513d09e80feaa5b29bb82e4"
    }
]'



### Example - Response



[
    {
        "userId": "P_1000199492",
        "userType": "PARTNER",
        "firstName": "[sj] test appln",
        "fullName": "[sj] test appln"
    },
    {
        "userId": "A_65113c865395ae2da5646b4b",
        "userType": "ANONYMOUS",
        "firstName": "First",
        "lastName": "Last",
        "fullName": "John Doe",
        "phoneNo": "1236754321",
        "email": "johndoe@partner.sprinklr.com"
    }
]



	[](https://dev.sprinklr.com/user-lookup-api)

[Back to top](https://dev.sprinklr.com/user-lookup-api)
