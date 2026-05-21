---
title: "Fetch Custom Pixel Event Types"
slug: fetch-custom-pixel-event-types
url: https://dev.sprinklr.com/fetch-custom-pixel-event-types
---

# Fetch Custom Pixel Event Types

#   POST Fetch Custom Pixel Event Types
 

This API allows you to retrieve custom pixel event types for a given ads account and pixel.



**Related Knowledge Base Article: **[Ads Pixel Overview](https://www.sprinklr.com/help/articles/getting-started/ads-pixel-overview/6400ab4e32d12b63c5f56118)



## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/customEventTypes

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


## Request Parameters
















[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-custom-pixel-event-types#account_userid)






[Steps to Retrieve Pixel Id](https://dev.sprinklr.com/fetch-custom-pixel-event-types#account_pixelid)







****

- [Facebook Ad Objectives](https://dev.sprinklr.com/fetch-custom-pixel-event-types#fb_ad_objective)
- [LinkedIn Ad Objectives](https://dev.sprinklr.com/fetch-custom-pixel-event-types#linkedinAdObjectives)
- [X Ad Objectives](https://dev.sprinklr.com/fetch-custom-pixel-event-types#xAdObjectives)







****
[Facebook Ad Objective and Destination Type Mapping](https://dev.sprinklr.com/fetch-custom-pixel-event-types#fb_ad_objective_destination_map)







****
[Facebook Smart Promotion Types](https://dev.sprinklr.com/fetch-custom-pixel-event-types#fb_smart_promotion_types)




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountUserId | Required | Id of the ad account.See . | String |
| pixelId | Required | Id of the pixel whose details you want to fetch.See . | String |
| adObjective | Optional | The objective of the advertisement campaign.Supported Values: | Enum |
| destinationType | Optional | The type of destination associated with the ad.Supported Values: | Enum |
| smartPromotionType | Optional | The type of smart promotion used.Supported Values: | Enum |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

### Steps to Retrieve Pixel Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Marketing** > **Advertising** tab.

-  Under **Plan**, click **Campaign Workflow** > **Tools and Settings**. This opens the Ads Settings page.

- Search for and select **Pixels**.

- On the Pixels page, locate the specific pixel you want to view.

- Once located, refer to the **Id** column to get the Pixel Id.
The pixel Id is the last part of the value in the Id column.
For example: `FACEBOOK_1000134302_609149790547258` -> Pixel Id: `609149790547258`.

### Facebook Channel Ad Objectives

The following table lists the supported ad objectives for Facebook (value for `adObjective` parameter):


















































| Enum | Label |
| --- | --- |
| OUTCOME_AWARENESS | Facebook Awareness |
| OUTCOME_TRAFFIC | Facebook Traffic |
| OUTCOME_ENGAGEMENT | Facebook Engagement |
| OUTCOME_LEADS | Facebook Leads |
| OUTCOME_SALES | Facebook Sales |
| OUTCOME_APP_PROMOTION | Facebook App Promotion |
| MESSAGES | Facebook Messages |
| CONVERSIONS | Facebook Conversions |
| CATALOG_SALES | Facebook Catalog Sales |
| STORE_VISITS | Facebook Store Visits |

### Facebook Ad Objective and Destination Type Mapping

The following table maps the supported ad objectives and destination types (value for `destinationType` parameter):














































| Ad Objective | Supported Destination Types |
| --- | --- |
| OUTCOME_AWARENESS | AWARENESS, WEBSITE |
| OUTCOME_TRAFFIC | WEBSITE, ON_POST, ON_PAGE, ON_EVENT, OPEN_MAP, APP_STORE, CLICK_TO_MESSENGER, PHONE_CALL, INSTAGRAM_PROFILE |
| OUTCOME_ENGAGEMENT | ON_POST, ON_PAGE, ON_EVENT, ON_VIDEO, ON_REMINDER |
| APP_INSTALLS | APP_STORE, CROSS_PIXEL_APP |
| LEAD_GENERATION | ON_AD (Instant Form), WEBSITE |
| MESSAGES | CLICK_TO_MESSENGER, MESSENGER, WEBSITE_MESSENGER, WHATSAPP, INSTAGRAM_DIRECT |
| CONVERSIONS | WEBSITE, APP_STORE, CROSS_PIXEL_APP |
| CATALOG_SALES | WEBSITE, INSTAGRAM_DIRECT |
| STORE_VISITS | STORE_VISIT, STORE, OPEN_MAP |

### Facebook Smart Promotion Types

The following table lists the supported Smart Promotion Types for Facebook (value for `smartPromotionType` parameter):


















| Enum | Label |
| --- | --- |
| SMART_APP_PROMOTION | Facebook Advantage+ App Campaigns |
| AUTOMATED_SHOPPING_ADS | Facebook Advantage+ Shopping Ads |


### LinkedIn Channel Ad Objectives

The following table lists the supported ad objectives for LinkedIn (value for adObjective parameter).






































| Ad Objective | Label |
| --- | --- |
| LINKEDIN_WEBSITE_VISIT | Website Visit |
| LINKEDIN_BRAND_AWARENESS | Brand Awareness |
| LINKEDIN_LEAD_GENERATION | Lead Generation |
| LINKEDIN_ENGAGEMENT | Engagement |
| LINKEDIN_VIDEO_VIEWS | Video Views |
| LINKEDIN_JOB_APPLICANT | Job Applicant |
| LINKEDIN_WEB_CONVERSION | Web Conversion |

### X (Twitter) Channel Ad Objectives

The following table lists the supported ad objectives for X (value for adObjective parameter).










































| Ad Objective | Label |
| --- | --- |
| PROMOTED_TWEETS | X Engagements |
| TWITTER_AWARENESS | X Reach |
| TWITTER_WEBSITE_CLICKS | X Website Traffic |
| PROMOTED_ACCOUNTS | X Followers |
| TWITTER_VIDEO_VIEWS | X Video Views |
| TWITTER_PREROLL_VIEWS | X Preroll Views |
| TWITTER_APP_INSTALLS | X App Installs |
| TWITTER_APP_ENGAGEMENTS | X App Re Engagements |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/customEventTypes' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}'\
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
      "accountUserId": "394232028806869",
      "pixelId": "609149790547258"
}'



## Example - Response





{
    "data": {
        "responseEntities": [
            {
                "pixelEventType": "STANDARD",
                "key": "ACHIEVEMENT_UNLOCKED",
                "label": "Unlock Achievement"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "ADD_PAYMENT_INFO",
                "label": "Add Payment Info"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "ADD_TO_CART",
                "label": "Add to Cart"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "ADD_TO_WISHLIST",
                "label": "Add to Wishlist"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "COMPLETE_REGISTRATION",
                "label": "Complete Registration"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "CONTACT",
                "label": "Contact"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "CONTENT_VIEW",
                "label": "View Content"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "CUSTOMIZE_PRODUCT",
                "label": "Customize Product"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "DONATE",
                "label": "Donate"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "FIND_LOCATION",
                "label": "Find Location"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "INITIATED_CHECKOUT",
                "label": "Initiate Checkout"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "LEAD",
                "label": "Lead"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "LEVEL_ACHIEVED",
                "label": "Achieve Level"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "OTHER",
                "label": "Other"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "PURCHASE",
                "label": "Purchase"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "RATE",
                "label": "Rate"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "SCHEDULE",
                "label": "Schedule"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "SEARCH",
                "label": "Search"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "SPENT_CREDITS",
                "label": "Spend Credits"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "START_TRIAL",
                "label": "Start Trial"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "SUBMIT_APPLICATION",
                "label": "Submit Application"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "SUBSCRIBE",
                "label": "Subscribe"
            },
            {
                "pixelEventType": "STANDARD",
                "key": "TUTORIAL_COMPLETION",
                "label": "Tutorial Completion"
            },
            {
                "pixelEventType": "CUSTOM",
                "key": "PageView",
                "label": "PageView"
            }
        ]
    },
    "errors": []
}




### Response Parameters
































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. |  |
|  | responseEntities | Object containing response entities.See Response Entities object table below. | Array |
| errors |  | Array containing error details, if any. | Array |


### Response Entities Object


























| Parameter | Description | Type |
| --- | --- | --- |
| pixelEventType | Type of event (for example, STANDARD or CUSTOM) | String |
| key | Event key (for example, ADD_TO_CART) | String |
| label | Label (for example, Add to Cart) | String |

[](https://dev.sprinklr.com/fetch-custom-pixel-event-types) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-custom-pixel-event-types)
