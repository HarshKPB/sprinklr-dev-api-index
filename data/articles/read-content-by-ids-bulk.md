---
title: "Read Content By Ids (Bulk)"
slug: read-content-by-ids-bulk
url: https://dev.sprinklr.com/read-content-by-ids-bulk
---

# Read Content By Ids (Bulk)

#
  POST Read Content By IDs (Bulk)


Using this API, you can fetch multiple knowledge base contents by passing the content Ids in the request payload. This API also provide the language variant details for the respective content.

**Dev Notes: **The API response will not include content variables' and content block details

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/contents

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













| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Ids | Required | Refers to the list of content Ids | List [String] |

## Example - Request















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/contents' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '[
     "64216a8b7ef3971d6d75782b",
     "647f0568d757383b0e8b9934"
]'
 

     
     
   

## Example - Response





{
    "data": [
        {
            "id": "683d73fcf8230370b3a105bc",
            "version": 17,
            "contributors": [
                1000385784,
                1000359404
            ],
            "tags": [],
            "content": {
                "contentType": "KNOWN_ISSUE",
                "contentSubType": "KB_ARTICLE",
                "title": "Sprinklr Service RN",
                "markUpText": "
Intro para for Service

# Inbound Voice

## Item Heading

Item description

## Enter Release Note Item Heading

Release Note Content

## Enter Release Note Item Heading

Release Note Content

# Module 2

# Module 3

​

| Item 3 | Item | Item | Item |
| --- | --- | --- | --- |
| Item | Item | Item | Item |
| Item 4 | Item | Item 4 | Item |
| Item 4 | Item | Item | Item |
| Item | Item | Item 4 | Item |
| Item | Item | Item 3 | Item |

| Item 2 | Item 2 | Item 3 | Item 4 |
| --- | --- | --- | --- |
| Item 2 | Item 2 | Item 2 | Item 2 |
| Item 4 | Item 4 | Item 4 | Item 2 |
| Item 2 | Item 2 | Item 2 | Item 2 |
| Item 2 | Item 2 | Item 2 | Item 2 |
| Item 2 | Item 2 | Item 3 | Text 2 Word |

​

| Item 4 | Item 4 | Item 4 |
| --- | --- | --- |
|  | Text 2 Word |  |
|  |  | Text 2 Word |

## Schedule Optimization

Optimizes Schedule Scenarios.

dd

# Heading 1

​

​
"
            },
            "publicContent": false,
            "hasConditionalSection": false,
            "externalContent": false,
            "originType": "SPRINKLR",
            "favourite": false,
            "textModifiedTime": "Mar 23, 2026, 08:28:02 AM",
            "lngVariants": {
                "nl": "683d73fcf8230370b3a105cb",
                "zh": "683d73fcf8230370b3a105ca"
            },
            "inactiveLngVariants": {},
            "countryVariants": {},
            "stats": {
                "recommendCount": 0,
                "usageCount": 0,
                "ratingCount": 0,
                "ratingAvg": 0.0,
                "agentViewCount": 0,
                "communityViewCount": 0,
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
            "status": "DRAFT",
            "saveInLngVariantEsEnabled": false,
            "locale": "hr_HR",
            "countryCodes": [
                "AL",
                "BT"
            ],
            "countryBaseContent": false,
            "linkedAssets": [],
            "translationProcess": {
                "updateTime": 1748857923698,
                "newContentAvailableForTranslation": true,
                "authorId": 1000385784
            },
            "languageSettingId": "68302bf74878553057327ad7",
            "grants": [
                "USER/1000385784/OWNERSHIP",
                "CLIENT/1000004509/OWNERSHIP"
            ],
            "clientId": 1000004509,
            "ownerUserId": 1000385784,
            "createdTime": "Jun 02, 2025, 09:50:52 AM",
            "modifiedTime": "Mar 23, 2026, 08:28:02 AM",
            "lastModifiedUserId": 1000359404,
            "deleted": false,
            "folderMetadata": {
                "folderId": "683d5891f8230370b39dbc7a",
                "confidential": false
            },
            "canEdit": false
        },
        {
            "id": "69bc0a51d3d3e04dfcfb4641",
            "version": 4,
            "contributors": [
                1000359404
            ],
            "tags": [],
            "content": {
                "contentType": "KNOWN_ISSUE",
                "contentSubType": "KB_ARTICLE",
                "title": "Editor Showcase (API Test)",
                "markUpText": "
An editor is a tool that helps you create and modify content. It allows you to write text, make changes, and organize information in a structured way. Editors are commonly used for documents, code, and online content, making them essential for both technical and non‑technical users.

A good editor improves productivity by offering features such as formatting options, search and replace, and version tracking. These features help you work more efficiently and reduce errors. Some editors also provide real‑time feedback, such as spelling or syntax checks, to improve the quality of your work.

Editors are designed to be flexible and easy to use. You can choose simple editors for basic tasks or advanced editors for complex projects. By selecting the right editor for your needs, you can create, review, and maintain content more effectively.

# More Information

An editor is a tool that helps you create and modify content. It allows you to write text, make changes, and organize information in a structured way. Editors are commonly used for documents, code, and online content, making them essential for both technical and non‑technical users.

A good editor improves productivity by offering features such as formatting options, search and replace, and version tracking. These features help you work more efficiently and reduce errors. Some editors also provide real‑time feedback, such as spelling or syntax checks, to improve the quality of your work.

Editors are designed to be flexible and easy to use. You can choose simple editors for basic tasks or advanced editors for complex projects. By selecting the right editor for your needs, you can create, review, and maintain content more effectively.
"
            },
            "publicContent": false,
            "hasConditionalSection": false,
            "externalContent": false,
            "originType": "SPRINKLR",
            "favourite": false,
            "textModifiedTime": "Mar 19, 2026, 02:38:16 PM",
            "lngVariants": {
                "ar": "69bc0c953c6d9104a678c5dd",
                "hi_IN": "69bc0c953c6d9104a678c5de"
            },
            "inactiveLngVariants": {},
            "countryVariants": {},
            "publishedCountryVariants": {},
            "stats": {
                "recommendCount": 0,
                "usageCount": 0,
                "ratingCount": 0,
                "ratingAvg": 0.0,
                "agentViewCount": 0,
                "communityViewCount": 0,
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
            "status": "DRAFT",
            "saveInLngVariantEsEnabled": false,
            "locale": "en",
            "countryCodes": [
                "global"
            ],
            "countryBaseContent": false,
            "linkedAssets": [],
            "translationProcess": {
                "updateTime": 1773931096916,
                "newContentAvailableForTranslation": true,
                "authorId": 1000359404
            },
            "languageSettingId": "68885d80f8bf2f3b8781886b",
            "grants": [
                "USER/1000359404/OWNERSHIP",
                "CLIENT/1000004509/OWNERSHIP"
            ],
            "clientId": 1000004509,
            "ownerUserId": 1000359404,
            "createdTime": "Mar 19, 2026, 02:38:09 PM",
            "modifiedTime": "Mar 19, 2026, 02:47:49 PM",
            "lastModifiedUserId": 1000359404,
            "deleted": false,
            "folderMetadata": {
                "folderId": "683d5891f8230370b39dbc7a",
                "confidential": false
            },
            "canEdit": false
        }
    ],
    "errors": []
}
 

     
     
   
 

## Response Schema

### Root Object





















| Field Name | Type | Description |
| --- | --- | --- |
| data | Array of Objects | List of content records returned for the requested IDs. |
| errors | Array of Objects | List of errors for content IDs that could not be retrieved. Empty if no errors occur. |

### Data Object







































| Field Name | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the content. |
| version | Integer | Version number of the content. |
| contributors | Array of Integers | List of user IDs who contributed to the content. May include system users (negative values). |
| tags | Array of Strings | Tags associated with the content. |
| content | Object | Core content details such as title and body. |
| publicContent | Boolean | Indicates whether the content is publicly accessible. |
| hasConditionalSection | Boolean | Indicates whether the content contains conditional sections. |
| externalContent | Boolean | Indicates whether the content originates from an external source. |
| originType | String | Source of the content (for example, SPRINKLR). |
| favourite | Boolean | Indicates whether the content is marked as a favorite. |
| lngVariants | Map of Objects | Language-to-content-ID mapping for language variants. |
| countryVariants | Map of Objects | Country-to-content-ID mapping for country variants. |
| stats | Object | Usage and feedback statistics for the content. |
| status | String | Current approval status of the content (for example, APPROVED). |
| mappingDetails | Array of Object | Mapping information to communities or projects. |
| saveInLngVariantEsEnabled | Boolean | Indicates whether saving in the ES language variant is enabled. |
| locale | String | Primary locale of the content (for example, en_US). |
| countryBaseContent | Boolean | Indicates whether the content is country-base content. |
| linkedAssets | Map of Object | Assets linked to the content. |
| grants | Array of Strings | Permissions granted on the content. |
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

### folderMetaData Object









| Field Name | Type | Description |
| --- | --- | --- |
| folderId | String | Identifier of the folder containing the content. |
| confidential | Boolean | Indicates whether the folder is confidential. |

### mappingDetails Object














| Field Name | Type | Description |
| --- | --- | --- |
| mappedProjectId | String | Project ID to which the content is mapped. |
| mappedCommunityMessageId | String | Community message ID associated with the content. |
| mappedCategoryIds | Array of Strings | Category IDs linked to the content. |
| mappedTopicIds | Array of Strings | Topic IDs linked to the content. |
| communityPermalink | String |  |
[](https://dev.sprinklr.com/read-content-by-ids-bulk)

[Back to top](https://dev.sprinklr.com/read-content-by-ids-bulk)
