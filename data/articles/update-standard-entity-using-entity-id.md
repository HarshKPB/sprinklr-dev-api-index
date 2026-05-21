---
title: "Update Standard Entity Using Entity Id"
slug: update-standard-entity-using-entity-id
url: https://dev.sprinklr.com/update-standard-entity-using-entity-id
---

# Update Standard Entity Using Entity Id

#
  PUT - Update Standard Entity Using Entity Id

Using this API, you can update the details for the standard entity field.

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



[create standard entity API](https://dev.sprinklr.com/create-standard-entity)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionSupported entity Definition Ids: _s_Consent, _s_PublishingQueue, _s_ConsentCatalogue, _s_PriceBook, _s_PublisherSettings | string |
| entityId | Required | entityId is one of the primary fields defined under standard entities.You can fetch this from the  response. | TEXT |

### Request Parameters
















**




**

**

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the entity definition id. | String |
| entityId | Required | The unique identity Id of the custom entity. You can either configure the entityId to some intuitive name using create standard entity API. If not configured, you can fetch the system-generated entity id from the create standard entity response. | TEXT |
| identityType (Primary Field) | Optional | The identity type value you want to update the standard entity to | TEXT |
| identityId (Primary Field) | Optional | The unique identity id of the standard entity | TEXT |
| channel (Primary Field) | Optional | The channel type you want to update the standard entity to | TEXT |

**Dev Notes: **

- The standard entity fields such as identityType, identityId, and channel are primary fields.
- It is mandatory to define one of the primary fields to update standard entity.
- The primary fields defined in the update standard entity call should match to the ones defined in the create standard entity call

## Example - Request














Copy Code




curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/field/_s_Consent/test122' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "identityType": "PHONEa",
    "identityId": "1234567895",
    "channel": "FACEBOOK",
    "type": "_s_Consent",
    "entityId": "test122"
}'





## Example - Response





{
    "data": {
        "identityType": "PHONEa",
        "identityId": "1234567895",
        "channel": "FACEBOOK",
        "consent": true,
        "consentSource": "postman",
        "id": "6364b6cfde0320132827911a",
        "entityId": "test122",
        "name": "6364b6cfde0320132827911a",
        "type": "_s_Consent",
        "ownerUserId": 600004599,
        "createdTime": "Nov 9, 2022 2:16:35 PM",
        "modifiedTime": "Nov 9, 2022 2:16:35 PM",
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/update-standard-entity-using-entity-id)




[Back to top](https://dev.sprinklr.com/update-standard-entity-using-entity-id)
