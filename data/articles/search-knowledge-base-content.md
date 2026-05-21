---
title: "Search Knowledge Base Content"
slug: search-knowledge-base-content
url: https://dev.sprinklr.com/search-knowledge-base-content
---

# Search Knowledge Base Content

#
  POST - Search Knowledge Base Content


Using this API, you can search the knowledge base content using filters. You can filter the following results:

- Article title and underlying content

- Search articles associated with a specific language

- Fetch all articles containing in the knowledgebase

- Fetch all articles associated with the given categories

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/search

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

### Request Parameters














****

-
-
-
-
-
-
-
-
-
-
-
-

****

-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| filters |  | Required | Array containing the content filtering details | Array |
|  | filterType | Optional | Refers to the type of filter that you want to apply.Supported Filter Types:ANDORNOTINGTGTELTLTENINEQUALSNOT_EQUALSCONTAINS | String |
|  | field | Optional | Refers to the field you want to apply the filter on.Supported Field Types:       KB_CONTRIBUTOR       KB_CONTENT_ID       KB_CONTENT_TYPE       KB_CONTENT_SUB_TYPE       KB_CONTENT_STATUS       KB_TAGS       PUBLIC_CONTENT       MAPPED_PROJECT_ID       KB_FAVOURITE       KB_CREATED_TIME       KB_MODIFIED_TIME       KB_ORIGIN_TYPE       KB_MIGRATED_ID       KB_MIGRATED_FROM       KB_EXPORT_IMPORT_ID       KB_BASE_LNG_CONTENT_ID       KB_BASE_COUNTRY_CONTENT_ID       KB_CONTENT_SCHEDULED_STATUS       KB_MAP_SCHEDULED_DATE       KB_UN_MAP_SCHEDULED_DATE       KB_LINKED_ASSET_ID       KB_TITLE       KB_MARK_UP_TEXT       KB_LOCALE | String |
|  | values | Optional | Refers to the value corresponding to the field provided | List [String/Integer] |

## Example - Request















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "filters": [
        {
            "filterType": "IN",
            "field": "KNOWLEDGE_BASE_CONTENT_CUSTOM_PROPERTY",
            "values": [
                "3"
            ],
            "details": {
                "srcType": "CUSTOM",
                "fieldName": "_c_62a1b36c0b1a504e6e0a035c",
                "type": "DIMENSION",
                "ASSET_CLASS": "KNOWLEDGE_BASE_CONTENT"
            }
        }
    ],
    "page": {
        "page": 0,
        "size": 2
    }
}'
 

     
     
   

**Dev Notes: **For fetching all the content available within Sprinklr's instance, send empty curly brackets `{ }` in the API request.

## Example - Response





{
    "data": {
        "searchResults": [
            {
                "id": "634979a2c037584e15546b52",
                "version": 65,
                "contributors": [
                    600040449,
                    -100,
                    600038885,
                    600041290,
                    600000218
                ],
                "tags": [
                    "63f1951095cf18948f84a54a",
                    "63f1951095cf18948f84a8b4"
                ],
                "content": {
                    "contentType": "KNOWN_ISSUE",
                    "contentSubType": "KB_ARTICLE",
                    "title": "kashish test article",
                    "markUpText": ""
                },
                "publicContent": false,
                "hasConditionalSection": false,
                "externalContent": false,
                "originType": "SPRINKLR",
                "favourite": false,
                "lngVariants": {},
                "stats": {
                    "recommendCount": 0,
                    "usageCount": 0,
                    "ratingCount": 0,
                    "ratingAvg": 0.0,
                    "agentViewCount": 0,
                    "communityViewCount": 1,
                    "livechatViewCount": 0,
                    "helpfulCount": 0,
                    "notHelpfulCount": 0,
                    "communityHelpfulCount": 0,
                    "communityNotHelpfulCount": 0,
                    "livechatHelpfulCount": 0,
                    "livechatNotHelpfulCount": 0,
                    "externalViewCount": 0,
                    "externalHelpfulCount": 0,
                    "externalNotHelpfulCount": 0
                },
                "partnerCustomProperties": {
                    "_c_62a1cf903df8d74b0e283e57": [
                        "213"
                    ],
                    "_c_62a1b36c0b1a504e6e0a035c": [
                        "3"
                    ]
                },
                "customProperties": {
                    "flatCustomProperties": [
                        "ALLµ_c_62a1cf903df8d74b0e283e57",
                        "ALL",
                        "ALLµ_c_62a1b36c0b1a504e6e0a035cµ3",
                        "ALLµ_c_62a1cf903df8d74b0e283e57µ213",
                        "ALLµ_c_62a1b36c0b1a504e6e0a035c"
                    ],
                    "customPropertyNames": [
                        "_c_62a1cf903df8d74b0e283e57",
                        "_c_62a1b36c0b1a504e6e0a035c"
                    ],
                    "mappedCustomProperties": {
                        "_c_62a1cf903df8d74b0e283e57": [
                            "213"
                        ],
                        "_c_62a1b36c0b1a504e6e0a035c": [
                            "3"
                        ]
                    },
                    "mappedControllingCustomPropertyList": [],
                    "customProperties": [
                        {
                            "key": "_c_62a1cf903df8d74b0e283e57",
                            "values": [
                                "213"
                            ]
                        },
                        {
                            "key": "_c_62a1b36c0b1a504e6e0a035c",
                            "values": [
                                "3"
                            ]
                        }
                    ]
                },
                "status": "DRAFT",
                "saveInLngVariantEsEnabled": false,
                "locale": "en_US",
                "countryBaseContent": false,
                "approvalDetails": {
                    "currentTaskId": 29197,
                    "currentTaskStatus": "CANCELLED",
                    "currentTaskOwnerId": 600041290,
                    "currentTaskAssigneeType": "USER",
                    "currentTaskAssigneeId": 600000218,
                    "approvalPathId": "6363f07c4683043227287895"
                },
                "grants": [
                    "USER/600041290/OWNERSHIP",
                    "CLIENT/2/OWNERSHIP"
                ],
                "clientId": 2,
                "ownerUserId": 600041290,
                "createdTime": "Oct 14, 2022, 3:00:50 PM",
                "modifiedTime": "Mar 9, 2023, 11:56:59 AM",
                "lastModifiedUserId": 600000218,
                "deleted": false,
                "folderMetadata": {
                    "folderId": "63611b24a7e8762e68bed5ad",
                    "confidential": false
                },
                "canEdit": false
            }
        ],
        "hasMore": false,
        "totalHits": 1
    },
    "errors": []
}
 

     
     
 


