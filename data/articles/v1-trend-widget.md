---
title: "Trend Widget"
slug: v1-trend-widget
url: https://dev.sprinklr.com/v1-trend-widget
---

# Trend Widget

# POST Trend Widget

This widget is used to gather time-based metrics. Request includes the trendAggregationPeriod attribute which is used to specify the data aggregation interval.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/listening/query/widget

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

## Volume Trend

This returns the daily volume of mentions for a Topic filter.




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "sinceTime": 1530417600000,
    "untilTime": 1547499885487,
    "details": {
        "widgetType": "TREND"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        }
    ],
    "metric": "MENTIONS",
    "start": 0,
    "rows": 20,
    "trendAggregationPeriod": "DAY"
}'



### Example - Response




{
    "status": "SUCCESS",
    "response": {
        "values": [
            {
                "timestampMillis": 1530403200000,
                "value": 2,
                "period": "DAY",
                "values": {}
            },
            {
                "timestampMillis": 1530489600000,
                "value": 9,
                "period": "DAY",
                "values": {}
            },
            {
                "timestampMillis": 1530576000000,
                "value": 4,
                "period": "DAY",
                "values": {}
            },
            {
                "timestampMillis": 1530662400000,
                "value": 4,
                "period": "DAY",
                "values": {}
            },
            {
                "timestampMillis": 1530748800000,
                "value": 3,
                "period": "DAY",
                "values": {}
            },
            {
                "timestampMillis": 1530835200000,
                "value": 11,
                "period": "DAY",
                "values": {}
            },
            {
                "timestampMillis": 1530921600000,
                "value": 7,
                "period": "DAY",
                "values": {}
            },
            {
                "timestampMillis": 1531008000000,
                "value": 0,
                "period": "DAY",
                "values": {}
            }
    }
}



[](https://dev.sprinklr.com/v1-trend-widget) 

 

 
[Back to top](https://dev.sprinklr.com/v1-trend-widget)
