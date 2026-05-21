---
title: "Source Agnostic Message Webhook"
slug: source-agnostic-message-webhook
url: https://dev.sprinklr.com/source-agnostic-message-webhook
---

# Source Agnostic Message Webhook

# Source Agnostic Message Webhook

**Source Agnostic Webhook Subscriptions:**
Source Agnostic Message Created

Whenever an agent replies to a case associated with a source agnostic account, source agnostic message create webhook gets triggered

### Source Agnostic Message Created Webhook




  Copy Code



{
  "id": "637f8f86a4a2a51ab8694f72",
  "type": "source.agnostic.message.created",
  "payload": {
    "messageId": "637f8f85a4a2a51ab8694f6d",
    "senderProfile": {
      "id": "637f7f3539fd5e34dea0ed04",
      "screenName": "Testing",
      "name": "Test"
    },
    "receiverProfile": {
      "id": "brand",
      "name": "brand"
    },
    "content": {
      "title": "",
      "text": "How can I assist you today"
    },
    "timeStamp": "2023-01-23 15:36:37",
    "conversationId": "test_123",
    "brandMessage": true
  },
  "eventTime": 1669304197977,
  "subscriptionDetails": {
    "subscriptionId": "637f8d3c39fd5e34dea24386"
  }
}





### Response Parameters




























| Parameter | Sub-Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- | --- |
| id |  |  | Refers to the unique identifier for the webhook triggered | String |
| type |  |  | Refers to the webhook type. "source.agnostic.message.created" in this case | String |
| payload |  |  | Object containing the case details details | Object |
|  | messageId |  | Refers to the unique message id for the reply sent | String |
|  | senderProfile |  | Refers to the object containing the sender (agent) details | Object |
|  |  | id | Refers to the unique identifier for sender's profile | String |
|  |  | screenName | Refers to screen name of the sender | String |
|  |  | name | Refers to the name of the sender |  |
|  | receiverProfile |  | Refers to the object containing the receiver details | Object |
|  |  | id | Refers to the unique identifier for receiver's profile | String |
|  |  | name | Refers to the name of the receiver | String |
|  | content |  | Object containing the message details | Object |
|  |  | title | Refers to the title of the message sent (if any) | String |
|  |  | text | Refers to the text of the message | String |
|  | timestamp |  | Date and time at which the message was sent | String |
|  | conversationId |  | The unique identifier for the conversation which was configured when the message was imported in Sprinklr | String |
|  | brandMessage |  | If true, the message has been sent by the brand | Boolean |
| eventTime |  |  | Refers to the time at which the webhook was triggered | Epoch |
| subscriptionDetails |  |  | Object defining the webhook subscription details | Object |
|  | subscriptionId |  | Refers to the unique identifier for the webhook subscription | String |

[](https://dev.sprinklr.com/source-agnostic-message-webhook)

[Back to top](https://dev.sprinklr.com/source-agnostic-message-webhook)
