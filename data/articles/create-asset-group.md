---
title: "Create Asset Group"
slug: create-asset-group
url: https://dev.sprinklr.com/create-asset-group
---

# Create Asset Group

#
  POST Create Asset Group

You can create an Asset group via this API call and you will get the Id and other related objects as Response after making the Request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/asset-group

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

###  Request Parameters



































































































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | Name of the group. | String |
| description | Required | Description of the group. | String |
| clientId | Required | The client id in which to make the changes 				You can find the client id with the Bootstrap endpoint in API 1.0 using types=CLIENTS | String |
| assetId | Required | Asset Id's in the group | String |
| clientCustomFields | Optional | Client level custom fields of the group. | String |
| partnerCustomFields | Optional | Partner level custom fields of the group. | String |
| groupType | Required | Type of the group (Static/Dynamic). | String |
| assetType | Required | Asset Type of the group.  Enum: [ USER, BRAND, ACCOUNT, CLIENT, BENCHMARKING_ACCOUNT ] | String |
| assetPermissions | Optional | Asset Permission assigned to the group | String |
| type | Required | Type e.g. USER, GLOBAL, CLIENT | String |
| ids | Optional | IDs based on type. | String |
| subscribers | Optional | Subscribers of the group | String |
| type | Required | Type e.g. USER, GLOBAL, CLIENT | String |
| ids | Optional | IDs based on type. | String |

## Example - Request














Copy Code




	 curl -X POST \
   https://api3.sprinklr.com/{env}/api/v2/asset-group \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
 {
  "name": "string",
  "description": "string",
  "clientId": 0,
  "assetIds": [
    "string"
  ],
  "clientCustomFields": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  },
  "partnerCustomFields": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  },
  "groupType": "DYNAMIC",
  "assetType": "USER",
  "assetPermissions": [
    {
      "type": "string",
      "ids": [
        "string"
      ]
    }
  ],
  "subscribers": [
    {
      "type": "string",
      "ids": [
        "string"
      ]
    }
  ]
}'





## Example - Response





{
  "id": "string",
  "name": "string",
  "description": "string",
  "assetIds": [
    "string"
  ],
  "clientCustomFields": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  },
  "partnerCustomFields": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  },
  "createdTime": 0,
  "modifiedTime": 0,
  "ownerUserId": 0,
  "clientId": 0,
  "deleted": false,
  "groupType": "DYNAMIC",
  "assetType": "USER",
  "assetPermissions": [
    {
      "type": "string",
      "ids": [
        "string"
      ]
    }
  ],
  "subscribers": [
    {
      "type": "string",
      "ids": [
        "string"
      ]
    }
  ]
}





### Response Definition











































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id of the asset group. | String |
| name | Name of the group. | String |
| description | Description of the group. | String |
| assetId | Asset Id's in the group | String |
| clientCustomFields | Client level custom fields of the group. | String |
| partnerCustomFields | Partner level custom fields of the group. | String |
| createdTime | Time of creation of the asset group. | Epoch |
| modifiedTime | Time of creation of the asset group. | Epoch |
| ownerUserId | Owner of the group. | Integer |
| spaceId | Client id of the group. | Integer |
| deleted | Is the group deleted. | Boolean |
| groupType | Type of the group (Static/Dynamic). | String |
| assetType | Asset Type of the group.  Enum: [ USER, BRAND, ACCOUNT, CLIENT, BENCHMARKING_ACCOUNT ] | String |
| assetPermissions | Asset Permission assigned to the group | String |
| type | Type e.g. USER, GLOBAL, CLIENT | String |
| ids | IDs based on type. | String |
| subscribers | Subscribers of the group | String |
| type | Type e.g. USER, GLOBAL, CLIENT | String |
| ids | IDs based on type. | String |

	 [](https://dev.sprinklr.com/create-asset-group)




[Back to top](https://dev.sprinklr.com/create-asset-group)
