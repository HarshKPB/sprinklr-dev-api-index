---
title: "Surveys v1"
slug: surveys-v1
url: https://dev.sprinklr.com/surveys-v1
---

# Surveys v1

#
  POST - Surveys

This report is used to gather the insights for the Survey.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/reports/query

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

**Description**

This report will show a Survey question response count.

**Request Body**

| Name | Values |
| --- | --- |
| reportingEngine | PLATFORM |
| report | SURVEY_QUESTION_RESPONSE |
| Supported groupBys.dimensionName | ANSWERS (groupType = FIELD) |
| Supported filters.dimensionName | CLIENT_ID ACCOUNT_ID |
| Supported projections.measurementName | QUESTION_RESPONSE_COUNT (aggregateFunction = SUM) ANSWERS (aggregateFunction = CARDINALITY |

## Example -  Request

Retrieve the results of a survey groupd by answers




 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v1/reports/query' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
 "startTime":1507694400000,
  "endTime":1510289999999,
  "timeZone":"UTC",
  "page":0,
  "pageSize":20,
  "reportingEngine":"PLATFORM",
  "report":"SURVEY_QUESTION_RESPONSE",
  "groupBys":[
    {
      "heading":"ANSWERS",
      "dimensionName":"ANSWERS",
      "groupType":"FIELD",
      "details":{}
    }
  ],
  "filters":[
    {
      "dimensionName":"ACCOUNT_ID",
      "filterType":"IN",
      "values":[
         201862,
         163082,
         163136,
         180698,
         104412,
         201365,
         202252,
         191460,
         "999998",
         "999999",
         "-65537",
         "-10"
      ],
      "details":null
    },
    {
      "dimensionName":"CLIENT_ID",
      "filterType":"IN",
      "values":[
         5547,
         5547,
         "-1"
      ],
      "details":null
    }
  ],
  "projections":[
    {
      "heading":"QUESTION_RESPONSE_COUNT",
      "measurementName":"QUESTION_RESPONSE_COUNT",
      "aggregateFunction":"SUM"
    },
    {
      "heading":"ANSWERS",
      "measurementName":"ANSWERS",
      "aggregateFunction":"CARDINALITY"
    }
  ]
}'





## Example - Response




{
    "headings": [
        "ANSWERS",
        "QUESTION_RESPONSE_COUNT",
        "ANSWERS"
    ],
    "rows": [
        [
            "Yes",
            3,
            1
        ],
        [
            "5 Star",
            2,
            1
        ],
        [
            "8",
            2,
            1
        ],
        [
            "10",
            1,
            1
        ],
        [
            "4",
            1,
            1
        ],
        [
            "5",
            1,
            1
        ],
        [
            "5 - 10 mins",
            1,
            1
        ],
        [
            "Great job! ",
            1,
            1
        ],
        [
            "Great service! ",
            1,
            1
        ],
        [
            "Lasagna",
            1,
            1
        ],
        [
            "Option 1",
            1,
            1
        ],
        [
            "Social Media (E.g. Facebook, Twitter)",
            1,
            1
        ],
        [
            "Twitter",
            1,
            1
        ],
        [
            "Unlocked my account ",
            1,
            1
        ],
        [
            "Yoga 910",
            1,
            1
        ]
    ]
}





[](https://dev.sprinklr.com/surveys-v1)




[Back to top](https://dev.sprinklr.com/surveys-v1)
