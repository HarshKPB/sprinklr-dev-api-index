---
title: "Find Users Using Project Id"
slug: find-users-using-project-id
url: https://dev.sprinklr.com/find-users-using-project-id
---

# Find Users Using Project Id

#
  POST - Find Users Using Project Id

You can find advocacy community users with this API using the unique projectId.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/xb-community/find/users/{projectId}

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














[fetch project Id API](https://dev.sprinklr.com/fetch-project-id)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| projectId | Required | The unique project id for the advocacy community. You can get access to the project Id using  documentation | String |

### Request Parameters



















****

``````

****
****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| query | Optional | Refers to the search query (if any) | String |
| statuses | Optional | To search the users based on statusSupported Statuses:SCREENER_PENDING, PENDING, APPROVED | String |
| projectIds | Optional | Refers to the specific project Ids for which the search is being made | List[String] |
| start | Required | The start offset that specifies the starting point for fetching the data.Default: 0 | Integer |
| rows | Required | The number of rows (assets) to fetch from the start offset | Integer |
| sortDirection | Optional | Decides the order of results, i.e., whether it will be ascending or descendingASC: for ascendingDESC: for descending | String |
| communityUserSortKey | Optional | The sorting filter, i.e, on what basis you want to sort the search results | string |
| deleted | Optional | If true, the user you are searching for is a deleted one | Boolean |

### Example - Request














Copy Code




curl -X POST \
  ' https://api3.sprinklr.com/{env}/api/v2/find/users/04b70a51-ad01-4872-90fd-47449cfd3e16'  \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
"query":"",
"Statuses": ["APPROVED"],
"projectIds":["04b70a51-ad01-4872-90fd-47449cfd3e16"],
"start":0,
"rows":18,
"sortDirection":"DESC",
"communityUserSortKey":"CREATED_TIME",
"deleted":false
}'





### Example - Response





 {
   "data": {
       "entities": [
           {
               "communityUser": {
                   "id": "62cbd60df9f2ee6605b1b263", - community user id
                   "universalProfileId": "62cbd60d0b2ba24af998e092", - profile id
                   "projectId": "04b70a51-ad01-4872-90fd-47449cfd3e16",
                   "experienceId": "66e05de0-353d-4cea-8edb-1bec8273c667", - community id
                   "experienceType": "ADVOCACY",
                   "firstName": "Tom",
                   "lastName": "Cruise",
                   "fullName": "Tom Cruise",
                   "gender": "MALE",
                   "dob": {
                       "day": 11,
                       "month": 7,
                       "year": 2022
                   },
                   "email": "tomcruiseddt@gmail.com",
                   "gamificationInfo": { - points and awards info
                       "points": 1.0,
                       "typeVsAwardIds": {}, - award id
                       "eventsCompleted": [],
                       "awardInfos": []
                   },
                   "stats": {
                       "LOGIN_COUNT": 1.0
                   },
                   "additional": {
                       "STATUS_CHANGED_BY": "SPR_600039095" - admin user can change
                   },
                   "partnerCustomFields": {
                       "5d30640bc7a0e35fe9789cc5": [
                           "Japanese",
                           "Português (Brasil)",
                           "German"
                       ]
                   },
                   "profileImageUrl": "https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=121775460562853&height=50&width=50&ext=1660117771&hash=AeRjuDXb2HQ8Lh0LIBM",
                   "largeProfileImageUrl": "https://graph.facebook.com/121775460562853/picture?type=large",
                   "screenerFilled": true,
                   "screenerCancelled": false,
                   "admin": false,
                   "screenerResponse": {
                       "5dc10c68c7a0e37674b568f4": [
                           "5dc10c69c7a0e37674b568f6"
                       ],
                       "5f48c985ed87992571ff0c1d": [
                           "5f48c986ed87992571ff0c1f"
                       ]
                   },
                   "lastLogin": 1657525776347,
                   "status": "APPROVED",
                   "statusChangeTime": 1657778127858,
                   "allStatusValues": [
                       "SCREENER_PENDING",
                       "PENDING",
                       "APPROVED"
                   ],
                   "preferredLangCode": "en",
                   "customProperties": {
                   },
                   "brandUser": false,
                   "optedOutOfChat": false,
                   "chatPartnerUser": false,
                   "ownerUserId": 600001669, - who created the project
                   "createdTime": "Jul 11, 2022 7:49:33 AM",
                   "modifiedTime": "Jul 15, 2022 10:50:40 AM",
                   "lastModifiedUserId": -100, - when it is modified by a rule
                   "deleted": false,
                   "canEdit": false
               }
           }
       ],
       "hasMore": false,
       "count": 11
   },
   "errors": []
}





	 [](https://dev.sprinklr.com/find-users-using-project-id)




[Back to top](https://dev.sprinklr.com/find-users-using-project-id)
