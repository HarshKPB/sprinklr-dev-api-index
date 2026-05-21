---
title: "Grouped Trend Widget"
slug: v1-grouped-trend-widget
url: https://dev.sprinklr.com/v1-grouped-trend-widget
---

# Grouped Trend Widget

# POST Grouped Trend Widget

This widget is used to gather time-based metrics. Request contains details.dimension attributes and the trendAggregationPeriod attribute.

trendAggregationPeriod attribute is used to specify the data aggregation interval.

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

**Dev Notes: **When the group trend data pull is requested, it is mandatory for the request to include filters.dimension attributes corresponding to details.dimension attributes.  But if filters.dimension is missing, the system will automatically pull the top five values for the dimension and apply them to groupBy.

### Volume Trend

This returns the daily volume of mentions grouped by Topic.

### Example - Request




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
        "widgetType": "GROUPED_TREND",
        "dimension": "TOPIC"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        },
        {
            "dimension": "GEO_COUNTRY",
            "filterValues": [
                "CN",
                "GB",
                "RU",
                "US"
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
    "response": [
        {
            "word": "Sprinklr",
            "id": "595c50dbe4b064e21f85d074",
            "values": [
                {
                    "timestampMillis": 1530489600000,
                    "value": 6,
                    "period": "DAY",
                    "values": {}
                },
                {
                    "timestampMillis": 1530576000000,
                    "value": 0,
                    "period": "DAY",
                    "values": {}
                },
                {
                    "timestampMillis": 1530662400000,
                    "value": 1,
                    "period": "DAY",
                    "values": {}
                },
                {
                    "timestampMillis": 1530748800000,
                    "value": 2,
                    "period": "DAY",
                    "values": {}
                },
                {
                    "timestampMillis": 1530835200000,
                    "value": 5,
                    "period": "DAY",
                    "values": {}
                },
                {
                    "timestampMillis": 1547078400000,
                    "value": 2,
                    "period": "DAY",
                    "values": {}
                }
            ],
            "min": {
                "timestampMillis": 1530576000000,
                "value": 0,
                "period": "DAY",
                "values": {}
            },
            "max": {
                "timestampMillis": 1534809600000,
                "value": 156,
                "period": "DAY",
                "values": {}
            }
        }
    ]
}



[](https://dev.sprinklr.com/v1-grouped-trend-widget) 

 

 
[Back to top](https://dev.sprinklr.com/v1-grouped-trend-widget)
