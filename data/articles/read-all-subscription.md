---
title: "Read All Subscription"
slug: read-all-subscription
url: https://dev.sprinklr.com/read-all-subscription
---

# Read All Subscription

#
	Read All Subscription


You can fetch all the subscription with respect to api-key and access token with this API call. In response, you will get all the webhook subscription data in JSON format.

## API Endpoint

 https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions

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
| subscriptionId | X | The Sprinklr webhook subscriptionid. | String |

## Example




  Copy Code



	curl -X GET \
  https://api2.sprinklr.com/{env}/api/v2/webhook-subscriptions \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'








  Copy Code



{
   "data":[
      {
         "id":"5cc678eae4b07983eaadfc46",
         "name":"Test webhook",
         "subscriptions":[
            "AUDIENCE_ACTIVITY"
         ],
         "url":"https://webhook.site/11b95a99-3375-4cbc-901a-4fb3e45cd7ac",
         "verified":false,
         "active":false
      },
      {
         "id":"5cc6b8dfe4b004c368e911eb",
         "name":"draft webhooks",
         "subscriptions":[
            "DRAFT_CREATED",
            "DRAFT_UPDATED",
            "DRAFT_SCHEDULED",
            "MESSAGE_PUBLISHED",
            "CASE_CREATED"
         ],
         "url":"https://webhook.site/d94b3f35-ce4c-4257-8a88-7fe73f26420f",
         "verified":false,
         "active":false
      },
      {
         "id":"5cd43e26e4b09b9858623a5d",
         "name":"NEW WEB",
         "subscriptions":[
            "MESSAGE_CREATED"
         ],
         "url":"google.com",
         "verified":false,
         "active":false
      },
      {
         "id":"5cffac43e4b02835b8a101d7",
         "name":"webhook case",
         "description":"case webhook ",
         "subscriptions":[
            "CASE_CREATED"
         ],
         "url":"https://webhook.site/b6911c27-9c7f-488f-9ace-b7b014f255d1",
         "verified":true,
         "active":false
      },
      {
         "id":"5d024bc0e4b05cd2f9d2e77e",
         "name":"L3 Webhook Check",
         "subscriptions":[
            "MESSAGE_CREATED"
         ],
         "url":"https://webhook.site/f7880fc2-6fb6-48ca-b3fb-7f8114260410",
         "verified":true,
         "active":false
      },
      {
         "id":"5d19adf8e4b0d7d1f4942189",
         "name":"testing webhook",
         "subscriptions":[
            "DRAFT_CREATED"
         ],
         "url":"https://webhook.site/4f2d4a0c-3028-48d7-a86d-cfa8740582a5",
         "verified":true,
         "active":false
      },
      {
         "id":"5d2c8d5de4b059de8737bdd4",
         "name":"Campaign Sachit",
         "subscriptions":[
            "CAMPAIGN_UPDATED"
         ],
         "url":"http://webhook.site/d0678105-5337-491f-9cf2-da664679245a",
         "verified":true,
         "active":false
      },
      {
         "id":"5d314710e4b0872c6916abc7",
         "name":"SAM Asset Create Webhook",
         "subscriptions":[
            "DIGITAL_ASSET_CREATED"
         ],
         "url":"https://www.webhook.site/8973b596-c624-46be-a50f-68852686020a",
         "verified":true,
         "active":false
      },
      {
         "id":"5d3148f7e4b0872c691715ba",
         "name":"SAM Asset Update Webhook",
         "subscriptions":[
            "DIGITAL_ASSET_UPDATED"
         ],
         "url":"https://www.webhook.site/89036596-c624-46be-a50f-68859686020a",
         "verified":true,
         "active":false
      },
      {
         "id":"5d314960e4b0872c69172d4a",
         "name":"SAM Asset Delete Webhook",
         "subscriptions":[
            "DIGITAL_ASSET_DELETED"
         ],
         "url":"https://www.webhook.site/8903b596-c924-46be-a50f-6885f986020a",
         "verified":true,
         "active":false
      }
   ],
   "errors":[
   ]
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


	[](https://dev.sprinklr.com/read-all-subscription)

[Back to top](https://dev.sprinklr.com/read-all-subscription)
