---
title: "Delete Listening Alert"
slug: delete-listening-alert
url: https://dev.sprinklr.com/delete-listening-alert
---

# Delete Listening Alert

#   DELETE Delete Listening Alert
 

This API allows you to delete a listening alert from Sprinklr.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/alert-manager/`{listening_alert_id}`

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

















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {listening_alert_id} | Required | Id of the listening alert you want to delete. You can get this Id from the Create Listening Alert API . | String |

## Example - Request




 Copy Code


curl --location --request DELETE 'https://api3.sprinklr.com/{env}/api/v2/alert-manager/{listening_alert_id}' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'key: kza3r3nx3x558ga8f74h74ej' \
--header 'Content-Type: application/json' \
--data '''



## Example - Response





204
No Content



**Dev Notes: **A `204 No Content` response indicates that the listening alert was successfully deleted.

[](https://dev.sprinklr.com/delete-listening-alert) 

 

 
[Back to top](https://dev.sprinklr.com/delete-business-holiday-list)
