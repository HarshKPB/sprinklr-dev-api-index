---
title: "Fetch Connection Objects"
slug: fetch-connection-objects
url: https://dev.sprinklr.com/fetch-connection-objects
---

# Fetch Connection Objects

#  POST Fetch Connection Objects

This API retrieves connection objects associated with a board, account user, and social page account. This endpoint is typically used in Ads Publishing workflows to retrieve objects required for configuring campaign components such as Pins, Boards, or Ad Sets on platforms like Pinterest.


## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/connectionObjects

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
| accountUserId | string | Yes | Unique identifier of the user account used for ad publishing. |
| boardId | string | No | ID of the board (typically used in platforms like Pinterest). |
| socialPageAccountUserId | string | No | ID of the social page account linked to the user account. |
| connectionObjectType | String (Enum) | No | The type of connection object. Supported Enum values: |
| activeOnly | Boolean | No | Whether to filter only active objects. |

## Steps to Retrieve `accountUserId`


- In Sprinklr, click the **New Page (+)** icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the Accounts page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the **User ID** column. This value corresponds to the `accountUserId`.

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/connectionObjects' \
--header 'Authorization: Bearer {Token}' \
--header 'Key: {Api_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "accountUserId":"549757105401",
    "boardId":"526076868911658396",
    "socialPageAccountUserId":"600003045"
}'

## Example - Response


{
    "data": {
        "responseEntities": [
            {
                "accountId": 66001282,
                "id": "PINTEREST_PINTEREST_BOARD_526076868912249431_66001282",
                "channelId": "526076868912249431",
                "channelType": "PINTEREST",
                "type": "PINTEREST_BOARD",
                "pageId": "526076937630787631",
                "name": "new board 123",
                "deleted": false,
                "status": "ACTIVE",
                "hasDSCPermission": false,
                "additional": {
                    "privacy": "PUBLIC"
                }
            },
            {
                "accountId": 66001282,
                "id": "PINTEREST_PINTEREST_BOARD_526076868912249450_66001282",
                "channelId": "526076868912249450",
                "channelType": "PINTEREST",
                "type": "PINTEREST_BOARD",
                "pageId": "526076937630787631",
                "name": "sample wdefr edfrgwdefr ",
                "deleted": false,
                "status": "ACTIVE",
                "hasDSCPermission": false,
                "additional": {
                    "privacy": "PUBLIC"
                }
            },
            {
                "accountId": 66001282,
                "id": "PINTEREST_PINTEREST_BOARD_526076868912249731_66001282",
                "channelId": "526076868912249731",
                "channelType": "PINTEREST",
                "type": "PINTEREST_BOARD",
                "pageId": "526076937630787631",
                "name": "Summer Recipes",
                "deleted": false,
                "status": "ACTIVE",
                "hasDSCPermission": false,
                "additional": {
                    "privacy": "PROTECTED"
                }
            },
            {
                "accountId": 66001282,
                "id": "PINTEREST_PINTEREST_BOARD_526076868912249739_66001282",
                "channelId": "526076868912249739",
                "channelType": "PINTEREST",
                "type": "PINTEREST_BOARD",
                "pageId": "526076937630787631",
                "name": "sample",
                "deleted": false,
                "status": "ACTIVE",
                "hasDSCPermission": false,
                "additional": {
                    "privacy": "PROTECTED"
                }
            },
            {
                "accountId": 66001282,
                "id": "PINTEREST_PINTEREST_BOARD_526076868912250010_66001282",
                "channelId": "526076868912250010",
                "channelType": "PINTEREST",
                "type": "PINTEREST_BOARD",
                "pageId": "526076937630787631",
                "name": "Sprinklr Ads New Board For shared testing",
                "deleted": false,
                "status": "ACTIVE",
                "hasDSCPermission": false,
                "additional": {
                    "privacy": "PROTECTED"
                }
            },
            {
                "accountId": 66001282,
                "id": "PINTEREST_PINTEREST_BOARD_526076868912250039_66001282",
                "channelId": "526076868912250039",
                "channelType": "PINTEREST",
                "type": "PINTEREST_BOARD",
                "pageId": "526076937630787631",
                "name": "sa123",
                "deleted": false,
                "status": "ACTIVE",
                "hasDSCPermission": false,
                "additional": {
                    "privacy": "PROTECTED"
                }
            }
        ]
    },
    "errors": []
}

## Response Schema






























| Field | Sub Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | object | Contains the list of response entities. |
| data | responseEntities | array of objects | List of connection objects associated with the specified board, account, and user. |
| errors |  | array | List of errors, if any. |

### responseEntities Object

Each object in the `responseEntities` array represents a connection object (e.g., a Pinterest board).


































































| Field | Type | Description |
| --- | --- | --- |
| accountId | number | ID of the ad account associated with the board. |
| id | string | Unique identifier for the connection object. |
| channelId | string | ID of the social media channel (e.g., Pinterest board ID). |
| channelType | string | Type of the social platform (e.g., PINTEREST). |
| type | string | Object type (e.g., PINTEREST_BOARD). |
| pageId | string | ID of the social page linked to the board. |
| name | string | Name of the board or connection object. |
| deleted | boolean | Indicates whether the board is deleted (true or false). |
| status | string | Status of the board (e.g., ACTIVE). |
| hasDSCPermission | boolean | Whether the board has DSC (Dynamic Social Creative) permission. |
| additional | object | Contains additional metadata for the object. |

[](https://dev.sprinklr.com/fetch-ad-user-accounts)

[Back to top](https://dev.sprinklr.com/fetch-ad-user-accounts)
