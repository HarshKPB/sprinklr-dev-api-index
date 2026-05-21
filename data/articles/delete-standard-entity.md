---
title: "Delete Standard Entity"
slug: delete-standard-entity
url: https://dev.sprinklr.com/delete-standard-entity
---

# Delete Standard Entity

#
  DELETE - Delete Standard Entity

Using this API, you can delete the standard entity details using the entity definition Id and the entity id.

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters














****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | Refers to the unique identifier for the pre-defined entity definitionSupported entity Definition Ids: _s_Consent, _s_PublishingQueue, _s_ConsentCatalogue, _s_PriceBook, _s_PublisherSettings | string |
| entityId | Required | The unique entity id of the standard field. You can fetch this from create standard entity API response | TEXT |

## Example - Request














Copy Code




curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/entity/_s_Consent/test122’  \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





## Example - Response





{
    "data": true,
    "errors": []
}





### Response Parameters















| Parameters | Description | Type |
| --- | --- | --- |
| data | If true, it implies that the standard entity has been successfully deleted | Boolean |

[](https://dev.sprinklr.com/delete-standard-entity)




[Back to top](https://dev.sprinklr.com/delete-standard-entity)
