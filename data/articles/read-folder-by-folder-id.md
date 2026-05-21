---
title: "Read Folder by Folder Id"
slug: read-folder-by-folder-id
url: https://dev.sprinklr.com/read-folder-by-folder-id
---

# Read Folder by Folder Id

#
  GET - Read Folder by Folder Id



Using this API, you can fetch the knowledge base folder (category) details for the given folder Id.

## API Endpoint


https://api3.sprinklr.com/`{env}`/api/v2/folder/{folderId}

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












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| folderId | Required | Refers to the unique identifier for the folder (category) | String |

## Example - Request




 Copy Code



curl -X GET 'https://api3.sprinklr.com/{env}/api/v2/folder/67f37bf8da1e7268d61d20d7' \
 -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example - Response



 
{
    "data": {
        "id": "67f37bf8da1e7268d61d20d7",
        "name": "Test Plot Comm Dim",
        "parentId": "",
        "path": [
            "67f37bf8da1e7268d61d20d7"
        ],
        "assetClasses": [
            "KNOWLEDGE_BASE_CONTENT"
        ],
        "tags": [],
        "confidential": false,
        "favourite": false,
        "assetMetadata": {},
        "mappingDetails": [
            {
                "mappedProjectId": "8538f0a0-5bdb-4f1d-91a3-98f8f3d3aaee",
                "mappedCategoryIds": [
                    "67f37c6eda1e7268d61d3164",
                    "67f37c81da1e7268d61d332b"
                ],
                "mappedTopicIds": []
            }
        ],
        "markPublic": false,
        "disableChildSharing": false,
        "shareConfigs": [
            {
                "shareLevel": "GLOBAL"
            }
        ],
        "grants": [
            "USER/66008139/OWNERSHIP",
            "CLIENT/66000002/OWNERSHIP"
        ],
        "clientId": 66000002,
        "ownerUserId": 66008139,
        "createdTime": "Apr 07, 2025, 07:17:12 AM",
        "modifiedTime": "Apr 07, 2025, 07:19:29 AM",
        "lastModifiedUserId": 66008139,
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/read-folder-by-folder-id) 

 

 
[Back to top](https://dev.sprinklr.com/read-folder-by-folder-id)
