---
title: "Update Primary Participant"
slug: update-primary-participant
url: https://dev.sprinklr.com/update-primary-participant
---

# Update Primary Participant

#
  POST Update Primary Participant




This API helps update and set or unset a primary participant with the given account id.


## API Endpoint

https://api3.sprinklr.com`/{env}/`/api/v2/account/update-primary-participant

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

















****



| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| participantId | Required | Refers to the participant Id received in the create participant API call response | String |
| accountId | Required | Refers to the social account id with which the participant needs to be associated | String |
| action | Required | Refers to the action that need to be performed to link the participant with the given accountSupported Action Types:SET, UNSET | String |

**Steps to Extract Account Id from UI: **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on Accounts Icon within "Manage Workspace" module
- Click on the three dots placed alongside the respective account name
- Click on "Details" option from the drop down menu
- Click on copy url icon on the top right corner from the window that appears
- Use any encoder-decoder tool and paste the copied URL
- The account id will be the part of the decoded URL, i.e., if you get `/ACCOUNT/100426226/OVERVIEW` in the decoded URL, your account id is 100426226.

## Example - Request















Copy Code



curl -X POST \'https://api3.sprinklr.com/{env}/api/v2/account/update-primary-participant '\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "participantId": "5ef186a897c4a85e608ca03e",
    "accountId": "1234",
    "action": "SET"
}'






## Example - Response





204 No Content







[](https://dev.sprinklr.com/update-primary-participant)




[Back to top](https://dev.sprinklr.com/update-primary-participant)
