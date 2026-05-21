---
title: "Create Standard Entity"
slug: create-standard-entity
url: https://dev.sprinklr.com/create-standard-entity
---

# Create Standard Entity

#
  POST - Create Standard Entity

Using this API, you can create a standard entity field, i.e., you can store values within the defined standard entity fields.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/entity/{entityDefinitionId}

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

### Path Parameters












| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | The standard definition Id for which you want to create an entity | String |

### Request Parameters
















****

-
-

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the entity definition Id | String |
| identityType | Optional | User-generated reference for the type of value you want to store for the standard entity. | TEXT |
| identityId | Optional | The unique value corresponding to the identity type. | TEXT |
| channel | Optional | The channel type set for the standard entity | TEXT |
| entityId | Optional | The user-generated reference for the standard entity.Note:Entity Id needs to be unique every time a new standard entity is created.If not configured in the API request, entity Id defaults to the standard entity field Id. | String |

**Dev Notes: **

- The standard entity fields such as identityType, identityId, and channel are primary fields.
- It is mandatory to define one of the primary fields to create standard entity.
- The values set for identityId should be unique every time you create a standard entity for a similar channel and identityType. Else, you'll receive 409 Conflict error.

## Example - Request














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/_s_Consent' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "identityType" : "PHONE",
    "identityId" : "1234567866",
    "channel" : "FACEBOOK",
    "type": "_s_Consent",
    "entityId": "test122"
}'





## Example - Response





 {
    "data": {
        "identityType": "PHONE",
        "identityId": "1234567866",
        "channel": "FACEBOOK",
        "consent": true,
        "id": "6364f425be54f726cc33605a",
        "entityId": "test122",
        "name": "6364f425be54f726cc33605a",
        "type": "_s_Consent",
        "ownerUserId": 600004599,
        "createdTime": "Nov 4, 2022 11:14:45 AM",
        "modifiedTime": "Nov 4, 2022 11:14:45 AM",
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/create-standard-entity)




[Back to top](https://dev.sprinklr.com/create-standard-entity)
