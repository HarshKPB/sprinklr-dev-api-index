---
title: "Delete User"
slug: delete-user
url: https://dev.sprinklr.com/delete-user
---

# Delete User

#
  DELETE - Delete User

	 You can delete a user of a given userId from all clients via this API call and you will get `HTTP/1.1 204 No Content` as Response after making the Request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/{userId}

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
| Content-Type | application/scim+json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

## Path Paramenter



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userId | Required | The Sprinklr user Id which needs to be deleted. | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v2/scim/{userId}' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}'
 

     
     
   

## Example - Response

 
 
     
 
	HTTP/1.1 204 No Content
 

     
     
   
 
[](https://dev.sprinklr.com/delete-user) 

 

 
[Back to top](https://dev.sprinklr.com/delete-user)
