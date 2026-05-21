---
title: "Custom Query Using Widget ID"
slug: custom-query-using-widget-id
url: https://dev.sprinklr.com/custom-query-using-widget-id
---

# Custom Query Using Widget ID

#
POST Custom Query Using Widget ID

	Using this API, you can export the reporting widget data using widget Id. The advantage of this approach is that you don't need to update the request payload every time any metric or dimension is updated in the widget.

**Help Resource:** **[Reporting Blueprint](https://dev.sprinklr.com/reporting-blueprints)**

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/reports/query/{widgetId}

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

**Dev Notes: **You can extract the API request payload from the reporting widget in the UI, using "[Generate API v2 Payload](https://help.sprinklr.com/articles/integration-guides/generate-api-v2-payload/613767325f2e7c0c9ed36f2b)" option. You can find the widgetId, startTime, endTime, and timeZone values from here to construct the payload.

Kindly note that widget Id would be static and the other fields in the API payload can be modified based on your requirements.

### Path Parameters







****

-
- ``
-
-
-

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| widgetId | Required | Refers to the unique identifier for the widget you want to extract the data for.How to find the Widget Id?Click on the three dots besides the widget you want to extract the data fromClick on "Generate API v2 Payload" option from the drop-down menuA new pop-up window will appear with the request payloadYou can locate the widget Id within the additional objectCopy the widgetId in the path parameters | String |

### Request Parameters







**

**

****

****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| startTime | Required | Refers to the start time since when you want to pull the data.You can manually configure this based on your requirements | Epoch (milliseconds) |
| endTime | Required | Refers to the end time till when you want to pull the data.You can manually configure this based on your requirements | Epoch (milliseconds) |
| page | Required | Refers to the page number for which you want to pull the data.The first page number be 0 (default value) and can be incremented by +1 to fetch the next page results | Integer |
| pageSize | Optional | Refers to the number of rows you wish to pull with one API call.It is recommended to maintain maximum page size of 1000 as exceeding it might lead to server load and frequent "504 Gateway Timeout" error | Integer |
| skipResolve | Required | This field controls if certain fields are expanded into objects or are displayed as references to the respective objects.Default: false | Boolean |
| jsonResponse | Required | This field controls if the data is returned in as an array of values or an array of JSON objects.Default: false | Boolean |
| interval | Optional | Refers to the interval between the two data sets.Only required when there is a "groupType": "DATE_HISTOGRAM" exists in the "Generate API v2 Payload." | String |
| timeZone | Required | Refers to the time zone in which you want the results.This field is auto generated based on your time zone and can be modified based on your requirements | String |

**Dev Notes: ** To get response as per industry standards, please keep the value of `"jsonResponse"`:`true`

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/reports/query/63c7c1060f8b267959c2be56' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "startTime": 1104537600000,
    "endTime": 1684175399999,
    "page": 0,
    "pageSize": 1000,
    "skipResolve": false,
    "jsonResponse": false,
    "interval": "weeks",
    "timeZone": "Asia/Kolkata"
}'
 

     
     
 

## Example - Response

 
 
     

{
    "data": {
        "headings": [
            "ACCOUNT_ID_0",
            "ACCOUNT_URL_1",
            "ACCOUNT_STATE_2",
            "USER_ID_3",
            "date_4",
            "M_ACCOUNT_STATE_REPORT_ACTIVE_ACCOUNT_COUNT_0"
        ],
        "rows": [
            [
                "Test Account",
                "https://www.linkedin.com/in/test-account-b5a866263/",
                "1",
                "Test 1",
                "1674585000000",
                3.0
            ]
        ]
    },
    "errors": []
}
 

     
     
   

	[](https://dev.sprinklr.com/custom-query-using-widget-id) 

 

 
[Back to top](https://dev.sprinklr.com/custom-query-using-widget-id)
