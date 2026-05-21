---
title: "Update Custom Entity Field"
slug: update-custom-entity-field
url: https://dev.sprinklr.com/update-custom-entity-field
---

# Update Custom Entity Field

#   PUT Update Custom Entity Field
 

This API call will help you update an existing custom entity field details.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

**Dev Notes: **Kindly note that the API will reset the values for the field parameters which are not passed in the API request. It is recommended to pass all the existing field parameters even if you want to update only one parameter.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/field/{fieldId}

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
| fieldId | Required | The unique id for the custom entity field. This is the combination of entity definition Id and field's apiName.Example:_c_caller__c_customer_bio | String |

### Request Parameters














****





****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| apiName | Required | Refers to the name you want to give to the field. Please note that the field name starts with prefix _c_.Example: _c_customer_bio | String |
| name | Optional | Refers to the name of the custom entity field | String |
| type | OptionalHowever, it is recommended to pass the data type for the field as this helps identify and plot the field in reporting.Supported Value Types: TEXT, DATE, BOOLEAN, NUMBER, DOUBLE, INTEGER | Refers to the data type of the field | String |
| entityDefinitionId | Required | Refers to the entity Id of the custom entity definition | String |

## Example - Request




 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/field/_c_caller__customer_bio\
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
        "apiName": "_c_customer_bio",
        "name": "Customer Bio",
        "type": "TEXT",
        "entityDefinitionId": "_c_caller"
}'



## Example - Response





   {
    "data": {
        "id": "_c_caller__c_customer_bio",
        "apiName": "_c_customer_bio",
        "name": "Customer Bio",
        "type": "TEXT",
        "entityDefinitionId": "_c_caller",
        "parentChild": false,
        "multivalued": false,
        "picklistValues": []
    },
    "errors": []
}



[](https://dev.sprinklr.com/update-custom-entity-field) 

 

 
[Back to top](https://dev.sprinklr.com/update-custom-entity-field)
