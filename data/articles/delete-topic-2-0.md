---
title: "Delete Topic 2.0"
slug: delete-topic-2-0
url: https://dev.sprinklr.com/delete-topic-2-0
---

# Delete Topic 2.0

#
  DELETE - Delete Topic


You can use this API end-point to delete a Listening Topic using the unique Id of the Listening Topic.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/listening-topic/{topicId}

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
| topicId | Required | The Listening Topic ID of the Listening Topic you want to delete. | String |

## Example - Request




 Copy Code


curl -X DELETE \
 'https://api3.sprinklr.com/{env}/api/v2/listening-topic/{topicId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'



## Example - Response



HTTP/1.1 204 (No Content)



[](https://dev.sprinklr.com/delete-topic-2-0)




[Back to top](https://dev.sprinklr.com/delete-topic-2-0)
