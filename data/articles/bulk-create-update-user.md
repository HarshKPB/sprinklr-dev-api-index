---
title: "Bulk Create/Update User"
slug: bulk-create-update-user
url: https://dev.sprinklr.com/bulk-create-update-user
---

# Bulk Create/Update User

#
  POST - Bulk Create/Update User


Using this API, you can create or update users in bulk. If the user names (emails) in the API request are unique, the API will create the users. Else, the existing users' details will be updated. The users can be added by both sync and async methods. Please refer to the document below for the details regarding the respective methods.

**Difference between sync and async User Creation/Updation**

**Sync Method:** The API will send a request to the server and won't return the response until the server responds. With sync method, the time to execute the API request increases and is susceptible to frequent gateway timeout errors.

**Async Method:** The API will send the request to a server and will return the response, even while it is still waiting the server to respond. The request success/failure can be tracked later on the webhook callback Url using the process id

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/bulk-upsert

**Dev Notes: **It is recommended to create/update using a maximum of 20 users per API call

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












| Parameters | Required | Description | Type |
| --- | --- | --- | --- |
| executeAsync | Required | If false, it implies that you are creating/updating users using sync method | Boolean |
| callbackUrl | OptionalRequired when executeAsync is true | Refers to the callback destination URL where the user API creation success/failure would be sent | String |
| callbackUrlHeaders | OptionalRequired when executeAsync is true | Refers to the custom headers that need to be sent in the response within callback response | Object |
| users | Required | Refers to the array containing the users' details.Kindly refer to the table below for the array details | Array |

## User Array Description Table











































































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





















****
``````````













			````




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| partnerCustomProperties | Optional | Refers to the custom properties of the user at partner level. You can “set” or “unset” partner custom properties when updating a user using this API | key and value pair object |
| productSeat | Optional | Refers to the product seat the user will occupySupported Product Seats:Modern Engagement, Modern Marketing, Modern Care, Modern Marketing Lite, DistributedBy default, the user falls under the Modern Engagement product seat | String |
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
| clientCustomProperties |  | Optional | Refers to the custom properties of the user at workspace level. You can “set” or “unset” client custom properties when updating a user using this API | key and value pair object |
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

## Sample Request - Sync Method














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/scim/bulk-upsert' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "executeAsync": false,
    "users": [
        {
            "userName": "testuser1@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User1"
            },
            "photos": [],
            "active": false,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {
                    "_c_6538e095e326b576ff6ebc4f": "TWO"
                },
                "passwordLoginDisabled": false,
                "productSeat": "MARKETING_CLOUD"
            },
            "clientAttributes": [
                {
                    "clientId": 1000004509,
                    "userType": "PARTNER_ADMIN"
                }
            ]
        },
        {
            "userName": "testuser2@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User2"
            },
            "photos": [],
            "active": true,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {
                    "_c_6538e095e326b576ff6ebc4f": "TWO"
                },
                "passwordLoginDisabled": false,
                "productSeat": "MARKETING_CLOUD"
            },
            "clientAttributes": [
                {
                    "clientId": 1000004509,
                    "userType": "PARTNER_ADMIN"
                }
            ]
        },
        {
            "userName": "testuser3@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User3"
            },
            "photos": [],
            "active": true,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {},
                "passwordLoginDisabled": false,
                "productSeat": "MARKETING_CLOUD"
            },
            "clientAttributes": [
                {
                    "clientId": 1000004509,
                    "userType": "PARTNER_ADMIN"
                }
            ]
        }
    ]
}'





## Example - Response





