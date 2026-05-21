---
title: "Fetch Campaigns for an Account"
slug: fetch-campaigns-for-an-account
url: https://dev.sprinklr.com/fetch-campaigns-for-an-account
---

# Fetch Campaigns for an Account

#   POST Fetch Campaigns for an Account
 

This API allows you to fetch a paginated list of campaigns associated with a given account.


**Related Knowledge Base Article: **[Campaign Management](https://www.sprinklr.com/help/categories/campaign-management/63e380f553842c2a03a26862)


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/get/campaigns

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


### Request Parameters














[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-campaigns-for-an-account#account_userid)



| Parameter | Required/Optional | Description |
| --- | --- | --- |
| accountUserId | Required | Id of the ad account userSee |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/get/campaigns' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "accountUserId": "394232028806869"
}'



## Example - Response





{
  "data": {
    "adEntities": [
      {
        "id": "670f8fad21799e635506beaf",
        "name": "||",
        "channelId": "120215997741860569",
        "channelType": "FACEBOOK",
        "adObjective": "OUTCOME_TRAFFIC",
        "status": "ARCHIVED",
        "startTime": 1729073074000
      },
      {
        "id": "FACEBOOK_120228581286360569",
        "name": "Automation_Fb_Leads_Forms_New_Obj 2025-05-08 12:28:22.931",
        "channelId": "120228581286360569",
        "channelType": "FACEBOOK",
        "adObjective": "OUTCOME_LEADS",
        "status": "ARCHIVED",
        "startTime": 1746687758000
      },
      {
        "id": "6819e4dcee4f7a0d6b60776b",
        "name": "sd",
        "channelType": "FACEBOOK",
        "adObjective": "OUTCOME_AWARENESS",
        "status": "DRAFT",
        "startTime": 1746527435422,
        "adCategories": []
      },
      {
        "id": "FACEBOOK_23851906132280568",
        "name": "abc",
        "channelId": "23851906132280568",
        "channelType": "FACEBOOK",
        "adObjective": "OUTCOME_ENGAGEMENT",
        "status": "ARCHIVED",
        "startTime": 1657901552000
      },
      {
        "id": "6853fb6f553ca14f41ddcc74",
        "name": "asdfasdf",
        "channelId": "120231811483380569",
        "channelType": "FACEBOOK",
        "adObjective": "OUTCOME_LEADS",
        "status": "PAUSED",
        "startTime": 1750334334000
      },
      {
        "id": "FACEBOOK_23851379066460568",
        "name": "abc",
        "channelId": "23851379066460568",
        "channelType": "FACEBOOK",
        "adObjective": "OUTCOME_APP_PROMOTION",
        "status": "ARCHIVED",
        "startTime": 1652872074000,
        "smartPromotionType": "Facebook Advantage+ App Campaigns"
      }
    ],
    "errors": []
  },
  "errors": []
}




### Response Parameters































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. |  |
|  | adEntities | Object containing product catalog objects.See the Product Catalog table below. | Object |
| errors |  | Array containing error details, if any. | Array |


### AdEntities Object














































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the paid initiative. | String |
| name | Name of the paid initiative. | String |
| channelId | Identifier for the ad account or platform-specific channel. | String |
| channelType | Advertising platform/channel type (For example, FACEBOOK). | String |
| adObjective | Advertising objective enum (For example, OUTCOME_TRAFFIC). | AdObjective |
| status | Current status of the initiative (For example, ARCHIVED, DRAFT). | String |
| startTime | Start time of the campaign (epoch timestamp). | Long |

[](https://dev.sprinklr.com/fetch-campaigns-for-an-account) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-campaigns-for-an-account)
