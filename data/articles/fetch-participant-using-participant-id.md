---
title: "Fetch Participant Using Participant Id"
slug: fetch-participant-using-participant-id
url: https://dev.sprinklr.com/fetch-participant-using-participant-id
---

# Fetch Participant Using Participant Id

#
  GET Fetch Participant Using Participant Id



Using this API, you can fetch all the participant details for the given participant Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/get-participant/{participantId}

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
| participantId | Required | Refers to the participant Id for which you want to fetch the details | String |

## Example - Request















Copy Code


curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/account/get-participant/65438f18bc6bf84f7df266e8'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






### Example - Response





{
    "data": {
        "id": "65438f18bc6bf84f7df266e8",
        "name": "TestBot"
    },
    "errors": []
}







	[](https://dev.sprinklr.com/fetch-participant-using-participant-id)




[Back to top](https://dev.sprinklr.com/fetch-participant-using-participant-id)
