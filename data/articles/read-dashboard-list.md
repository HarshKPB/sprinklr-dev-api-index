---
title: "Read Dashboard List"
slug: read-dashboard-list
url: https://dev.sprinklr.com/read-dashboard-list
---

# Read Dashboard List

#
POST - Read Dashboard List


This API allows you to retrieve a comprehensive list of Sprinklr reporting and listening dashboards. In addition to fetching the dashboard names, you can also access detailed metadata, such as dashboard tags, associated listening topic IDs, and more. If enabled in the Sprinklr UI, you can also obtain external dashboard links.

**Dev Notes: ** If you want to get an external dashboard link which can we accessed outside Sprinklr UI, you need to enable the feature within Sprinklr UI.

### API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/entity/{entityType}/filter

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

### Path Parameters







````

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| entityType | Required | String | The entity type can either be REPORTING_DASHBOARD_MANAGER or  LISTENING_DASHBOARD_MANAGER |

### Request Body Parameters

The request body payload for the API is given below.







````

``

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| entityType | Required | String | The entity type for the request. Options include REPORTING_DASHBOARD_MANAGER or LISTENING_DASHBOARD_MANAGER. |
| q | Optional | String | A search query string. An empty string can be used if no query is needed. |
| groupingField | Optional | String | Specifies how the results should be grouped. The value UNGROUPED can be used to avoid grouping. |
| page | Optional | Object | Defines pagination details. |
| sorts | Optional | Array of Objects | Specifies the sorting criteria. |
| requestType | Required | String | Defines the type of request being made. Options include: <code>FILTER</code> <code>FACETS</code><code>COUNT</code> |

**Dev Notes: ** You will generally have three filter queries with different request types as `FILTER`, `FACETS`, and `COUNT` select as per the use case.







| Request Type | Description |
| --- | --- |
| FILTER | Provide details on the dashboard Ids, tags, topics, along with other metadata. |
| FACETS | It is used to get the different types of facets present in the dashboard. |
| COUNT | This provides the total count of the dashboards. |

#### Sample API Request Body Payload for Reporting Dashboard

 Copy Code



{
"entityType": "REPORTING_DASHBOARD_MANAGER",
"filters": [
{
"field": "MODULE_TYPE",
"values": [
"REPORTING"
]
}
],
"groupingField": "UNGROUPED",
"query": "",
"paginationInfo": {
"start": 0,
"rows": 50
},
"sort": {
"key": "lcName",
"order": "ASC"
},
"requestType": "FILTER"
}




#### Sample API Request Body Payload for Listening Dashboard




{
    "entityType": "LISTENING_DASHBOARD_MANAGER",
    "filters": [
        {
            "field": "MODULE_TYPE",
            "values": [
                "LISTENING"
            ]
        }
    ],
    "groupingField": "UNGROUPED",
    "query": "",
    "paginationInfo": {
        "start": 0,
        "rows": 50
    },
    "sort": {
        "key": "lcName",
        "order": "ASC"
    },
    "requestType": "FILTER"
}





### Response Schema



























































































































































































| Parameter | Sub-Parameter | Type | Description |  |
| --- | --- | --- | --- | --- |
| data |  |  | Object | The main container for the API response data. |
|  | hasMore |  | Boolean | Indicates if there are more results available. |
|  | assetCount |  | Integer | The total number of assets found. |
|  | folderCount |  | Integer | The total number of folders found. |
|  | results |  | Array | A list of dashboards or reports that match the filter criteria. |
|  |  | isExternalLinkEnabled | Boolean | Indicates if an external link is enabled for the dashboard. |
|  |  | id | String | The unique identifier of the dashboard/report. |
|  |  | name | String | The name of the dashboard/report. |
|  |  | moduleType | String | The type of module (e.g., REPORTING) associated with the dashboard/report. |
|  |  | type | String | The type of dashboard/report, such as CUSTOM or STANDARD. |
|  |  | filters | Array | A list of filters applied to the dashboard/report. |
|  |  | widgetLayout | String | The layout configuration for widgets within the dashboard/report, stored as a JSON string. |
|  |  | tags | Array | A list of tags associated with the dashboard/report. |
|  |  | locked | Boolean | Indicates if the dashboard/report is locked from edits. |
|  |  | compareMode | Boolean | Indicates if compare mode is enabled. |
|  |  | slaPresetEnabled | Boolean | Indicates if an SLA preset is enabled. |
|  |  | extended | Boolean | Indicates if the dashboard/report has extended features enabled. |
|  |  | spaceWidgetLayout | String | The layout configuration for space widgets within the dashboard/report, stored as a JSON string. |
|  |  | hidden | Boolean | Indicates if the dashboard/report is hidden from view. |
|  |  | canEdit | Boolean | Indicates if the user has permission to edit the dashboard/report. |
|  |  | deleted | Boolean | Indicates if the dashboard/report has been deleted. |
|  |  | modifiedTime | String | The timestamp of the last modification made to the dashboard/report (format: MMM dd, yyyy, hh:mm:ss a). |
|  |  | createdTime | String | The timestamp of when the dashboard/report was created (format: MMM dd, yyyy, hh:mm:ss a). |
|  | count |  | Integer | The total number of results returned in the response. |
| errors |  |  | Array | A list of errors, if any occurred during the request. |

