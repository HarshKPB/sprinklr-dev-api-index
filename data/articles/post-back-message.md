---
title: "Post Back Message"
slug: post-back-message
url: https://dev.sprinklr.com/post-back-message
---

# Post Back Message

#
		Post Back Message


This API helps sending post back response for different template assets posted to the live chat application. That is, the user responses to the forms, carousels, surveys, and feedbacks are sent using this API.

This documentation covers the following Use Cases:

1. Text Post Back

2. Survey Post Back

3. Feedback Post Back

4. Contact Details Form post Back

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

## 1. Text Post Back

If a message is published or card or a carousel is published and the user clicks on a button, then a text post back message will need to be sent.

### Request Parameters - TEXT_POST_BACK



















| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| conversationId |  | Required | The unique identifier for the conversation where you want to send the message | String |
| messagePayload |  | Required | Refers to the object containing the message details | Object |
|  | text | Required | Refers to the text of the message | String |
|  | textEntities | Optional | Refers to the meta data associated with the text | List [String] |
|  | attachment | Required | Refers to the object containing the attachment detailsRefer to the table below for attachment object parameters' details | Object |
|  | messageType | Required | Refers to the post back message type, i.e., POST_BACK_MESSAGE in this case | String |
| sender |  | Required | Refers to the unique identifier for the sender |  |
| clientMessageId |  | Optional | It is a client generated field which refers to the unique identifier for the message | String |
| inReplyToChatMessageId |  | Optional | Refers to the unique identifier for the message the reply was sent for | String |

### Attachment Object Description Table

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| templateType | Required | If true, the message is sent on a template | Boolean |
| type | Required | Refers to the type of attachment, i.e., TEXT_POST_BACK | String |
| buttonId | Optional | Refers to the unique identifier for the button that the user clicked on | String |
| messageId | Required | Refers to the unique identifier for the message | String |
| section | Required | Refers to the section on which the reply was sentSupported Values: TEMPLATE | String |
| text | Required | Refers to the text of the message | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "6572f54090ad002220def477",
    "messagePayload": {
        "text": "Building button",
        "textEntities": [],
        "attachment": {
            "templateType": true,
            "type": "TEXT_POST_BACK",
            "buttonId": "6d0c4376-7245-4834-a981-4d9ec84b86ff",
            "messageId": "6572f54090ad002220def47a",
            "section": "TEMPLATE",
            "text": "Building button"
        },
        "messageType": "POST_BACK_MESSAGE"
    },
    "sender": "A_6572db6853f3510cc9810353",
    "clientMessageId": "e119e5ee-fc6d-458e-9007-fdd8cc652b1e",
    "inReplyToChatMessageId": "6572f54090ad002220def47a"
}'





### Example - Response



{
    "id": "6572f66a8ba0bd7e98bf7347",
    "clientMessageId": "e119e5ee-fc6d-458e-9007-fdd8cc652b1e",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "Building button",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "TEXT_POST_BACK",
            "templateType": true,
            "expired": false,
            "messageId": "6572f54090ad002220def47a",
            "section": "TEMPLATE",
            "buttonId": "6d0c4376-7245-4834-a981-4d9ec84b86ff",
            "text": "Building button"
        }
    },
    "conversationId": "6572f54090ad002220def477",
    "sender": "A_6572db6853f3510cc9810353",
    "creationTime": 1702033002537,
    "updatedTime": 1702033002537,
    "deleted": false,
    "inReplyToChatMessageId": "6572f54090ad002220def47a"
}





## 2. Survey Post Back

If a survey is published, and user responds to it, survey post back message needs to be sent

### Request Parameters - SURVEY_POST_BACK



















| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| conversationId |  | Required | The unique identifier for the conversation where you want to send the message | String |
| messagePayload |  | Required | Refers to the object containing the message details | Object |
|  | text | Required | Refers to the text of the message | String |
|  | textEntities | Optional | Refers to the meta data associated with the text | List [String] |
|  | attachment | Required | Refers to the object containing the attachment detailsRefer to the table below for attachment object parameters' details | Object |
|  | messageType | Required | Refers to the post back message type, i.e., POST_BACK_MESSAGE in this case | String |
| sender |  | Required | Refers to the unique identifier for the sender |  |
| clientMessageId |  | Optional | It is a client generated field which refers to the unique identifier for the message | String |
| inReplyToChatMessageId |  | Optional | Refers to the unique identifier for the message the reply was sent for | String |

### Attachment Object Description Table

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| templateType | Required | If true, the message is sent on a template | Boolean |
| type | Required | Refers to the type of attachment, i.e., SURVEY_POST_BACK | String |
| buttonId | Optional | Refers to the unique identifier for the button that the user clicked on | String |
| messageId | Required | Refers to the unique identifier for the message | String |
| section | Required | Refers to the section on which the reply was sentSupported Values: TEMPLATE | String |
| text | Required | Refers to the text of the message | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "651cf22c5a1b0c1114ba1e57",
    "messagePayload": {
        "text": "",
        "textEntities": [],
        "attachment": {
            "templateType": true,
            "type": "SURVEY_POST_BACK",
            "buttonId": "046d0d6f-f923-4476-a8f6-b6aa163f3113",
            "messageId": "64e8427250c19016abdeb674",
            "section": "TEMPLATE"
        },
        "messageType": "POST_BACK_MESSAGE"
    },
    "sender": "A_65113c865395ae2da5646b4b",
    "clientMessageId": "b1caf8d6-45d7-4f18-9af2-60d5f76a6767"
}'





### Example - Response



{
    "id": "6572f66a8ba0bd7e98bf7348",
    "clientMessageId": "b1caf8d6-45d7-4f18-9af2-60d5f76a6767",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "Building button",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "SURVEY_POST_BACK",
            "templateType": true,
            "expired": false,
            "messageId": "64e8427250c19016abdeb674",
            "section": "TEMPLATE",
            "buttonId": "046d0d6f-f923-4476-a8f6-b6aa163f3113",
            "text": ""
        }
    },
    "conversationId": "651cf22c5a1b0c1114ba1e57",
    "sender": "A_65113c865395ae2da5646b4b",
    "creationTime": 1702033002537,
    "updatedTime": 1702033002537,
    "deleted": false
}





### 3. Feedback Post Back



















| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| conversationId |  | Required | The unique identifier for the conversation where you want to send the message | String |
| messagePayload |  | Required | Refers to the object containing the message details | Object |
|  | text | Required | Refers to the text of the message | String |
|  | textEntities | Optional | Refers to the meta data associated with the text | List [String] |
|  | attachment | Required | Refers to the object containing the attachment detailsRefer to the table below for attachment object parameters' details | Object |
|  | messageType | Required | Refers to the post back message type, i.e., POST_BACK_MESSAGE in this case | String |
| sender |  | Required | Refers to the unique identifier for the sender |  |
| clientMessageId |  | Optional | It is a client generated field which refers to the unique identifier for the message | String |
| inReplyToChatMessageId |  | Optional | Refers to the unique identifier for the message the reply was sent for | String |

### Attachment Object Description Table

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| templateType | Required | If true, the message is sent on a template | Boolean |
| type | Required | Refers to the type of attachment, i.e., "FEEDBACK_POST_BACK" | String |
| buttonId | Optional | Refers to the unique identifier for the button that the user clicked on | String |
| messageId | Required | Refers to the unique identifier for the message | String |
| section | Required | Refers to the section on which the reply was sentSupported Values: TEMPLATE | String |
| feedbackRating | Required | Refers to the feedback score given by the customer | String |
| feedbackType | Required | Refers to the type of feedback | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env{-live-chat.sprinklr.com/api/livechat/v1/conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "651cf22c5a1b0c1114ba1e57",
    "messagePayload": {
        "text": "",
        "textEntities": [],
        "attachment": {
            "templateType": true,
            "type": "FEEDBACK_POST_BACK",
            "buttonId": "8",
            "messageId": "651cf22c5a1b0c1114ba1e5c",
            "section": "TEMPLATE",
            "feedbackRating": "8",
            "feedbackType": "nps"
        },
        "messageType": "POST_BACK_MESSAGE"
    },
    "sender": "A_65113c865395ae2da5646b4b",
    "clientMessageId": "8e190be6-5399-4b50-9489-d8818e319918",
    "inReplyToChatMessageId": "651cf22c5a1b0c1114ba1e5c"
}'





