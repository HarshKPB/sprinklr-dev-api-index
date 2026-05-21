---
title: "Remove Awards from Users"
slug: remove-awards-from-users
url: https://dev.sprinklr.com/remove-awards-from-users
---

# Remove Awards from Users

#
Remove Awards from Users


Using this API, you can remove assigned awards such as ranks and badges from users.

**Dev Notes: **

- To assign a rank, you’ll first need to use this API to remove the existing rank of the user
- To fetch badge Id, refer to Search Awards by Name API

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/gamification/award/remove-from-user

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Authenticated token for making API calls that require creating, updating, deleting tasks |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Query Parameters

-
-

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| awardId | Required | The unique identifier for the award you want to removeRank id for rankBadge Id for badge | String |
| userId | Required | The unique identifier for the user you want to revoke the award for | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/gamification/award/remove-from-user?awardId=60feac3559ba7a5bc4606e0e&userId=611fc6d41da62f70570ca100' \
 -H 'X-Community-Authorization: Bearer {authenticated Token}' \
 -H 'Content-Type: application/json' \





## Example - Response

      

204 No Content





**Dev Notes: **204 No Content implies that the award has been removed from the user

 [](https://dev.sprinklr.com/remove-awards-from-users)




[Back to top](https://dev.sprinklr.com/remove-awards-from-users)
