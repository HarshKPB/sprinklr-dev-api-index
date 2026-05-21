---
title: "Update Community User"
slug: update-community-user
url: https://dev.sprinklr.com/update-community-user
---

# Update Community User

#
  PUT - Update Community User

Using this API, you can update information for the given community user Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/xb-community/update/user/{communityUserId}

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters












[find community users API](https://dev.sprinklr.com/find-users-using-project-id)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| communityUserId | Required | The user Id of the community userYou can use the  to fetch the required community user Id | String |

### Request Parameters












****








``

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Field name will depend on the chosen update action.Example:profileImageUrl for updating profile imageOr,name for updating name | Required | The parameter defining the updated value for the given field | String |
| updateActions | Required | Refers to the update action typeSupported UPDATE_ACTIONS include: UPDATE_SCREENER, UPDATE_NAME, UPDATE_DOB, UPDATE_BIO, UPDATE_CONTACT_INFO, UPDATE_PROFILE_IMAGE_URL, UPDATE_STATUS | String |

### Example - Request














Copy Code




curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/xb-community/update/user/605062da38e94c6bfe186ea0' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
  {
    "profileImageUrl": "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg",
    "updateActions": [
        "UPDATE_PROFILE_IMAGE_URL"
    ]
}'





### Example - Response





  {
    "data": {
        "id": "630776cfa14754297250e797",
        "universalProfileId": "630776cfd631435e150b62cd",
        "projectId": "e2b2758d-9525-4b1f-bcf3-18c2ddaa571d",
        "experienceId": "f7141a8f-45c1-4e54-a017-05838d3c85c8",
        "experienceType": "ADVOCACY",
        "firstName": "Orange",
        "lastName": "Hegde",
        "fullName": "Orange Hegde",
        "gender": "MALE",
        "dob": {
            "day": 25,
            "month": 8,
            "year": 2022
        },
        "email": "orangehegde+1@gmail.com",
        "contactInfo": {},
        "gamificationInfo": {
            "points": 438.0,
            "typeVsAwardIds": {
                "BADGE": [
                    "a8c0c2c5-0ec1-4c7b-9f4a-43fd671dfd04",
                    "de3b2edb-4df0-4e46-a11f-3edb284ab98c"
                ]
            },
            "eventsCompleted": [],
            "awardInfos": []
        },
        "stats": {
            "LOGIN_COUNT": 16.0,
            "SHARE_COUNT": 15.0,
            "SHARE_COUNT_TWITTER": 2.0,
            "UPLOAD_CONTENT_COUNT": 1.0,
            "COMMENT_COUNT": 3.0,
            "REPLY_COUNT": 1.0,
            "SHARE_COUNT_INSTAGRAM": 9.0,
            "USER_CREATED_POST_SHARE_COUNT": 5.0,
            "USER_CREATED_POST_SHARE_COUNT_INSTAGRAM": 3.0,
            "USER_CREATED_POST_SHARE_COUNT_FACEBOOK": 1.0,
            "SHARE_COUNT_FACEBOOK": 4.0,
            "USER_CREATED_POST_SHARE_COUNT_TWITTER": 1.0,
            "BOOKMARK_COUNT": 1.0
        },
        "additional": {
            "STATUS_CHANGED_BY": "CU_62d7a9cd6ae53055aff97714"
        },
        "partnerCustomFields": {
            "_c_62c4001c7824c50967f02946": [
                "Singapore"
            ],
            "_c_605b22d83611ba66e59603de": [
                "Hockey"
            ]
        },
        "profileImageUrl": "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg",
        "largeProfileImageUrl": "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg",
        "screenerFilled": true,
        "screenerCancelled": false,
        "admin": false,
        "screenerResponse": {
            "6131bc36d228cd27e2ea1b26": [
                "6131bc37d228cd27e2ea1b59"
            ],
            "61403e4c9cbdaf3bb18a9374": [
                "61403e4d9cbdaf3bb18a93bb"
            ]
         },
        "lastLogin": 1662005652813,
        "status": "APPROVED",
        "statusChangeTime": 1661433702299,
        "allStatusValues": [
            "SCREENER_PENDING",
            "PENDING",
            "APPROVED"
        ],
        "preferredLangCode": "en",
        "customProperties": {},
        "brandUser": false,
        "gamificationDisabled": false,
        "permissions": [],
        "chatPartnerUser": false,
        "ownerUserId": 600001669,
        "createdTime": "Aug 25, 2022 1:19:11 PM",
        "modifiedTime": "Sep 1, 2022 2:56:33 PM",
        "lastModifiedUserId": 600001669,
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}





	 [](https://dev.sprinklr.com/update-community-user)




[Back to top](https://dev.sprinklr.com/update-community-user)
