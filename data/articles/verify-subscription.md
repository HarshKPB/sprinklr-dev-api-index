---
title: "Verify Subscription"
slug: verify-subscription
url: https://dev.sprinklr.com/verify-subscription
---

# Verify Subscription

#
		Verify Subscription




A Sprinklr Webhook Subscription can be verified with this API call. You will get a response based on a subscription after making the Request.


## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/{subscriptionId}/verify

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

## Example




  Copy Code


curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/{subscriptionId}/verify \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'








  Copy Code


{
   "data": true,
   "errors": []
}





True if verfied, otherwise False.

[](https://dev.sprinklr.com/verify-subscription)

[Back to top](https://dev.sprinklr.com/verify-subscription)
