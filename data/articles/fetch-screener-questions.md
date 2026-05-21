---
title: "Fetch Screener Questions"
slug: fetch-screener-questions
url: https://dev.sprinklr.com/fetch-screener-questions
---

# Fetch Screener Questions

#
  GET - Fetch Screener Questions

Using this API, you can find all the screener questions defined for a project.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/xb-community/screener/{projectId}

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














[Fetch Project Id API](https://dev.sprinklr.com/fetch-project-id)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| projectId | Required | The unique project Id for the advocacy communityUse  documentation to get projectId | String |

### Example - Request















Copy Code



curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/xb-community/screener/04b70a51-ad01-4872-90fd-47449cfd3e16’ /
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





### Example - Response





{
   "data": [
       {
           "id": "5dc10c68c7a0e37674b568f4",
           "questionType": "REGISTRATION",
           "answerType": "PICKLIST",
           "displayText": "Region",
           "sourceType": "ADVOCACY",
           "questionControllingConfig": {
               "visibilityControllingEntity": "CONTROL_BASED_ON_VALUE",
               "controllingFieldConfig": {
                   "5dc10c69c7a0e37674b568f6": [
                       "5f48c985ed87992571ff0c1d"
                   ],
                   "5dc10c71c7a0e37674b56915": [
                       "5fa3a4d152a5dd2ac32fc85d"
                   ]
               }
           },
           "additional": { - additional details
               "answerType": [
                   "RADIO"
               ],
               "REQUIRED": [
                   "true"
               ],
               "IS_PUBLIC": [
               ],
               "FROM_SSO": [
                   "false"
               ]
           },
           "siteId": "04b70a51-ad01-4872-90fd-47449cfd3e16",
           "clientId": 19,
           "ownerUserId": 600001669,
           "createdTime": "Nov 5, 2019 5:45:12 AM",
           "modifiedTime": "Jul 22, 2022 5:10:45 AM",
           "lastModifiedUserId": 600005781,
           "deleted": false,
           "canEdit": false
       }
   ],
   "errors": []
}





	 [](https://dev.sprinklr.com/fetch-screener-questions)




[Back to top](https://dev.sprinklr.com/fetch-screener-questions)
