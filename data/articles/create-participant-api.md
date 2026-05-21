---
title: "Create Participant API"
slug: create-participant-api
url: https://dev.sprinklr.com/create-participant-api
---

# Create Participant API

#
  POST Create Participant API




Create participant API allows setting up a participant Id for the third-party bot.


**How Many Participant Ids can be Configured for an Account?: **

- Participant Id is added at the account level and is created using the user’s Authorization token
-  For one user, only one participant id gets created for the given account

## API Endpoint

https://api3.sprinklr.com`/{env}/`/api/v2/account/create-participant

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



















| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | Refers to the name you want to assign to the default participant | String |
| imageUrl | Optional | Refers to the publicly accessible url for the profile image of the participant | String |

## Example - Request















Copy Code



	curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/account/create-participant'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Test_Participant",
    "imageUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg"
}'






## Example - Response





{
    "data": {
        "id": "60373b34a595b42cd7677865",
        "name": "Test_Participant",
        "imageUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg"
    },
    "errors": []
}







### Response Definition

























| Parameter | Description | Type |
| --- | --- | --- |
| id | Refers to the backend id created for the participant | String |
| name | Refers to the configured for the participant | String |
| imageUrl | Refers to the publicly accessible url for the profile image | String |

[](https://dev.sprinklr.com/create-participant-api)




[Back to top](https://dev.sprinklr.com/create-participant-api)
