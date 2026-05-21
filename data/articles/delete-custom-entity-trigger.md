---
title: "Delete Custom Entity Trigger"
slug: delete-custom-entity-trigger
url: https://dev.sprinklr.com/delete-custom-entity-trigger
---

# Delete Custom Entity Trigger

#   DELETE Delete Custom Entity Trigger
 

Using this API, you can delete the trigger configuration of a custom entity for the given trigger id.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/trigger/{id}

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














[create custom entity trigger](https://dev.sprinklr.com/create-custom-entity-trigger)



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | The unique reference id for the trigger you want to deleteYou can fetch this id from API's response | string |

## Example - Request




 Copy Code



curl -X DELETE \
  'https://api2.sprinklr.com/{env}/api/v2/custom-entity/trigger/6308aaa0fc434903a2cabc0d’  \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'



## Example - Response




{
    "data": true,
    "errors": []
}



### Response Parameters















| Parameters | Description | Type |
| --- | --- | --- |
| data | If true, it implies that the custom entity trigger has been successfully deleted | Boolean |


[](https://dev.sprinklr.com/delete-custom-entity-trigger) 

 

 
[Back to top](https://dev.sprinklr.com/delete-custom-entity-trigger)
