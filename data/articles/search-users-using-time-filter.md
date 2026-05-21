---
title: "Search Users Using Time Filter"
slug: search-users-using-time-filter
url: https://dev.sprinklr.com/search-users-using-time-filter
---

# Search Users Using Time Filter

#
Search Users Using Time Filter


Using this API, you can search the users in a specific time range.

### API Endpoint

https://care-api-`{env}`.sprinklr.com/care/community/rest/un-authenticated/user/search-users

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {unauthenticated token} | Unauthenticated token for making API calls that returns publicly accessible data |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

****

****

****

| Parameter | Sub-Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- | --- |
| timeFilter |  | Required if you need to search a user existing within a certain time range | Object defining the time range details for searching the user | Object |
|  | field | Required | The field on which the time filter needs be applied.Example: createdTime, modifiedTime | String |
|  | sinceTime | Optional | The start time for the search | Epoch |
|  | untilTime | Required | The ending time for the search | Epoch |
| page |  | OptionalNote: If pagination object is missing, you’ll be able to fetch 10 rows in the response by default | Object defining the pagination information | Object |
|  | page |  | Refers to the page you want to view in the responseDefault: 0 | Integer |
|  | size |  | Refers to the rows you want to fetch in a single response | Integer |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/user/search-users' \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
 "timeFilter":{
       "field":"createdTime",
       "sinceTime":0,
       "untilTime":1649083110265
   },
   "page":{
       "page":0,
       "size":10
   }
}'





## Example - Response

      

{
   "data": [
       {
           "communityUser": {
               "id": "614d982561ce8f5a6f1ab386",
               "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
               "experienceId": "cd6aaaad-7d02-4599-9c62-aee8068f78da",
               "experienceType": "COMMUNITY",
               "firstName": "Bharat",
               "lastName": "Gera",
               "fullName": "Bharat Gera",
               "gamificationInfo": {
                   "points": 0.0,
                   "awardInfos": []
               },
               "additional": {},
               "partnerCustomFields": {},
               "screenerFilled": false,
               "screenerCancelled": false,
               "lastLogin": 1632475173980,
               "deleted": false,
               "createdTime": "Sep 24, 2021 9:19:33 AM",
               "modifiedTime": "Sep 24, 2021 9:19:33 AM",
               "lastActivityAt": 1632475174157,
               "inactiveNotificationSentTime": 0,
               "status": "PENDING",
               "brandUser": false,
               "username": "gera3012",
               "lowerCaseUsername": "gera3012",
               "userGroupIds": [],
               "sprUrl": "https://space-qa.sprinklr.com/new?qTyp=AUDIENCE_PROFILE&qId=COMMUNITY:614d982561ce8f5a6f1ab386",
               "externalLogin": false,
               "accessibleSurveyIds": [],
               "roleSignatures": [],
               "lSSearchDetails": {},
               "grants": [],
               "optedOutOfChat": false,
               "chatPartnerUser": false,
               "chatTnCAccepted": true,
               "globalNotificationsCursor": 0,
               "participatedInChat": false,
               "registrationCompleted": false,
               "partnerDetails": {}
           },
           "communityUserProfiles": [
               {
                   "id": "614d9825f4872916b2983c5b",
                   "communityUserId": "614d982561ce8f5a6f1ab386",
                   "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
                   "snType": "COMMUNITY",
                   "snId": "614d982561ce8f5a6f1ab386",
                   "disconnected": false,
                   "inActive": false,
                   "modifiedTime": "Sep 24, 2021 9:19:33 AM"
               }
           ]
       },
       {
           "communityUser": {
               "id": "61d6f946f5b9527873e651a8",
               "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
               "experienceId": "cd6aaaad-7d02-4599-9c62-aee8068f78da",
               "experienceType": "COMMUNITY",
               "firstName": "hey_2",
               "lastName": "hey_2",
               "fullName": "hey_2 hey_2",
               "gamificationInfo": {
                   "points": 0.0,
                   "awardInfos": []
               },
               "additional": {},
               "partnerCustomFields": {},
               "screenerFilled": false,
               "screenerCancelled": false,
               "lastLogin": 1641478470236,
               "deleted": false,
               "createdTime": "Jan 6, 2022 2:14:30 PM",
               "modifiedTime": "Jan 6, 2022 2:14:49 PM",
               "lastActivityAt": 1641478489456,
               "inactiveNotificationSentTime": 0,
               "status": "PENDING",
               "brandUser": false,
               "username": "hey_2",
               "lowerCaseUsername": "hey_2",
               "userGroupIds": [],
               "sprUrl": "https://space.sprinklr.com/new?qTyp=AUDIENCE_PROFILE&qId=COMMUNITY:61d6f946f5b9527873e651a8",
               "externalLogin": false,
               "accessibleSurveyIds": [],
               "roleSignatures": [],
               "lSSearchDetails": {},
               "grants": [],
               "optedOutOfChat": false,
               "chatPartnerUser": false,
               "chatTnCAccepted": true,
               "globalNotificationsCursor": 0,
               "participatedInChat": false,
               "registrationCompleted": false,
               "partnerDetails": {}
           },
           "communityUserProfiles": [
               {
                   "id": "61d6f946f4872916b20b8d36",
                   "communityUserId": "61d6f946f5b9527873e651a8",
                   "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
                   "snType": "COMMUNITY",
                   "snId": "61d6f946f5b9527873e651a8",
                   "disconnected": false,
                   "inActive": false,
                   "modifiedTime": "Jan 6, 2022 2:14:30 PM"
               }
           ]
       }
   ],
   "totalHitCount": 47,
   "hasMore": true,
   "pageNumber": 0
}





	 [](https://dev.sprinklr.com/search-users-using-time-filter)

[Back to top](https://dev.sprinklr.com/search-users-using-time-filter)
