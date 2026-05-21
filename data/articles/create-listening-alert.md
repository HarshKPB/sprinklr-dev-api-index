---
title: "Create Listening Alert"
slug: create-listening-alert
url: https://dev.sprinklr.com/create-listening-alert
---

# Create Listening Alert

#  POST  Create Listening Alert API

The Create Listening Alert API allows you to configure alerts that monitor specific topics or dimensions in Sprinklr Listening. This API supports two types of alerts:


- Static (Threshold) Alert: Triggers when defined conditions—such as mention volume—cross a specified threshold within a given time interval.

- Smart Alert: Uses anomaly detection to identify unusual spikes or trends based on selected listening metrics.

Use this API to automate alert creation for real-time monitoring, enabling faster response to critical events or shifts in conversation.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/alert-manager

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

## Request Body - Create Static Listening Alert























      ``






      ``













      ``






      ``




















      ``




















      ``



























      ``













      ``



| Parameter | Sub Parameter | Type | Required / Optional | Description |
| --- | --- | --- | --- | --- |
| name |  | string | Required | Name of the alert. Appears in the UI and email subject unless overridden by customEmailSubject. |
| category |  | string | Required | Alert type. Use STATIC_ALERT for static listening alerts. |
| module |  | string | Required | Product module. Use LISTENING for listening alerts. |
| filterDimensions |  | array of objects | Required | Dimensions and filters that define the alert scope. |
|  | dimensionName | string | Required | Name of the dimension to filter on. Example: TOPIC_IDS. |
|  | filterType | string | Required | Type of filter. Example: IN. |
|  | values | array | Required | Values to match against the specified dimension. |
| tags |  | array of string | Optional | Tags used for internal classification of the alert. |
| enabled |  | boolean | Required | Enables the alert when set to true. |
| distributionConfig |  | object | Required | Configuration for email notification delivery. |
|  | emailIds | array of string | Required | List of email addresses to notify when alert is triggered. |
|  | sendEmailNotification | boolean | Required | Enables email notifications when set to true. |
|  | customEmailSubject | string | Optional | Custom subject line for the alert email. Overrides default alert name. |
|  | senderAlias | string | Optional | Email alias shown as the sender of the alert email. |
| volumetricAlertConfig |  | object | Required | Configuration for threshold-based alerting logic. |
|  | alertTriggerConditionType | string | Required | Specifies the type of trigger. Use ALERT_TRIGGER_TYPE_THRESHOLD. |
|  | conditions | Array of Objects | Optional | List of conditions that trigger the alert. |
|  | frequency | string | Required | Evaluation frequency for the alert. Example: MINS_15. |

### Conditions Object Description Table














      ``











      ``



| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| dimensionName | string | Required | Dimension used for threshold condition. Example: STATIC_ALERT_MENTIONS_VOLUME. |
| values | array of number | Required | Threshold values for triggering the alert. |
| filterType | string | Required | Comparison operator. Example: GT (greater than). |

## Example - Request to Create Static Listening Alert

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/alert-manager' \
--header 'Authorization: Bearer {access_token}\
--header 'key: {API_Key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Alert API - Threshold doc test",
    "category": "STATIC_ALERT",
    "module": "LISTENING",
    "filterDimensions": [
        {
            "dimensionName": "TOPIC_IDS",
            "filterType": "IN",
            "values": [
                "680f4da9b38ac15f91ac77dc"
            ]
        }
    ],
    "tags": [
        " Test API"
    ],
    "enabled": true,
    "distributionConfig": {
        "emailIds": [
            "prabhav12082002@gmail.com"
        ],
        "sendEmailNotification": true,
        "customEmailSubject": "Alert API - Threshold test",
        "senderAlias": "prabhav+qa6@sprinklr.com"
    },
    "volumetricAlertConfig": {
        "alertTriggerConditionType": "ALERT_TRIGGER_TYPE_THRESHOLD",
        "conditions": [
            {
                "dimensionName": "STATIC_ALERT_MENTIONS_VOLUME",
                "values": [
                    100
                ],
                "filterType": "GT"
            }
        ],
        "frequency": "MINS_15"
    }
}'

