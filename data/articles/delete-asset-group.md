---
title: "Delete Asset Group"
slug: delete-asset-group
url: https://dev.sprinklr.com/delete-asset-group
---

# Delete Asset Group

#
  DELETE Delete Asset Group

You can delete an Asset group via this API using group Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/asset-group/{groupId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Accept | application/json | Determines the acceptable response type from the server |

###  Path Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| groupId | Required | Id of the group. | String |

## Example - Request














Copy Code




curl -X DELETE \
   https://api3.sprinklr.com/{env}/api/v2/asset-group/{groupId} \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example - Response





204 (No Content)





	 [](https://dev.sprinklr.com/delete-asset-group)




[Back to top](https://dev.sprinklr.com/delete-asset-group)
