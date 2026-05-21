---
title: "Fetch Standard Entity Using Primary Key Prefix"
slug: fetch-standard-entity-using-primary-key-prefix
url: https://dev.sprinklr.com/fetch-standard-entity-using-primary-key-prefix
---

# Fetch Standard Entity Using Primary Key Prefix

#
  GET - Fetch Standard Entity Using Primary Key Prefix

Using this API, you can fetch the standard entity using at least one of the primary key parameters, i.e., `identityType`, `identityId`, and `channel`.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/byPrimaryKeyPrefix/{entityDefinitionId}

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














****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionSupported entity Definition Ids: _s_Consent, _s_PublishingQueue, _s_ConsentCatalogue, _s_PriceBook, _s_PublisherSettings | string |

### Query Parameters
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| identityType | Optional | The identity type configured for the standard entity | TEXT |
| identityId | Optional | The unique identity id of the standard entity | TEXT |
| channel | Optional | The channel type set for the standard entity | TEXT |

**Dev Notes: **It is mandatory to pass at least one of the query parameters, i.e., `identityType`, `identityId`, or `channel`to fetch successful response.

## Example - Request














Copy Code




curl -X GET \
  'https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/byPrimaryKeyPrefix/_s_Consent?identityType=PHONE&identityId=1234567895' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'





### Example - Response





{
    "data": [
        {
            "identityType": "PHONE",
            "identityId": "1234567895",
            "channel": "FACEBOOK",
            "consent": true,
            "consentSource": "postman",
            "id": "632026bfb14f2d6a2a0960ac",
            "entityId": "test123",
            "name": "632026bfb14f2d6a2a0960ac",
            "type": "_s_Consent",
            "ownerUserId": 600004599,
            "createdTime": "Nov 4, 2022 11:44:33 AM",
            "modifiedTime": "Nov 4, 2022 11:44:33 AM",
            "lastModifiedUserId": 600004599,
            "deleted": false,
            "canEdit": false
        }
    ],
    "errors": []
}





[](https://dev.sprinklr.com/fetch-standard-entity-using-primary-key-prefix)




[Back to top](https://dev.sprinklr.com/fetch-standard-entity-using-primary-key-prefix)
