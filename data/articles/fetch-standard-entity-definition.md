---
title: "Fetch Standard Entity Definition"
slug: fetch-standard-entity-definition
url: https://dev.sprinklr.com/fetch-standard-entity-definition
---

# Fetch Standard Entity Definition

#
  GET - Fetch Standard Entity Definition

With this API, you can fetch the pre-defined standard entity definition details using the unique definition Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/definition/{entityDefinitionId}

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














****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionSupported entity Ids: _s_Consent, _s_PublishingQueue, _s_ConsentCatalogue, _s_PriceBook, _s_PublisherSettings | string |

### Example - Request














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/definition/_s_Consent’ /
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''





### Example - Response





{
   "data": {
       "id": "_s_Consent",
       "name": "User Consent",
       "pluralName": "User Consents",
       "description": "Entity to capture various kind of user consent",
       "createdTime": 0,
       "modifiedTime": 0
   },
   "errors": []
}





### Response Parameters
















| Parameters | Description | Type |
| --- | --- | --- |
| id | Refers to the standard entity definition Id | String |
| name | Refers to the name of the standard entity definition | String |
| pluralName | Refers to the name of the standard entity in plural form | String |
| description | Refers to the description of the standard entity | String |
| createdTime | Refers to the time at which the standard entity was created | Epoch |
| modifiedTime | Refers to the time at which the standard entity was modified | Epoch |

[](https://dev.sprinklr.com/fetch-standard-entity-definition)




[Back to top](https://dev.sprinklr.com/fetch-standard-entity-definition)
