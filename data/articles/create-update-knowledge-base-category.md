---
title: "Create/Update Knowledge Base Category"
slug: create-update-knowledge-base-category
url: https://dev.sprinklr.com/create-update-knowledge-base-category
---

# Create/Update Knowledge Base Category

#
POST Create/Update Knowledge Base Category

Knowledge Base categories (folders) help you organize content into logical groups based on shared characteristics or properties. Using the Create/Update Knowledge Base Category API, you can programmatically create new categories or update existing ones to keep your Knowledge Base structured and up to date. This API enables seamless integration of category creation into your content workflows.

**Prerequisites**

- You must have the **View** and **Create Category** permissions under the Knowledge Base module. Refer to [this link](https://www.sprinklr.com/help/articles/introduction-to-sprinklr-knowledge-base/knowledge-base-permissions/68340aabc74d2f1a73c55bf3) for more details.

- The required Knowledge Base Category (folder) must be shared with you.

## API Endpoint


https://api3.sprinklr.com/`{env}`/api/v2/folder/save

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allow access to protected resources.











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

## Request Parameter













****``

























****````







****````

****````




























































| Field | Description | Type | Required / Optional |
| --- | --- | --- | --- |
| id | Specify the Knowledge Base category (folder) ID. Dev Note: When you provide this value, the system updates the Category. When you omit it, the system creates a new Category unless it finds a match using migrationDetails. | String | Optional |
| name | Name of the Category. | String | Required |
| description | Description of the Category. | String | Optional |
| parentId | ID of the parent Category. If not provided, the value defaults to the root. | String | Optional |
| moduleTypes | Module types associated with the Category, such as SAM.  Dev Note: At least one of moduleTypes or assetClasses must be non-empty. | Array of Strings | Optional |
| assetClasses | Asset classes associated with the Category, such as KNOWLEDGE_BASE_CONTENT.Dev Note: At least one of moduleTypes or assetClasses must be non-empty.       Dev Note: If moduleTypes is empty, assetClasses must contain only KNOWLEDGE_BASE_CONTENT. | Array of Strings | Optional |
| tags | Tags associated with the Category. | Array of Strings | Optional |
| thumbnail | Thumbnail URL for the Category. | String | Optional |
| confidential | Whether the folder is confidential. Defaults to FALSE. | Boolean | Optional |
| markPublic | Whether the Category is publicly accessible. | Boolean | Optional |
| locked | Whether the Category is locked. | Boolean | Optional |
| migrationDetails | Migration details for upsert based on external system IDs. See below. | Object | Optional |
| additional | Additional metadata as key-value pairs. | Array of Strings, String | Optional |
| assetMetadata | Asset metadata associated with the Category. | Array of Strings, String | Optional |
| priority | Priority of the folder. | Integer | Optional |

### `migrationDetails` Objects

Controls upsert behaviour when `id` is not provided. If `migratedId` and `migratedFrom` match an existing category, the system updates that category instead of creating a new one.




































| Field | Description | Type | Required / Optional |
| --- | --- | --- | --- |
| migratedId | The unique ID of the folder in the external or source system. | String | Required |
| migratedFrom | Identifier of the source system the folder was migrated from. | String | Required |
| migratedSlug | Slug of the folder in the source system. | String | Optional |
| migrationKey | Migration key for additional context. | String | Optional |

## Example - Request




 Copy Code



curl --location 'https://api3.sprinklr.com/{env}/api/v2/folder/save' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Access Token}' \
--header 'Key: {API Key}' \
--data '{
    "id": "69ca1b75063c432f16e271d2",
    "parentId": "6715fb6edd12033df96bffe3",
    "name": "RKP API Testing - 2",
    "description": "Postman Testing 23 April",
    "assetClasses": ["KNOWLEDGE_BASE_CONTENT"]
}'





