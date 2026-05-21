---
title: "Fetch All Entity Definitions"
slug: fetch-all-entity-definitions
url: https://dev.sprinklr.com/fetch-all-entity-definitions
---

# Fetch All Entity Definitions

#   GET Fetch All Entity Definitions
 

This API call helps in fetching all the existing custom entity definitions present in the partner environment.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/definitions

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal. |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide. |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body. |
| Accept | application/json | Determines the acceptable response type from the server. |

### Path Parameters














****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | The entity definition id you configured while creating the entity definition.Example: _c_caller | string |

## Example - Request





 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/definitions' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''



## Example - Response





{
    "data": [
        {
            "id": "_c_Test1",
            "name": "Test1 Data",
            "description": "For testing custom entity",
            "permissionEnabled": false,
            "createdTime": 1588426469795,
            "modifiedTime": 1588426469795
        },
        {
            "id": "_c_Test2",
            "name": "Test2 Data",
            "pluralName": "For testing custom entity",
            "description": "CSM Opportunity",
            "permissionEnabled": false,
            "createdTime": 1601101335809,
            "modifiedTime": 1601101335809
        },
        {
            "id": "_c_Test3",
            "name": "Test3 Data",
            "pluralName": "For testing custom entity",
            "description": "Events created on Products.",
            "permissionEnabled": false,
            "createdTime": 1609089717542,
            "modifiedTime": 1609089717542
        },
        {
            "id": "_c_Test4",
            "name": "Test4 Data",
            "pluralName": "For testing custom entity",
            "description": "Describes Cart Abandoned Event",
            "permissionEnabled": false,
            "createdTime": 1610980267381,
            "modifiedTime": 1610980267381
        }
    ],
    "errors": []
}



### Response Parameters




























| Parameters | Description | Type |
| --- | --- | --- |
| id | The unique identifier for the custom entity definition | String |
| name | The name of the custom entity definition | String |
| pluralName | The plural form of the custom entity definition name | String |
| description | The description of the custom entity definition | String |
| createdTime | The time at which the custom entity definition was created | String |
| modifiedTime | The time at which the custom entity definition was last modified | String |

[](https://dev.sprinklr.com/fetch-all-entity-definitions) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-all-entity-definitions)
