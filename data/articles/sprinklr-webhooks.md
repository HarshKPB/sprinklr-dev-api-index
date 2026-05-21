---
title: "Sprinklr Webhooks"
slug: sprinklr-webhooks
url: https://dev.sprinklr.com/sprinklr-webhooks
---

# Sprinklr Webhooks

# Webhooks


A webhook (also called a web callback or HTTP push API) enables third-party services to send real-time updates to your app. Updates are triggered by some event that occurs and the data is delivered to you immediately as it happens. When you receive the request, you handle it with some custom logic, like storing the data in a database or sending an email. Webhooks are also referred to as “Reverse APIs,” unlike typical APIs where you would need to poll for data very frequently in order to get it real-time. This makes webhooks much more efficient for both provider and consumer.

Sprinklr offers a variety of robust, convenient and simple Webhook APIs to perform  various functions related to webhooks within Sprinklr. Among the available features include APIs using JSON format, authentication via OAuth 2.0 invoking the existing user-level governance and security model built into Sprinklr. We have APIs to Create Subscription, push or pull subscription data, handle activation and deactivation of webhooks, and work triggered events.

In Sprinklr, you can apply webhooks on various entities, as of now the following are available:

- **Case:** Create, Update, Delete, Association Change

-
	**Message:**


  - **Inbound:** Updated, Received, Deleted

  - **Outbound:** Published, Publish Failed


- **Draft:** Created, Scheduled, Updated

- **Audience Activity**

- **Profile:** Created, Updated, Deleted, Merged

- **Campaign:** Create, Update, Delete

- **Comment:** Create, Update

- **SAM:** Asset Updated, Asset Created, Asset Deleted

- **Task:** Create, Update, Delete

For example, you can create a webhook subscription for Case Create. Whenever a new case gets created, the webhook gets triggered and you will get the event notification immediately. You can even use the different sets of available Authorization to protect your data.

**Dev Notes: **

- We recommend using an **asynchronous** webhook endpoint that sends `200 OK` within 10 seconds (default setup for [webhook retries logic](https://dev.sprinklr.com/webhook-retries-logic)). This helps avoid unwanted congestion at either the sender's or receiver's end

### Webhook Use Cases


- **Webhook for Case Events**: Notifies you when a case is created, updated, deleted or a new message gets associated with a case in Sprinklr for your partner.


**Note: **Case event triggered payloads also have sentiment key and values.

	For Poistive Sentiment value = 1

For Negative Sentiment value = -1

For Nuetral Sentiment value = 0

- **Webhook for Message Events**: Notifies you on any event occurred in Messages (like message created/published/received/deleted).

- **Webhook for Draft Events**: Notifies you with event-triggered updates to the registered url in case of a Draft post created, scheduled or updated.

- **Webhook for Comment Events**: Notifies you to stay abreast of changes in Comment Create, and Update.

- **Webhook for Profile Events**: Notifies you on real-time updates on Profile being Created, Updated, Deleted or Merged.

- **Webhook for Campaign Events**: Notifies you when a Campaign is Created, Updated or Deleted by the user.

## Schema of Subscription Response:




  Copy Code


"data": {
    "id": "5dfa53ce7edc203f0f725fe3",
    "type": "case.create",
    "payload": {
        "id": "5dfa53ce7edc203f0f725fde",
        "caseNumber": 7003525,
        "subject": "Abhinav Sinha",
        "description": "lol",
        "version": 0,
        "status": "New",
        "priority": "Medium",
        "caseType": "Complaint",
        "workflow": {
            "assignment": {
                "assigneeId": "600000788",
                "assigneeType": "USER",
                "assignedById": 600000788,
                "assignmentTime": 1576686542050
            },
            "customProperties": {
                "spr_uc_type": [
                    "Complaint"
                ],
                "5d42c773c7a0e3543eea8cdc": [
                    "1",
                    "2",
                    "3"
                ],
                "5d24a455f9e3b7349ecd2524": [
                    "2"
                ]
            },
            "queues": []
        },
        "contact": {
            "id": "FACEBOOK_1858570567593719",
            "name": "Abhinav Sinha"
        },
        "dueDate": 1577550480000,
        "createdTime": 1576686542050,
        "modifiedTime": 1576686542062,
        "firstMessageId": "ACCOUNT_600001381_1576677109000_FACEBOOK_38_m_UiRgh4Pob0uTrPUR4yOpcvRJXh9gUxIVolM8Iy2KLYAugSM8vBVW4jryjiJg4f1nGLlR8tVN4WE4MD9uDscu7g",
        "sentiment": -1
    },
    "eventTime": 1576686542099,
    "subscriptionDetails": {
        "subscriptionId": "5dd7d1a473f52c00019820a7"
    }
}








  Copy Code


{
   "id":"1326579629556925",
   "type":"case.update",
   "payload":{
   }
    "eventTime":1564558431472
}





	[](https://dev.sprinklr.com/sprinklr-webhooks)




[Back to top](https://dev.sprinklr.com/sprinklr-webhooks)