### Example - Response



{
    "id": "6572f66a8ba0bd7e98bf7349",
    "clientMessageId": "8e190be6-5399-4b50-9489-d8818e319918",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "Building button",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "FEEDBACK_POST_BACK",
            "templateType": true,
            "expired": false,
            "messageId": "651cf22c5a1b0c1114ba1e5c",
            "section": "TEMPLATE",
            "buttonId": "8",
            "feedbackRating": "8",
            "feedbackType": "nps"
},
    "conversationId": "651cf22c5a1b0c1114ba1e57",
    "sender": "A_65113c865395ae2da5646b4b",
    "creationTime": 1702033002537,
    "updatedTime": 1702033002537,
    "deleted": false
}





### 4. Contact Details Post Back



















| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| conversationId |  | Required | The unique identifier for the conversation where you want to send the message | String |
| messagePayload |  | Required | Refers to the object containing the message details | Object |
|  | text | Required | Refers to the text of the message | String |
|  | textEntities | Optional | Refers to the meta data associated with the text | List [String] |
|  | attachment | Required | Refers to the object containing the attachment detailsRefer to the table below for attachment object parameters' details | Object |
|  | messageType | Required | Refers to the post back message type, i.e., POST_BACK_MESSAGE in this case | String |
| sender |  | Required | Refers to the unique identifier for the sender |  |
| clientMessageId |  | Optional | It is a client generated field which refers to the unique identifier for the message | String |
| inReplyToChatMessageId |  | Optional | Refers to the unique identifier for the message the reply was sent for | String |

### Attachment Object Description Table

****

****

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| templateType |  | Required | If true, the message is sent on a template | Boolean |
| type |  | Required | Refers to the type of attachment, i.e., "CONTACT_DETAILS_POST_BACK" | String |
| buttonId |  | Optional | Refers to the unique identifier for the button that the user clicked on | String |
| messageId |  | Required | Refers to the unique identifier for the message | String |
| section |  | Required | Refers to the section on which the reply was sentSupported Values: TEMPLATE | String |
| filledForm |  | Required | Refers to the object containing the filled form details | Object |
|  | formId | Required | Refers to the unique identifier for the form filled | String |
|  | plainFieldValues | Required | Object containing key and value pairs for field name and value respectivelyExample: "Name": "John Doe", "firstName": "John","lastName": "Doe" | Object |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/send' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversationId": "651cf22c5a1b0c1114ba1e57",
    "messagePayload": {
        "text": "Done",
        "textEntities": [],
        "attachment": {
            "templateType": true,
            "type": "CONTACT_DETAILS_POST_BACK",
            "buttonId": "fd30b28e-618d-4f3c-9177-8819b3f3a837",
            "messageId": "651cf22c5a1b0c1114ba1e58",
            "section": "TEMPLATE",
            "filledForm": {
                "formId": "a3ef5ea1-62a9-4a69-b007-7042714f2e24",
                "plainFieldValues": {
                    "NAME": "John Doe",
                    "FIRST_NAME": "First",
                    "LAST_NAME": "Last",
                    "EMAIL": "email@gmail.com",
                    "PHONE_NO": "9740152111",
                    "d6c3259c-9e99-4e33-aa3e-2eefeabd518f": true,
                    "1f8ff9f8-5d95-4a4c-b555-776b8471f4f7": [
                        "question 2",
                        "question 1"
                    ],
                    "dcec37ec-17af-442a-8246-969124d26044": "option 2",
                    "41f00be6-85b8-47e3-9d07-5dae41360a4b": "abcde",
                    "636a7e7f-28b6-4f36-8f7c-eff6a0856d68": 7,
                    "a4df2c84-8c86-43db-bfa1-ab1215b6f05d": 1697740200330,
                    "eb552d2f-ca6a-4bf3-a40e-8d0f82d5929c": [
                        "m1",
                        "m2"
                    ],
                    "3fbd2b27-1bee-4e78-ae94-81bea5de67cf": "po 2",
                    "fe0bb2f4-7038-41e5-a509-991b2733dee7": [
                        "mpo 2",
                        "mpo 3"
                    ],
                    "cb76aee8-2e6d-4d8b-9771-62655105a2b2": "1234",
                    "a89336d9-c1cc-4329-9af0-ade3a4ec11ce": "Some text",
                    "5789d5b4-e86a-4c34-a8f6-507ff071cd0b": "abcde"
                }
            }
        },
        "messageType": "POST_BACK_MESSAGE"
    },
    "sender": "A_65113c865395ae2da5646b4b",
    "clientMessageId": "e3633c91-c48b-45cf-b47e-dcf3b64ed8b3"
}'





