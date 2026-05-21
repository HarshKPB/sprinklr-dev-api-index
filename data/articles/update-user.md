---
title: "Update User"
slug: update-user
url: https://dev.sprinklr.com/update-user
---

# Update User

#
Update User

This API helps in updating the details of the community user.

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/update-user

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Authenticated token for making API calls that require creating, updating, deleting tasks |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

****

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| userId | Required | The user Id of the community account holder.Note:If the userId is missing, the admin profile details will get updated | String |
| email | Optional | Refers to the new email Id | String |
| profileImageUrl | Optional | Refers to the new profileImageUrl | Url |
| bio | Optional | Refers to the new bio | String |
| username | Optional | Refers to the new username | String |
| organizationDetails | Optional | Refers to the new employeeId | String |
| password | Optional | Current password of the community account | String |
| userGroupIds | Optional | Refers to the new user group Ids | String |

## Example - Request for Editing Username




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/update-user’ \
 -H 'X-Community-Authorization: Bearer {Unauthenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
      "userId": 62d81f2bd4c4e35f2ebb0f18,
      "username": communityHelper
    }'





## Example - Response

      

{
    "id": "62d81f2bd4c4e35f2ebb0e07",
    "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
    "experienceId": "cd6aaaad-7d02-4599-9c62-aee8068f78da",
    "experienceType": "COMMUNITY",
    "firstName": "Test",
    "lastName": "User",
    "fullName": "Test User",
    "email": "rashis.139m@gmail.com",
    "lowerCaseEmail": "rashis.139m@gmail.com",
    "gamificationInfo": {
        "points": 0.0,
        "awardInfos": []
    },
    "additional": {},
    "partnerCustomFields": {},
    "profileImageUrl": "https://sprcdn-assets.sprinklr.com/787/8e173fc3-49e5-4aa7-9aa8-a756dc626703-1059447212.jpg",
    "screenerFilled": false,
    "screenerCancelled": false,
    "lastLogin": 1659446205709,
    "deleted": false,
    "createdTime": "Jul 20, 2022 3:28:44 PM",
    "modifiedTime": "Aug 2, 2022 1:18:00 PM",
    "lastActivityAt": 1659446280567,
    "status": "APPROVED",
    "brandUser": false,
    "username": "disqushelper1",
    "lowerCaseUsername": "disqushelper1",
    "userGroupIds": [
        "4706_2382"
    ],
    "sprUrl": "https://space.sprinklr.com/new?qTyp=AUDIENCE_PROFILE&qId=COMMUNITY:62d81f2bd4c4e35f2ebb0e07",
    "organizationDetails": {},
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
}





## Example - Request for Editing Username and Profile Image




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/update-user’ \
 -H 'X-Community-Authorization: Bearer {Unauthenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
            "userId": 124,
            "username": "_NEW_USER_NAME_",
           "profileImageUrl": "_NEW_PROFILE_IMAGE_URL_"
}'





## Example - Response

      

{
    "id": "62d81f2bd4c4e35f2ebb0e07",
    "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
    "experienceId": "cd6aaaad-7d02-4599-9c62-aee8068f78da",
    "experienceType": "COMMUNITY",
    "firstName": "Test",
    "lastName": "User",
    "fullName": "Test User",
    "email": "rashis.139m@gmail.com",
    "lowerCaseEmail": "rashis.139m@gmail.com",
    "gamificationInfo": {
        "points": 0.0,
        "awardInfos": []
    },
    "additional": {},
    "partnerCustomFields": {},
    "profileImageUrl": "https://sprcdn-assets.sprinklr.com/787/8e173fc3-49e5-4aa7-9aa8-a756dc626703-1059447212.jpg",
    "screenerFilled": false,
    "screenerCancelled": false,
    "lastLogin": 1659446205709,
    "deleted": false,
    "createdTime": "Jul 20, 2022 3:28:44 PM",
    "modifiedTime": "Aug 2, 2022 1:18:00 PM",
    "lastActivityAt": 1659446280567,
    "status": "APPROVED",
    "brandUser": false,
    "username": "disqushelper1",
    "lowerCaseUsername": "disqushelper1",
    "userGroupIds": [
        "4706_2382"
    ],
    "sprUrl": "https://space.sprinklr.com/new?qTyp=AUDIENCE_PROFILE&qId=COMMUNITY:62d81f2bd4c4e35f2ebb0e07",
    "organizationDetails": {},
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
}





 [](https://dev.sprinklr.com/update-user)

[Back to top](https://dev.sprinklr.com/update-user)
