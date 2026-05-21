---
title: "Client-Credentials-Get"
slug: client-credentials-get
url: https://dev.sprinklr.com/client-credentials-get
---

# Client-Credentials-Get

Table of Contents












-
    [Authorize](https://dev.sprinklr.com/authorize)


        [OAuth 2.0 for Customers](https://dev.sprinklr.com/oauth-2-0-for-customers)
        [OAuth 2.0 - SSO for Partners](https://dev.sprinklr.com/oauth-2-0-for-partners)
        [Enable Client Credentials Grant Type](https://dev.sprinklr.com/client-credentials-get)
        [JWT Certificate Based Token Generation](https://dev.sprinklr.com/jwt-token-generation)
        [OAuth 2.0 for Customers Using Postman](https://dev.sprinklr.com/oauth-2-0-using-postman)
        [Refreshing Access Token](https://dev.sprinklr.com/refreshing-access-token)
							[Mutual TLS Authentication](https://dev.sprinklr.com/mutual-tls-authentication)
        [Authorization - Troubleshooting Guide](https://dev.sprinklr.com/authorization-troubleshooting)






#
 Client Credentials Grant Type

Client credentials grant type strictly facilitates flow between client app and authorization server and runs in the background without the user’s involvement. This grant helps clients request an authorization token to access their own resources instead of user’s resources.

**Dev Notes: **A default user needs to be setup before generating token using client credentials grant type. Please reach out to the Support team for enabling it before moving ahead with the process. Please share the following information with the support team:

- `API key` (Client_id)
- `User Id` of the user you want to associate the token with. Alternatively, you can also provide Sprinklr login email address of the user.
**How to Find User Id of the User?**

- Go to "All Settings" on Sprinklr's UI and click on "Users" icon within "Manage Workspace".
- Using the Search bar, find the user you want to set up client credentials for
- Click on the three vertical dots besides the User Name and choose "Details" option from the drop down menu
- You can find the user Id as part of the browser URL in this format: `/users/1000127865/overview`. Here 1000127865 is the user Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`oauth/token

**Steps to Extract Environment from the UI: **

- Login to the Sprinklr's UI platform
- Right click anywhere on the homepage
- Select `"View Page Source"` from the drop-down menu
- Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.

### Headers

The following set of HTTP header fields provide required information about the request or response, or about the object sent in the message body. Both request headers and response headers can be controlled using these endpoints.











			``




| Key | Value | Description |
| --- | --- | --- |
| Content-Type | application/x-www-form-urlencoded | Refers to the content type used in the request body |

### Form Parameters (x-www-form-urlencoded)













            ``





			[Sprinklr's developer portal](https://dev.sprinklr.com/developer-portal-registration)





            ``




| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| grant_type | Required | Grant_type must be set to: client_credentials | String |
| client_id | Required | The application client ID (Key) that is received when you register your application on | String |
| client_secret | Required | The secret you received upon application activation. This can be found in the Sprinklr Development Portal under My Account | String |

### Example - Sample Request




  Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={API Key}' \
--data-urlencode 'client_secret={Client Secret}' \
--data-urlencode 'grant_type=client_credentials'





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

**Dev Notes: **Only one token can exist per API key. If you have multiple stateless instances, you'll have to generate a new API key and token pair for each of them. Kindly note that generating a new token will also update the refresh token.

For example, you have two stateless applications called A and B. If application A is using a token and now application B generates the token using the same API key (client_id), application A's token and refresh token will get invalidated.




				 [](https://dev.sprinklr.com/client-credentials-get)




[Back to top](https://dev.sprinklr.com/client-credentials-get)
