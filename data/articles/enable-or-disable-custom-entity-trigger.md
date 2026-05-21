---
title: "Enable or Disable Custom Entity Trigger"
slug: enable-or-disable-custom-entity-trigger
url: https://dev.sprinklr.com/enable-or-disable-custom-entity-trigger
---

# Enable or Disable Custom Entity Trigger

#   POST Enable or Disable Custom Entity Trigger
 

Using this API, you can enable or disable the custom entity trigger for the given trigger id.

The documentation covers APIs for both enabling and disabling custom entity triggers:

- [Enable Custom Entity Trigger](https://dev.sprinklr.com/enable-or-disable-custom-entity-trigger/#Enable)

- [Disable Custom Entity Trigger](https://dev.sprinklr.com/enable-or-disable-custom-entity-trigger/#Disable)

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

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
| Content-Type | multipart/form-data; boundary=<calculated when request is sent> | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

##  1. Enable Custom Entity Trigger

Using this API, you can enable the custom entity trigger.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/trigger/{id}/enable

### Path Parameters















[create custom entity trigger](https://dev.sprinklr.com/create-custom-entity-trigger)




| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| id | Required | The unique reference id for the trigger you want to enableYou can fetch this id from API's response | String |

### Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/trigger/6308aaa0fc434903a2cabc0d/enable’ \
  -H 'Authorization: Bearer {{token}}' \
  -H 'key: {{apikey}}' \
  -H 'Content-Type: application/json'



### Example - Response



{
 {
    "data": true,
    "errors": []
}



### Response Parameters
















| Parameter | Description | Type |
| --- | --- | --- |
| data | If true, it implies that the trigger has been successfully disabled | Boolean |

##  2. Disable Custom Entity Trigger

Using this API, you can disable the custom entity trigger.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/trigger/{id}/disable

### Path Parameters















[create custom entity trigger](https://dev.sprinklr.com/create-custom-entity-trigger)




| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| id | Required | The unique reference id for the trigger you want to disableYou can fetch this id from API's response | String |

### Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/trigger/6308aaa0fc434903a2cabc0d/disable’ \
  -H 'Authorization: Bearer {token}' \
  -H 'key: {apikey}' \
  -H 'Content-Type: application/json'



### Example - Response



{
 {
    "data": true,
    "errors": []
}



### Response Parameters
















| Parameter | Description | Type |
| --- | --- | --- |
| data | If true, it implies that the trigger has been successfully disabled | Boolean |


[](https://dev.sprinklr.com/enable-or-disable-custom-entity-trigger) 

 

 
[Back to top](https://dev.sprinklr.com/enable-or-disable-custom-entity-trigger)
