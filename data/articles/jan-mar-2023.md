---
title: "Jan - Mar, 2023"
slug: jan-mar-2023
url: https://dev.sprinklr.com/jan-mar-2023
---

# Jan - Mar, 2023

# Jan - Mar, 2023

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****Fetch All Keyword Lists  -  March 29th, 2023

Using this API, you can fetch all keyword lists available within the workspace.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/keyword-list/fetchKeywordListsNameIdMapping



## ****Create/Read/Update Custom Fields in Listening Topic APIs  -  March 28th, 2023

You can now create, fetch, and update custom properties for a listening topic.

** Endpoint Details**

- Create Listening Topic

- Read Listening Topic

- Update Listening Topic



## ****Publish Apple Business Chat Template  -  Feb 27th, 2023

You can use this API to publish dynamic templates on Apple Business Chat.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/message



## ****Account Created, Account Updated Webhook  -  Jan 23rd, 2023

Using these webhooks, you can receive notification every time an account is created or updated within Sprinklr.

**Response Payload Details**

Refer to [Account Created](https://dev.sprinklr.com/account-webhooks#accountCreated), [Account Updated](https://dev.sprinklr.com/account-webhooks#accountUpdated) Response Payloads



## ****Create/Update Live Chat Event  -  Jan 23rd, 2023

Using this API, you can create or update a live chat event for sending or receiving messages.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/live-chat/create-or-update-live-stream-event



## ****Fetch Live Stream Chat Events  -  Jan 23rd, 2023

Using this API, you can fetch multiple live stream chat events for the given live chat stream Ids.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/live-chat/fetch-live-stream-events



## ****Fetch Live Stream Chat Event  -  Jan 23rd, 2023

Using this API, you can fetch a single chat event for the given live chat stream Id

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/live-chat/fetch-live-stream-event/{id}



## ****Start Live Stream Chat Event  -  Jan 23rd, 2023

Using this API, you can start an event instantly for the given live chat stream Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/live-chat/start-live-stream-event/{Id}



## ****End Live Stream Chat Event  -  Jan 23rd, 2023

Using this API, you can end an event instantly for the given live chat stream Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/live-chat/end-live-stream-event/{Id}



## ****Update Partial Custom Properties for Account -  Jan 19th, 2023

Using this API, you can partially update partner/client custom properties for the given account Id. The API will only update the custom properties that are passed in the request body.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/account/update/{accountId}/customProperties



## ****Deactivate Account -  Jan 17th, 2023

Using this API, you can deactivate an account for the given account Id.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/account/{accountId}/deactivate



## ****BETA! Update Channel Details -  Jan 16th, 2023

Using this API call, the 3rd party platform channel case Id can be stored within a Sprinklr case.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/case/channel-case-details


[](https://dev.sprinklr.com/jan-mar-2023)

[Back to top](https://dev.sprinklr.com/jan-mar-2023)
