---
title: "Fetch Custom Metrics"
slug: fetch-custom-metrics
url: https://dev.sprinklr.com/fetch-custom-metrics
---

# Fetch Custom Metrics

#
GET Fetch Custom Metrics


This API allows you to fetch custom metrics associated with the given report name.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/reports/customMetric/{reportingEngineId}?reportNames={reportName}

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

## Path Parameters







[Fetch Reporting Engines API](https://dev.sprinklr.com/fetch-reporting-engines)

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| reportingEngineId | Required | String | Refers to the module specific reporting engine Id. You can refer to  to fetch the relevant engine Id |

## Query Parameters







[Fetch Report Names API](https://dev.sprinklr.com/fetch-report-names)

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| reportNames | Required | String | Refers to the report name for which you want to fetch the custom metrics information. You can refer to the  for fetching the relevant report name |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X GET \
'https://api3.sprinklr.com/{env}/api/v2/reports/customMetric/PLATFORM?reportnames=ACCOUNT_INSIGHTS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": {
        "ACCOUNT_INSIGHTS": [
            {
                "script": "(__formula__elem__453*1000)",
                "requiredProjections": [
                    {
                        "key": "__formula__elem__453",
                        "measurement": "FOLLOWERS_COUNT",
                        "aggregateFunction": "SUM"
                    }
                ],
                "measurementGroups": [
                    "COMMON"
                ],
                "groupNames": [
                    "Custom Measurement"
                ],
                "isShared": false,
                "sharedKey": "TIMETEST21795",
                "filterMeasurement": true,
                "name": "TIMETEST21795",
                "fieldName": "TIMETEST21795",
                "displayName": "timetest",
                "lcName": "timetest",
                "hidden": false,
                "enabledForAiConcierge": false,
                "dataType": "NUMERIC",
                "additional": {
                    "measurement_type": "Custom Measurement",
                    "clientId": 4706,
                    "IS_PERMISSIBLE": "false",
                    "definitionId": "5a157659e4b0e7ba1aef4ab6"
                }
            },
            {
                "script": "(__formula__elem__1582433862695673+__formula__elem__158243386269537)",
                "requiredProjections": [
                    {
                        "key": "__formula__elem__1582433862695673",
                        "measurement": "FOLLOWERS_COUNT",
                        "aggregateFunction": "SUM"
                    },
                    {
                        "key": "__formula__elem__158243386269537",
                        "measurement": "FACEBOOK_PAGE_FANS",
                        "aggregateFunction": "SUM"
                    }
                ],
                "type": "CALCULATED",
                "measurementGroups": [
                    "COMMON"
                ],
                "groupNames": [
                    "Custom Measurement"
                ],
                "isShared": false,
                "sharedKey": "SUNDAY_TESTING_621",
                "filterMeasurement": true,
                "name": "SUNDAY_TESTING_621",
                "fieldName": "SUNDAY_TESTING_621",
                "displayName": "sunday testing ",
                "lcName": "sunday testing",
                "filters": [],
                "hidden": false,
                "enabledForAiConcierge": false,
                "dataType": "NUMERIC",
                "additional": {
                    "definitionId": "5e5206465abe65520ec9f2cb",
                    "measurement_type": "Custom Measurement",
                    "IS_PERMISSIBLE": "false",
                    "clientId": 4706
                }
            },
              "code": "label.field.KS_19.5Zephyr"
            }
        ]
    },
    "errors": []
}
 

     
     
   
 

## Response Schema







| Parameter |  | Sub-Parameter | Type | Description |
| --- | --- | --- | --- | --- |
| data |  |  | Object | Container for measurement data |
|  | {GANALYTICS4_GENDER} |  | Array of Objects | List of measurement objects for the "GANALYTICS4_GENDER" category. |
|  |  | type | String | Type of measurement (e.g., DELTA). |
|  |  | measurementGroups | Array of Objects | Measurement groups to which the measurement belongs. |
|  |  | groupNames | Array of Strings | Names of the groups the measurement belongs to. |
|  |  | isShared | Boolean | Indicates if the measurement is shared. |
|  |  | sharedKey | String | Key for shared measurements. |
|  |  | shortName | String | Short name for the measurement. |
|  |  | filterMeasurement | Boolean | Indicates if the measurement can be filtered. |
|  |  | name | String | Name of the measurement. |
|  |  | fieldName | String | Field name for the measurement. |
|  |  | displayName | String | Display name for the measurement. |
|  |  | hidden | Boolean | Indicates if the measurement is hidden. |
|  |  | enabledForAiConierge | Boolean | Indicates if the measurement is enabled for AI Concierge. |
|  |  | dataType | String | Data type of the measurement (e.g., NUMERIC, TIME_DIFFERENCE). |
|  |  | Additional | Object | Additional metadata related to the measurement. It includes information about ID, type, client ID, and channel types associated with the measurement. |
|  |  | channelTypes | Array of Strings | List of channel types associated with the measurement. |
|  |  | code | String | Code representing the measurement. |
| errors |  |  | Array of Objects | List of error objects, if any. |

	[](https://dev.sprinklr.com/fetch-custom-metrics) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-custom-metrics)
