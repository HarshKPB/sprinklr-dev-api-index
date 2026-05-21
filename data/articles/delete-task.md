---
title: "Delete Task"
slug: delete-task
url: https://dev.sprinklr.com/delete-task
---

# Delete Task

#
 DELETE   Delete Task



You can use the api to delete a Task using task id.

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



curl -X DELETE \
 'https://api3.sprinklr.com/{env}/api/v2/task/{taskId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'






## Example - Response





204 No Content






[](https://dev.sprinklr.com/delete-task)




[Back to top](https://dev.sprinklr.com/delete-task)
