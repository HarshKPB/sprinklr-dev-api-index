---
title: "Activate Subscription"
slug: activate-subscription
url: https://dev.sprinklr.com/activate-subscription
---

# Activate Subscription

#
		Activate Subscription

A Sprinklr Webhook Subscription can be activated with this API call. You will get the response after making the Request.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/{subscriptionId}/activate

## Header

The following set of HTTP header fields provide required information about the request or response, or about the object sent in the message body. Both request headers and response headers can be controlled using these endpoints.











			``




			``




			``




| Key | Value | Description |
| --- | --- | --- |
| Content-Type | application/json | Request format should be JSON as the endpoint expects a JSON body. |
| Authorization | Bearer {{token}} | Credential used by an application to access an API. |
| Key | api-key | The API key acts as both a unique identifier and a secret token for authentication to a set of access rights. |

### Request Parameters















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| subscriptionId | Required | The webhook subscriptionId. | String |

## Example API Request




  Copy Code


curl -X POST \
   https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/{subscriptionId}/activate \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example API Response




  Copy Code


{
    "data": true,
    "errors": []
}





True if verfied, otherwise False.

[](https://dev.sprinklr.com/activate-subscription)

[Back to top](https://dev.sprinklr.com/activate-subscription)
