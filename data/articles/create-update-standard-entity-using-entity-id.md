---
title: "Create/Update Standard Entity Using Entity Id"
slug: create-update-standard-entity-using-entity-id
url: https://dev.sprinklr.com/create-update-standard-entity-using-entity-id
---

# Create/Update Standard Entity Using Entity Id

#
  POST - Create/Update Standard Entity Using Entity Id

This API helps create/update a standard entity using entity Id. If the entity details passed in the request payload are not found, the API will create a new standard entity using the given details. Else, it will update the standard entity.

## API Endpoint

	 https://api3.sprinklr.com/`{env}`/api/v2/standard-entity/entity/upsert/{entityDefinitionId}/{entityId}

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


















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityId | Required | entityId is of the standard entity. You can fetch the entity id from the create standard entity response.It should match the field in the path parameter | TEXT |
| identityType | Optional | The identity type configured for the standard entity | TEXT |
| identityId | Optional | The unique identity id of the standard entity | TEXT |
| channel | Optional | The channel type set for the standard entity | TEXT |
| type | Required | Refers to the entity definition Id | String |

## Example - Request














Copy Code




curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/upsert/_s_Consent/6321e6684eed2b006dc0abdb' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "identityType": "PHONE",
    "identityId": "12345678913",
    "entityId": "6321e6684eed2b006dc0abdb",
    "channel": "FACEBOOK",
    "type": "_s_Consent"
}'





## Example - Response





   {
    "data": {
        "identityType": "PHONE",
        "identityId": "12345678913",
        "channel": "FACEBOOK",
        "consent": false,
        "id": "6321e6684eed2b006dc0abdb",
        "entityId": "6321e6684eed2b006dc0abdb",
        "name": "6321e6684eed2b006dc0abdb",
        "type": "_s_Consent",
        "ownerUserId": 600004599,
        "createdTime": "Nov 4, 2022 6:50:10 AM",
        "modifiedTime": "Nov 4, 2022 6:50:10 AM",
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/create-update-standard-entity-using-entity-id)




[Back to top](https://dev.sprinklr.com/create-update-standard-entity-using-entity-id)
