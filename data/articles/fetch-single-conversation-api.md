---
title: "Fetch Single Conversation API"
slug: fetch-single-conversation-api
url: https://dev.sprinklr.com/fetch-single-conversation-api
---

# Fetch Single Conversation API

# Fetch Single Conversation API



Using this API, you can fetch a single conversation for the given conversation Id. Kindly note that the API returns the metadata about the conversation and not the messages present in that conversation.

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/fetch/{Conversation Id}


### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Path Parameter
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| conversationId | Required |  | String |

## Example - Request




  Copy Code


curl -X GET \
 'https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/fetch/653a2bd029526076e78e8df9'\
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \



### Example - Response



{
    "id": "653a34fa4b4051546cb90516",
    "appId": "app_1000163501",
    "conversationType": "SUPPORT",
    "participants": [
        "A_653a276b4b4051546cb8d21b"
    ],
    "creationTime": 1698313466594,
    "lastMessageId": "653a352f4b4051546cb90584",
    "caseId": "653a34fa4b4051546cb90516",
    "lastInteractionTime": 1698313519283,
    "closed": false,
    "startedByContext": {
        "CHANNELπSPRINKLR_LIVE_CHATπconversationClosed": [
            "No"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπipAddress": [
            "54.86.50.139"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπbrowser": [
            "Unknown"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπdevice": [
            "Unknown"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπinitiator": [
            "User"
        ]
    },
    "lastMessage": {
        "id": "653a352f4b4051546cb90584",
        "clientMessageId": "26885d0b-8bb4-491a-bf30-36b6ed77b400",
        "messagePayload": {
            "messageType": "MESSAGE",
            "disableManualResponse": false,
            "text": "First customer message",
            "richText": false,
            "textEntities": []
        },
        "conversationId": "653a34fa4b4051546cb90516",
        "sender": "A_653a276b4b4051546cb8d21b",
        "creationTime": 1698313519283,
        "updatedTime": 1698313519283,
        "deleted": false
    },
    "readStatusList": [
        {
            "readUptoTime": 0,
            "unreadCount": 6,
            "userId": "A_653a276b4b4051546cb8d21b"
        }
    ]
}



	[](https://dev.sprinklr.com/fetch-single-conversation-api)

[Back to top](https://dev.sprinklr.com/fetch-single-conversation-api)
