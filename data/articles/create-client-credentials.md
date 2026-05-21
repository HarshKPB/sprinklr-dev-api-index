---
title: "Create Client Credentials"
slug: create-client-credentials
url: https://dev.sprinklr.com/create-client-credentials
---

# Create Client Credentials

#  POST Create Client Credentials

The API facilitates the creation of authentication credentials using the Client Credentials Flow of OAuth 2.0. This flow is ideal for machine-to-machine communication, where a client application needs to authenticate itself to access protected resources on behalf of the client, rather than a user.

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
| authType | String | Yes | The type of authentication being used. Supported values include OAUTH_TOKEN, OAUTH_PASSWORD, etc. |
| tokenEndpoint | String | Yes | The endpoint URL to obtain the authentication token. |
| oauthClientId | String | Yes | The client ID used for OAuth authentication. |
| oauthClientSecret | String | Yes | The client secret used for OAuth authentication. |


## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "name": "Shivangi Test OAuth Client",
    "authType": "OAUTH_TOKEN",
    "tokenEndpoint": "https://www.google.com",
    "oauthClientId": "shivangi+test@sprinklr.com",
    "oauthClientSecret": "56789abcdefgh "
}'   

     
     
 

## Example - Response




	{
    "data": "6792330a03c40e09db22f9ca",
    "errors": []
}
	 

     
     
   

### Response Schema






















| Parameter | Type | Description |
| --- | --- | --- |
| data | string | The data returned from the API, which contains a unique identifier associated with the newly created authentication credential.                  This ID can be used to delete the credential. |
| errors | object | Array of errors, if any, returned from the API. If there are no errors, it will be an empty array. |

**Dev Note:** When attempting to create connector credentials, the API will return a 400 Bad Request error response if the provided credential name already exists.


	[](https://dev.sprinklr.com/create-client-credentials)




[Back to top](https://dev.sprinklr.com/create-client-credentials)
