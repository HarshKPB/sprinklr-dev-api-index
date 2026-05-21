---
title: "Callback URL Verification Check"
slug: callback-url-verification-check
url: https://dev.sprinklr.com/callback-url-verification-check
---

# Callback URL Verification Check

#
Callback URL Verification Check


You can use this API call to verify the callback URL. For any callback URL to work within webhook subscription this API call with empty payload must return either of the one from **2XX(0-4)** response. Here the API Endpoint will be the callback URL that you want to use within Sprinklr webhook subscription.

## API Endpoint

https://{Callback Url}

## Header

The following set of HTTP header fields provide required information about the request or response, or about the object sent in the message body. Both request headers and response headers can be controlled using these endpoints.











			``




| Key | Value | Description |
| --- | --- | --- |
| Content-Type | application/json | Request format should be JSON as the endpoint expects a JSON body. |

## Sample




  Copy Code



	curl -X POST \
  https://{Callback Url} \
  -H 'Content-Type: application/json' \
  -d '{}'








  Copy Code



200 OK



## Sample




  Copy Code



curl --location --request POST 'https://webhook.site/5b2dab1d-e65b-4a53-b480-c025145df095' --header 'Content-Type: application/json' --data-raw '{}'








  Copy Code



200 OK



[](https://dev.sprinklr.com/callback-url-verification-check)

[Back to top](https://dev.sprinklr.com/callback-url-verification-check)
