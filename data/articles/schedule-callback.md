---
title: "Schedule Callback"
slug: schedule-callback
url: https://dev.sprinklr.com/schedule-callback
---

# Schedule Callback

#
 POST  Schedule Callback



Using this API, brands can schedule callbacks directly from the IVR. This feature comes in handy when customers face extended wait times or need assistance during off-hours.

## API Endpoint

https://api3.sprinklr.com`/{env}/`/api/v2/voice/schedule-callback

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
























































****











| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| campaignId | Required | Refers to the campaign under which the call needs to be scheduled | String |
| phoneNumber | Required | Refers to the phone number to which the callback is scheduled | String |
| WorkqueueID | Required | String |  |
| WorkqueueName | Required | Refers to the name of the work queue. | String |
| requiredSkills | Optional | An Object in a key-value pair where the key is the skill id and the value is the minimum required proficiency level. Example: "requiredSkills": {"65faaef0a4df7700e55c4351": 80} | Object |
| priority | Optional | This attribute lets you define the callback’s priority. | Integer |
| fromTime | Optional | This attribute specifies the callback time as an epoch timestamp. If both fromTime and SlotInformation are provided, the callback time is derived from SlotInformation. If both attributes are not provided, the system schedules the callback 30 seconds afterwards. | String |
| customProperties | Optional | Refers to the object defining the key and value pair for the custom propertiesNote: Only “Task” and “Case” level asset properties can be defined in the API request | Object |
| slotInformation | Optional | Refers to the object containing the slot id, slot config id, starttime and endtimeYou can fetch the slot object details from the fetch slot details API | Object |

### slotInformation Object Description Table












| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| startTime | Required | Refers to the start time of the slot | Epoch (Milliseconds) |
| endTime | Required | Refers to the end time of the slot | Epoch (Milliseconds) |
| available | Required | If true, the slot is available | Boolean |
| slotConfigId | Required | Refers to the unique identifier for the slot | String |
| slotDefinitionId | Required | Refers to the unique identifier for the slot definition | String |

## Example - Request















Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/voice/schedule-callback \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "campaignId": "66000002_3374",
    "phoneNumber": "+911234567891",
    "fromTime": "1771237253000",
    "priority": 70,
    "requiredSkills": {
        "65faaef0a4df7700e55c4351": 80
    },
    "workQueueId": "685541e4939f5541dc2b3fdd",
    "workQueueName": "Test work queue",
    "customProperties": {
        "_c_652649bc2113dd326b9b6767": [
            "12345"
        ],
        "_c_652649bb2113dd326b9b6669": [
            "Interaction Date"
        ]
    },
     "SlotInformation":
            {
                "startTime": 1771074600000,
                "endTime": 1771076400000,
                "available": true,
                "slotConfigId": "6915e164eab8a713f8b1bf4d",
                "slotDefinitionId": "68931a97bb28be4632a1e375"
            }
}'






## Example - Response





{
    "data": {
        "taskId": "698f2dca459f7a7f223c8ffa"
    },
    "errors": []
}







### Response Definition
















| Parameter | Description | Type |
| --- | --- | --- |
| taskId | Refers to the unique identifier for the updated callback request | String |

[](https://dev.sprinklr.com/schedule-callback)




[Back to top](https://dev.sprinklr.com/schedule-callback)
