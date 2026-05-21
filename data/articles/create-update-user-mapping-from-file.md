---
title: "Create/Update User Mapping - From File"
slug: create-update-user-mapping-from-file
url: https://dev.sprinklr.com/create-update-user-mapping-from-file
---

# Create/Update User Mapping - From File

#
  PUT - Create/Update User Mapping - From File


	 Using this API, you can perform a bulk operation to create or update CRM user mapping from a CSV file.

## API Endpoint

https://api2.sprinklr.com`/{env}/`api/v2/crm-user-mapping/{installedAppId}/import


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

### Body - Form-Data Parameters

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| file | Required | The uploaded csv mapping file for crm and spr user Ids | CSV |

## CSV File Format













| Column Name | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Sprinklr User Id/Email | Required | Refers to the unique identifier for the Sprinklr user or their unique email address | Integer, String |
| CRM User Id | Required | Refers to the unique identifier for the CRM user | String |


**Dev Note: **If either of the key-value pair of CRM user Id or SPR user Id already exist, the mapping will be updated. And, if both the SPR user Id and CRM user Id are unique, a new mapping will be created.

## Example - Request

 Copy Code



	curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/crm-user-mapping/6685495f74c1b74c1659ad74/import' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: application/json' \
  -H 'key: {apikey}'
  -F 'file=@"/Users/Desktop/BulkUpdateCrmUserMappings"'





### Example - Response




CRM User ID,Sprinklr User Id/Email,Status,Failure Reason
0051S00000AtoLjQAJ,66000142,Success,null
0055j00000CGFCwAAP,66004678,Failed,Failed for row index: 1, tried to map crmUserId 0055j00000CGFCwAAP to sprUserId 66004678 . Error: Invalid crm user Id.
005J4000000YJw8IAG,66009154,Failed,Failed for row index: 2, tried to map crmUserId 005J4000000YJw8IAG to sprUserId 66009154 . Error: Invalid spr user Id.





### Response Parameters








| Parameter | Definition | Type |
| --- | --- | --- |
| CRM User ID | Refers to the given CRM user Id | String |
| Sprinklr User Id/Email | Refers to the email or Id associated with the Sprinklr user | String, Integer |
| Status | Refers to the status of the CRM user mapping, i.e, either Success or Failed | String |
| Failure Reason | If the status is failed, this parameter returns the reason behind the failure | String |

[](https://dev.sprinklr.com/create-update-user-mapping-from-file) 

 

 
[Back to top](https://dev.sprinklr.com/create-update-user-mapping-from-file)
