---
title: "Create/Update User"
slug: create-update-user
url: https://dev.sprinklr.com/create-update-user
---

# Create/Update User

#
  POST - Create/Update User

Using this API, you can create a user or update details for an existing user. If the user name (email) in the API request is unique, the API will create the user. Else, the existing user details will get updated.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/upsert

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/scim+json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

## Request Parameters












































































| Parameters | Sub-Parameter | Required | Description | Type |
| --- | --- | --- | --- | --- |
| userName |  | Required | Refers to the email Id of the userIf the username is unique — a new user will be created AND If the username already exists — user details will be updated | String |
| name |  | Required | Object that specifies the familyName and givenName | Object |
|  | familyName | Required | Refers to the last name of the user | String |
|  | givenName | Required | Refers to the first name of the user | String |
| photos |  | Optional | Refers to the array of photos. However, Sprinklr will always use the first photo passed in the request payload | Array |
|  | value | Optional | Refer to the url for the photo | URL |
| active |  | Optional | If true, the user will be set to active state | Boolean |
| isSpaceUser |  | Optional | If true, the user can access Space UI only.Set it to false to create a "Distributed" user | Boolean |
| locale |  | Optional | Refers to the language code of the userRefer to the table below for common language codes | String |
| globalAttributes |  | Optional | Refers to the properties of the user at the partner levelRefer to the table below for globalAttributes object description | Object |
| clientAttributes |  | Required | Refers to the properties of the user at the workspace levelRefer to the table below for clientAttributes object description | Array |

## Global Attributes Object - Description Table



















			****``````````












			````




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| partnerCustomProperties | Optional | Refers to the custom properties of the user at partner level. You can “set” or “unset” partner custom properties when updating a user using this API | key and value pair object |
| productSeat | Optional | Refers to the product seat the user will occupySupported Product Seats:Modern Engagement, Modern Marketing, Modern Care, Modern Marketing Lite, DistributedBy default, the user falls under the Modern Engagement product seat | String |
| federationId | Optional | Assigning a Federation ID helps with unique identification. You cannot assign the same federation identity to more than one user. The federation ID is additionally used by Customer Environments for attaching extra SSO Login information | String |
| passwordLoginDisabled | Optional | By default false, In case of SSO user this need to be true along with federationId | Boolean |

## Client Attributes Array - Description Table

The following table describes the parameters within clientAttributes object that can be used in Request Payload.
























****






















































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| clientId |  | Required | Refers to the workspace Id where you want to add the user | Integer |
| userType |  | Required | The type of user you want to create.Supported user types: PARTNER_ADMIN, PARTNER_USER,    CLIENT_ADMIN, CLIENT_USER | String |
| phoneNumbers |  | Optional | Array containing phone details. | Array |
|  | value | Optional | Refers to the phone number of the user | String |
|  | type | Optional | Refers to the type of phone number, i.e., whether it is for work or personal | String |
|  | primary | Optional | If true, the phone number is primary to the user | Boolean |
| clientCustomProperties |  | Optional | Refers to the custom properties of the user at workspace levelYou can “set” or “unset” client custom properties when updating a user using this API | key and value pair object |
| businessCategory |  | Optional | The category of business.Either CORPORATE or DISTRIBUTED | String |
| designation |  | Optional | Refers to the designation of user. | String |
| department |  | Optional | Refers to the department of user. | String |
| userGroupIds |  | Optional | The user group Ids where you want to add the user | List [String] |
| primaryUserGroupId |  | Optional | The primary user group id where you want to add the user | String |

**Dev Notes: ** To create Distributed User you can use ` "businessCategory":"DISTRIBUTED"` and `"isSpaceUser":false`.

### Commonly Used locale Codes










| Language | Code |
| --- | --- |
| English (US) | EN_US |
| Deutsch (German) | de_DE |
| Español (Spanish) | es_ES |
| Français (France) | fr_FR |
| Italiano (Italian) | it_IT |
| Português (Brasil) | pt_BR |
| Русский (Russian) | ru_RU |
| (Arabic) | ar_SA |
| (Chinese) | zh_CN |

## Sample Request - Create User














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/scim/upsert' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "userName": "Test+QA@sprinklr.com",
    "name": {
        "familyName": "John",
        "givenName": "Doe"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
        }
    ],
    "active": true,
    "locale": "EN_US",
    "globalAttributes": {
        "partnerCustomProperties": {},
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 1,
            "userType": "PARTNER_ADMIN",
            "phoneNumbers": [
                {
                    "value": "+9189799405"
                }
            ],
            "businessCategory": "CORPORATE",
            "userGroupIds": []
        }
    ]
}'





## Example - Response





{
    "data": {
        "schemas": [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
            "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
            "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
            "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
        ],
        "id": "1244542",
        "userName": "Test+QA@sprinklr.com",
        "name": {
            "familyName": "John",
            "givenName": "Doe"
        },
        "photos": [
            {
                "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
            }
        ],
        "active": true,
        "locale": "EN_US",
        "globalAttributes": {
            "partnerCustomProperties": {},
            "passwordLoginDisabled": false
        },
        "clientAttributes": [
            {
                "clientId": 1,
                "userType": "PARTNER_ADMIN",
                "phoneNumbers": [
                    {
                        "value": "+9189799405"
                    }
                ],
                "businessCategory": "CORPORATE",
                "userGroupIds": []
            }
        ],
        "meta": {
            "resourceType": "User",
            "createdTime": "2023-06-06 06:22:41",
            "lastModified": "2023-06-06 06:23:10",
            "location": "/api/scim/upsert"
        },
        "emails": [
            {
                "value": "Test+QA@sprinklr.com",
                "primary": true
            }
        ]
    },
    "errors": []
}





## Sample Request - Update User














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/scim/upsert' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "userName": "Test+QA@sprinklr.com",
    "name": {
        "familyName": "John",
        "givenName": "Doe"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
        }
    ],
    "active": false,
    "locale": "EN_US",
    "globalAttributes": {
        "partnerCustomProperties": {},
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 1,
            "userType": "PARTNER_USER",
            "phoneNumbers": [
                {
                    "value": "+9189563241"
                }
            ],
            "businessCategory": "CORPORATE",
            "userGroupIds": []
        }
    ]
}'





## Example - Response





{
    "data": {
        "schemas": [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
            "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
            "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
            "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
        ],
        "id": "1244542",
        "userName": "Test+QA@sprinklr.com",
        "name": {
            "familyName": "John",
            "givenName": "Doe"
        },
        "photos": [
            {
                "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
            }
        ],
        "active": false,
        "locale": "EN_US",
        "globalAttributes": {
            "partnerCustomProperties": {},
            "passwordLoginDisabled": false
        },
        "clientAttributes": [
            {
                "clientId": 1,
                "userType": "PARTNER_USER",
                "phoneNumbers": [
                    {
                        "value": "+9189563241"
                    }
                ],
                "businessCategory": "CORPORATE",
                "userGroupIds": []
            }
        ],
        "meta": {
            "resourceType": "User",
            "createdTime": "2023-06-06 06:22:41",
            "lastModified": "2023-06-06 06:23:10",
            "location": "/api/scim/upsert"
        },
        "emails": [
            {
                "value": "Test+QA@sprinklr.com",
                "primary": true
            }
        ]
    },
    "errors": []
}





[](https://dev.sprinklr.com/update-account-custom-properties)




[Back to top](https://dev.sprinklr.com/update-account-custom-properties)
