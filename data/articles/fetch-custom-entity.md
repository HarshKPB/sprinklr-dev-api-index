---
title: "Fetch Custom Entity"
slug: fetch-custom-entity
url: https://dev.sprinklr.com/fetch-custom-entity
---

# Fetch Custom Entity

#   GET Fetch Custom Entity
 

Using this API, you can fetch the custom entity details using the entity type and the entity id.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/entity/{entityType}/{entityId}

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













[custom entity definition](https://dev.sprinklr.com/create-entity-definition)

****



[create custom entity API](https://dev.sprinklr.com/create-custom-entity)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | The type of entity, i.e., the unique id of the  Example: _c_caller | string |
| entityId | Required | The unique identifier for the created custom entityThis is the id you receive in response of the | String |

## Example - Request




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity/_c_caller/624bd7dcc9ca0d00b21f2b56’  \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'



## Example - Response





{
   "data": {
       "id": "63086035fc434903a2ca6868",
       "entityId": "Test",
       "name": "Test",
       "type": "_c_caller",
       "values": {
           "_c_credit_score": 25,
           "_c_rating": 5,
           "_c_customer_bio": "Works in corporate"
       },
       "createdTime": "Fri Aug 26 05:55:01 UTC 2022",
       "modifiedTime": "Fri Aug 26 05:55:01 UTC 2022"
   },
   "errors": []
}



### Response Parameters















































| Parameters | Description | Type |
| --- | --- | --- |
| id | The unique id for the entity created | String |
| entityId | Refers to the unique name configured for the entity | String |
| name | The name of the entity | String |
| type | Refers to the custom entity definition Id | String |
| values | The entity field and value pair configured in the request body {"entityField"= value} | Object |
| createdTime | The time at which the custom entity was created | String |
| modifiedTime | The time at which the custom entity was last modified | String |

[](https://dev.sprinklr.com/fetch-custom-entity) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-custom-entity)
