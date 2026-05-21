---
title: "Distribution Widget v1"
slug: v1-distribution-widget
url: https://dev.sprinklr.com/v1-distribution-widget
---

# Distribution Widget v1

# POST Distribution Widget

This widget is used for gathering data with single groupBy value. The group-by can be done on any Dimension. See Dimension for a list of supported dimensions. Response type is DistributionResponse.

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters

****

| Parameter | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| sinceTime |  | Optional | start time of the time range | Epoch |
| untilTime |  | Optional | end time of the time range | Epoch |
| details |  | Required | Object containing the widget details | Object |
|  | widgetType | Required | Refers to the type of the widgetSupported widget types:DISTRIBUTION, GROUPED_DISTRIBUTION, TREND, GROUPED_TREND, USERS, TOPIC_CLUSTER | String |
|  | dimension | Required | Refers to the type of dimension.Refer to the table below for supported dimension types | String |
| filters |  | Optional | Object containing the filter details that you want to apply on the widget | Object |
|  | dimension | Optional | Refers to the field on which the filtering needs to be applied | String |
|  | filterValues | Optional | The list of values for the given dimension type | List[String] |
|  | customFieldName | Optional | Refers to the name of the custom fieldOnly required if Dimension is one of the following:MESSAGE_PARTNER_CUSTOM_FIELDS MESSAGE_CLIENT_CUSTOM_FIELDS PROFILE_PARTNER_CUSTOM_FIELDS PROFILE_CLIENT_CUSTOM_FIELDS | String |
| metric |  | Optional | The metric type for the widgetSupported Values:MENTIONS (default), REACH | String |

## Dimension

The dimension keys which are supported for performing the queries.






















      [Media Source](https://dev.sprinklr.com/listening-v1/)































































































| Dimension | Description |
| --- | --- |
| TOPIC_GROUP | Sprinklr's categorization for topics. Every topic is a member of exactly one topic group. *As of April 30, 2016, this field can no longer be used as a filter in Widget Query or Stream requests. |
| TOPIC | The listening topic query. Topic queries are used by Sprinklr to fetch data from its data providers. |
| SENTIMENT | Sentiment of the message - Positive, Neutral, or Negative. Sentiment is currently supported forthe following languages: Arabic, Chinese, Dutch, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish. |
| MEDIA_SOURCE | The source of the message. See  for a list of sources. |
| LANGUAGE | The language of the message, as identified by Sprinklr or its data providers. |
| GEO_COUNTRY | The user-provided or Sprinklr-identified country of origin of the message. |
| GEO_STATE | The user-provided or Sprinklr-identified state of origin of the message. |
| GEO_CITY | The user-provided or Sprinklr-identified city of origin of the message. |
| GENDER | Gender of the sender - Male or Female. Gender is not available for all messages. |
| WORD_CLOUD_OVERALL | Terms used within the title or body of a message, weighted by frequency of use. |
| WORD_CLOUD_HASH_TAGS | Hashtags used within the title or body of a message, weighted by frequency of use. |
| WORD_CLOUD_PRODUCTS | Products mentioned within the title or body of a message, weighted by frequency of use. |
| DOMAIN | The domain name of a message's website of origin. |
| LINKS | URLs used within the body of a message. |
| USER_ID | Dimension for filtering by user id. Can only be used in WidgetFilter. The values in WidgetFilter.filterValues should be in format of “<media source>:<user-id>”. For example, “TWITTER:18806338” |
| USER_SCREEN_NAME | Dimension for filtering by user screen name. Can only be used in WidgetFilter. The values in WidgetFilter.filterValues should be in format of “<media source>:<user-screen-name>”. For example, “TWITTER:barackobama” |
| MESSAGE_PARTNER_CUSTOM_FIELDS | Custom labels that can be applied to messages for more granular categorization. Partner custom fields can be viewed across all clients within a Sprinklr partner. Can be used to group and filter. |
| MESSAGE_CLIENT_CUSTOM_FIELDS | Custom labels that can be applied to messages for more granular categorization. Client custom fields can be viewed across particular clients. Can be used to group and filter. |
| PROFILE_PARTNER_CUSTOM_FIELDS | Custom labels that can be applied to message authors for more granular categorization. Partner custom fields can be viewed across all clients within a Sprinklr partner. Can be used to group and filter. |
| PROFILE_CLIENT_CUSTOM_FIELDS | Custom labels that can be applied to message authors for more granular categorization. Client custom fields can be viewed across particular clients. Can be used to group and filter. |
| MESSAGE_PRIORITY | Workflow-level dimension set by Sprinklr users indicating the priority of a message. |
| MESSAGE_TAGS | Workflow-level dimension applied by Sprinklr users. Message tags are freeform strings that can be applied to one or more messages. |
| MESSAGE_STATUS | Workflow-level dimension set by Sprinklr users indicating the status of a message. |
| MESSAGE_ASSIGNED_TO | Workflow-level dimension indicating to whom a message has been assigned. |
| MESSAGE_ASSIGNED_BY | Workflow-level dimension indicating who has assigned a message to another user. |
| PARTNER_QUEUES | Workflow-level dimension indicating the queue to which a message has been assigned. Partner queues can be used across a Sprinklr partner. |
| CLIENT_QUEUES | Workflow-level dimension indicating the queue to which a message has been assigned. Client queues can be used within clients. |

## Example 1: Sentiment Analysis

This returns the number of mentions grouped by Sentiment values.




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "sinceTime": 1488034511000,
    "untilTime": 1490972111000,
    "details": {
        "widgetType": "DISTRIBUTION",
        "dimension": "SENTIMENT"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
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
            "word": "Positive",
            "id": "pos",
            "count": 16,
            "values": {},
            "additional": {}
        },
        {
            "word": "Neutral",
            "id": "neu",
            "count": 16,
            "values": {},
            "additional": {}
        },
        {
            "word": "Negative",
            "id": "neg",
            "count": 1,
            "values": {},
            "additional": {}
        }
    ]
}



