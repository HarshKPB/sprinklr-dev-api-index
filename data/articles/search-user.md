---
title: "Search User"
slug: search-user
url: https://dev.sprinklr.com/search-user
---

# Search User

#
Search User

This API helps in searching community users using their respective usernames.

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

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| filters |  | Optional | Array defining the filters you want to apply on users | Array |
|  | field |  | Field name you want to search forRefer to the table below to see the supported field names | String |
|  | filterType |  | Refers to the applied filter type.Supported filter types:GT - greater thanGTE - greater than equal toLT - less thanLTE - less than  equal toIN- should contain at least one of the values mentioned along the IN filterNIN - opposite to IN | String |
|  | values |  | Values corresponding to the given filter type | List [String, Integer] |
| queries |  | Optional | Array defining the details of the query | Array |
|  | queryType |  | Refers to the type of query madeSupported queryType values:SEARCH - searches for the given value anywhere in the fieldAND - similar to boolean AND. For combining multiple filters/queriesOR - similar to boolean OR. For combining multiple filters/queries | String |
|  | field |  | The field name on which you want to run the query | String |
|  | values |  | List of values corresponding to the given filed name | List [String, Integer] |
| sorts |  | Optional | Array specifying the sorting information | Array |
|  | key |  | Refers to the field name based on which you want to sort results | String |
|  | order |  | Specifies whether you want the results in ascending or descending orderDESC - for descendingASC - for ascending | String |
| page |  | Optional | Object defining the pagination information | Object |
|  | page |  | The page number you want the response from.Default: 0 | Integer |
|  | size |  | Refers to the number of results that will be shown on a single page | Integer |

### Supported Field Names

****

****

****

****

| Field Name | Description |
| --- | --- |
| firstName | first name of the user |
| lastName | last name of the user |
| middleName | middle name of the user |
| email | email id of the user |
| gamificationInfo.awardInfos.awardId | Id of the badge/rank |
| profileImageUrl | Image url of profile pic |
| lastLogin | Last login time in epoch |
| createdTime | time when profile was created in epoch |
| modifiedTime | time when profile was last edited in epoch |
| lastActivityAt | last activity done by profile in epoch |
| status | Supported Values: PENDING / BLOCKED / HALF_BAKEDBLOCKED - Users that are blockedHALF_BAKED - Users from before migration who have not logged inPENDING - All other normal users |
| bio | Bio filled by the user |
| username | The unique username |
| brandUser | Boolean - if user is a brand user or not |
| lowerCaseUsername | user name in lower case |
| organizationDetails.employeeId | employeeid |
| stats.followers | Number of followers of the profile |
| stats.numPosts | Number of posts made by user |
| stats.numComments | Number of comments made by user |
| stats.numReplies | Number of replies made by user |
| stats.numLikes | Received likes on posts/comments/replies |
| stats.numLiked | Number of likes given on posts/comments/replies |
| stats.numAcceptedSolutions | Number of solutions of user which got accepted as solution |
| stats.numAcceptedSolutionsd | Number of solutions the user has marked as accepted solution |

## Example - Request for searching all users where employee id exists




  Copy Code



curl -X POST \
  'https://care-api-`{env}`.sprinklr.com/care/community/rest/un-authenticated/user/search-users' \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
   "filters": [
       {
           "filterType": "EXISTS",
           "field": "organizationDetails.employeeId",
           "values": [
               true
           ]
       }
   ],
   "page": {
       "page": 0,
       "size": 10
   }
}'





## Example - Response

      

