---
title: "Fetch Facebook Ads Account Details for Paid Initiatives "
slug: fetch-facebook-ads-account-details-for-paid-initiatives
url: https://dev.sprinklr.com/fetch-facebook-ads-account-details-for-paid-initiatives
---

# Fetch Facebook Ads Account Details for Paid Initiatives 

#  POST  Fetch Facebook Ads Account Details for Paid Initiatives


Use this API to retrieve Facebook Ads account details required for managing paid initiatives within Sprinklr. The API returns key account-level information such as account ID, name, status, etc.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/instagram/accounts

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
| accountUserId | integer | Yes | Account ID of the Facebook Ads account. |
| pageId | string | No | Identifier of the linked business page. |


## Example Request

Copy Code


curl --location --globoff 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/instagram/accounts' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {API_Key}' \
--data '{
        "pageId": "0",
        "accountUserId":"2040369466198246"
}'

## Example - Response


{ 
    "data": { 
        "userAccountDTOS": [ 
            { 
                "account": { 
                    "accountId": -1747123755, 
                    "accountType": "INSTAGRAM", 
                    "accountUserId": "17841400826158211", 
                    "screenName": “name”, 
                    "displayName": “name”, 
                    "isActive": true, 
                    "snType": "INSTAGRAM", 
                    "isDeleted": false, 
                    "isGrabbingDisabled": false, 
                    "isVariant": false, 
                    "profileImgUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t51.2885-15/12142450_157279231293241_2115688096_a.jpg?_nc_cat=1&ccb=1-7&_nc_sid=7d201b&_nc_ohc=SeMNwbNuQKMQ7kNvwE2zu8V&_nc_oc=AdnnagOv-mPx6UaaQTnCD7e9Z5sfYu6jMzytxnGqgLOrh2xKtIwCa3ueHKelJ9fLUDU&_nc_zt=23&_nc_ht=scontent-bom2-1.xx&edm=AFBc56wEAAAA&oh=00_AfVATEuBnWP5HuF50jpS714Owsz7HjbNooczcI-UrVl2ZA&oe=689A3649", 
                    "report": "ACCOUNT" 
                }, 
                "type": "PAGE" 
            } 
        ] 
    }, 
    "errors": [] 
}

### Response Schema






























| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | Object | Contains the API response data.. |
|  | userAccountDTOS | array of objects | List of connected user account objects. |
| errors |  | array | List of errors, if any. |

#### userAccountDTOS Object
































































































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| account |  | object | Contains metadata for the connected account. |
|  | accountId | number | Account ID used for paid publishing. |
|  | accountType | string | Type of account (e.g., INSTAGRAM) |
|  | accountUserId | string | Social network user ID. |
|  | screenName | string | Screen name of the account. |
|  | displayName | string | Display name of the account. |
|  | isActive | boolean | Indicates if the account is active. |
|  | snType | string | Social network type (e.g., INSTAGRAM). |
|  | isDeleted | boolean | Indicates if the account is deleted. |
|  | isGrabbingDisabled | boolean | Indicates if data grabbing is disabled for the account. |
|  | isVariant | boolean | Indicates if the account is a variant. |
|  | profileImgUrl | string (URL) | URL of the account’s profile image. |
|  | report | string | Report type for the account (e.g., ACCOUNT). |
| type |  | string | Type of entity (e.g., PAGE). |

[](https://dev.sprinklr.com/fetch-facebook-ads-account-details-for-paid-initiatives)

[Back to top](https://dev.sprinklr.com/fetch-facebook-ads-account-details-for-paid-initiatives)
