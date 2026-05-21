---
title: "Create User (SCIM)"
slug: create-user-scim
url: https://dev.sprinklr.com/create-user-scim
---

# Create User (SCIM)

# POST Create User (SCIM)

Using this API, you can create/add a user within the Sprinklr platform. Kindly note that the Kindly username, i.e., the user email is the unique identifier when creating a user.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/Users

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/scim+json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

## Request Parameters

The following table describes the Request Parameters in use.





























































			****






			****



| Parameters | Sub-Parameter | Required | Description | Type |
| --- | --- | --- | --- | --- |
| userName |  | Required | The email Id of the user.The email of the user needs to be unique every time you hit the create user API | String |
| name |  | Required | Object that specifies the familyName and givenName | Object |
|  | familyName | Required | Refers to the last name of the user | String |
|  | givenName | Required | Refers to the first name of the user | String |
| photos |  | Optional | Array of photos, but Sprinklr will use the first one only. | Array |
|  | value | Optional | Refer to the url for the photo | URL |
| active |  | Optional | If true, the user will be set to active state | Boolean |
| isSpaceUser |  | Optional | If true, the user can access Space UI only | Boolean |
| locale |  | Optional | Refers to the language code of the userRefer to the table below for common language codes | String |
| globalAttributes |  | Optional | The global attributes of the user. Kindly check the Custom Global Attributes Description Table below. | Object |
| clientAttributes |  | Required | The client-level attributes of the user. Kindly check the Client Attributes Description Table below. | Array |

## Global Attributes Object - Description Table

The following table describes the parameters within globalAttributes object that can be used in Request Payload.





















****













			````




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| partnerCustomProperties | Optional | Refers to the global-level custom properties. | Object |
| productSeat | Optional | Refers to the product seat you want to assign to the userSupported Product Seats:Modern Engagement, Modern Marketing, Modern Care, Modern Marketing Lite, DistributedBy default, the user falls under the Modern Engagement product seat | String |
| federationId | Optional | Assigning a Federation ID helps with unique identification. You cannot assign the same federation identity to more than one user The federation ID is additionally used by Customer Environments for attaching extra SSO Login information | String |
| passwordLoginDisabled | Optional | By default false, In case of SSO user this need to be true along with federationId. | Boolean |

## Client Attributes Array - Description Table

The following table describes the parameters within clientAttributes object that can be used in Request Payload.
























****``









































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| clientId |  | Required | Refers to the workspace Id where you want to add the user | Integer |
| userType |  | Required | The type of user you want to create.Supported user types:PARTNER_ADMIN, PARTNER_USER,    CLIENT_ADMIN, CLIENT_USER | String |
| phoneNumbers |  | Optional | Array containing phone details. | Array |
|  | value | Optional | Refers to the phone number of the user | String |
|  | type | Optional | Refers to the type of phone number, i.e., whether it is for work or personal | String |
|  | primary | Optional | If true, the phone number is primary to the user | Boolean |
| clientCustomProperties |  | Optional | The workspace level custom properties. | Object |
| businessCategory |  | Optional | The category of business.Either CORPORATE or DISTRIBUTED | String |
| designation |  | Optional | Refers to the designation of user. | String |
| department |  | Optional | Refers to the department of user. | String |
| managerId |  | Optional | User ID of the user's manager. | integer |
| persona |  | Optional | The persona assigned to the user (e.g., ML Annotator). | string |
| personaViewEnabled |  | Optional | Indicates whether persona-based view is enabled for the user. | boolean |
| personaApp |  | Optional | Name of the application linked to the user's persona. | String |
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

## Example - Request



 Copy Code



curl -X POST \
  'https://api2.sprinklr.com/{env}/api/v2/scim/Users' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "userName": "ben.turner+scimapi@sprinklr.com",
    "name": {
        "familyName": "Ben",
        "givenName": "Turner"
    },
        "locale": "EN_US",
        "globalAttributes": {
            "partnerCustomProperties": {
                "58f7681be4b027b9a722d5c5": [
                    "pp"
                      ],
                "5b1006f1e4b0a54914f86e45": [
                    "Yes"
                ]
            },
            "federationId": "",
            "passwordLoginDisabled": false
        },
        "clientAttributes": [
            {
                "clientId": 1000004509,
                "userType": "CLIENT_ADMIN",
                "phoneNumbers": [
                    {
                        "value": "+919123456789"
                    }
                ],
                "businessCategory": "CORPORATE",
                "clientCustomProperties": {
                    "580745abe4b027d61cf738d8": [
                        "5"
                    ]
                },
                "designation": "test",
                "department": "test"
            },
            {
                "clientId": 1000004510,
                "userType": "CLIENT_ADMIN",
                "phoneNumbers": [
                    {
                        "value": "+919123456789"
                    }
                ],
                "businessCategory": "CORPORATE",
                "userGroupIds": [
            ],
            "clientCustomProperties": {

            },
            "designation": "test",
            "department": "test"
        }
    ]

}'



## Example - Response




{
   {
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "id": "66008997",
    "userName": "testuser@sprinklr.com",
    "name": {
        "familyName": "Test",
        "givenName": "User"
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
            "clientId": 66000002,
            "userType": "CLIENT_USER",
            "phoneNumbers": [
                {
                    "value": "+919123456789"
                }
            ],
            "businessCategory": "CORPORATE",
            "userGroupIds": [
                "653fc0293618cc7784db2976"
            ],
            "clientCustomProperties": {},
            "designation": "test",
            "department": "test"
        }
    ],
    "meta": {
        "resourceType": "User",
        "location": "/api/scim/Users66008997"
    },
    "emails": [
        {
            "value": "testuser361@sprinklr.com",
            "primary": true
        }
    ]
}

[](https://dev.sprinklr.com/create-user-scim) 

 

 
[Back to top](https://dev.sprinklr.com/create-user-scim)
