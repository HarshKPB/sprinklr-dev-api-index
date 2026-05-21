---
title: "Signup - New User"
slug: signup-new-user
url: https://dev.sprinklr.com/signup-new-user
---

# Signup - New User

#
Signup - New User



UnAuthenticated token helps authorize API calls that return publicly accessible data present on the community forum. This token doesn’t require any login process and can be used for read API calls.

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/jwt/un-authenticated/token

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | {{Bearer}}unauthenticated token}} | Unauthenticated token for making API calls that returns publicly accessible data |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

| Parameter | Sub-Param | Required/Optional | Decsription | Type |
| --- | --- | --- | --- | --- |
| email |  | OptionalRequired if username is not provided | Refers to the email of the user | String |
| password |  | Required | Refers to the password you need to setup for sign-up | String |
| firstName |  | Optional | Refers to the first name of the user | String |
| middleName |  | Optional | Refers to the middle name of the user | String |
| lastName |  | Optional | Refers to the last name of the user | String |
| profileImageUrl |  | Optional | Refers to the profile image url | Url |
| username |  | OptionalRequired if email is not provided | Refers to the unique username you want to set for the user | String |
| organizationDetails |  | Optional | Object defining the organization details of the user | Object |
|  | employeeId |  | Refers to the unique employee id of the user | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/user/sign-up' \
 -H 'X-Community-Authorization: Bearer {{Unauthenticated Token}}' \
 -H 'Content-Type: application/json' \
 -d '{
  "email" : "test@gmail.com",
   "password" : "Secret@123",
   "firstName" : "Test",
   "lastName" : "User",
   "profileImageUrl" : "https://www.gravatar.com/avatar/00000000000000000000000000000000.png",
   "username" : "test"
}'





## Example - Response




{
   "communityUserId": "635a89693fb53901923b4fba",
   "accessToken": "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJBY2Nlc3MgVG9rZW4gR2VuZXJhdGVkIGZyb20gQ29tbXVuaXR5IiwiaXNzIjoiU1BSSU5LTFIiLCJ0eXAiOiJKV1QiLCJjb21tdW5pdHlVc2VySWQiOiI2MzVhODk2OTNmYjUzOTAxOTIzYjRmYmEiLCJleHBlcmllbmNlSWQiOiJjZDZhYWFhZC03ZDAyLTQ1OTktOWM2Mi1hZWU4MDY4Zjc4ZGEiLCJhdWQiOlsiU1BSSU5LTFIiXSwibmJmIjoxNjY2ODc2NjAxLCJzY29wZSI6WyJSRUFEIiwiV1JJVEUiXSwiYXV0aFR5cGUiOiJTUFJfQVVUSEVOVElDQVRFRCIsInRva2VuVHlwZSI6IkFDQ0VTUyIsImV4cCI6MTY2OTQ2OTgwMSwicHJvamVjdElkIjoiOTVkYTI3YjItOGUzOC00MGVhLWEyZTEtNGUwNzY5Y2Q3NDcxIiwiaWF0IjoxNjY2ODc3ODAxLCJqdGkiOiJzcHJpbmtsciJ9.rv7V8lP_GiA3FmpYWFsttqo1b7F9KoqE1boRdqu_Ph_ByP0TVM77aub1b_VsWqzGcC-3i0y7j4wnVTuCfXN8pwwJ7i6uXMdTJSIhpWVSLZhstCY3obQo32FCAdVSOzPtotYySIBIBYorF90i-AC9Aij1MEniDAXV2wYHu0fEzGruemnlBA1Lr7oRqqwZbID7rLPWzhW4Nath5UHbOPdH4f_Fufj7y5P0WhqGVyOGVJw_27usUPhNKBR3G73qQuM4pfsO-_aC6Y4l_ecT8e6H_9esqBPimiVTfO2LKNTYie7ue6ZGe6_gKq0lUU5H-xddHoMwpV2AHKpab3yqC0H43A",
   "success": true,
   "status": "OK"
}





**Dev Notes: **The access token received in the response can be used for all community API calls, where authenticated token is required.

[](https://dev.sprinklr.com/reporting-blueprints)

[Back to top](https://dev.sprinklr.com/reporting-blueprints)
