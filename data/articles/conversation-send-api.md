---
title: "Conversation Send API"
slug: conversation-send-api
url: https://dev.sprinklr.com/conversation-send-api
---

# Conversation Send API

# Conversation Send API




This API allows sending messages on the live chat application.

This documentation covers the following Use Cases:

1. Send Text Message

2. Send Image Message

3. Send Video Message

4. Send Document Message

5. Send Audio Message

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/send

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters



























****``

****

[Create Custom Field API](https://dev.sprinklr.com/create-custom-field)

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| conversationId |  | Required | The unique identifier for the conversation where you want to send the message | String |
| clientMessageId |  | Optional | Refers to the client generated message Id for tracking the messages that are being sent | String |
| sender |  | Optional | Refers to the unique identifier for the sender who is sending the messageDev Note: If the sender's value is set to P_-200, it helps register messages sent by the brand (ex - brand's side bot). However, the first message sent after creating the conversation has to be a fan message | String |
| messagePayload |  | Required | Refers to the object containing the message details | Object |
|  | text | Required for sending text messagesOptional when sending attachments such as image, document, video, and audio | Refers to the text of the message | String |
|  | textEntities | Optional |  |  |
|  | attachment | Required when sending image, audio, video, document attachmentNot required when sending simple text message | Refers to the object containing the attachment detailsRefer to the table below for attachment object parameters' details | Object |
|  | messageType | Required | Refers to the type of message you are sending in the conversationSupported Values: MESSAGE | String |
| additionalContext |  | Optional | Object containing key-value pairs of custom fields and their corresponding values. These custom fields provide additional contextual information related to the message. You can obtain the custom field name from the response of the  or copy it directly from the Sprinklr user interface. Steps to fetch the custom field name from Sprinklr UI are outlined below. | Object |

**Steps to Extract Custom Field Name from UI: **

- In the Sprinklr UI, click the **New Page** (**+**) icon.
- Search for **Custom Fields**.
- On the Custom Fields page, locate the custom field you want to use.
- Click the three dots next to the relevant custom field.
- Select the **Copy Field Name** option from the dropdown menu.
- Use the copied field name in the API request path parameters.

### Attachment Object Description Table

****

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of the attachmentSupported Types:IMAGE, VIDEO, DOCUMENT, AUDIO | String |
| title | Optional | Refers to the title of the attachment | String |
| mimeType | Optional | Refers to the combination of attachment and extension typeExample: image/png for IMAGE attachment, audio/wav for AUIDIO attachment, video/mov for VIDEO attachments, etc. | String |
| fileToken | Required for when sending attachment in the payload | Refers to the unique identifier for the uploaded file you receive in the upload file API response | String |
| width | Optional | Refers to the width of the image/video | Integer |
| height | Optional | Refers to the height of the image/video | Integer |
| previewFileToken | OptionalRequired when sending video attachments | Refers to the unique identifier for the preview url that you receive in the upload file API response | String |

### 1. Send Text Message

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1//conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "681b9771ad0b6e115a04714e",
    "messagePayload": {
        "text": "First customer message",
        "textEntities": [],
        "messageType": "MESSAGE"
    },
	"additionalContext": {
                "_c_6828d9803fc6de54447b2ac1": [
                    "asd"
                ]
            },
    "sender": "A_681b4b0c1e3538651d1bf2a2",
    "clientMessageId": "0"
}'





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





### 2. Send Image Message

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "6516b26bb2a421591acecd61",
    "clientMessageId": "0",
    "sender": "A_65113c865395ae2da5646b4b",
    "messagePayload": {
        "text": "",
        "textEntities": [],
        "attachment": {
            "type": "IMAGE",
            "height": 4000,
            "width": 6000,
            "title": "simpleImage.jpeg",
            "fileToken": "6516b27e2ce93949915cd6e7"
        },
        "messageType": "MESSAGE"
    }
}'





### Example - Response



