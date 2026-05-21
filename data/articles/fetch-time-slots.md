---
title: "Fetch Time Slots"
slug: fetch-time-slots
url: https://dev.sprinklr.com/fetch-time-slots
---

# Fetch Time Slots

#
 POST  Fetch Time Slots


	Using this API, you can fetch the available slot information for the given work queue Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/work-queue/slot-information

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


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
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| workQueueId | Required | Refers to the work queue Id to which the callback request needs to be assigned | String |

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/work-queue/slot-information'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -H 'accept: application/json'
  -d '{
    "workQueueId": "65d8ed2fc5105e19393ebbbe"
}'






## Example - Response





{
    "data": {
        "WorkQueueName": "Work Queue 1",
        "WorkQueueId": "65d8ed2fc5105e19393ebbbe",
        "SlotInformation": [
            {
                "startTime": 1715943600000,
                "endTime": 1715945400000,
                "available": true,
                "slotConfigId": "662f6a84d0783e4268ef7d3e",
                "slotDefinitionId": "662f6a84d0783e4268ef7d3f"
            },
            {
                "startTime": 1716543600000,
                "endTime": 1716545400000,
                "available": true,
                "slotConfigId": "662f6a84d0783e4268ef7d3e",
                "slotDefinitionId": "662f6a84d0783e4268ef7d3f"
            }
        ]
    },
    "errors": []
}







### Response Parameters



























































| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| workQueueId |  | Refers to the work queue Id to which the callback request needs to be assigned | String |
| workQueueName |  | Refers to the name assigned to the work queue | String |
| slotInformation |  | Refers to the array containing the available slots' details | Array |
|  | startTime | Refers to the start time of the available slot | Epoch (milliseconds) |
|  | endTime | Refers to the end time of the available slot | Epoch (milliseconds) |
|  | available | If true, the slot is available for booking | Boolean |
|  | slotConfigId | Refers to the unique identifier for the slot | String |
|  | slotDefinitionId | Refers to the unique identifier for the slot definition | String |

[](https://dev.sprinklr.com/fetch-time-slots)




[Back to top](https://dev.sprinklr.com/fetch-time-slots)
