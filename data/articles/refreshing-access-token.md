---
title: "Refreshing Access Token"
slug: refreshing-access-token
url: https://dev.sprinklr.com/refreshing-access-token
---

# Refreshing Access Token

#
Refreshing Access Token

You can use this api to refresh the access token using refresh token.

https://api3.sprinklr.com`/{env}/`oauth/token


**Example:** `https://api3.sprinklr.com/{env}/oauth/token?client_id={apikey}&client_secret={secret}&redirect_uri={redirect_uri}&grant_type=refresh_token&refresh_token={URL encoded refresh_token}`

**Steps to Extract Environment {env} from the UI: **

- Login to the Sprinklr's UI platform
- Right click anywhere on the homepage
- Select `"View Page Source"` from the drop-down menu
- Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.



**Dev Note: ** You can send the parameters either as query parameters or as request body parameters. Both methods are supported.

## Method 1

### Headers

The following set of HTTP header fields provide required information about the request or response, or about the object sent in the message body. Both request headers and response headers can be controlled using these endpoints.











			``




| Key | Value | Description |
| --- | --- | --- |
| Content-Type | application/x-www-form-urlencoded | Refers to the content type used in the request body |

## Query Parameters











			``





			``





			``


			****


			``





``

``



| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| {client_id} | Required | String | Value of API Key from the console. |
| {client_secret} | Required | String | Value of API Secret from the console. |
| {refresh_token} | Required | String | Populate with the refresh_token value from access token response. This should be URL encoded. |
| {redirect_uri} | Required | String | Redirect uri used while registering the application. |
| {grant_type} | Required | String | Grant type must be set to: refresh_tokenShould be url encoded |


**Dev Note: **`{refresh_token}` should be URL encoded.

**Dev Note: ** If sending key/secret details as part of query params and getting 411 error, then add Content-Length Header with value 0



## Example - Request




  Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/oauth/token?client_id={apikey}&client_secret={secret}&redirect_uri={redirect_uri}&grant_type=refresh_token&refresh_token={URL encoded refresh_token}' \
--header 'Content-Type: application/x-www-form-urlencoded'






## Example - Response

      

{
    "access_token": "[token]",
    "refresh_token": "[token]",
    "token_type": "Bearer",
    "expires_in": 28799
}






**Dev Note: **The Refresh Token has no expiry time but can be used only once. When you regenerate the token using the refresh token API, a new refresh token will be generated, and the previous one will become invalid.

## Response Definitions:










			``




			``




			``
			``



			``





| Response | Description | Type |
| --- | --- | --- |
| {access_token} | Access Token is a credential that can be used by an application to access an API | String |
| {refresh_token} | You can use refresh token to receive a new access token | String |
| {token_type} | Bearer | String |
| {expires_in} | Token expiry duration in seconds | String |

### Access Token Version

In the response headers you will receive the version of access token i.e. `SPR-TOKEN-VERSION
`

 

**Dev Notes: **Only one token can exist per API key. If you have multiple stateless instances, you'll have to generate a new API key and token pair for each of them. For example, you have two stateless applications called A and B. If application A is using a token and now application B generates the token using the same API key (client_id), application A's token will get invalidated.

## Method 2

### Headers

The following set of HTTP header fields provide required information about the request or response, or about the object sent in the message body. Both request headers and response headers can be controlled using these endpoints.











			``




| Key | Value | Description |
| --- | --- | --- |
| Content-Type | application/x-www-form-urlencoded | Refers to the content type used in the request body |

### Body Parameters











			``





			``





			``


			****


			``





``

``



| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| {client_id} | Required | String | Value of API Key from the console. |
| {client_secret} | Required | String | Value of API Secret from the console. |
| {refresh_token} | Required | String | Populate with the refresh_token value from access token response. This should be URL encoded. |
| {redirect_uri} | Required | String | Redirect uri used while registering the application. |
| {grant_type} | Required | String | Grant type must be set to: refresh_tokenShould be url encoded |

### Example - Sample Request




  Copy Code



curl -X POST 'https://api3.sprinklr.com/{env}/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={apikey}' \
--data-urlencode 'client_secret={secret}' \
--data-urlencode 'redirect_uri={redirect_uri}' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token={URL encoded refresh_token}'




### Example - Sample Response


      

{
    "access_token": "[token]",
    "refresh_token": "[token]",
    "token_type": "Bearer",
    "expires_in": {expiration duration in seconds}
}





### Response Parameters










			``




			``




			``




			``





| Response Item | Description | Type |
| --- | --- | --- |
| {access_token} | Access Token is a credential that can be used by an application to access an API | String |
| {refresh_token} | Refresh Token is a credential that can be used to refresh access token post its expiry | String |
| {token_type} | Bearer | String |
| {expires_in} | Token expiry duration in seconds | String |

 [](https://dev.sprinklr.com/refreshing-access-token)




[Back to top](https://dev.sprinklr.com/refreshing-access-token)
