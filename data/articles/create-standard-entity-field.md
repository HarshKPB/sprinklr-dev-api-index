---
title: "Create Standard Entity Field"
slug: create-standard-entity-field
url: https://dev.sprinklr.com/create-standard-entity-field
---

# Create Standard Entity Field

#
  POST - Create Standard Entity Field

Using this API, you can create a standard entity field.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/standard-entity/field/{entityDefinitionId}

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












| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | The standard definition Id for which you want to create a field | String |

### Request Parameters















****







****







****




| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| apiName | Required | The name that you want to set for the fieldExample: _c_ConsentAge | String |
| name | Optional | The name that describes the field's objective.Example: Customer Age | String |
| type | Required | Defines the data type for the fiield.Supported Types:TEXT, DATE, BOOLEAN, NUMBER, DOUBLE, INTEGER | String |
| entityDefinitionId | Required | The standard definition Id for which you want to create a field | String |

### Request - Example














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/standard-entity/field/_s_Consent' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
            "apiName": "_c_ConsentName",
            "name": "User Consent Name",
            "type": "TEXT",
            "entityDefinitionId": "_s_Consent"
}'





### Response - Example





{
    "data": {
        "id": "_s_Consent__c_ConsentName",
        "apiName": "_c_ConsentName",
        "name": "User Consent Name",
        "type": "TEXT",
        "entityDefinitionId": "_s_Consent",
        "parentChild": false,
        "multivalued": false,
        "picklistValues": []
    },
    "errors": []
}





[](https://dev.sprinklr.com/create-standard-entity-field)




[Back to top](https://dev.sprinklr.com/create-standard-entity-field)
