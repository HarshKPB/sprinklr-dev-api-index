---
title: "Fetch Standard Entity Field Using apiName"
slug: fetch-standard-entity-field-using-apiname
url: https://dev.sprinklr.com/fetch-standard-entity-field-using-apiname
---

# Fetch Standard Entity Field Using apiName

#
  GET - Fetch Standard Entity Field Using apiName

Using this API, you can fetch the configured details for the standard entity field using the unique apiName.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/field/{entityDefinitionId}/{apiName}

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
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionSupported entity Definition Ids: _s_Consent, _s_PublishingQueue, _s_ConsentCatalogue, _s_PriceBook, _s_PublisherSettings | string |
| apiName | Required | Refers to the unique name configured for the field | String |

### Example - Request














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/field/_s_Consent/ConsentAgeNew’ /
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''





### Example - Response





{
    "data": {
        "id": "_s_Consent_ConsentAgeNew",
        "apiName": "ConsentAgeNew",
        "name": "User Consent Age 2",
        "type": "TEXT",
        "entityDefinitionId": "_s_Consent",
        "parentChild": false,
        "multivalued": false,
        "picklistValues": []
    },
    "errors": []
}





[](https://dev.sprinklr.com/fetch-standard-entity-field-using-apiname)




[Back to top](https://dev.sprinklr.com/fetch-standard-entity-field-using-apiname)
