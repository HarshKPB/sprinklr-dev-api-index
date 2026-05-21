---
title: "Find Alert by Id"
slug: find-alert-by-id
url: https://dev.sprinklr.com/find-alert-by-id
---

# Find Alert by Id

# GET Find Alert by Id
  

This API allows you to fetch the details of an alert by using its Id.

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

### Path Parameter

















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {listening_alert_id} | Required | Id of the listening alert you want to fetch. You can get this Id from the Create Listening Alert API . | String |

## Example - Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/alert-manager/68106e0eb619a0355b323bd2' \
--header 'Authorization: Bearer {token} ' \
--header 'Key: {API_Key}' \
--header 'content-type: application/json' \
--header 'accept: application/json' \

## Example - Response


{
    "data": {
        "id": "68106e0eb619a0355b323bd2",
        "name": "ABC - Smart Test",
        "category": "SMART_ALERT",
        "module": "LISTENING",
        "status": "SUCCESS",
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
            "ABC API"
        ],
        "enabled": true,
        "distributionConfig": {
            "emailIds": [
                "prabhav12082002@gmail.com"
            ],
            "sendEmailNotification": true,
            "customEmailSubject": "ABC Alert API - Smart Test",
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
        "createdTime": 1745907213139,
        "modifiedTime": 1745907548949,
        "ownerUserId": 1000053136,
        "lastModifiedUserId": -100,
        "clientId": 1000004523
    },
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

[](https://dev.sprinklr.com/find-alert-by-id)

[Back to top](https://dev.sprinklr.com/find-alert-by-id)
