---
title: "Toggle Alert"
slug: toggle-alert
url: https://dev.sprinklr.com/toggle-alert
---

# Toggle Alert

#  POST  Toggle Alert

 Use this API to enable or disable one or more alerts by passing their alert IDs.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/alert-manager/toggle?enabled=`true`

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














      ````



| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Set to true to enable alerts, or false to disable them. |

### Request Body















****

```

```




| Name | Type | Required | Description |
| --- | --- | --- | --- |
| alertId | Array of strings | Yes | List of alert IDs to be toggled (enabled or disabled).         Example         [   "680f6efdf0b5e91a95c88757" ] |

## Example - Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/alert-manager/toggle?enabled=false' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {API_Key}' \
--header 'content-type: application/json' \
--header 'accept: application/json' \
--data '[
    "5e7507b757e63326c10c0bfc"
]'

## Example - Response


204 No Content

### Response Schema














| Status Code | Description |
| --- | --- |
| 204 | No Content — Alerts updated successfully. The API does not return a response body. |

[](https://dev.sprinklr.com/toggle-alert)

[Back to top](https://dev.sprinklr.com/toggle-alert)
