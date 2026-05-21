---
title: "Task Webhooks"
slug: task-webhooks
url: https://dev.sprinklr.com/task-webhooks
---

# Task Webhooks

# Task Webhooks

**Task Webhook Subscriptions:**
 Task Create, Task Update and Task Delete

Whenever an action is performed on task either via Sprinklr UI or API, the webhook notification are triggered with the details that are described in the following documents:


- [Task.Created Webhook](https://dev.sprinklr.com/task-webhooks#taskCreate)

- [Task.Updated Webhook](https://dev.sprinklr.com/task-webhooks#taskUpdate)

- [Task.Deleted Webhook](https://dev.sprinklr.com/task-webhooks#taskDelete)

### Task.Create Webhook




  Copy Code



{
  "id": "5f9120bc1b61ad6029c29dc4",
  "type": "task.create",
  "payload": {
    "id": "5f9120bc1b61ad6829c29dc2",
    "assignment": {},
    "taskType": "Review Task",
    "taskStatus": "AVAILABLE",
    "title": "2",
    "assetId": "MESSAGE_3921426077",
    "assetType": "OUTBOUND_MESSAGE",
    "dueDate": 1613631480000,
    "customProperties": {
      "spr_ut_status": [
        "New"
      ]
    },
    "inactive": false,
    "queueDetails": [],
    "createdTime": 1603346620661,
    "modifiedTime": 1603346620661
  },
  "eventTime": 1603346620695,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf07e0a2"
  }
}





### Task.Update Webhook




  Copy Code



{
  "id": "5f9120bc302a696349e15980",
  "type": "task.update",
  "payload": {
    "id": "5f9120a6fecf0f378cd86abc",
    "assignment": {
      "assigneeType": "USER"
    },
    "taskType": "Review Task",
    "taskStatus": "COMPLETED",
    "title": "1",
    "assetId": "MESSAGE_3921420677",
    "assetType": "OUTBOUND_MESSAGE",
    "completionDate": 1603346620475,
    "dueDate": 1603432998855,
    "customProperties": {
      "spr_ut_status": [
        "New"
      ]
    },
    "inactive": false,
    "queueDetails": [
      {
        "queueId": 102879,
        "assignmentTime": 1603346599054
      }
    ],
    "createdTime": 1603346599054,
    "modifiedTime": 1603346620475
  },
  "eventTime": 1603346620510,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf07e0a2"
  }
}





### Task.Delete Webhook




  Copy Code



{
  "id": "5f90114551b66f612bc4606b",
  "type": "task.delete",
  "payload": "5f900d9251b66f612ac39a61",
  "eventTime": 1603277125615,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf07e0a2"
  }
}





### Response Definition




















































































































































































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
| queueDetails |  | Queue details of the task. | List<Queue> |
|  | queueId | Id of the queue. | Long |
|  | assignmentTime | The queue assignment time. | Epoch |
| createdTime |  | The created time of the task. | Epoch |
| modifiedTime |  | The Last modified time of the task. | Epoch |

[](https://dev.sprinklr.com/task-webhooks)

[Back to top](https://dev.sprinklr.com/task-webhooks)
