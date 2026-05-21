---
title: "Search Folder (Category)"
slug: search-folder-category
url: https://dev.sprinklr.com/search-folder-category
---

# Search Folder (Category)

#
  POST - Search Folder (Category)


	 Using this API, you can search any folder existing within Sprinklr using filtering conditions.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/folder/search

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

****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetClasses | Optional | List of asset classes to which the folder is associated | List [String] |
| includeAssetCount | Optional | If true, the asset count is also provided in the API response | Boolean |
| query | Optional | Refers to the search query (if any) | String |
| scope | Optional | Refers to the scope of the searchSupported Values:ALL_FOLDERSONLY_TOP_LEVEL_FOLDERS | String |
| start | Optional | Refers to the pagination information, i.e., the page you want to search.Default: 0 | Integer |
| rows | Optional | Refers to the number of results you want to display in one page | Integer |

## Example - Request




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/folder/search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "assetClasses": [
        "KNOWLEDGE_BASE_CONTENT"
    ],
    "includeAssetCount": false,
    "scope": "ONLY_TOP_LEVEL_FOLDERS" ,
    "start" : 0 ,
    "rows" : 1
}'
 

     
     
 

**Dev Notes: **For fetching all the folders available within Sprinklr's instance, send empty curly brackets `{ }` in the API request.

## Example - Response




 
{
    "data": {
        "hasMore": true,
        "result": [
            {
                "id": "648d813a0ed83e533e7545f7",
                "name": "Star Wars",
                "description": "Star Wars Series",
                "parentId": "",
                "path": [
                    "648d813a0ed83e533e7545f7"
                ],
                "assetClasses": [
                    "KNOWLEDGE_BASE_CONTENT"
                ],
                "tags": [
                    "648d813a0ed83e533e7545f1",
                    "648d813a0ed83e533e7545f0",
                    "648d813a0ed83e533e7545ef"
                ],
                "confidential": false,
                "favourite": false,
                "additional": {
                    "MAPPED_PROJECT_ID": "f23c6b2d-bcfe-40ba-ad80-ae2bd60e756e"
                },
                "assetMetadata": {
                    "MAPPED_PROJECT_ID": [
                        "f23c6b2d-bcfe-40ba-ad80-ae2bd60e756e"
                    ]
                },
                "mappingDetails": [
                    {
                        "mappedProjectId": "f23c6b2d-bcfe-40ba-ad80-ae2bd60e756e",
                        "mappedCategoryIds": [
                            "648d87600ed83e533e759398"
                        ],
                        "mappedTopicIds": []
                    }
                ],
                "markPublic": false,
                "disableChildSharing": false,
                "shareConfigs": [
                    {
                        "shareLevel": "CLIENT",
                        "sharedWithIds": [
                            "2"
                        ]
                    },
                    {
                        "shareLevel": "CLIENT_GROUP",
                        "sharedWithIds": []
                    },
                    {
                        "shareLevel": "USER",
                        "sharedWithIds": []
                    },
                    {
                        "shareLevel": "USER_GROUP",
                        "sharedWithIds": []
                    }
                ],
                "grants": [
                    "USER/600000218/OWNERSHIP",
                    "CLIENT/2/OWNERSHIP"
                ],
                "clientId": 2,
                "ownerUserId": 600000218,
                "createdTime": "Jun 17, 2023, 9:47:38 AM",
                "modifiedTime": "Jun 17, 2023, 10:13:52 AM",
                "deleted": false,
                "canEdit": false
            }
        ],
        "totalHits": 482,
        "perfStats": {
            "getFolderSearchResponse.statTotalTime": 999,
            "adaptRequest": 0,
            "esSearch": 718,
            "BaseReportingEngine.queryAdaptTime": 1,
            "FOLDER_customDimensions": 0,
            "FOLDER_dynamicDimensions": 0,
            "FOLDER_customEntityDimensions": 0,
            "createFilter": 0,
            "createFiltersInternal": 0,
            "createQuery": 0,
            "BaseReportingEngine.searchTime": 717,
            "es_FOLDER_core2-es7_ESSearchRequestBuilder.executeActionGet": 545,
            "statTotalTime": 1,
            "pickupDelay": 0,
            "_taskTimeTaken": 1,
            "es.FOLDER.executeActionGet": 544,
            "collectAllAncestors": 96,
            "collectAllAncestors.connWaitTime": 0,
            "mongo.folder.find": 92,
            "filterVisibleFolders": 184,
            "assetGroupRedisCacheAccessor.getCrossClientGroupsFor": 1,
            "getCrossClientGroupsFor.getAssetGroupsByAssetId": 0,
            "redis.mGet": 0,
            "lc.kryo.deserialize": 0,
            "getCrossClientGroupsFor.getAssetGroupsByIds": 0,
            "assetCountEnrich": 0
        },
        "selectAllSupported": false
    },
    "errors": []
}
 

     
     
   

[](https://dev.sprinklr.com/search-folder-category) 

 

 
[Back to top](https://dev.sprinklr.com/search-folder-category)
