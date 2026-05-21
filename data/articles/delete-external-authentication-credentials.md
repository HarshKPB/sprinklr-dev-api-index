---
title: "Delete External Authentication Credentials"
slug: delete-external-authentication-credentials
url: https://dev.sprinklr.com/delete-external-authentication-credentials
---

# Delete External Authentication Credentials

#  DELETE Delete External Authentication Credentials

This API allows you to delete external API credentials by specifying the unique credential ID in the URL path.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/connector-cred/{credentialId}

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

## Path Parameter



















| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| credentialId | String | Yes | The unique identifier of the credential to delete. |

## Example - Request




 Copy Code


curl --location --request DELETE 'https://api3.sprinklr.com/{env}/api/v2/connector-cred/679228515882ec48d9c99e62' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_KEY}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \  

     
     
 

## Example - Response




{
    "data": true,
    "errors": []
}  

     
     
   

### Response Schema






















| Parameter | Type | Description |
| --- | --- | --- |
| data | Boolean | Indicates the success of the operation. A value of `true` signifies that the deletion was successful, while a value of `false` indicates that the specified credential ID had already been deleted. |
| errors | Array | Array of errors, if any, returned from the API. If there are no errors, it will be an empty array. |

**Dev Note:** When attempting to delete connector credentials, the API will return a 404 Not Found error response if the provided credential id has already been deleted.


	[](https://dev.sprinklr.com/delete-external-authentication-credentials)




[Back to top](https://dev.sprinklr.com/delete-external-authentication-credentials)