### Example - Request

 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/entity/LISTENING_DASHBOARD_MANAGER/filter' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'Content-Type: application/json' \
-d '{{
"entityType": "LISTENING_DASHBOARD_MANAGER",
"filter": {
"type": "AND",
"filters": [
{
"type":"IN",
"key": "MODULE_TYPE",
"values": [
"REPORTING"
]
}
]
},
"q": "",
"groupingField": "UNGROUPED",
"page": {
"start": 0,
"size": 10
},
"sorts": [
{
"key": "name",
"order": "ASC"
}
],
"requestType": "FILTER"
}'




### Example - Response




	{
    "data": {
        "hasMore": true,
        "assetCount": 0,
        "folderCount": 0,
        "results": [
            {
                "isExternalLinkEnabled": false,
                "id": "66b089ad242cb400a1a1c653",
                "name": "\tSPACE-103558",
                "moduleType": "REPORTING",
                "type": "CUSTOM",
                "filters": [
                    {
                        "filterType": "IN",
                        "field": "ACCOUNT_ID",
                        "values": [],
                        "details": {
                            "missing": "-1",
                            "reportName": "ACCOUNT_CREDENTIALS_VALUE_REPORT",
                            "uniqueId": "D_ACCOUNT_ID",
                            "type": "NORMAL",
                            "fieldId": "ACCOUNT_ID"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "CLIENT_ID",
                        "values": [],
                        "details": {
                            "uniqueId": "D_CLIENT_ID",
                            "fieldId": "CLIENT_ID"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "SN_TYPE",
                        "values": [],
                        "details": {
                            "uniqueId": "D_SN_TYPE",
                            "fieldId": "SN_TYPE"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "KEYWORD_SEARCH",
                        "values": [],
                        "details": {
                            "uniqueId": "D_KEYWORD_SEARCH",
                            "fieldId": "KEYWORD_SEARCH"
                        }
                    }
                ],
                "widgetLayout": "{\"tabs\":[],\"layouts\":[[{\"id\":\"66b08b6f242cb400a1a28fa4\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"66b0ce17fceb597d82291541\",\"pos\":{\"row\":1,\"col\":7},\"size\":{\"x\":6,\"y\":9}}]]}",
                "tags": [],
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "spaceWidgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\"\\tSPACE-103558\"}],\"layouts\":[[{\"id\":\"66b08b6f242cb400a1a28fa4\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"66b0ce17fceb597d82291541\",\"pos\":{\"row\":1,\"col\":7},\"size\":{\"x\":6,\"y\":9}}]]}",
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Aug 05, 2024, 01:13:07 PM",
                "createdTime": "Aug 05, 2024, 08:13:33 AM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "667321953bdcde4aa5c1e7ce",
                "name": " Associate CARE-56979 ok",
                "moduleType": "REPORTING",
                "type": "CUSTOM",
                "filters": [
                    {
                        "filterType": "IN",
                        "field": "ACCOUNT_ID",
                        "values": [],
                        "details": {
                            "uniqueId": "D_ACCOUNT_ID",
                            "fieldId": "ACCOUNT_ID"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "CLIENT_ID",
                        "values": [],
                        "details": {
                            "uniqueId": "D_CLIENT_ID",
                            "fieldId": "CLIENT_ID"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "SN_TYPE",
                        "values": [],
                        "details": {
                            "reportName": "ACCOUNT_STATE_REPORT",
                            "uniqueId": "D_SN_TYPE",
                            "type": "NORMAL",
                            "fieldId": "SN_TYPE"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "KEYWORD_SEARCH",
                        "values": [],
                        "details": {
                            "uniqueId": "D_KEYWORD_SEARCH",
                            "fieldId": "KEYWORD_SEARCH"
                        }
                    }
                ],
                "widgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\" Associate CARE-56979\"}],\"layouts\":[[{\"id\":\"667323493bdcde4aa5c24635\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"667d2cb3c229b717b73948b4\",\"pos\":{\"row\":1,\"col\":7},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"667d2ffdc229b717b73a8af6\",\"pos\":{\"row\":1,\"col\":13},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"667e6d58cbddbe6c836aa1dd\",\"pos\":{\"row\":10,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"6683c5c447f6366e189481d0\",\"pos\":{\"row\":10,\"col\":7},\"size\":{\"x\":6,\"y\":9}}]]}",
                "tags": [],
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "spaceWidgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\" Associate CARE-56979\"}],\"layouts\":[[{\"id\":\"667323493bdcde4aa5c24635\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"667d2cb3c229b717b73948b4\",\"pos\":{\"row\":10,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"667d2ffdc229b717b73a8af6\",\"pos\":{\"row\":1,\"col\":7},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"667e6d58cbddbe6c836aa1dd\",\"pos\":{\"row\":19,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"6683c5c447f6366e189481d0\",\"pos\":{\"row\":19,\"col\":7},\"size\":{\"x\":6,\"y\":9}}]]}",
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Jul 02, 2024, 09:19:12 AM",
                "createdTime": "Jun 19, 2024, 06:21:09 PM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "66869d45590c795740b87894",
                "name": " IG Tagged message- Inbound Merge Issue",
                "moduleType": "REPORTING",
                "type": "CUSTOM",
                "filters": [
                    {
                        "filterType": "IN",
                        "field": "ACCOUNT_ID",
                        "values": [],
                        "details": {
                            "uniqueId": "D_ACCOUNT_ID"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "CLIENT_ID",
                        "values": [],
                        "details": {
                            "uniqueId": "D_CLIENT_ID"
                        }
                    },
                    {
                        "filterType": "IN",
                        "field": "SN_TYPE",
                        "values": [],
                        "details": {
                            "uniqueId": "D_SN_TYPE"
                        }
                    }
                ],
                "widgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\"IG tagged Media Testing\"}],\"layouts\":[[{\"id\":\"66869d49590c795740b87b5d\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"66869d49590c795740b87b88\",\"pos\":{\"row\":1,\"col\":7},\"size\":{\"x\":20,\"y\":12}}]]}",
                "tags": [],
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "spaceWidgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\"IG tagged Media Testing\"}],\"layouts\":[[{\"id\":\"66869d49590c795740b87b5d\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":10,\"y\":12}},{\"id\":\"66869d49590c795740b87b88\",\"pos\":{\"row\":13,\"col\":1},\"size\":{\"x\":10,\"y\":12}}]]}",
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Jul 04, 2024, 01:02:01 PM",
                "createdTime": "Jul 04, 2024, 01:01:57 PM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "65bbbb8cc6dd055609b4de24",
                "name": " MATRIX - WIDGET TESTReporting",
                "moduleType": "REPORTING",
                "type": "STANDARD",
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Apr 02, 2024, 05:57:11 AM",
                "createdTime": "Feb 01, 2024, 03:41:00 PM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "668e3e42adc2010212aeda83",
                "name": " Offline Event Feedback Survey p view Survey Analytics",
                "moduleType": "REPORTING",
                "type": "STANDARD",
                "groupKey": "SURVEY_ANALYTICS_DASHBOARD",
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Jul 10, 2024, 07:54:42 AM",
                "createdTime": "Jul 10, 2024, 07:54:42 AM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "668e3e42adc2010212aeda7e",
                "name": " Offline Event Feedback Survey p view Text Analytics",
                "moduleType": "REPORTING",
                "type": "STANDARD",
                "filters": [
                    {
                        "filterType": "IN",
                        "field": "QUESTION_ID",
                        "values": [],
                        "details": {}
                    }
                ],
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Jul 10, 2024, 07:54:42 AM",
                "createdTime": "Jul 10, 2024, 07:54:42 AM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "65a66e25ea0d5939ce6f002f",
                "name": " Re-structure Audit Calibration Report and add relevant data jan 16",
                "moduleType": "REPORTING",
                "type": "CUSTOM",
                "filters": [
                    {
                        "filterType": "IN",
                        "field": "ACCOUNT_ID",
                        "values": [],
                        "details": {}
                    },
                    {
                        "filterType": "IN",
                        "field": "CLIENT_ID",
                        "values": [],
                        "details": {}
                    },
                    {
                        "filterType": "IN",
                        "field": "SN_TYPE",
                        "values": [],
                        "details": {}
                    }
                ],
                "widgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\" Re-structure Audit Calibration Report and add relevant data jan 16\"}],\"layouts\":[[{\"id\":\"65b3b676671f1118ccc28f1c\",\"pos\":{\"row\":1,\"col\":13},\"size\":{\"x\":6,\"y\":9}}]]}",
                "tags": [],
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "spaceWidgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\" Re-structure Audit Calibration Report and add relevant data jan 16\"}],\"layouts\":[[{\"id\":\"65b3b676671f1118ccc28f1c\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":12,\"y\":9}}]]}",
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Apr 02, 2024, 05:57:11 AM",
                "createdTime": "Jan 16, 2024, 11:53:09 AM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "668d19889b2f9c4e09797872",
                "name": " bugs- image/video in question normal view Survey Analytics",
                "moduleType": "REPORTING",
                "type": "STANDARD",
                "groupKey": "SURVEY_ANALYTICS_DASHBOARD",
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Jul 09, 2024, 11:05:44 AM",
                "createdTime": "Jul 09, 2024, 11:05:44 AM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "668d19889b2f9c4e0979786d",
                "name": " bugs- image/video in question normal view Text Analytics",
                "moduleType": "REPORTING",
                "type": "STANDARD",
                "filters": [
                    {
                        "filterType": "IN",
                        "field": "QUESTION_ID",
                        "values": [],
                        "details": {}
                    }
                ],
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Jul 09, 2024, 11:05:44 AM",
                "createdTime": "Jul 09, 2024, 11:05:44 AM"
            },
            {
                "isExternalLinkEnabled": false,
                "id": "669645edb47c4957ce855039",
                "name": " cfm-1563 normal view EXTERNAL_APPLICATION",
                "moduleType": "REPORTING",
                "type": "STANDARD",
                "widgetLayout": "[{\"size\":{\"x\":6,\"y\":5},\"pos\":{\"col\":7,\"row\":6},\"id\":\"669645ecb47c4957ce854fa9_1\",\"span\":{\"className\":\"flex-1\"}},{\"size\":{\"width\":110,\"x\":6,\"y\":5},\"pos\":{\"col\":1,\"row\":6},\"id\":\"669645ecb47c4957ce854fa9_0\",\"span\":{\"className\":\"flex-none\"}}]",
                "locked": false,
                "compareMode": false,
                "slaPresetEnabled": false,
                "extended": false,
                "spaceWidgetLayout": "[{\"size\":{\"x\":6,\"y\":5},\"pos\":{\"col\":7,\"row\":6},\"id\":\"669645ecb47c4957ce854fa9_1\",\"span\":{\"className\":\"flex-1\"}},{\"size\":{\"width\":110,\"x\":6,\"y\":5},\"pos\":{\"col\":1,\"row\":6},\"id\":\"669645ecb47c4957ce854fa9_0\",\"span\":{\"className\":\"flex-none\"}}]",
                "hidden": false,
                "canEdit": true,
                "deleted": false,
                "modifiedTime": "Jul 16, 2024, 10:05:33 AM",
                "createdTime": "Jul 16, 2024, 10:05:33 AM"
            }
        ],
        "count": 10
    },
    "errors": []
}





**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

[](https://dev.sprinklr.com/read-dashboard-list)




[Back to top](https://dev.sprinklr.com/read-dashboard-list)
