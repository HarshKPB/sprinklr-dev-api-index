---
title: "Create Update Live Chat Event"
slug: create-update-live-chat-event
url: https://dev.sprinklr.com/create-update-live-chat-event
---

# Create Update Live Chat Event

#
  POST Create Update Live Chat Event




Using this API, you can create or update a live chat event for sending or receiving messages.

## API Endpoint

https://api3.sprinklr.com/{env}//api/v2/live-chat/create-or-update-live-stream-event

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
| id | Required for updating a live chat event | Live stream event id.Note: Only used for updating the live chat event | String |
| name | Required | Live stream event name | String |
| startTime | Required | Starting time of the Live stream event | Long |
| endTime | Required | Ending time of the Live stream event | Long |
| chatApplicationId | Required | Refers to the unique identifier for the live chat application.Should be a valid live chat application Id | String |

**Dev Notes: **Steps to extract Chat Application Id and Event Id from UI:

- Within Modern Care module, click on "Live Stream Care" available under "Brand Care"

- All the available live stream events will be visible in this section

- Click on the three dots besides the live stream event name

- Choose "Embed" option from the drop down menu that appears

- You can now extract the Chat Application Id and stream event Id from embed code

## Example - Create Live Stream Chat Event















Copy Code


 curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/live-chat/create-or-update-live-stream-event \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
           "name": "Test Stream-2",
           "startTime": 1672221658778,
           "endTime": 1672226535392,
           "chatApplicationId": "app_600000938"
       }'






## Example - Response





{
   "data": {
       "id": "63c12d22a2f7d761509a47a2",
       "name": "Test Stream-2",
       "startTime": 1672221658778,
       "endTime": 1672226535392,
       "streamStatus": "IN_PROGRESS",
       "chatApplicationId": "app_600000938"
   },
   "errors": []
}







## Example - Update Live Stream Chat Event















Copy Code


 curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/live-chat/create-or-update-live-stream-event \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
       "id": "63c12d22a2f7d761509a47a2",
       "name": "Test Stream-2",
       "startTime": 1672221658778,
       "endTime": 1672226535392,
       "chatApplicationId": "app_600000938"
   }'






## Example - Response





{
   "data": {
       "id": "63c12d22a2f7d761509a47a2",
       "name": "Test Stream-2",
       "startTime": 1672221658778,
       "endTime": 1672226535392,
       "streamStatus": "STOPPED",
       "chatApplicationId": "app_600000938"
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

[](https://dev.sprinklr.com/create-update-live-chat-event)




[Back to top](https://dev.sprinklr.com/create-update-live-chat-event)
