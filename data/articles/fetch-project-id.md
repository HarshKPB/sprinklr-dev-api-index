---
title: "Fetch Project Id"
slug: fetch-project-id
url: https://dev.sprinklr.com/fetch-project-id
---

# Fetch Project Id

#
  GET - Fetch Project Id

Using this API, you can find the project Id for the advocacy community instance using the unique project key.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/xb-community/projectId/{projectKey}

**Dev Notes: **To get access to the unique project key, kindly reach out to the Advocacy support team.

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| projectKey | Required | The unique project key for the advocacy community | String |

### Example - Request




 Copy Code



curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/xb-community/projectId/qa4Interest’ \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





### Example - Response





 {
   "data": "04b70a51-ad01-4872-90fd-47449cfd3e16",
   "errors": []
}





### Response Parameters











| Key | Value | Description |
| --- | --- | --- |
| data | The project Id for the advocacy community | String |

	 [](https://dev.sprinklr.com/fetch-project-id)




[Back to top](https://dev.sprinklr.com/fetch-project-id)
