---
title: "Fetch Categories Using Category Ids"
slug: fetch-categories-using-category-ids
url: https://dev.sprinklr.com/fetch-categories-using-category-ids
---

# Fetch Categories Using Category Ids

#
Fetch Categories Using Category Ids


Using this API, you can fetch categories using the respective category Ids.

**Dev Notes: **The Community APIs are designed to support limited and specific use cases only. They are not intended for building or replicating a full-scale community platform. For more advanced or large-scale community features, please contact your Sprinklr representative to explore supported solutions.

### API Endpoint

https://care-api-`{env}`.sprinklr.com/care/community/rest/un-authenticated/category/fetch-categories

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {unauthenticated token} | Unauthenticated token for making API calls that returns publicly accessible data |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| categoryIds | OptionalRequired when looking for specific categories | Refers to the category parent Id | String |
| page | Optional | Refers to the page number starting from which you want to fetch the categories.Default: 0 | Integer |
| size | Optional | Refers to the number of rows you want to fetch on every page | Integer |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/category/fetch-categories’ \
 -H 'X-Community-Authorization: Bearer {Unauthenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
   "categoryIds": ["6239d09c3a4b6b7634bc32cb" , "61925430076c6a4d132014ac" ] ,
   "size": 10,
   "page": 0
}





## Example - Response

      

{
    "data": [
        {
            "id": "61925430076c6a4d132014ac",
            "parentId": "-1",
            "name": "hdhdhh",
            "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
            "slug": "hdhdhh-61925430076c6a4d132014ac",
            "path": "hdhdhh/61925430076c6a4d132014ac",
            "order": 0,
            "createdTime": 1636987896177,
            "modifiedTime": 1658491780777,
            "deleted": false,
            "banner": {
                "type": "image"
            },
            "additional": {},
            "ownerUserId": 56842,
            "shareConfigs": [],
            "uniqueIdentifier": "hdhdhh",
            "grants": [],
            "lSContent": {},
            "allowedPostTypes": [],
            "categories": [],
            "communityTopics": []
        },
        {
            "id": "6239d09c3a4b6b7634bc32cb",
            "parentId": "60ae3424aff5d141f229a101",
            "name": "Category new",
            "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
            "slug": "category-new-6239d09c3a4b6b7634bc32cb",
            "path": "category-new/6239d09c3a4b6b7634bc32cb",
            "order": 0,
            "createdTime": 1647956334248,
            "modifiedTime": 1658491780791,
            "deleted": false,
            "banner": {
                "type": "image"
            },
            "additional": {},
            "ownerUserId": 219689,
            "isPrivate": false,
            "shareConfigs": [],
            "uniqueIdentifier": "category-new",
            "grants": [],
            "lSContent": {},
            "allowedPostTypes": [],
            "folderIds": [
                "6239cbfda751a462d21ccab5",
                "604f2a77e2e1d15191e969a9"
            ],
            "categories": [],
            "communityTopics": []
        }
    ],
    "totalHitCount": 2,
    "hasMore": false
}





**Dev Notes: **For every category returned in the response, the child topics and categories are appended up to one level

 [](https://dev.sprinklr.com/fetch-categories-using-category-ids)




[Back to top](https://dev.sprinklr.com/fetch-categories-using-category-ids)
