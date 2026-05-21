---
title: "Read Dashboard List v1"
slug: read-dashboard-list-v1
url: https://dev.sprinklr.com/read-dashboard-list-v1
---

# Read Dashboard List v1

#
POST - Read Dashboard List


You can use this API to pull a list of Sprinklr reporting and listening dashboards and can view the metadata including dashboard tags, listening topic IDs, and other metadata including the external dashboard link if enabled within Sprinklr UI.

**Dev Notes: ** If you want to get an external dashboard link which can we accessed outside Sprinklr UI, you need to enable the feature within Sprinklr UI.

### API Endpoint

https://api3.sprinklr.com/`{env}`/api/v1/entity/{entityType}/filter

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

### Path Parameters














			````




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | The entity type can either be REPORTING_DASHBOARD_MANAGER or  LISTENING_DASHBOARD_MANAGER | String |

### Request Body Parameters

The request body payload for the API can be fetched from the UI. The steps are given below.

#### The Copied UI Request for Reporting Dashboard

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





#### The Copied UI Request for Listening Dashboard

 Copy Code



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





**Dev Notes: ** You will generally have three filter queries with different request types as `FILTER`, `FACETS`, and `COUNT` select as per the use case.






















| Request Type | Description |
| --- | --- |
| FILTER | Provide details on the dashboard Ids, tags, topics, along with other metadata. |
| FACETS | It is used to get the different types of facets present in the dashboard. |
| COUNT | This provides the total count of the dashboards. |

### Example - Request

 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v1/entity/{{entityType}}/filter' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'Content-Type: application/json' \
-d '{
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
}'




### Example - Response




