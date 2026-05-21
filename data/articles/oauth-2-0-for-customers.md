---
title: "OAuth 2.0 for Customers"
slug: oauth-2-0-for-customers
url: https://dev.sprinklr.com/oauth-2-0-for-customers
---

# OAuth 2.0 for Customers

#
OAuth 2.0 for Customers

Authentication is a 2-step process. URL #1 is used to authenticate a key via a browser. URL #2 is used to generate an OAuth token via a POST request using a API tool such as Postman.


- **Generate Code (to be run on Browser)**: https://api3.sprinklr.com/`{env}`/oauth/authorize?client_id=`{apikey}`&response_type=code&redirect_uri=`{redirect_uri}`


- **Generate Token (to be Run Using API Tool)**: https://api3.sprinklr.com/`{env}`/oauth/token?client_id=`{apikey}`&client_secret=`{secret}`&redirect_uri=`{redirect_uri}`&grant_type=authorization_code&code=`{code}`

**Dev Notes: **To generate authorization token, you need to be assigned the `Generate Token` permission from within the Sprinklr Platform. This ensures that only authorized users can generate token and access Sprinklr APIs. For more details, refer to this [Add Roles](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658) article.

### Path Parameters:


- **{env}**:  Sprinklr environment like Prod0, prod2, etc. A key generated for one environment, cannot be used in another environment. URL conventions are different for each environment. **No need to enter {env} in case of Production environment, remove {env} from URL**.

**Steps to Extract Environment from the UI: **

  - Login to the Sprinklr's UI platform
  - Right click anywhere on the homepage
  - Select `"View Page Source"` from the drop-down menu
  - Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.


- **{apikey}**: The key you get after registering your application on developer portal. This can be found in the Sprinklr Development Portal under My Account. [Click](https://dev.sprinklr.com/getting-started) for tutorial on API KEY.

- **{secret}**: The secret you received upon application activation. This can be found in the Sprinklr Development Portal under My Account.

- **{redirect_uri}**: The exact Register Callback URL you listed upon creation of your application.

- **{code}**: A code that you will receive upon user authentication. You will need this code to receive the access token.

### Step 1: Request Access to the Sprinklr Account

Direct your client browser to: `https://api3.sprinklr.com/{env}/oauth/authorize?client_id={apikey}&response_type=code&redirect_uri={redirect_uri}` Upon directing your browser, you should see a screen similar to the following:
Click Submit.

**Dev Notes: **It is recommended to have a service user with an email group created in the Sprinklr platform and giving that user the necessary access. This ensures that the token isn't tied to a specific user and it doesn't expire if the user loses access to Sprinklr platform. Where to use this service user?

- **Key Generation**: Save the service user email in the `Platform User Email Address` field.
- **Token Generation**: Use the platform login that is linked to the service user while authenticating the key via browser.

### Step 2: Authenticate the Sprinklr User

Log into Sprinklr's platform with your Sprinklr credentials. If this is the first time that you are logging in, you will need to reset your password.

### Step 3: Choose Environment Access

Check the combination of workspaces that should have access to the token.
Click Submit.

### Step 4: Access Your Redirect Code

Upon success, you will be redirected to the Redirect URI. This URI includes a returned code that you will need for authorization. **This code is valid for 10 minutes. If you do not successfully complete the following step in 10 minutes, you will need to repeat the API Access Process.** **Example**: *https://www.google.com?code=123456789*

### Step 5: Gaining Authorization



**Dev Note: ** You can send the parameters either as query parameters or as request body parameters. Both methods are supported.

Make a **POST** request using the following URL. You must set Content-Type to "`application/x-www-form-urlencoded`" in the header.

**Method 1 Using Query Parameters: **

`https://api3.sprinklr.com/{env}/oauth/token?client_id={apikey}&client_secret={secret}&redirect_uri={redirect_uri}&grant_type=authorization_code&code={code}`

**Dev Note: ** If sending Key and Secret as part of query params and getting 411 Length-Required error, then add Content-Length Header with value 0



**Method 2 with Body Parameters**

**URL: ** `https://api3.sprinklr.com/{env}/oauth/token`


**Body Parameters:**











































| Parameter | Value | Description | Required/Optional |
| --- | --- | --- | --- |
| client_id | {apikey} | Your API key | Required |
| client_secret | {secret} | Your client secret | Required |
| redirect_uri | {redirect_uri} | The redirect URI you have configured | Required |
| grant_type | authorization_code | The type of grant you are using | Required |
| code | {code} | The authorization code you received | Required |

### Response

**The response is returned in JSON.**










			```




			``




			``

			``


			``





| Response item | Type | Description |
| --- | --- | --- |
| {access_token} | String | Access Token is a credential that can be used by an application to access an API |
| {refresh_token} | String | You can use refresh token to receive a new access token |
| {token_type} | String | Bearer |
| {expires_in} | String | Token expiry duration in seconds |

```

{
    "access_token": "[token]",
    "refresh_token": "[token]",
    "token_type": "Bearer",
    "expires_in": 2591999
}

```

**Dev Notes: **Only one token can exist per API key. If you have multiple stateless instances, you'll have to generate a new API key and token pair for each of them. Kindly note that generating a new token will also update the refresh token.

For example, you have two stateless applications called A and B. If application A is using a token and now application B generates the token using the same API key (client_id), application A's token and refresh token will get invalidated.

 [](https://dev.sprinklr.com/oauth-2-0-for-customers)




[Back to top](https://dev.sprinklr.com/oauth-2-0-for-customers)
