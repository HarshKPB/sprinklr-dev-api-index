---
title: "Fetch Supported CTA Options"
slug: fetch-supported-cta-options
url: https://dev.sprinklr.com/fetch-supported-cta-options
---

# Fetch Supported CTA Options

#   POST Fetch Supported CTA Options
 

This API allows you to retrieve a list of Call-To-Action (CTA) options that are supported for a specific ad setup on an advertising channel (for example, Facebook).

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/supported/cta

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
















****
















****

- [Facebook Ad Objectives](https://dev.sprinklr.com/fetch-supported-cta-options#fb_ad_objective)
- [LinkedIn Ad Objectives](https://dev.sprinklr.com/fetch-supported-cta-options#linkedinAdObjectives)
- [X Ad Objectives](https://dev.sprinklr.com/fetch-supported-cta-options#xAdObjectives)








****

- ****
- ****
- ****






      [Creative Type Object](https://dev.sprinklr.com/fetch-supported-cta-options#creative_type_object)














****
****








****
[Facebook Ad Positions](https://dev.sprinklr.com/fetch-supported-cta-options#fb_ad_positions)















****
[Facebook Objective and Destionation Type Mapping](https://dev.sprinklr.com/fetch-supported-cta-options#fb_objective_dest_type)







****







****




| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| channelType |  | Optional | Type of advertising channel.         Supported Values: FACEBOOK, LINKEDIN, TWITTER | String |
| accountUserId |  | Required | User Id associated with the advertising account.See Steps to Retrieve Account User Id | String |
| objective |  | Optional | The objective of the advertisement campaign.Supported Values: | Enum |
| postTypes |  | Optional | Type of post used in the ad Supported Values:    Facebook: LINK, PHOTO, VIDEO, TEMPLATE_DATA   LinkedIn: LINK, PHOTO, VIDEO, STATUS, DOCUMENT, TEXT   X: LINK, PHOTO, VIDEO, STATUS, OFFER, TEMPLATE_DATA, DOCUMENT, TEXT | Enum |
| creativeType |  | Optional | Object containing the details of the creative type used in the ad. See . | Object |
| adPlacementDetail |  | Optional | Object containing ad placement information | Object |
|  | publisherPlatforms | Optional | Platforms where ads will be published.Supported Values:Facebook:  FACEBOOK, INSTAGRAM, AUDIENCE_NETWORK, MESSENGER,WHATSAPP | Array |
|  | positions | Optional | Specific positions within platforms where ads will be shown.Supported Values: | Array |
| dynamicAdVoiceType |  | Optional | The type of voice used in dynamic ads. | Enum |
| destinationType |  | Optional | The type of destination associated with the ad.Supported Values: | Enum |
| optimizationType |  | Optional | Optimization strategy for the dynamic ad         Supported Values: COST_OPTIMIZATION | Enum |
| buyingType |  | Optional | Buying method for ads         Supported Values: AUCTION | Enum |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User Id** column corresponds to the `accountUserId` parameter.

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


### Facebook Ad Positions







































| Position Enum | Display Name |
| --- | --- |
| FEED | Facebook Feed |
| INSTANT_ARTICLE | Instant Articles |
| INSTREAM_VIDEO | Facebook In-Stream Videos |
| RIGHT_HAND_COLUMN | Facebook right column |
| SUGGESTED_VIDEO | Facebook Video Feeds |
| MARKETPLACE | Facebook Marketplace |
| FACEBOOK_STORIES | Facebook Stories |
| FACEBOOK_SEARCH | Facebook Search Results |
| INSTAGRAM_FEED | Instagram Feed |
| INSTAGRAM_EXPLORE | Instagram Explore |
| INSTAGRAM_STORIES | Instagram Stories |
| CLASSIC | Audience Network native, banner and interstitial |
| AUDIENCE_NETWORK_INSTREAM_VIDEO | Audience Network In-Stream Videos |
| REWARDED_VIDEO | Audience Network rewarded videos |
| SPONSORED_MESSAGES | Messenger sponsored messages |
| MESSENGER_STORY | Messenger Stories |
| INSTAGRAM_IGTV | Instagram TV |
| INSTAGRAM_REELS | Instagram Reels |
| FACEBOOK_REELS | Facebook Reels |
| FACEBOOK_REELS_OVERLAY | Ads on Facebook Reels |
| FACEBOOK_BIZ_DISCO_FEED | Facebook Business Explore |
| INSTAGRAM_PROFILE_FEED | Instagram Profile Feed |
| INSTAGRAM_EXPLORE_HOME | Instagram Explore Home |
| INSTAGRAM_SEARCH_RESULTS | Instagram search results |
| INSTAGRAM_REELS_OVERLAY | Ads on Instagram Reels |
| WHATSAPP_MARKETING_MESSAGE | WhatsApp Marketing Messages |
| FACEBOOK_PROFILE_FEED | Facebook Profile Feed |
| INSTAGRAM_PROFILE_REELS | Instagram Profile Reels |


### Facebook Objective and Destination Type Mapping






































| Objective (objective) | Destination Type (destinationType) |
| --- | --- |
| OUTCOME_TRAFFIC | WEBSITE_MESSENGER, APP_STORE, WHATSAPP, MESSENGER, INSTAGRAM_DIRECT, PHONE_CALL, INSTAGRAM_PROFILE |
| OUTCOME_AWARENESS | STORE_VISIT, WEBSITE_MESSENGER |
| OUTCOME_ENGAGEMENT | ON_POST, ON_VIDEO, WEBSITE_MESSENGER, ON_PAGE, WHATSAPP, APP_STORE, PHONE_CALL, ON_EVENT, CLICK_TO_MESSENGER, ON_REMINDER, SPONSORED_MESSAGES |
| OUTCOME_SALES | WEBSITE_MESSENGER, CATALOG, APP_STORE, WEBSITE_APP, WHATSAPP, MESSENGER, PHONE_CALL |
| OUTCOME_LEADS | ON_AD, WEBSITE_MESSENGER, MESSENGER, LEAD_FORM_MESSENGER, APP_STORE, LEAD_FROM_IG_DIRECT, PHONE_CALL |
| OUTCOME_APP_PROMOTION | (No destination types) |
| MARKETING_MESSAGES | (No destination types) |


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


### Creative Type Object










































































































































































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| name |  | Name of the creative | String |
| creativeId |  | Unique identifier for the creative | String |
| postType |  | Type of post used in the adSupported values: LINK, PHOTO, VIDEO, STATUS, OFFER, TEMPLATE_DATA, DOCUMENT, TEXT | String |
| isDarkPost |  | Whether it is a dark post | Boolean |
| pageId |  | ID of the associated page | String |
| secondaryPageId |  | ID of the secondary page/Instagram Page | String |
| postChannelId |  | ID of the post channel | String |
| title |  | Title of the creative | String |
| description |  | Description of the creative | String |
| linkUrl |  | URL link in the creative | String |
| linkDescription |  | Description for the link | String |
| displayLink |  | Display link | String |
| appLink |  | Deep Link URL | String |
| imageUrl |  | URL of the image | String |
| videoUrl |  | URL of the video | String |
| callToAction |  | Call to action text | String |
| leadFormId |  | Lead form ID | String |
| previewPageCount |  | Number of preview pages | Integer |
| sponsoredPageId |  | Sponsored page ID | String |
| instagramSponsoredPageId |  | Instagram-sponsored page ID | String |
| dynamicAdVoice |  | Dynamic ad voice values: DYNAMIC, STORY_OWNER | String |
| destinationObject | type | Type of the destination | String |
|  | url | URL of the destination | String |
|  | storeUrl | Store URL if applicable | String |
|  | appId | Application ID if relevant | String |
| deepLinkDetails | deepLinkType | Type of deep link (ANDROID, WEB, IOS, IPHONE, IPAD, APP, WINDOW) | String |
|  | packageName | Android package name | String |
|  | url | Deep link URL | String |
|  | appName | Name of the application | String |
|  | webUrl | Web URL | String |
|  | webFallBack | Fallback URL for web | String |
|  | appId | Application ID | String |
|  | appStoreId | Application store ID | String |
|  | configAppId | Configuration App ID | String |
| carouselObjects (List<AdChildMedia>) | title | Card/Media Title | String |
|  | description | Card/Media Description | String |
|  | linkUrl | Card/Media Link URL | String |
|  | appLink | Application-specific link (if applicable) | String |
|  | imageUrl | Card/Media Image URL | String |
|  | videoUrl | Card/Media Video URL (pass thumbnail URL in imageUrl) | String |
|  | callToAction | Call-to-action text or identifier | String |
|  | destinationObject | Destination object containing navigation details | ApiDestinationObject |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/supported/cta' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}'\
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "channelType": "FACEBOOK",
    "accountUserId": "394232028806869",
    "objective": "OUTCOME_TRAFFIC",
    "postTypes": "LINK",
    "buyingType": "AUCTION",
    "adPlacementDetail": {
                    "publisherPlatforms": [
                        "MESSENGER",
                        "AUDIENCE_NETWORK",
                        "FACEBOOK",
                        "INSTAGRAM"
                    ],
                    "positions": [
                        "INSTAGRAM_STORIES",
                        "INSTAGRAM_EXPLORE",
                        "HOME",
                        "REWARDED_VIDEO",
                        "INSTAGRAM_PROFILE_FEED",
                        "FEED",
                        "FACEBOOK_SEARCH",
                        "FACEBOOK_STORIES",
                        "MESSENGER_STORY",
                        "INSTAGRAM_FEED",
                        "FACEBOOK_REELS_OVERLAY",
                        "FACEBOOK_REELS",
                        "INSTAGRAM_REELS",
                        "INSTAGRAM_EXPLORE_HOME",
                        "CLASSIC",
                        "MARKETPLACE",
                        "INSTREAM_VIDEO"
                    ]}
}'



## Example - Response





{
    "data": {
        "responseEntity": {
            "LEARN_MORE": "Learn More",
            "APPLY_NOW": "Apply Now",
            "GET_QUOTE": "Get Quote",
            "GET_PROMOTIONS": "Get Promotions",
            "NO_BUTTON": "No Button",
            "BUY_NOW": "Buy Now",
            "MESSAGE_PAGE": "Send Message",
            "OPEN_LINK": "Open Link",
            "SEND_UPDATES": "Get Updates",
            "SHOP_NOW": "Shop Now",
            "SUBSCRIBE": "Subscribe",
            "SEE_MENU": "See Menu",
            "GET_OFFER": "Get Offer",
            "SIGN_UP": "Sign up",
            "VIEW_INSTAGRAM_PROFILE": "View Instagram Profile",
            "WATCH_MORE": "Watch More",
            "USE_APP": "Use App",
            "WHATSAPP_MESSAGE": "Send Whatsapp Message",
            "PLAY_GAME": "Play Game",
            "START_ORDER": "Start Order",
            "DONATE_NOW": "Donate Now",
            "REQUEST_TIME": "Request Time",
            "LISTEN_NOW": "Listen Now",
            "PAY_TO_ACCESS": "Get Access",
            "INSTAGRAM_MESSAGE": "Send Instagram Message",
            "USE_MOBILE_APP": "Use Mobile App",
            "DOWNLOAD": "Download",
            "CONTACT_US": "Contact Us",
            "GET_SHOWTIMES": "Get ShowTimes",
            "BOOK_TRAVEL": "Book Now",
            "ORDER_NOW": "Order Now"
        }
    },
    "errors": []
}




### Response Parameters






























| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. | Object |
|  | responseEntities | Object containing response entities. | Array |
| errors |  | Array containing error details, if any. | Array |

### Response Entity Object










































| Parameter | Description | Type |
| --- | --- | --- |
| MESSAGE_PAGE | Send Message | String |
| PLAY_GAME | Play Game | String |
| DOWNLOAD | Download | String |
| SEE_MENU | See Menu | String |
| BOOK_TRAVEL | Book Now | String |
| LISTEN_NOW | Listen Now | String |
| VIEW_INSTAGRAM_PROFILE | View Instagram Profile | String |
| SUBSCRIBE | Subscribe | String |
| PAY_TO_ACCESS | Get Access | String |
| DONATE_NOW | Donate Now | String |
| GET_SHOWTIMES | Get ShowTimes | String |
| INSTAGRAM_MESSAGE | Send Instagram Message | String |
| SEND_UPDATES | Get Updates | String |
| WHATSAPP_MESSAGE | Send Whatsapp Message | String |
| WATCH_MORE | Watch More | String |
| LEARN_MORE | Learn More | String |
| ORDER_NOW | Order Now | String |
| REQUEST_TIME | Request Time | String |
| START_ORDER | Start Order | String |
| GET_QUOTE | Get Quote | String |
| GET_OFFER | Get Offer | String |
| OPEN_LINK | Open Link | String |
| SHOP_NOW | Shop Now | String |
| USE_APP | Use App | String |
| USE_MOBILE_APP | Use Mobile App | String |
| APPLY_NOW | Apply Now | String |
| SIGN_UP | Sign up | String |
| NO_BUTTON | No Button | String |
| BUY_NOW | Buy Now | String |
| CONTACT_US | Contact Us | String |
| GET_PROMOTIONS | Get Promotions | String |

[](https://dev.sprinklr.com/fetch-supported-cta-options) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-supported-cta-options)
