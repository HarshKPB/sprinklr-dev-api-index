---
title: "Fetch Live Stream Chat Event"
slug: fetch-live-stream-chat-event
url: https://dev.sprinklr.com/fetch-live-stream-chat-event
---

# Fetch Live Stream Chat Event

#
  GET Fetch Live Stream Chat Event



Using this API, you can fetch a single chat event for the given live chat stream Id

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/live-chat/fetch-live-stream-event/{id}

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

### Path Parameter

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Live stream event id.This is the live chat stream Id you received in the create live chat stream event API response | String |

**Dev Notes: **Steps to extract event Id from UI:

- Within Modern Care module, click on "Live Stream Care" available under "Brand Care"

- All the available live stream events will be visible in this section

- Click on the three dots besides the live stream event name

- Choose "Embed" option from the drop down menu that appears

- You can now extract the stream event Id from embed code

## Example - Request















Copy Code


 curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/live-chat/fetch-live-stream-event/63aef5cdbf5a932511df5cca' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






### Example - Response





{
   "data": {
       "id": "63aef5cdbf5a932511df5cca",
       "name": "2G_API8",
       "startTime": 1672410913257,
       "endTime": 1672410940300,
       "streamStatus": "STOPPED",
       "chatApplicationId": "app_600016927"
   },
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

[](https://dev.sprinklr.com/fetch-live-stream-chat-event)




[Back to top](https://dev.sprinklr.com/fetch-live-stream-chat-event)
