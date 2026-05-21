---
title: "Update Listening Alert"
slug: update-listening-alert
url: https://dev.sprinklr.com/update-listening-alert
---

# Update Listening Alert

#   PUT Update Listening Alert
 

This API allows you to update a listening alert in Sprinklr.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/alert-manager/`{listening_alert_id}`

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

### Query Parameters


















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {listening_alert_id} | Required | Id of the listening alert you want to delete. You can get this Id from the Create Listening Alert API response. | String |

### Request Body Parameters













****

****

****



****




****







****









| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | Name of the alert. | String |
| category |  | Required | Alert category. Supported Values: SMART_ALERT, STATIC_ALERT | String |
| module |  | Required | Associated module. Supported Values: LISTENING | String |
| status |  | Required | Status of the alert. Supported Values: NEW | String |
| filterDimensions |  | Required | List of filter criteria for the alert | Array |
|  | dimensionName | Required | Dimension to filter on. | String |
|  | filterType | Required | Type of filter. Supported Values: See Filter Type table below | String |
|  | values | Required | Values to filter by | Array |
|  | details | Optional | Additional filter details | Object |
| tags |  | Optional | Tags associated with the alert | Array |
| enabled |  | Required | Indicates whether the alert is activeSupported Values: true, false | Boolean |
| distributionConfig |  | Optional | Alert distribution configuration | Object |
|  | emailIds | Optional | List of email recipients | Array |
|  | sendEmailNotification | Required | Whether to send email notifications | Boolean |
|  | customEmailSubject | Optional | Custom subject line for emails | String |
|  | senderAlias | Optional | Email sender alias | String |
| smartAlertConfig |  | Optional | Smart alert configuration | Object |
|  | smartAlertMetrics | Optional | Metrics to track. Supported Values: MENTIONS_COUNT, LISTENING_RETWEETS | Array |
|  | suddenAnomalyEnabled | Optional | Enable sudden anomaly detection | Boolean |
|  | longTermTrendsEnabled | Optional | Enable long-term trend detection | Boolean |
| createdTime |  | Optional | Time the alert was created (epoch) | Timestamp |
| modifiedTime |  | Optional | Time the alert was last modified (epoch) | Timestamp |
| ownerUserId |  | Required | Id of the user who owns the alert | Number |
| lastModifiedUserId |  | Required | Id of the user who last modified the alert | Number |
| clientId |  | Required | Client Id | Number |

### Filter Types - Description







| Filter Type | Description |
| --- | --- |
| AND | Similar to boolean AND. It is added where more than one filter exists and returns values that meet all filter conditions. |
| OR | Similar to boolean OR. It is added where more than one filter exists and returns values that meet at least one filter condition. |
| NOT | Similar to boolean NOT, i.e., it returns values where that do not match the applied filter conditions. |
| IN | Returns resources where the key matches with any of the values mentioned in the list of values |
| GT (greater than) | Returns resources where the key is greater than the value/s mentioned in the list of values |
| GTE (Greater than equal to) | Returns resources where the key is greater than equal to the value/s mentioned in the list of values |
| LT (Less than) | Returns resources where the key is less than the value/s mentioned in the list of values |
| LTE (Less than equal to) | Returns resources where the key is less than equal to the value/s mentioned in the list of values |
| NIN (Not In) | Returns resources where the key does not match with the values mentioned in the list of values |
| EQUALS | Returns resources where the given key is equal to the value/s mentioned in the list of values |
| NOT_EQUALS | Returns resources where the given key is not equal to the value/s mentioned in the list of values |
| CONTAINS | Returns resources where the given key contains the values mentioned in the list of values |

## Example - Request




 Copy Code


curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v2/alert-manager/688b11d08dc2116653924234' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'key: {Enter Your API Key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Smart Alert Test BR",
    "category": "SMART_ALERT",
    "module": "LISTENING",
    "status": "NEW",
    "filterDimensions": [
        {
            "dimensionName": "TOPIC_IDS",
            "filterType": "IN",
            "values": [
                "680f4da9b38ac15f91ac77dc"
            ],
            "details": {}
        }
    ],
    "tags": [
        "SMART Alerts","Listening alerts"
    ],
    "enabled": false,
    "distributionConfig": {
        "emailIds": [
            "xyz@sprinklr.com"
        ],
        "sendEmailNotification": true,
        "customEmailSubject": "Smart Alert Test BR",
        "senderAlias": "xyz@sprinklr.com"
    },
    "smartAlertConfig": {
        "smartAlertMetrics": [
            "MENTIONS_COUNT",
            "LISTENING_RETWEETS"
        ],
        "suddenAnomalyEnabled": true,
        "longTermTrendsEnabled": false
    },
    "createdTime": 1747202762724,
    "modifiedTime": 1747202779761,
    "ownerUserId": 1000053136,
    "lastModifiedUserId": 1000053136,
    "clientId": 1000004523
}'



## Example - Response





{
    "data": {
        "id": "688b11d08dc2116653924234",
        "name": "Smart Alert Test BR",
        "category": "SMART_ALERT",
        "module": "LISTENING",
        "status": "NEW",
        "filterDimensions": [
            {
                "dimensionName": "TOPIC_IDS",
                "filterType": "IN",
                "values": [
                    "680f4da9b38ac15f91ac77dc"
                ],
                "details": {}
            }
        ],
        "tags": [
            "SMART Alerts",
            "Listening alerts"
        ],
        "enabled": false,
        "distributionConfig": {
            "emailIds": [
                "xyz@sprinklr.com"
            ],
            "sendEmailNotification": true,
            "customEmailSubject": "Smart Alert Test BR",
            "senderAlias": "xyz@sprinklr.com"
        },
        "smartAlertConfig": {
            "smartAlertMetrics": [
                "MENTIONS_COUNT",
                "LISTENING_RETWEETS"
            ],
            "suddenAnomalyEnabled": true,
            "longTermTrendsEnabled": false
        },
        "createdTime": 1753944526341,
        "modifiedTime": 1753944671014,
        "ownerUserId": 66014658,
        "lastModifiedUserId": 66014658,
        "clientId": 66000002
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

[](https://dev.sprinklr.com/update-listening-alert) 

 

 
[Back to top](https://dev.sprinklr.com/update-listening-alert)
