---
title: "API Key and Secret Generation"
slug: api-key-and-secret-generation
url: https://dev.sprinklr.com/api-key-and-secret-generation
---

# API Key and Secret Generation

# API Key and Secret Generation

This guide walks you through the steps required to generate an API Key (Client_Id) and API secret (Client_secret). Once the API key is generated, you can proceed with the token generation process.

	**Dev Notes:**

- The API key and secret do not expire. These remain static and can only be deleted or disabled from customer's Sprinklr developer account.

- The secret is a masked entity and will only be visible once you verify from the confirmation email sent to the developer portal registered email address.

### Step 1

Register for an account at [dev.sprinklr.com](https://dev.sprinklr.com/create). You will receive an email confirmation upon successful registration. Once confirmed, you can login to the Sprinklr developer portal.

Reference Article: [Register on Developer Portal](https://dev.sprinklr.com/developer-portal-registration)

### Step 2

Once registered and logged in, click on your email address appearing at the top right corner and select "Apps" from the drop down menu.

### Step 3

	Click on `"+ New App"` button to create a new application (key & secret generation).

### Step 4

Fill the Register Application form. The form field definitions are as follows:






























****

-
-
-







| Field Name | Required/Optional | Description |
| --- | --- | --- |
| App Name | Required | Refers to the name of your application. It is recommended to name your application based on the use case you will be using it for. 			You can also tie the name of your application with the environment you'll be using it for, for example, Sandbox or Production. |
| Description | Optional | Refers to the use case your application is trying to solve. This helps identify the objective of the application when monitoring usage in future. |
| Owner | Required | Refers to the email address of the user, the app will be registered against. This is auto-populated with the signed in email address. |
| APIs | Required | Refers to the environment you want to create the API key and secret for. 		Notes: 		 			Sprinklr is hosted across environments such as Prod, Prod2, Prod3, Prod5, Prod8, and so on. 			Refer to the steps below for extracting your environment. 			The environment for Sandbox and Production would be the same. The authorization token will be the unique identifier to validate whether the token belongs to Sandbox or Production. |
| Callback URL | Required | The URL must be a valid, publicly accessible URI; otherwise, the authorization call will return an error. For example, if you are entering Sprinklr’s web URL, it should be https://www.sprinklr.com. |

	**Steps to Extract Environment from the UI:**


- Log in to the Sprinklr UI platform.

- Right click anywhere on the homepage.

- Select `"View Page Source"` from the drop-down menu.

- Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr instance is hosted.




### Step 5

Click on the `"Save"` button and you will gain access to your app key and secret.
[](https://dev.sprinklr.com/api-key-and-secret-generation)

[Back to top](https://dev.sprinklr.com/api-key-and-secret-generation)
