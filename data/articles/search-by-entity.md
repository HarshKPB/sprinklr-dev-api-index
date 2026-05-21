---
title: "Search by Entity"
slug: search-by-entity
url: https://dev.sprinklr.com/search-by-entity
---

# Search by Entity

# POST Search by Entity

You can use the Search API to fetch data on the basis of entity types using filters. In the response you will receive a cursor which can be used in the Search by Cursor API to fetch the next set of data.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/search/`{entityType}`

**Dev Note: ** Supported entity types: `MESSAGE, CASE, USER, OUTBOUND_MESSAGE, CAMPAIGN, SUB_CAMPAIGN, COMMENT, SOCIAL_ASSET, TASK, AUDIENCE_ACTIVITY, PROFILE, CUSTOM_FIELD, TRANSACTION`

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

## Request Parameters







-
-
-

``
****``

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| filter |  | Required | Filter to apply on the entity type |  |
|  | type | Required | You can choose from the available filter types. Supported types include: AND, OR, NOT, IN, GT, GTE, LT, LTE, NIN, EQUALS, NOT_EQUALS, CONTAINS. Refer to the table below for understanding the purpose of the given filter types | filterTypes |
|  | filters  type key values | Required | Filters represents the list of nested filters. Kindly note that the type of filter should match the provided key and values, it can be a list of filter types, the key on which you want to apply the filter, and the value of the key. It should match with the key. The supported combination of "key" and "type" are given below | List of Filter, String |
| timeFilter |  | OptionalRequired for MESSAGE entity type | The time filter object for filtering entities | Object |
|  | key | Required | The keys for timeFilter, i.e., channelCreatedTime or createdTime | String |
|  | since | Required | Time since when you want to fetch the results | yyyy - MM format |
|  | until | Required | Time until when you want to fetch the results | yyyy - MM format |
| sorts |  | Required | Sorting information. |  |
|  | key | Required | Key on the basis of which you want to sort the query. | String |
|  | order | Optional | Short in ascending or descending order.i.e. ASC and DESC. | String |
| Page |  | Required | Pagination information. |  |
|  | start | Optional | Specifies the starting index for pagination when retrieving records. Use this parameter to define the position from which the API should begin returning results. | Integer |
|  | size | Required | Size of the page to fetch in response. | Integer |
| includeCount |  | Optional | When set to true, the API response includes the total number of records available for the specified entity type. This helps determine the overall dataset size when implementing pagination. Developer Note:This is supported only for the Case entity type. | Boolean |


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

### Entity Type Supported Filters


-  MESSAGE

-  CASE

-  CAMPAIGN / SUB_CAMPAIGN

-  COMMENT

-  SOCIAL_ASSET

-  TASK

-  AUDIENCE_ACTIVITY

-  PROFILE

-  USER

-  OUTBOUND_MESSAGE

-  CUSTOM_FIELD

-  TRANSACTION

### Supported MESSAGE filters







``

``

``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| sourceType | IN, NIN, EQUALS, NOT_EQUALS |
| content.title | IN, NIN, EQUALS, NOT_EQUALS, CONTAINS |
| content.text | IN, SEARCH |
| channelType | IN, NIN, EQUALS, NOT_EQUALS |
| deleted | IN, NIN, EQUALS, NOT_EQUALS |
| enrichments.sentiment | IN, NIN, EQUALS, NOT_EQUALS, GT, GTE, LT, LTE |
| workflow.customProperties / workflow.spaceWorkflows.customProperties | IN, NIN, EQUALS, NOT_EQUALS |
| workflow.campaignId | IN, NIN, EQUALS, NOT_EQUALS |
| postId | IN, NIN, EQUALS, NOT_EQUALS |
| brandPost | EQUALS, NOT_EQUALS |
| sourceId | IN, NIN, EQUALS, NOT_EQUALS |
| caseNumber | IN, EQUALS |

### Supported MESSAGE timeFilter







``

``

| Key | Type |
| --- | --- |
| channelCreatedTime | LT, LTE, GT, GTE, EQUALS |
| createdTime | LT, LTE, GT, GTE, EQUALS |

### Supported CASE filters







``

``

``

``

``

``

****``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| caseNumber | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| externalCase.caseNumber | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| modifiedTime | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| contact.channelId | IN, NIN, EQUALS, NOT_EQUALS |
| workflow.customPropertiesSyntax Example: workflow.customProperties.{customProperty id} | IN, NIN, EQUALS, NOT_EQUALS |
| createdTime | LT, LTE, GT, GTE, EQUALS |
| deleted | EQUALS,NOT_EQUALS |
| externalCase.channelType | EQUALS,NOT_EQUALS,IN,NIN |
| workflow.queues.queueId | EQUALS,NOT_EQUALS,IN,NIN |
| latestProfileAUMSnCreatedTime | LT, LTE, GT, GTE, EQUALS |

### Supported SOCIAL_ASSET filters







``

``

``

``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, EQUALS, NOT_EQUALS |
| assetType | IN, NIN, EQUALS, NOT_EQUALS |
| assetSource | IN, NIN, EQUALS, NOT_EQUALS |
| status | IN, NIN, EQUALS, NOT_EQUALS |
| taxonomy.clientCustomProperties | IN, NIN, EQUALS, NOT_EQUALS |
| taxonomy.partnerCustomProperties | IN, NIN, EQUALS, NOT_EQUALS |
| restricted | IN, NIN, EQUALS, NOT_EQUALS |
| validity.availableFrom | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| validity.expiryTime | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| shareConfigs.type | IN, NIN, EQUALS, NOT_EQUALS |
| templateType | IN, NIN, EQUALS, NOT_EQUALS |
| name | SEARCH |
| channels | IN, NIN, EQUALS, NOT_EQUALS |

