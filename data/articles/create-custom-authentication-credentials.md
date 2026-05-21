---
title: "Create Custom Authentication Credentials"
slug: create-custom-authentication-credentials
url: https://dev.sprinklr.com/create-custom-authentication-credentials
---

# Create Custom Authentication Credentials

#  POST Create Custom Authentication Credentials

This API allows you to create external API credentials using a Custom Authentication Type. This includes support for various authentication configurations such as JWT and custom claim handling.

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
| name | String | Yes | The name of the external API credential. |
| authType | String | Yes | Specifies the type of authentication being used. Supported values include JWT. |
| signatureAlgorithm | String | Yes | The algorithm used to sign the JWT. Supported values: HS256, HS384, HS512. |
| jwtSecret | String | Yes | The secret key used to sign the JWT. |
| jwtClaims | Object | Yes | A key-value pair object defining claims to include in the JWT payload. |
| jwtHeaders | Object | Yes | A key-value pair object defining custom headers to include in the JWT. |
| preRequestScript | String | No | A script to execute before sending the API request. |
| responseAdapter | String | No | A custom logic adapter to process and transform the API response. |
| customClaimsAdapter | String | No | A custom logic adapter to dynamically modify the claims included in the JWT. |


### Custom Authentication Configuration


















| Parameter | Description |
| --- | --- |
| httpMethod | Specifies the HTTP method for authentication. Supported values: POST, GET. |
| contentTypeHeader | Specifies the content type for authentication. Supported values: application/x-www-form-urlencoded, multipart/form-data, application/json. |

## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "name": "Avinash Test 6",
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
                       },
    "preRequestScript": "asd",
    "responseAdapter": "asd",
    "customClaimsAdapter": "asd"
}'  

     
     
 

## Example - Response




	{
    "data": "67921bb703c40e09db21a59d",
    "errors": []
}
	 

     
     
   

### Response Schema






















| Parameter | Type | Description |
| --- | --- | --- |
| data | string | The data returned from the API, which contains a unique identifier associated with the newly created authentication credential.                  This ID can be used to delete the credential. |
| errors | object | Array of errors, if any, returned from the API. If there are no errors, it will be an empty array. |

**Dev Note:** When attempting to create connector credentials, the API will return a 400 Bad Request error response if the provided credential name already exists.


	[](https://dev.sprinklr.com/create-custom-authentication-credentials)




[Back to top](https://dev.sprinklr.com/create-custom-authentication-credentials)
