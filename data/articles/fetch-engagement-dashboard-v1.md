---
title: "Fetch Engagement Dashboard v1"
slug: fetch-engagement-dashboard-v1
url: https://dev.sprinklr.com/fetch-engagement-dashboard-v1
---

# Fetch Engagement Dashboard v1

#
  GET Fetch Engagement Dashboard



Using this API, you can fetch the details of a monitoring dashboard using the unique dashboard name.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/dashboard/{dashboardName}


### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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

## Path Parameter












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| dashboardName | Required | Refers to the "URL-encoded" name of the dashboard | String |

**Note: **

- You can fetch the dashboard name by using [fetch dashboards API](https://dev.sprinklr.com/fetch-all-engagement-dashboards-v1)

- The Dashboard Name must be URL Encoded.

**Example**: Sprinklr Dashboard = `Sprinklr%20Dashboard`

- You can use this endpoint to find the stream id & the stream name

### Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/dashboard/Social%20Channel%20Inbox' \
  -H 'Authorization: Bearer {token}' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}'






### Example - Response





    {
        "id": "5c7bdaf7e4b03d655cf612ca",
        "name": "Social Channel Inbox",
        "shareConfigs": [
            {
                "shareLevel": "CLIENT",
                "sharedWithIds": []
            },
            {
                "shareLevel": "CLIENT_GROUP",
                "sharedWithIds": []
            },
            {
                "shareLevel": "USER",
                "sharedWithIds": [
                    "185370",
                    "188984",
                    "189145"
                ]
            },
            {
                "shareLevel": "USER_GROUP",
                "sharedWithIds": []
            }
        ],
        "columnOrder": [
            "5c7c8914e4b0b25907ef1937",
            "5c7c8930e4b0b25907ef1bb5",
            "5c7e76c6e4b03d655d46a739",
            "5cbf8089e4b0704c5cdf2c03"
        ],
        "columns": [
            {
                "id": "5c7c8914e4b0b25907ef1937",
                "dashboardId": "5c7bdaf7e4b03d655cf612ca",
                "channel": "TWITTER",
                "type": "RECEIVED_DIRECT_MESSAGES",
                "tags": [],
                "properties": {
                    "SORT_ENABLED": [
                        "true"
                    ],
                    "ACCOUNT": [
                        "255156"
                    ],
                    "SOURCE_ID": [
                        "255156"
                    ],
                    "SHOW_COUNT": [
                        "true"
                    ],
                    "CATEGORY": [
                        "5"
                    ],
                    "POST_TYPE": [
                        "all"
                    ],
                    "TIME_RANGE_FILTER_KEY": [
                        "LIFETIME"
                    ],
                    "SEARCH_ENABLED": [
                        "true"
                    ]
                },
                "clientCustomProperties": {},
                "partnerCustomProperties": {
                    "5bd6c0c6e4b03983d42572d1": [
                        "English"
                    ]
                },
                "spaceCustomProperties": {},
                "userCustomProperties": {},
                "profileClientCustomProperties": {},
                "profilePartnerCustomProperties": {},
                "channelCustomProperties": {},
                "sourceType": "ACCOUNT",
                "assignedToUserId": [],
                "clientQueues": [],
                "partnerQueues": [],
                "sortField": {
                    "fieldName": "snCreatedTime",
                    "displayName": "Created Time",
                    "inboundMessageFilterKey": "snCreatedTime",
                    "order": "DESC"
                },
                "name": "Twitter Inbox",
                "columnColor": "#ccc",
                "autoRender": false,
                "locked": false,
                "additional": {
                    "refreshTime": "5"
                },
                "ownerUserId": 185370,
                "createdTime": "2019-03-04 02:10:28",
                "modifiedTime": "2019-05-14 17:45:41",
                "deleted": false
            },
            {
                "id": "5c7c8930e4b0b25907ef1bb5",
                "dashboardId": "5c7bdaf7e4b03d655cf612ca",
                "channel": "FACEBOOK",
                "type": "PRIVATE_MESSAGES",
                "tags": [],
                "properties": {
                    "WITH_BRAND_COMMENTS": [
                        "all"
                    ],
                    "SORT_ENABLED": [
                        "true"
                    ],
                    "ACCOUNT": [
                        "257708"
                    ],
                    "SOURCE_ID": [
                        "257708"
                    ],
                    "SHOW_COUNT": [
                        "true"
                    ],
                    "CATEGORY": [
                        "38",
                        "39"
                    ],
                    "POST_TYPE": [
                        "all"
                    ],
                    "TIME_RANGE_FILTER_KEY": [
                        "LIFETIME"
                    ],
                    "SEARCH_ENABLED": [
                        "true"
                    ]
                },
                "clientCustomProperties": {},
                "partnerCustomProperties": {
                    "5bd6c0c6e4b03983d42572d1": [
                        "English"
                    ]
                },
                "spaceCustomProperties": {},
                "userCustomProperties": {},
                "profileClientCustomProperties": {},
                "profilePartnerCustomProperties": {},
                "channelCustomProperties": {},
                "sourceType": "ACCOUNT",
                "clientQueues": [],
                "partnerQueues": [],
                "sortField": {
                    "fieldName": "snCreatedTime",
                    "displayName": "Created Time",
                    "inboundMessageFilterKey": "snCreatedTime",
                    "order": "DESC"
                },
                "name": "Facebook Inbox",
                "columnColor": "#ccc",
                "autoRender": true,
                "locked": false,
                "ownerUserId": 185370,
                "createdTime": "2019-03-04 02:10:56",
                "modifiedTime": "2019-03-04 02:22:37",
                "deleted": false
            },
            {
                "id": "5c7e76c6e4b03d655d46a739",
                "dashboardId": "5c7bdaf7e4b03d655cf612ca",
                "channel": "FACEBOOK",
                "type": "SHARES",
                "tags": [],
                "properties": {
                    "SORT_ENABLED": [
                        "true"
                    ],
                    "ACCOUNT": [
                        "257708"
                    ],
                    "SOURCE_ID": [
                        "257708"
                    ],
                    "SHOW_COUNT": [
                        "true"
                    ],
                    "CATEGORY": [
                        "227"
                    ],
                    "POST_TYPE": [
                        "all"
                    ],
                    "TIME_RANGE_FILTER_KEY": [
                        "LIFETIME"
                    ],
                    "SEARCH_ENABLED": [
                        "true"
                    ]
                },
                "clientCustomProperties": {},
                "partnerCustomProperties": {},
                "spaceCustomProperties": {},
                "userCustomProperties": {},
                "profileClientCustomProperties": {},
                "profilePartnerCustomProperties": {},
                "channelCustomProperties": {},
                "sourceType": "ACCOUNT",
                "clientQueues": [],
                "partnerQueues": [],
                "sortField": {
                    "fieldName": "snCreatedTime",
                    "displayName": "Created Time",
                    "inboundMessageFilterKey": "snCreatedTime",
                    "order": "DESC"
                },
                "name": "Shared posts",
                "columnColor": "#ccc",
                "autoRender": true,
                "locked": false,
                "ownerUserId": 196648,
                "createdTime": "2019-03-05 13:16:54",
                "modifiedTime": "2019-03-05 13:16:54",
                "deleted": false
            },
            {
                "id": "5cbf8089e4b0704c5cdf2c03",
                "dashboardId": "5c7bdaf7e4b03d655cf612ca",
                "channel": "TWITTER",
                "type": "CHANNEL_SEARCH",
                "tags": [],
                "properties": {
                    "LANGUAGE": [
                        "en"
                    ],
                    "SORT_ENABLED": [
                        "false"
                    ],
                    "ACCOUNT": [
                        "255156"
                    ],
                    "SOURCE_ID": [
                        "-1"
                    ],
                    "QUERY": [
                        "ubisoft"
                    ],
                    "SHOW_COUNT": [
                        "false"
                    ],
                    "SEARCH_ENABLED": [
                        "false"
                    ]
                },
                "clientCustomProperties": {},
                "partnerCustomProperties": {},
                "spaceCustomProperties": {},
                "userCustomProperties": {},
                "profileClientCustomProperties": {},
                "profilePartnerCustomProperties": {},
                "channelCustomProperties": {},
                "sourceType": "PERSISTENT_SEARCH",
                "clientQueues": [],
                "partnerQueues": [],
                "sortField": {
                    "fieldName": "snCreatedTime",
                    "displayName": "Created Time",
                    "inboundMessageFilterKey": "snCreatedTime",
                    "order": "DESC"
                },
                "name": "Twitter search",
                "columnColor": "#ccc",
                "autoRender": true,
                "locked": false,
                "ownerUserId": 189145,
                "createdTime": "2019-04-23 21:15:53",
                "modifiedTime": "2019-04-23 21:15:53",
                "deleted": false
            }
        ],
        "tags": [],
        "locked": false,
        "shared": false
    }







