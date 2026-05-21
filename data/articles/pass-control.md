---
title: "Pass Control"
slug: pass-control
url: https://dev.sprinklr.com/pass-control
---

# Pass Control

#
POST  Pass Control



The API is used to pass control of a conversation between Chatbots and from Chatbot to Sprinklr and vice-versa, depending on the business use-case.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/thread/pass-control

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
| entityId | Required | The Id of the entity type. Case ID of the case. | String |
| participantId | Required | The ID of the participant to whom you want to pass the control can either be Participant unique ID or Sprinklr. | String |

## Example-Request















Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/thread/pass-control' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
 "entityType": "CASE",
 "entityId": "{Case ID of the case}",
 "participantId": "{Participant ID or Sprinklr}",
}'






**Request Sample to Pass the control to a Participating Chatbot:**





{
 "entityType": "CASE",
 "entityId": "5ebead2e231b094eb1cefcfd",
 "participantId": "5ebeae6ed02aeb736f07a3ac"
}






**Request Sample to Pass the control to Sprinklr:**





{
 "entityType": "CASE",
 "entityId": "5ebead2e231b094eb1cefcfd",
 "participantId": "Sprinklr"
}






## Example-Response





"data":
     {
     	"controllingParticipantId":"5eb8f0f125984c2cf367f6bb"
     },
"errors":[]
}







## Response Definition
















| Parameter | Description | Type |
| --- | --- | --- |
| controllingParticipantId | Participant Id of the controlling participant. | String |

	[](https://dev.sprinklr.com/pass-control)




[Back to top](https://dev.sprinklr.com/pass-control)
