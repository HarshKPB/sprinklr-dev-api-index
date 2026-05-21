---
title: "Delete Post"
slug: delete-post
url: https://dev.sprinklr.com/delete-post
---

# Delete Post

#
DELETE Delete Post

You can delete a post using post Id with this API call.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/publishing/post/{postId}

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```




			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |

### Path Parameter















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {postId} | Required | Unique Id of the published post. | String |

## Example

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post/{postId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

## Example - Response

 
 
     

HTTP/1.1 204 (No Content)
 

     
     
   
 

	[](https://dev.sprinklr.com/delete-post) 

 

 
[Back to top](https://dev.sprinklr.com/delete-post)
