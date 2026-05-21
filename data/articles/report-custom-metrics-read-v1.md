---
title: "Report Custom Metrics Read v1"
slug: report-custom-metrics-read-v1
url: https://dev.sprinklr.com/report-custom-metrics-read-v1
---

# Report Custom Metrics Read v1

#
  GET - Report Custom Metrics Read

Using this API, you can fetch reporting custom metrics.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/reports/customMetric/{reportingEngineId}

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

## Path Parameters

[Fetch Reporting Engines API](https://dev.sprinklr.com/fetch-reporting-engines)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| reportingEngineId | Required | Refers to the name of the reporting engine.You can fetch supported reporting engines Ids using . | String |

## Query Parameters

****

[Fetch Report Name API](https://dev.sprinklr.com/fetch-report-names)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| reportName | Required | Refers to the report name corresponding to the report engine Id.Example: POST_INSIGHTS, ACCOUNT_INSIGHTSYou can fetch the report name using the | String |

## Example - Request

Fetch custom metrics for report engine ‘PLATFORM’ and report ‘POST_INSIGHTS’

## Example - Sample Call




 Copy Code



curl -X GET \
'https://api3.sprinklr.com/{env}/api/v1/reports/customMetric/PLATFORM?reportName=POST_INSIGHTS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example - Response




 {
    "POST_INSIGHTS":[
        {
            "script":"(__formula__elem__3684)",
            "requiredProjections":[
                {
                  "key":"__formula__elem__3684",
                  "measurement":"INSTAGRAM_POST_COMMENTS_COUNT",
                  "aggregateFunction":"SUM"
                }
            ],
            "type":"CALCULATED",
            "measurementGroups":[
                "COMMON"
            ],
            "additional":{
                "definitionId":"56b8416ee4b0ac4e5aac79e8"
            },
            "groupNames":[
                "Custom Measurement"
            ],
            "isShared":false,
            "sharedKey":"LOCALSHARECM201602081248510643683",
            "name":"LOCALSHARECM201602081248510643683",
            "fieldName":"LOCALSHARECM201602081248510643683",
            "displayName":"LocalShareCM20160208124851064",
            "description":"TestDesc",
            "hidden":false,
            "dataType":"NUMERIC"
        },
        {
            "script":"(__formula__elem__3407)",
            "requiredProjections":[
                {
                    "key":"__formula__elem__3407",
                    "measurement":"INSTAGRAM_POST_COMMENTS_COUNT",
                    "aggregateFunction":"SUM"
                }
            ],
            "type":"CALCULATED",
            "measurementGroups":[
                "COMMON"
            ],
            "additional":{
                "definitionId":"56b42471e4b0da0bed35cebb"
            },
            "groupNames":[
                "Custom Measurement"
            ],
            "isShared":false,
            "sharedKey":"LOCALSHARECM201602050956144283406",
            "name":"LOCALSHARECM201602050956144283406",
            "fieldName":"LOCALSHARECM201602050956144283406",
            "displayName":"LocalShareCM20160205095614428",
            "description":"TestDesc",
            "hidden":false,
            "dataType":"NUMERIC"
        }
    ]
}





[](https://dev.sprinklr.com/report-custom-metrics-read-v1)




[Back to top](https://dev.sprinklr.com/report-custom-metrics-read-v1)