### Supported CAMPAIGN filters







``

``

``

``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, EQUALS, NOT_EQUALS |
| name | IN, NIN, CONTAINS |
| description | IN, NIN, CONTAINS |
| startDate | LT, LTE, GT, GTE, EQUALS |
| endDate | LT, LTE, GT, GTE, EQUALS |
| tags | IN, NIN, EQUALS, NOT_EQUALS |
| owner | IN, NIN, EQUALS, NOT_EQUALS |
| status | IN, NIN, EQUALS, NOT_EQUALS |
| archived | EQUALS, NOT_EQUALS |
| partnerCustomProperties | IN, NIN, EQUALS, NOT_EQUALS |
| clientCustomProperties | IN, NIN, EQUALS, NOT_EQUALS |
| createdTime | LT, LTE, GT, GTE, EQUALS |
| modifiedTime | LT, LTE, GT, GTE, EQUALS |

### Supported AUDIENCE_ACTIVITY filters







``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, CONTAINS |
| activityTime | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| accountId | IN, NIN, CONTAINS |
| messageId | IN, NIN, CONTAINS |
| activityType | IN, NIN, CONTAINS |
| channelType | IN, NIN, CONTAINS |

### Supported USER filters







``

``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| clientAttributes.userType | IN, NIN, EQUALS, NOT_EQUALS |
| clientAttributes.clientId | IN, NIN, EQUALS, NOT_EQUALS |
| clientAttributes.clientCustomProperties | IN, NIN, EQUALS, NOT_EQUALS |
| globalAttributes.partnerCustomProperties | IN, NIN, EQUALS, NOT_EQUALS |
| globalAttributes.federationId | IN, NIN, EQUALS, NOT_EQUALS |
| globalAttributes.passwordLoginDisabled | IN, NIN, EQUALS, NOT_EQUALS |
| userName | IN, NIN, EQUALS, NOT_EQUALS |
| active | IN, NIN, EQUALS, NOT_EQUALS |
| meta.lastModified | LT, LTE, GT, GTE, EQUALS |
| meta.createdTime | LT, LTE, GT, GTE, EQUALS |

### Supported TASK filters







``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, EQUALS, NOT_EQUALS |
| taskStatus | IN, NIN, EQUALS, NOT_EQUALS |
| title | IN, NIN |
| taskType | IN, NIN, EQUALS, NOT_EQUALS |
| assetId | IN, NIN, EQUALS, NOT_EQUALS |
| customProperties | IN, NIN, EQUALS, NOT_EQUALS |
| assetType | IN, NIN, EQUALS, NOT_EQUALS |
| dueDate | LT, LTE, GT, GTE, EQUALS |
| createdTime | LT, LTE, GT, GTE, EQUALS |
| modifiedTime | LT, LTE, GT, GTE, EQUALS |

### Supported COMMENT Filters







``

``

``

``

| Key | Type |
| --- | --- |
| createdTime | LT, LTE, GT, GTE, EQUALS |
| includeReplyOnComments | EXISTS → true/false |
| entityId(caseNumber, messageId, profileId) | IN, NIN, EQUALS, NOT_EQUALS |
| entityType(UNIVERSAL_CASE/MESSAGE_WORKFLOW/PROFILE_WORKFLOW) | IN, NIN, EQUALS, NOT_EQUALS |

**Dev Notes: **entityId and entityType are required filter types when searching for a comment

### Supported PROFILE filters







``

``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, EQUALS, NOT_EQUALS, LT, LTE, GT, GTE |
| channelType | IN, NIN, CONTAINS |
| channelId | IN, NIN, CONTAINS |
| profileWorkflow.customProperties | IN, NIN, EQUALS, NOT_EQUALS |
| profileWorkflow.profileSpaceWorkflows.customProperties | IN, NIN, EQUALS, NOT_EQUALS |
| createdTime | LT, LTE, GT, GTE, EQUALS |
| modifiedTime | LT, LTE, GT, GTE, EQUALS |
| profileWorkflow.profileLists | IN, NIN, EQUALS, NOT_EQUALS |
| profileWorkflow.profileSpaceWorkflows.profileLists | IN, NIN, EQUALS, NOT_EQUALS |
| contact.email | IN, NIN, EQUALS, NOT_EQUALS |
| contact.phoneNo | IN, NIN, EQUALS, NOT_EQUALS |

### Supported OUTBOUND_MESSAGE filters







``

``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| templateId | IN, NIN |
| createdDate | GTE, LTE, BETWEEN |
| createdTime | GTE, LTE, BETWEEN |
| scheduleDate | GTE, LTE, BETWEEN |
| scheduleTime | GTE, LTE, BETWEEN |
| modifiedDate | LTE, GTE, BETWEEN |
| modifiedTime | LTE, GTE, BETWEEN |
| publishedDate | GTE, LTE, BETWEEN |
| publishedTime | GTE, LTE, BETWEEN |
| searchDetails.customProperties | IN, NIN |
| status | IN, NIN |


**Dev Note: **To apply customProperties filter:
"filters": [
            {
                "type": "IN",
                "key": "workflow.customProperties.5e4e5f3954e68b2a475c05b6",
                "values": [
                    "Andhra Pradesh"
                ]
            }
        ]

### Supported CUSTOM FIELD Filters







``

``

``

``

``

``

``

``

``

``

| Key | Type |
| --- | --- |
| id | IN, NIN, EQUALS, NOT_EQUALS |
| clientId | IN, NIN, EQUALS, NOT_EQUALS |
| assetTypes | IN, NIN, EQUALS, NOT_EQUALS |
| category | IN, NIN, EQUALS, NOT_EQUALS |
| fieldName | IN, NIN, EQUALS, NOT_EQUALS |
| type | IN, NIN, EQUALS, NOT_EQUALS |
| label | IN, NIN, EQUALS, NOT_EQUALS |
| enabled | IN, NIN, EQUALS, NOT_EQUALS |
| modifiedTime | LT, LTE, GT, GTE, EQUALS |
| createdTime | LT, LTE, GT, GTE, EQUALS |

