---
title: "OAuth 2.0 Using Postman"
slug: oauth-2-0-using-postman
url: https://dev.sprinklr.com/oauth-2-0-using-postman
---

# OAuth 2.0 Using Postman

#
OAuth 2.0 Using Postman

A customer can either generate a token using the combination of browser and Postman using [this guide](https://dev.sprinklr.com/oauth-2-0-for-customers) or they can generate a token using Postman alone.

This article talks about the latter. You can generate an authentication token through Postman in 8 simple steps.

**Dev Notes:**Before you move ahead with generating the authorization token, please ensure that you have generated the key (client_id) and secret (client_secret) using the [Getting Started](https://dev.sprinklr.com/getting-started) guide.

Once you have access to the key and secret, follow through the steps below for generating access token.

### Step 1

Click on the Authorization Tab on the Postman console.

### Step 2

From the drop-down menu that appears against Type, select OAuth 2.0

### Step 3

In the Configure New Token section, fill in the following parameters:












			****





			``







``

``

[registering your application](https://dev.sprinklr.com/api-key-and-secret-generation)

[key](https://dev.sprinklr.com/api-key-and-secret-generation)

-
-
``

| Parameter | Description | Value |
| --- | --- | --- |
| Token Name | The name that you want to assign to the access token | Example: Application Test |
| Grant Type | Choose authorization code as grant_type.It will allow the user to authenticate with the provider | Select authorization code from the drop down menu |
| Callback URL | The client application callback URL | Use the exact Register Callback URL you listed upon application creation |
| Auth URL | The endpoint for Sprinklr’s authorization server.This will help retrieve the auth code | https://api3.sprinklr.com/{env}/oauth/authorize |
| Access Token URL | Refers to Sprinklr’s authentication server to facilitate exchange of the authorization code for an access token | https://api3.sprinklr.com/{env}/oauth/token |
| Client ID | Your API key | The key you receive after  on the developer portal. This can be found in the Sprinklr Development Portal under My Account.Here’s an article that talks about the process of generating a . |
| Client Secret | Your API secret | The secret you receive post key generation.This can be found under MY ACCOUNT section on the dev portal along with the respective key details. |
| Client Authentication | You can select from the following options based on your requirements: Send as Basic Auth HeaderSend Client Credentials in Body | For generating a bearer token, select “Send Client Credentials in Body” from the drop down list |

**Steps to Extract Environment from the UI: **

- Login to the Sprinklr's UI platform
- Right click anywhere on the homepage
- Select `"View Page Source"` from the drop-down menu
- Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.

**Dev Notes:**It is not essential to fill fields such as `scope` and `state`.

### Step 4

Click on “Get New Access Token” button

### Step 5

This action will redirect you to your Sprinklr’s account where you can login using your username and password to authorize.

**Dev Notes:**If you are logging to your Sprinklr’s account for the first time, you will be redirected to reset your password upon first time login.

### Step 6

Once logged in successfully, click on Submit

### Step 7

Choose the combination of partner and client environments that should have access to the token and click on submit.

### Step 8

Wait for Postman to process the request. And. there it is! Your access token is ready for use.

**Dev Notes:**You will be able to create, manage, and use all your tokens from Postman itself. You can manage them by clicking on the `Authorization tab`, selecting `Oauth 2.0` from the drop-down menu, and choosing the token from the drop-down list of `available tokens`.

 [](https://dev.sprinklr.com/oauth-2-0-using-postman)




[Back to top](https://dev.sprinklr.com/oauth-2-0-using-postman)