## Example 2: Volume Distribution By Source

This returns the number of mentions grouped by Source.

## MENTIONS




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "sinceTime": 1488034511000,
    "untilTime": 1490972111000,
    "details": {
        "widgetType": "DISTRIBUTION",
        "dimension": "MEDIA_SOURCE"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
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
            "word": "Twitter",
            "id": "TWITTER",
            "count": 21,
            "values": {},
            "additional": {}
        },
        {
            "word": "Blogs/Websites",
            "id": "BLOGS",
            "count": 9,
            "values": {},
            "additional": {}
        },
        {
            "word": "Facebook",
            "id": "FACEBOOK",
            "count": 2,
            "values": {},
            "additional": {}
        },
        {
            "word": "News",
            "id": "NEWS",
            "count": 2,
            "values": {},
            "additional": {}
        }
    ]
}



## REACH




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "sinceTime": 1488034511000,
    "untilTime": 1490972111000,
    "details": {
        "widgetType": "DISTRIBUTION",
        "dimension": "MEDIA_SOURCE"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        }
    ],
    "metric": "REACH"
}'



## Example - Response



{
    "status": "SUCCESS",
    "response": [
        {
            "word": "Twitter",
            "id": "TWITTER",
            "count": 48234,
            "values": {},
            "additional": {}
        },
        {
            "word": "Facebook",
            "id": "FACEBOOK",
            "count": 0,
            "values": {},
            "additional": {}
        },
        {
            "word": "Flickr",
            "id": "FLICKR",
            "count": 0,
            "values": {},
            "additional": {}
        },
        {
            "word": "Disqus",
            "id": "DISQUS",
            "count": 0,
            "values": {},
            "additional": {}
        }
        {
            "word": "Instagram",
            "id": "INSTAGRAM",
            "count": 0,
            "values": {},
            "additional": {}
        },
        {
            "word": "Sina Weibo",
            "id": "SINA_WEIBO",
            "count": 0,
            "values": {},
            "additional": {}
        },
        {
            "word": "Tencent Weibo",
            "id": "TENCENT_WEIBO",
            "count": 0,
            "values": {},
            "additional": {}
        }
    ]
}



## Example 3: Share of Voice

This returns the number of mentions grouped by Topic.




 Copy Code



curl -X POST \
  'https://api2.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "sinceTime": 1488034511000,
    "untilTime": 1490972111000,
    "details": {
        "widgetType": "DISTRIBUTION",
        "dimension": "TOPIC"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074, 595b8b78e4b00bd3a9a9c30a, 5a7aa09ee4b03f7741067b5d"
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
            "word": "Sprinklr",
            "id": "595c50dbe4b064e21f85d074",
            "count": 23,
            "values": {},
            "additional": {}
        },
        {
            "word": "Hashtag Inquiry",
            "id": "595b8b78e4b00bd3a9a9c30a",
            "count": 0,
            "values": {},
            "additional": {}
        },
        {
            "word": "Location Based Topic",
            "id": "5a7aa09ee4b03f7741067b5d",
            "count": 0,
            "values": {},
            "additional": {}
        }
    ]
}



## Example 4: Gender Analysis






 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "sinceTime": 1488034511000,
    "untilTime": 1490972111000,
    "details": {
        "widgetType": "DISTRIBUTION",
        "dimension": "GENDER"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074, 595b8b78e4b00bd3a9a9c30a, 5a7aa09ee4b03f7741067b5d"
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
            "word": "Male",
            "id": "MALE",
            "count": 12143,
            "values": {},
            "additional": {}
        },
        {
            "word": "Female",
            "id": "FEMALE",
            "count": 1501,
            "values": {},
            "additional": {}
        }
    ]
}



## Example 5: Top Words

Use Dimension WORD_CLOUD_OVERALL.




 Copy Code



