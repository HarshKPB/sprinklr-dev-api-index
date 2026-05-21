---
title: "Block User"
slug: block-user
url: https://dev.sprinklr.com/block-user
---

# Block User

#
Block User

Using this API, you can block a user for the given user id.

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/block

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Authenticated token for making API calls that require creating, updating, deleting tasks |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| objectId | Required | Refers to the unique user id associated with the user you want to block | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/block' \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
"objectId" : "611fc6d41da62f70570ca100"
}'





## Example - Response

      

{
   "userActivity": {
       "id": "66061BE4E176862C9411B06BA4168531",
       "actorId": "60ae445e4a5ae60c2e29aa03",
       "actUsername": "autouser1",
       "actFullName": "autouser1 autouser1",
       "actGrp": "block",
       "actType": "block",
       "actorType": "community_user",
       "receiverId": "611fc6d41da62f70570ca100",
       "recType": "community_user",
       "receiverUsername": "navya1198",
       "receiverFullName": "Navya A",
       "objId": "611fc6d41da62f70570ca100",
       "objType": "community_user",
       "actTm": 1666791262843,
       "actExpTm": -1,
       "del": false,
       "rD": {
           "experienceId": [
               "cd6aaaad-7d02-4599-9c62-aee8068f78da"
           ],
           "experienceType": [
               "COMMUNITY"
           ],
           "projectId": [
               "95da27b2-8e38-40ea-a2e1-4e0769cd7471"
           ],
           "awardsGivenFromReceiver": [
               "612336c9452a1c120caddc2e"
           ],
           "awardsGivenFromActor": [
               "612336c9452a1c120caddc2e"
           ]
       },
       "cTm": 1666791262843,
       "mTm": 1666791262874
   }
}





	[](https://dev.sprinklr.com/block-user)

[Back to top](https://dev.sprinklr.com/block-user)
