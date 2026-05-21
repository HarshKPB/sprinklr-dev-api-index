---
title: "Update Subscription"
slug: update-subscription
url: https://dev.sprinklr.com/update-subscription
---

# Update Subscription

#
Update Subscription


You can update a Webhook Subscription in the Sprinklr UI via this API call and you will get the response based on update.

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

### Request Payload

Add a Request Body in PUT request. In the body, enter a raw request with the format type as JSON since we have to send the correct format according to the server. This endpoint expects a JSON body which contains the details of the Create Webhook endpoint. **Request Parameters**










































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| subscriptionId | Required | The webhook subscriptionId. | String |
| name | Optional | The name of the webhook subscription. | String |
| description | Optional | The description of the webhook subscription. | String |
| addSubscriptions | Optional | To add subscriptions. | Array |
| removeSubscriptions | Optional | To remove subscriptions. | Array |

## Example




  Copy Code



	curl -X PUT \
  https://api2.sprinklr.com/{env}/api/v2/webhook-subscriptions/{subscriptionId}/ \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Cache-Control: no-cache' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
   "name":"string",
   "description":"string",
   "addSubscriptions":[
   ],
   "removeSubscriptions":[
   ]
}








  Copy Code



{
   "id":"string",
   "name":"string",
   "description":"string",
   "subscriptions":[
      "string"
   ],
   "url":"string",
   "preSharedKey":"string",
   "verified":false,
   "active":false,
   "lastSuccessTimestamp":0,
   "lastFailedTimestamp":0
}



## Response Definitions:





| Response | Description | Type |
| --- | --- | --- |
| Id | The {Id} is associated with the subscription you have created via an API call or in the Sprinklr UI. | String |
| name | Name of the Webhook Subscription. | String |
| description | Description of the subscription. | String |
| subscriptions | Data related to subscription type and attributes. | String |
| url | The URL of the webhook endpoint. | String |
| preSharedKey | An authorization key that can be used to confirm if the request is valid. A valid webhook will have a header 'X-Hub-Signature' with value 'sha256={sha256 digested payload using the preSharedKey}'. | String |
| verified | If True, verified. | Boolean |
| active | If True, the webhook subscription is active. | Boolean |
| lastSuccessTimestamp | Last success timestamp of the webhook | Integer |
| lastFailedTimestamp | Last failed timestamp of the webhook. | Integer |

[](https://dev.sprinklr.com/update-subscription)

[Back to top](https://dev.sprinklr.com/update-subscription)
