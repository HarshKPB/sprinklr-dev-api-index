---
title: "Create Subscription"
slug: create-subscription
url: https://dev.sprinklr.com/create-subscription
---

# Create Subscription

#
		 Create Subscription




You can create a Webhook Subscription in the Sprinklr UI via this API call and you will get the Subscription {Id} as Response after making the Request. Make a POST request and in the Body, enter a raw request with the JSON format, as the endpoint expects a JSON body which contains the details of the keys and values required in Create Webhook Subscription.

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

### Request Payload

Add a Request Body in POST request. In the body, enter a raw request with the format type as JSON since we have to send the correct format according to the server. This endpoint expects a JSON body which contains the details of the Create Webhook endpoint.

### Request Parameters








































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | X | The name of the webhook subscription. | String |
| description | X | The description of the webhook subscription. | String |
| subscriptions | X | The list of webhook types on which you want to create subscription. | Array |
| url | X | The URL of the webhook endpoint. | String |
| preSharedKey | X | An authorization key that can be used to confirm if the request is valid. A valid webhook will have a header 'X-Hub-Signature' with value 'sha256={sha256 digested payload using the preSharedKey}'. | String |

## Example-Request




  Copy Code


curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/ \
  -H 'Authorization: {{Enter your Access Token}}' \
  -H 'Key: {{Enter your API KEY}}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
   "name":"case create webhook",
   "description":"Webhook for case creation events",
   "subscriptions":[
        "CASE_CREATED"
   ],
   "url":"https://sprinklr.com/",
   "preSharedKey":"string"
}'





## Example-Response




  Copy Code


{
   "data":{
      "id":"string",
      "name":"case create webhook",
      "description":"Webhook for case creation events",
      "subscriptions":[
         "CASE_CREATED"
      ],
      "url":"https://cosmos.net/",
      "preSharedKey":"string",
      "verified":false,
      "active":false,
      "lastSuccessTimestamp":0,
      "lastFailedTimestamp":0
   }
}





## Sample - Create Multiple Subscription




  Copy Code


curl -X POST \
  https://api3.sprinklr.com/{{env}}/api/v2/webhook-subscriptions/ \
  -H 'Authorization: {{Enter your Access Token}}' \
  -H 'Key: {{Enter your API KEY}}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
   "name":"case create webhook",
   "description":"Webhook for case creation events",
   "subscriptions":[
        "CASE_CREATED","MESSAGE_CREATED"
   ],
   "url":"https://sprinklr.com/",
   "preSharedKey":"937565859393027346487dndjdjdbdbdk"
}'





## Sample - Create Subscription With Filters




  Copy Code


curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/ \
  -H 'Authorization: {{Enter your Access Token}}' \
  -H 'Key: {{Enter your API KEY}}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
   "name":"API test",
   "description":"Webhook for case creation.",
   "subscriptions":[
        "CASE_CREATED"
   ],
   "filteredSubscriptions":[
       {
        "webhookType": "CASE_CREATED",
        "filters":[
             {
                    "id": "ACCOUNT_TYPE",
                    "type": "ACCOUNT_TYPE",
                    "checkCondition": "IS",
                    "values": [
                         "Whatsapp_Business"
                    ]
                }
        ]
       }
   ],
   "url":"https://sprinklr.com/",
   "preSharedKey":"string"
}'





### Sample Response




  Copy Code


{
   {
    "data": {
        "id": "625d7548216b7f6f8abee3f4",
        "name": "AAAAAAAA12112",
        "description": "Webhook for case creation events",
        "subscriptions": [
            "CASE_CREATED"
        ],
        "filteredSubscriptions": [
            {
                "webhookType": "CASE_CREATED",
                "filters": [
                    {
                        "id": "ACCOUNT_TYPE",
                        "type": "ACCOUNT_TYPE",
                        "checkCondition": "IS",
                        "values": [
                            "Whatsapp_Business"
                        ]
                    }
                ]
            }
        ],
        "url": "https://sprinklr.com/",
        "preSharedKey": "string",
        "verified": false,
        "active": false
    },
    "errors": []
}





## Response Definitions:





























































| Response | Description | Type |
| --- | --- | --- |
| id | The {Id} is associated with the subscription you have created via an API call or in the Sprinklr UI. | String |
| name | Name of the Webhook Subscription. | String |
| description | Description of the subscription. | String |
| subscriptions | Data related to subscription type and attributes. | String |
| url | The URL of the webhook endpoint. | String |
| preSharedKey | An authorization key that can be used to confirm if the request is valid. A valid webhook will have a header 'X-Hub-Signature' with value 'sha256={sha256 digested payload using the preSharedKey}'. | String |
| verified | If True, verified. | Boolean |
| active | If True, the webhook subscription is active. | Boolean |
| lastSuccessTimestamp | Last success timestamp of the webhook | Integer |
| lastFailedTimestamp | Last failed timestamp of the webhook. | Integer |

[](https://dev.sprinklr.com/create-subscription)




[Back to top](https://dev.sprinklr.com/create-subscription)