{
    "items": [
        {
            "isExternalLinkEnabled": true,
            "externalLink": "https://abc.com/insights/listening/dashboard/5f1ff9f0jhk67d6a8baa48d6?id=DASHBOARD_5f1ff9f68d3d79jkh89hb8d6",
            "externalLinkExpiryDate": 1212895399999,
            "id": "5f1ff9f0jhk67d6a8baa48d6",
            "name": "#123",
            "moduleType": "LISTENING",
            "type": "CUSTOM",
            "filters": [
                {
                    "filterType": "IN",
                    "field": "QUERY",
                    "values": [],
                    "userFilter": false,
                    "allValuesAllowed": true,
                    "favourite": true,
                    "mandatory": false,
                    "locked": false,
                    "details": {
                        "contentType": "DB_FILTER",
                        "OLD_DIM_NAME": "TOPIC_QUERY",
                        "INPUT_TYPE": "FREE_TEXT",
                        "EXIST_FILTER": false,
                        "singleSelect": "true"
                    }
                },
                {
                    "filterType": "IN",
                    "field": "TOPIC_IDS",
                    "values": [],
                    "userFilter": false,
                    "allValuesAllowed": true,
                    "favourite": true,
                    "mandatory": false,
                    "locked": false,
                    "details": {
                        "contentType": "DB_FILTER",
                        "DRILLDOWN": false,
                        "dF": true,
                        "OLD_DIM_NAME": "TOPIC",
                        "EXIST_FILTER": false
                    }
                }
            ],
            "widgetLayout": "{\"layouts\":[[{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":12,\"y\":3},\"noVisibleHeader\":true},{\"id\":\"5f1ff9f0jhk67d6a8baa4836\",\"pos\":{\"row\":4,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d4\",\"pos\":{\"row\":13,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d8\",\"pos\":{\"row\":22,\"col\":1},\"size\":{\"x\":12,\"y\":9}}],[{\"id\":\"5f1ff9f0jhk67d6a8baa28d6\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":24,\"y\":8}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":9,\"col\":1},\"size\":{\"x\":24,\"y\":8}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":17,\"col\":1},\"size\":{\"x\":24,\"y\":8}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":25,\"col\":1},\"size\":{\"x\":24,\"y\":8}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":33,\"col\":1},\"size\":{\"x\":24,\"y\":8}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":41,\"col\":1},\"size\":{\"x\":24,\"y\":8}}],[{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":24,\"y\":8}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":9,\"col\":1},\"size\":{\"x\":12,\"y\":8}},{\"id\":\"5f1ff9f0jhk67d6a8baa48d6\",\"pos\":{\"row\":9,\"col\":13},\"size\":{\"x\":12,\"y\":8}]}",
            "tags": [
                "#testLI",
                "ABCDE",
                "Adoption",
                "akash",
                "asdasd"
            ],
            "locked": false,
            "compareMode": false,
            "slaPresetEnabled": false,
            "partiallyLocked": false,
            "extended": false,
            "additional": {
                "layout": "TAB",
                "version": "5",
                "IS_CLONE_DISABLED": "false"
            },
            "lcName": "#123",
            "spaceWidgetLayout": "{\"layouts\":[[{\"id\":\"5f1ff9f68d3d8jkdbh3448d2\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":12,\"y\":3},\"noVisibleHeader\":true},{\"id\":\"5f1ff9f68d3d8jkdbh3448e7\",\"pos\":{\"row\":4,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f68d3d8jkdbh3443d7\",\"pos\":{\"row\":13,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f68d3d8jkdbh3446d7\",\"pos\":{\"row\":22,\"col\":1},\"size\":{\"x\":12,\"y\":9}}],[{\"id\":\"5f1ff9f68d3d8jkdbh3448d3\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":12,\"y\":3},\"noVisibleHeader\":true},{\"id\":\"5f1ff9f68d3d8jkdbh3458d7\",\"pos\":{\"row\":4,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f68d3d8jkdbh3448d7\",\"pos\":{\"row\":13,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f68d3d8jkdbh3448d7\",\"pos\":{\"row\":22,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f68d3d8jkdbh3448d7\",\"pos\":{\"row\":31,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f68d3d8jkdbh3448d7\",\"pos\":{\"row\":40,\"col\":1},\"size\":{\"x\":12,\"y\":9}},{\"id\":\"5f1ff9f68d3d8jkdbh3448d7\",\"pos\":{\"row\":49,\"col\":1},\"size\":{\"x\":12,\"y\":3}]}",
            "partnerCustomProperties": {
                "listening_dashboard_purpose": [
                    "None"
                ]
            },
            "tabs": [
                {
                    "id": 6,
                    "tabFiltersEnabled": true
                },
                {
                    "id": 7,
                    "tabFiltersEnabled": true
                }
            ],
            "versionId": 18,
            "grants": [
                "USER/600000001/OWNERSHIP",
                "CLIENT/2/OWNERSHIP"
            ],
            "clientId": 2,
            "ownerUserId": 603456001,
            "createdTime": 1595931127178,
            "modifiedTime": 1613550957496,
            "lastModifiedUserId": 603456001,
            "deleted": false,
            "folderMetadata": {
                "folderId": "5ffe920c7bd6023bhldbde45",
                "confidential": false
            },
            "canEdit": true
        },
        {
            "isExternalLinkEnabled": false,
            "id": "5fd0ab282f3ba1449ae42644",
            "name": "#fashiondesignweek",
            "moduleType": "LISTENING",
            "type": "CUSTOM",
            "filters": [],
            "widgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\"#fashiondesignweek\"},{\"id\":1,\"tabDisplayName\":\"#fashiondesignweek\"},{\"id\":2,\"tabDisplayName\":\"Untitled tab 3\"},{\"id\":3,\"tabDisplayName\":\"Untitled tab 4\"}],\"layouts\":[[{\"id\":\"fake_1268\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"5fd0ab282f3ba1449ae426e7\",\"pos\":{\"row\":1,\"col\":7},\"size\":{\"x\":6,\"y\":9}]]}",
            "locked": false,
            "compareMode": false,
            "slaPresetEnabled": false,
            "partiallyLocked": false,
            "extended": false,
            "additional": {
                "layout": "TAB",
                "version": "5",
                "IS_CLONE_DISABLED": "false"
            },
            "lcName": "#fashiondesignweek",
            "spaceWidgetLayout": "{\"tabs\":[{\"id\":0,\"tabDisplayName\":\"#fashiondesignweek\"},{\"id\":1,\"tabDisplayName\":\"#fashiondesignweek\"},{\"id\":2,\"tabDisplayName\":\"Untitled tab 3\"},{\"id\":3,\"tabDisplayName\":\"Untitled tab 4\"}],\"layouts\":[[{\"id\":\"fake_1268\",\"pos\":{\"row\":1,\"col\":1},\"size\":{\"x\":6,\"y\":9}},{\"id\":\"5fd0ab282f3ba1449ae426e7\",\"pos\":{\"row\":1,\"col\":7},\"size\":{\"x\":6,\"y\":9}]]}",
            "tabs": [
                {
                    "id": 1,
                    "tabFiltersEnabled": true
                }
            ],
            "versionId": 7,
            "grants": [
                "USER/603456001/OWNERSHIP",
                "CLIENT/2/OWNERSHIP"
            ],
            "clientId": 2,
            "ownerUserId": 603456001,
            "createdTime": 1607509232135,
            "modifiedTime": 1612975111080,
            "lastModifiedUserId": 603456001,
            "deleted": false,
            "folderMetadata": {
                "confidential": false
            },
            "canEdit": true
        }
],
    "itemsCount": 2,
    "hasMore": true
}





**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

[](https://dev.sprinklr.com/read-dashboard-list-v1)




[Back to top](https://dev.sprinklr.com/read-dashboard-list-v1)
