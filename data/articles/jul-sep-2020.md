---
title: "Jul - Sep, 2020"
slug: jul-sep-2020
url: https://dev.sprinklr.com/jul-sep-2020
---

# Jul - Sep, 2020

# Jul - Sep, 2020

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## **Message Conversation Read** - September 28th, 2020

You can fetch the children messages that are linked with parent message Id within a conversation.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/conversations/new/children

## **Message Action API** - September 20th, 2020

You use this API to perform different actions on Messages like `HIDE, UNHIDE, LIKE, UNLIKE, FAVORITE, UNFAVORITE, DELETE `and many more specific to native channel type.


**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/message/action
**Channel Type: ** TWITTER

## **Message Workflow Properties Update API** - September 20th, 2020

You can use this API to update the message workflow properties.


**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/message/workflow/properties/update
**Custom Properties Type: **
 clientCustomProperties
 partnerCustomProperties
 userCustomProperties

## **Intuition API Endpoint** -  July 25th, 2020

Introduction of Intuition API endpoints. We’re exposing new set of API endpoints using which you can make prediction requests either on a single or batch of messages.

**Text Predict API Endpoints**

The Text Predict API is capable of analyzing the Sentiment and Emotion of a message and can also detect whether a message is a Spam or not. Using the text predict API, you can make a prediction request on a single message.
POST https://api2.sprinklr.com/{env}/api/v2/intuition/text/predict

The Text Batch Predict API is capable of analyzing the Sentiment and Emotion of messages. It can also detect whether a batch of messages is spam or not. Using the text batch predict API, you can make a prediction request on a list of messages.

POST https://api2.sprinklr.com/{env}/api/v2/intuition/text/batch-predict

**Product Insights Predict API Endpoints**

The Product Insights Predict API is capable of identifying common trends within unstructured data to apply structure and drive analysis based on modeling structure of respective business. Using this API, you can make a prediction request on a single message.
POST https://api2.sprinklr.com/{env}/api/v2/intuition/product-insights/predict

The Product Insights Batch Predict API is capable of identifying common trends within unstructured data to apply structure and drive analysis based on modeling structure of respective business. Using this API, you can make a prediction request on a list of messages.

POST https://api2.sprinklr.com/{env}/api/v2/intuition/product-insights/batch-predict

**Location Insights Predict API Endpoints**

The Location Insights Predict API is capable of identifying common trends within unstructured data to apply structure and drive analysis based on modeling structure of respective business. Using this API, you can make a prediction request on a single message, that is, one at a time.
POST https://api2.sprinklr.com/{env}/api/v2/intuition/location-insights/predict
The Location Insights Batch Predict API is capable of identifying common trends within unstructured data to apply structure and drive analysis based on modeling structure of respective business. Using this API, you can make a prediction request on a list of messages.
POST https://api2.sprinklr.com/{env}/api/v2/intuition/location-insights/batch-predict

**Intent Predict API Endpoints**

The Intent Predict API is capable of identifying issue type in a message and this helps in routing the message or case according to the identified intent. Using this API, you can make a prediction request on a single message, that is, one at a time.
POST https://api2.sprinklr.com/{env}/api/v2/intuition/intent/predict

The Intent Batch Predict API is capable of identifying issue types in a list of messages and this helps in routing the messages or cases according to the identified intent. Using this API, you can make a prediction request on a list of messages.
POST https://api2.sprinklr.com/{env}/api/v2/intuition/intent/batch-predict

## **Task API Endpoint** -  July 25th, 2020

Introduction of Task API endpoints. We’re exposing new set of API endpoints by which you can Read, Create, Update and Delete task within Sprinklr.


**API Endpoints**

GET https://api2.sprinklr.com/{env}/api/v2/task/{taskId}

POST https://api2.sprinklr.com/{env}/api/v2/task
PUT https://api2.sprinklr.com/{env}/api/v2/task/{taskId}
DELETE https://api2.sprinklr.com/{env}/api/v2/task/{taskId}

## **Webhook Replay API Endpoint** - July 25th, 2020

Introduction of Webhook Replay API endpoints. We’re exposing new API endpoints by which you can get the stream of webhooks as response for a given time duration. To replay the webhook stream for a given time duration, you need to make two API call. First you need to generate the replay id using webhook subscription Id via /Init API call. Now you can use this replayId in the /stream API call with start and end time as query parameters to replay the stream of webhook in the API response.

**API Endpoints**

POST  https://api2.sprinklr.com/{env}/api/v2/webhook-replay/init
POST https://api2.sprinklr.com/{env}/api/v2/webhook-replay/stream

## **Search API Endpoint Enhancement** - July 25th, 2020

To improve the efficiency and performance of Sprinlkr Search APIs in terms of Task, Campaign and Sub-Campaign within Sprinklr. We have added TASK, CAMPAIGN and SUB_CAMPAIGN as a new entity type, you can use search api to read through these entities within Sprinklr using available filtering and sorting.

**Search API Enhancement**

POST https://api2.sprinklr.com/{env}/api/v2/search/{entityType}

## **Asset Async Import API Endpoint** - July 25th, 2020

Introduction of Asset Import Async API endpoints. We’re exposing new API endpoints by which you can get the asset imported via URL and in response you will get the task id which you can use in status check api call to get the uploded content Id. Once you have the uploadedContentId, you can use it in Sam Asset Create call to create an asset in Sprinklr Asset Manager.

**API Endpoints**

POST https://api2.sprinklr.com/{env}/api/v1/sam/importUrl/async
GET https://api2.sprinklr.com/{env}/api/v1/sam/task/status/{taskId}

## **Email Generate API Endpoint** - July 25th, 2020

Introduction of new enhanced Email API that can be used to send and an email with and without attachments.

**Supported Attachment Types: **
 pdf, excel, mp3, mp4, doc, txt, html, image, csv & zip

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/email/generate?aId={Account Id}

## **Webhook Enhancement** - July 25th, 2020.

Now Geo-Location information is available as attachments in message.created webhook whenever a user shares location.

**Geo Location Attachment: **

```

"content": {
            "attachment": {
                "latitude": 12.971117,
                "longitude": 77.597645,
                "address": "Bangalore",
                "name": "Majestic, Bangalore",
                "url": "https://www.facebook.com/325730668182255",
                "type": "GEO_LOCATION"
            }
        }

```

[](https://dev.sprinklr.com/jul-sep-2020)

[Back to top](https://dev.sprinklr.com/jul-sep-2020)
