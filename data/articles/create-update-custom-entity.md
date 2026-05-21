---
title: "Create (Update) Custom Entity"
slug: create-update-custom-entity
url: https://dev.sprinklr.com/create-update-custom-entity
---

# Create (Update) Custom Entity

#   POST Create (Update) Custom Entity
 

This API helps create/update a custom entity. If the entity details passed in the request payload are not found, the API will create a new entity using the given details. Else, it will update the custom entity.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/entity/upsert

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

### Request Parameters














****





















****

****




| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | The type of custom entity, i.e., the custom entity definition IdExample: _c_caller | String |
| entityId | Required | The unique identifier for the custom entity. If you pass an existing entityId, the API call will update the custom entity. If you pass a new entityId, the API call will create a new custom entity. | String |
| name | Required | Refers to the name of the custom entity.If you pass an existing name, the API call will update the custom entity.If you pass a new name, the API call will create a new custom entity | String |
| values | Optional | Refers to custom entity field and value pair. Used for updating the values for the given custom entity field.Example:{_c_field1": "value1"}Note: You cannot create a new custom entity field using this API. You can only update the values for the existing custom entity fields that are pre-defined for the given custom entity type. | Object |

## Example - Request




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity/upsert' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "type": "_c_caller",
   "entityId": "Test",
   "name": "Test1",
   "values": {
       "_c_credit_score": 9
   }
}’



## Example - Response





    {
   "data": {
       "id": "63086dd8132d644dda72c65e",
       "entityId": "Test",
       "name": "Test1",
       "type": "_c_caller",
       "values": {
           "_c_credit_score": 9
       },
       "createdTime": "Thu Sep 01 07:22:25 UTC 2022",
       "modifiedTime": "Thu Sep 01 07:22:25 UTC 2022"
   },
   "errors": []
}



### Response Parameters















































| Parameters | Description | Type |
| --- | --- | --- |
| id | The reference id for the created/updated custom entity | String |
| entityId | Refers to the unique identifier for the custom entity | String |
| name | Refers to the name for the custom entity | String |
| type | Refers to the custom entity definition Id | String |
| values | Refers to custom entity field and value pair{"entityField"= value} | Object |
| createdTime | The time at which the custom entity was created or updated | String |
| modifiedTime | The time at which the custom entity was last modified | String |

**Dev Notes: **To fetch the details for the created or updated custom entity, refer to [fetch custom entity API](https://dev.sprinklr.com/fetch-custom-entity) documentation.

[](https://dev.sprinklr.com/create-update-custom-entity) 

 

 
[Back to top](https://dev.sprinklr.com/create-update-custom-entity)
