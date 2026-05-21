---
title: "Read Account"
slug: read-account
url: https://dev.sprinklr.com/read-account
---

# Read Account

#
  GET Fetch Account

An Account refers to a social network account that has been added and authorized within Sprinklr. Each of the accounts added in Sprinklr has a unique account Id. This API call helps customers fetch account details using the unique account Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/{accountId}


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
| accountId | Required | The unique Id of the account added in the Sprinklr | String |

**Steps to Extract Account Id from UI: **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on Accounts Icon within "Manage Workspace" module
- Click on the three dots placed alongside the respective account name
- Click on "Details" option from the drop down menu
- Click on copy url icon on the top right corner from the window that appears
- Use any encoder-decoder tool and paste the copied URL
- The account id will be the part of the decoded URL, i.e., if you get `/ACCOUNT/100426226/OVERVIEW` in the decoded URL, your account id is 100426226.

## Example - Request




 Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/account/600001987'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



### Example - Response




{
    "data": {
        "id": "1000069676",
        "type": "FBPAGE",
        "displayName": "Facebook Test Account",
        "channelId": "866846660087941",
        "owner": 1000052916,
        "properties": "{\"isAdvetiser\":\"true\",\"currentAdminRole\":\"ADMIN\",\"real_time_update_key\":\"402131656569013\",\"isVerified\":\"false\",\"verificationStatus\":\"not_verified\",\"coverImageUrl\":\"https:\/\/scontent-lga3-2.xx.fbcdn.net\/v\/t1.18169-9\/14265080_910043652434508_3602145346517657247_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=1091cb&_nc_ohc=scqZyjAuSQoAX90hcvn&_nc_ht=scontent-lga3-2.xx&edm=AJdBtusEAAAA&oh=582c26f1006d6de40f4bbdd52742febf&oe=61C1DC3A\",\"isWhatsappNumberConnected\":\"false\",\"isAdmin\":\"true\",\"hasMailboxPermssion\":\"true\",\"hasIGDMPermission\":\"true\",\"eligibleForBrandedContent\":\"false\",\"isLocation\":\"false\",\"managePagesDeprecatedTS\":\"1637662279175\",\"hasReviewEnabled\":\"false\",\"isHOPv2Enabled\":\"true\",\"relayEnabled\":\"true\",\"accountId\":\"1000069676\",\"isAccountPolitical\":\"false\",\"ELIGIBLE_FOR_RIGHTS_MANAGEMENT\":\"false\"}",
        "channelType": "FACEBOOK",
        "spaceId": 1000004509,
        "partnerCustomProperties": {
            "5b3f6a8ee4b0df2023c53017": [
                "Profile"
            ],
            "_c_63763607c9b1435779c91350": [
                "8"
            ],
            "_c_63e09d349542a07754276277": [
                "sds"
            ],
            "5c76b93be4b035d83e9811f2": [
                "logged_in_user"
            ]
        },
        "permalink": "https://www.facebook.com/8668466600870941",
        "active": true,
        "deactivationReason": "",
        "deleted": false,
        "createdTime": "2016-12-29 06:53:12.0",
        "modifiedTime": "2023-04-12 15:22:17"
    },
    "errors": []
}



### Response Parameters





















****





























			[channel type](https://dev.sprinklr.com/channels-v1)































































| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| id |  | The unique account Id | Integer |
| type |  | The type of account. Example: TWITTER, LINKEDIN, FBPAGE | String |
| displayName |  | The display name on the social account | String |
| channelId |  | The unique id of the channel where the account exists | String |
| owner |  | Refers to user id of the account owner | Integer |
| properties |  | Object defining the different properties (attributes) of the respective account | Object |
| channelType |  | The respective | String |
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
| deactivationReason |  | If deactivated, determines the reason of account deactivation | String |
| createdTime |  | The time when the account was created | String |
| modifiedTime |  | The time when the account was last modified | String |

### Array Details for permissions and shareConfigs




















| Parameter | Definition | Type |
| --- | --- | --- |
| type | The type of permission/shareConfig | String |
| Id | Ids related to the mentioned type | List [String] |

[](https://dev.sprinklr.com/read-account)




[Back to top](https://dev.sprinklr.com/read-account)
