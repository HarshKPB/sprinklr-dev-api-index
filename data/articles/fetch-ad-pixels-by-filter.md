---
title: "Fetch Ad Pixels by Filter "
slug: fetch-ad-pixels-by-filter
url: https://dev.sprinklr.com/fetch-ad-pixels-by-filter
---

# Fetch Ad Pixels by Filter 

#  POST  Fetch Ad Pixels by Filter

An Ad Pixel is a small piece of code that places a blank 1x1 pixel image on your website and allows website owners to track user behavior on their website. The pixel is placed on the website and is triggered when a user performs a specific action. Using this API, you can fetch the details of all Ad Pixels on the environment created by an Account using the Account ID.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/pixelsByFilter

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

### Request Body Parameters
























| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| accountUserId | integer | Yes | Unique Account ID used to create the Ad Pixel. |
| pixelTypes | string | No | Fetch Ad Pixels of the specified type. |

## Example Request

Copy Code


curl --location --globoff 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/pixelsByFilter' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Token}' \
--header 'Key: {API_Key}' \
--data '    {
        "accountUserId": "394232028806869",
        "pixelTypes": "CUSTOM_CONVERSION"
} '


## Example - Response


{
    "data": {
        "responseEntities": [
            {
                "id": "FACEBOOK_66122206_1274549753655107",
                "accountId": 66122206,
                "channelId": "1274549753655107",
                "channelType": "FACEBOOK",
                "pixelType": "CUSTOM_CONVERSION",
                "pixelTypeLabel": "Custom Conversion",
                "name": "Sample FB Pixel_edited",
                "description": "Sample Description",
                "type": "COMPLETE_REGISTRATION",
                "jsPixel": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

## Response Schema






























| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | array | Contains the main data objects. |
|  | responseEntities | array of objects | List of all Ad Pixel details. |
| errors |  | array | List of errors, if any. |

### responseEntities Description Table




































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| id |  | string | A combination of the Channel Type, Account ID, and Channel ID. |
| accountId |  | integer | Account ID used for paid publishing. |
| channelId |  | integer | Identifier for the Ad channel. |
| channelType |  | string | Name of the channel associated with the Ad Pixel. |
| pixelType |  | string | CUSTOM_CONVERSION, FACEBOOK_PIXEL, and so on. It varies with the associated Channel Type. |
| pixelTypeLabel |  | string | Custom Conversion, Facebook Pixel, and so on. It varies with the associated Channel Type. |
| name |  | string | Name of the Ad Pixel. |
| type |  | string | Type of Ad Pixel. |
| jsPixel |  | string | - |
| lastVerified |  | string | The timestamp of the most recent verification event in ISO 8601 format (UTC). |
| firstVerified |  | string | The timestamp of the first verification event in ISO 8601 format (UTC). |
| createdTime |  | integer | Shows the epoch timestamp when the Ad Pixel was created. |
| isArchived |  | boolean | Indicates whether the Ad Pixel has been archived (true) or not (false). |
| retargetingEnabled |  | boolean | Indicates whether retargeting has been enabled (true) or not (false). |
| parentChannelId |  | integer | Unique ID of the parent channel used to create the Ad Pixel. |
| parentPixelName |  | string | Name of the parent channel used to create the Ad Pixel. |
| rule |  | string | Inclusion rules target events. |
| ruleObject |  | object | A structured representation of logical rules used for audience segmentation. |
|  | type | string | The logical operator at the top level of the rule object (e.g., AND, OR). |
|  | childRules | array | An array of nested rule groups defining logical conditions. |
|  | options | array of objects | A list of condition objects specifying the key, operator, and values. |
| pixelDataSources |  | array | A list of data sources associated with tracking pixels. |
|  | id | integer | The unique identifier of the pixel data source. |
|  | sourceType | string | The type of the data source. |


### options (under ruleObject) Description Table










































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| key |  | object | The key used in the condition, including its name and value. |
|  | name | string | The name of the key used in the condition (e.g., URL). |
|  | value | string | The actual value of the key used in the condition. |
| operator |  | object | The operator used to evaluate the condition. |
| values |  | array | A list of values used in the condition. |

[](https://dev.sprinklr.com/fetch-ad-pixels-by-filter)

[Back to top](https://dev.sprinklr.com/fetch-ad-pixels-by-filter)
