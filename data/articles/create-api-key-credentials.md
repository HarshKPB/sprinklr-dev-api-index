---
title: "Create API Key Credentials"
slug: create-api-key-credentials
url: https://dev.sprinklr.com/create-api-key-credentials
---

# Create API Key Credentials

#  POST Create API Key Credentials

This API allows you to create external API credentials using a API key Authentication Type.

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

## Response Body





































| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | The name of the external API credential. |
| authType | String | Yes | Specifies the type of authentication being used. Supported value: API_KEY. |
| apiKey | String | Yes | The API key used for authentication. |
| password | String | Yes | Password to provide additional security for the API key. |

## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/create' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "name": "Shivangi Test API Key",
    "authType": "API_KEY",
    "apiKey": "abcd1234",
    "password": "asd"
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


	[](https://dev.sprinklr.com/create-api-key-credentials)




[Back to top](https://dev.sprinklr.com/create-api-key-credentials)
