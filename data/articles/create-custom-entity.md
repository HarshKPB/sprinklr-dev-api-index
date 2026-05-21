---
title: "Create Custom Entity"
slug: create-custom-entity
url: https://dev.sprinklr.com/create-custom-entity
---

# Create Custom Entity

#   POST Create Custom Entity
 

This API helps create the values for the different fields of the custom entity i.e., it helps store the data that is being collected for different custom entity fields.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/entity

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
































| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Optional | The name of the entityIf the name of the entity is not passed, its default value will be same as that of "Id" in the response | String |
| entityId | OptionalHowever, it is recommended to pass entityId.If not passed, it defaults to the id in the response. | Configured from client-side and needs to be unique for every entity. The entity Id is a unique reference for the entity that helps identifying the created entity | String |
| type | Required | Refers to the custom definition IdExample: _c_caller | String |
| values | Required | The object containing the entity name and value pairs | Object |

## Example - Request




 Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
            "name": "Test",
            "type": "_c_caller",
            "values": {
       		"_c_credit_score": 25,
       		"_c_rating": 5,
       		"_c_customer_bio": "Works in corporate"
           }
}'



## Example - Response




    {
   "data": {
       "id": "624bd7dcc9ca0d00b21f2b56",
       "entityId": "Test",
       "name": "Test",
       "type": "_c_caller",
       "values": {
           "_c_credit_score": 25,
           "_c_rating": 5,
           "_c_customer_bio": "Works in corporate"
       },
       "createdTime": "Tue Apr 05 05:47:08 UTC 2022",
       "modifiedTime": "Tue Apr 05 05:47:08 UTC 2022"
   },
   "errors": []
}



### Response Parameters















































| Parameters | Description | Type |
| --- | --- | --- |
| id | The unique id for the entity created | String |
| entityId | Refers to the unique name set for the entity | String |
| name | The name of the entity | String |
| type | Refers to the custom entity definition Id | String |
| values | The entity field and value pair configured in the request body {"entityField"= value} | Object |
| createdTime | The time at which the custom entity was created | String |
| modifiedTime | The time at which the custom entity was last modified | String |

[](https://dev.sprinklr.com/create-custom-entity) 

 

 
[Back to top](https://dev.sprinklr.com/create-custom-entity)
