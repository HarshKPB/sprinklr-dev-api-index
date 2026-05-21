---
title: "Create Post"
slug: create-post
url: https://dev.sprinklr.com/create-post
---

# Create Post

#
Create Post

Using this API, you can create a post on the community forum.

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/message/post

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.















``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Authenticated token for making API calls that require creating, updating, deleting tasks |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

****

********

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| topics | Optional | Refers to the list of topic Ids | String |
| title | Optional | Refers to the title of the post | String |
| message | Optional | Refers to the content of the post | String |
| communityPostType | Required | Refers to the post type.Supported post types:ARTICLE, IDEA, QUESTION, PROBLEM, PRAISE, ANNOUNCEMENT, DISCUSSION, UPDATE, ANSWER | String |
| customFields | Optional | Object containing key and value pair for custom field and its corresponding valueSyntax:"_c_60915cd9ea4e9c2a0aced328"  : [ "article1" ]where _c_60915cd9ea4e9c2a0aced32 refers to the custom field and Article1 refers to the custom field value | Object |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/message/post’ \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
 "topics": [
       "60ae342caff5d141f229a3d1"
   ],
   "title": "New Title",
   "message": "New Post",
   "communityPostType": "QUESTION",
   "customFields" : {
"_c_60915cd9ea4e9c2a0aced328"  : [ "article1" ],
"_c_60915d21011fb174c4c8b3a8" : ["articleTitle1"],
"_c_60915d4b011fb174c4c8c4c9" : ["article_url"]
}
}'





## Example - Response




{
   "id": "635a74bd7a4a1a660b1ee3c1",
   "projId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
   "topics": [
       "60ae342caff5d141f229a3d1"
   ],
   "snT": "COMMUNITY",
   "mTp": 229,
   "mSTp": 5,
   "t": "New Title",
   "m": "New Post",
   "pL": "https://95da27b2-8e38-40ea-a2e1-4e0769cd7471.prod-tier2-care.sprinklr.com/conversations/t1/new-title/635a74bd7a4a1a660b1ee3c1",
   "slug": "new-title-635a74bd7a4a1a660b1ee3c1",
   "path": "t1/new-title/635a74bd7a4a1a660b1ee3c1",
   "fU": "60ae445e4a5ae60c2e29aa03",
   "fUInfo": {
       "communityUserId": "60ae445e4a5ae60c2e29aa03",
       "fullName": "autouser1 autouser1",
       "profileImageUrl": "https://prod-content-care-community-cdn.sprinklr.com/95da27b2-8e38-40ea-a2e1-4e0769cd7471/ScreenShot20211013at6.41.27PM-a25e5ec0-ab2f-4965-8dbb-7dd5783ddce1-12686.png",
       "username": "autouser1",
       "color": "#25D54B"
   },
   "pMTp": 0,
   "psnCTm": 0,
   "cId": "635a74bd7a4a1a660b1ee3c1",
   "locale": "en_US",
   "cTm": 1666872509816,
   "mTm": 1666872509816,
   "lastActivityAt": 1666872509795,
   "indexDisabled": false,
   "iD": false,
   "hConv": false,
   "stats": {},
   "additional": {},
   "engagedUsers": [
       "60ae445e4a5ae60c2e29aa03"
   ],
   "customFields": {},
   "brandPost": true,
   "privateMessage": false,
   "archived": false,
   "closed": false,
   "escalated": false,
   "merged": false,
   "spam": false,
   "accepted": false,
   "official": false,
   "pinned": false,
   "sprUrl": "https://space.sprinklr.com/new?qId=COMMUNITY-:-229-:-635a74bd7a4a1a660b1ee3c1-:-ACCOUNT-:-822932&qTyp=UNIVERSAL",
   "hasAuthorMarkedSolution": false,
   "reminderSent": false,
   "hierarchyDetails": [
       {
           "id": "60ae342caff5d141f229a3d1",
           "name": "t1",
           "slug": "t1-60ae342caff5d141f229a3d1",
           "path": "t1/60ae342caff5d141f229a3d1",
           "type": "TOPIC",
           "banner": {
               "type": "image"
           },
           "uniqueIdentifier": "t1",
           "lSContent": {}
       },
       {
           "id": "60ae3424aff5d141f229a101",
           "name": "c1",
           "slug": "c1-60ae3424aff5d141f229a101",
           "path": "c1/60ae3424aff5d141f229a101",
           "type": "CATEGORY",
           "banner": {
               "type": "image"
           },
           "uniqueIdentifier": "c1",
           "lSContent": {},
           "imageUrl": "https://sprcdn-assets.sprinklr.com/787/bfbe9108-ca11-4f1d-9f86-55373d8ebba8-1443191582/a_pin_carousel_-_title.jpg"
       }
   ],
   "lSContent": {},
   "hasConditionalSection": false,
   "grants": [
       "post",
       "comment"
   ]
}





	 [](https://dev.sprinklr.com/create-post)

[Back to top](https://dev.sprinklr.com/create-post)
