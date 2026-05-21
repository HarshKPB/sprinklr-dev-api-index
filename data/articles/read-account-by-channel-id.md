---
title: "Read Account by Channel Id"
slug: read-account-by-channel-id
url: https://dev.sprinklr.com/read-account-by-channel-id
---

# Read Account by Channel Id

#
  GET Read Account by Channel Id

An Account refers to a social network account that has been added and authorized within Sprinklr. Each account added in Sprinklr has a unique channel and account Id. This API call helps customers fetch account details using the account type and channel Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/{accountType}/{channelId}


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





















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountType | Required | Type of account. e.g FACEBOOK, FBPAGE etc. | String |
| channelId | Required | Unique id of the account on channel. | String |

## Example - Request




 Copy Code



	 curl -X GET \
 https://api3.sprinklr.com/{env}/api/v2/account/FBPAGE/501 \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



## Example - Response




{
    "data": {
        "id": "600000004",
        "type": "FBPAGE",
        "displayName": "Quality",
        "channelId": "501",
        "owner": 600000080,
        "properties": "{\"isAdvetiser\":\"true\",\"isVerified\":\"false\",\"verificationStatus\":\"not_verified\",\"real_time_update_key\":\"125481627589244\",\"isAdmin\":\"true\",\"hasMailboxPermssion\":\"true\",\"hasIGDMPermission\":\"true\",\"eligibleForBrandedContent\":\"false\",\"accountId\":\"600001554\",\"isLocation\":\"false\",\"isAccountPolitical\":\"false\",\"hasReviewEnabled\":\"false\"}",
        "channelType": "FACEBOOK",
        "spaceId": 1,
        "partnerCustomProperties": {
            "5ccc20d1e4b0f6774e2d6274": [
                "All Accounts"
            ],
            "5ccc20d1e4b0f6774e2d62e5": [
                "No"
            ],
            "5d01fb46c7a0e3563d017a49": [
                "a"
            ],
            "5d0766caf9e3b75e00af2b9b": [
                "c"
            ],
            "5d021faef9e3b75620adfa37": [
                "12"
            ]
        },
        "active": true,
        "deleted": false,
        "createdTime": "2019-07-18 04:04:00.0",
        "modifiedTime": "2019-07-18 04:04:00.0"
    },
    "errors": []
}





### Response Parameters


















































































































| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| id |  | The account Id | Integer |
| type |  | The specific account type | String |
| displayName |  | The display name on the social media account | String |
| channelId |  | The unique Id of the account on the channel | String |
| owner |  | Refers to user id of the account owner | Integer |
| properties |  | Refers to the different properties set for an account | String |
| channelType |  | The channel on which the account existsInsight Into Different Channel Types | String |
| spaceId |  | The client id related to the account | String |
| clientCustomProperties |  | Workspace level custom properties | String |
| partnerCustomProperties |  | Global level custom properties | String |
| visibility |  | Object containing account sharing (visibility) details | Object |
|  | globallyVisible | Determines whether the account is globally visible or not | Boolean |
|  | shareConfigs | The object containing details of account sharing configuration | Array |
| permissions |  | Array defining the details of different permissions on the account | Array |
| permalink |  | Account url | URL |
| active |  | Determines whether the account is active or not | Boolean |
| deleted | Boolean | Determines whether the account is deleted or not | Boolean |
| deactivationReason |  | If deactivated, determines the reason of account deactivation | String |
| createdTime |  | The time when the account was created | String |
| modifiedTime |  | The time when the account was last modified | String |

### Array Details for permissions and shareConfigs




















| Parameter | Definition | Type |
| --- | --- | --- |
| type | The type of permission/shareConfig | String |
| Id | Ids related to the mentioned type | List [String] |

[](https://dev.sprinklr.com/read-account-by-channel-id)




[Back to top](https://dev.sprinklr.com/read-account-by-channel-id)
