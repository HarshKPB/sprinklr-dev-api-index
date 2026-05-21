---
title: "Profile List Update v1"
slug: profile-list-update-v1
url: https://dev.sprinklr.com/profile-list-update-v1
---

# Profile List Update v1

#
  POST - Profile List Update

Using this API, you can update the profile list for the given client Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/profile/workflow/profileList

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

### Path Parameters













[Bootstrap](https://dev.sprinklr.com/bootstrap-api-v1)

```

```





| Field | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| clientId | Required | The client id in which to make the changes                 You can find the client id with the  endpoint using types=CLIENTS                 Example:                 clientid=4 | Integer |

### Request Payload













```

```
``
[app-scoped](https://developers.facebook.com/docs/apps/faq#faq_610616752452545)








```

```








[Bootstrap](https://dev.sprinklr.com/bootstrap-api-v1)

```

```








[Bootstrap](https://dev.sprinklr.com/bootstrap-api-v1)

```

```





| Field | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| universalProfileKeyList | Required | The JSON array of the Universal Profile Key                 Use the universalProfileKeyList when you know the social network profile id, but not the Sprinklr profile id                 Example:                  "universalProfileKeyList": [{     "snType": "FACEBOOK",     "snUserId": 215244391952058 }]                                  NOTE: Facebook's profile ids are , so match rates are low for integrated apps. | Array |
| ids | Required | An array of profile ids derived from Sprinklr                 Use the id when you know the Sprinklr profile id                 Example:                 "ids": [     "5152879be4b0f59a42d8c7ea",      "5152879be4b0f59a42d8c7eb" ] | List < String > |
| clientProfileLists | Optional | An array of client profile list ids                 You can find the client profile list ids with the  endpoint using types=CLIENT_PROFILE_LISTS                 Example:                 "clientProfileLists": [1, 2] | List < Long > |
| partnerProfileLists | Optional | An array of partner profile list ids                 You can find the partner profile list ids with the  endpoint using types=PARTNER_PROFILE_LISTS                 Example:                 "partnerProfileLists": [8, 10] | Long |

### Note:

Facebook's profile ids are [app-scoped](https://developers.facebook.com/docs/apps/faq#faq_610616752452545)

## Example - Request




 Copy Code


curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v1/profile/worfklow/profileList&clientId=4' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
   "universalProfileKeyList":[
      {
         "snType":"INSTAGRAM",
         "snUserId":181037639
      }
   ],
   "partnerProfileLists":[
      1
   ]
}'





## Example - Response




true





[](https://dev.sprinklr.com/profile-list-update-v1)




[Back to top](https://dev.sprinklr.com/profile-list-update-v1)
