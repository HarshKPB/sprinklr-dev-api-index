---
title: "Getting Started"
slug: getting-started
url: https://dev.sprinklr.com/getting-started
---

# Getting Started

#
Getting Started


This guide walks you through the process for registering an application, i.e., generating the API key and the corresponding authentication token for accessing Sprinklr APIs. Once you have the access to the API key and the authentication token, you can make API calls by referring to the respective documentation on the developer portal.

**Dev Notes: **Starting with the 26.1 release, it is recommended to use the Developer Tools built into the Sprinklr platform to create Developer Apps and to generate API Key and Secret.
Refer to the [Developer Tools in Sprinklr documentation](https://www.sprinklr.com/help/articles/developer-tools/developer-tools-in-sprinklr/692e8b39f0afa271d18a5929) for detailed steps and requirements.

To begin with, here's the step-by-step process to make your first API call:



- Generate an API Key

- Generate an Access Token

- Make your first API call

- Example - Making a Bootstrap Call



**Dev Notes: **

- It is prequisite to generate the API key and authentication token before you make any API call. The generated key and token should be provided in the header section or else you will receive 401 unauthorized (developer inactive) error.
- The login for Sprinklr's platform is different from developer portal's. However, you would be needing login credentials to both the platforms for generating the key and token.
- Access to Developer Portal is needed to register the application (generate API key).
- Access to Sprinklr Platform is needed to gain authorization and generate bearer token.
- The generated key and token will work for Sandbox environments as well
- Ensure that the right workspaces are given access while authorizing. You can only fetch data from the workspaces to which the token has been given access to

##  Generate an API Key



**Dev Notes: **We recommend you register on the developer portal using a service account email to ensure the account isn't tied to an individual user. This ensures you have access to Developer Portal and the associated keys even if an individual isn't part of the organization anymore. Please note that you should have access to the service email account, as you will receive all the developer portal confirmation emails there.


### Step 1:


Register for an account at [dev.sprinklr.com](https://dev.sprinklr.com/developer-portal-registration). You will receive an email confirmation upon successful registration.


  **Note: **

   If you do not receive the confirmation message within a few minutes of signing up, please check your Spam folder just in case the confirmation email got delivered there instead of your inbox. If so, select the confirmation message and click "Not Spam", which will allow future messages to get through.

  If it's not present in the Spam folder as well then please check with your IT team/mail admins to see if they have any rule to reject emails sent via AWS SES service. You might additionally have to whitelist AWS SES service to send you emails on behalf of api@psprinklr.com. 


### Step2:


Once you’ve registered using the developer portal, you can create your own application and API key.


### Step3:


Fill the Register an Application and Select which Web APIs this application will use.

Don’t forget to enter the correct “Register Callback URL”. Once you fill the application details click Register Application at the bottom of the page. All the Web APIs Key and Secret will automatically be created.



**Dev Notes: **The Register Callback URL is the redirect_uri that tells the authorization server where to send the user back after the successful account authorization. This must be a publicly available safe URL as when you get redirected you will receive the authorization code in the URL.
 You can also use `https://www.google.com/`



**Steps to Extract Environment from the UI: **

- Login to the Sprinklr's UI platform
- Right click anywhere on the homepage
- Select `"View Page Source"` from the drop-down menu
- Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.



## Generate Access Token for Sprinklr APIs


**Pre-requisite**: You must have access to a user account on Sprinklr platform before you will be able to proceed.After getting the API KEY, you need to run the following OAuth process to generate the access token. An OAuth token is environment specific. A key generated for one environment, cannot be used in another environment.


URL conventions are different for each environment:



- app.sprinklr.com: `https://api3.sprinklr.com/api/v1/{endpoint}`

    This is the most common environment and is considered as "Production".

- prod0.sprinklr.com: `https://api3.sprinklr.com/prod0/api/v1/{endpoint}`

- prod2.sprinklr.com: `https://api3.sprinklr.com/prod2/api/v1/{endpoint}
`


**Access token generation is a 2-step process**


URL #1 is used to authenticate a key via a browser. URL #2 is used to generate an OAuth token via a POST request.



- https://api3.sprinklr.com/**{env}**/oauth/authorize?client_id=**{apikey}**&response_type=code&redirect_uri=**{redirect_uri}**

- https://api3.sprinklr.com/**{env}**/oauth/token?client_id=**{apikey}**&client_secret=**{secret}**&redirect_uri=**{redirect_uri}**&grant_type=authorization_code&code=**{code}**



### Path Parameters:



- **{env}**:  Sprinklr environment like Prod0, prod2, etc. A key generated for one environment, cannot be used in another environment. URL conventions are different for each environment. **No need to enter {env} in case of Production environment, remove {env} from URL**.

- **{apikey}**: The key you get after registering your application on developer portal. This can be found in the Sprinklr Development Portal under My Account. 

- **{secret}**: The secret you received upon application activation. This can be found in the Sprinklr Development Portal under My Account.

- **{redirect_uri}**: The URL you listed upon creation of your application.

- **{code}**: A code that you will receive upon user authentication. You will need this code to receive the access token.


For more information, visit the [OAuth for customers](https://dev.sprinklr.com/oauth-2-0-for-customers) page.


### Step 1: Request Access to the Sprinklr Account


Direct your client browser to: `https://api3.sprinklr.com/{env}/oauth/authorize?client_id={apikey}&response_type=code&redirect_uri={redirect_uri}` Upon directing your browser, you should see a screen similar to the following:

  Click Submit.



### Step 2: Authenticate the Sprinklr User


Log into Sprinklr with your Sprinklr credentials. If this is the first time that you are logging in, you will need to reset your password.



### Step 3: Choose Environment Access


Choose the combination of partner and client environments that should have access to the token.


Click Submit.



### Step 4: Access Your Redirect Code


Upon success, you will be redirected to the Redirect URI. This URI includes a returned code ( in the URL itself ) that you will need for authorization. **This code is valid for 10 minutes. If you do not successfully complete the following step in 10 minutes, you will need to repeat the API Access Process.** **Example**: *https://www.google.com/?code=62cbdbcd25968d7e2dce55gb

  *





### Step 5: Gaining Authorization


Make a **POST** request using the following URL. You must set Content-Type to "`application/x-www-form-urlencoded`" in the header.
	**Example:** `https://api3.sprinklr.com/{env}/oauth/token?client_id={apikey}&client_secret={secret}&redirect_uri={redirect_uri}&grant_type=authorization_code&code={code}`


### Response


**The response is returned in JSON.**











        ``




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


**Note**: The tokens will remain valid as long as the authenticated user's password in Sprinklr is valid. If the password changes, you may refresh the token to receive a new access_token.


## Make your first API call


Make a **GET** request to the following endpoint:




#### Request




```
curl -X GET \
    'https://api3.sprinklr.com/{env}/api/v2/me' \
    -H 'Authorization: Bearer {token}' \
    -H 'cache-control: no-cache' \
    -H 'key: {apikey}'

```




### The following information will be displayed as a JSON result:




#### Response




```

  {
    "data": {
        "name": "Shivangi Singh",
        "customerId": 66000000,
        "id": 66014640,
        "type": "PARTNER_ADMIN",
        "email": "shivangi.singh@sprinklr.com",
        "properties": {
            "_c_65b8a60cb6c96a319161e7c6": [
                "No"
            ],
            "_c_650c385a2b5a8629918ace0b": [
                "DEFAULT VALUE - ENGLISH"
            ],
        },
        "workspaceId": 66000002
    },
    "errors": []
}


```




Congratulations, you have successfully made an API call to retrieve data in from the Sprinklr platform!

 [](https://dev.sprinklr.com/getting-started)

[Back to top](https://dev.sprinklr.com/getting-started)