curl -X POST \
  'https://api2.sprinklr.com/{{env}}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {{apikey}}' \
  -d '{
    "sinceTime": 1530417600000,
    "untilTime": 1547499885487,
    "details": {
        "widgetType": "DISTRIBUTION",
        "dimension": "WORD_CLOUD_OVERALL"
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
            "word": "auto",
            "id": "auto",
            "count": 11308,
            "values": {},
            "additional": {}
        },
        {
            "word": "visit",
            "id": "visit",
            "count": 10543,
            "values": {},
            "additional": {}
        },
        {
            "word": "insurance",
            "id": "insurance",
            "count": 9120,
            "values": {},
            "additional": {}
        },
        {
            "word": "today",
            "id": "today",
            "count": 8195,
            "values": {},
            "additional": {}
        },
        {
            "word": "complicated",
            "id": "complicated",
            "count": 7114,
            "values": {},
            "additional": {}
        },
        {
            "word": "don",
            "id": "don",
            "count": 6661,
            "values": {},
            "additional": {}
        },
        {
            "word": "simplicity",
            "id": "simplicity",
            "count": 6654,
            "values": {},
            "additional": {}
        },
        {
            "word": "expensive",
            "id": "expensive",
            "count": 6652,
            "values": {},
            "additional": {}
        },
        {
            "word": "savings",
            "id": "savings",
            "count": 6652,
            "values": {},
            "additional": {}
        },
        {
            "word": "enjoying",
            "id": "enjoying",
            "count": 6650,
            "values": {},
            "additional": {}
        },
        {
            "word": "quote",
            "id": "quote",
            "count": 6650,
            "values": {},
            "additional": {}
        },
        {
            "word": "started",
            "id": "started",
            "count": 2397,
            "values": {},
            "additional": {}
        },
        {
            "word": "save",
            "id": "save",
            "count": 2392,
            "values": {},
            "additional": {}
        },
        {
            "word": "money",
            "id": "money",
            "count": 2382,
            "values": {},
            "additional": {}
        },
        {
            "word": "policy",
            "id": "policy",
            "count": 2380,
            "values": {},
            "additional": {}
        },
        {
            "word": "experience",
            "id": "experience",
            "count": 1914,
            "values": {},
            "additional": {}
        },
        {
            "word": "easy",
            "id": "easy",
            "count": 1767,
            "values": {},
            "additional": {}
        },
        {
            "word": "years",
            "id": "years",
            "count": 1378,
            "values": {},
            "additional": {}
        }
    ]
}



## Example 6: Top Hashtags

Use Dimension WORD_CLOUD_HASHTAGS.





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
        "widgetType": "DISTRIBUTION",
        "dimension": "WORD_CLOUD_HASHTAGS"
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
            "word": "#ai",
            "id": "#ai",
            "count": 248,
            "values": {},
            "additional": {}
        },
        {
            "word": "#vmworld",
            "id": "#vmworld",
            "count": 210,
            "values": {},
            "additional": {}
        },
        {
            "word": "#analyticsx",
            "id": "#analyticsx",
            "count": 200,
            "values": {},
            "additional": {}
        },
        {
            "word": "#analytics",
            "id": "#analytics",
            "count": 177,
            "values": {},
            "additional": {}
        },
        {
            "word": "#cloud",
            "id": "#cloud",
            "count": 170,
            "values": {},
            "additional": {}
        },
        {
            "word": "#iot",
            "id": "#iot",
            "count": 152,
            "values": {},
            "additional": {}
        },
        {
            "word": "#socialmedia",
            "id": "#socialmedia",
            "count": 142,
            "values": {},
            "additional": {}
        }
    ]
}



## Example 7: Distribution of Mentions by Location

Use Dimension GEO_COUNTRY.




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
        "widgetType": "DISTRIBUTION",
        "dimension": "GEO_COUNTRY"
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
            "word": "Unknown",
            "id": "UN",
            "count": 13243,
            "values": {},
            "additional": {}
        },
        {
            "word": "United States",
            "id": "US",
            "count": 2990,
            "values": {},
            "additional": {}
        },
        {
            "word": "United Kingdom",
            "id": "GB",
            "count": 425,
            "values": {},
            "additional": {}
        },
        {
            "word": "Canada",
            "id": "CA",
            "count": 290,
            "values": {},
            "additional": {}
        }
    ]
}



## Example 8: Groupby custom field




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
        "widgetType": "DISTRIBUTION",
        "dimension": "MESSAGE_CLIENT_CUSTOM_FIELDS",
        "customFieldName": "PICKLIST"
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
      "word": "valid",
      "id": "valid",
      "count": 5,
      "values": {
      },
      "additional": {
      }
    },
    {
      "word": "invalid",
      "id": "invalid",
      "count": 2,
      "values": {
      },
      "additional": {
      }
    }
  ]
}



## Example 9: Group by PARTNER_QUEUES (Workflow property)




 Copy Code



curl -X POST \
  'https://api2.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {{apikey}}' \
  -d '{
    "sinceTime": 1530417600000,
    "untilTime": 1547499885487,
    "details": {
        "widgetType": "DISTRIBUTION",
        "dimension": "PARTNER_QUEUES"
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
      "word": "Auto_Part01",
      "id": "28",
      "count": 44,
      "values": {
      },
      "additional": {
      }
    }
  ]
}



[](https://dev.sprinklr.com/v1-distribution-widget) 

 

 
[Back to top](https://dev.sprinklr.com/v1-distribution-widget)
