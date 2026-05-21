---
title: "Read Content by Content ID"
slug: read-content-by-content-id
url: https://dev.sprinklr.com/read-content-by-content-id
---

# Read Content by Content ID

#
  GET Read Content by Content ID

Using this API, you can fetch the knowledge base content along with details around content variable, content block, featured image, and content description

## API Endpoint


https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/{contentId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/ /api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| contentId | Required | Refers to the unique identifier for the content (article) | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/knowledgebase/64216a8b7ef3971d6d75782f' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": {
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
            "communityViewCount": 2,
            "livechatViewCount": 0,
            "helpfulCount": 30,
            "notHelpfulCount": 4,
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
    },
    "errors": []
}

## Response Schema





















| Field Name | Type | Description |
| --- | --- | --- |
| data | Object | Search response containing results and metadata. |
| errors | Array of Objects | List of errors encountered during the search operation. Empty if no errors occur. |

### data Object
















































































































































































| Field Name | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the content. |
| version | Integer | Version number of the content. |
| contributors | Array of Integers | List of user IDs who contributed to the content. May include system users. |
| tags | Array of Strings | Tags associated with the content. |
| content | Object | Core content details such as type, title, and body. |
| publicContent | Boolean | Indicates whether the content is publicly accessible. |
| hasConditionalSection | Boolean | Indicates whether the content includes conditional sections. |
| externalContent | Boolean | Indicates whether the content originates from an external source. |
| originType | String | Source of the content (for example, SPRINKLR). |
| favourite | Boolean | Indicates whether the content is marked as a favorite. |
| textModifiedTime | String | Timestamp of the last text modification. |
| lngVariants | Maps of Objects | Language-to-content-ID mapping for language variants. |
| inactiveLngVariants | Maps of Objects | Language variants that are currently inactive. |
| countryVariants | Map of Objects | Country-specific variants of the content. |
| publishedCountryVariants | Map of Objects | Published country-specific content variants. |
| stats | Object | Usage and feedback statistics for the content. |
| status | String | Current status of the content (for example, DRAFT). |
| saveInLngVariantEsEnabled | Boolean | Indicates whether saving in the ES language variant is enabled. |
| locale | String | Primary locale of the content (for example, en_US). |
| countryCodes | Array of Strings | List of country codes where the content applies. |
| countryBaseContent | Boolean | Indicates whether the content is country-base content. |
| linkedAssets | Array of Objects | Assets linked to the content. Empty if none exist. |
| translationProcess | Object | Metadata related to translation workflow. |
| languageSettingId | Array of Strings | Identifier for the Language Setting associated with the content. |
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
| markUpText | String | HTML-encoded rich text body of the content. |

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

### translationProcess Object














| Field Name | Type | Description |
| --- | --- | --- |
| updateTime | Integer (Epoch ms) | Timestamp of the last translation update. |
| newContentAvailableForTranslation | Boolean | Indicates whether new content is available for translation. |
| authorId | Integer | User ID of the author who triggered the translation update. |

### folderMetadata Object













| Field Name | Type | Description |
| --- | --- | --- |
| folderId | String | Identifier of the folder containing the content. |
| confidential | Boolean | Indicates whether the folder is confidential. |

[](https://dev.sprinklr.com/read-content-by-content-id) 

 

 
[Back to top](https://dev.sprinklr.com/read-content-by-content-id)
