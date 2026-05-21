---
title: "Delete Custom Entity Field"
slug: delete-custom-entity-field
url: https://dev.sprinklr.com/delete-custom-entity-field
---

# Delete Custom Entity Field

#   DELETE Delete Custom Entity Field
 

This API helps delete a field existing within a custom entity definition.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

**Dev Notes: **Kindly note that the API will reset the values for the field parameters which are not passed in the API request. It is recommended to pass all the existing field parameters even if you want to update only one parameter.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/field/{id}

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

## Path Parameter













``




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | definitionId_apiNameExample: _c_caller__c_customer_bio | String |

## Example - Request




 Copy Code



curl -X DELETE \
  'https://api2.sprinklr.com/{env}/api/v2/custom-entity/field/{id}' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''



## Example - Response





 {
    "data": true,
    "errors": []
}



[](https://dev.sprinklr.com/delete-custom-entity-field) 

 

 
[Back to top](https://dev.sprinklr.com/delete-custom-entity-field)
