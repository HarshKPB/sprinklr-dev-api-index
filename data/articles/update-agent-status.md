---
title: "Update Agent Status"
slug: update-agent-status
url: https://dev.sprinklr.com/update-agent-status
---

# Update Agent Status

#
  POST - Update Agent Status



This API allows you to update an agent's availability status, which will be stored in the `spr_user_availability_status` custom field.

### Use Cases:

- **For Global Admins:** Provides the capability to update the availability status of any agent directly from the backend.

- **For Agents:** Empowers agents to update their own availability status independently.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/user/update-user-status

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the server.For generating authorization token, refer to  section on the developer portal. |
| Key | api-key | API key helps authenticate the application with the server.For generating API key, refer to  guide. |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body. |
| Accept | application/json | Determines the acceptable response type from the server. |

### Path Parameters







****

| Parameters | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| status | Required | String | The status of the agent you want to update.Example: If the status needs to be updated from available to busy, we will pass Busy in the query parameter. |
| userId | Required | String | Refers to the user Id of the customer service agent. |
| federationId | Optional | String | Refers to the external user Id of the customer service agent. Assigning a Federation ID helps with unique identification. You cannot assign the same federation identity to more than one user. The federation ID is additionally used by Customer Environments for attaching extra SSO Login information |

## Sample - Request














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/user/update-user-status?status=Busy&userId=731510' \
  -H 'Authorization: Bearer {token}' \
  -H 'key: {apikey}' \
  -H 'Content-Type: application/json' \
 

     
     
   

## Sample - Response





204 No Content
 

     
     
   
 

**Dev Notes: **You can use the [Read User API](https://dev.sprinklr.com/read-user) to fetch the status of the agent. Refer to `data.globalAttributes.partnerCustomProperties.spr_user_availability_status` within the response to see the current agent status.

[](https://dev.sprinklr.com/update-agent-status) 

 

 
[Back to top](https://dev.sprinklr.com/update-agent-status)
