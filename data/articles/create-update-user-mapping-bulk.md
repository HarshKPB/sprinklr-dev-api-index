---
title: "Create/Update User Mapping - Bulk"
slug: create-update-user-mapping-bulk
url: https://dev.sprinklr.com/create-update-user-mapping-bulk
---

# Create/Update User Mapping - Bulk

#
  PUT - Create/Update User Mapping - Bulk


Using this API, you can perform a bulk operation to create or update CRM user mapping for the given CRM and SPR user Ids.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/crm-user-mapping/{installedAppId}/bulk-upsert


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

### Path Parameter
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| InstalledAppId | Required | Refers to the unique identifier for the CRM installed appRefer to the table below for the steps for extracting Installed App Id | String |

**Steps to Extract Installed App Id from UI: **

- Click on the `**+**` tab on Sprinklr's homepage.
- Search and navigate to "All Marketplace".
- Search for the CRM app you want the user mapping for
- Hover and click on the edit button
- The app installed Id will be appended in the suffix of the browser URL

## Request Parameters - Array of SPR and CRM User Ids













| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sprUser | Required | Refers to the unique identifier for the Sprinklr user | Integer |
| crmUser | Required | Refers to the unique identifier for the CRM user | String |


**Dev Note: **If either of the key-value pair of CRM user Id or SPR user Id already exist, the mapping will be updated. And, if both the SPR user Id and CRM user Id are unique, a new mapping will be created.

## Example - Request

 Copy Code



	curl -X PUT \
 'https://api3.sprinklr.com/{{env}}/api/v2/crm-user-mapping/6685495f74c1b74c1659ad74/bulk-upsert'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
  -d' [
    {
        "crmUser": "0051S00000AtoLjQAJ",
        "sprUser": "66000142"
    }
]'





### Example - Response




{
    "data": [
        {
            "installedAppId": "6685495f74c1b74c1659ad74",
            "crmUserId": "0051S00000AtoLjQAJ",
            "sprUserId": 66000142,
            "createdBy": 66000101,
            "lastModifiedBy": 66000101,
            "createdTime": 1720101365700,
            "lastModifiedTime": 1721297053058
        }
    ],
    "errors": []
}





### Response Parameters












































| Parameter | Definition | Type |
| --- | --- | --- |
| installedAppId | Refers to the unique identifier for the CRM installed app | String |
| crmUserId | Refers to the unique identifier for the CRM user | String |
| sprUserid | Refers to the unique identifier for the Sprinklr user | Integer |
| createdBy | Refers to the unique identifier for the user who created the app | Integer |
| lastModifiedBy | Refers to the unique identifier for the user who last modified the app | Integer |
| CreatedTime | Refers to the time at which the CRM app was created | Epoch (Milliseconds) |
| lastModifiedTime | Refers to the time at which the CRM app was last modified | Epoch (Milliseconds) |

[](https://dev.sprinklr.com/create-update-user-mapping-bulk) 

 

 
[Back to top](https://dev.sprinklr.com/create-update-user-mapping-bulk)
