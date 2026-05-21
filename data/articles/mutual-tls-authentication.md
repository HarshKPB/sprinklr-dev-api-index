---
title: "Mutual TLS Authentication"
slug: mutual-tls-authentication
url: https://dev.sprinklr.com/mutual-tls-authentication
---

# Mutual TLS Authentication

# Mutual TLS Authentication in Sprinklr API

Sprinklr APIs support Mutual TLS (mTLS) Authentication as an additional layer of security for client-server communication. In mTLS, both the client and the server authenticate each other using their respective TLS certificates, offering enhanced protection against unauthorized access.

## Uploading an mTLS Certificate for Sprinklr APIs

To use Mutual TLS (mTLS) authentication with Sprinklr APIs, follow these steps:



- **Contact Sprinklr Support:** mTLS authentication is not enabled by default. To enable it, contact the Sprinklr team and request activation for your account.

- **Submit Certificate Details:** Provide your mTLS certificate details according to the guidelines shared by Sprinklr. The Sprinklr ITOps team will upload the certificate on your behalf.

- **Wait for Confirmation:** Once the configuration is complete, you’ll receive confirmation that mTLS authentication has been enabled for your account.


After mTLS is enabled, proceed with the steps outlined in the next section to complete the setup.


## Enabling mTLS for an Existing App in the Sprinklr Developer Portal



Follow these steps to enable mTLS authentication for an existing application in the Sprinklr Developer Portal:



- Sign in to your account at [dev.sprinklr.com](https://dev.sprinklr.com).

- In the upper-right corner, select your email address, and then choose **Apps** from the dropdown menu.

- On the **My Apps** screen, select the application for which you want to enable mTLS authentication.

- Scroll down to the **Enhanced Security with Mutual TLS** section and select the **Enable Mutual TLS Authentication** checkbox.

- Click the **Save** button to apply your changes.


Your application is now configured to use mTLS authentication for enhanced security.


Once mTLS authentication is enabled for an application, the app’s display name will include the suffix **“--MTLS”**. If mTLS is later disabled, the suffix will be removed automatically.

**Dev Notes: **If you enable this option without uploading a valid mTLS certificate, all API calls will fail due to failed client authentication.
