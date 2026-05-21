---
title: "Delete Participant"
slug: delete-participant
url: https://dev.sprinklr.com/delete-participant
---

# Delete Participant

#
  DELETE Delete Participant



Using this API, you can delete an existing participant and unlink it from the account.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/account/delete-participant/{participantId}

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

### Path Parameter
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| participantId | Required | Refers to the unique identifier for the participant you want to delete | String |

**Dev Notes: **Please note that if a participant is a primary participant, it cannot be deleted

## Example - Request















Copy Code



	curl -X DELETE \
  https://api3.sprinklr.com/{env}/api/v2/account/delete-participant/5e4e591a30372d6687a6d363' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





	204 No Content







[](https://dev.sprinklr.com/delete-participant)




[Back to top](https://dev.sprinklr.com/delete-participant)