### Supported TRANSACTION Filter







``

``

| Key | Type |
| --- | --- |
| transactionGroupId | IN, NIN, EQUALS, NOT_EQUALS |
| Id | IN, NIN, EQUALS, NOT_EQUALS |


## Example 1: Entity Type - SOCIAL_ASSET














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/SOCIAL_ASSET' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "filter":{
        "type":"AND",
        "filters":[{
            "type":"EQUALS",
            "key":"assetType",
            "values":["PHOTO"]
        },
        {
        "key":"status",
        "values":["APPROVED"],
            "type": "IN"
        }]
    },
    "sorts":[{
        "key":"id",
        "order": "DESC"
    }],
    "page":{
        "size": 10
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "5d761ddd642f3d466ba32e7e",
                "name": "title",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/title-f6bfb54a-1105-478d-b2cc-bcf9a975f8af-2136884405.jpg",
                    "title": "title",
                    "description": "title",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 3.0,
                    "LINKEDIN_COMPANY_POST_IMPRESSIONS_COUNT": 0.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 0.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568014121327,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d762a596df5636b24e563df",
                "name": "title",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/title-f2e336fe-c411-4427-b7ff-e9e4d80c0137-2136884405.jpg",
                    "title": "title",
                    "description": "title",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 3.0,
                    "LINKEDIN_COMPANY_POST_IMPRESSIONS_COUNT": 0.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568026828310,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            },
            {
                "id": "5d761e866df5636b24df4204",
                "name": "hello",
                "description": "",
                "assetType": "PHOTO",
                "status": "Approved",
                "attachment": {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/https___testproxy-qa4.sprinklr-e8cd76d4-4cbf-4396-a383-01d888b92cf5-61632744.jpg",
                    "type": "IMAGE"
                },
                "taxonomy": {
                    "campaignId": "2_11"
                },
                "insights": {
                    "POST_COMMENT_COUNT": 0.0,
                    "FOLLOWER_COUNT_AT_POST": 33.0,
                    "TOTAL_ENGAGEMENT": 0.0,
                    "POST_REACH_COUNT": 0.0,
                    "POST_LIKE_COUNT": 0.0,
                    "POST_SHARE_COUNT": 0.0,
                    "ENGAGEMENT_METRICS": 0.0
                },
                "validity": {
                    "expiryTime": 2208988800000,
                    "availableFrom": 1568004190000,
                    "neverExpire": false
                },
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "CLIENT",
                        "ids": [
                            "2"
                        ]
                    }
                ],
                "restricted": false
            }
        ],
        "cursor": "id=5dd2699aaf47f50001d3299d"
    },
    "errors": []
}





**Dev Note: ** The `cursor` you get in the response will be used in the [Search by Cursor API](https://dev.sprinklr.com/search-by-cursor) to fetch the next set of data.

## Example 2: Entity Type - CAMPAIGN














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/CAMPAIGN' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter":{
        "type":"AND",
        "filters":[
         {
        "type":"NIN",
        "key":"name",
        "values":["test"]
        },
        {
        "key":"status",
        "values":["DRAFT"],
            "type": "IN"
        },
        {
        "key":"archived",
        "values":["true"],
            "type": "EQUALS"
        },
        {
        "key":"startDate",
        "values":[1553222256404],
            "type": "GTE"
        },
        {
        "key":"endDate",
        "values":[1599562732566],
            "type": "LTE"
        },
        {
        "key":"description",
        "values":["Testing"],
            "type": "NIN"
        }]
    },
    "sorts":[{
        "key":"createdTime",
        "order": "DESC"
    }],
    "page":{
        "size": 10
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "4_2558",
                "name": "Campaign_New1591297808492",
                "description": "Campaign_New1591297808492_Description",
                "createdTime": 1591297898987,
                "modifiedTime": 1596704001531,
                "startDate": 1591536540000,
                "endDate": 1591795740000,
                "tags": [
                    "Nike",
                    "Ajeya"
                ],
                "owner": 600000034,
                "partnerCustomProperties": {
                    "5eccd4d41d8cc46356a764d3": [
                        "Updated",
                        "Macro"
                    ],
                    "5ec68d9c664fa72b5c92d264": [
                        "C1"
                    ],
                    "5cb04a61e4b0236917610910": [
                        "1"
                    ],
                    "5ddfb43e7edc2035533d40b3": [
                        "Bangalore"
                    ],
                    "5bf6b0a1e4b01d5346ac9ded": [
                        "5dde6b66c7a0e37beda140ab",
                        "5c331bb1e4b01f952b049875"
                    ],
                    "5ec68ddd664fa72b5c92d561": [
                        "C'22"
                    ],
                    "5ea68df81ff1472cdd59e380": [
                        "1592728380000"
                    ],
                    "5bf6adb2e4b0d3d98bda7eeb": [
                        "Jammu KASHMIR"
                    ],
                    "5bf6adfae4b01d5346ac99bc": [
                        "600000033"
                    ],
                    "spr_campaign_goal": [
                        "Product Awareness"
                    ],
                    "5ea68e5d1ff1472cdd59e9a8": [
                        "Two",
                        "Three"
                    ]
                },
                "status": "DRAFT",
                "archived": true
            },
            {
                "id": "4_1135",
                "name": "30 it",
                "createdTime": 1569921924219,
                "modifiedTime": 1592562739079,
                "startDate": 1569921914790,
                "endDate": 1569921900000,
                "owner": 600000034,
                "partnerCustomProperties": {
                    "5bf6adb2e4b0d3d98bda7eeb": [
                        "BanGAlore"
                    ],
                    "5bf6aeb5e4b01d5346ac9b30": [
                        "600000087"
                    ]
                },
                "status": "DRAFT",
                "archived": true
            },
            {
                "id": "4_1133",
                "name": "24",
                "createdTime": 1569921264555,
                "modifiedTime": 1592562746004,
                "startDate": 1574590440000,
                "endDate": 1574590500000,
                "owner": 600000034,
                "partnerCustomProperties": {
                    "5bf6adb2e4b0d3d98bda7eeb": [
                        "BanGAlore"
                    ],
                    "5bf6aeb5e4b01d5346ac9b30": [
                        "600000087"
                    ]
                },
                "status": "DRAFT",
                "archived": true
            },
            {
                "id": "4_1131",
                "name": "30-11111111",
                "createdTime": 1569921145330,
                "modifiedTime": 1592562753654,
                "startDate": 1569834720000,
                "endDate": 1569921120000,
                "owner": 600000034,
                "partnerCustomProperties": {
                    "5bf6adb2e4b0d3d98bda7eeb": [
                        "BanGAlore"
                    ],
                    "5bf6aeb5e4b01d5346ac9b30": [
                        "600000087"
                    ]
                },
                "status": "DRAFT",
                "archived": true
            },
            {
                "id": "4_1127",
                "name": "15-18",
                "createdTime": 1569918716618,
                "modifiedTime": 1592562770814,
                "startDate": 1573806660000,
                "endDate": 1574065920000,
                "owner": 600000034,
                "partnerCustomProperties": {
                    "5bf6adb2e4b0d3d98bda7eeb": [
                        "BanGAlore"
                    ],
                    "5bf6aeb5e4b01d5346ac9b30": [
                        "600000087"
                    ]
                },
                "status": "DRAFT",
                "archived": true
            }
        ],
        "cursor": "id=5f3e6bd4673bdd3d0b25329d"
    },
    "errors": []
}





