---
title: "Update User (SCIM)"
slug: update-user-scim
url: https://dev.sprinklr.com/update-user-scim
---

# Update User (SCIM)

#  PUT  Update User (SCIM)

Using this API, you can update the details for the user existing within the Sprinklr platform. When updating the partner/client custom properties for the user, the newly added custom properties will get synced, while the existing ones will be retained.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/scim/Users/{userId}

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

## Path Parameters















[search by entity](https://dev.sprinklr.com/search-by-entity)[read user by User Name](https://dev.sprinklr.com/read-user-by-email-id)[bootstrap API](https://dev.sprinklr.com/bootstrap-resources-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userId | Required | Refers to the unique identifier for the user whose details need to be updated.You can use ,  API, or  to fetch the user Id details | Integer |

**Steps to Extract User Id from UI: **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on Users Icon within "Manage Workspace" module
- Search the user you are want the details for
- Click on "Details" icon palced beside the three dots
- The user Id will be part of the web URL
- Example: https://space.sprinklr.com/social/governance/users/1000211373/overview. Thus the user will be: 1000211373

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
| supervisorTeamIds |  | Optional | List of team IDs where the user acts as a supervisor. | Array of Strings |
| recordingShareConfigs |  | Optional | Configuration for sharing recordings with other users. | Array of Objects |
|  | type | Required | Sharing type (e.g., USER, TEAM). | String |
|  | ids | Required | IDs of the users or teams with whom recordings are shared. | Array of Integers |

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
| sessionTimeout |  | Optional | Session timeout value in minutes | Integer |
| customProfileConfigs |  | Optional | Custom profile configurations for specific channels. | Array of Objects |


### customProfileConfigs Object Description











































| Parameter | Type | Required / Optional | Description |
| --- | --- | --- | --- |
| customProfileEnabled | boolean | Required | Indicates whether a custom profile is enabled for the user. |
| userId | integer | Required | Unique identifier of the user this profile configuration applies to. |
| channelType | string | Required | Specifies the channel for which the custom profile is configured (e.g., SPRINKLR_LIVE_CHAT). |
| sprCustomProfileConfigs | array of objects | Optional | Contains the actual profile settings to be applied for the specified channel. |
| shouldUseDefaultProfile | boolean | Optional | If true, the system will use the default profile settings in the absence of a matching custom profile. |


### sprCustomProfileConfigs Object Description

















































| Parameter | Type | Required / Optional | Description |
| --- | --- | --- | --- |
| url | string | Required | URL to the image or avatar used in the custom profile. |
| name | string | Required | Name associated with the custom profile. |
| enabled | boolean | Required | Indicates if this specific profile is active/enabled. |
| userId | integer | Required | User ID to which the profile is linked (typically same as parent userId). |
| channelType | string | Required | The channel for which this profile configuration is valid. |
| accountId | integer | Optional | Account ID related to the specific custom profile. Use -1 for a default or global profile. |

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

## Example 1 - Request for Deactivating/Disabling a User



 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/scim/Users/66009014' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
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
    "active": false,
    "isSpaceUser": false,
    "locale": "de_DE",
    "globalAttributes": {
        "partnerCustomProperties": {
        },
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 66000002,
            "userType": "CLIENT_ADMIN",
            "phoneNumbers": [
                {
                    "value": "+919123456789"
                }
            ],
            "businessCategory": "CORPORATE",
            "clientCustomProperties": {},
            "userGroupIds": [
                "653fc0293618cc7784db2976"
            ]
        }
    ]
}'



## Example - Response




{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "id": "66009014",
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
    "active": false,
    "locale": "DE_DE",
    "globalAttributes": {
        "partnerCustomProperties": {},
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 66000002,
            "userType": "CLIENT_ADMIN",
            "phoneNumbers": [
                {
                    "value": "+919123456789"
                }
            ],
            "businessCategory": "CORPORATE",
            "userGroupIds": [
                "653fc0293618cc7784db2976"
            ],
            "clientCustomProperties": {}
        }
    ],
    "meta": {
        "resourceType": "User",
        "createdTime": "2024-05-28 08:03:01",
        "lastModified": "2024-05-28 08:47:36",
        "location": "/api/scim/Users/66009014"
    },
    "emails": [
        {
            "value": "testuser@sprinklr.com",
            "primary": true
        }
    ]
}

## Example 2 - Request for Updating partnerCustomProperties



 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/scim/Users/66009014' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
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
    "active": false,
    "isSpaceUser": false,
    "locale": "de_DE",
    "globalAttributes": {
        "partnerCustomProperties": {
            "_c_664b5c8d485a61414fe65fda": "1",
            "_c_66335b9f58046d2a90f3b73c": "user"
        },
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 66000002,
            "userType": "CLIENT_ADMIN",
            "phoneNumbers": [
                {
                    "value": "+919123456789"
                }
            ],
            "businessCategory": "CORPORATE",
            "clientCustomProperties": {},
            "userGroupIds": [
                "653fc0293618cc7784db2976"
            ]
        }
    ]
}'



