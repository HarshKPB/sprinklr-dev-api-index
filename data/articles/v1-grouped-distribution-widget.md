---
title: "Grouped Distribution Widget"
slug: v1-grouped-distribution-widget
url: https://dev.sprinklr.com/v1-grouped-distribution-widget
---

# Grouped Distribution Widget

# POST Grouped Distribution Widget

This widget is used to get data with two group-bys - outer and inner. Response type is `GroupedDistributionResponse`.

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

## Example 1: Volume Distribution by Topic by Source

This returns the number of mentions grouped by Topic and then by Source.




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
        "widgetType": "GROUPED_DISTRIBUTION",
        "dimension": "TOPIC",
        "otherDimension": "MEDIA_SOURCE"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        },
        {
            "dimension": "MEDIA_SOURCE",
            "filterValues": [
                "FACEBOOK",
                "TWITTER"
            ]
        }
    ],
    "metric": "MENTIONS"
}'




### Response




{
    "status": "SUCCESS",
    "response": [
        {
            "term": "Sprinklr",
            "id": "595c50dbe4b064e21f85d074",
            "count": 17908,
            "groupedTerms": [
                {
                    "word": "Twitter",
                    "id": "TWITTER",
                    "count": 17882,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "Facebook",
                    "id": "FACEBOOK",
                    "count": 26,
                    "values": {},
                    "additional": {}
                }
            ],
            "timeZoneOffset": 0,
            "cacheHit": false
        }
    ]
}



## Example 2: Positive and Negative Sentiments in Mentions across Sources

This returns the number of mentions grouped by Source, followed by Sentiment.




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
        "widgetType": "GROUPED_DISTRIBUTION",
        "dimension": "MEDIA_SOURCE",
        "otherDimension": "SENTIMENT"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        },
        {
            "dimension": "MEDIA_SOURCE",
            "filterValues": [
                "FACEBOOK",
                "TWITTER"
            ]
        }
    ],
    "metric": "MENTIONS"
}'




### Response




{
    "status": "SUCCESS",
    "response": [
        {
            "term": "Twitter",
            "id": "TWITTER",
            "count": 17882,
            "groupedTerms": [
                {
                    "word": "Neutral",
                    "id": "neu",
                    "count": 8936,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "Positive",
                    "id": "pos",
                    "count": 7392,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "Negative",
                    "id": "neg",
                    "count": 472,
                    "values": {},
                    "additional": {}
                }
            ],
            "timeZoneOffset": 0,
            "cacheHit": false
        },
        {
            "term": "Facebook",
            "id": "FACEBOOK",
            "count": 26,
            "groupedTerms": [
                {
                    "word": "Neutral",
                    "id": "neu",
                    "count": 20,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "Negative",
                    "id": "neg",
                    "count": 3,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "Positive",
                    "id": "pos",
                    "count": 2,
                    "values": {},
                    "additional": {}
                }
            ],
            "timeZoneOffset": 0,
            "cacheHit": false
        }
    ]
}



## Example 3: Word cloud across topics.

This returns the word cloud across different topics specified in filter.




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
        "widgetType": "GROUPED_DISTRIBUTION",
        "dimension": "TOPIC",
        "otherDimension": "WORD_CLOUD_OVERALL",
        "otherDimensionRows": 50
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        },
        {
            "dimension": "MEDIA_SOURCE",
            "filterValues": [
                "FACEBOOK",
                "TWITTER"
            ]
        }
    ],
    "metric": "MENTIONS"
}'



## Example - Response



{
    "status": "SUCCESS",
    "response": [
        {
            "term": "Sprinklr",
            "id": "595c50dbe4b064e21f85d074",
            "count": 17908,
            "groupedTerms": [
                {
                    "word": "switch",
                    "id": "switch",
                    "count": 644,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "smart",
                    "id": "smart",
                    "count": 604,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "deserve",
                    "id": "deserve",
                    "count": 600,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "matches",
                    "id": "matches",
                    "count": 600,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "choices",
                    "id": "choices",
                    "count": 599,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "realizes",
                    "id": "realizes",
                    "count": 599,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "good",
                    "id": "good",
                    "count": 595,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "driving",
                    "id": "driving",
                    "count": 569,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "drivers",
                    "id": "drivers",
                    "count": 551,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "data",
                    "id": "data",
                    "count": 536,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "sprinklr",
                    "id": "sprinklr",
                    "count": 509,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "clear",
                    "id": "clear",
                    "count": 471,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "believes",
                    "id": "believes",
                    "count": 465,
                    "values": {},
                    "additional": {}
                },
                {
                    "word": "billing",
                    "id": "billing",
                    "count": 465,
                    "values": {},
                    "additional": {}
                }
            ],
            "timeZoneOffset": 0,
            "cacheHit": false
        }
    ]
}



[](https://dev.sprinklr.com/v1-grouped-distribution-widget) 

 

 
[Back to top](https://dev.sprinklr.com/v1-grouped-distribution-widget)