## Example 3: Entity Type - CASE














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/CASE' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter": {
        "type": "AND",
        "filters": [
            {
                "type": "IN",
                "key": "caseNumber",
                "values": [
                    "8919793", "11495562","12223686"
                ]
            }
        ]
    },
    "page": {
        "start": 1,
        "size": 2
    },
    "includeCount":true
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "6899f8a4d948bc4ac3623331",
                "caseNumber": 8919793,
                "subject": "#8919793 Instagram test",
                "description": "test",
                "version": 60,
                "externalCase": {
                    "id": "500Ig00000ELKwiIAH",
                    "caseNumber": "00012198",
                    "channelType": "SALESFORCE",
                    "permalink": "https://sprinklr-2a-dev-ed.develop.my.salesforce.com/500Ig00000ELKwiIAH",
                    "createdTime": 1758704343000,
                    "modifiedTime": 1758704343000
                },
                "externalCaseInfo": {
                    "externalCases": []
                },
                "workflow": {
                    "customProperties": {
                        "_c_682337c8200a494ab9bec5c9": [
                            "test"
                        ],
                        "_c_65252be5825bb637b9857139": [
                            "147258"
                        ]
                    },
                    "queues": [
                        {
                            "queueId": 100022,
                            "assignmentTime": 1758462541707
                        },
                        {
                            "queueId": 101517,
                            "assignmentTime": 1758462541707
                        }
                    ]
                },
                "channelCustomProperties": [],
                "contact": {
                    "id": "INSTAGRAM_39463695228",
                    "channelType": "INSTAGRAM",
                    "fromSnUserId": "39463695228"
                },
                "createdTime": 1754921124610,
                "modifiedTime": 1759834275823,
                "firstMessageId": "ACCOUNT_600037626_1754921106000_INSTAGRAM_36_3696868581603797985_39463695228",
                "sentiment": 0,
                "latestProfileMessageAssociatedTime": 1758462515000,
                "firstMessageAssociatedTime": 1754921106000,
                "latestMessageAssociatedTime": 1758462515000,
                "firstUserBrandResponseCreationTime": 1754921106000,
                "totalProcessingClockTime": 127147555,
                "allEngagedUsersList": [],
                "associatedFanMessageCount": 0,
                "associatedBrandMessageCount": 2,
                "associatedUserBrandMessageCount": 2,
                "deleted": false,
                "conversationIntentIds": []
            }
        ],
        "count": 3
    },
    "errors": []
}





