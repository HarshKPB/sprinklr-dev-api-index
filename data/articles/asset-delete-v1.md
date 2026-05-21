---
title: "Asset Delete v1"
slug: asset-delete-v1
url: https://dev.sprinklr.com/asset-delete-v1
---

# Asset Delete v1

#  DELETE Asset Delete v1

Using this API, you can delete an asset from the Sprinklr Asset Manager.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/sam/{assetId}

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

### Query Parameters

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetId | Required | The Id of the asset which needs to be deleted | String |

### Example - Request




 Copy Code


curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v1/sam/57bc8723e4b0a2509nj66726' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



### Example - Response



HTTP/1.1 204 (No Content)



[](https://dev.sprinklr.com/asset-delete-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-delete-v1)
