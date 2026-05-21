---
title: "Check Control"
slug: check-control
url: https://dev.sprinklr.com/check-control
---

# Check Control

#
POST  Check Control



To check who has the current control of the conversation. The Get Controlling Participant API provides the participant ID of the participant who is having the control of the conversation.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/thread/get-controlling-participant

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Request Parameters
























| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | The entity type on which the action needs to be performed. By default CASE. | String |
| entityId | Required | Case ID of the case. | String |

## Example - Request















Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/thread/get-controlling-participant' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
 "entityType": "CASE",
 "entityId": "{Case ID of the case}"
}'






**Note: **The response can either be the participant ID or Sprinklr.





"data":
     {
     	"controllingParticipantId":"5eb8f0f125984c2cf367f6bb"
     },
"errors":[]
}







## Response Parameters
















| Parameter | Description | Type |
| --- | --- | --- |
| controllingParticipantId | Participant Id of the controlling participant. | String |

	[](https://dev.sprinklr.com/check-control)




[Back to top](https://dev.sprinklr.com/check-control)