## Example 4: Entity Type - TASK














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/TASK' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
       "filter":
       {
        "type":"AND",
        "filters":[
        {
        "key":"assetType",
        "values":["OUTBOUND_MESSAGE"],
            "type": "IN"
        },
        {
        "key":"taskStatus",
        "values":["NEW","APPROVED"],
            "type": "IN"
        },
         {"key":"title",
        	"values":["task"],
        	"type" : "IN"
        },
        {"key":"taskType",
        	"values":["Design Task"],
        	"type" : "IN"
        },
        {"key":"dueDate",
        	"values":["1596096420000"],
        	"type" : "LTE"
        }
    ,
         {"key":"modifiedTime",
        	"values":["1593677264945"],
        	"type" : "LTE"
        },
         {"key":"createdTime",
        	"values":["1593677264945"],
        	"type" : "LT"
        }
        ]
    },
    "sorts":[{
        "key":"modifiedTime",
        "order": "DESC"
    }],
    "page":{
        "size": 10
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "5da568af7edc2075a14a0c7e",
                "assignment": {},
                "taskType": "Design Task",
                "taskStatus": "NEW",
                "title": "task",
                "assetId": "MESSAGE_700000001258202",
                "assetType": "OUTBOUND_MESSAGE",
                "dueDate": 1571121300000,
                "customProperties": {
                    "5bf6aeb5e4b01d5346ac9b30": [],
                    "5bf6ac70e4b0d3d98bda7bb4": [
                        "Is Variant Condition satisfied but author condition not satisfied"
                    ],
                    "5bf6ae59e4b0d3d98bda80a0": [],
                    "5d6685057edc202c4c6f1d50": [],
                    "spr_task_status": [
                        "New"
                    ],
                    "5d382e5cc7a0e321bf009d6b": [],
                    "5bf6ac28e4b01d5346ac95b0": [],
                    "spr_task_type": [
                        "Design Task"
                    ],
                    "5bf6b03fe4b0d3d98bda84b2": [],
                    "5d3831f4c7a0e321bf00f97a": [],
                    "5d77761ac7a0e336585b78d8": [],
                    "5bf6b0a1e4b01d5346ac9ded": [],
                    "5bf6ad45e4b0d3d98bda7dfb": [
                        "Campaign"
                    ],
                    "5bf6af77e4b0d3d98bda823c": [],
                    "5bf6adb2e4b0d3d98bda7eeb": [
                        "Noida"
                    ],
                    "5bf6adfae4b01d5346ac99bc": [],
                    "5d8c8c9f7edc203dcb2cec10": [],
                    "5d777224c7a0e336585a0584": [],
                    "5d130203f9e3b77f0811be3b": [],
                    "5eccd4341d8cc46356a75eb4": [
                        "Not Satisfied "
                    ]
                },
                "inactive": false,
                "queueDetails": [],
                "createdTime": 1571121327382,
                "modifiedTime": 1592491179562
            }
        ]
    },
    "errors": []
}





## Example 5: Entity Type - MESSAGE














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/MESSAGE' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter": {
        "type": "AND",
        "filters": [
            {
                "type": "NOT_EQUALS",
                "key": "brandPost",
                "values": [
                    "true"
                ]
            },
            {
                "type": "EQUALS",
                "key": "sourceType",
                "values": [
                    "ACCOUNT"
                ]
            }
        ]
    },
     "timeFilter":{
        "key":"channelCreatedTime",
        "since":1601541365000,
        "until":1603787765000
    },
    "page": {
        "size": 10
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "sourceType": "ACCOUNT",
                "sourceId": 1000071593,
                "content": {
                    "text": "test text"
                },
                "channelMessageId": "1321007651849826304",
                "channelType": "TWITTER",
                "accountType": "TWITTER",
                "channelCreatedTime": 1603787741000,
                "senderProfile": {
                    "name": "Test",
                    "channelType": "TWITTER",
                    "channelId": "29958928",
                    "permalink": "https://twitter.com/TOIIndiaNews",
                    "avatarUrl": "https://pbs.twimg.com/profile_images/1282407636/icon_512.png",
                    "bio": "Latest news from all over the country brought to by India’s No.1 digital news destination https://t.co/VSKi1mkZBr",
                    "followers": 1649458,
                    "username": "test123",
                    "verified": true,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "receiverProfile": {
                    "name": "TOI India",
                    "channelType": "TWITTER",
                    "channelId": "29958928",
                    "permalink": "https://twitter.com/TOIIndiaNews",
                    "avatarUrl": "https://pbs.twimg.com/profile_images/1282407636/icon_512.png",
                    "bio": "Latest news from all over the country brought to by India’s No.1 digital news destination https://t.co/VSKi1mkZBr",
                    "followers": 1649458,
                    "username": "TOIIndiaNews",
                    "verified": true,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "permalink": "https://twitter.com/TOIIndiaNews/status/1321007651849826304",
                "language": "en",
                "messageId": "ACCOUNT_1000071593_1603787741000_TWITTER_2_1321007651849826304",
                "brandPost": false,
                "createdTime": 1603787792259,
                "modifiedTime": 1603800616951,
                "textEntities": {
                    "message": [
                        {
                            "indices": [
                                80,
                                103
                            ],
                            "url": "https://t.co/rK4jarXoXf"
                        }
                    ]
                },
                "location": {
                    "lat": 0.0,
                    "lon": 0.0
                },
                "insights": {
                    "FOLLOWER_COUNT_AT_POST": 1628413.0,
                    "POST_REACH_COUNT": 1634692.0,
                    "POST_LIKE_COUNT": 6.0,
                    "POST_SHARE_COUNT": 4.0
                },
                "workflow": {},
                "enrichments": {
                    "sentiment": -1
                },
                "conversationId": "1321007651849826304",
                "autoImported": false
            },
            {
                "sourceType": "ACCOUNT",
                "sourceId": 1000067567,
                "content": {
                    "text": "Indian Army going out of its way to have terrorists surrender. \n\nDetails by Sohil. https://t.co/7AMBP4duFS",
                    "attachment": {
                        "url": "https://video.twimg.com/amplify_video/1321004988756156416/vid/1280x720/r4T1CHTMA6DWRKVu.mp4?tag=13",
                        "previewUrl": "https://pbs.twimg.com/amplify_video_thumb/1321004988756156416/img/gWLeqz2uCpcFGZmx.jpg",
                        "type": "VIDEO",
                        "attachmentOptions": [
                            {
                                "embeddable": true,
                                "channelType": "TWITTER"
                            }
                        ]
                    }
                },
                "channelMessageId": "1321005039935057920",
                "channelType": "TWITTER",
                "accountType": "TWITTER",
                "channelCreatedTime": 1603787119000,
                "senderProfile": {
                    "name": "TIMES NOW",
                    "channelType": "TWITTER",
                    "channelId": "240649814",
                    "permalink": "https://twitter.com/TimesNow",
                    "avatarUrl": "https://pbs.twimg.com/profile_images/1295231274366509057/ip_k3ncs.jpg",
                    "bio": "TIMES NOW is India’s most watched English news channel. Follow for lightning fast #BreakingNews and #Alerts.",
                    "followers": 9912540,
                    "username": "TimesNow",
                    "verified": true,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "receiverProfile": {
                    "name": "TIMES NOW",
                    "channelType": "TWITTER",
                    "channelId": "240649814",
                    "permalink": "https://twitter.com/TimesNow",
                    "avatarUrl": "https://pbs.twimg.com/profile_images/1295231274366509057/ip_k3ncs.jpg",
                    "bio": "TIMES NOW is India’s most watched English news channel. Follow for lightning fast #BreakingNews and #Alerts.",
                    "followers": 9912540,
                    "username": "TimesNow",
                    "verified": true,
                    "unSubscribed": false,
                    "deleted": false,
                    "snCreatedTime": 0,
                    "snModifiedTime": 0
                },
                "permalink": "https://twitter.com/TimesNow/status/1321005039935057920",
                "language": "en",
                "messageId": "ACCOUNT_1000067567_1603787119000_TWITTER_2_1321005039935057920",
                "brandPost": false,
                "createdTime": 1603787135656,
                "modifiedTime": 1603808070263,
                "textEntities": {
                    "message": [
                        {
                            "indices": [
                                83,
                                106
                            ],
                            "url": "https://t.co/7AMBP4duFS"
                        }
                    ]
                },
                "location": {
                    "lat": 0.0,
                    "lon": 0.0
                },
                "insights": {
                    "POST_COMMENT_COUNT": 2.0,
                    "FOLLOWER_COUNT_AT_POST": 9872723.0,
                    "POST_REACH_COUNT": 9891849.0,
                    "POST_LIKE_COUNT": 84.0,
                    "POST_SHARE_COUNT": 13.0
                },
                "workflow": {},
                "enrichments": {
                    "sentiment": -1
                },
                "conversationId": "1321005039935057920",
                "autoImported": false
            }
        ],
        "cursor": "id=5fdb8e4c3d859b3f282a9ced"
    },
    "errors": []
}





