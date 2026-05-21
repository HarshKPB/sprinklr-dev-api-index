---
title: "Deactivate Account"
slug: deactivate-account
url: https://dev.sprinklr.com/deactivate-account
---

# Deactivate Account

#
  PUT Deactivate Account

Using this API, you can deactivate an account for the given account Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/{accountId}/deactivate

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

### Path Parameter













-
-
-
-
-
-
-
- ``



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Required | Unique Id of the account.Steps to extract account id from the UI:Click on the hamburger menu on the top left cornerNavigate to All Settings OptionsClick on Accounts IconClick on the three dots alongside the account name you want the fetch the id forClick on details from the drop down menuClick on copy url icon on the top right corner from the window that appearsUse any encoder-decoder tool and paste the copied URLThe account id will be the part of the decoded URL, i.e., if you get /ACCOUNT/100426226/OVERVIEW in the decoded URL, your account id is 100426226. | String |

## Example - Request




 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/account/600000132/deactivate' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \





## Example - Response




 {
    "data": true,
    "errors": []
}





**Dev Notes: **

- `200 OK` and `"data": true` implies that the account has been successfully deactivated
- In case you pass an invalid account Id, you'll receive `404 Not Found` in the response along with the message — `"No object found for ACCOUNT : {accountId}"`
[](https://dev.sprinklr.com/deactivate-account)




[Back to top](https://dev.sprinklr.com/deactivate-account)
