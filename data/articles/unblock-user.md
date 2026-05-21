---
title: "Unblock User"
slug: unblock-user
url: https://dev.sprinklr.com/unblock-user
---

# Unblock User

#
Unblock User

Using this API, you can unblock a user for the given user id.

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/un-block

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
| objectId | Required | Refers to the unique user id associated with the user you want to unblock | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/un-block' \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
"objectId" : "611fc6d41da62f70570ca100"
}'





## Example - Response



{
   "userActivity": {
       "id": "3CDD0008865901D5278B7AF1E7455AFE",
       "actorId": "60ae445e4a5ae60c2e29aa03",
       "actUsername": "autouser1",
       "actFullName": "autouser1 autouser1",
       "actGrp": "block",
       "actType": "unblock",
       "actorType": "community_user",
       "receiverId": "611fc6d41da62f70570ca100",
       "recType": "community_user",
       "receiverUsername": "navya1198",
       "receiverFullName": "Navya A",
       "objId": "611fc6d41da62f70570ca100",
       "objType": "community_user",
       "actTm": 1666791535808,
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
       "cTm": 1666791535808,
       "mTm": 1666791535842
   }
}





	[](https://dev.sprinklr.com/unblock-user)

[Back to top](https://dev.sprinklr.com/unblock-user)