##
Example 6: Entity Type - AUDIENCE_ACTIVITY














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/AUDIENCE_ACTIVITY' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter": {
        "type": "AND",
        "filters": [
            {
                "type": "IN",
                "key": "activityType",
                "values": [
                    "like"
                ]
            },
            {
                "type": "IN",
                "key": "accountId",
                "values": [
                    "123000"
                ]
            },
            {
                "type": "IN",
                "key": "messageId",
                "values": [
                    "LINKEDIN_70_6823923551947644928"
                ]
            },
            {
                "type": "IN",
                "key": "channelType",
                "values": [
                    "LINKEDIN"
                ]
            }
        ]
    },
   "timeFilter": {
        "key": "activityTime",
        "since": 1626993138000,
        "until": 1627252338000
    },
    "page":{
        "size": 10
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "64EBEC2BC7690865B9CE0FCBD9C1ADB1",
                "actorProfile": {
                    "id": "60fd60faddf7722d41ffe131",
                    "contact": {
                        "firstName": "userFirstName",
                        "lastName": "userLastName",
                        "fullName": "userFirstName userLastName"
                    },
                    "profiles": [
                        {
                            "name": "userFirstName userLastName",
                            "channelType": "LINKEDIN",
                            "channelId": "hG3wPIVtSe",
                            "permalink": "https://www.linkedin.com/in/userFirstName-userLastName-64b6b220/",
                            "avatarUrl": "https://media-exp1.licdn.com/dms/image/C5603AQG7T5FCsw7IXw/profile-displayphoto-shrink_800_800/0/1613475004493?e=1632960000&v=beta&t=pyxnlMm_Fxax_-skoMd0owjG-SddL9P1Ij3T4Vts_Y0",
                            "followers": 0,
                            "following": 0,
                            "username": "userFirstName userLastName",
                            "unSubscribed": false,
                            "deleted": false,
                            "snCreatedTime": 0,
                            "snModifiedTime": 0
                        }
                    ],
                    "profileWorkflow": {
                        "profileLists": [],
                        "customProperties": {
                            "5b2bf053e4b0cde609a8191b": [
                                "B"
                            ]
                        },
                        "profileSpaceWorkflows": []
                    },
                    "createdTime": 1627218170356,
                    "modifiedTime": 1627218170890
                },
                "objectId": "LINKEDIN_70_6823923551947644928",
                "object": {
                    "sourceType": "ACCOUNT",
                    "sourceId": 123000,
                    "content": {
                        "text": "yup done by the way how are you doing?"
                    },
                    "channelMessageId": "6823923551947644928",
                    "channelType": "LINKEDIN",
                    "accountType": "LINKEDIN_COMPANY",
                    "channelCreatedTime": 1626950157153,
                    "senderProfile": {
                        "name": "Durga",
                        "channelType": "LINKEDIN",
                        "channelId": "kQ-5S0O1HE",
                        "permalink": "https://www.linkedin.com/in/durga-75909820b/",
                        "followers": 0,
                        "following": 0,
                        "username": "Durga",
                        "unSubscribed": false,
                        "deleted": false,
                        "snCreatedTime": 0,
                        "snModifiedTime": 0
                    },
                    "receiverProfile": {
                        "name": "Cold Coffee House",
                        "channelType": "LINKEDIN",
                        "channelId": "31128678",
                        "permalink": " ",
                        "avatarUrl": " ",
                        "followers": 291,
                        "following": 0,
                        "username": "cold-coffee-house",
                        "unSubscribed": false,
                        "deleted": false,
                        "snCreatedTime": 0,
                        "snModifiedTime": 0
                    },
                    "permalink": " ",
                    "language": "en",
                    "messageId": "ACCOUNT_123000_1626950157153_LINKEDIN_70_6823923551947644928",
                    "postId": 5203559964,
                    "brandPost": false,
                    "createdTime": 1626957575814,
                    "modifiedTime": 1627278436724,
                    "textEntities": {},
                    "insights": {},
                    "workflow": {
                        "modifiedTime": 1627299757186,
                        "customProperties": {},
                        "queues": [],
                        "spaceWorkflows": [],
                        "campaignId": "4706_2"
                    },
                    "enrichments": {
                        "sentiment": 0,
                        "engageable": false
                    },
                    "conversationId": "urn:li:ugcPost:6823923276096536576",
                    "parentMessageId": "ACCOUNT_123000_1626950091454_LINKEDIN_68_urn:li:ugcPost:6823923276096536576",
                    "autoImported": true,
                    "autoResponse": false
                },
                "accountId": 123000,
                "channelType": "LINKEDIN",
                "activityData": {
                    "brandLink": false,
                    "type": "like",
                    "id": "urn:li:like:(urn:li:person:hG3wPIVtSe,urn:li:comment:(ugcPost:6823923276096536576,6823923551947644928))"
                },
                "activityType": "like",
                "activityTime": 1627218009623
            }
        ],
        "cursor": "id=61125ee56c45be7982a5de35"
    },
    "errors": []
}





