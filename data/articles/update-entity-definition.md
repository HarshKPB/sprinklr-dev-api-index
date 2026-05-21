---
title: "Update Entity Definition"
slug: update-entity-definition
url: https://dev.sprinklr.com/update-entity-definition
---

# Update Entity Definition

#   PUT Update Entity Definition
 

This API call will help you update an existing custom entity definition using the entity definition Id.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/definition/{entityDefinitionId}

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
| entityDefinitionId | Required | The unique id for the entity definition.Example:_c_caller | String |

### Request Parameters













****





| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Optional | Refers to the entity definition IdExample: _c_caller | String |
| name | Optional | The name of the custom entity definition | String |
| puralName | Optional | The plural form of the custom definition name | String |
| description | Optional | The description of the custom entity definition | String |
| script | Required | The script for updating the custom entity definition | String |
| scriptVersion | Optional | The version of the updated script | String |

## Example - Request




 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/definition/_c_caller\
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
    "id": "_c_caller",
    "name": "Caller",
    "pluralName": "Callers",
    "description": "Describes Caller Data",
    "script": "{Update script}",
    "scriptVersion": "v1.3"
}



## Example - Response





    {
    "data": {
        "id": "_c_caller",
        "name": "Caller",
        "pluralName": "Callers",
        "description": "Caller Data",
        "permissionEnabled": false,
        "script": "{updated Script}",
        "scriptVersion": "v1.3",
        "createdTime": 1659013303517,
        "modifiedTime": 1659013303517
    },
    "errors": []
}



[](https://dev.sprinklr.com/update-entity-definition) 

 

 
[Back to top](https://dev.sprinklr.com/update-entity-definition)
