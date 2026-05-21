---
title: "Fetch Funding Instruments"
slug: fetch-funding-instruments
url: https://dev.sprinklr.com/fetch-funding-instruments
---

# Fetch Funding Instruments

#   GET Fetch Funding Instruments


This API allows you to retrieve the list of funding instruments associated with an ad account user Id. Funding Instruments are the sources of campaign budgets used to finance advertising across various social media platforms, including X, Pinterest, and others.



**Related Knowledge Base Article: **[X Funding Instruments](https://www.sprinklr.com/help/articles/setting-up-twitter-in-sprinklr/x-funding-instruments/63f36afae02459133724a034)

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/fundingInstruments

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


## Query Parameters
















[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-funding-instruments#account_uid)







****




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountUserId | Required | Id of the ad account user. See . | String |
| fetchExpiredToo | Optional | Indicates whether to include expired funding instruments. Supported Values: true, false | Boolean |


### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request




 Copy Code


curl --location --request GET 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/fundingInstruments?accountUserId=18ce54wwx23&fetchExpiredToo=false' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}'



## Example - Response





{
    "data": {
        "responseEntities": [
            {
                "id": "TWITTER_ven6b",
                "channelId": "ven6b",
                "description": "MasterCard ending in 4762",
                "channelType": "TWITTER",
                "adAccountId": 66001284,
                "channelAccountId": "18ce54wwx23",
                "type": "CREDIT_CARD",
                "currency": "USD",
                "entityStatus": "ACTIVE",
                "fundedAmount": 395.02,
                "creditLimit": 1000.0,
                "creditRemaining": 0.0,
                "deleted": false,
                "blacklisted": false,
                "startTime": 1560258400000,
                "updatedAt": 1680701852000,
                "createdAt": 1560258400000
            }
        ]
    },
    "errors": []
}




### Response Parameters
































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. |  |
|  | responseEntities | Object containing response entities.See Response Entities object table below. | Object |
| errors |  | Array containing error details, if any. | Array |


### Response Entities Object

































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id of the funding instrument | String |
| channelId | Id of the advertising channel | String |
| description | Description of the funding instrument (for example, card details) | String |
| channelType | Type of the advertising channel (for example, TWITTER) | String |
| adAccountId | Id of the ad account | Number |
| channelAccountId | Account Id of the channel | String |
| type | Type of funding instrument (for example, CREDIT_CARD) | String |
| currency | Currency code (for example, USD) | String |
| entityStatus | Current status of the funding instrument (for example, ACTIVE) | String |
| fundedAmount | Amount already funded | Number |
| creditLimit | Maximum credit limit | Number |
| creditRemaining | Remaining credit | Number |
| deleted | Indicates if the funding instrument is deleted | Boolean |
| blacklisted | Indicates if the funding instrument is blacklisted | Boolean |
| startTime | Time when the funding instrument became active | Epoch |
| updatedAt | Last updated timestamp | Epoch |
| createdAt | Creation timestamp | Epoch |

[](https://dev.sprinklr.com/fetch-funding-instruments) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-funding-instruments)
