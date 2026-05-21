---
title: "Delete Knowledge Base Article"
slug: delete-knowledge-base-article
url: https://dev.sprinklr.com/delete-knowledge-base-article
---

# Delete Knowledge Base Article

#
  POST - Delete Knowledge Base Article


Using this API, you can delete a knowledge base article from within Sprinklr.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/delete

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












| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| isLngVariant | Required | If true, you are deleting a language variant of the article.Else, the base article will be deleted | Boolean |

### Request Parameters












| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | If you are deleting the base article, pass the  Id of the base article.If you are deleting a language variant, pass the id of the respective lngVariant | List [String] |

**Dev Notes: **Deleting the base article will delete all the translated articles too.

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/delete?isLngVariant=true' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
["6319e2ab3adc853b97d22fb5"]'
 

     
     
   

## Example - Response

 
 
     
 
204 No Content
 

     
     
   
 

**Dev Notes: **204 No Content Implies that the knowledge base article has been successfully deleted.

[](https://dev.sprinklr.com/delete-knowledge-base-article) 

 

 
[Back to top](https://dev.sprinklr.com/delete-knowledge-base-article)
