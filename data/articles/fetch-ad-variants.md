---
title: "Fetch Ad Variants"
slug: fetch-ad-variants
url: https://dev.sprinklr.com/fetch-ad-variants
---

# Fetch Ad Variants

#   POST Fetch Ad Variants
 

This API allows you to fetch a paginated list of ad variants associated with a given account.


**Related Knowledge Base Article: **[Ad Variant](https://www.sprinklr.com/help/articles/sprinklr-marketing-glossary/ad-variant/641497432680c35a78bc5173)


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/get/adVariants

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














[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-ad-variants#account_userid)



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


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/get/adVariants' \
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
                "id": "684c0e5804a3dc4783612e1f",
                "name": "Media Catalog",
                "creativeObject": {
                    "name": "catalog",
                    "postType": "TEMPLATE_DATA",
                    "isDarkPost": true,
                    "pageId": "425005714027650",
                    "secondaryPageId": "17841461320091337",
                    "title": "Bulk {{product.price}}",
                    "description": "Bulk {{product.brand}}",
                    "linkUrl": "https://www.acmesprinklr.com/",
                    "linkDescription": "bulk {{product.price}}",
                    "callToAction": "ORDER_NOW",
                    "destinationObject": {
                        "type": "WEBSITE",
                        "url": "https://www.acmesprinklr.com/"
                    },
                    "deepLinkDetails": {
                        "deepLinkType": "IOS",
                        "webUrl": "{{product.url}}"
                    },
                    "forceSingleLink": true,
                    "productSetChannelId": "3322153764754822",
                    "multiAdvertiserAd": false
                }
            },
            {
                "id": "684c0e5804a3dc4783612e1d",
                "name": "Carousel Ad",
                "creativeObject": {
                    "postType": "LINK",
                    "isDarkPost": true,
                    "pageId": "425005714027650",
                    "secondaryPageId": "17841461320091337",
                    "title": "Rathi page 3",
                    "description": "latest products at http://www.sprinklr.com?adChannelId=120223652357610569&test=true",
                    "linkUrl": "https://www.acmesprinklr.com/?adChannelId=120223652357610569&test=true",
                    "linkDescription": "",
                    "displayLink": "https://www.acmesprinklr.com",
                    "callToAction": "WATCH_MORE",
                    "destinationObject": {
                        "type": "WEBSITE",
                        "url": "https://www.acmesprinklr.com/?adChannelId=120223652357610569&test=true"
                    },
                    "deepLinkDetails": {
                        "deepLinkType": "IOS"
                    },
                    "forceSingleLink": false,
                    "carouselObjects": [
                        {
                            "title": "headline one",
                            "description": "desc one",
                            "linkUrl": "https://www.acmesprinklr.com/?adChannelId=120223652357610569&test=true",
                            "imageUrl": "https://pz.cdata.prod0.sprinklr.com/PAID/9004/3e4c5f2e-8c90-4b23-8582-a1a01a3b62aa-879288554/image.png"
                        },
                        {
                            "title": "headline two",
                            "description": "desc two",
                            "linkUrl": "https://www.acmesprinklr.com/?adChannelId=120223652357610569&test=true",
                            "imageUrl": "https://pz.cdata.prod0.sprinklr.com/PAID/9004/87ae04fb-c1f7-49b0-a371-f7042bb13130-879294258/image.jpg"
                        },
                        {
                            "title": "headline three",
                            "description": "desc three",
                            "linkUrl": "https://www.acmesprinklr.com/?adChannelId=120223652357610569&test=true",
                            "imageUrl": "https://pz.cdata.prod0.sprinklr.com/PAID/9004/c822c369-5f0a-4943-8154-c47084e235c3-879294258/image.jpg"
                        },
                        {
                            "title": "headline four",
                            "description": "desc four",
                            "linkUrl": "https://www.acmesprinklr.com/?adChannelId=120223652357610569&test=true",
                            "imageUrl": "https://pz.cdata.prod0.sprinklr.com/PAID/9004/ec897304-429b-43eb-8b7e-93acfb7315e6-879288554/image.png"
                        },
                        {
                            "title": "headline five",
                            "description": "desc five",
                            "linkUrl": "https://www.acmesprinklr.com/?adChannelId=120223652357610569&test=true",
                            "imageUrl": "https://pz.cdata.prod0.sprinklr.com/PAID/9004/ce802224-8c21-4b00-bcb1-05bd70d79fa6-879288554/image.png"
                        }
                    ],
                    "multiAdvertiserAd": false
                },
                "trackingPixelChannelIds": [
                    "526418185586840"
                ],
        "errors": []
    },
    "errors": []
}




### Response Parameters































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. |  |
|  | adEntities | Object containing ad variant objects.See the Ad Variant table below. | Object |
| errors |  | Array containing error details, if any. | Array |


### Ad Variant Object
































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the ad variant | String |
| name | Name of the ad variant | String |
| creativeObject | The creative associated with the adSee the Creative Object table below | Object |
| trackingPixelChannelIds | Tracking pixel channel identifiers | List<String> |


### Creative Object







































































































































































































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| name |  | Name of the creative | String |
| creativeId |  | Unique identifier for the creative | String |
| postType |  | Type of the post | String |
| isDarkPost |  | Whether it is a dark post | Boolean |
| pageId |  | ID of the associated page | String |
| secondaryPageId |  | ID of the secondary page/Instagram Page | String |
| postChannelId |  | ID of the post channel | String |
| title |  | Title of the creative | String |
| description |  | Description of the creative | String |
| linkUrl |  | URL link in the creative | String |
| linkDescription |  | Description for the link | String |
| displayLink |  | Display link | String |
| imageUrl |  | URL of the image | String |
| videoUrl |  | URL of the video | String |
| callToAction |  | Call to action text | String |
| leadFormId |  | Lead form ID | String |
| previewPageCount |  | Number of preview pages | Integer |
| sponsoredPageId |  | Sponsored page ID | String |
| instagramSponsoredPageId |  | Instagram-sponsored page ID | String |
| dynamicAdVoice |  | Dynamic ad voice values | String |
| isStoreVisitCreative |  | Whether it is a store visit creative | Boolean |
| destinationObject |  | Destination details | Object |
|  | type | Type of the destination | String |
|  | url | URL of the destination | String |
|  | pageWelcomeMessage | Welcome message for the page | String |
|  | phoneNumber | Contact phone number | String |
|  | storeUrl | Store URL if applicable | String |
|  | appId | Application ID if relevant | String |
| deepLinkDetails |  | Deep linking information | Object |
|  | deepLinkType | Type of deep link | String |
|  | packageName | Android package name | String |
|  | url | Deep link URL | String |
|  | appName | Name of the application | String |
|  | webUrl | Web URL | String |
|  | webFallBack | Fallback URL for web | String |
|  | appId | Application ID | String |
|  | appStoreId | Application store ID | String |
|  | configAppId | Configuration App ID | String |
| forceSingleLink |  | Force single link usage | Boolean |
| carouselObjects |  | List of carousel media objects | Array |
|  | title | Card/Media Title | String |
|  | description | Card/Media Description | String |
|  | linkUrl | Card/Media Link URL | String |
|  | appLink | Application-specific link | String |
|  | imageUrl | Card/Media Image URL | String |
|  | videoUrl | Card/Media Video URL | String |
|  | callToAction | Call-to-action text or identifier | String |

[](https://dev.sprinklr.com/fetch-ad-variants) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-ad-variants)
