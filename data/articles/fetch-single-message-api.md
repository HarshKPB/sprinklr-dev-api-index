---
title: "Fetch Single Message API"
slug: fetch-single-message-api
url: https://dev.sprinklr.com/fetch-single-message-api
---

# Fetch Single Message API

#
		 Fetch Single Message API




Using this API, you can fetch the a single message within a live chat conversation using the unique identifier for the conversation and message.

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/fetchMessage


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
| conversationId | Required | Refers to the unique identifier for the conversation | String |
| messageId | Required | Refers to the unique identifier for the message | String |

## Example - Request




  Copy Code


curl -X GET \
 'https://{env{-live-chat.sprinklr.com/api/livechat/v1/conversation/fetchMessage?conversationId=6513d09e80feaa5b29bb82e4&messageId=6513d21819a98b52f41801df'\
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \



### Example - Response



{
    "results": [
        {
            "id": "682c50dd4e1aab2ba452a4d5",
            "clientMessageId": "0",
            "messagePayload": {
                "messageType": "MESSAGE",
                "disableManualResponse": false,
                "text": "Hello Testing",
                "previewUrls": null,
                "richText": false,
                "language": null,
                "textEntities": [],
                "attachment": null,
                "quickReplies": null
            },
            "conversationId": "681b9771ad0b6e115a04714e",
            "additionalContext": {
                "_c_6828d9803fc6de54447b2ac1": [
                    "asd"
                ]
            },
            "sender": "A_681b4b0c1e3538651d1bf2a2",
            "creationTime": 1747734749514,
            "updatedTime": 1747734749514,
            "deleted": false,
            "inReplyToChatMessageId": null
        }
    ],
    "hasMore": false,
    "totalCount": 0,
    "beforeCursor": "B_1746638705405_681b9771ad0b6e115a04714f",
    "afterCursor": "A_1747734749514_682c50dd4e1aab2ba452a4d5",
    "before": null,
    "after": null,
    "perfStats": null
}



[](https://dev.sprinklr.com/fetch-single-message-api)

[Back to top](https://dev.sprinklr.com/fetch-single-message-api)
