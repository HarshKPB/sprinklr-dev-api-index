---
title: "Create OAuth 1.0 Credentials"
slug: create-oauth-1-0-credentials
url: https://dev.sprinklr.com/create-oauth-1-0-credentials
---

# Create OAuth 1.0 Credentials

#  POST Create OAuth 1.0 Credentials

This API enables the creation of authentication credentials using the OAuth 1.0 protocol. OAuth 1.0 is an authorization framework that allows secure, token-based authentication for third-party applications without exposing user credentials.

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
| authType | String | Yes | The type of authentication being used. Supported values include OAUTH_1, OAUTH_2, etc. |
| tokenEndpoint | String | Yes | The endpoint URL to obtain the authentication token. |
| oauthClientId | String | Yes | The client ID used for OAuth 1.0 authentication. |
| oauthClientSecret | String | Yes | The client secret used for OAuth 1.0 authentication. |
| addAuthDataTo | String | Yes | Indicates where the authentication data should be added. Supported values: request, header. |
| oauthAccessToken | String | No | The access token required for OAuth 1.0 authentication. |
| oauthAccessTokenSecret | String | No | The access token secret required for OAuth 1.0 authentication. |


## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "name": "Shivangi Test OAuth",
    "authType": "OAUTH_1",
    "tokenEndpoint": "https://www.google.com",
    "oauthClientId": "shivangi+test@sprinklr.com",
    "oauthClientSecret": "56789abcdefgh ",
    "addAuthDataTo": "request",
    "oauthAccessToken": "E13zqlMcOuEMobsKSLvdqCU4A6e1jddL8oM36tx8",
    "oauthAccessTokenSecret": "MeE6EjoFfmsMa9Wy6RMSiYXxKpF3VSpSHx"
}'  

     
     
 

## Example - Response




	{
    "data": "679230705882ec48d9ca1554",
    "errors": []
}
	 

     
     
   

### Response Schema






















| Parameter | Type | Description |
| --- | --- | --- |
| data | string | The data returned from the API, which contains a unique identifier associated with the newly created authentication credential.                  This ID can be used to delete the credential. |
| errors | object | Array of errors, if any, returned from the API. If there are no errors, it will be an empty array. |

**Dev Note:** When attempting to create connector credentials, the API will return a 400 Bad Request error response if the provided credential name already exists.


	[](https://dev.sprinklr.com/create-oauth-1-0-credentials)




[Back to top](https://dev.sprinklr.com/create-oauth-1-0-credentials)
