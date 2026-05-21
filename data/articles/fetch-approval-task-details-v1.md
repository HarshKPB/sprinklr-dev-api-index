---
title: "Fetch Approval Task Details v1"
slug: fetch-approval-task-details-v1
url: https://dev.sprinklr.com/fetch-approval-task-details-v1
---

# Fetch Approval Task Details v1

#
GET Fetch Approval Task Details v1

This API fetches detailed information about an approval task associated with a specific post.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/tasks/approval/POST_APPROVAL/`{postId}`

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
















| Parameter | Type | Description |
| --- | --- | --- |
| postId | Long | Unique identifier of the post for which the approval task details are to be fetched. |


### Example Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X GET \ 'https://api3.sprinklr.com/{env}/api/v1/tasks/approval/POST_APPROVAL/2166263375' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {api_key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \'
 

     
     
   

### Example - Response

 
 
     
 
[
    {
        "approvalTask": {
            "postId": 2166263375,
            "approvalPathId": "6618c923e4c3de47d0cb13a6",
            "stepId": 0,
            "minimumApprovalsRequired": -1,
            "approvalObjectId": "2166263375",
            "reminderCount": 0,
            "documentType": "TASK",
            "ownerUserId": 1000059523,
            "createdTime": 1744706988896,
            "modifiedTime": 1744706989097,
            "deleted": false,
            "inactive": false,
            "currentStatus": "AVAILABLE",
            "assigneeType": "USER",
            "assigneeId": 1000059523,
            "id": 161741,
            "dueDate": 2208988800000,
            "taskType": "POST_APPROVAL",
            "version": 0,
            "createdTimeInMillis": 1744706988896,
            "additional": {}
        }
    }
]
 

     
     
   
 

### API Response Schema

































| Field | Type | Description |
| --- | --- | --- |
| postId | Long | ID of the post linked to the approval task. |
| approvalPathId | String | Identifier for the approval path. |
| stepId | Integer | Step number in the approval flow. |
| minimumApprovalsRequired | Integer | Minimum number of approvals required. |
| approvalObjectId | Long | Object ID associated with the approval (usually same as postId). |
| reminderCount | Integer | Number of reminders sent for the approval. |
| documentType | String | Type of document (e.g., TASK). |
| ownerUserId | Long | User ID of the task owner. |
| createdTime | Long | Task creation timestamp (epoch millis). |
| modifiedTime | Long | Task last modified timestamp (epoch millis). |
| deleted | Boolean | Whether the task has been deleted. |
| inactive | Boolean | Whether the task is inactive. |
| currentStatus | String | Current status of the task (e.g., AVAILABLE). |
| assigneeType | String | Type of the assignee (USER, GROUP, etc.). |
| assigneeId | Long | ID of the user/group assigned to the task. |
| id | Long | Unique ID of the approval task. |
| dueDate | Long | Due date timestamp (epoch millis). |
| taskType | String | Type of the task (POST_APPROVAL). |
| version | Integer | Version number of the task. |
| createdTimeInMillis | Long | Creation time in milliseconds (same as createdTime). |
| additional | Object | Placeholder for additional metadata (empty by default). |


	[](https://dev.sprinklr.com/fetch-approval-task-details-v1) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-approval-task-details-v1)
