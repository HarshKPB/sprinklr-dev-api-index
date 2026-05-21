---
title: "Update Task"
slug: update-task
url: https://dev.sprinklr.com/update-task
---

# Update Task

#
 PUT  Update Task


	You can update a Task via this API call and you will get the updated task object as Response after making the Request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/task/{taskId}


### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/ /api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters












| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| assignment |  | Required | The object containing task assignment details. |  |
|  | assigneeId | Required | The Id of the user to whim the task is assigned. | String |
|  | assigneeType | Required | The type of user. | String |
|  | assignedById | Optional | The Id of the user who assigned the task. | String |
|  | assignmentTime | Optional | The time of assignment. | Epoch |
| taskType |  | Required | The type of task. | String |
| taskStatus |  | Required | The status of task. | String |
| title |  | Required | The title of task. | String |
| description |  | Required | The task description. | String |
| assetId |  | Required | The Id of the entity for which the task is created. | String |
| assetType |  | Required | The type of entity for which the task is created. | String |
| completionDate |  | Required | The task completion date. | Epoch |
| dueDate |  | Required | The task due date. | Epoch |
| customProperties |  | Required | The custom fields on the task. | Map<string, List<string>> |
| inactive |  | Required | True, if the task is inactive. | Boolean |
| newTaskId |  | Required | The task Id of the new task. | String |
| attachment |  | Required | The object containing attachment details of the task. |  |
|  | url | Required | The Url of the attachment. | URL |
|  | tittle | Optional | The title of the attachment. | String |
|  | description | Optional | The description related to attachment. | String |
|  | previewUrl | Required | Preview Url of the attachment. | URL |
|  | type | Required | The Type of attachment. | String |
| subscriber |  | Optional | Describer the schema for Subscriber. |  |
| queueIds |  | Optional | Queue Id for the task. | List<Long> |

## Example - Request















Copy Code



curl -X PUT \
 'https://api3.sprinklr.com/{env}/api/v2/task/{taskId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'
  -d'{
        "assignment": {
            "assigneeId": "600005371",
            "assigneeType": "USER"
        },
        "taskType": "Design Task",
        "taskStatus": "NEW",
        "title": "mahi task 1234 890",
        "description": "description",
        "assetId": "FACEBOOK_39_m_HMzX00-COmqKMDXnnejknYeOQi2LSz7h1eyCbN3C_F3MDatqkHz3PAeDT9pEfSR7iTn31yg4EJtwATHHDbC0ZQ_ACCOUNT_600001490_1593519956000_2020_06",
        "assetType": "MESSAGE",
        "dueDate": 1593523260000,
        "attachment": {
            "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_Eb-d27b1a43-7b71-47e1-9a10-50aabb63b146-1077356742.jpg",
            "title": "@TikTok_IN What is this? Mr. Nikhil Gandhi https://t.co/tHVVfIKgI6",
            "previewUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_Eb-d27b1a43-7b71-47e1-9a10-50aabb63b146-1077356742_p.jpg",
            "type": "IMAGE"
        },
        "queueIds": ["123"]
}'






## Example - Response





{
    "data": {
        "id": "5f04455b3b85b607a1ab2694",
        "assignment": {
            "assigneeId": "600005371",
            "assigneeType": "USER"
        },
        "taskType": "Design Task",
        "taskStatus": "NEW",
        "title": "mahi task 1234 890",
        "description": "description",
        "assetId": "FACEBOOK_39_m_HMzX00-COmqKMDXnnejknYeOQi2LSz7h1eyCbN3C_F3MDatqkHz3PAeDT9pEfSR7iTn31yg4EJtwATHHDbC0ZQ_ACCOUNT_600001490_1593519956000_2020_06",
        "assetType": "MESSAGE",
        "dueDate": 1593523260000,
        "customProperties": {},
        "inactive": false,
        "attachment": {
            "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_Eb-d27b1a43-7b71-47e1-9a10-50aabb63b146-1077356742.jpg",
            "title": "@TikTok_IN What is this? Mr. Nikhil Gandhi https://t.co/tHVVfIKgI6",
            "previewUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___pbs.twimg.com_media_Eb-d27b1a43-7b71-47e1-9a10-50aabb63b146-1077356742_p.jpg",
            "type": "IMAGE"
        },
        "queueDetails": [
            {
                "queueId": 123,
                "assignmentTime": 1594119713125
            }
        ],
        "createdTime": 1594115419177,
        "modifiedTime": 1594119713125
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

[](https://dev.sprinklr.com/update-task)




[Back to top](https://dev.sprinklr.com/update-task)
