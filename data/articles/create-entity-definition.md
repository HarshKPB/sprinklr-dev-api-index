---
title: "Create Entity Definition"
slug: create-entity-definition
url: https://dev.sprinklr.com/create-entity-definition
---

# Create Entity Definition

#   POST Create Entity Definition

 

Using this API call, you will be able to create a custom entity definition.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/custom-entity/definition

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

### Request Parameters













****





| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | The unique id of the custom entity definitionExample: _c_caller | String |
| name | Optional | The name of the custom entity definition | String |
| puralName | Optional | The plural form of the custom definition name | String |
| description | Optional | The description of the custom entity definition | String |

**Dev Note: **The entity definition Id must have `**_c_**` prefix (underscore "c" underscore)

## Example - Request




 Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/definition \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
  "id" : "_c_caller",
  "name" : "Caller ",
  "pluralName" : "Callers",
  "description" : "Describes Caller Data"
}'



## Example - Response





  {
    "data": {
        "id": "_c_caller",
        "name": "Caller ",
        "pluralName": "Callers",
        "description": "Describes Caller Data",
        "createdTime": 1659005929667,
        "modifiedTime": 1659005929667
    },
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

[](https://dev.sprinklr.com/create-entity-definition) 

 

 
[Back to top](https://dev.sprinklr.com/create-entity-definition)
