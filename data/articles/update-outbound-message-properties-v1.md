---
title: "Update Outbound Message Properties v1"
slug: update-outbound-message-properties-v1
url: https://dev.sprinklr.com/update-outbound-message-properties-v1
---

# Update Outbound Message Properties v1

#
POST Update Outbound Message Properties v1

Using this API, you can update customer properties associated with an outbound message.

**Dev Notes: **This API will update the custom fields passed in the payload and remove existing custom fields if not passed in the payload.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/outbound/posts/`{postId}`/properties


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

### Query Parameters












[Read Post by Post Id](https://dev.sprinklr.com/read-post-by-post-id-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| version | Required | Refers to the current version of the message and should be an exact match or you'll receive an errorYou can fetch the current version using "" API. Refer to the version field in the API response. | Integer |

## Request Parameters













| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| partnerCustomProperties | Optional | Key and value pair for custom properties at global levelSyntax Example: {         "_c_6464cca6756ab906d3373f99": [             "TEST1"         ] } | Object |
| clientCustomProperties | Optional | Key and value pair for custom properties at workspace levelSyntax Example: {         "_c_6464cca6756ab906d3373f54": [             "TEST2"         ] } | Object |

## Example: Update Custom Properties

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X POST \
  'https://api3.sprinklr.com/{env}api/v1/outbound/posts/10005188644/properties?version=2' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "partnerCustomProperties": {
        "_c_6464cca6756ab906d3373f99": [
            "TEST 1"
        ]
    },
    "clientCustomProperties": {
        "645402c7bc81745149abd4ac": [
            "TEST 2"
        ]
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
204 No Content
 

     
     
   
 

**Dev Notes: **`"204 No Content"` implies that the custom fields have been updated successfully. Kindly recheck the version configured in the query parameters if you receive `"500 Internal Server Error"`. Updating the version to a valid value will will help resolve this error.

	[](https://dev.sprinklr.com/update-outbound-message-properties-v1) 

 

 
[Back to top](https://dev.sprinklr.com/update-outbound-message-properties-v1)
