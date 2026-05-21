---
title: "Update Agent Status v1"
slug: update-agent-status-v1
url: https://dev.sprinklr.com/update-agent-status-v1
---

# Update Agent Status v1

#
  POST - Update Agent Status

This API call helps update the availability status of the customer service agent.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/user/update/user/status

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters














****



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| status | Required | The status of the agent you want to updateExample: If the status needs to be updated from available to busy, we will pass Busy in the query parameter | String |
| userId | Required | Refers to the user Id of the customer service agent | String |


## Sample - Request














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/user/update/user/status?status=Busy&userId=731510' \
  -H 'Authorization: Bearer {token}' \
  -H 'key: {apikey}' \
  -H 'Content-Type: application/json' \





## Sample - Response





204 No Content





**Dev Notes: **You can use the [Read User API](https://dev.sprinklr.com/read-user) to fetch the status of the agent. Refer to `data.globalAttributes.partnerCustomProperties.spr_user_availability_status` within the response to see the current agent status.

[](https://dev.sprinklr.com/v1-update-agent-status)




[Back to top](https://dev.sprinklr.com/v1-update-agent-status)
