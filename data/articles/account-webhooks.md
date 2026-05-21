---
title: "Account Webhooks"
slug: account-webhooks
url: https://dev.sprinklr.com/account-webhooks
---

# Account Webhooks

# Account Webhooks

**Account Webhook Subscriptions:**
Account Created Event, Account Updated Event

Whenever an account is created or updated either via Sprinklr UI or API, account.created and account.updated webhooks get triggered, respectively.


- [account.created Webhook](https://dev.sprinklr.com/account-webhooks#accountCreated)

- [account.updated Webhook](https://dev.sprinklr.com/account-webhooks#accountUpdated)

### account.created Webhook - Response Payload




  Copy Code



	{
"id": "63cf7d3a328d923955979a37",
  "type": "account.created",
  "payload": {
    "id": "1000136867",
    "type": "INSTAGRAM",
    "displayName": "test.brand",
    "channelId": "58083033125",
    "owner": 1000053136,
    "channelType": "INSTAGRAM",
    "spaceId": 1000004509,
    "permalink": "https://www.instagram.com/test.brand",
    "active": true,
    "deactivationReason": "",
    "deleted": false,
    "createdTime": "2023-01-24 06:39:04",
    "modifiedTime": "2023-01-24 06:39:04"
  },
  "eventTime": 1674542394044,
  "subscriptionDetails": {
    "subscriptionId": "63ce853b97ce0d0046ce7f70"
  }
}





### account.updated Webhook - Response Payload




  Copy Code



{
    "id": "63ce81dd3f206b4679cfcf94",
    "type": "account.updated",
    "payload": {
        "id": "1000135835",
        "type": "TWITTER",
        "displayName": "Test Account",
        "channelId": "1570344873588412416",
        "owner": 1000053136,
        "properties": "{\"orgProfImgUrl\":\"https:\\/\\/pbs.twimg.com\\/profile_images\\/1571807702606647298\\/Rm2hCBas_normal.jpg\",\"relayEnabled\":\"true\"}",
        "channelType": "TWITTER",
        "spaceId": 1000004509,
        "clientCustomProperties": {},
        "partnerCustomProperties": {},
        "permalink": "https://twitter.com/testingaccountangfs05",
        "active": true,
        "deactivationReason": "",
        "deleted": false,
        "createdTime": "2022-09-26 07:23:02",
        "modifiedTime": "2023-01-23 12:47:17"
    },
    "eventTime": 1674478044773,
    "subscriptionDetails": {
        "subscriptionId": "63ce733e97ce0d0046cb363b"
    }
}





### Response Parameters

























[channel type](https://dev.sprinklr.com/channels-v1)

****

****

| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Refers to the unique identifier for the webhook triggered | String |
| type |  | Refers to the webhook type.account.updated in this case | String |
| payload |  | Object containing the account level details | Object |
|  | id | Refers to the account Id for the account residing in Sprinklr | String |
|  | type | Refers to the type of account | String |
|  | displayName | Refers to the name of the account owner | String |
|  | channelId | Refers to the unique identifier for the channel based on the channel type | String |
|  | owner | Refers to the user Id (within Sprinklr) of the account owner | Integer |
|  | properties | Refers to the object defining the account properties | Object |
|  | channelType | Refers to the  of the account | String |
|  | spaceId | Refers to the workspace Id where the account exists within Sprinklr | Integer |
|  | clientCustomProperties | Refers to the workspace level properties of the account | ObjectSyntax: "clientCustomProperties": {       "581b0602e4b0046846c201b3": [         "Hello"       ]} |
|  | partnerCustomProperties | Refers to the global (customer) level properties of the account | ObjectSyntax: "clientCustomProperties": {       "581b0602e4b0046846c201b4": [         "Testing"       ]} |
|  | permalink | Refers to the url of the account existing in native channel | Url |
|  | active | If true, the account is in active state | Boolean |
|  | deactivationReason | If the account is not active, this parameter conveys the reason for deactivation | String |
|  | deleted | If true, the account has been deleted from Sprinklr | Boolean |
|  | createdTime | Refers to the time at which the account was created | String |
|  | modifiedTime | Refers to the time at which the account was last modified | String |
| eventTime |  | Refers to the time at which the webhook was triggered | Epoch |
| subscriptionDetails |  | Object defining the webhook subscription details |  |
|  | subscriptionId | Refers to the unique identifier for the webhook subscription | String |

[](https://dev.sprinklr.com/account-webhooks)

[Back to top](https://dev.sprinklr.com/account-webhooks)
