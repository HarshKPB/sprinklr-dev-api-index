---
title: "Batch Query"
slug: batch-query
url: https://dev.sprinklr.com/batch-query
---

# Batch Query

#
POST Batch Query

If the configured metrics and dimensions in a widget are being pulled from multiple report types, batch query API is used. For information on different report types, refer to [fetch report names API documentation.](https://dev.sprinklr.com/fetch-report-names)

**Help Resource:** **[Reporting Blueprint](https://dev.sprinklr.com/reporting-blueprints)**

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/reports/batchQuery

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

**Dev Notes: **You can extract the API request payload from the reporting widget in the UI, using "[Generate API v2 Payload](https://www.sprinklr.com/help/articles/integration-guides/generate-api-v2-payload/633c5ca8a0522e093b06c1a2)" option. Once extracted, copy the payload and use it in the request body of the API call as is.

### Request Parameters







****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| collate | Optional | If true, collate implies for grouping multiple queries together in the response.This field is valid for batch queries.Default: False | Boolean |
| requests | Required | Applicable where multiple requests need to be passed | Object |
| req | Required | Refers to the request number in the response.Contains information on report name and reporting engine.Refer to the table below for req object details. | Object |

### req Object Details







****

****










****












****







































| Parameters | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| report |  | Required | This defines the type of the report you want insights forExample: SURVEY_QUESTION_RESPONSE, DAILY_AD_STATYou can copy the exact value mentioned in the UI payload | String |
| reportingEngine |  | Required | Copy exact value from the UI payload.Supported engines include: PLATFORM, INBOUND_MESSAGE | String |
| timeField |  | Optional | Set the type of time range (sinceTime + untilTill) to use.Example: SYSTEM_CREATED_TIME, SN_CREATED_TIME | String |
| startTime |  | Required | Starting time from when you want the report | Epoch |
| endTime |  | Required | Ending time till when you want the report records | Epoch |
| timeZone |  | Required | Copy exact value from the UI payload.Default value = UTC | String |
| page |  | Optional | Specify the starting page number you want to extract from the report.Default value: 0 | Integer |
| pageSize |  | Optional | Specifies the numbers of entries shown on a single page | Integer |
| filters |  | Optional | Defines the filter types that are applied on the widget.Refer to the table below for filter array details | Array |
| groupBys |  | Required | Allows grouping the data according to the mentioned categoriesThe segregated groups make it easy to analyze groups and result in better analysis | Array |
|  | heading |  | The heading of the groups we are referring to | String |
|  | dimensionName | Required | Name of the dimension, this should match exactly “group by” field from UI payload | String |
|  | groupType | Required | Defines the type of group.Copy value exactly from the UI PayloadSupported groupTypes:DATE_HISTOGRAM, TIME_OF_DAY,DAY_OF_WEEK,MONTH_OF_YEAR,FIELD | String |
|  | details |  | Additional details (if any) such as custom field details if they are being passed | String,Integer |
|  | namedFilters |  | Copy exact value from the UI payload | String |
| Projections |  | Required | Information regarding different metrics | Array |
|  | heading | Required | Any string value which defines the data | String |
|  | measurementName | Required | Refers to the metrics you want the report forExample:CUSTOM_EVENT_MOBILE_SEARCH,FB_APP_STORE_CLICKS | String |
|  | aggregateFunction | Required | Supported functions include:SUM, AVG, MIN, MAX, STATS | String |
|  | details | Optional | Additional details (if any) | Object |
| projectionDecorations |  | Optional | Available values:CHANGE, PERCENTAGE_CHANGE, PERCENTAGE | Object |
| sorts |  | Optional | sorting information | Array |
|  | heading |  | Heading of the groupbys you are sorting | String |
|  | order |  | The order of the results.For example: ASC for ascendingDESC for descending | String |
| streamRequestInfo |  | Required | Copy exact value from the UI payload | String |
| additional |  | Optional | Report dimensions are automatically resolved to include additional information | Map |
|  | translateResponse | Optional | Copy exact value from the UI payload | Boolean |
|  | dashboardId |  | Id of the dashboard | String |
|  | engine |  | Refers to the data sources we are using | String |
|  | widgetId |  | The widget ID from which you are pulling reports | String |
|  | showTotal |  | Copy exact value from the UI payload | String |
|  | Currency |  | Copy exact value from the UI payload | String |
|  | ChartType |  | Copy exact value from the UI payload | String |
|  | showRolloverTrends |  | Copy exact value from the UI payload | Boolean |
|  | Tabular |  | Table chart is selected.If true,  more than one groupBys are being plotted | Boolean |
| skipResolve |  | Optional | Copy exact value from the UI payload | Boolean |
| jsonResponse |  | Required | Set it to true to get the industry standard structured response | Boolean |

### filters Array Description Table







| Parameter | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| dimensionName |  | Required | Attributes you want to get filtered | String |
| filterType |  | Required | Defines the type of the filter applied.The value should match exactly the UI payload filterTypeAvailable values include: IN, GT, GTE, LT, LTE, NIN, BETWEEN, STARTS_WITH, CONTAINS, EQUALS , FILTER, EXISTS | String |
| values |  | Required | These are filter values, copy them exactly from UI payload | list |
| details |  | Optional | Details w.r.t to the applied filters | Object |
|  | type |  | Copy exact value from the UI payload The value of the parameter is requirement specific | String |
|  | canBeAnonymised |  | Copy exact value from the UI payloadThe value of the parameter is requirement specific | Boolean |
|  | showAsDashboardFilter |  | Copy exact value from the UI payloadThe value of the parameter is requirement specific | Boolean |

	**Note:** If “`Collate`” is present in the UI payload, it implies that the query is a batch query.

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/reports/batchQuery' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "collate": false,
    "requests": {
        "req2": {
            "report": "POST_INSIGHTS",
            "reportingEngine": "PLATFORM",
            "timeField": null,
            "startTime": 1648665000000,
            "endTime": 1651256999999,
            "timeZone": "Asia/Kolkata",
            "page": 0,
            "pageSize": 20,
            "filters": null,
            "groupBys": null,
            "projections": [
                {
                    "heading": "M_POST_INSIGHTS_TWITTER_IMPRESSIONS_0",
                    "measurementName": "TWITTER_IMPRESSIONS",
                    "aggregateFunction": "SUM",
                    "details": {}
                }
            ],
            "projectionDecorations": [],
            "projectionFilters": null,
            "sorts": [
                {
                    "heading": "TWITTER_MENTIONS__SUM__ACCOUNT_INSIGHTS",
                    "order": "DESC"
                }
            ],
            "streamRequestInfo": null,
            "additional": {
                "translateResponse": "false",
                "dashboardId": "623df6a297ce7f74aa32d143",
                "engine": "PLATFORM",
                "widgetId": "6256a8b9c5cf6913875f45a0",
                "showTotal": "false",
                "Currency": "DEFAULT",
                "chartType": "TABLE",
                "showRolloverTrends": "true",
                "TABULAR": "true"
            },
            "skipResolve": false,
            "jsonResponse": false
        },
        "req1": {
            "report": "ACCOUNT_INSIGHTS",
            "reportingEngine": "PLATFORM",
            "timeField": null,
            "startTime": 1648665000000,
            "endTime": 1651256999999,
            "timeZone": "Asia/Kolkata",
            "page": 0,
            "pageSize": 20,
            "filters": null,
            "groupBys": null,
            "projections": [
                {
                    "heading": "M_ACCOUNT_INSIGHTS_TWITTER_MENTIONS_0",
                    "measurementName": "TWITTER_MENTIONS",
                    "aggregateFunction": "SUM",
                    "details": {}
                }
            ],
            "projectionDecorations": [],
            "projectionFilters": null,
            "sorts": [
                {
                    "heading": "TWITTER_MENTIONS__SUM__ACCOUNT_INSIGHTS",
                    "order": "DESC"
                }
            ],
            "streamRequestInfo": null,
            "additional": {
                "translateResponse": "false",
                "dashboardId": "623df6a297ce7f74aa32d143",
                "engine": "PLATFORM",
                "widgetId": "6256a8b9c5cf6913875f45a0",
                "showTotal": "false",
                "Currency": "DEFAULT",
                "chartType": "TABLE",
                "showRolloverTrends": "true",
                "TABULAR": "true"
            },
            "skipResolve": false,
            "jsonResponse": false
        }
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": {
        "reports": {
            "req3": {
                "headings": [
                    "REQUIRED_USER_GROUP_2",
                    "LOGIN_CURRENT_STATUS_1",
                    "REQUIRED_USER_0",
                    "M_INBOUND_CASE_CASE_COUNT_0"
                ],
                "rows": [
                    [
                        "Video Permissions",
                        "Logged In",
                        "PA",
                        3.0
                    ],
                    [
                        "gugg",
                        "Logged In",
                        "PA",
                        3.0
                    ],
                    [
                        "Video Permissions",
                        "Logged In",
                        "Moderation User",
                        2.0
                    ],
                    [
                        "gugg",
                        "Logged In",
                        "Moderation User",
                        2.0
                    ]
                ]
            }
        }
    },
    "errors": []
}
 

     
     
   
 

### Response Parameters







| Parameter | Sub-Param | Sub-Param | Description | Type |
| --- | --- | --- | --- | --- |
|  | reports |  | Object containing details of multiple requests | Object |
|  |  | req[number] | Object containing headings and row data | Object |

### req Object Details





| Parameter | Description | Type |
| --- | --- | --- |
| headings | Refers to headings of the rows present in the report | list |
| rows | Provides details of data present in the rows | list |

    **Note:**To understand how to extract UI payload, refer to this knowledge portal [article](https://www.sprinklr.com/help/articles/integration-guides/generate-api-v2-payload/633c5ca8a0522e093b06c1a2b).

[](https://dev.sprinklr.com/batch-query) 

 

 
[Back to top](https://dev.sprinklr.com/batch-query)
