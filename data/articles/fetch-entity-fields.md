---
title: "Fetch Entity Fields"
slug: fetch-entity-fields
url: https://dev.sprinklr.com/fetch-entity-fields
---

# Fetch Entity Fields

#   GET Fetch Entity Fields
 

This API call helps in fetching all the fields for the given entity definition Id.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/fields/{entityDefinitionId}

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
| entityDefinitionId | Required | Refers to the custom entity definition IdExample: _c_caller | string |

## Example - Request





 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/fields/_c_caller ' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d ''



## Example - Response





 {
    "data": [
{
            "id": "_c_caller__c_customer_bio",
            "apiName": "_c_customer_bio",
            "name": "Customer Bio",
            "type": "TEXT",
            "entityDefinitionId": "_c_caller",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        },
        {
            "id": "_c_caller__c_credit_score",
            "apiName": "_c_credit_score",
            "name": "Credit Score",
            "type": "INTEGER",
            "entityDefinitionId": "_c_caller",
            "parentChild": false,
            "multivalued": false,
            "picklistValues": []
        }
],
    "errors": []
}



[](https://dev.sprinklr.com/fetch-entity-fields) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-entity-fields)
