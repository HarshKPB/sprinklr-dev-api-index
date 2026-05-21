---
title: "Delete Campaign"
slug: delete-campaign
url: https://dev.sprinklr.com/delete-campaign
---

# Delete Campaign

#
  DELETE Delete Campaign

You can delete a Campaign using campaignId via this API call and on success you will get  HTTP/1.1 204 (No Content) as Response after making the Request.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/campaign/{campaignId}

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
| {campaignId} | Required | Id of the campaign that needs to be deleted. | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
     
 
curl -X DELETE \
  https://api3.sprinklr.com/{env}/api/v2/campaign/{campaignId} \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
  
  

## Example - Response





	HTTP/1.1 204 (No Content)







204 (No Content) if successful otherwise 400.

	  [](https://dev.sprinklr.com/delete-campaign)




[Back to top](https://dev.sprinklr.com/delete-campaign)
