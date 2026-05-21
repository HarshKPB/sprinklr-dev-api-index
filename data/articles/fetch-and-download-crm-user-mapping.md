---
title: "Fetch and Download CRM User Mapping"
slug: fetch-and-download-crm-user-mapping
url: https://dev.sprinklr.com/fetch-and-download-crm-user-mapping
---

# Fetch and Download CRM User Mapping

#
  GET - Fetch and Download CRM User Mapping


Using this API, you can fetch and export (download) the CRM user mappings for the given installed App Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/crm-user-mapping/{InstalledAppId}/export


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

## Example - Request

 Copy Code



curl -X GET

'https://api3.sprinklr.com/{env}/api/v2/crm-user-mapping/6685495f74c1b74c1659ad74'

-H 'Authorization: Bearer {Enter your Access Token}'

-H 'Key: {Enter your API KEY}'

-H 'accept: application/json'




### Example - Response




Sprinklr User ID,CRM User ID
66000027,0051S00000AtoLjQAJ





### Response Parameters




















| Parameter | Definition | Type |
| --- | --- | --- |
| sprUserId | Refers to the unique identifier for the Sprinklr user | Integer |
| crmUserId | Refers to the unique identifier for the CRM user | String |

 [](https://dev.sprinklr.com/fetch-and-download-crm-user-mapping)




[Back to top](https://dev.sprinklr.com/fetch-and-download-crm-user-mapping)
