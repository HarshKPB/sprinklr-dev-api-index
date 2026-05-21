---
title: "External Authentication Credential APIs"
slug: external-authentication-credential-apis
url: https://dev.sprinklr.com/external-authentication-credential-apis
---

# External Authentication Credential APIs

# External Authentication Credential APIs

The External Authentication Credential APIs allow you to seamlessly create and delete external API credentials within Sprinklr, enabling secure integrations with third-party applications.
























































| Authentication Name | AuthType Value | Description |
| --- | --- | --- |
| Basic Auth | STD_BASIC_AUTH | Username and password based authentication, encoded in Base64 and passed in the Authorization header. |
| OAUTH 2.0 ROPC | BASIC | OAuth 2.0 Resource Owner Password Credentials flow that uses a Base64-encoded username and password as a Basic Auth header to obtain an access token from the Token URL. |
| OAuth Refresh Token | OAUTH_REFRESH | OAuth 2.0 authentication using a Client ID, Client Secret, Token URL, and Refresh Token to generate a new access token. |
| Password Auth | OAUTH_PASSWORD | OAuth 2.0 authorization using the 'password' grant type with a username and password to generate an access token from the Token URL. |
| Client Credential Auth | OAUTH_TOKEN | OAuth 2.0 authorization using the 'client_credentials' grant type with a Client ID and Client Secret to obtain an access token from the Token URL. |
| OAuth 1.0 | OAUTH_1 | Authentication where each request is securely signed with a shared secret and token credentials. |
| JWT Auth | JWT | Authentication using a digitally signed JSON Web Token (JWT) to verify identity and grant API access. |
| Custom Auth | CUSTOM_AUTH | A custom authentication mechanism tailored to the specific needs of the application. |
| API Key | API_KEY | Uses an API Key and Password to authorize access. |

### Key Highlights

	**Broad Authentication Suport**

Sprinklr supports all authentication types, ensuring compatibility with various external systems.
Supported AuthTypes ` [OAUTH_TOKEN, OAUTH_PASSWORD, CUSTOM_AUTH, JWT, OAUTH_1, API_KEY, BASIC, OAUTH_REFRESH, STD_BASIC_AUTH]`

**Static Authentication Note**

For static authentication (key-based), there’s no need to add external authentication credentials in Sprinklr.

	**	Access Control**


- Only Global Admins and Global Users can add external APIs in Sprinklr.

- To grant users permission to manage external authentication credentials, administrators can:


- Create a custom role with the required permissions.

- Assign the role to the appropriate user or user group.

**Related Knowledge Base Article:** ** [Add an External Authentication Credential in Sprinklr](https://www.sprinklr.com/help/articles/configure-an-extension-in-sprinklr/add-an-external-authentication-credential-in-sprinklr/633c5ca9a0522e093b06c1c6)**
