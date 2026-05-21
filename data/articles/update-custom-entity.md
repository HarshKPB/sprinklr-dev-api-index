---
title: "Update Custom Entity"
slug: update-custom-entity
url: https://dev.sprinklr.com/update-custom-entity
---

# Update Custom Entity

#   PUT Update Custom Entity
 

This API helps update the values for the different fields of the custom entity i.e., it helps update the stored data for different custom entity fields. In the request payload, you can pass all the fields that need to be updated and assign values to them (all at once).

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/entity/{entityId}

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












[create custom entity API](https://dev.sprinklr.com/create-custom-entity)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityId | Required | The unique id you received in the  response | String |

### Request Parameters











| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the custom entity definition Id | String |
| values | Required | Object containing custom entity field along with its new/updated value | Object |

## Example - Request




 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity/624bd7dcc9ca0d00b21f2c67 \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
    "type": "_c_caller",
   "values": {
        "_c_credit_score": 30,
        "_c_rating": 10,
        "_c_customer_bio": "Works in corporate XYZ"
    }
}'



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
            "_c_customer_bio": "Works in corporate XYZ"
        },
        "createdTime": "Thu Jul 28 10:12:40 UTC 2022",
        "modifiedTime": "Thu Jul 28 10:12:40 UTC 2022"
    },
    "errors": []
}



### Response Parameters














































| Parameters | Description | Type |
| --- | --- | --- |
| id | The id for the custom entity passed in the request endpoint | String |
| entityId | The Id of the newly created entity | String |
| name | The name of the entity | String |
| type | Refers to the custom entity definition Id | String |
| values | The name and corresponding value pair configured in the request body | Object |
| createdTime | The time at which the custom entity was created | String |
| modifiedTime | The time at which the custom entity was last modified | String |

[](https://dev.sprinklr.com/update-custom-entity) 

 

 
[Back to top](https://dev.sprinklr.com/update-custom-entity)