{
    "data": [
        {
            "communityUser": {
                "id": "611fc6d41da62f70570ca100",
                "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
                "experienceId": "cd6aaaad-7d02-4599-9c62-aee8068f78da",
                "experienceType": "COMMUNITY",
                "firstName": "Navya",
                "lastName": "A",
                "fullName": "Navya A",
                "gamificationInfo": {
                    "points": 0.0,
                    "awardInfos": [
                        {
                            "awardId": "61d6fb1c647f770539e1ee65",
                            "awardType": "BADGE",
                            "earnedTime": 1641479639025
                        },
                        {
                            "awardId": "60feac3d59ba7a5bc4606e0f",
                            "awardType": "BADGE",
                            "earnedTime": 1641479646540
                        },
                        {
                            "awardId": "619398d49bc0176d403afe48",
                            "awardType": "BADGE",
                            "earnedTime": 1641479684599
                        },
                        {
                            "awardId": "60febfe759ba7a5bc460714b",
                            "awardType": "BADGE",
                            "earnedTime": 1641479684599
                        },
                        {
                            "awardId": "616d36f04af5626ba6b4c5d8",
                            "awardType": "BADGE",
                            "earnedTime": 1641479684599
                        },
                        {
                            "awardId": "619254ce9bc0176d403afe45",
                            "awardType": "BADGE",
                            "earnedTime": 1641479684599
                        },
                        {
                            "awardId": "61692e4b4af5626ba6b4b707",
                            "awardType": "BADGE",
                            "earnedTime": 1641479684599
                        },
                        {
                            "awardId": "62139685a9496c44a95a1675",
                            "awardType": "BADGE",
                            "earnedTime": 1645451069094
                        },
                        {
                            "awardId": "621395a10e3b4804945c2242",
                            "awardType": "BADGE",
                            "earnedTime": 1649080220173
                        },
                        {
                            "awardId": "621394a40e3b4804945c1e2c",
                            "awardType": "BADGE",
                            "earnedTime": 1649080220173
                        },
                        {
                            "awardId": "612336c9452a1c120caddc2e",
                            "awardType": "RANK",
                            "earnedTime": 1666791535831
                        }
                    ]
                },
                "additional": {
                    "isP2PAudioNotifEnabled": false,
                    "IMPORTED": [
                        "true"
                    ]
                },
                "partnerCustomFields": {},
                "profileImageUrl": "https://prod-content-care-community-cdn.sprinklr.com/95da27b2-8e38-40ea-a2e1-4e0769cd7471/CuteCartoonBoyWallpaper1-8acf0db9-a28adf54210861cb-1610665123.jpg",
                "screenerFilled": false,
                "screenerCancelled": false,
                "lastLogin": 1663321896071,
                "deleted": false,
                "createdTime": "Aug 20, 2021 3:14:28 PM",
                "modifiedTime": "Oct 27, 2022 1:07:40 PM",
                "lastActivityAt": 1663322254545,
                "inactiveNotificationSentTime": 0,
                "status": "APPROVED",
                "stats": {
                    "numReads": 18.0,
                    "numPosts": 12.0,
                    "numTags": 6.0,
                    "numFollowedPosts": 17.0,
                    "numLikes": 4.0,
                    "numUnLikes": 2.0,
                    "numHelpful": 1.0,
                    "numHelpfuled": 1.0,
                    "numLiked": 2.0,
                    "numComments": 7.0,
                    "numFollowedUsers": 1.0,
                    "numUnLiked": 1.0,
                    "numReplies": 2.0,
                    "numImageUploads": 1.0
                },
                "brandUser": true,
                "username": "navya1198",
                "lowerCaseUsername": "navya1198",
                "userGroupIds": [],
                "sprUrl": "https://space-qa.sprinklr.com/new?qTyp=AUDIENCE_PROFILE&qId=COMMUNITY:611fc6d41da62f70570ca100",
                "externalLogin": false,
                "accessibleSurveyIds": [],
                "roleSignatures": [],
                "lSSearchDetails": {},
                "grants": [],
                "optedOutOfChat": false,
                "chatPartnerUser": false,
                "chatTnCAccepted": true,
                "globalNotificationsCursor": 0,
                "participatedInChat": true,
                "registrationCompleted": false,
                "partnerDetails": {}
            },
            "communityUserProfiles": [
                {
                    "id": "611fc6d4f4872916b247a2cb",
                    "communityUserId": "611fc6d41da62f70570ca100",
                    "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
                    "snType": "COMMUNITY",
                    "snId": "611fc6d41da62f70570ca100",
                    "disconnected": false,
                    "username": "navya1198",
                    "inActive": false,
                    "modifiedTime": "Sep 16, 2022 9:51:36 AM"
                }
            ]
        },
        {
            "communityUser": {
                "id": "61d6fb770c79de5b6578bd58",
                "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
                "experienceId": "cd6aaaad-7d02-4599-9c62-aee8068f78da",
                "experienceType": "COMMUNITY",
                "firstName": "hey_31",
                "lastName": "hey_31",
                "fullName": "hey_31 hey_31",
                "gamificationInfo": {
                    "points": 0.0,
                    "awardInfos": [
                        {
                            "awardId": "61d6faee647f770539e1ee63",
                            "awardType": "BADGE",
                            "earnedTime": 1641479032080
                        },
                        {
                            "awardId": "61d6fb1c647f770539e1ee65",
                            "awardType": "BADGE",
                            "earnedTime": 1641479185947
                        },
                        {
                            "awardId": "60feac3d59ba7a5bc4606e0f",
                            "awardType": "BADGE",
                            "earnedTime": 1641479186201
                        },
                        {
                            "awardId": "619398d49bc0176d403afe48",
                            "awardType": "BADGE",
                            "earnedTime": 1641479238834
                        },
                        {
                            "awardId": "60feac3559ba7a5bc4606e0e",
                            "awardType": "BADGE",
                            "earnedTime": 1641479391824
                        },
                        {
                            "awardId": "612336c9452a1c120caddc2e",
                            "awardType": "RANK",
                            "earnedTime": 1641484154265
                        }
                    ]
                },
                "additional": {},
                "partnerCustomFields": {
                    "ban_reason": [
                        ""
                    ]
                },
                "screenerFilled": false,
                "screenerCancelled": false,
                "lastLogin": 1641481739698,
                "deleted": false,
                "createdTime": "Jan 6, 2022 2:23:51 PM",
                "modifiedTime": "Jan 6, 2022 3:49:14 PM",
                "lastActivityAt": 1641484154068,
                "inactiveNotificationSentTime": 0,
                "status": "APPROVED",
                "bio": "numDownVotednumDownVotednumDownVotednumDownVoted",
                "stats": {
                    "numPosts": 2.0,
                    "numFollowedPosts": 3.0,
                    "numReads": 6.0,
                    "numTags": 1.0,
                    "numComments": 1.0,
                    "numLiked": 2.0,
                    "numReplies": 1.0,
                    "numFlags": 1.0,
                    "numUnFlags": 1.0,
                    "numFollowedTopics": 0.0,
                    "numHelpfuled": 1.0,
                    "numNotHelpfuled": 1.0
                },
                "brandUser": false,
                "username": "hey_3",
                "lowerCaseUsername": "hey_3",
                "userGroupIds": [],
                "sprUrl": "https://space.sprinklr.com/new?qTyp=AUDIENCE_PROFILE&qId=COMMUNITY:61d6fb770c79de5b6578bd58",
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
                    "id": "61d6fb77f4872916b2258e79",
                    "communityUserId": "61d6fb770c79de5b6578bd58",
                    "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
                    "snType": "COMMUNITY",
                    "snId": "61d6fb770c79de5b6578bd58",
                    "disconnected": false,
                    "inActive": false,
                    "modifiedTime": "Jan 6, 2022 3:08:59 PM"
                }
            ]
        }
    ],
    "totalHitCount": 2,
    "hasMore": false,
    "pageNumber": 0
}





	 [](https://dev.sprinklr.com/search-user)

[Back to top](https://dev.sprinklr.com/search-user)