{
    "data": {
        "processId": "65bcae0bb428181ca8ea988a",
        "users": [
            {
                "schemas": [
                    "urn:ietf:params:scim:schemas:core:2.0:User",
                    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                    "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                    "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
                    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
                ],
                "id": "1000263189",
                "userName": "testuser1@sprinklr.com",
                "name": {
                    "familyName": "Test",
                    "givenName": "User1"
                },
                "photos": [],
                "active": false,
                "locale": "EN_US",
                "globalAttributes": {
                    "partnerCustomProperties": {},
                    "productSeat": "MARKETING_CLOUD",
                    "passwordLoginDisabled": false
                },
                "clientAttributes": [
                    {
                        "clientId": 1000004509,
                        "userType": "PARTNER_ADMIN",
                        "phoneNumbers": []
                    }
                ],
                "meta": {
                    "resourceType": "User",
                    "createdTime": "2023-05-16 13:07:37",
                    "lastModified": "2024-02-02 08:55:39",
                    "location": "/api/scim/bulk-upsert"
                },
                "emails": [
                    {
                        "value": "testuser1@sprinklr.com",
                        "primary": true
                    }
                ]
            },
            {
                "schemas": [
                    "urn:ietf:params:scim:schemas:core:2.0:User",
                    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                    "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                    "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
                    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
                ],
                "id": "1000263190",
                "userName": "testuser2@sprinklr.com",
                "name": {
                    "familyName": "Test",
                    "givenName": "User2"
                },
                "photos": [],
                "active": true,
                "locale": "EN_US",
                "globalAttributes": {
                    "partnerCustomProperties": {},
                    "productSeat": "MARKETING_CLOUD",
                    "passwordLoginDisabled": false
                },
                "clientAttributes": [
                    {
                        "clientId": 1000004509,
                        "userType": "PARTNER_ADMIN",
                        "phoneNumbers": []
                    }
                ],
                "meta": {
                    "resourceType": "User",
                    "createdTime": "2023-05-16 13:09:54",
                    "lastModified": "2024-02-02 08:55:39",
                    "location": "/api/scim/bulk-upsert"
                },
                "emails": [
                    {
                        "value": "testuser2@sprinklr.com",
                        "primary": true
                    }
                ]
            },
            {
                "schemas": [
                    "urn:ietf:params:scim:schemas:core:2.0:User",
                    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                    "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                    "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
                    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
                ],
                "id": "1000326999",
                "userName": "testuser3@sprinklr.com",
                "name": {
                    "familyName": "Test",
                    "givenName": "User3"
                },
                "photos": [],
                "active": true,
                "locale": "EN_US",
                "globalAttributes": {
                    "partnerCustomProperties": {},
                    "productSeat": "MARKETING_CLOUD",
                    "passwordLoginDisabled": false
                },
                "clientAttributes": [
                    {
                        "clientId": 1000004509,
                        "userType": "PARTNER_ADMIN",
                        "phoneNumbers": []
                    }
                ],
                "meta": {
                    "resourceType": "User",
                    "createdTime": "2024-01-24 13:00:53",
                    "lastModified": "2024-02-02 08:55:39",
                    "location": "/api/scim/bulk-upsert"
                },
                "emails": [
                    {
                        "value": "testuser3@sprinklr.com",
                        "primary": true
                    }
                ]
            }
        ]
    },
    "errors": []
}





## Sample Request - Async Method














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/scim/bulk-upsert' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "callbackUrlHeaders": {},
    "callbackUrl": "https://webhook.site/c7280ed0-9f8a-40d0-830e-6f00e441cd9b",
    "executeAsync": true,
    "users": [
        {
            "userName": "testuser1@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User1"
            },
            "photos": [],
            "active": false,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {},
                "passwordLoginDisabled": false,
                "productSeat": "MARKETING_CLOUD"
            },
            "clientAttributes": [
                {
                    "clientId": 1000004509,
                    "userType": "PARTNER_ADMIN"
                }
            ]
        },
        {
            "userName": "testuser2@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User2"
            },
            "photos": [],
            "active": true,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {},
                "passwordLoginDisabled": false,
                "productSeat": "MARKETING_CLOUD"
            },
            "clientAttributes": [
                {
                    "clientId": 1000004509,
                    "userType": "PARTNER_ADMIN"
                }
            ]
        },
        {
            "userName": "testuser3@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User3"
            },
            "photos": [],
            "active": true,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {},
                "passwordLoginDisabled": false,
                "productSeat": "MARKETING_CLOUD"
            },
            "clientAttributes": [
                {
                    "clientId": 1000004509,
                    "userType": "PARTNER_ADMIN"
                }
            ]
        }
    ]
}'





## Example - Response





{
    "data": {
        "processId": "65bcafbdb428181ca8ea9ae1"
    },
    "errors": []
}





**Dev Notes: **For async method, you can check the complete API response on the callback URL destination. The response can be identified using the processId mentioned in the API response.

[](https://dev.sprinklr.com/bulk-create-update-user) 

 

 
[Back to top](https://dev.sprinklr.com/bulk-create-update-user)
