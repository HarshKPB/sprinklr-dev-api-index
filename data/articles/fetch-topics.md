---
title: "Fetch Topics"
slug: fetch-topics
url: https://dev.sprinklr.com/fetch-topics
---

# Fetch Topics

#
Fetch Topics


This API helps fetch the list of topics for the given topic Id/s.

**Dev Notes: **The Community APIs are designed to support limited and specific use cases only. They are not intended for building or replicating a full-scale community platform. For more advanced or large-scale community features, please contact your Sprinklr representative to explore supported solutions.

### API Endpoint

https://care-api-`{env}`.sprinklr.com/care/community/rest/un-authenticated/topic/fetch-topics

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {unauthenticated token} | Unauthenticated token for making API calls that returns publicly accessible data |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| topicId | Required | Unique identifier for the topic | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/topic/fetch-topics' \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '[
"60ae342caff5d141f229a3d1",
"6192548a076c6a4d13203152"
]'





## Example - Response

      

[
   {
       "id": "60ae342caff5d141f229a3d1",
       "parentId": "60ae3424aff5d141f229a101",
       "projectIds": [
           "95da27b2-8e38-40ea-a2e1-4e0769cd7471"
       ],
       "name": "t1",
       "medias": [],
       "createdTime": 1622029357260,
       "modifiedTime": 1658491780796,
       "stats": {
           "numPosts": 83.0
       },
       "deleted": false,
       "isPrivate": false,
       "shareConfigs": [],
       "slug": "t1-60ae342caff5d141f229a3d1",
       "path": "t1/60ae342caff5d141f229a3d1",
       "pinned": false,
       "banner": {
           "type": "image"
       },
       "order": 0,
       "uniqueIdentifier": "t1",
       "lSContent": {},
       "grants": [],
       "allowedPostTypes": []
   },
   {
       "id": "6192548a076c6a4d13203152",
       "parentId": "61925406076c6a4d132008e4",
       "projectIds": [
           "95da27b2-8e38-40ea-a2e1-4e0769cd7471"
       ],
       "name": "Topic",
       "medias": [],
       "createdTime": 1636979850381,
       "modifiedTime": 1658491781235,
       "stats": {
           "numPosts": 39.0,
           "followers": 0.0
       },
       "deleted": false,
       "shareConfigs": [],
       "slug": "topic-6192548a076c6a4d13203152",
       "path": "topic/6192548a076c6a4d13203152",
       "pinned": false,
       "banner": {
           "type": "image"
       },
       "order": 0,
       "uniqueIdentifier": "topic",
       "lSContent": {},
       "grants": [],
       "allowedPostTypes": []
   }
]





 [](https://dev.sprinklr.com/fetch-topics)




[Back to top](https://dev.sprinklr.com/fetch-topics)
