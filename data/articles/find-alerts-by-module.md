---
title: "Find Alerts by Module"
slug: find-alerts-by-module
url: https://dev.sprinklr.com/find-alerts-by-module
---

# Find Alerts by Module

# GET Find Alerts by Module
  

This API allows you to fetch details on all Listening Alerts in your environment.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/alert-manager/find/LISTENING

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

## Example - Request to Create Static Listening Alert

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/alert-manager/find/LISTENING' \
--header 'Authorization: Bearer {token} ' \
--header 'Key: {API_Key}' \
--header 'content-type: application/json' \
--header 'accept: application/json' \

## Example - Response


{
    "data": [
        {
            "id": "5e7507b757e63326c10c0bfc",
            "name": "test2",
            "category": "SMART_ALERT",
            "module": "LISTENING",
            "status": "FAILED",
            "filterDimensions": [
                {
                    "dimensionName": "TOPIC_IDS",
                    "filterType": "IN",
                    "values": [],
                    "details": {
                        "filterMetadata": {
                            "reportName": "SPRINKSIGHTS",
                            "cfName": "TOPIC_IDS",
                            "name": "TOPIC_IDS",
                            "displayName": "Topic",
                            "uniqueKey": "D_TOPIC_IDS",
                            "additional": {
                                "dF": true,
                                "OLD_DIM_NAME": "TOPIC",
                                "nameQueryLookupSupported": "true",
                                "DRILLDOWN": false,
                                "supportedMediaCSV": "PRINT,FACEBOOK,FORUMS,TV,INSTAGRAM,REDDIT,QUORA,WORDPRESS,REVIEWS,YOUTUBE,CLASSIFIED,BLOGS,VK,NEWS,SINA_WEIBO,RADIO,PODCAST,VIDEOS,TWITTER",
                                "EXIST_FILTER": false
                            }
                        }
                    }
                }
            ],
            "enabled": true,
            "distributionConfig": {
                "emailIds": [
                    "vibhav.sharma@sprinklr.com"
                ],
                "sendEmailNotification": true
            },
            "smartAlertConfig": {
                "smartAlertMetrics": [
                    "MENTIONS_COUNT"
                ],
                "suddenAnomalyEnabled": true,
                "longTermTrendsEnabled": true
            },
            "createdTime": 1598524121478,
            "modifiedTime": 1752311403726,
            "ownerUserId": 1000073627,
            "lastModifiedUserId": -100,
            "clientId": 1000004509
        },
        {
            "id": "5e7733ab2bfcc43f52b56a91",
            "name": "test language",
            "category": "SMART_ALERT",
            "module": "LISTENING",
            "status": "NEW",
            "filterDimensions": [
                {
                    "dimensionName": "LST_SUPP_LNG",
                    "filterType": "IN",
                    "values": [
                        "en"
                    ],
                    "details": {
                        "filterMetadata": {
                            "reportName": "SPRINKSIGHTS",
                            "cfName": "LST_SUPP_LNG",
                            "name": "LST_SUPP_LNG",
                            "displayName": "Language",
                            "uniqueKey": "D_LST_SUPP_LNG",
                            "additional": {
                                "OLD_DIM_NAME": "LANGUAGE",
                                "nameQueryLookupSupported": "true",
                                "supportedMediaCSV": "PRINT,FACEBOOK,FORUMS,TV,INSTAGRAM,REDDIT,QUORA,WORDPRESS,REVIEWS,YOUTUBE,CLASSIFIED,BLOGS,VK,NEWS,SINA_WEIBO,RADIO,PODCAST,VIDEOS,TWITTER"
                            }
                        }
                    }
                },
                {
                    "dimensionName": "TOPIC_IDS",
                    "filterType": "IN",
                    "values": [],
                    "details": {
                        "filterMetadata": {
                            "reportName": "SPRINKSIGHTS",
                            "cfName": "TOPIC_IDS",
                            "name": "TOPIC_IDS",
                            "displayName": "Topic",
                            "uniqueKey": "D_TOPIC_IDS",
                            "additional": {
                                "dF": true,
                                "OLD_DIM_NAME": "TOPIC",
                                "nameQueryLookupSupported": "true",
                                "DRILLDOWN": false,
                                "supportedMediaCSV": "PRINT,FACEBOOK,FORUMS,TV,INSTAGRAM,REDDIT,QUORA,WORDPRESS,REVIEWS,YOUTUBE,CLASSIFIED,BLOGS,VK,NEWS,SINA_WEIBO,RADIO,PODCAST,VIDEOS,TWITTER",
                                "EXIST_FILTER": false
                            }
                        }
                    }
                }
            ],
            "enabled": false,
            "distributionConfig": {
                "userIds": [
                    1000073627
                ],
                "emailIds": [
                    "vibhav.sharma@sprinklr.com"
                ],
                "sendEmailNotification": true
            },
            "smartAlertConfig": {
                "smartAlertMetrics": [
                    "MENTIONS_COUNT",
                    "LISTENING_RETWEETS"
                ],
                "suddenAnomalyEnabled": true,
                "longTermTrendsEnabled": true
            },
            "createdTime": 1584995335415,
            "modifiedTime": 1737711838247,
            "ownerUserId": 1000073627,
            "lastModifiedUserId": 0,
            "clientId": 1000004509
        }
 ],
  "errors": []
}