### Response Parameters







| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the dashboard. | String |
| name |  | Name of the dashboard. | String |
| shareConfigs |  | Shows sharing configurationeither local or global."shareLevel": "GLOBAL" | List of Object |
| columnOrder |  | Represents the number of column in your dashboard from left to right. | List of String |
| columns |  | Contains the params related to a column. | String |
|  | id | The id of the column. | String |
|  | dashboardId | Id of the Dashboard in which column is present | String |
|  | channel | Source type selected for coulmn. | String |
|  | type | The type of column within source type. | String |
|  | properties | Properties you selected while creating a column.like SORT_ENABLED, etc. | List of String |
|  | clientCustomProperties | Custom properties related to client. | Map<String, List <string>> |
|  | partnerCustomProperties | Custom properties related to partner. | Map<String, List <string>> |
|  | SpaceCustomProperties | Custom properties related to space env. | Map<String, List <string>> |
|  | userCustomProperties | Custom properties related to user. | Map<String, List <string>> |
|  | profileClientCustomProperties | Custom properties related to client profile. | Map<String, List <string>> |
|  | profilePartnerCustomProperties | Custom properties related to partner profile. | Map<String, List <string>> |
|  | channelCustomProperties | Custom properties related to native social channel. | Map<String, List <string>> |
|  | sourceType | The source type you selected while creating a column. | String |
|  | clientQueues | Queues corresponding to client. | List of String |
|  | partnerQueues | Queues corresponding to partner. | List of String |
|  | sortField | Sort metrics. like name, column color, auto render, locked, etc. | List of String |
| tags |  | Array of string for unique identification on web search. | List of String |
|  | locked | If true, locked. | Boolean |
|  | shared | If true, shared. | Boolean |

	[](https://dev.sprinklr.com/fetch-engagement-dashboard-v1)






[Back to top](https://dev.sprinklr.com/fetch-engagement-dashboard-v1)
