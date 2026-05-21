---
title: "Update Standard Entity (Partial)"
slug: update-standard-entity-partial
url: https://dev.sprinklr.com/update-standard-entity-partial
---

# Update Standard Entity (Partial)

#
  PATCH - Update Standard Entity (Partial)

Using this API call, you can partially update standard entity field value for a given entity definition Id and and entity Id. In the request payload, you only need to pass the fields that need to be updated.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/entity/{entitydefinitionId}/{entityId}

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
| entityId | Required | identityId is one of the fields stored in the standard entity definition. If you have create a standard entity for this field, you can use it to fetch the standard entity details. | TEXT |

### Request Parameters














**````**





| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| op | Required | The operation you want to perform on the field within the standard entityExample: SET, UNSET | String |
| fieldName | Required | The name of the standard entity field you want to update | String |
| value | Required | The new value that you want to update for that particular field | Integer/String |

## Example - Request














Copy Code




curl -X PATCH \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/_s_Consent/test008' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
[
    {
        "fieldName": "identityType",
        "value": "phone",
        "op": "SET"
    }
]'





## Example - Response





{
    "data": {
        "identityType": "phone",
        "identityId": "12345678909124",
        "channel": "INSTAGRAM",
        "consent": true,
        "consentSource": "postman2 new",
        "id": "6329611ebe609431f9c44a31",
        "entityId": "test008",
        "name": "6329611ebe609431f9c44a31",
        "type": "_s_Consent",
        "ownerUserId": 600004599,
        "createdTime": "Sep 20, 2022 6:47:25 AM",
        "modifiedTime": "Sep 20, 2022 6:47:25 AM",
        "lastModifiedUserId": 600004599,
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/update-standard-entity-partial)




[Back to top](https://dev.sprinklr.com/update-standard-entity-partial)
