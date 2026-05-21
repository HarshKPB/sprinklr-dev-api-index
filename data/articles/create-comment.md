---
title: "Create Comment"
slug: create-comment
url: https://dev.sprinklr.com/create-comment
---

# Create Comment

#
Create Comment

Using this API, you can create a comment on an existing message on the community forum.

### API Endpoint

https://care-api-`{env}`.sprinklr.com/care/community/rest/authenticated/message/comment

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
| message | Required | Refers to the comment’s content | String |
| objectId | Required | Refers to the post Id to which the comment needs to be added | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-`{env}`.sprinklr.com/care/community/rest/authenticated/message/comment’ \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
   "objectId": "635a74bd7a4a1a660b1ee3c1",
   "message": "New Comment"
}'





## Example - Response

      

{
   "id": "635a7687766ae57355aeaa29",
   "projId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
   "topics": [
       "60ae342caff5d141f229a3d1"
   ],
   "snT": "COMMUNITY",
   "mTp": 230,
   "mSTp": 0,
   "m": "New Comment",
   "pL": "https://95da27b2-8e38-40ea-a2e1-4e0769cd7471.prod-tier2-care.sprinklr.com/conversations/t1/new-title/635a74bd7a4a1a660b1ee3c1?commentId=635a7687766ae57355aeaa29",
   "path": "t1/new-title/635a74bd7a4a1a660b1ee3c1?commentId=635a7687766ae57355aeaa29",
   "fU": "60ae445e4a5ae60c2e29aa03",
   "fUInfo": {
       "communityUserId": "60ae445e4a5ae60c2e29aa03",
       "fullName": "autouser1 autouser1",
       "profileImageUrl": "https://prod-content-care-community-cdn.sprinklr.com/95da27b2-8e38-40ea-a2e1-4e0769cd7471/ScreenShot20211013at6.41.27PM-a25e5ec0-ab2f-4965-8dbb-7dd5783ddce1-12686.png",
       "username": "autouser1",
       "color": "#25D54B"
   },
   "tU": "60ae445e4a5ae60c2e29aa03",
   "pMTp": 229,
   "pSnMId": "635a74bd7a4a1a660b1ee3c1",
   "psnCTm": 1666872509816,
   "cId": "635a74bd7a4a1a660b1ee3c1",
   "locale": "en_US",
   "cTm": 1666872967583,
   "mTm": 1666872967590,
   "lastActivityAt": 1666872967583,
   "indexDisabled": false,
   "iD": false,
   "hConv": false,
   "additional": {},
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
   "sprUrl": "https://space.sprinklr.com/new?qId=COMMUNITY-:-230-:-635a7687766ae57355aeaa29-:-ACCOUNT-:-822932&qTyp=UNIVERSAL",
   "hasAuthorMarkedSolution": false,
   "reminderSent": false,
   "lSContent": {},
   "hasConditionalSection": false,
   "grants": []
}





 [](https://dev.sprinklr.com/create-comment)

[Back to top](https://dev.sprinklr.com/create-comment)
