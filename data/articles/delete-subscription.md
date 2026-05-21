---
title: "Delete Subscription"
slug: delete-subscription
url: https://dev.sprinklr.com/delete-subscription
---

# Delete Subscription

#
		Delete Subscription




To delete a Sprinklr Webhook Subscription, you can use this API call.


## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/{subscriptionId}

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


curl -X DELETE \
  https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/{subscriptionId} \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'








  Copy Code



204 No Content





204 No Content if Successful.

[](https://dev.sprinklr.com/delete-subscription)

[Back to top](https://dev.sprinklr.com/delete-subscription)
