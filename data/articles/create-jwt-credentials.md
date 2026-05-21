---
title: "Create JWT Credentials"
slug: create-jwt-credentials
url: https://dev.sprinklr.com/create-jwt-credentials
---

# Create JWT Credentials

#  POST Create JWT Credentials

This API allows you to create authentication credentials using JSON Web Tokens (JWT). JWT is a compact, URL-safe means of representing claims between two parties. This API enables secure generation and management of JWT-based credentials for applications that require token-based authentication.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/connector-cred/create

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

## Request Body





























































| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | The name of the external authentication credential. |
| authType | String | Yes | The type of authentication being used. For this request, it is JWT. |
| signatureAlgorithm | String | Yes | The algorithm used to sign the JWT. Supported values: HS256, HS384, HS512. |
| jwtSecret | String | Yes | The secret key used to sign the JWT. |
| jwtClaims | Object | Yes | A key-value pair object defining the claims to include in the JWT payload. |
| jwtHeaders | Object | Yes | A key-value pair object defining custom headers to include in the JWT. |
| responseAdapter | String | No | A custom logic adapter to modify or process the response received from the external API. |
| customClaimsAdapter | String | No | A custom logic adapter to modify or process the claims included in the JWT. |

## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data ' {
"name": "Shivangi Test JWT",
"authType": "JWT",
"signatureAlgorithm": "HS256",
"jwtSecret": "asd",
"jwtClaims": {
                       "userRole": "admin",
                       "organizationId": "org-12345",
                        "isVerified": true
},
"jwtHeaders": {
                         "x-client-id": "12345",
                         "x-request-id": "abcde-12345"
                       }
} '  

     
     
 

## Example - Response




	{
    "data": "67990e387b60507fc0a88f77",
    "errors": []
}
 

     
     
   

### Response Schema






















| Parameter | Type | Description |
| --- | --- | --- |
| data | string | The data returned from the API, which contains a unique identifier associated with the newly created authentication credential.                  This ID can be used to delete the credential. |
| errors | object | Array of errors, if any, returned from the API. If there are no errors, it will be an empty array. |

**Dev Note:** When attempting to create connector credentials, the API will return a 400 Bad Request error response if the provided credential name already exists.


	[](https://dev.sprinklr.com/create-jwt-credentials)




[Back to top](https://dev.sprinklr.com/create-jwt-credentials)
