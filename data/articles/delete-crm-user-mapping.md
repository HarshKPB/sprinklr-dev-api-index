---
title: "Delete CRM User Mapping"
slug: delete-crm-user-mapping
url: https://dev.sprinklr.com/delete-crm-user-mapping
---

# Delete CRM User Mapping

#
  DELETE - Delete CRM User Mapping


Using this API, you can delete CRM user mapping for the given installed app Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/crm-user-mapping/{installedAppId}


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

## Query Parameters













| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sprUser | Optional | Refers to the unique identifier for the Sprinklr user. All the mappings matching the SPR user Ids will get deleted. | Integer |
| crmUser | Optional | Refers to the unique identifier for the CRM user. All the mappings matching the CRM user Ids will get deleted | String |


**Dev Note: **If the SPR user Id or CRM user Id are not passed, the API will delete all the CRM user mappings for the given installed app Id. Also, if one the SPR user Id or CRM user Id is passed, it deletes all the mapping records that match the given Id.

## Example - Request

 Copy Code



curl -X DELETE \
'https://api3.sprinklr.com/{env}/api/v2/crm-user-mapping/6685495f74c1b74c1659ad74?sprUser=66000142&crmUser=0051S00000AtoLjQAJ'\
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'accept: application/json'




### Example - Response




{
    "data": [
        {
            "installedAppId": "6685495f74c1b74c1659ad74",
            "crmUserId": "0051S00000AtoLjQAJ",
            "sprUserId": 66000142,
            "createdTime": 1720011116638,
            "lastModifiedTime": 1720011116638
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

[](https://dev.sprinklr.com/delete-crm-user-mapping) 

 

 
[Back to top](https://dev.sprinklr.com/delete-crm-user-mapping)
