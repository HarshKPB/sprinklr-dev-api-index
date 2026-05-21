---
title: "Update Profile List"
slug: update-profile-list
url: https://dev.sprinklr.com/update-profile-list
---

# Update Profile List

#
  POST Update Profile List



This API allows you to update the profile list in a workflow.

The API is particularly useful in the following scenarios:


- **Audience Segmentation:** Since profiles can be added to multiple profile lists, this API can be used to segment your audience based on various criteria, such as demographics, behavior, etc. This can help in targeted marketing or personalized customer engagement.

- **Triggering a Journey Based on Profile Lists:** You can use this API to add profiles to a list that is used as a trigger for a journey. For example, if you want to start a journey for all users who have recently made a purchase, you can add these users to a profile list and then use this list as the trigger for the journey.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/profile/workflow/profile-list

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```







[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |

### Request Payload













- ****[Channel Type](https://dev.sprinklr.com/channels-v1)
- ****

```

```
``







[Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1)

```

```








[Bootstrap](https://dev.sprinklr.com/bootstrap-api-v1)

```

```





| Field | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| universalProfileKeyList | Required | This is a JSON array that contains the Universal Profile Keys. A Universal Profile Key is a unique identifier for a profile in the system.                  Each key is an object that includes:                                               channelType: The type of the channel. Refer to  for detailed information.                          channelId: The unique identifier for the channel. You can find this Id from the properties section mentioned under user profile on Sprinklr's platform                                          Example:                  "universalProfileKeyList": [         {             "channelType": "FACEBOOK",             "channelId": 5027904559         }] | Array |
| clientProfileLists | Optional | An array of client profile list ids                 You can find the client profile list ids with the  endpoint using types=CLIENT_PROFILE_LISTS                 Example:                 "clientProfileLists": [1, 2] | List < Long > |
| partnerProfileLists | Optional | An array of partner profile list ids                 You can find the partner profile list ids with the  endpoint using types=PARTNER_PROFILE_LISTS                 Example:                 "partnerProfileLists": [8, 10] | Long |

### Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/profile/worfklow/profileList' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
    "universalProfileKeyList": [
        {
            "channelType": "FACEBOOK",
            "channelId": 5027904559
        }
    ],
    "partnerProfileLists": [
        205,
        473
    ],
    "clientProfileLists": [
        952,
        400,
        1595
    ]
}'






### Example - Response





true







**Dev Note: ** The true response implies that the profile list has been successfully updated.

 [](https://dev.sprinklr.com/update-profile-list)




[Back to top](https://dev.sprinklr.com/update-profile-list)
