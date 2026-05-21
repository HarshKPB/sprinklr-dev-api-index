---
title: "Deflection API"
slug: deflection-api
url: https://dev.sprinklr.com/deflection-api
---

# Deflection API

#
POST Deflection API

You can use this API to deflect the customer call to Modern Engagement channels via giving option in IVR.

**Related Knowledge Base Article:** **[Implement IVR Deflection](https://www.sprinklr.com/help/articles/ivr-use-cases/deflection-to-other-channel/63d7c434468ae80d39347af2)**

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/deflect

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

## Request Parameters














































































| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| assetId | Required | Id of the asset to be sent.. | String |
| snId | Required | Social network id of the profile for which deflection is being done. | String |
| accountId | Required | Account id to use for replying. | String |
| deflectionType | Required | Channel being deflected to. | String |
| createCase | Optional | Whether or not a new case needs to be created. Default value is true. | Boolean |
| caseNumber | Optional | Case number to which the conversation needs to be linked. | String |
| customProperties | Optional | Refers to the map of case custom properties and the corresponding values | Map<String, List<String>> |
| messageCustomProperties | Optional | Refers to the map of outbound message custom properties and the corresponding values | Map<String, List<String>> |
| comment | Optional | Any comments to be included from any previous cases/interactions in the case. | String |
| configId | Optional | Id of configuration which contains the logic if the message is to be associated to already existing case or to create a new case. | String |
| urlShortnerId | Optional | Id of the urlShortner when sending a deflection link. (Used when sending a link in SMS for deflection to Apple Business Chat or Live Chat). | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
		curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/deflect' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "assetId": "5e6f8c7d9bf510038b93c3ed",
    "snId": "917382455480",
    "accountId": 100099022,
    "deflectionType": "WHATSAPP_BUSINESS",
    "createCase": true,
    "messageCustomProperties": {
        "_c_61162c4650452b7c29f4cb2c": [
            "Test1"
        ]
    },
    "customProperties": {
        "_c_609b17a8b637cf5e52b848c0": [
            "Test2"
        ],
        "_c_609b18fdb637cf5e52b897a7": [
            "Test3"
        ],
        "_c_609b192eb637cf5e52b8a42d": [
            "Test4"
        ]
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": {
        "data": "[\"gBGGM2QYEJR_AgkpF9ry2N9IuLk\"]",
        "errors": []
    },
    "errors": []
}
 

     
     
   
 

## Example - viaAccount Deflection

When you are deflecting to a social channel using another social channel, like deflecting to Sprinklr Live Chat via SMS.
 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
	curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/deflect' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
   "assetId" : "5e6f8c7d9bf51gfh57d3c3ed",
    "snId" : phone,
    "accountId" : 100022,
    "deflectionType" : "SPRINKLR_LIVE_CHAT",
    "viaDeflectionType" : "SMS",
    "viaAccountId" : 100122,
    "createCase" : true
}'
 

     
     
   

## Response Parameters
















| Parameter | Description | Type |
| --- | --- | --- |
| gBEGkXOCRVSAAgkZjtqUyuIMJ1I | Represents the Social Network Message id of published message. | String |

	[](https://dev.sprinklr.com/deflection-api) 

 

 
[Back to top](https://dev.sprinklr.com/deflection-api)
