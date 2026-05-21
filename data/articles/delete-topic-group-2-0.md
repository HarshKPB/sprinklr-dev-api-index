---
title: "Delete Topic Group 2.0"
slug: delete-topic-group-2-0
url: https://dev.sprinklr.com/delete-topic-group-2-0
---

# Delete Topic Group 2.0

#
  DELETE - Delete Topic Group


You can delete a Topic Group using Topic Group Id with this API call.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/listening-topic-group/{Id}

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
| Id | Required | The unique Id of the Topic Group you want to delete. | String |

## Example - Request




 Copy Code


>curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v2/listening-topic-group/{Id}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'



## Example - Response




HTTP/1.1 204 (No Content)





[](https://dev.sprinklr.com/delete-topic-group-2-0)




[Back to top](https://dev.sprinklr.com/delete-topic-group-2-0)
