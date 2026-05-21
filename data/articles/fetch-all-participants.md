---
title: "Fetch All Participants"
slug: fetch-all-participants
url: https://dev.sprinklr.com/fetch-all-participants
---

# Fetch All Participants

#
  GET Fetch All Participants



Using this API, you can fetch all the participants setup for the given account Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/all-participants/{accountId}


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















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Required | Refers to the social account Id (existing within Sprinklr) for which you want to fetch all the participants | String |

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



	curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/account/all-participants/600001510'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






### Example - Response





{
    "data": [
        "65438f18bc6bf84f7df266e8"
    ],
    "errors": []
}







[](https://dev.sprinklr.com/fetch-all-participants)




[Back to top](https://dev.sprinklr.com/fetch-all-participants)
