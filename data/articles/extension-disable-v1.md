---
title: "Extension Disable v1"
slug: extension-disable-v1
url: https://dev.sprinklr.com/extension-disable-v1
---

# Extension Disable v1

#
  DELETE Extension Disable




You can disable an extension point via this API call, which defines the callback URL destinations to receive a pushed data payload from Sprinklr.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/extension/{Id}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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

## Path Parameters


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | The id of the Extension point on wish to disable | String |

## Example - Request















Copy Code



curl -X DELETE \
  https://api3.sprinklr.com/{env}/api/v1/extension/5c2f44c8e4b08015475d35ac' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





"Extension has been disabled"







	[](https://dev.sprinklr.com/extension-disable-v1)






[Back to top](https://dev.sprinklr.com/extension-disable-v1)
