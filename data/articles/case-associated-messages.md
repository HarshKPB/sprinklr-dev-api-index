---
title: "Case Associated Messages"
slug: case-associated-messages
url: https://dev.sprinklr.com/case-associated-messages
---

# Case Associated Messages

#
  GET - Case Associated Messages

Using this API, you can fetch all the message Ids associated with the case so far. Once you have the message Ids, you can call [Read message by message Id](https://dev.sprinklr.com/read-message-by-id) or [Read Messages (Bulk) API](https://dev.sprinklr.com/read-messages-bulk) to fetch all the messages associated with the given message Ids. Moreover, you can also use a cursor to fetch all message ids associated with case after a certain time.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/case/associated-messages?id=`{case_id}`


**Dev Notes: ** If you want to fetch all message ids associated in case after a certain time frame, you can use cursor.

	https://api3.sprinklr.com`/{env}/`api/v2/case/associated-messages?id=`{case_id}`&cursor=`{epoch_time}`

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

### Query Parameters













[read case by case number](https://dev.sprinklr.com/read-case-by-case-number)[search entity (case)](https://dev.sprinklr.com/search-by-entity)










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| caseId | Required | Id of the case for which you want fetch all associated messages.If you have the case number, you can fetch the case Id using  API or  API | String |
| epoch_time | Optional | If you want to fetch all message ids associated in case after a certain time frame, you can use cursor. | Unix timestamp |

## Example - Using CaseId




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/case/associated-messages?id=6387800c59a6a6228f8c5ee2' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





## Example - Response




"data": [
        "ACCOUNT_600000163_1567258145000_INSTAGRAM_37_17927074666310191",
        "ACCOUNT_600000163_1567259773000_INSTAGRAM_305_2122651287519496869_5026524167",
        "ACCOUNT_600000163_1567260408000_INSTAGRAM_304_17843614366624845",
        "ACCOUNT_600000163_1568369975000_INSTAGRAM_311_17960988046292062",
        "ACCOUNT_600000163_1568378183000_INSTAGRAM_311_17986342540277270",
        "ACCOUNT_600000163_1568386528000_INSTAGRAM_311_18098451478040067"
     ]





 

## Example - Using CaseId and Epoch Time




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/case/associated-messages?id=6387800c59a6a6228f8c5ee2&cursor=1669824524315' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





## Example - Response




"data": [
        "ACCOUNT_600000163_1570101975000_INSTAGRAM_311_18104664901025841",
        "ACCOUNT_600000163_1570105564000_INSTAGRAM_311_17859543286536540"
    ]






**Dev Notes: ** If you want to read through the associated message Ids in above response, you can use this [Endpoint](https://dev.sprinklr.com/read-message-by-id).


 

[](https://dev.sprinklr.com/case-associated-messages)




[Back to top](https://dev.sprinklr.com/case-associated-messages)
