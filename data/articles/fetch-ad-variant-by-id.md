---
title: "Fetch Ad Variant by Id"
slug: fetch-ad-variant-by-id
url: https://dev.sprinklr.com/fetch-ad-variant-by-id
---

# Fetch Ad Variant by Id

#   POST Fetch AdVariant by Id
 

This API retrieves the details of a specific ad variant using its unique identifier. Ad Variants are the individual advertisements within an ad campaign structure. They can be customized to fit different formats (such as image, video, or carousel ads) or for specific placements (such as mobile or desktop news feed, Instagram, or audience network).


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/get/adVariantByIds

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
















[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-ad-variant-by-id#account_userid)









| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| accountUserId | Required | String | Id of the ad account user.See |
| adEntityIds | Required | String | Ad Variant ID to fetch details for. |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request



 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/get/adVariantByIds' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "accountUserId": "394232028806869",
    "adEntityIds": "6841688ede8f43199833bf4e"
}'



## Example - Response





{
    "data": {
        "adEntities": [
            {
                "id": "6841688ede8f43199833bf4e",
                "name": "Sales Catalog - API Media Ad",
                "creativeObject": {
                    "name": "Creative Media",
                    "postType": "TEMPLATE_DATA",
                    "isDarkPost": true,
                    "pageId": "425005714027650",
                    "secondaryPageId": "9602910379797775",
                    "title": "Updated Price at {{product.price}}",
                    "description": "Updated Brand at {{product.brand}}",
                    "linkUrl": "https://www.acmesprinklr.com/",
                    "linkDescription": "Updated Desc at {{product.brand}}",
                    "callToAction": "SHOP_NOW",
                    "destinationObject": {
                        "type": "WEBSITE",
                        "url": "https://www.acmesprinklr.com/"
                    },
                    "deepLinkDetails": {
                        "deepLinkType": "WEB",
                        "webUrl": "{{product.url}}"
                    },
                    "forceSingleLink": true,
                    "productSetChannelId": "2209640879195270",
                    "multiAdvertiserAd": false
                },
                "trackingPixelChannelIds": [
                    "526418185586840"
                ],
                "campaignGroupId": "120226989230490569",
                "channelCampaignId": "120226989231500569"
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
|  | adEntities | List of ad entities with variant details.See the adVariant table below. | Array of Objects |
|  | errors | List of errors, if any, within the data object. | Array |
| errors |  | List of errors, if any, at the root level. | Array |

### `adEntities` Object









































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of the ad variant. | String |
| name | Name of the ad variant. | String |
| creativeObject | Object containing creative details of the ad. | Object |
| trackingPixelChannelIds | List of tracking pixel channel identifiers. | Array of Strings |
| campaignGroupId | ID of the campaign group. | String |
| channelCampaignId | ID of the campaign in the respective channel. | String |

### `creativeObject`






















































































| Parameter | Description | Type |
| --- | --- | --- |
| name | Name of the creative. | String |
| postType | Type of post (e.g., TEMPLATE_DATA). | String |
| isDarkPost | Indicates if the creative is a dark post. | Boolean |
| pageId | ID of the associated page. | String |
| secondaryPageId | ID of the secondary page, if any. | String |
| title | Title text with dynamic placeholders. | String |
| description | Description text with dynamic placeholders. | String |
| linkUrl | Landing page URL for the ad. | String |
| linkDescription | Description for the link. | String |
| callToAction | Call-to-action type (e.g., SHOP_NOW). | String |
| destinationObject | Object defining ad destination details. | Object |
| deepLinkDetails | Object defining deep link configuration. | Object |
| forceSingleLink | Indicates if the creative enforces a single link. | Boolean |
| productSetChannelId | Identifier for the product set channel. | String |
| multiAdvertiserAd | Indicates if the creative supports multiple advertisers. | Boolean |

### `destinationObject`





















| Parameter | Description | Type |
| --- | --- | --- |
| type | Type of destination (e.g., WEBSITE). | String |
| url | Destination URL for the ad. | String |

### `deepLinkDetails`





















| Parameter | Description | Type |
| --- | --- | --- |
| deepLinkType | Type of deep link (e.g., WEB). | String |
| webUrl | URL for the deep link, often dynamic with placeholders. | String |

[](https://dev.sprinklr.com/fetch-ad-variant-by-id) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-ad-variant-by-id)
