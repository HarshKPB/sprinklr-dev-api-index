---
title: "Fetch Audience Metadata"
slug: fetch-audience-metadata
url: https://dev.sprinklr.com/fetch-audience-metadata
---

# Fetch Audience Metadata

#  POST  Fetch Audience Metadata

This API retrieves available audience targeting fields for a given combination of ad objective, destination type, and buying type. This metadata helps you determine which targeting options are applicable when creating or editing paid social campaigns.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/audience/metadata

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


## Request Body Parameters




















      ````





      ````





      ``






-
-
-
-
-















| Field | Type | Required | Description |
| --- | --- | --- | --- |
| accountUserId | String | Yes | Social network user ID associated with the ad account. |
| adObjective | String (Enum) | No | The objective of the ad campaign (e.g., OUTCOME_TRAFFIC, BRAND_AWARENESS). |
| destinationType | String (Enum) | No | The destination associated with the ad (e.g., LEAD_FORM_MESSENGER, WEBSITE). |
| buyingType | String (Enum) | No | The media buying type for the campaign. Set it to AUCTION. |
| adCategories | Array of strings | No | The ad category. Supported enum values:                    HOUSING           CREDIT           FINANCIAL_PRODUCTS_SERVICES           EMPLOYMENT           ISSUES_ELECTIONS_POLITICS |
| adCategoriesCountries | Array of strings | No | Countries associated with ad categories. |
| isPulseCampaign | Boolean | No | Specifies whether the campaign is Pulse-based. |

### Enum Values for adObjective

















| Enum | Label |
| --- | --- |
| OUTCOME_AWARENESS | Facebook Awareness |
| OUTCOME_ENGAGEMENT | Facebook Engagement |
| OUTCOME_LEADS | Facebook Leads |
| OUTCOME_SALES | Facebook Sales |
| OUTCOME_TRAFFIC | Facebook Traffic |
| OUTCOME_APP_PROMOTION | Facebook App Promotion |
| MARKETING_MESSAGES | Marketing Messages |

## Objective to Destination Type Mapping

The following table lists the supported `destinationType` values for each `adObjective`. Use this reference to determine valid destination types for your selected objective when configuring an ad.

Objectives like `OUTCOME_APP_PROMOTION` and `MARKETING_MESSAGES` do not support any destination types.


















| Objective (adObjective) | Destination Type (destinationType) |
| --- | --- |
| OUTCOME_TRAFFIC | WEBSITE_MESSENGER |
| APP_STORE |  |
| WHATSAPP |  |
| MESSENGER |  |
| INSTAGRAM_DIRECT |  |
| PHONE_CALL |  |
| INSTAGRAM_PROFILE |  |
| OUTCOME_AWARENESS | STORE_VISIT |
| WEBSITE_MESSENGER |  |
| OUTCOME_ENGAGEMENT | ON_POST |
| ON_VIDEO |  |
| WEBSITE_MESSENGER |  |
| ON_PAGE |  |
| WHATSAPP |  |
| APP_STORE |  |
| PHONE_CALL |  |
| ON_EVENT |  |
| CLICK_TO_MESSENGER |  |
| ON_REMINDER |  |
| SPONSORED_MESSAGES |  |
| OUTCOME_SALES | WEBSITE_MESSENGER |
| CATALOG |  |
| APP_STORE |  |
| WEBSITE_APP |  |
| WHATSAPP |  |
| MESSENGER |  |
| PHONE_CALL |  |
| OUTCOME_LEADS | ON_AD |
| WEBSITE_MESSENGER |  |
| MESSENGER |  |
| LEAD_FORM_MESSENGER |  |
| APP_STORE |  |
| LEAD_FROM_IG_DIRECT |  |
| PHONE_CALL |  |
| OUTCOME_APP_PROMOTION | (No destination types) |
| MARKETING_MESSAGES | (No destination types) |

## Steps to Retrieve `accountUserId`


- In Sprinklr, click the **New Page (+)** icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the Accounts page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the **User ID** column. This value corresponds to the `accountUserId`.


## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/audience/metadata' \
--header 'Authorization: Bearer {Token}’ \
--header 'Key: {Api_Key}’ \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "adObjective": "OUTCOME_TRAFFIC",
    "destinationType": "LEAD_FORM_MESSENGER",
    "buyingType": "AUCTION",
    "adCategories": "EMPLOYMENT",
    "accountUserId": "394232028806869"
}'


## Example - Response


{
    "data": {
        "audienceTargetFields": [
            "TARGETING_TYPE",
            "CUSTOM_AUDIENCES",
            "LOCATION",
            "LOCATION_INTEREST_TARGETING",
            "AGE_RANGE",
            "GENDER",
            "LOCALES",
            "FLEXIBLE",
            "CONNECTION_TARGETING",
            "PLATFORM",
            "PLATFORM_VERSION_RANGE",
            "DEVICE",
            "EXCLUDED_DEVICE",
            "USER_DEVICE_WIRELESS_CARRIER"
        ]
    },
    "errors": []
}

## Response Schema






























| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | object | Contains the response payload for the request. |
|  | audienceTargetFields | array | List of audience targeting field identifiers available for the given campaign configuration. |
| errors |  | array | Any errors encountered during the request. |

[](https://dev.sprinklr.com/fetch-audience-metadata)

[Back to top](https://dev.sprinklr.com/fetch-audience-metadata)
