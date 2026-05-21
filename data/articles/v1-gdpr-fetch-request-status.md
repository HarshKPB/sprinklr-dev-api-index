---
title: "GDPR - Fetch Request Status"
slug: v1-gdpr-fetch-request-status
url: https://dev.sprinklr.com/v1-gdpr-fetch-request-status
---

# GDPR - Fetch Request Status

#
  GET GDPR - Fetch Request Status

This API call will help in fetching the status of the [view profile data](https://dev.sprinklr.com/v1-gdpr-create-view-request), [edit profile data](https://dev.sprinklr.com/v1-gdpr-create-edit-request), and [delete profile data](https://dev.sprinklr.com/v1-gdpr-create-delete-request) GDPR requests.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/gdpr/{requestId}

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters













            [Create View Request API](https://dev.sprinklr.com/v1-gdpr-create-view-request)



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| requestId | Required | Refers to the Id received in the  response | String |


## Sample - Request














Copy Code




curl -X GET \
 https://api3.sprinklr.com/{env}/api/v1/gdpr/2cfc8e84db9d25b22b6e857 \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \





## Sample - Response





"SUCCESS"





### Response Parameters















| Parameter | Description | Type |
| --- | --- | --- |
| Request Status | Enum: SUCCESS, NEW, IN_PROCESS, FAILED | String |


**Dev Note: ** Kindly note that if the "FAILED" request status is returned, it might be due to some internal processing error. Kindly reach out to us using the form below to debug this.

[](https://dev.sprinklr.com/v1-gdpr-fetch-request-status)




[Back to top](https://dev.sprinklr.com/v1-gdpr-fetch-request-status)
