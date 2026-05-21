---
title: "Search Awards by Name"
slug: search-awards-by-name
url: https://dev.sprinklr.com/search-awards-by-name
---

# Search Awards by Name

#
Search Awards by Name


Using this API, you can search the award details using its name. This API also helps fetch badge Id and Rank Id, which can be used in Add Awards and Remove Awards APIs.

**Dev Notes: **

- To assign a rank, you’ll first need to use this API to remove the existing rank of the user
- To fetch badge Id, refer to Search Awards by Name API

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/gamification/awards/search

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Authenticated token for making API calls that require creating, updating, deleting tasks |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| keyword | Required | Refers to the awards’ name you want the details for | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-`{env}`.sprinklr.com/care/community/rest/authenticated/gamification/awards/search' \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
 "keyword" : "b 192"
}'





## Example - Response

      

{
   "data": [
       {
           "id": "60feac3559ba7a5bc4606e0e",
           "name": "b 192",
           "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
           "type": "BADGE",
           "description": "b1",
           "imageUrl": "https://sprcdn-assets.sprinklr.com/787/ef53a962-0cf0-4c7d-9684-cd2744f3f61b-424688391/https___prod-media-proxy.sprin_p.jpg",
           "multipleAwardsAllowed": false,
           "deleted": false,
           "createdTime": 1627302965564,
           "modifiedTime": 1658491780630,
           "ownerUserId": 256295,
           "lastModifiedUserId": 219689,
           "filter": {
               "details": {},
               "filters": [
                   {
                       "filterType": "GT",
                       "field": "TOTAL_POSTS",
                       "values": [
                           1
                       ],
                       "details": {}
                   }
               ]
           },
           "awardedCount": 1,
           "order": 192,
           "disabled": false,
           "lSContent": {}
       }
   ],
   "totalHitCount": 1,
   "hasMore": false
}





 [](https://dev.sprinklr.com/search-awards-by-name)




[Back to top](https://dev.sprinklr.com/search-awards-by-name)
