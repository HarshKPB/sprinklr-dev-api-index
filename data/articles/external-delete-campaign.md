---
title: "External Delete Campaign"
slug: external-delete-campaign
url: https://dev.sprinklr.com/external-delete-campaign
---

# External Delete Campaign

#
  DELETE External Delete Campaign


You can delete an External Campaign using external Id and source via this API call and on success you will get  HTTP/1.1 204 (No Content) as Response after making the Request.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/campaign/{externalSource}/{externalId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters





















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| externalSource | Required | Name of extenal source. | String |
| externalSourceId | Required | Id of the external source. | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
     
 curl -X DELETE \
  https://api3.sprinklr.com/{env}/api/v2/campaign/{externalSource}/{externalId} \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'
 

     
     
   

## Example - Response





HTTP/1.1 204 (No Content)







204 (No Content)  if successful otherwise 400.

 [](https://dev.sprinklr.com/external-delete-campaign)






[Back to top](https://dev.sprinklr.com/external-delete-campaign)
