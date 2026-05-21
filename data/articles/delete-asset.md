---
title: "Delete Asset"
slug: delete-asset
url: https://dev.sprinklr.com/delete-asset
---

# Delete Asset

#
  DELETE - Delete Asset


You can delete a sprinklr asset via this API call and you will get 204 (No Content) as Response after making the Request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/sam/{assetId}


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
| assetId | Required | Asset id of the existing Sprinklr asset, you want to delete. | String |

## Example - Request




 Copy Code



curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v2/sam/{assetId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
 

## Example - Response




HTTP/1.1 204 (No Content)
 

     
     
   
 
[](https://dev.sprinklr.com/delete-asset) 

 

 
[Back to top](https://dev.sprinklr.com/delete-asset)
