---
title: "Fetch Role Using Role Id"
slug: fetch-role-using-role-id
url: https://dev.sprinklr.com/fetch-role-using-role-id
---

# Fetch Role Using Role Id

#
Fetch Role Using Role Id

Using this API, you can fetch the role details for the given role Id.

**Dev Notes: **The Community APIs are designed to support limited and specific use cases only. They are not intended for building or replicating a full-scale community platform. For more advanced or large-scale community features, please contact your Sprinklr representative to explore supported solutions.

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/user-role/{roleid}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {unauthenticated token} | Unauthenticated token for making API calls that returns publicly accessible data |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Path Parameters

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| roleId | Required | The unique identifier for the role you want to fetch the details for | String |

## Example - Request




  Copy Code



curl -X GET \
  'https://care-api-{env}.sprinklr.com/care/community/rest/un-authenticated/user-role/619398ac9bc0176d403afe47' \
 -H 'X-Community-Authorization: Bearer {Unauthenticated Token}' \
 -H 'Content-Type: application/json' \





## Example - Response

      

{
   "id": "619398ac9bc0176d403afe47",
   "name": "Limited access",
   "projectId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
   "permissions": [
       "RESET_USER_PASSWORD",
       "MARK_AS_ACCEPTED_ANSWER",
       "MERGE_POST",
       "MANAGE_PRIVATE_MESSAGES",
       "UPDATE_TOPIC",
       "MARK_AS_SPAM",
       "EDIT_USER_EMPLOYEE_ID"
   ],
   "deleted": false,
   "createdTime": 1637062828341,
   "modifiedTime": 1637062828341
}





	[](https://dev.sprinklr.com/fetch-role-using-role-id)

[Back to top](https://dev.sprinklr.com/fetch-role-using-role-id)
