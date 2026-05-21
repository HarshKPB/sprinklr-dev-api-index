---
title: "Create Update Bulk Leads"
slug: create-update-bulk-leads
url: https://dev.sprinklr.com/create-update-bulk-leads
---

# Create Update Bulk Leads

#
  POST Create Update Bulk Leads




This API helps create or update bulk leads based on the data collected from create/update lead event API. Alternatively, you can also use this API to create direct leads based on the user/lead information you have at your end.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/dmp/audience-lead/{partnerName}/bulk

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











| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| partnerName | Required | Refers to the partner name  for which the lead is being generated | String |

### Request Parameters























****[Different Types of Segments](https://www.sprinklr.com/help/articles/different-type-of-segments/different-type-of-segments/648837ff29354c07912fb0f9)



























































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| leadId |  | Required | Refers to the unique identifier for the audience lead.This is a client generated field, which helps identify and distinguish the lead later on | String |
| segmentIds |  | Optional | The unique identifier for the segments where you want to add the lead.A segment is a categorized group created to target customers sharing similar behaviors or attributes. For example, you might have segments for “Black Friday Sale” or “Cyber Monday Sale.” By mentioning the corresponding segment IDs, you can add a lead to one or more of these segments.This parameter is optional. If not specified, lead attributes can be used to filter target customers while creating the Voice Campaign. However, if specified, the lead will be added to the segment regardless of segment conditions. The main use case for specifying segment IDs is to enable almost real-time dialing of leads. For general use cases, it is recommended not to specify the segment ID.Related: | String |
| userInfo |  | Required | Object containing the user details | Object |
|  | customerId | Optional | The unique identifier for the customer | String |
|  | email | Optional | The email Id of the customer | String |
|  | phoneNo | Optional | The phone number of the customer | String |
|  | firstName | Optional | The first name of the customer | String |
|  | lastName | Optional | The last name of the customer | String |
|  | fullName | Optional | The full name of the customer | String |
|  | phoneDetails | Optional | A collection of phone numbers associated with a lead, allowing multiple entries for different contact types. | Array of Objects |
| demographics |  | Optional | Object defining the age and gender of the lead | Object |
|  | age | Optional | Defines the age of the lead | Integer |
|  | gender | Optional | Defines the gender of the lead | String |
| attributes |  | Optional | Defines the additional properties of the lead event based on key and value parametersRefer to the table below for array definition | Array |

**Dev Notes: **If the attributes are defined for the user and the lead event, defining the array parameters such as `key`, `value`, and `fieldType` becomes essential.


### phoneDetails Array Description Table



























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| phoneNo | Required | The actual phone number of the lead, with or without the country code. | String |
| countryCode | Required | The country dialing code associated with the phone number (e.g., +91 for India)., if not present in phoneNo. | String |
| type | Optional | It defines the type of phone number, such as Primary, Alternate, or any other custom tag. These values will be available within the platform for configurations like retry strategies. | String |

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
 'https://api3.sprinklr.com/{env}/api/v2/dmp/audience-lead/{partnerName}/bulk' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '​​[
   {
        "leadId": "2675",
        "segmentIds" : ["65b249ca4b13a738ab599213"],
        "userInfo": {
            "firstName": "Test",
            "lastName": "123",
            "phoneNo": "+918447380993",
            "customerId": "+918447380993",
	"phoneDetails":[{
	"phoneNo": "982719211",
	"countryCode": "+91",
	"type": "Primary"
	},
					{
	"phoneNo": "982719912",
	"countryCode": "+91",
	"type": "customphonetag"
	}]
        },
        "attributes":
        [
            {
                "key": "PorterLeadID",
                "value": "2675",
                "fieldType": "TEXT"
            },
            {
                "key": "PorterCustomerID",
                "value": "Yaksh_20112023",
                "fieldType": "TEXT"
            },
           {
                "key": "PorterLiveChat",
                "value": "32",
                "fieldType": "TEXT"
            },
           {
                "key": "PorterCampaign",
                "value": "11JAN_UAT",
                "fieldType": "TEXT"
            },
             {
                "key": "PorterSegment",
                "value": "seg2_25Jan",
                "fieldType": "TEXT"
            }
        ]
    },
    {
        "leadId": "2676",
        "segmentIds" : ["65b249ca4b13a738ab599213"],
        "userInfo": {
            "firstName": "Test",
            "lastName": "123",
            "phoneNo": "+918447380993",
            "customerId": "+918447380993"
        },
        "attributes":
        [
            {
                "key": "PorterLeadID",
                "value": "2676",
                "fieldType": "TEXT"
            },
            {
                "key": "PorterCustomerID",
                "value": "Yaksh_20112024",
                "fieldType": "TEXT"
            },
           {
                "key": "PorterLiveChat",
                "value": "33",
                "fieldType": "TEXT"
            },
           {
                "key": "PorterCampaign",
                "value": "11JAN_UAT",
                "fieldType": "TEXT"
            },
             {
                "key": "PorterSegment",
                "value": "seg2_25Jan",
                "fieldType": "TEXT"
            }
        ]
    }
]'






## Example - Response





{
    "data": "\"Lead Created Successfully for LeadIds: [ 2676, 2675 ]\"",
    "errors": []
}







**Dev Notes: **You can use the same API to update the lead. While updating a lead, passing the `segmentId` and `customerId` that was used to create a lead is ​​prerequisite.

[](https://dev.sprinklr.com/create-update-bulk-leads)




[Back to top](https://dev.sprinklr.com/create-update-bulk-leads)
