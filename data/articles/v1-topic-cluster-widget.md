---
title: "Topic Cluster Widget"
slug: v1-topic-cluster-widget
url: https://dev.sprinklr.com/v1-topic-cluster-widget
---

# Topic Cluster Widget

# POST Topic Cluster Widget

You can use this API to fetch the Topic Cluster widget. You can even use `TOPIC`, `THEMES` and `KEYWORD_LIST` in filters to fetch the required response.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/listening/query/widget

### Topic Cluster

This returns the daily reach grouped by Topic.

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

## Request Parameters

The following table describes the Request Parameters in use.




































































































| Fields | Required | Type | Description |
| --- | --- | --- | --- |
| sinceTime | Required | Long | start time of the time range in milliseconds |
| untilTime | Required | Long | end time of the time range in milliseconds |
| timeField | Optional | String | Set the type of time range (sinceTime + untilTill) to use. It takes either 				"SYSTEM_CREATED_TIME": The time message is created on Sprinklr 				"SN_CREATED_TIME": The time message is created on social network (default) |
| timezoneOffset | Required | Long | The timezone UTC offset in milliseconds. Default offset set to 0 for UTC based time. e.g.  EST timezone -5 UTC it will be -(5*60*60*1000) |
| details | Required | WidgetDetails | The details for the widget. |
| filters | Required | List<WidgetFilter> | The filters applied to the widget. |
| metric | Required | WidgetMetricType | The metric type for the widget; MENTIONS (default), REACH |
| trendAggregationPeriod | Optional | TrendAggregationPeriod | The trend aggregate period; applicable for TREND and GROUPED_TREND Widget  				{HOUR, DAY, WEEK, MONTH, QUARTER, YEAR} |
| start | Optional | int | starting page number; default=0; applicable for only STREAM Widget |
| rows | Optional | int | max number of items in the page; default=20; applicable for only STREAM |
| echoRequest | Optional | boolean | flag to state where to get back request in response object. |
| tag | Optional | String | A state parameter. It can be used as version attached with the response. It will remain unchanged from api and will be returned as it is. |
| sortKey | Optional | String | It can take 3 values -  				‘SYSTEM_CREATED_TIME’ - system created time 				‘CREATED_TIME’ - social network created time 				‘MODIFIED_TIME’ - modified time 				It sorts the response messages based upon the specified field. by default it sorts the response message based upon CREATED_TIME |
| messageFormatOptions | Optional | String | Comma delimit format values = {strip_html, text strip_url, include_original} 				strip_html - Strip html from the message text 				strip_url - Strip Urls from the message text 				include_original - Include the original text as well in the field "originalText" |

### Example - Request



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
        "widgetType": "TOPIC_CLUSTER"
    },
   "metric" : "REACH",
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "5f7ec8f17ca3ef034edaf372"
            ]
        },
        {
            "dimension": "THEMES",
            "filterValues": [
                "5f50f271705193346ba6cf5c"]
        },
        {
            "dimension": "LST_KEYWORD_LIST",
            "filterValues": [
                "5ee70691173df121293e98f7"]
        }
    ],
    "start": 0,
    "rows": 10,
    "timezoneOffset": 14400000
}'



### Example - Response




{
    "status": "SUCCESS",
    "response": {
        "groups": [
            {
                "id": "India",
                "label": "India",
                "weight": 100,
                "groups": [
                    {
                        "id": "Covid Cases India",
                        "label": "Covid Cases",
                        "weight": 100,
                        "groups": []
                    },
                    {
                        "id": "COVID-19 Pandemic with India India",
                        "label": "COVID-19 Pandemic with India",
                        "weight": 93,
                        "groups": []
                    }
                ]
            },
            {
                "id": "COVID-19",
                "label": "COVID-19",
                "weight": 93,
                "groups": []
            },
            {
                "id": "Support",
                "label": "Support",
                "weight": 79,
                "groups": []
            },
            {
                "id": "Air",
                "label": "Air",
                "weight": 67,
                "groups": []
            },
            {
                "id": "Money",
                "label": "Money",
                "weight": 67,
                "groups": []
            },
            {
                "id": "Covid",
                "label": "Covid",
                "weight": 65,
                "groups": [
                    {
                        "id": "Flattening of Curve, Total Cases Covid",
                        "label": "Flattening of Curve, Total Cases",
                        "weight": 100,
                        "groups": []
                    },
                    {
                        "id": "Country Covid",
                        "label": "Country",
                        "weight": 72,
                        "groups": []
                    },
                    {
                        "id": "Govt Covid",
                        "label": "Govt",
                        "weight": 72,
                        "groups": []
                    }
                ]
            }
        ]
    }
}



[](https://dev.sprinklr.com/v1-topic-cluster-widget) 

 

 
[Back to top](https://dev.sprinklr.com/v1-topic-cluster-widget)
