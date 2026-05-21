---
title: "Update Custom Entity (Partial)"
slug: update-custom-entity-partial
url: https://dev.sprinklr.com/update-custom-entity-partial
---

# Update Custom Entity (Partial)

#   PATCH Update Custom Entity (Partial)
 

Using this API call, you can partially update entity field value for a given custom entity type. In the request payload, you only need to pass the fields that need to be updated.

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters













****





****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | Refers to the custom entity definition IdExample: _c_caller | String |
| entityId | Required | The unique identifier for the custom entityExample: 624bd7dcc9ca0d00b21f26cd | String |

### Request Parameters














**````**





| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| op | Required | The operation you want to perform on the field within the custom entityExample: SET, UNSET | String |
| fieldName | Required | The name of the custom entity field you want to update | String |
| value | Required | The new value that you want to update for that particular field | Integer/String |

## Example - Request




 Copy Code



curl -X PATCH \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/_c_caller/624bd7dcc9ca0d00b21f2b56' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
        "op": "SET",
        "fieldName": "_c_caller_bio",
        "value": "ABC"
    }



## Example - Response





  {
    "data": {
        "id": "624bd7dcc9ca0d00b21f2b56",
        "entityId": "624bd7dcc9ca0d00b21f2b56",
        "name": "624bd7dcc9ca0d00b21f2b56",
        "type": "_c_caller",
        "values": {
            "_c_credit_score": 30,
            "_c_rating": 10,
            "_c_caller_bio": "ABC"
        },
        "createdTime": "Thu Jul 28 10:12:40 UTC 2022",
        "modifiedTime": "Thu Jul 28 12:46:16 UTC 2022"
    },
    "errors": []
}



	[](https://dev.sprinklr.com/update-custom-entity-partial) 

 

 
[Back to top](https://dev.sprinklr.com/update-custom-entity-partial)