## Response Schema













  ````
  ``
  ``````











    ````





| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| id |  | string | Unique identifier of the listening alert. |
| name |  | string | Name of the Alert. |
| description |  | string | Description provided for the Alert. |
| category |  | string | Type of alert. Values include SMART_ALERT or STATIC_ALERT. |
| module |  | string | It will be LISTENING. |
| status |  | string | Shows the current status of the Alert (IN_PROGRESS, SUCCESS, or FAILED). |
| filterDimensions |  | Array of Objects | Details of the filters and dimensions applied to the alert. |
|  | dimensionName | string | Name of the dimension. |
|  | filterType | string | Filter type applied. |
|  | values | Array | Values used for filtering. |
|  | details | Object | Metadata about the filter dimension. |
| tags |  | Array | Shows the selected tag(s) for the Alert. |
| enabled |  | Boolean | Shows if the Alert is enabled or disabled. |
| distributionConfig |  | Object | Provides information about how the Alert is delivered, including the list of recipients and the channels used to notify them. |
|  | userIds | Array of Integer | Shows the Sprinklr User(s) who will receive notifications on the Alert. |
|  | userGroupIds | Array of Integer | Shows the Sprinklr User Group(s) who will receive notifications on the Alert. |
|  | emailIds | Array of String | Shows the external email addresses who will receive notifications on the Alert. |
|  | sendEmailNotification | Boolean | Indicates whether an email notification will be sent for the Alert. Possible values are true or false. |
|  | customEmailSubject | String | Refers to the subject line of the email notification sent for the Alert. |
|  | senderAlias | String | Shows the email address used to send the Alert notification. |
| smartAlertConfig |  | Object | Defines the configuration that determines when alerts will be triggered. |
|  | smartAlertMetrics | Array of String | Refer to the metric used to determine whether an alert should be triggered. |
|  | suddenAnomalyEnabled | Boolean | Refers to alerts on anomalies identified over shorter time frames (minutes/hourly level). |
|  | longTermTrendsEnabled | Boolean | Alerts on anomalies identified over longer time frames (daily/weekly level). |
| createdTime |  | Integer | Shows the epoch timestamp when the Alert was created. |
| modifiedTime |  | Integer | Shows the epoch timestamp when the Alert was last modified. |
| ownerUserId |  | Integer | Shows the Sprinklr User ID of the creator of the Alert. |
| lastModifiedUserId |  | Integer | User ID of the last person who modified the alert. |
| clientId |  | Integer | Sprinklr client ID associated with the alert. |

[](https://dev.sprinklr.com/find-alerts-by-module)

[Back to top](https://dev.sprinklr.com/find-alerts-by-module)
