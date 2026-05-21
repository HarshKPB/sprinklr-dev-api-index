---
title: "Create Update Lead"
slug: create-update-lead
url: https://dev.sprinklr.com/create-update-lead
---

# Create Update Lead

#
  POST Create Update Lead




This API helps create or update a lead based on the data collected from create/update lead event API. Alternatively, you can also use this API to create a direct lead based on the user/lead information you have at your end.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/dmp/audience-lead

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
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  	 guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters







****[Different Types of Segments](https://www.sprinklr.com/help/articles/different-type-of-segments/different-type-of-segments/648837ff29354c07912fb0f9)

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| segmentIds |  | Required | The unique identifier for the segments where you want to add the leadSegment is a segregated category create to target customers sharing similar behavior or other attributesExample: You have a segment for “Black Friday Sale” and “Cyber Monday Sale.” You can mention the corresponding segmentIds for the two sales and add a lead to both the segments.Related: | String |
| userInfo |  | Required | Object containing the user details. | Object |
|  | customerId | Optional | The unique identifier for the customer. | String |
|  | email | Optional | The email Id of the customer. | String |
|  | phoneNo | Optional | The phone number of the customer. | String |
|  | firstName | Optional | The first name of the customer. | String |
|  | lastName | Optional | The last name of the customer. | String |
|  | fullName | Optional | The full name of the customer. | String |
|  | attributes | Optional | Array defining the user based on key and value parametersRefer to the table below for attributes array definition | Array |
| demographics |  | Optional | Object defining the age and gender of the lead. | Object |
|  | age | Optional | Defines the age of the lead. | Integer |
|  | gender | Optional | Defines the gender of the lead. | String |
| attributes |  | Optional | Defines a set of additional properties for the lead event. Each attribute is represented as a key-value pair that provides specific data points for the event.  Refer to the table below for array definition. | Array |

**Dev Notes: **If the attributes are defined for the user and the lead event, defining the array parameters such as `key`, `value`, and `fieldType` becomes essential.

### Attributes Array Description Table







``````

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| key | Required | Represents the unique identifier for segmenting a customer. The key triggers the customer journey for a lead, and must be distinct within each ‘attributes’ array. Duplicate keys are not allowed within the same array. | String |
| value | Required | The corresponding value for the provided key, representing the specific data for that property. | String |
| fieldType | Required | Specifies the type of custom field associated with the key-value pair. Supported field types: NUMBER, DATETIME, TEXT | String |

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/dmp/audience-lead' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "leadId": "test_campaign_cf646ce1-c07a-4f46-8632-6be3698662ae",
   "segmentIds": ["659d56109a2a1f05a9eede39","659c2885de6aa9004970a36c"],
   "userInfo": {
     "firstName": "yoga",
     "lastName": "nanda",
     "customerId": "+918197849508",
     "anonymousId": "customer-123",
     "phoneNo": "+918197849508",
     "email": "abc@sprinklr.com",
     "phoneDetails": [
       {
         "phoneNo": "+918197849508",
         "type": "ABC"
       },
       {
         "phoneNo": "+919999999999",
         "type": "XYZ"
       }
     ]
   },
   "demographics": {
     "gender": "Female",
     "age": 24
   },
   "attributes": [
     {
       "key": "Name_cult_test_2",
       "value": "cultapi",
       "fieldType": "TEXT"
     },
     {
           "key": "taskRefId",
           "value": "4491d5da-8498-451d-845b-69ad018cb410",
           "fieldType": "TEXT"
      },
      {
           "key": "campaignSubType",
           "value": "TRIAL_TO_PACK_CONVERSION_CF_LIVE_V2",
           "fieldType": "TEXT"
       }
   ]
  }'






## Example - Response





[
    {
        "id": "670523365e5c051912a81196"
    },
    {
        "id": "6704d1e528a0990fd7a9bf97"
    }
]







### Response Parameters







| Parameters | Description | Type |
| --- | --- | --- |
| id | The unique identifier for the lead | String |

**Dev Notes: **You can use the same API to update the lead. While updating a lead, passing the `segmentId` and `customerId` that was used to create a lead is ​​prerequisite.

	[](https://dev.sprinklr.com/create-update-lead)




[Back to top](https://dev.sprinklr.com/create-update-lead)
