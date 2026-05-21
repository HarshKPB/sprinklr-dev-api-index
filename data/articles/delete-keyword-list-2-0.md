---
title: "Delete Keyword List 2.0"
slug: delete-keyword-list-2-0
url: https://dev.sprinklr.com/delete-keyword-list-2-0
---

# Delete Keyword List 2.0

#
  DELETE - Delete Keyword List

You can delete a Keyword List using the unique keyword list Id with this API call.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/keyword-list/{Id}

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
| Id | Required | Id of the keyword list you want to delete. | String |

## Example - Request




 Copy Code



curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v2/keyword-list/{Id}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





## Example - Response



204 No Content





**Dev Notes: **204 No Content implies that the keyword list associated with the given Id has been successfully deleted.

[](https://dev.sprinklr.com/delete-keyword-list-2-0)




[Back to top](https://dev.sprinklr.com/delete-keyword-list-2-0)
