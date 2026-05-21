---
title: "Delete Custom Entity"
slug: delete-custom-entity
url: https://dev.sprinklr.com/delete-custom-entity
---

# Delete Custom Entity

#   DELETE Delete Custom Entity
 

Using this API, you can delete the created custom entity details using the entity type and the entity id.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/entity/{entityDefinitionId}/{entityId}

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













[custom entity definition](https://dev.sprinklr.com/create-entity-definition)

****



[create custom entity API](https://dev.sprinklr.com/create-custom-entity)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | The type of entity, i.e., the unique id of the  Example: _c_caller | string |
| entityId | Required | The unique identifier for the created custom entityThis is the id you receive in response of the | String |

## Example - Request




 Copy Code


curl -X DELETE \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity/_c_caller/624bd7dcc9ca0d00b21f2b56  \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



## Example - Response




{
    "data": true,
    "errors": []
}



### Response Parameters















| Parameters | Description | Type |
| --- | --- | --- |
| data | If true, it implies that the custom entity has been successfully deleted | Boolean |


[](https://dev.sprinklr.com/delete-custom-entity) 

 

 
[Back to top](https://dev.sprinklr.com/delete-custom-entity)