### Example - Response



{
    "id": "6572f66a8ba0bd7e98bf7350",
    "clientMessageId": "e3633c91-c48b-45cf-b47e-dcf3b64ed8b3",
    "messagePayload": {
        "messageType": "MESSAGE",
        "disableManualResponse": false,
        "text": "Building button",
        "richText": false,
        "textEntities": [],
        "attachment": {
            "type": "CONTACT_DETAILS_POST_BACK",
            "templateType": true,
            "expired": false,
            "messageId":  "651cf22c5a1b0c1114ba1e58",
            "section": "TEMPLATE",
            "buttonId": ""fd30b28e-618d-4f3c-9177-8819b3f3a837",
            "filledForm": {
                "formId": "a3ef5ea1-62a9-4a69-b007-7042714f2e24",
                "plainFieldValues": {
                    "NAME": "John Doe",
                    "FIRST_NAME": "First",
                    "LAST_NAME": "Last",
                    "EMAIL": "email@gmail.com",
                    "PHONE_NO": "9740152111",
                    "d6c3259c-9e99-4e33-aa3e-2eefeabd518f": true,
                    "1f8ff9f8-5d95-4a4c-b555-776b8471f4f7": [
                        "question 2",
                        "question 1"
                    ],
                    "dcec37ec-17af-442a-8246-969124d26044": "option 2",
                    "41f00be6-85b8-47e3-9d07-5dae41360a4b": "abcde",
                    "636a7e7f-28b6-4f36-8f7c-eff6a0856d68": 7,
                    "a4df2c84-8c86-43db-bfa1-ab1215b6f05d": 1697740200330,
                    "eb552d2f-ca6a-4bf3-a40e-8d0f82d5929c": [
                        "m1",
                        "m2"
                    ],
                    "3fbd2b27-1bee-4e78-ae94-81bea5de67cf": "po 2",
                    "fe0bb2f4-7038-41e5-a509-991b2733dee7": [
                        "mpo 2",
                        "mpo 3"
                    ],
                    "cb76aee8-2e6d-4d8b-9771-62655105a2b2": "1234",
                    "a89336d9-c1cc-4329-9af0-ade3a4ec11ce": "Some text",
                    "5789d5b4-e86a-4c34-a8f6-507ff071cd0b": "abcde"
                }
            }
        },
    "conversationId": "651cf22c5a1b0c1114ba1e57",
    "sender": "A_65113c865395ae2da5646b4b",
    "creationTime": 1702033002537,
    "updatedTime": 1702033002537,
    "deleted": false
}





[](https://dev.sprinklr.com/post-back-message)

[Back to top](https://dev.sprinklr.com/post-back-message)
