---
title: "Listening Widget"
slug: v1-listening-widget
url: https://dev.sprinklr.com/v1-listening-widget
---

# Listening Widget

#  Listening Widget

Listening Dashboard Widgets are customizable widgets that you can add to a Listening Dashboard to visualize data. They allow you to engage with relevant data sets and help you listen, learn, and act on critical developments in real-time. At a time, you can add single or multiple widgets to a Listening dashboard.
The primary purpose of adding a widget on a Listening dashboard is to visualize data insightfully. You can translate large data sets and metrics into graphs, charts, and other visuals by adding customizable widgets. As a result, the visual representation of data makes it easier to identify and share real-time trends, outliers, and new insights about the information represented in the widget.

**Related Knowledge Base Article:** **[Create Listening Dashboard Widgets](https://www.sprinklr.com/help/articles/custom-listening-dashboards/create-custom-listening-dashboards/645cfd4b0104980882a5abc7)**

## Request Parameters






































      [WidgetDetails](https://dev.sprinklr.com/v1-listening-widget#widget_details)





      [WidgetFilter](https://dev.sprinklr.com/v1-listening-widget#widget_filter)









































| Fields | Required | Type | Description |
| --- | --- | --- | --- |
| sinceTime | Optional | Long | start time of the time range in milliseconds |
| untilTime | Optional | Long | end time of the time range in milliseconds |
| timeField | Optional | String | Set the type of time range (sinceTime + untilTill) to use. It takes either         "SYSTEM_CREATED_TIME": The time message is created on Sprinklr         "SN_CREATED_TIME": The time message is created on social network (default) |
| timezoneOffset | Optional | Long | The timezone UTC offset in milliseconds. Default offset set to 0 for UTC based time. e.g.  EST timezone -5 UTC it will be -(5*60*60*1000) |
| details | Required |  | The details for the widget. |
| filters | Optional | List<> | The filters applied to the widget. |
| metric | Optional | WidgetMetricType | The metric type for the widget; MENTIONS (default), REACH |
| trendAggregationPeriod |  | TrendAggregationPeriod | The trend aggregate period; applicable for TREND and GROUPED_TREND Widget        {HOUR, DAY, WEEK, MONTH, QUARTER, YEAR} |
| start | Optional | int | starting page number; default=0; applicable for only STREAM Widget |
| rows | Optional | int | max number of items in the page; default=100; applicable for only STREAM |
| echoRequest | Optional | boolean | flag to state whete to get back request in response object. |
| tag | Optional | String | A state parameter. It can be used as version attached with the response. It will remain unchanged from api and will be returned as it is. |

## WidgetDetails

WidgetDetails object is used to select the widget and specify any group-by information (if applicable).










      [WidgetType](https://dev.sprinklr.com/v1-listening-widget#widget_type)
























| Fields | Type | Description |
| --- | --- | --- |
| widgetType* |  | The type of widget. |
| subType | String | secondary widgetType, optional |
| dimension | Dimension | The outer group-by. |
| otherDimension | Dimension | The inner group-by. |
| customFieldName | String | Name of custom field. Only required if Dimension is one of the following : MESSAGE_PARTNER_CUSTOM_FIELDS MESSAGE_CLIENT_CUSTOM_FIELDS PROFILE_PARTNER_CUSTOM_FIELDS PROFILE_CLIENT_CUSTOM_FIELDS |

## WidgetFilter

The list of WidgetFilter object is used to specify any filtering configurations. Please note that when TOPIC is used as a filter, a maximum of 10 topics may be specified per request.



























| Fields | Type | Description |
| --- | --- | --- |
| dimension | Dimension | The field on which filtering must be made. |
| filterValues | List<String> | The values of the filter. |
| customFieldName | String | Name of custom field. Only required if Dimension is one of the following : MESSAGE_PARTNER_CUSTOM_FIELDS MESSAGE_CLIENT_CUSTOM_FIELDS PROFILE_PARTNER_CUSTOM_FIELDS PROFILE_CLIENT_CUSTOM_FIELDS |

## WidgetType

The currently supported widgetTypes are:









      [DISTRIBUTION](https://dev.sprinklr.com/v1-distribution-widget)



      [GROUPED_DISTRIBUTION](https://dev.sprinklr.com/v1-grouped-distribution-widget)



      [TREND](https://dev.sprinklr.com/v1-trend-widget)



      [GROUPED_TREND](https://dev.sprinklr.com/v1-grouped-trend-widget)



      [USERS](https://dev.sprinklr.com/v1-users-widget)



      [TOPIC_CLUSTER](https://dev.sprinklr.com/v1-topic-cluster-widget)




| WidgetType | Return type |
| --- | --- |
|  | DistributionResponse |
|  | GroupedDistributionResponse |
|  | TrendResponse |
|  | GroupedTrendResponse |
|  | UsersResponse |
|  | TopicClusterResponse |

## Dimension

The dimension keys which are supported for performing the queries.






















































































































| Dimension | Description |
| --- | --- |
| TOPIC_GROUP | Sprinklr's categorization for topics. Every topic is a member of exactly one topic group. *As of April 30, 2016, this field can no longer be used as a filter in Widget Query or Stream requests. |
| TOPIC | The listening topic query. Topic queries are used by Sprinklr to fetch data from its data providers. |
| SENTIMENT | Sentiment of the message - Positive, Neutral, or Negative. Sentiment is currently supported forthe following languages: Arabic, Chinese, Dutch, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish. |
| MEDIA_SOURCE | The source of the message. |
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

## Response

All responses follow the same structure.































| Fields | Type | Description |
| --- | --- | --- |
| status | String | SUCCESS or FAILED |
| response | <depending on actual widget> | This depends on the actual widget request |
| failureMessage | String | Failure message in case of status=FAILED |
| errorCode | String | Error code in case of status=FAILED |

[](https://dev.sprinklr.com/v1-listening-widget) 

 

 
[Back to top](https://dev.sprinklr.com/v1-listening-widget)
