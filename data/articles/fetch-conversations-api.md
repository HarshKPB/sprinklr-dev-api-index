---
title: "Fetch Conversations API"
slug: fetch-conversations-api
url: https://dev.sprinklr.com/fetch-conversations-api
---

# Fetch Conversations API

#
	Fetch Conversations API




Using this API, you can fetch the conversations that have been initiated so far within the live chat application. The API returns both open and closed conversations for the user associated with the x-chat-token.

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/fetch


### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Query Parameter





















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| fetchNumberOfOpenConversations | Optional | If true, only the open conversations will be returned in the API response | Boolean |
| size | Optional | Refers to the number of conversations you want to fetch per API callIt is recommended to keep size at 20 for fetching the oldest to newest conversations | Integer |

## Example - Request




  Copy Code


curl -X GET \
 'https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/fetch?fetchNumberOfOpenConversations=true&size=10' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \



**Dev Notes: **For fetching the previous or next set of results, kindly use the beforeCursor and afterCursor respectively in the query parameters. If hasMore is true, you can use the beforeCursor and afterCursor from the response in the API request for fetching the previous/next set of results.

### Example - Response



{
    "results": [
        {
            "id": "6526436cb564200a98221ce2",
            "appId": "app_1000163501",
            "conversationType": "SUPPORT",
            "participants": [
                "A_65113c865395ae2da5646b4b"
            ],
            "creationTime": 1697006444990,
            "lastMessageId": "652644a1b564200a98221fd0",
            "caseId": "6526436cb564200a98221ce2",
            "lastInteractionTime": 1697006753031,
            "closed": false,
            "startedByContext": {
                "_c_6512d347d8b5f43fd91f7fb4": [
                    "Example case custom field value"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπinitiator": [
                    "User"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπbrowser": [
                    "Chrome 11"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπdevice": [
                    "Computer"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπpageTitle": [
                    "Sprinklr Live Chat"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπpageUrl": [
                    "https://live-chat-static.sprinklr.com/test-html/index.html?appId=65015cddb2678b575c01b175_app_1000163501&env=prod0"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπipAddress": [
                    "54.86.50.139"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπlocale": [
                    "en"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπlanguage": [
                    "en"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπtimeZone": [
                    "Asia/Calcutta"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπconversationClosed": [
                    "No"
                ],
                "CHANNELπSPRINKLR_LIVE_CHATπuserAgent": [
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
                ]
            },
            "lastMessage": {
                "id": "652644a1b564200a98221fd0",
                "clientMessageId": "2002d6d6-2451-4ae0-9c38-bfc04d18967c",
                "messagePayload": {
                    "messageType": "MESSAGE",
                    "disableManualResponse": false,
                    "text": "",
                    "richText": false,
                    "textEntities": [],
                    "attachment": {
                        "type": "IMAGE",
                        "url": "https://s3.amazonaws.com/prod0-spr-livechat/chat/9178/app_1000163501/6526446db564200a98221ef6/simpleImage.jpeg",
                        "fileToken": "65264474b564200a98221f0e",
                        "width": 6000,
                        "height": 4000,
                        "title": "simpleImage.jpeg"
                    }
                },
                "conversationId": "6526436cb564200a98221ce2",
                "sender": "A_65113c865395ae2da5646b4b",
                "creationTime": 1697006753031,
                "updatedTime": 1697006753031,
                "deleted": false
            },
            "readStatusList": [
                {
                    "readUptoTime": 1697006753031,
                    "messageId": "652644a1b564200a98221fd0",
                    "userId": "65015cddb2678b575c01b175"
                },
                {
                    "readUptoTime": 1697006753031,
                    "messageId": "652644a1b564200a98221fd0",
                    "userId": "P_1000127760"
                },
                {
                    "readUptoTime": 1697006753031,
                    "messageId": "652644a1b564200a98221fd0",
                    "userId": "P_1000279679"
                },
                {
                    "readUptoTime": 0,
                    "unreadCount": 6,
                    "userId": "A_65113c865395ae2da5646b4b"
                }
            ]
        }
    ],
    "hasMore": true,
    "totalCount": 0,
    "beforeCursor": "B_6526436cb564200a98221ce2",
    "afterCursor": "A_6526436cb564200a98221ce2",
    "noOfOpenConversations": 5
}



**Dev Notes: **Every Conversation object will include a "closed" boolean field which when true implies that the conversation has been closed. You can filter for open conversation by looking for "closed": false in the API response.

[](https://dev.sprinklr.com/fetch-conversations-api)

[Back to top](https://dev.sprinklr.com/fetch-conversations-api)
