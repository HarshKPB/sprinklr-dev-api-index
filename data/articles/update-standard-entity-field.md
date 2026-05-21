---
title: "Update Standard Entity Field"
slug: update-standard-entity-field
url: https://dev.sprinklr.com/update-standard-entity-field
---

# Update Standard Entity Field

#
  PUT - Update Standard Entity Field

Using this API, you can update the details for the standard entity field.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/field/{entitydefinitionId}/{apiName}

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
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionSupported entity Definition Ids: _s_Consent, _s_PublishingQueue, _s_ConsentCatalogue, _s_PriceBook, _s_PublisherSettings | String |
| apiName | Required | Refers to the unique name configured for the field you wish to update | String |

### Request Parameters


















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| apiName | Required | Refers to the unique name of the field. This should match with the one specified in the path parameter. | String |
| name | Optional | The name of the standard entity field | String |
| type | Optional | Refers to the data type of the field. | String |
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definition. This should match with the one specified in the path parameter | String |

## Example - Request














Copy Code




curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/field/_s_Consent/_c_ConsentAge' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
            "apiName": "_c_ConsentAge",
            "name": "User Consent Age",
            "type": "TEXT",
            "entityDefinitionId": "_s_Consent"
}'





## Example - Response





{
    "data": {
        "id": "_s_Consent__c_consentAge1",
        "apiName": "_c_consentAge1",
        "name": "User Consent Age2",
        "type": "TEXT",
        "entityDefinitionId": "_s_Consent",
        "parentChild": false,
        "multivalued": false,
        "picklistValues": []
    },
    "errors": []
}





[](https://dev.sprinklr.com/update-standard-entity-field)




[Back to top](https://dev.sprinklr.com/update-standard-entity-field)
