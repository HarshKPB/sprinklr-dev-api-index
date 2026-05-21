---
title: "Fetch Campaigns by Id"
slug: fetch-campaigns-by-id
url: https://dev.sprinklr.com/fetch-campaigns-by-id
---

# Fetch Campaigns by Id

#   POST Fetch Campaigns by Id
 

This API retrieves campaign details for the specified campaign IDs from a given advertising account.


**Related Knowledge Base Article: **[Campaign Management](https://www.sprinklr.com/help/categories/campaign-management/63e380f553842c2a03a26862)


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/get/campaignByIds

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
















[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-campaigns-by-id#account_userid)





      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| accountUserId | Required | String | Id of the ad account userSee |
| adEntityIds | Required | String | Campaign ID to fetch details for. Format: {CHANNEL}_{ID}(for example, FACEBOOK_120213190680540130). |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request



 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/get/campaignByIds' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "accountUserId": "394232028806869",
    "adEntityIds": "FACEBOOK_120213190680540130"
}'



## Example - Response





{
    "data": {
        "adEntities": [
            {
                "id": "FACEBOOK_120213190680540130",
                "name": "Sprinklr Test (DO NOT DELETE)",
                "channelId": "120213190680540130",
                "channelType": "FACEBOOK",
                "adObjective": "OUTCOME_AWARENESS",
                "status": "PAUSED",
                "startTime": 1726662600000,
                "lifeTimeBudget": 100.0
            }
        ],
        "errors": []
    },
    "errors": []
}



## Response Parameters





































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. | Object |
|  | adEntities | List of campaign details.See the adEntities table below. | Array of Objects |
|  | errors | List of errors, if any, within the data object. | Array |
| errors |  | List of errors, if any, at the root level. | Array |

### adEntities Object














































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the paid initiative. | String |
| name | Name of the paid initiative. | String |
| channelId | Identifier for the ad account or platform-specific channel. | String |
| channelType | Advertising platform/channel type (For example, FACEBOOK). | String |
| adObjective | Advertising objective enum (For example, OUTCOME_TRAFFIC). | AdObjective |
| status | Current status of the initiative (For example, ARCHIVED, DRAFT). | String |
| startTime | Start time of the campaign (epoch timestamp). | Long |

[](https://dev.sprinklr.com/fetch-campaigns-by-id) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-campaigns-by-id)
