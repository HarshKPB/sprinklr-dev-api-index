---
title: "Fetch Screener Answers"
slug: fetch-screener-answers
url: https://dev.sprinklr.com/fetch-screener-answers
---

# Fetch Screener Answers

#
  POST - Fetch Screener Answers

Using this API, you can find the answers to the screener questions using the unique screen question Ids.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/xb-community/screener-answer

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

### Request Parameters












| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| screenerQuestionId | Required | the unique identifier for the screen questions | List[Integer] |

### Example - Request














Copy Code




curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/xb-community/screener-answer’ /
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'
  -d '{
[
 "5f48c99aed87992571ff0cf9",
 "5da944f67edc204b061604b5"
]
}'





### Example - Response





{
   "data": {
       "5f48c99aed87992571ff0cf9": [
           {
               "id": "5f48c99aed87992571ff0cfb",
               "questionId": "5f48c99aed87992571ff0cf9",
               "displayText": "A", - question
               "siteId": "04b70a51-ad01-4872-90fd-47449cfd3e16", - project id
               "clientId": 19,
               "ownerUserId": 600001669, - project owner
               "createdTime": "Aug 28, 2020 9:08:42 AM",
               "modifiedTime": "Aug 28, 2020 9:08:42 AM",
               "deleted": false,
               "canEdit": false
           },
           {
               "id": "5f48c9abed87992571ff0db5",
               "questionId": "5f48c99aed87992571ff0cf9",
               "displayText": "B",
               "siteId": "04b70a51-ad01-4872-90fd-47449cfd3e16",
               "clientId": 19,
               "ownerUserId": 600001669,
               "createdTime": "Aug 28, 2020 9:08:59 AM",
               "modifiedTime": "Aug 28, 2020 9:08:59 AM",
               "deleted": false,
               "canEdit": false
           }
       ]
   },
   "errors": []
}





### Response Parameters - Array of Screen Answer Ids











| Parameters | Description | Type |
| --- | --- | --- |
| id | The unique answer Id corresponding to the given screener question Id | String |
| questionId | The unique question Id. The same as the one passed in the request payload | String |
| displayText | The display text of the answer | String |
| siteId | The unique identifier for the project | string |
| clientId | Refers to the unique client Id (workspace) | Integer |
| ownerUserId | Refers to the owner Id of the user who owns the project | Integer |
| createdTime | The time at which the answer was recorded | String |
| modifiedTime | The time at which the answer was last modified | String |
| deleted | If yes, the screener answer has been deleted | Boolean |
| canEdit | If true, the screen answer can be edited | Boolean |

	 [](https://dev.sprinklr.com/fetch-screener-answers)




[Back to top](https://dev.sprinklr.com/fetch-screener-answers)
