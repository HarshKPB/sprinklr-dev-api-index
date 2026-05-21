---
title: "Update Account Visibility"
slug: update-account-visibility
url: https://dev.sprinklr.com/update-account-visibility
---

# Update Account Visibility

#
  PUT Update Account Visibility

While sharing an account with other users, you can restrict its visibility. This enables you to take control of your account and how different teams access them. This API call will help update visibility permissions of any given account.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/{accountId}/visibility-permissions

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
| accountId | Required | Refers to the unique Id of the account. | String |

## Sample - Request




 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/account/600001987/visibility-permissions \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -d '{
        "permissions": [
            {
                "type": "CLIENT",
                "ids": [
                    "1","2"
                ]
            },
            {
                "type": "CLIENT_GROUP",
                "ids": []
            }
        ]
    }'




## Sample - Response




"data":
   {
        "id": "600001987",
        "type": "LINKEDIN",
        "displayName": "Mal Ad",
        "channelId": "NxEiRW4qB0",
        "owner": 600000103,
        "properties": "{\"eligibleForBrandedContent\":\"false\",\"accountId\":\"600001987\",\"isAdvetiser\":\"true\",\"isVerified\":\"false\",\"verificationStatus\":\"not_verified\",\"isLocation\":\"false\",\"isAccountPolitical\":\"false\",\"isAdmin\":\"true\",\"hasReviewEnabled\":\"false\",\"hasMailboxPermssion\":\"true\",\"hasIGDMPermission\":\"true\"}",
        "channelType": "LINKEDIN",
        "spaceId": 19,
        "partnerCustomProperties": {
            "5ccc20d1e4b0f6774e2d6274": [
                "All Accounts"
            ],
            "5ccc20d1e4b0f6774e2d62e5": [
                "No"
            ],
            "5d01fb46c7a0e3563d017a49": [
                "a"
            ]
 },
"visibility": {
            "globallyVisible": false,
            "shareConfigs": [
                {
                    "type": "CLIENT",
                    "ids": [
                        "1",
                        "7"
                    ]
                },
                {
                    "type": "CLIENT_GROUP",
                    "ids": []
                }
            ]
        },
        "permissions": [
            {
                "type": "CLIENT",
                "ids": [
                    "1",
                    "2"
                ]
            },
            {
                "type": "CLIENT_GROUP",
                "ids": []
            }
        ],
        "permalink": "https://www.linkedin.com/in/malnad-ma-business-ad-a8b241195/",
        "active": true,
        "deactivationReason": "",
        "deleted": true,
        "createdTime": "2019-10-11 09:41:08.0",
        "modifiedTime": "2022-06-29 15:29:37"
    },
    "errors": []
}





### Response Parameters





















****





























































































| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| id |  | The unique account Id | Integer |
| type |  | The type of account. Example: TWITTER, LINKEDIN, FBPAGE | String |
| displayName |  | The display name on the social account | String |
| channelId |  | The unique id of the channel where the account exists | String |
| owner |  | Refers to user id of the account owner | Integer |
| properties |  | Object defining the different properties (attributes) of the respective account | Object |
| channelType |  | Refers to the respective channel type | String |
| spaceId |  | The client id related to the account | String |
| clientCustomProperties |  | Workspace level custom properties | Object |
| partnerCustomProperties |  | Global level custom properties | Object |
| visibility |  | Object containing account sharing (visibility) details | Object |
|  | globallyVisible | Determines whether the account is globally visible or not | Boolean |
|  | shareConfigs | The object containing details of account sharing configuration | Array |
| permissions |  | Array defining the details of different permissions on the account | Array |
| permalink |  | Account url | URL |
| active |  | Determines whether the account is active or not | Boolean |
| deleted | Boolean | Determines whether the account is deleted or not | Boolean |
| deactivationReason | If deactivated, determines the reason of account deactivation | String |  |
| createdTime |  | The time when the account was created | String |
| modifiedTime |  | The time when the account was last modified | String |

### Array Details for permissions and shareConfigs




















| Parameter | Definition | Type |
| --- | --- | --- |
| type | The type of permission/shareConfig | String |
| Id | Ids related to the mentioned type | List [String] |

[](https://dev.sprinklr.com/update-account-visibility)




[Back to top](https://dev.sprinklr.com/update-account-visibility)