## Example - Response



 
{
    "data": {
        "id": "69ca1b75063c432f16e271d2",
        "name": "RKP API Testing - 2",
        "description": "Postman Testing 23 April",
        "parentId": "6715fb6edd12033df96bffe3",
        "path": [
            "6715fb6edd12033df96bffe3",
            "69ca1b75063c432f16e271d2"
        ],
        "assetClasses": [
            "KNOWLEDGE_BASE_CONTENT"
        ],
        "tags": [
            "RKP_API_1",
            "RKP_API_2",
            "RKP_API_3"
        ],
        "confidential": false,
        "favourite": false,
        "assetMetadata": {},
        "markPublic": false,
        "userVisiblePath": [
            {
                "id": "6715fb6edd12033df96bffe3",
                "name": "TW Testing",
                "description": "Testing for technical writing team",
                "parentId": "",
                "path": [
                    "6715fb6edd12033df96bffe3"
                ],
                "assetClasses": [
                    "KNOWLEDGE_BASE_CONTENT"
                ],
                "tags": [],
                "confidential": false,
                "favourite": false,
                "additional": {
                    "mappedProjectName": "Encom Qa6"
                },
                "assetMetadata": {},
                "mappingDetails": [
                    {
                        "mappedProjectId": "8538f0a0-5bdb-4f1d-91a3-98f8f3d3aaee",
                        "mappedCategoryIds": [
                            "681c900df879d34473c8d943"
                        ],
                        "mappedTopicIds": []
                    },
                    {
                        "mappedProjectId": "1be6adab-c28d-4f32-ba15-acc738b08be4",
                        "mappedCategoryIds": [
                            "688b58ac14613202c9184aa0"
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
                    "CLIENT/66000002/OWNERSHIP",
                    "USER/66011271/OWNERSHIP"
                ],
                "clientId": 66000002,
                "ownerUserId": 66011271,
                "createdTime": "Oct 21, 2024, 06:57:50 AM",
                "modifiedTime": "Dec 11, 2025, 12:39:18 PM",
                "lastModifiedUserId": 66011271,
                "deleted": false,
                "canEdit": false
            },
            {
                "id": "69ca1b75063c432f16e271d2",
                "name": "RKP API Testing - 2",
                "description": "Postman Testing 23 April",
                "parentId": "6715fb6edd12033df96bffe3",
                "path": [
                    "6715fb6edd12033df96bffe3",
                    "69ca1b75063c432f16e271d2"
                ],
                "assetClasses": [
                    "KNOWLEDGE_BASE_CONTENT"
                ],
                "tags": [
                    "RKP_API_1",
                    "RKP_API_2",
                    "RKP_API_3"
                ],
                "confidential": false,
                "favourite": false,
                "assetMetadata": {},
                "markPublic": false,
                "disableChildSharing": false,
                "grants": [
                    "USER/66011271/OWNERSHIP",
                    "CLIENT/66001165/OWNERSHIP"
                ],
                "clientId": 66001165,
                "ownerUserId": 66011271,
                "createdTime": "Mar 30, 2026, 06:43:01 AM",
                "modifiedTime": "Apr 23, 2026, 09:56:40 AM",
                "lastModifiedUserId": 66011271,
                "deleted": false,
                "canEdit": false
            }
        ],
        "disableChildSharing": false,
        "grants": [
            "USER/66011271/OWNERSHIP",
            "CLIENT/66001165/OWNERSHIP"
        ],
        "clientId": 66001165,
        "ownerUserId": 66011271,
        "createdTime": "Mar 30, 2026, 06:43:01 AM",
        "modifiedTime": "Apr 23, 2026, 09:56:40 AM",
        "lastModifiedUserId": 66011271,
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





## Response Parameters







































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of the Knowledge Base category (folder). | String |
| name | Display name of the Knowledge Base category. | String |
| description | Description of the Knowledge Base category. | String |
| parentId | ID of the parent category. If not provided, the category is created at the root level. | String |
| path | Ordered list of category IDs representing the hierarchy from the root to this category. | Array of strings |
| assetClasses | List of asset classes supported by this category. | Array of strings |
| tags | User-defined tags associated with the category. | Array of strings |
| confidential | Indicates whether the category is marked as confidential. | Boolean |
| favourite | Indicates whether the category is marked as a favourite by the user. | Boolean |
| assetMetadata | Additional metadata associated with assets in the category. | Object |
| markPublic | Indicates whether the category is publicly visible. | Boolean |
| userVisiblePath | Provides details of each parent category in the hierarchy leading to the current category. | Array of strings |

[](https://dev.sprinklr.com/create-update-knowledge-base-category)

 

 
[Back to top](https://dev.sprinklr.com/create-update-knowledge-base-category)