##
Example 7: Entity Type - PROFILE














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/PROFILE' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter":{
        "type":"AND",
        "filters":[{
            "type":"IN",
            "key":"channelType",
            "values":["WHATSAPP_BUSINESS"]
        },
        {
        "key":"channelId",
        "values":["8826000001"],
            "type": "IN"
        }]
    },
    "sorts":[{
        "key":"modifiedTime",
        "order": "DESC"
    }],
    "page":{
        "size": 10
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "612e7b46794a79c9c6c14fd2",
                "contact": {
                    "fullName": "Test",
                    "phoneNo": "882600000111"
                },
                "demographics": {
                    "location": "Brazil",
                    "gender": "Male"
                },
                "profiles": [
                    {
                        "name": "Test L4",
                        "channelType": "WHATSAPP_BUSINESS",
                        "channelId": "8826000001",
                        "permalink": "https://twitter.com/non",
                        "bio": "Singer",
                        "followers": 0,
                        "following": 0,
                        "username": "Test L9",
                        "unSubscribed": false,
                        "deleted": false,
                        "snCreatedTime": 0,
                        "snModifiedTime": 0
                    }
                ],
                "profileWorkflow": {
                    "profileLists": [],
                    "customProperties": {},
                    "profileSpaceWorkflows": []
                },
                "createdTime": 1630436166902,
                "modifiedTime": 1630436166901
            }
        ]
    },
    "errors": []
}





## Example 8: Entity Type - USER














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/USER' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
	"filter": {
        "type": "AND",
        "filters": [
            {
                "type": "IN",
                "key": "active",
                "values": [
                    "true"
                ]
            },
            {
                "type": "IN",
                "key": "globalAttributes.partnerCustomProperties.spr_user_availability_status",
                "values": [
                    "Available"
                ]
            },
            {
                "type": "IN",
                "key": "userName",
                "values": [
                ]
            }
            ]
	},
	"page": {
		"size": 10
	}
}'





## Example - Response





{
    "data": {
{
       "results": [
           {
               "schemas": [
                   "urn:ietf:params:scim:schemas:core:2.0:User",
                   "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                   "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User"
               ],
               "id": "1000140488",
               "externalId": "",
               "lyearnId": "",
               "userPermissions": [],
               "accessibleClientIds": [],
               "userName": "cat.s@hotmail.com",
               "name": {
                   "familyName": "A sint nam voluptatem minus sint excepturi.",
                   "givenName": "Repellendus explicabo quae error dolorem."
               },
               "photos": [
                   {
                       "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png",
                       "primary": true
                   }
               ],
               "active": true,
               "locale": "en_US",
               "globalAttributes": {
                   "partnerCustomProperties": {
                       "spr_user_availability_status": [
                           "Available"
                       ],
                       "595e9c31e4b0c05cc4bf746b": [
                           "Tech"
                       ],
                       "595e9c00e4b0c05cc4bf744c": [
                           "Bangalore"
                       ],
                       "5a056a34e4b05d59a02b1ded": [
                           "logged_in_user"
                       ],
                       "_c_606a938d4bb7530840519a7c": [
                           "A"
                       ],
                       "_c_606a93ed4bb7530840519ba3": [
                           "1"
                       ]
                   },
                   "productSeat": "SOCIAL_CLOUD",
                   "passwordLoginDisabled": false
               },
               "clientAttributes": [
                   {
                       "clientId": 1000004657,
                       "userType": "PRTADMN",
                       "phoneNumbers": [
                           {
                               "primary": true
                           }
                       ],
                       "businessCategory": "CORPORATE",
                       "designation": "Desc:Ipsa tempora voluptatem id non aliquam asperiores vitae."
                   }
               ],
               "meta": {
                   "resourceType": "User",
                   "createdTime": "2022-01-05 11:01:36",
                   "lastModified": "1970-01-01 00:00:00"
               }
           }
       ],
       "cursor": "id=62b2c696362c231a5aa483dd"
   },
   "errors": []
}





## Example 9: Entity Type - COMMENT














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/COMMENT' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter": {
        "type": "AND",
        "filters": [
            {
                "type": "IN",
                "key": "entityType",
                "values": [
                    "UNIVERSAL_CASE"
                ]
            },
            {
                "type": "IN",
                "key": "entityId",
                "values": [
                    "829"
                ]
            },
            {
                "type": "EXISTS",
                "key": "includeReplyOnComments",
                "values": [
                    "false"
                ]
            }
        ]
    },
    "page": {
        "size": 2
    },
     "sorts": [
        {
            "key": "createdTime",
            "order": "ASC"
        }
    ]
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "64e5febee06bd348943340bc",
                "text": "
