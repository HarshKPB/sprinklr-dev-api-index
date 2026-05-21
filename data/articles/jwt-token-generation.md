---
title: "JWT Token generation"
slug: jwt-token-generation
url: https://dev.sprinklr.com/jwt-token-generation
---

# JWT Token generation

#
 JWT Certificate Based Token Generation

This documentation walks you through the process of generating an access token using a digital certificate and a private key. It is a certificate-based token generation approach that eliminates the need to store/cache tokens while ensuring secure authentication and information exchange.

## Six Steps to Generate Certificate Based Token

Here are the detailed steps that need to be followed for generating the certificate based access token:

### 1. Generate Key

Generate an environment specific key. Refer to the [Getting Started](https://dev.sprinklr.com/getting-started) guide for the detailed steps.

**Steps to Extract Environment from the UI: **

- Login to the Sprinklr's UI platform
- Right click anywhere on the homepage
- Select `"View Page Source"` from the drop-down menu
- Ctrl+F or Cmd+F `"sentry-environment"` to find where your Sprinklr's instance is hosted.

### 2. Generate Authentication Token

Once you have the key, the next step involves generating an authentication token. Refer to [OAuth 2.0 for Customers](https://dev.sprinklr.com/oauth-2-0-for-customers) guide for the detailed steps.

### 3. Generate X509 Certificate

This step involves generating X509 Certificate, which will provide:

- A `server.key` file to authorize your organization with the auth:jwt:grant command.

- A `server.crt` file to create the connected app required by the JWT bearer flow.

#### How to Generate X509 Certificate?

-

Generate a private key, and store it in a file called server.key. You can delete the server.pass.key file because you no longer need it.

*openssl genrsa -des3 -passout pass:SomePassword -out server.pass.key 2048
openssl rsa -passin pass:SomePassword -in server.pass.key -out server.key*

-

Generate a certificate signing request using the server.key file. Store the certificate signing request in a file called server.csr. Enter information about your company when prompted.

*openssl req -new -key server.key -out server.csr*

-

Generate a self-signed digital certificate from the server.key and server.csr files. Store the certificate in a file called server.crt.

*openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt*

-

Generate the key in .der format from .key(.der key will be used in step 4 Java Code)

*openssl pkcs8 -topk8 -inform PEM -outform DER -in server.key -out server.der -nocrypt*

### 4. Generate JWT Token

This step involves generating a JWT Token that needs to be used as the refresh token in the authentication process.

**Dev Notes: **The generated JWT Token should not be cached/stored by the user in any way. The user should generate this new JWT Token each time to get a new access token.

**Dev Notes: **Must Know Conventions:

- {iss} : `issuer` - App ID (generated using step 5)
- {sub}: `subject` - Sprinklr’s instance login username
- {aud}: `audience` - https://www.sprinklr.com/

### 5. App Registration

This step involves executing an API call for app registration. The API details are mentioned as follows:

## Method Type

**`POST`**

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/app/register


### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/getting-started)



			``



| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| X-API-KEY | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| X509 certificate(server.crt) | Required | This is the digital certification. You upload this file when you create the connected app required by the JWT bearer flow.The JWT token uses a public/private key pair in the form of a X.509 certificate for signing | String |

## Example - Request




  Copy Code



	 curl -X POST \
  https://api3.sprinklr.com/{env}/api/app/register \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
-----BEGIN CERTIFICATE-----
MIIDeDCCAmACCQDSxQ6ZAucMNDANBgkqhkiG9w0BAQsFADB+MQswCQYDVQQGEwJV
UzELMAkGA1UECAwCQ0ExFjAUBgNVBAcMDU1vdW50YWluIFZpZXcxDzANBgNVBAoM
Bkdvb2dsZTERMA8GA1UECwwIM1AgVHJ1c3QxJjAkBgkqhkiG9w0BCQEWFzNwLXRy
dXN0LWVuZ0Bnb29nbGUuY29tMB4XDTIyMDcxMjE5MDMzNVoXDTIzMDcxMjE5MDMz
NVowfjELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkNBMRYwFAYDVQQHDA1Nb3VudGFp
biBWaWV3MQ8wDQYDVQQKDAZHb29nbGUxETAPBgNVBAsMCDNQIFRydXN0MSYwJAYJ
KoZIhvcNAQkBFhczcC10cnVzdC1lbmdAZ29vZ2xlLmNvbTCCASIwDQYJKoZIhvcN
AQEBBQADggEPADCCAQoCggEBAMV3AkcrG2t8WO6gU6hokvIv4wjOhF+Gk/s5MaqK
qMW+JTltwH2HtO2u8Yl9+iYpzx8GnT2EVUPqwe8bO0knW8w1X1zcv7wTrPmheEc2
Zeog00+c9qUBZ/C01Qn5e9gkiwI31/iOBQx8YNyfAynizoO0MxQRyIe2AEnYufn3
NhURzRxTiz8m+fliJa+wEllZErs0eCr6UpspBLdcwN5d+YL9tLOM6pgL0HAaerMI
3c5WrapyORCsdAczhqC+OBqEj+uMZxRFlil9BXxV41jRCAuw9Tj1elhuiFYOZ2aA
t4ZZs/qAKB3JpdyihHN14sLD/GByKysTjE/20spZaexvj3ECAwEAATANBgkqhkiG
9w0BAQsFAAOCAQEAVCWib5EMECvNeqExsqsoAPZ82fJV5k71bHRSBoj+0q9m3NK8
1vfKwLo571gPQKR1sgpRMeCkTMM6ZLw2Yms4Le3thw1CJVLuryBQ6CVYqWATGnQy
9C45iemb8VTqcs3Qq4y13wgJyFvp0vKZLG3dgW4/ZAPJ3HvTABEfNqf8+J7a3TeT
luRI8zNMAM2PU16Bkz9LLJgZktQzAe5qa80lJKIK2GaBjm5HdwkPEhxYtqQS7mfY
y9Hjpky4ne+AReLY73XZ9DqQvzJykDqVTd0C5r/1VkgDMhrcmcgYjT8zZZbWgxcA
QCbOK7Zao8r0l8aJ94V+uyTMX1c9HlzTYRjzGw==
-----END CERTIFICATE-----'





## Example - Response

      

{
"data":"eyJwSWQiOjgwMDAwLCAidElkIjoxNjU4MTI4NTUyMTA2fQ\u003d\u003d",
"Errors": []
}





### ResponseParameters











| Parameter | Description | Type |
| --- | --- | --- |
| App Id | Id associated with the registered app.Used for creating the JWT powered access token and can also be used to update the certificate if required. | String |

**Dev Notes: **App Id is static and thus can be reused when regenerating the access token.

### 6. Generating Certificate-Based Access Token

This step involves executing an API call for certificate-based token generation. The API details are mentioned as follows:

## Method Type

**`POST`**

## API Endpoint

https://api3.sprinklr.com/`{env}`/oauth/apptoken/{appid}

**Dev Notes: **Replace the refresh token with the JWT token in the above API endpoint.

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



| Key | Value | Description |
| --- | --- | --- |
| key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/x-www-form-urlencoded | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Path Parameters












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| appId | The appid you received in the response of the API call made in step 6 | String |  |

### Query Parameters












****

``

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| client_id | Required | The API key you generated using Getting Started guide | String |
| client_secret | Required | The secret you received upon application registration. This can be found in the Sprinklr Development Portal under My Account. | String |
| redirect_uri | Required | The exact Register Callback URL you listed upon creation of your application.Example: https://www.google.com/ | Url |
| grant_type | Required | Set the grant type to:authorization_code | String |
| refresh_token | Required | Use the JWT token generated at your endJSON web tokens consist of three parts — header, payload and signature.The JWT token is separated by dots (.). The syntax looks something like this: xxx.yyyy.zzzzz | String |

## Example - Request




  Copy Code



	 curl -X POST \
  'https://api3.sprinklr.com/{env}/oauth/apptoken/{appid}?client_id={apikey}&client_secret={secret}&redirect_uri={redirect_uri}&grant_type=authorization_code&refresh_token={JWT_token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'





## Example - Response

      

{
"access_token":"{Certificate Based Authentication Token}",
"token_type":"Bearer",
"Expires_in":{expiry time in seconds}
}





### Response Parameters










			```




			``
			``



		``




| Parameter | Description | Type |
| --- | --- | --- |
| {access_token} | The JWT powered access token | String |
| {token_type} | Bearer | String |
| {expires_in} | Token expiry duration in seconds | Epoch |

**Dev Notes: **Once the certificate token is generated using the last step, the token generated using OAuth 2.0 for Customers, will no longer be active/valid.

 [](https://dev.sprinklr.com/jwt-token-generation)




[Back to top](https://dev.sprinklr.com/jwt-token-generation)