{
    "id": "6540f8ad1a53377a0964ec28",
    "clientMessageId": "0",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "IMAGE",
            "fileToken": "6516b27e2ce93949915cd6e7",
            "width": 6000,
            "height": 4000,
            "title": "simpleImage.jpeg"
        }
    },
    "conversationId": "6516b26bb2a421591acecd61",
    "sender": "A_65113c865395ae2da5646b4b",
    "creationTime": 1698756781462,
    "updatedTime": 1698756781462,
    "deleted": false
}





### 3. Send Video Message

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1//conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "6516b26bb2a421591acecd61",
    "clientMessageId": "079090de-2df9-4c3f-b12c-2c4689cab90e",
    "sender": "A_65015cf949af065446feb777",
    "messagePayload": {
        "text": "",
        "textEntities": [],
        "attachment": {
            "type": "VIDEO",
            "height": 364,
            "width": 976,
            "title": "testVideo.mov",
            "fileToken": "6516eb1f2ce93949915e083c",
            "previewFileToken": "6516eb452ce93949915e091c",
            "mimeType": "video/mov"
        },
        "messageType": "MESSAGE"
    }
}'





### Example - Response



{
    "id": "6540f68dd17a386df3c40852",
    "clientMessageId": "079090de-2df9-4c3f-b12c-2c4689cab90e",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "VIDEO",
            "fileToken": "6516eb1f2ce93949915e083c",
            "title": "testVideo.mov",
            "mimeType": "video/mov",
            "previewFileToken": "6516eb452ce93949915e091c",
            "width": 976,
            "height": 364,
            "privateMedia": false
        }
    },
    "conversationId": "6516b26bb2a421591acecd61",
    "sender": "A_65113c865395ae2da5646b4b",
    "creationTime": 1698756237434,
    "updatedTime": 1698756237434,
    "deleted": false
}





### 4. Send Document Message

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "6516b26bb2a421591acecd61",
    "clientMessageId": "762f96d6-d01e-4d86-a88f-62e949b73807",
    "sender": "A_65015cf949af065446feb777",
    "messagePayload": {
        "text": "",
        "textEntities": [],
        "attachment": {
            "type": "DOCUMENT",
            "title": "Test Document",
            "mimeType": "document/pdf",
            "fileToken": "6516e73d2ce93949915df16d"
        },
        "messageType": "MESSAGE"
    }
}'





### Example - Response



{
    "id": "6540f96ed17a386df3c41fd1",
    "clientMessageId": "762f96d6-d01e-4d86-a88f-62e949b73807",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "DOCUMENT",
            "fileToken": "6516e73d2ce93949915df16d",
            "title": "Test Document",
            "mimeType": "document/pdf"
        }
    },
    "conversationId": "6516b26bb2a421591acecd61",
    "sender": "A_65113c865395ae2da5646b4b",
    "creationTime": 1698756974695,
    "updatedTime": 1698756974695,
    "deleted": false
}





### 5. Send Audio Message

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "6516b26bb2a421591acecd61",
    "clientMessageId": "762f96d6-d01e-4d86-a88f-62e949b73807",
    "sender": "A_65015cf949af065446feb777",
    "messagePayload": {
        "text": "",
        "textEntities": [],
        "attachment": {
            "type": "AUDIO",
            "title": "Test Audio File",
            "mimeType": "audio/wav",
            "fileToken": "6516e73d2ce93949915df16d"
        },
        "messageType": "MESSAGE"
    }
}'





### Example - Response



{
    "id": "6540f6131a53377a0964d602",
    "clientMessageId": "762f96d6-d01e-4d86-a88f-62e949b73807",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "AUDIO",
            "fileToken": "6516e73d2ce93949915df16d",
            "title": "Test Audio File",
            "mimeType": "audio/wav"
        }
    },
    "conversationId": "6516b26bb2a421591acecd61",
    "sender": "A_65113c865395ae2da5646b4b",
    "creationTime": 1698756115828,
    "updatedTime": 1698756115828,
    "deleted": false
}





[](https://dev.sprinklr.com/conversation-send-api)

[Back to top](https://dev.sprinklr.com/conversation-send-api)
