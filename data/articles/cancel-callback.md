---
title: "Cancel Callback"
slug: cancel-callback
url: https://dev.sprinklr.com/cancel-callback
---

# Cancel Callback

#
 POST  Cancel Callback



Using this API, the scheduled callback can be cancelled

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/voice/cancel-callback

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/ /api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters













[schedule callback API](https://dev.sprinklr.com/schedule-callback)




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| taskId | Required | Refers to the task id of the callbackThe task Id can be fetched from the  response | String |

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/voice/cancel-callback'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
  -d '{
    "taskId": "662222c12b77c55fd5f77e80"
}'






## Example - Response





{
    "data": true,
    "errors": []
}







### Response Parameters















| Parameter | Definition | Type |
| --- | --- | --- |
| data | If true, it implies that the callback has been successfully cancelled | Boolean |

[](https://dev.sprinklr.com/cancel-callback)




[Back to top](https://dev.sprinklr.com/cancel-callback)
