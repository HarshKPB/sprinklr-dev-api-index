---
title: "v1 Case Delete"
slug: v1-case-delete
url: https://dev.sprinklr.com/v1-case-delete
---

# v1 Case Delete

#
DELETE v1 Case Delete


Using this API, you can delete an existing case in Sprinklr.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/case/{caseId}

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

## Path Parameter

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| caseId | Required | The Id/number of the case which needs to be deleted | String |

## Example - Sample Call

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
		curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v1/case/121662' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   
 
 
     

	200 OK
 

     
     
   
 

	[](https://dev.sprinklr.com/v1-case-delete) 

 

 
[Back to top](https://dev.sprinklr.com/v1-case-delete)