## Example - Response


{
    "data": {
        "id": "688b6e0dfa585e61d1374763",
        "name": "Alert API - Threshold test Shivi 2",
        "category": "STATIC_ALERT",
        "module": "LISTENING",
        "status": "IN_PROGRESS",
        "filterDimensions": [
            {
                "dimensionName": "TOPIC_IDS",
                "filterType": "IN",
                "values": [
                    "680f4da9b38ac15f91ac77dc"
                ]
            }
        ],
        "tags": [
            "Test API"
        ],
        "enabled": true,
        "distributionConfig": {
            "emailIds": [
                "shivangi.singh@sprinklr.com"
            ],
            "sendEmailNotification": true,
            "customEmailSubject": "Alert API - Threshold test",
            "senderAlias": "prabhav+qa6@sprinklr.com"
        },
        "volumetricAlertConfig": {
            "alertTriggerConditionType": "ALERT_TRIGGER_TYPE_THRESHOLD",
            "conditions": [
                {
                    "dimensionName": "STATIC_ALERT_MENTIONS_VOLUME",
                    "filterType": "GT",
                    "values": [
                        100
                    ]
                }
            ],
            "frequency": "MINS_15"
        },
        "createdTime": 1753968130844,
        "modifiedTime": 1753968141018,
        "ownerUserId": 1000360519,
        "lastModifiedUserId": 1000360519,
        "clientId": 1000004523
    },
"errors": []
}

## Request Body - Create Smart Listening Alert
















      ``






      ``






      ``













      ``






      ``




















      ``




















      ``



























      ````

















| Parameter | Sub Parameter | Type | Required / Optional | Description |
| --- | --- | --- | --- | --- |
| name |  | string | Required | Name of the alert. Appears in the UI and email subject unless overridden by customEmailSubject. |
| category |  | string | Required | Alert type. Use SMART_ALERT for smart listening alerts. |
| module |  | string | Required | Product module. Use LISTENING for listening alerts. |
| filterDimensions |  | array of objects | Required | Dimensions and filters that define the alert scope. |
|  | dimensionName | string | Required | Name of the dimension to filter on. Example: TOPIC_IDS. |
|  | filterType | string | Required | Type of filter. Example: IN. |
|  | values | array | Required | Values to match against the specified dimension. |
| tags |  | array of string | Optional | Tags used for internal classification of the alert. |
| enabled |  | boolean | Required | Enables the alert when set to true. |
| distributionConfig |  | object | Required | Configuration for email notification delivery. |
|  | emailIds | array of string | Required | List of email addresses to notify when alert is triggered. |
|  | sendEmailNotification | boolean | Required | Enables email notifications when set to true. |
|  | customEmailSubject | string | Optional | Custom subject line for the alert email. Overrides default alert name. |
|  | senderAlias | string | Optional | Email alias shown as the sender of the alert email. |
| smartAlertConfig |  | object | Required | Configuration specific to smart alert behavior. |
|  | smartAlertMetrics | array of string | Required | Metrics monitored by the smart alert. Examples: MENTIONS_COUNT, LISTENING_RETWEETS. |
|  | suddenAnomalyEnabled | boolean | Required | Enables detection of sudden spikes in the selected metrics. |
|  | longTermTrendsEnabled | boolean | Required | Enables detection of long-term anomalies in the selected metrics. |

