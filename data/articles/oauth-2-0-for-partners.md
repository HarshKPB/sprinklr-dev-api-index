---
title: "OAuth 2.0 for Partners"
slug: oauth-2-0-for-partners
url: https://dev.sprinklr.com/oauth-2-0-for-partners
---

# OAuth 2.0 for Partners

#
 OAuth 2.0 for Partners

If your Sprinklr environment uses SSO (NOTE: the public Sandbox does not use SSO), see the OAuth for SSO Workflow.  An OAuth token is environment specific. A key generated for one environment, cannot be used in another environment.  URL conventions are different for each environment:


- app.sprinklr.com: `https://api3.sprinklr.com/api/v1/{endpoint}`
This is the most common environment and is considered as "Production".

- prod0.sprinklr.com: `https://api3.sprinklr.com/prod0/api/v1/{endpoint}`

- prod2.sprinklr.com: `https://api3.sprinklr.com/prod2/api/v1/{endpoint}`

Authentication is a 2-step process. URL #1 is used to authenticate a key via a browser. URL #2 is used to generate an OAuth token via a POST request.


- https://api3.sprinklr.com/{env}/oauth/authorize?client_id={apikey}&redirect_uri={redirect_uri}&response_type=code&domain_name={SSO Domain Name}

- https://api3.sprinklr.com/{env}/oauth/token?client_id={apikey}&client_secret={secret}&redirect_uri={redirect_uri}&grant_type=authorization_code&code={code}

### Key Terms

- **{env}**: Sprinklr environment like Prod0, prod2, etc. A key generated for one environment, cannot be used in another environment. URL conventions are different for each environment. **No need to enter {env} in case of Production environment, remove {env} from URL**

**Steps to Extract Environment from the UI: **

  - Login to the Sprinklr's UI platform
  - Right click anywhere on the homepage
  - Select `"View Page Source"` from the drop-down menu
  - Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.


- **apikey**: The key you received upon application activation. This can be found in the Sprinklr Development Portal under My Account.

- **secret**: The secret you received upon application activation. This can be found in the Sprinklr Development Portal under My Account.

- **redirect_uri**: The URL you listed upon creation of your application.

- **code**: A code that you will receive upon user authentication. You will need this code to receive the access token.

- **SSO Domain Name**: Your Production Environment URL, found in the following format: example.sprinklr.com.

### Step 1: Request Access to the Sprinklr Account

Direct your client browser to: `https://api3.sprinklr.com/{env}/oauth/authorize?client_id={apikey}&redirect_uri={redirect_uri}&response_type=code&domain_name={SSO Domain Name}` Upon directing your browser, you should see a screen similar to the following:  Click **Submit**

### Step 2: Authenticate the Sprinklr User

Log into Sprinklr with your Sprinklr credentials. If this is the first time that you are logging in, you will need to reset your password.

### Step 3: Choose Environment Access

Choose the combination of partner and client environments that should have access to the token.  Click **Submit**

### Step 4: Access Your Redirect Code

Upon success, you will be redirected to the Redirect URI. This URI includes a returned code that you will need for authorization. **This code is valid for 10 minutes. If you do not successfully complete the following step in 10 minutes, you will need to repeat the API Access Process.** **Example**: *http://www.google.com?code=123456789*

### Step 5: Gaining Authorization

Make a **POST** request using the following URL. You must set Content-Type to "`application/x-www-form-urlencoded`" in the header.  **Example:** `https://api3.sprinklr.com/{env}/oauth/token?client_id={apikey}&client_secret={secret}&redirect_uri={redirect_uri}&grant_type=authorization_code&code={code}`

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

 [](https://dev.sprinklr.com/oauth-2-0-for-partners)




[Back to top](https://dev.sprinklr.com/oauth-2-0-for-partners)
