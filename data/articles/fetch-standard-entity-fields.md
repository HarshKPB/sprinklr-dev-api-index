---
title: "Fetch Standard Entity Fields"
slug: fetch-standard-entity-fields
url: https://dev.sprinklr.com/fetch-standard-entity-fields
---

# Fetch Standard Entity Fields

#
  GET - Fetch Standard Entity Fields

Using this API, you can fetch all the standard entity fields created for the given definition Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/fields/{entityDefinitionId}

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

### Example - Request














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/fields/_s_Consent’ /
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''





### Example - Response





{
    "data": [
        {
            "id": "_s_Consent_modifiedTime",
            "apiName": "modifiedTime",
            "name": "User Consent Modified Date",
            "type": "DATETIME",
            "entityDefinitionId": "_s_Consent",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        },
        {
            "id": "_s_Consent__c_consentName",
            "apiName": "_c_consentName",
            "name": "User Consent Name",
            "type": "TEXT",
            "entityDefinitionId": "_s_Consent",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        },
        {
            "id": "_s_Consent__c_ConsentNumber",
            "apiName": "_c_ConsentNumber",
            "name": "User Consent Number",
            "type": "TEXT",
            "entityDefinitionId": "_s_Consent",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        },
        {
            "id": "_s_Consent_channel",
            "apiName": "channel",
            "name": "Sprinklr Channel",
            "description": "",
            "type": "TEXT",
            "entityDefinitionId": "_s_Consent",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        },
        {
            "id": "_s_Consent_entityId",
            "apiName": "entityId",
            "name": "User Consent Id",
            "type": "TEXT",
            "entityDefinitionId": "_s_Consent",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        },
        {
            "id": "_s_Consent_ConsentSource",
            "apiName": "consentSource",
            "name": "Consent Source",
            "description": "Place where consent was given",
            "type": "TEXT",
            "entityDefinitionId": "_s_Consent",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        }
    ],
    "errors": []
}





[](https://dev.sprinklr.com/fetch-standard-entity-fields)




[Back to top](https://dev.sprinklr.com/fetch-standard-entity-fields)
