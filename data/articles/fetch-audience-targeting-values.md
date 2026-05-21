---
title: "Fetch Audience Targeting Values"
slug: fetch-audience-targeting-values
url: https://dev.sprinklr.com/fetch-audience-targeting-values
---

# Fetch Audience Targeting Values

#  POST  Fetch Audience Targeting Values

Use this endpoint to retrieve available audience targeting options associated with a specific ad account user. These values are typically used when building or previewing audience targeting configurations during campaign creation.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/audience/values

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















































| Field | Type | Required | Description |
| --- | --- | --- | --- |
| accountUserId | string | Yes | Unique identifier of the user associated with the ad account. |
| type | String (Enum) | Yes | The targeting field type. |
| keyword | String | Yes | Search keyword for audience targeting. |
| excluded | Boolean | No | Whether to exclude results. |
| exclusionMode | Boolean | No | Whether to enable exclusion mode. |
| alwaysEnableOptions | Boolean | No | Whether to always enable options. |
| forSegmentAssetCustomization | Boolean | No | Whether the search is for segment asset customization. |
| limit | Integer | No | The maximum number of results to return. |
| offset | Integer | No | The offset for pagination. |

## Steps to Retrieve `accountUserId`


- In Sprinklr, click the **New Page (+)** icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the Accounts page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the **User ID** column. This value corresponds to the `accountUserId`.

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/audience/values' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
      "accountUserId": "549757105401",
      "keyword": "game",
      "type": "KEYWORDS",
      "excluded": "false",
      "exclusionMode": "false",
      "alwaysEnableOptions": "true",
      "forSegmentAssetCustomization": "true",
      "limit": "10",
      "offset": "10"
  }'

## Example - Response


{
    "data": {
        "audienceTargetFieldOptions": [
            {
                "key": "game",
                "label": "game"
            }
        ]
    },
    "errors": []
}

### Response Schema






























| Field | Sub Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | object | Contains the response data. |
|  | audienceTargetFieldOptions | array of objects | List of available audience targeting field options. |
| errors |  | array | List of errors, if any. |

#### audienceTargetFieldOptions Object





















| Field | Type | Description |
| --- | --- | --- |
| key | string | Internal identifier for the targeting field. |
| lable | string | Display name for the targeting field. |

[](https://dev.sprinklr.com/fetch-audience-targeting-values)

[Back to top](https://dev.sprinklr.com/fetch-audience-targeting-values)
