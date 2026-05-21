---
title: "Fetch Entity Definition"
slug: fetch-entity-definition
url: https://dev.sprinklr.com/fetch-entity-definition
---

# Fetch Entity Definition

#   GET Fetch Entity Definition

 

This API call helps in fetching the configured definition for the given entity Id.

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal. |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide. |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body. |
| Accept | application/json | Determines the acceptable response type from the server. |

### Path Parameters














****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | The entity definition id you configured while creating the entity definition.Example: _c_caller | string |




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/definition/_c_caller' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''



## Example - Response





 {
    "data": {
        "id": "_c_caller",
        "name": "Caller",
        "description": "For testing custom entity",
        "permissionEnabled": false,
        "createdTime": 1588426469795,
        "modifiedTime": 1588426469795
    },
    "errors": []
}



[](https://dev.sprinklr.com/fetch-entity-definition) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-entity-definition)
