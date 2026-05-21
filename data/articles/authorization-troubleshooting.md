---
title: "Authorization Troubleshooting"
slug: authorization-troubleshooting
url: https://dev.sprinklr.com/authorization-troubleshooting
---

# Authorization Troubleshooting

#
Authorization Troubleshooting Guide

Authorization is imperative for accessing Sprinklr APIs. There are three standard methods for generating the access token, namely:


#### 1. [OAuth 2.0 for Customers](https://dev.sprinklr.com/oauth-2-0-for-customers)

This is the standard method for generating the Authentication token. OAuth 2.0 for Customers requires generating a temporary code in exchange for an authentication token. The customer needs to log in to their Sprinklr’s instance every time a code needs to be generated for authentication.

####  2. [Client Credentials Grant Type](https://dev.sprinklr.com/client-credentials-get)

This method requires setting up a default user prior to making the token generation API call. Once the default user is set up, you can make the API call for generating the token where all the parameters are static such as API key, secret, and grant type.

**Dev Note: **Setting up a default user will be a one-time process and will be done once you raise a ticket with the Integrations support team.

#### 3. [JWT Certificate-Based Token Generation](https://dev.sprinklr.com/jwt-token-generation)

The certificate-based token generation approach eliminates the need to store/cache tokens while ensuring secure authentication and information exchange. JWT Certificate based tokens are more secure as it uses a public/private key pair in the form of an X.509 certificate for signing and eliminates the need to store/cache tokens

## Troubleshooting Common Authorization Errors

This section covers common authorization issues and their corresponding fixes:

### 1. Why Do I get Internal Server Error and How to Fix It?


**Cause**:

- The redirect URI that you configured in the code generation URL is probably incorrect.

**Code Generation Url:**
https://api3.sprinklr.com/`{env}`/oauth/authorize?client_id=`{apikey}`&response_type=code&redirect_uri=`{redirect_uri}`

**Fix**:

- The redirect URI is a publicly accessible URL that you configure while creating an application on the [developer portal](https://dev.sprinklr.com/). The redirect URI in the code generation URL should be an exact match of the “Register Callback URL.”

- You can check the redirect URI by logging into Developer Portal and redirecting to `Apps` -> `Open App` -> `Update "Callback URL"`

### 2. Why do I Get 421 Misdirected Request and How to Fix It?

**Causes**:

- The configured environment (prod, prod0, prod2, prod3, prod4, prod8, prod12, prod15) is wrongly configured in the code generation URL

- The dynamic values are configured within curly brackets {} within the code generation URL

**Code Generation Url:**
https://api3.sprinklr.com/`{env}`/oauth/authorize?client_id=`{apikey}`&response_type=code&redirect_uri=`{redirect_uri}`

**Fix:**

- Please check the environment for your Sprinklr instance using the steps mentioned below. Kindly note that you can skip the environment configuration if the setup exists in the Production environment.

- **{env}**:  Sprinklr environment like Prod0, prod2, etc. A key generated for one environment, cannot be used in another environment. URL conventions are different for each environment. **No need to enter {env} in case of Production environment, remove {env} from URL**.

**Steps to Extract Environment from the UI: **

  - Login to the Sprinklr's UI platform
  - Right click anywhere on the homepage
  - Select `"View Page Source"` from the drop-down menu
  - Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.

- Kindly remove curly brackets while configuring the environment, clientId, and redirect URI. The right format would be as follows:

**Code Generation Url:**
https://api3.sprinklr.com/`{env}`/oauth/authorize?client_id=`dc2eekzzhyhdhnbq8u9np26w`&response_type=code&redirect_uri=`https://www.sprinklr.com/`

### 3. What Does Developer Inactive Error Imply and How to Fix It?

**Cause**:

- The client_Id (API key) configured in the code generation URL is either incorrect or doesn't correspond to the right environment

**Code Generation Url:**
https://api3.sprinklr.com/`{env}`/oauth/authorize?client_id=`{apikey}`&response_type=code&redirect_uri=`{redirect_uri}`

**Fix**:

- Check the API key bundle to which the key is added. This key should fall under the environment that is assigned to your Sprinklr instance. Check the box against the right environment

- Check the API key from the “[Your Account](https://dev.sprinklr.com/my-apps)” section on the dev portal. This should be configured wherever the client_id parameter is mentioned.

## Authorization FAQs

### 1. Why Do I Receive the “Code has Expired” Error when I try Generating a Token Using API?

The code you generate using the first step mentioned on Oauth 2.0 for Customers is only valid for 10 minutes. If you are unable to complete the second step within those ten minutes, you’ll receive 400 Bad request error indicating that the code has expired.

### 2. What is the Validity of Different Parameters Used in the Authorization Process?

- **Code**: Expires in 10 minutes

- **Key**: Doesn’t have an expiry. Can only be deleted or disabled

- **Authorization Token**: Valid for 30 days by default. You will need to regenerate or refresh the token once it expires. If required, the validity can be increased by approval from your Success Manager

### 3. Is Any Platform Permission Required for Generating Access Tokens?

Yes, the user generating the access token should have “Generate API Token” permission enabled from within the Sprinklr platform. For more details, refer to this [Add Roles](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658#_9c0baa46-86c5-40df-bbb3-72fa7778ad29) article.

### 5. What do I need to Do for Setting up Client Credentials Grant Type?

You can reach out to our support team for setting up a default user. Setting up a default User is a one-time process. Once the setup is complete, you can make the API call mentioned in the documentation for generating the token.

Please provide the following details at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

- **Client_Id (API Key)**: The API key that you generated using [Getting Started Guide](https://dev.sprinklr.com/getting-started)

- **Sprinklr Platform Email Address**: The platform user email address you want to associate the token to

### 6. What is a Service Email and Why Does Sprinklr Recommend Using It?

A service email is an email account that is shared and accessible by multiple users at the same time. Sprinklr recommends using service email while generating the access token for the following reasons:

- Registered dev portal account will not be linked to an individual user

- The API token will not be linked to an individual’s account

- Disabling/Deleting a user might affect the API workflow, which gets eliminated if you have a service email Sprinklr account

 [](https://dev.sprinklr.com/authorization-troubleshooting)




[Back to top](https://dev.sprinklr.com/authorization-troubleshooting)