note1
",
                "commentingUser": 66000101,
                "createdTime": 1692794558032,
                "modifiedTime": 1692794558032,
                "entityType": "CASE",
                "entityId": "829",
                "conversationId": "19:6d1c3966-4da1-4eb6-9ee7-b07d72756abf_b1fc70a6-3878-4635-9462-29564f60fa6d@unq.gbl.spaces",
                "externalComment": {
                    "channelType": "MICROSOFT_TEAMS"
                }
            }
        ],
        "cursor": "id=64fb032043c117552cf6df89"
    },
    "errors": []
}





##
Example 10: Entity Type - OUTBOUND_MESSAGE














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/OUTBOUND_MESSAGE' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter": {
        "type": "AND",
        "filters": [
            {
                "type": "LTE",
                "key": "modifiedDate",
                "values": [
                    1697850751013
                ]
            }
        ]
    },
    "page": {
        "size": 100
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": 2152127216,
                "accountIds": [],
                "version": 11,
                "accountTypes": [],
                "variantDetails": {
                    "variant": false,
                    "variantParentMessageId": "MESSAGE_2152127216",
                    "hasVariants": false
                },
                "content": {
                    "text": "Update Draft API2 POST without accountId 2023-10-20 23:02:22.635",
                    "isRichText": false
                },
                "channelOptions": [],
                "scheduleDate": 1697842948625,
                "taxonomy": {
                    "campaignId": "1000004509_1594"
                },
                "status": "DRAFT",
                "autoResponse": false,
                "createdTime": 1697842941238,
                "modifiedTime": 1697842948625,
                "authorId": 1000063395
            },
            {
                "id": 2152127215,
                "accountIds": [
                    1000074726
                ],
                "version": 11,
                "accountTypes": [
                    "TWITTER"
                ],
                "variantDetails": {
                    "variant": false,
                    "variantParentMessageId": "MESSAGE_2152127215",
                    "hasVariants": false
                },
                "content": {
                    "text": "2023-10-20 23:02:12.892",
                    "isRichText": false
                },
                "channelOptions": [],
                "scheduleDate": 1697842938891,
                "taxonomy": {
                    "campaignId": "1000004509_1594"
                },
                "status": "DRAFT",
                "autoResponse": false,
                "createdTime": 1697842931463,
                "modifiedTime": 1697842938892,
                "authorId": 1000063395
            }
        ],
        "cursor": "id=664b472a5ade502cf7d2bd3a"
    },
    "errors": []
}





## Example 11: Entity Type - CUSTOM_FIELD














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/CUSTOM_FIELD' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter": {
        "type": "AND",
        "filters": [
            {
"type": "IN",
        "key": "assetTypes",
        "values": [
            "SURVEY"
        ]
            }
        ]
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "66a9c4e20ed459552eeb342c",
                "fieldName": "_c_66a9c4e20ed459552eeb3428",
                "label": "Label Test",
                "assetTypes": [
                    "SURVEY"
                ],
                "type": "NUMBER",
                "values": [],
                "enabled": true,
                "visibility": {
                    "globallyVisible": true,
                    "visibilityConfig": []
                },
                "permissions": [],
                "optionType": "GENERAL",
                "accessibleClientIds": [
                    66000004
                ],
                "createdTime": "Jul 31, 2024, 05:00:18 AM",
                "modifiedTime": "Jul 31, 2024, 05:00:18 AM"
            }
        ],
        "cursor": "id=66a9eb200358627a76a1d4ed"
    },
    "errors": []
}






## Example 12: Entity Type - TRANSACTION














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/search/TRANSACTION' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "filter": {
        "type": "AND",
        "filters": [
            {
                "type": "IN",
                "key": "transactionGroupId",
                "values": [
                    "6867b32dc8ff014fb8f12309"
                ]
            }
        ]
    },
    "sorts": [
        {
            "key": "id",
            "order": "ASC"
        }
    ],
    "page": {
        "size": 3
    }
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "id": "68b578d2c5fba01bb3cfa290",
                "transactionGroupId": "6867b32dc8ff014fb8f12309",
                "profileName": "Smith",
                "channelProfileId": "alice@example.com",
                "distributionChannel": "EMAIL",
                "transactionGroupType": "UDC",
                "customProperties": {
                    "_c_68529d06324a1b7ff2e6fc7f": [
                        "yes"
                    ]
                },
                "isArchived": false,
                "createdTime": 1756723410196
            },
            {
                "id": "68b578d2c5fba01bb3cfa291",
                "transactionGroupId": "6867b32dc8ff014fb8f12309",
                "profileName": "Johnson",
                "channelProfileId": "919876543210",
                "distributionChannel": "SMS",
                "transactionGroupType": "UDC",
                "customProperties": {},
                "isArchived": false,
                "createdTime": 1756723410196
            },
            {
                "id": "68b578d2c5fba01bb3cfa292",
                "transactionGroupId": "6867b32dc8ff014fb8f12309",
                "profileName": "Brown",
                "channelProfileId": "919876543211",
                "distributionChannel": "WHATSAPP_BUSINESS",
                "transactionGroupType": "UDC",
                "customProperties": {},
                "isArchived": false,
                "createdTime": 1756723410196
            }
        ],
        "cursor": "id=68b6cbe7dfc2985407917bfa"
    },
    "errors": []
}







**Dev Note: **For fetching the next set of results, you can input the "cursorId" received in the API response to [Search by Cursor](https://dev.sprinklr.com/search-by-cursor) API

[](https://dev.sprinklr.com/search-by-entity) 

 

 
[Back to top](https://dev.sprinklr.com/search-by-entity)
