---
title: "GDPR - Fetch Profile Data"
slug: v1-gdpr-fetch-profile-data
url: https://dev.sprinklr.com/v1-gdpr-fetch-profile-data
---

# GDPR - Fetch Profile Data

#
  GET GDPR - Fetch Profile Data

Once you receive "SUCCESS" response in the [Fetch Request Status API](https://dev.sprinklr.com/v1-gdpr-fetch-request-status), you can call this API to fetch the profile data associated with user profile details passed in the Create View Request API.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/gdpr/view/{requestid}

### Headers

API headers include the mandatory information that you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











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













            [create GDPR request API](https://dev.sprinklr.com/v1-gdpr-create-view-request)



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| requestId | Required | Refers to the status Id received in the  response | String |


## Sample - Request














Copy Code




curl -X GET \
 ' https://api3.sprinklr.com/{env}/api/v1/gdpr/view/2cfc8e84db9d25b22b6e857' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \





## Sample - Response





{
   "profileActivities": [
       {
           "metaData": {
               "total": 2,
               "countByActivityType": {
                   "SOCIAL": 1,
                   "LISTENING": 1
               }
           },
           "profile": {
               "id": "62cdbf7ab8ef87db9870dcec",
               "contactInfo": {
                   "fullName": "Maria"
               },
               "socialProfiles": [
                   {
                       "name": "Maria",
                       "type": "FACEBOOK",
                       "snId": "4948814915245829",
                       "username": "Maria",
                       "following": 0,
                       "followers": 0,
                       "favCount": 0,
                       "reach": 0,
                       "statusCount": 0,
                       "snCreatedTime": 0,
                       "snModifiedTime": 1657651066075,
                       "unSubscribed": false,
                       "additional": {
                           "appId": [
                               "402131656569235"
                           ],
                           "isPsid": [
                               "true"
                           ]
                       },
                       "accountSpecificInfos": [
                           {
                               "accountId": 1000071183,
                               "additional": {
                                   "ePCT": "1657651066186",
                                   "iEEP": "false"
                               }
                           }
                       ],
                       "deleted": false
                   }
               ],
               "socialScoreCard": {
                   "participationIndex": 0.0,
                   "influencerIndex": 0.0,
                   "spamIndex": 0.0
               },
               "profileWorkflowProperties": {
                   "tags": [],
                   "comments": [],
                   "notifyUserIds": [],
                   "partnerProfileLists": [
                       48
                   ],
                   "clientProfileLists": [
                       2702,
                       8
                   ],
                   "partnerCustomProperties": {
                       "5efb406d06a9f468bb3184bd": [
                           "JB_True"
                       ],
                       "_c_61fe07bb089a63416fce3cb5": [
                           "Pro"
                       ]
                   },
                   "clientCustomProperties": {},
                   "spaceCustomProperties": {},
                   "userCustomProperties": {},
                   "clientTags": [
                       "new tag"
                   ]
               },
               "snCreatedTime": 0,
               "snModifiedTime": 1657651066075,
               "createdTime": 1657651066076,
               "modifiedTime": 1657651076067,
               "createdByUserId": 0,
               "accountsFollowedByUser": [],
               "accountsFollowingUser": [],
               "accountsUnFollowingUser": [],
               "accountsUnFollowedByUser": [],
               "accountsBlockingUser": [],
               "accountsSuspendingUser": [],
               "accountsDeactivatingUser": [],
               "engagedAccountIds": [
                   1000071183
               ],
               "additional": {},
               "exactMatch": true,
               "totalTicketCount": 0,
               "openTicketCount": 0,
               "lastContacted": 0
           },
           "activities": [
               {
                   "activityId": "2767651048000_0_SOCIAL",
                   "activityType": "SOCIAL",
                   "message": "awesome",
                   "messageType": "14",
                   "messageSubType": "257",
                   "snType": "FACEBOOK",
                   "snMsgId": "2533112974782829_1282640339178224",
                   "permalink": "https://www.facebook.com/257844304643041/posts/2533112974782829/?comment_id=1282640339178224",
                   "language": "en",
                   "associatedCases": "5164064",
                   "time": 2767651048000
               },
               {
                   "activityId": "2767651048000_0_LISTENING",
                   "activityType": "LISTENING",
                   "message": "awesome",
                   "messageType": "14",
                   "messageSubType": "257",
                   "snType": "FACEBOOK",
                   "snMsgId": "2533112974782829_1282640339178224",
                   "permalink": "https://www.facebook.com/257844304643041/posts/2533112974782829/?comment_id=1282640339178224",
                   "language": "en",
                   "associatedCases": "5164953",
                   "time": 1657651048000
               }
           ]
       }
   ]
}





**Dev Notes: **If there are more than 100 records for the associated profile, you will receive a cursor id in the response. To view the next set of data, you will have to make the GET request again by passing the cursor Id again in the path parameter. The endpoint in this case would be: `https://api3.sprinklr.com/{env}/api/v1/gdpr/view/{cursor id}`

[](https://dev.sprinklr.com/v1-gdpr-fetch-profile-data)




[Back to top](https://dev.sprinklr.com/v1-gdpr-fetch-profile-data)
