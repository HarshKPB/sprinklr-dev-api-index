---
title: "Delete Content Brief v1"
slug: delete-content-brief-v1
url: https://dev.sprinklr.com/delete-content-brief-v1
---

# Delete Content Brief v1

#
DELETE - Delete Content Brief


Using this API, you can delete the Content Brief using the unique content brief Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/content/brief/{Id}

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
| Id | Required | The content brief Id. | String |

### Example - Request

 Copy Code



curl -X DELETE \
'https://api3.sprinklr.com/{env}/api/v1/content/brief/6214a640c72c085362b89b87' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'accept: application/json'




### Example - Response




204 No Content





**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

[](https://dev.sprinklr.com/delete-content-brief-v1)




[Back to top](https://dev.sprinklr.com/delete-content-brief-v1)
