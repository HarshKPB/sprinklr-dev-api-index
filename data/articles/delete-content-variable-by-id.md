---
title: "Delete Content Variable by Id"
slug: delete-content-variable-by-id
url: https://dev.sprinklr.com/delete-content-variable-by-id
---

# Delete Content Variable by Id

# DELETE  Delete Content Variable by Id

This endpoint deletes a specific Content Variable based on its ID. Use it to remove variables that are no longer needed, or that should not be used in content or workflows going forward.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/knowledgebase/content-variable/`{id}`

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

## Path Parameter

















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| id | Required | String | The unique identifier of the Content Variable. |

## Example Request

Copy Code


curl --location --request DELETE 'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/content-variable/67ee4505c166491398cfb057' \
--header 'Authorization: Bearer {Access_Token}'
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \

## Example - Response


204 No Content

**Developer Note:** 204 No Content implies that the Content Variable has been successfully deleted.

[](https://dev.sprinklr.com/delete-content-variable-by-id)

[Back to top](https://dev.sprinklr.com/delete-content-variable-by-id)
