---
title: "Read Task"
slug: read-task
url: https://dev.sprinklr.com/read-task
---

# Read Task

#
 GET  Read Task


You can use the api to fetch the details of a Task using task id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/task/{taskId}


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

### Path Parameters
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {taskId} | Required | Id of the task to fetch details. | String |

## Example - Request















Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/task/{taskId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'






## Example - Response





{
    "data": {
        "id": "5bb6f469e4b03310c324639f",
        "assignment": {
            "assigneeId": "0",
            "assigneeType": "USER"
        },
        "taskType": "Design Task",
        "taskStatus": "Approved",
        "title": "Task type check1538716711240",
        "assetId": "2_13",
        "assetType": "CAMPAIGN",
        "dueDate": 1538716837302,
        "customProperties": {
            "spr_task_status": [
                "Available"
            ],
            "spr_task_type": [
                "Design Task"
            ]
        },
        "inactive": false,
        "queueDetails": [],
        "createdTime": 1538716777315,
        "modifiedTime": 1589010980979
    },
    "errors": []
}







### Response Parameters











| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | The task Id. | String |
| assignment |  | The object containing task assignment details. |  |
|  | assigneeId | The Id of the user to whim the task is assigned. | String |
|  | assigneeType | The type of user. | String |
|  | assignedById | The Id of the user who assigned the task. | String |
|  | assignmentTime | The time of assignment. | Epoch |
| taskType |  | The type of task. | String |
| taskStatus |  | The status of task. | String |
| title |  | The title of task. | String |
| description |  | The task description. | String |
| assetId |  | The Id of the entity for which the task is created. | String |
| assetType |  | The type of entity for which the task is created. | String |
| completionDate |  | The task completion date. | Epoch |
| dueDate |  | The task due date. | Epoch |
| customProperties |  | The custom fields on the task. | Map<string, List<string>> |
| inactive |  | True, if the task is inactive. | Boolean |
| newTaskId |  | The task Id of the new task. | String |
| attachment |  | The object containing attachment details of the task. |  |
|  | url | The Url of the attachment. | URL |
|  | tittle | The title of the attachment. | String |
|  | description | The description related to attachment. | String |
|  | previewUrl | Preview Url of the attachment. | URL |
|  | type | The Type of attachment. | String |
| subscriber |  | Describer the schema for Subscriber. |  |
| queueDetails |  | Queue details of the task. | List<Queue> |
|  | queueId | Id of the queue. | Long |
|  | assignmentTime | The queue assignment time. | Epoch |
| createdTime |  | The created time of the task. | Epoch |
| modifiedTime |  | The Last modified time of the task. | Epoch |

[](https://dev.sprinklr.com/read-task)




[Back to top](https://dev.sprinklr.com/read-task)
