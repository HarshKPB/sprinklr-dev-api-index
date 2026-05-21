---
title: "Apr - Jun, 2023"
slug: apr-jun-2023
url: https://dev.sprinklr.com/apr-jun-2023
---

# Apr - Jun, 2023

#
Apr - Jun, 2023

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****Create Bulk Cases via Profile  -  June 5th, 2023

Using this API, you can create a user or update details for an existing user.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/scim/upsert

## ****API Support for Fetching Voice Recordings and Transcriptions -  May 25th, 2023

You can now fetch voice recordings and transcription for Sprinklr Voice channel using the read message by Id or read bulk messages API.

## ****Template Webhooks -  May 25th, 2023

Now you can subscribe to template webhooks which get triggered whenever an omnichannel template is created, updated, or deleted.

**Webhook Response Details**

Refer to [Template Asset Webhook Response](https://dev.sprinklr.com/template-asset-webhooks) documentation

## ****Publish "Question with Answers" Facebook Template -  May 17th, 2023

Using this API, you can reply to messages using Facebook’s “Question with Answers” template. This template allows sending a template that helps send a question and corresponding answers in the form of buttons. The user can select from the appropriate answer from the list of given buttons.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/message

## ****Custom Query Using Widget Id -  May 17th, 2023

Using this API, you can export the reporting widget data using widget Id. The advantage of this approach is that you don't need to update the request payload every time any metric or dimension is updated in the widget.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/reports/query/{widgetId}



## ****PRIVATE_MSG_LINK Support in Publishing Reply API -  May 15th, 2023

Publishing reply API now supports adding a private message link button along with the reply suggesting the user to send a private message instead.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/reply

## ****Account Custom Field Support in Lookup by Dimension API -  May 10th, 2023

When you query for ACCOUNT_ID in lookup by dimension API, now you'll also receive account associated custom properties in the response.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/lookup/byDimensions



## ****Fetch All Profile Information from Fetch Profile APIs -  May 10th, 2023

Now you can fetch all the profile information, that is, data and metadata associated with a social profile. The API will fetch all the profile details that are stored within Sprinklr.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/profile/{profileId}



## ****User Current State Webhook  -  May 9th, 2023

This webhook provides real time updates for the current user state within Sprinklr.

**Response Payload Details**

Refer to [User Current State Webhook](https://dev.sprinklr.com/user-current-state-webhook) documentation



## ****Voice Call Event Updates Webhook  -  May 9th, 2023

This webhook provides real-time updates for changes in call status associated with Sprinklr Voice cases.

**Response Payload Details**

Refer to [Voice Call Event Updates Webhook](https://dev.sprinklr.com/voice-call-event-updates-webhook) documentation



## ****Create Bulk Cases via Profile  -  May 5th, 2023

Using this API, you can create cases along with audience profiles in bulk. A maximum of 10 cases associated profiles can be created using this API.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/case/bulk/profile



## ****Source Agnostic (Send Message API)  -  April 5th, 2023

Source agnostic API now supports sending Image, Video, Multimedia, Simple Base64, Audio, and Video attachments. The API returns the case number in the response with which the message has been associated.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/source-agnostic/{accountId}/send


[](https://dev.sprinklr.com/apr-jun-2023)

[Back to top](https://dev.sprinklr.com/apr-jun-2023)