## Response Schema





















| Field Name | Type | Description |
| --- | --- | --- |
| data | Object | Search response containing results and metadata. |
| errors | Array<ErrorObject> | List of errors encountered during the search operation. Empty if no errors occur. |

### data Object


























| Field Name | Type | Description |
| --- | --- | --- |
| searchResults | Array of Objects | List of knowledge base content items that match the search criteria. |
| hasMore | Boolean | Indicates whether more results are available for pagination. |
| totalHits | Integer | Total number of matching results for the search query. |

### searchResults Object







































| Field Name | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the content. |
| version | Integer | Version number of the content. |
| contributors | Integer[] | List of user IDs who contributed to the content. May include system users. |
| tags | String[] | Tags associated with the content. |
| content | Object | Core content details such as type, title, and body. |
| publicContent | Boolean | Indicates whether the content is publicly accessible. |
| hasConditionalSection | Boolean | Indicates whether the content includes conditional sections. |
| externalContent | Boolean | Indicates whether the content originates from an external source. |
| originType | String | Source of the content (for example, SPRINKLR). |
| favourite | Boolean | Indicates whether the content is marked as a favorite. |
| lngVariants | Object (Map) | Language-to-content-ID mapping for language variants. |
| stats | Object | Usage and feedback statistics for the content. |
| partnerCustomProperties | Object (Map) | Partner-specific custom properties mapped to the content. |
| customProperties | Object | Custom property metadata associated with the content. |
| status | String | Current workflow status of the content (for example, DRAFT). |
| saveInLngVariantEsEnabled | Boolean | Indicates whether saving in the ES language variant is enabled. |
| locale | String | Primary locale of the content (for example, en_US). |
| countryBaseContent | Boolean | Indicates whether the content is country-base content. |
| approvalDetails | Object | Approval workflow details for the content. |
| grants | String[] | Permissions granted on the content. |
| clientId | Integer | Client identifier. |
| ownerUserId | Integer | User ID of the content owner. |
| createdTime | String | Content creation timestamp. |
| modifiedTime | String | Last modification timestamp. |
| lastModifiedUserId | Integer | User ID of the last editor. |
| deleted | Boolean | Indicates whether the content is deleted. |
| folderMetadata | Object | Folder and confidentiality details. |
| canEdit | Boolean | Indicates whether the current user can edit the content. |

### content Object















| Field Name | Type | Description |
| --- | --- | --- |
| contentType | String | High-level content type (for example, KNOWN_ISSUE). |
| contentSubType | String | Content subtype (for example, KB_ARTICLE). |
| title | String | Title of the content. |
| markUpText | String | Escaped HTML markup representing the content body. |

### stats Object



























| Field Name | Type | Description |
| --- | --- | --- |
| recommendCount | Integer | Number of recommendations. |
| usageCount | Integer | Number of times the content was used. |
| ratingCount | Integer | Total number of ratings received. |
| ratingAvg | Number | Average rating value. |
| agentViewCount | Integer | Number of agent views. |
| communityViewCount | Integer | Number of community views. |
| livechatViewCount | Integer | Number of live chat views. |
| helpfulCount | Integer | Number of helpful votes. |
| notHelpfulCount | Integer | Number of not helpful votes. |
| communityHelpfulCount | Integer | Helpful votes from the community. |
| communityNotHelpfulCount | Integer | Not helpful votes from the community. |
| livechatHelpfulCount | Integer | Helpful votes from live chat. |
| livechatNotHelpfulCount | Integer | Not helpful votes from live chat. |
| externalViewCount | Integer | Number of external views. |
| externalHelpfulCount | Integer | Helpful votes from external users. |
| externalNotHelpfulCount | Integer | Not helpful votes from external users. |

### approvalDetails Object

















| Field Name | Type | Description |
| --- | --- | --- |
| currentTaskId | Integer | Identifier of the current approval task. |
| currentTaskStatus | String | Status of the current approval task. |
| currentTaskOwnerId | Integer | User ID of the task owner. |
| currentTaskAssigneeType | String | Type of the assignee (for example, USER). |
| currentTaskAssigneeId | Integer | User ID of the task assignee. |
| approvalPathId | String | Approval workflow path identifier. |

### folderMetadata Object













| Field Name | Type | Description |
| --- | --- | --- |
| folderId | String | Identifier of the folder containing the content. |
| confidential | Boolean | Indicates whether the folder is confidential. |

[](https://dev.sprinklr.com/search-knowledge-base-content) 

 

 
[Back to top](https://dev.sprinklr.com/search-knowledge-base-content)
