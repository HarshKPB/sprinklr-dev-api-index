---
title: "Fetch Live Stream Chat Events"
slug: fetch-live-stream-chat-events
url: https://dev.sprinklr.com/fetch-live-stream-chat-events
---

# Fetch Live Stream Chat Events

#
  POST Fetch Live Stream Chat Events



Using this API, you can fetch multiple live stream chat events for the given live chat stream Ids.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/live-chat/fetch-live-stream-events

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters















****



| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| eventIds | Required | Refrers to the Live stream event ids.These are the live chat stream Ids that you received in the create live chat stream event API responseNote:If you pass any invalid event id in the request, the API response will be a success including the details for valid event Ids | List [String] |

**Dev Notes: **Steps to extract event Id from UI:

- Within Modern Care module, click on "Live Stream Care" available under "Brand Care"

- All the available live stream events will be visible in this section

- Click on the three dots besides the live stream event name

- Choose "Embed" option from the drop down menu that appears

- You can now extract the stream event Id from embed code

## Example - Request















Copy Code


 curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/live-chat/fetch-live-stream-events \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d ' {
    "eventIds": [
        "63aef5cdbf5a932511df5cca",
        "63ac3e44f7c76a70651a7afb"
    ]
}'






## Example - Response





{
   "data": [
       {
           "id": "63ac3e44f7c76a70651a7afb",
           "name": "2G_API2",
           "startTime": 1672232639516,
           "endTime": 1704025329000,
           "streamStatus": "IN_PROGRESS",
           "chatApplicationId": "app_600043918"
       },
       {
           "id": "63aef5cdbf5a932511df5cca",
           "name": "2G_API8",
           "startTime": 1672410913257,
           "endTime": 1672410940300,
           "streamStatus": "STOPPED",
           "chatApplicationId": "app_600016927"
       }
   ],
   "errors": []
}







### Response Parameters

































****









| Parameter | Description | Type |
| --- | --- | --- |
| id | Refers to the unique identifier for the live stream chat event | String |
| name | Refers to the name of the live stream chat event | String |
| startTime | Refers to the starting time of the live stream chat event | Long |
| endTime | Refers to the ending time of the live stream chat event | Long |
| streamStatus | Refers to the status of the live chat stream.Example: SCHEDULED, STOPPED, IN_PROGRESS, etc. | String |
| chatApplicationId | Refers to the unique chat application id of the live chat present on the Sprinklr platform | String |

[](https://dev.sprinklr.com/fetch-live-stream-chat-events)




[Back to top](https://dev.sprinklr.com/fetch-live-stream-chat-events)
