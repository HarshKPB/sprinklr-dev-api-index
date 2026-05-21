---
title: "Find Linked Assets"
slug: find-linked-assets
url: https://dev.sprinklr.com/find-linked-assets
---

# Find Linked Assets

#
  POST - Find Linked Assets



Using this API, you can fetch **content variables** and **reusable content blocks** present in the knowledge base content

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/linked-assets

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












****

-
-

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| linkedAssetType | Required | Refers to the type of linked asset you want to fetch.Supported Values:spr-content-variable for Content Variablesspr-content-block for Reusable Content Blocks | String |


### Request Parameters













| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetIds | Required | List containing the unique identifiers for the linked assets.You can find linked assets using any content read/search API. | List [String] |


## Example - Request for Fetching Content Variables




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/linked-assets?linkedAssetType=spr-content-variable' \ ' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '[
      "63d8ff94b2ff6344b248a3bc",
     "63d8de3bb2ff6344b248600b"
]'
 

     
     
 

## Example - Response




 
{
    "data": {
        "63d8de3bb2ff6344b248600b": {
            "id": "63d8de3bb2ff6344b248600b",
            "name": "sadasd123",
            "description": "111asdsad",
            "countrySpecificDetails": {
                "GLOBAL": {
                    "defaultValue": "sasdsad",
                    "lngVsValue": {
                        "en_US": "ss",
                        "nl_NL": "as"
                    }
                }
            },
            "clientId": 2,
            "ownerUserId": 600000218,
            "createdTime": "Jan 31, 2023 9:26:34 AM",
            "modifiedTime": "Jan 31, 2023 9:26:34 AM",
            "lastModifiedUserId": 600000218,
            "deleted": false,
            "canEdit": false
        },
        "63d8ff94b2ff6344b248a3bc": {
            "id": "63d8ff94b2ff6344b248a3bc",
            "name": "Test new content variable",
            "description": "sadsad",
            "countrySpecificDetails": {
                "GLOBAL": {
                    "defaultValue": "test default value",
                    "lngVsValue": {
                        "en_US": "english default value",
                        "de_DE": "german default value"
                    }
                }
            },
            "clientId": 2,
            "ownerUserId": 600000218,
            "createdTime": "Jan 31, 2023 11:46:28 AM",
            "modifiedTime": "Jan 31, 2023 11:46:28 AM",
            "lastModifiedUserId": 600000218,
            "deleted": false,
            "canEdit": false
        }
    },
    "errors": []
}
 

     
     
   


## Example - Request for Fetching Reusable Content Blocks




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/linked-assets?linkedAssetType=spr-content-block' \ ' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '[
      "60eff2391f8dd110fe0dab23"
]'
 

     
     
 

## Example - Response




 
{
    "data": {
        "60eff2391f8dd110fe0dab23": {
            "id": "60eff2391f8dd110fe0dab23",
            "version": 7,
            "contributors": [
                600000001,
                600000218,
                600030478
            ],
            "tags": [
                "OS Independent"
            ],
            "content": {
                "contentType": "KNOWN_ISSUE",
                "contentSubType": "KB_ARTICLE",
                "title": "testing Notifications",
                "markUpText": "
testing Notifications

testing Notifications
"
            },
            "publicContent": true,
            "hasConditionalSection": false,
            "externalContent": false,
            "originType": "NOMINATED",
            "favourite": false,
            "communityPermalink": "https://edba44e5-64dc-4975-91eb-14abab0a512f.qa4-socialadvocacy.sprinklr.com/knowledge-base/articles/14th-july/testing-notifications/60eff24c5ce19a5e80bfd95d",
            "mappedProjectId": "edba44e5-64dc-4975-91eb-14abab0a512f",
            "mappedCommunityMessageId": "60eff24c5ce19a5e80bfd95d",
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
            "status": "APPROVED",
            "nominationInfo": {
                "status": "PUBLISHED",
                "nominatedByUserInfo": {
                    "communityUserId": "60e866ca8f007d2673ac6a2e",
                    "fullName": "Robert Zane",
                    "username": "Robert"
                },
                "nominatedPostId": "60eff2145ce19a5e80bfd95b"
            },
            "saveInLngVariantEsEnabled": false,
            "locale": "en_US",
            "grants": [
                "USER/600000218/OWNERSHIP",
                "CLIENT/2/OWNERSHIP"
            ],
            "clientId": 2,
            "ownerUserId": 600000218,
            "createdTime": "Jul 15, 2021 8:30:49 AM",
            "modifiedTime": "Dec 29, 2022 5:00:38 AM",
            "lastModifiedUserId": 600000218,
            "deleted": false,
            "folderMetadata": {
                "folderId": "60eec95c09ab1f31a3474f49",
                "confidential": false
            },
            "canEdit": false
        }
    },
    "errors": []
}
 

     
     
   

	 [](https://dev.sprinklr.com/find-linked-assets) 

 

 
[Back to top](https://dev.sprinklr.com/find-linked-assets)
