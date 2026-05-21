---
title: "Create Basic Authentication Credentials"
slug: create-basic-authentication-credentials
url: https://dev.sprinklr.com/create-basic-authentication-credentials
---

# Create Basic Authentication Credentials

#  POST Create Basic or OAuth2.0 ROPC Authentication Credentials

This API allows you to create external authentication credentials using the Basic Authentication Type.


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





















            ````



























| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| name | string | required | The name of the external authentication credential. |
| authType | string | required | The type of authentication being used. For this request, use ‘BASIC’ to create OAuth2.0 RPOC credentials or 'STD_BASIC_AUTH' to create standard basic authentication credentials. |
| grantType | string | optional | Defines the grant type. For this request, use ‘client_credentials’ for client-based authentication. |
| userID | string | required | The user identifier associated with the authentication. |
| password | string | required | The password associated with the provided userId. |
| requestViaProxy | Boolean | optional | Indicates if the request should be routed through a proxy. Default is false. If set to true, the request is sent via a proxy. |

## Example 1 - Create OAuth 2.0 ROPC Authentication Credentials




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "name": "Shivangi Test Basic",
    "authType": "BASIC",
    "grantType": "client_credentials",
    "userId": "shivangi.singh+test@sprinklr.com",
    "password": "1234@",
    "requestViaProxy": true
}'
	 

     
     
 

## Example - Response




	{
    "data": "67990812259f4a0ca47468ab",
    "errors": []
}
	 

     
     
   


## Example 2 - Create Standard Basic Authentication




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "name": "Shivangi Test Basic",
    "authType": "STD_BASIC_AUTH",
    "grantType": "client_credentials",
    "userId": "shivangi.singh+test@sprinklr.com",
    "password": "1234@",
    "requestViaProxy": true
}'
	 

     
     
 

## Example - Response




	{
    "data": "67990812259f4a0ca6789ab",
    "errors": []
}
	 

     
     
   

### Response Schema






















| Parameter | Type | Description |
| --- | --- | --- |
| data | string | The data returned from the API, which contains a unique identifier associated with the newly created authentication credential.                  This ID can be used to delete the credential. |
| errors | object | Array of errors, if any, returned from the API. If there are no errors, it will be an empty array. |



**Dev Note:** When attempting to create connector credentials, the API will return a 400 Bad Request error response if the provided credential name already exists.

	[](https://dev.sprinklr.com/create-basic-authentication-credentials)




[Back to top](https://dev.sprinklr.com/create-basic-authentication-credentials)
