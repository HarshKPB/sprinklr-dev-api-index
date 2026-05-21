---
title: "Create Update Lead Event"
slug: create-update-lead-event
url: https://dev.sprinklr.com/create-update-lead-event
---

# Create Update Lead Event

#
  POST Create Update Lead Event



A lead event is an action that a lead/customer performs along the customer journey. For example, watching a demo or subscribing for the newsletter could be one lead event. Similarly, adding the product to cart or asking for a free consultation could be another. This API call helps create and update such lead events.

## API Endpoint

https://api3.sprinklr.com{env}api/v2/dmp/lead/{sourceId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sourceId | Required | The unique identifier for the lead’s source | String |

### Request Parameters


















































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| eventId |  | Required | The unique Id of the lead eventIf the lead already exists for the given eventId, the lead will get updated based on the given payload | String |
| eventType |  | Optional | Describes the type of lead eventeventType is use case specific | String |
| user |  | Required | Object defining the customer/lead details | Object |
|  | customerId | Required | The unique Id for the customer | String |
|  | anonymousId | Optional | The unique identifier for a customer who has not registered as a user. I.e., who has not logged in and is a guest userWhen a customer signs in, this anonymousId helps identify that the lead created (before signing in) was related to which customer | String |
|  | attributes | Optional | Array defining the customer/lead attributes based on key and value parametersRefer to the table below for array definition | Array |
| sourceInfo |  | Optional | Array defining the lead sourceRefer to the table below for array definition | Array |
| demographics |  | Optional | Object defining the age and gender of the lead | Object |
|  | age | Optional | Defines the age of the lead | Integer |
|  | gender | Optional | Defines the gender of the lead | String |
| attributes |  | Optional | Defines the additional properties of the lead event based on key and value parametersRefer to the table below for array definition | Array |

**Dev Notes: **If the attributes are defined for the user and the lead event, defining the array parameters such as `key`, `value`, and `fieldType` becomes essential.

### Attributes Array Description Table


























``````



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| key | Required | A customer is segmented based on this key valueThe key helps trigger the customer journey for the lead | String |
| value | Required | The value corresponding to the given key | String |
| fieldType | Required | The custom field type.Supported field types: NUMBER, DATETIME, TEXT | String |

### sourceInfo Array Description Table























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sourceId | Optional | The unique identifier for the lead source | String |
| sourceName | Optional | The name of the source from where the lead is coming | String |

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/dmp/lead/test1' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "eventId": "LeadEvent_Test",
   "eventType": "SUBSCRIBER",
   "user": {
       "customerId": "dsv_30thMay_04",
       "anonymousId": "dsv_30thMay_04",
       "attributes": [
           {
               "key": "SN_TYPE",
               "value": "SPRINKLR_VOICE",
               "fieldType": "TEXT"
           }
       ]
   },
"sourceInfos": [
           {
               "sourceId": "test1",
               "sourceName": "fileName1"
           }
       ],
   "demographics": {
       "gender": "Other/Unspecified"
   },
   "attributes": [
       {
           "key": "FUNCTION",
           "value": "Update",
           "fieldType": "TEXT"
       }
   ]
}'






## Example - Response





 {
    "data": "Lead Created Successfully for eventIds: LeadEvent_Test",
    "errors": []
}







**Dev Notes: **You can use the same API to update the lead event. While updating a lead event, passing the `eventId` that was used to create a lead event is ​​prerequisite.

	[](https://dev.sprinklr.com/create-update-lead-event)






[Back to top](https://dev.sprinklr.com/create-update-lead-event)
