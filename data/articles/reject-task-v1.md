---
title: "Reject Task v1"
slug: reject-task-v1
url: https://dev.sprinklr.com/reject-task-v1
---

# Reject Task v1

#
PUT Reject Task v1

This API rejects a publishing task by updating its status and optionally including a rejection comment.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/publishing/`{taskId}`/reject

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
| taskId | Long | Unique ID of the publishing task to approve. |


### Request Body Parameters

















| Parameter | Type | Description |  |
| --- | --- | --- | --- |
| comment | String | Optional | Optional comment for the approval. |


### Example Request




 Copy Code


curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v1/publishing/161741/reject' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {api_key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{    "comment": "rejected"
}' 

     
     
   

### Example - Response



 
204 No Content
 

     
     
   
 

	[](https://dev.sprinklr.com/reject-task-v1) 

 

 
[Back to top](https://dev.sprinklr.com/reject-task-v1)
