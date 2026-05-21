---
title: "Create OAuth Refresh Token Credentials"
slug: create-oauth-refresh-token-credentials
url: https://dev.sprinklr.com/create-oauth-refresh-token-credentials
---

# Create OAuth Refresh Token Credentials

#  POST Create OAuth Refresh Token Credentials

This API allows you to create external authentication credentials for the OAuth Refresh Token authentication mechanism. It is designed to facilitate the integration of external systems that require OAuth 2.0 authentication with a refresh token for obtaining access to protected resources.


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

















































| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| name | string | required | The name of the external authentication credential. |
| authType | string | required | The type of authentication being used. To create a credential for OAuth Refresh Token authentication type, use ‘OAuth Refresh Token’. |
| tokenEndpoint | string | required | The endpoint URL to obtain the authentication token. |
| oauthClientId | string | required | The client ID used for OAuth Refresh Token authentication. |
| oauthClientSecret | string | required | The client secret used for OAuth Refresh Token authentication. |
| oauthRefreshToken | string | required | The refresh token used for OAuth Refresh Token authentication. |


## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{    "name": "Avinash Test OAuth 1",
    "authType": "OAUTH_REFRESH",
    "tokenEndpoint": "https://www.google.com",
    "oauthClientId": "shivangi+test@sprinklr.com",
    "oauthClientSecret": "56789abcdefgh",
    "oauthRefreshToken": " E13zqlMcOuEMobsKSLvdqCU4A6e1jddL8oM36tx8oQE1MTQzYmY2Ni0wM2U2LTM2NmUtOWFkMy01MGI5ZTE1ZjIwYTA="
	}' 

     
     
 

## Example - Response




	{
    "data": "679205cb03c40e09db205925",
    "errors": []
}
	 

     
     
   

### Response Schema






















| Parameter | Type | Description |
| --- | --- | --- |
| data | string | The data returned from the API, which contains a unique identifier associated with the newly created authentication credential.                  This ID can be used to delete the credential. |
| errors | object | Array of errors, if any, returned from the API. If there are no errors, it will be an empty array. |

**Dev Note:** When attempting to create connector credentials, the API will return a 400 Bad Request error response if the provided credential name already exists.

	[](https://dev.sprinklr.com/create-oauth-refresh-token-credentials)




[Back to top](https://dev.sprinklr.com/create-oauth-refresh-token-credentials)
