---
title: "Fetch Content Template Details by Channel Type"
slug: fetch-content-template-details-by-channel-type
url: https://dev.sprinklr.com/fetch-content-template-details-by-channel-type
---

# Fetch Content Template Details by Channel Type

#
GET Fetch Content Template Details by Channel Type

This API helps fetch content template id and name details, which are specific to a [channel type](https://dev.sprinklr.com/channels-v1).

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/contentTemplate/findAll?channelTypes={channelType}

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

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET\
   'https://api3.sprinklr.com/{env}/api/v2/contentTemplate/findAll?channelTypes=EMAIL' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
 

     
     
   

## Example - Response

 
 
     
 

```

{
   "data": [
       {
           "id": "69bbb004e4b0fa51134c70ac",
           "name": "Template1"
       },
       {
           "id": "58bbb026e4b03265b9ddff19",
           "name": Template2"
       },
       {
           "id": "58bbb086e4b03265b9ddff87",
           "name": "Template3"
       },
       {
           "id": "58bcf82ce4b0ea4a91ecbbf5",
           "name": "Template4"
       }
],
   "errors": []
}
 

     
     
   
 

### Response Parameters














| Parameter | Definition | Type |
| --- | --- | --- |
| id | Id of the content template | String |
| name | The name of the content template | String |

			[](https://dev.sprinklr.com/fetch-content-template-details-by-channel-type) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-content-template-details-by-channel-type)