## Example - Request to Create Smart Listening Alert

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/alert-manager' \ 
--header 'Authorization: Bearer {access_token}\ 
--header 'key: {API_Key}' \ 
--header 'Content-Type: application/json' \ 
--data-raw '{ 
    "name": "Alert API - Smart Test Doc", 
    "category": "SMART_ALERT", 
    "module": "LISTENING", 
    "filterDimensions": [ 
        { 
            "dimensionName": "TOPIC_IDS", 
            "filterType": "IN", 
            "values": [ 
                "680f4da9b38ac15f91ac77dc" 
            ] 
        } 
    ], 
    "tags": [ 
        "Test API" 
    ], 
    "enabled": true, 
    "distributionConfig": { 
        "emailIds": [ 
            "prabhav12082002@gmail.com" 
        ], 
        "sendEmailNotification": true, 
        "customEmailSubject": "Alert API - Smart Test", 
        "senderAlias": "prabhav+qa6@sprinklr.com" 
    }, 
    "smartAlertConfig": { 
        "smartAlertMetrics": [ 
            "MENTIONS_COUNT", 
            "LISTENING_RETWEETS" 
        ], 
        "suddenAnomalyEnabled": true, 
        "longTermTrendsEnabled": false 
    } 
}'

## Example - Response


{
    "data": {
        "id": "6877868a9d4d371d95e2e072", 
        "name": "Alert API - Smart Test Doc", 
        "category": "SMART_ALERT", 
        "module": "LISTENING", 
        "status": "IN_PROGRESS", 
        "filterDimensions": [ 
            { 
                "dimensionName": "TOPIC_IDS", 
                "filterType": "IN", 
                "values": [ 
                    "680f4da9b38ac15f91ac77dc" 
                ] 
            } 
        ], 
        "tags": [ 
            "Test API" 
        ], 
        "enabled": true, 
        "distributionConfig": { 
            "emailIds": [ 
                "prabhav12082002@gmail.com" 
            ], 
            "sendEmailNotification": true, 
            "customEmailSubject": "Alert API - Smart Test", 
            "senderAlias": "prabhav+qa6@sprinklr.com" 
        }, 
        "smartAlertConfig": { 
            "smartAlertMetrics": [ 
                "MENTIONS_COUNT", 
                "LISTENING_RETWEETS" 
            ], 
            "suddenAnomalyEnabled": true, 
            "longTermTrendsEnabled": false 
        }, 
        "createdTime": 1752663689935, 
        "modifiedTime": 1752663690469, 
        "ownerUserId": 1000053136, 
        "lastModifiedUserId": 1000053136, 
        "clientId": 1000004523 
    }, 
    "errors": [] 
}

### Response Parameters










| Parameter | Sub-parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id for the alert | String |
| name |  | Name of the alert | String |
| category |  | Type of alert category | String |
| module |  | Module associated with the alert | String |
| status |  | Status of the alert. For example, SUCCESS | String |
| filterDimensions |  | List of filter criteria applied to the alert | Array |
|  | dimensionName | Name of the dimension used for filtering. For example, TOPIC_IDS | String |
|  | filterType | Type of filter applied. For example, IN | String |
|  | values | Values used in the filtering criteria | Array |
|  | details | Additional configuration for the filter (if any) | Object |
| tags |  | Tags associated with the alert | Array |
| enabled |  | Indicates whether the alert is currently enabled | Boolean |
| distributionConfig |  | Configuration for how the alert is delivered to recipients | Object |
|  | emailIds | List of email addresses to receive notifications | Array |
|  | sendEmailNotification | Whether email notifications are enabled | Boolean |
|  | customEmailSubject | Custom subject line used for the email | String |
|  | senderAlias | Name or email to display as the sender | String |
| smartAlertConfig |  | Configuration for smart alert behavior | Object |
|  | smartAlertMetrics | Metrics tracked by the alert. For example, MENTIONS_COUNT, LISTENING_RETWEETS | Array |
|  | suddenAnomalyEnabled | Indicates if sudden anomaly detection is enabled | Boolean |
|  | longTermTrendsEnabled | Indicates if long-term trend detection is enabled | Boolean |
| createdTime |  | Time when the alert was created (epoch format) | Timestamp |
| modifiedTime |  | Time when the alert was last updated (epoch format) | Timestamp |
| ownerUserId |  | ID of the user who originally created the alert | Number |
| lastModifiedUserId |  | ID of the user who last modified the alert | Number |
| clientId |  | Sprinklr tenant or client ID | Number |

[](https://dev.sprinklr.com/create-listening-alert)

[Back to top](https://dev.sprinklr.com/create-listening-alert)
