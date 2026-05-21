---
title: "Fetch Standard Entity Using Entity Id"
slug: fetch-standard-entity-using-entity-id
url: https://dev.sprinklr.com/fetch-standard-entity-using-entity-id
---

# Fetch Standard Entity Using Entity Id

#
  GET - Fetch Standard Entity Using Entity Id

Using this API, you can fetch the standard entity details using the entity Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/entity/{entityDefinitionId}/{entityId}

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



[create standard entity API](https://dev.sprinklr.com/create-standard-entity)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionSupported entity Definition Ids: _s_Consent, _s_PublishingQueue, _s_ConsentCatalogue, _s_PriceBook, _s_PublisherSettings | String |
| entityId | Required | entityId is one of the primary fields defined under standard entities.You can fetch this from the  response. | TEXT |

### Example - Request














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/_s_Consent/test122’ /
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''





### Example - Response





{
    "data": {
        "identityType": "PHONE",
        "identityId": "1234567894",
        "channel": "FACEBOOK",
        "consent": true,
        "consentSource": "postman",
        "id": "632026b696181f6d01ac487e",
        "entityId": "test122",
        "name": "632026b696181f6d01ac487e",
        "type": "_s_Consent",
        "ownerUserId": 600004599,
        "createdTime": "Sep 13, 2022 6:44:06 AM",
        "modifiedTime": "Sep 13, 2022 6:44:06 AM",
        "lastModifiedUserId": 600004599,
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/fetch-standard-entity-using-entity-id)




[Back to top](https://dev.sprinklr.com/fetch-standard-entity-using-entity-id)