## Example - Response




{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "id": "66009014",
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
    "active": false,
    "locale": "DE_DE",
    "globalAttributes": {
        "partnerCustomProperties": {
            "_c_664b5c8d485a61414fe65fda": [
                "1"
            ],
            "_c_66335b9f58046d2a90f3b73c": [
                "user"
            ]
        },
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 66000002,
            "userType": "CLIENT_ADMIN",
            "phoneNumbers": [
                {
                    "value": "+919123456789"
                }
            ],
            "businessCategory": "CORPORATE",
            "userGroupIds": [
                "653fc0293618cc7784db2976"
            ],
            "clientCustomProperties": {}
        }
    ],
    "meta": {
        "resourceType": "User",
        "createdTime": "2024-05-28 08:03:01",
        "lastModified": "2024-05-28 08:47:36",
        "location": "/api/scim/Users/66009014"
    },
    "emails": [
        {
            "value": "testuser@sprinklr.com",
            "primary": true
        }
    ]
}


## Example 3 - Request for Updating customProfileConfigs



 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/scim/Users/66009014' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "userName": "deepak.bala+scimapi500@sprinklr.com",
    "name": {
        "familyName": "Deepak",
        "givenName": "Bala Scim 500"
    },
    "active": true,
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png"
        }
    ],
    "isSpaceUser": true,
    "globalAttributes": {
        "partnerCustomProperties": {
            "dummy": [
                "test"
            ],
            "_c_65fc4d74687dc60dc84b6076": [
                "google.com"
            ]
        },
        "productSeat": "MARKETING_CLOUD"
    },
    "clientAttributes": [
        {
            "clientId": "66000002",
            "userType": "PARTNER_ADMIN",
            "clientCustomProperties": {
                "dummy": [
                    "test"
                ]
            },
            "phoneNumbers": [
                {
                    "value": "7708675309",
                    "type": "work",
                    "primary": true
                }
            ],
            "sessionTimeout": 60,
            "customProfileConfigs": [
                {
                    "customProfileEnabled": true,
                    "userId": 66062688,
                    "channelType": "SPRINKLR_LIVE_CHAT",
                    "sprCustomProfileConfigs": [
                        {
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "506 Deepak",
                            "enabled": true,
                            "userId": 66062688,
                            "channelType": "SPRINKLR_LIVE_CHAT",
                            "accountId": -1
                        }
                    ],
                    "shouldUseDefaultProfile": true
                }
            ]
        }
    ],
    "supervisorTeamIds": [
        "64edac60d8489c6113bd17fe",
        "658401290284c761c774b6ac"
    ],
    "recordingShareConfigs": [
        {
            "type": "USER",
            "ids": [
                66007998,
                66016241,
                66016488
            ]
        }
    ]
}'



## Example - Response




	{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "id": "66062688",
    "userName": "deepak.bala+scimapi500@sprinklr.com",
    "name": {
        "familyName": "Deepak",
        "givenName": "Bala Scim 500"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png"
        }
    ],
    "active": true,
    "locale": "EN_US",
    "globalAttributes": {
        "partnerCustomProperties": {
            "_c_65fc4d74687dc60dc84b6076": [
                "google.com"
            ]
        },
        "productSeat": "MARKETING_CLOUD",
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 66000002,
            "userType": "PARTNER_ADMIN",
            "phoneNumbers": [
                {
                    "value": "7708675309",
                    "type": "work",
                    "primary": true
                }
            ],
            "clientCustomProperties": {},
            "sessionTimeout": 60,
            "customProfileConfigs": [
                {
                    "userId": 66062688,
                    "channelType": "SPRINKLR_LIVE_CHAT",
                    "customProfileEnabled": true,
                    "shouldUseDefaultProfile": true,
                    "sprCustomProfileConfigs": [
                        {
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "506 Deepak",
                            "enabled": true,
                            "userId": 66062688,
                            "channelType": "SPRINKLR_LIVE_CHAT",
                            "accountId": -1
                        }
                    ]
                }
            ]
        }
    ],
    "meta": {
        "resourceType": "User",
        "createdTime": "2025-05-05 10:12:38",
        "lastModified": "2025-05-15 14:40:07",
        "location": "/api/scim/Users/66062688"
    },
    "emails": [
        {
            "value": "deepak.bala+scimapi500@sprinklr.com",
            "primary": true
        }
    ],
    "supervisorTeamIds": [
        "658401290284c761c774b6ac",
        "64edac60d8489c6113bd17fe"
    ],
    "recordingShareConfigs": [
        {
            "type": "USER",
            "ids": [
                "66007998",
                "66016488",
                "66016241"
            ]
        }
    ]
}






[](https://dev.sprinklr.com/update-user-scim) 

 

 
[Back to top](https://dev.sprinklr.com/update-user-scim)
