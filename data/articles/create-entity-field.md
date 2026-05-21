---
title: "Create Entity Field"
slug: create-entity-field
url: https://dev.sprinklr.com/create-entity-field
---

# Create Entity Field

#   POST Create Entity Field

 

This API call helps create the corresponding fields for the created custom entity definition.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/field

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

****``







****







****





        [create entity definition API](https://dev.sprinklr.com/create-entity-definition)

****



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Optional | The name that you want to assign to the field.Syntax: definitionId_apiNameExample: _c_caller__c_customer_bio | String |
| apiName | Required | The name that you want to set for the fieldExample: _c_customer_bio | String |
| name | Optional | The name that describes the field's purpose.Example: Customer Bio | String |
| entityDefinitionId | Required | The entity definition Id you created using Example: _c_caller | String |
| type | Required | Refers to the data type of the fieldSupported Value Types: TEXT, DATE, BOOLEAN, NUMBER, DOUBLE, INTEGER | Integer, String |
| multivalued | Optional | If true, the custom entity field supports multiple values | Boolean |
| picklistValues | Optional | A list of picklist options available for selection. Each object contains details about a picklist value. | Array of Objects |


### picklistValues Parameter Description Table





































| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| label | String | Required | The display name of the picklist option. |
| value | String | Required | The internal value associated with the picklist option. |
| active | Boolean | Required | Indicates whether the picklist value is active (true) or inactive (false). |
| defaultValue | Boolean | Required | Specifies if this value is the default selection (true) or not (false). |

### Request - Example




 Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/field \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
            "apiName": "_c_value",
            "name": "Value",
            "entityDefinitionId": "_c_caller",
            "type": "NUMBER",
            "multivalued": false,
            "picklistValues": [
				{
           "label": "Kitty",
           "value": "cat",
           "active": true,
           "defaultValue": false
        },
        {
           "label": "Doggo",
           "value": "dog",
           "active": true,
           "defaultValue": true
        }
	]
}'

### Response - Example





 {
    "data": {
        "id": "_c_caller__c_value",
        "apiName": "_c_value",
        "name": "Value",
        "type": "NUMBER",
        "entityDefinitionId": "_c_caller",
        "parentChild": false,
        "multivalued": false,
        "picklistValues": [
				{
           "label": "Kitty",
           "value": "cat",
           "active": true,
           "defaultValue": false
        },
        {
           "label": "Doggo",
           "value": "dog",
           "active": true,
           "defaultValue": true
        }
																]
    },
    "errors": []
}



[](https://dev.sprinklr.com/create-entity-field) 

 

 
[Back to top](https://dev.sprinklr.com/create-entity-field)
