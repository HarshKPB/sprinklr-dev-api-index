---
title: "Message Lookup"
slug: message-lookup
url: https://dev.sprinklr.com/message-lookup
---

# Message Lookup

#
Message Lookup

Using this API, you can search for a specific message using the unique message Id.



**Dev Notes: **The Community APIs are designed to support limited and specific use cases only. They are not intended for building or replicating a full-scale community platform. For more advanced or large-scale community features, please contact your Sprinklr representative to explore supported solutions.

## API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/lookup/community_message/{communityMessageId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {unauthenticated token} | The unauthenticated token for making API calls that returns publicly accessible data |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters




| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| communityMessageId | Required | Refers to the unique message Id you are fetching the details for | String |

## Example - Request




  Copy Code


curl -X GET \
 'https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/lookup/community_message/626ffa59cb111564f6fae9e0' \
  -H 'Accept: application/json' \
  -H 'X-Community-Authorization: Bearer {un-authenticated-token}' \
  -H 'Content-Type: application/json' \





### Example - Response

      

{
   "id": "626ffa59cb111564f6fae9e0",
   "projId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
   "topics": [
       "6192548a076c6a4d13203152"
   ],
   "snT": "COMMUNITY",
   "mTp": 230,
   "mSTp": 0,
   "m": "
https://prod-gitlab.sprinklr.com/sprinklr-qa/spr-automation/-/merge_requests/912https://prod-gitlab.sprinklr.com/sprinklr-qa/spr-automation/-/merge_requests/912
",
   "pL": "https://95da27b2-8e38-40ea-a2e1-4e0769cd7471.prod-tier2-care.sprinklr.com/conversations/topic/9c0ac3/626e8d2100de2474fe541c39?commentId=626ffa59cb111564f6fae9e0",
   "path": "topic/9c0ac3/626e8d2100de2474fe541c39?commentId=626ffa59cb111564f6fae9e0",
   "fU": "60fe8aeb7b2456681eb424c7",
   "fUInfo": {
       "communityUserId": "60fe8aeb7b2456681eb424c7",
       "fullName": "Navya1 Prod1",
       "profileImageUrl": "https://prod-content-care-community-cdn.sprinklr.com/95da27b2-8e38-40ea-a2e1-4e0769cd7471/Capture_421-74c84594-fac6-445f-b59f-09bc6381f677-420448523.PNG",
       "username": "Navyaprodtest",
       "color": "#25D54B"
   },
   "fromCommunityUser": {
       "id": "60fe8aeb7b2456681eb424c7",
       "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
       "experienceId": "cd6aaaad-7d02-4599-9c62-aee8068f78da",
       "experienceType": "COMMUNITY",
       "firstName": "Navya1",
       "lastName": "Prod1",
       "fullName": "Navya1 Prod1",
       "gamificationInfo": {
           "points": 0.0,
           "awardInfos": [
               {
                   "awardId": "60febfe759ba7a5bc460714b",
                   "awardType": "BADGE",
                   "earnedTime": 1627308595070
               },
               {
                   "awardId": "60feac3559ba7a5bc4606e0e",
                   "awardType": "BADGE",
                   "earnedTime": 1634282978863
               },
               {
                   "awardId": "60feac3d59ba7a5bc4606e0f",
                   "awardType": "BADGE",
                   "earnedTime": 1634282979041
               },
               {
                   "awardId": "61692e4b4af5626ba6b4b707",
                   "awardType": "BADGE",
                   "earnedTime": 1634283151758
               },
               {
                   "awardId": "616d36f04af5626ba6b4c5d8",
                   "awardType": "BADGE",
                   "earnedTime": 1634547486539
               },
               {
                   "awardId": "619254ce9bc0176d403afe45",
                   "awardType": "BADGE",
                   "earnedTime": 1636980180699
               },
               {
                   "awardId": "619398d49bc0176d403afe48",
                   "awardType": "BADGE",
                   "earnedTime": 1637065343742
               },
               {
                   "awardId": "61d6fb1c647f770539e1ee65",
                   "awardType": "BADGE",
                   "earnedTime": 1641479476272
               },
               {
                   "awardId": "621394a40e3b4804945c1e2c",
                   "awardType": "BADGE",
                   "earnedTime": 1645450571564
               },
               {
                   "awardId": "62139685a9496c44a95a1675",
                   "awardType": "BADGE",
                   "earnedTime": 1645450955264
               },
               {
                   "awardId": "621395a10e3b4804945c2242",
                   "awardType": "BADGE",
                   "earnedTime": 1645450955264
               },
               {
                   "awardId": "612336c9452a1c120caddc2e",
                   "awardType": "RANK",
                   "earnedTime": 1666797632183
               }
           ]
       },
       "additional": {},
       "partnerCustomFields": {},
       "profileImageUrl": "https://prod-content-care-community-cdn.sprinklr.com/95da27b2-8e38-40ea-a2e1-4e0769cd7471/Capture_421-74c84594-fac6-445f-b59f-09bc6381f677-420448523.PNG",
       "screenerFilled": false,
       "screenerCancelled": false,
       "lastLogin": 1663321934185,
       "deleted": false,
       "createdTime": "Jul 26, 2021 10:14:03 AM",
       "modifiedTime": "Oct 26, 2022 3:20:32 PM",
       "lastActivityAt": 1663321975876,
       "inactiveNotificationSentTime": 0,
       "status": "PENDING",
       "stats": {
           "numReads": 37.0,
           "numPosts": 46.0,
           "numTags": 13.0,
           "numFollowedPosts": 51.0,
           "numLikes": 17.0,
           "numLiked": 7.0,
           "numComments": 7.0,
           "numAcceptedSolutions": 0.0,
           "numReplies": 2.0,
           "numHelpful": 3.0,
           "numHelpfuled": 2.0,
           "followers": 1.0,
           "numFlags": 2.0,
           "numUnLikes": 3.0,
           "numImageUploads": 9.0,
           "numUnLiked": 2.0,
           "numFlagged": 2.0,
           "numUnFlagged": 1.0,
           "numVideoUploads": 4.0
       },
       "brandUser": false,
       "username": "Navyaprodtest",
       "lowerCaseUsername": "navyaprodtest",
       "userGroupIds": [],
       "sprUrl": "https://space-qa.sprinklr.com/new?qTyp=AUDIENCE_PROFILE&qId=COMMUNITY:60fe8aeb7b2456681eb424c7",
       "signature": "
Remember !
",
       "externalLogin": false,
       "accessibleSurveyIds": [],
       "roleSignatures": [],
       "lSSearchDetails": {},
       "grants": [],
       "optedOutOfChat": false,
       "chatPartnerUser": false,
       "chatTnCAccepted": false,
       "globalNotificationsCursor": 0,
       "participatedInChat": true,
       "registrationCompleted": false,
       "partnerDetails": {}
   },
   "tU": "60fe8aeb7b2456681eb424c7",
   "pMTp": 229,
   "pSnMId": "626e8d2100de2474fe541c39",
   "psnCTm": 1651412257428,
   "cId": "626e8d2100de2474fe541c39",
   "locale": "en_US",
   "cTm": 1651505753025,
   "mTm": 1666795427958,
   "lastActivityAt": 1666795427958,
   "indexDisabled": false,
   "iD": false,
   "hConv": false,
   "additional": {},
   "customFields": {},
   "brandPost": false,
   "privateMessage": false,
   "archived": false,
   "closed": false,
   "escalated": false,
   "merged": false,
   "spam": false,
   "mUIds": [],
   "accepted": false,
   "official": true,
   "pinned": false,
   "sprUrl": "https://space.sprinklr.com/new?qId=COMMUNITY-:-230-:-626ffa59cb111564f6fae9e0-:-ACCOUNT-:-822932&qTyp=UNIVERSAL",
   "hasAuthorMarkedSolution": false,
   "reminderSent": false,
   "hierarchyDetails": [
       {
           "id": "6192548a076c6a4d13203152",
           "name": "Topic",
           "slug": "topic-6192548a076c6a4d13203152",
           "path": "topic/6192548a076c6a4d13203152",
           "type": "TOPIC",
           "banner": {
               "type": "image"
           },
           "uniqueIdentifier": "topic",
           "lSContent": {}
       },
       {
           "id": "61925406076c6a4d132008e4",
           "name": "Category",
           "slug": "category-61925406076c6a4d132008e4",
           "path": "category/61925406076c6a4d132008e4",
           "type": "CATEGORY",
           "banner": {
               "type": "image"
           },
           "uniqueIdentifier": "category",
           "lSContent": {},
           "imageUrl": "https://sprcdn-assets.sprinklr.com/787/53d3ce5f-242d-4b1c-903d-275bb9689872-2042670142/Album.jpg"
       }
   ],
   "lSContent": {},
   "hasConditionalSection": false,
   "grants": [
       "post",
       "comment"
   ]
}





 [](https://dev.sprinklr.com/message-lookup)

[Back to top](https://dev.sprinklr.com/message-lookup)
