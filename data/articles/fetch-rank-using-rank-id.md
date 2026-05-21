---
title: "Fetch Rank Using Rank Id"
slug: fetch-rank-using-rank-id
url: https://dev.sprinklr.com/fetch-rank-using-rank-id
---

# Fetch Rank Using Rank Id

#
Fetch Rank Using Rank Id


Using this API, you can fetch the rank details for the given rank Id.

### API Endpoint

https://care-api-`{env}`.sprinklr.com/care/community/rest/un-authenticated/metadata/awards/fetch

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
| rankIds | Required | List of rank Ids for which you want to fetch the details | List [String] |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/metadata/awards/fetch' \
 -H 'X-Community-Authorization: Bearer {Unauthenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '[
"60feac3559ba7a5bc4606e0e"
]'





## Example - Response

      

[
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
]





 [](https://dev.sprinklr.com/fetch-rank-using-rank-id)




[Back to top](https://dev.sprinklr.com/fetch-rank-using-rank-id)
