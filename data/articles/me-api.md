---
title: "Me Api"
slug: me-api
url: https://dev.sprinklr.com/me-api
---

# Me Api

#
  GET Me API


	 
You can fetch your own details using API key and Access token via this API call. After making the GET Request, you will get the all details in JSON format as Response.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/me


### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``



| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Accept | application/json | Determines the acceptable response type from the server |

## Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/me' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \






## Example - Response





{
    "data": {
        "name": "Sumit Kaushik",
        "customerId": 1,
        "id": 000551,
        "type": "PARTNER_USER",
        "email": "sumit@abc.com",
        "properties": {
        },
        "workspaceId": 123
    },
    "errors": []
}






[](https://dev.sprinklr.com/me-api)




[Back to top](https://dev.sprinklr.com/me-api)
