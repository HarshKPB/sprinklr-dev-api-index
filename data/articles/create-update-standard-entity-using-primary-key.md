---
title: "Create/Update Standard Entity Using Primary Key"
slug: create-update-standard-entity-using-primary-key
url: https://dev.sprinklr.com/create-update-standard-entity-using-primary-key
---

# Create/Update Standard Entity Using Primary Key

#
  POST - Create/Update Standard Entity Using Primary Key

This API helps create/update a standard entity using primary key. If the entity details passed in the request payload are not found, the API will create a new standard entity using the given details. Else, it will update the standard entity.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/upsertByPrimaryKey/{entityDefinitionId}

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
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionExample: _s_Consent | string |

### Request Parameters















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| identityType | Optional | The identity type configured for the standard entity | TEXT |
| identityId | Optional | The unique identity id of the standard entity | TEXT |
| channel | Optional | The channel type set for the standard entity | TEXT |
| type | Required | Refers to the entity definition Id | String |

**Dev Notes: **

- The standard entity fields such as identityType, identityId, and channel are primary fields.
- If none of the primary fields are passed in the request, a basic entity will get created with none of the primary keys.

## Example - Request














Copy Code




curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/upsertByPrimaryKey/_s_Consent' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
	"identityType" : "PHONE",
	"identityId" : "12345678913",
	"channel" : "FACEBOOK",
	"type" : "_s_Consent"
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
        "createdTime": "Nov 14, 2022 8:16:29 AM",
        "modifiedTime": "Nov 14, 2022 8:16:29 AM",
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/create-update-standard-entity-using-primary-key)




[Back to top](https://dev.sprinklr.com/create-update-standard-entity-using-primary-key)
