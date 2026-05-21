---
title: "Partial Update User (SCIM)"
slug: partial-update-user-scim
url: https://dev.sprinklr.com/partial-update-user-scim
---

# Partial Update User (SCIM)

#  PATCH  Partial Update User (SCIM)

Use this API to update specific attributes of an existing user in Sprinklr without replacing the entire user record. The API follows the SCIM 2.0 PATCH standard and supports operations such as `add` and `replace` for user attributes like name, active status, locale, emails, client attributes, and custom properties.

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


**Dev Note:**
  The `add` and `replace` operations behave differently in SCIM PATCH requests:



- `add`: Inserts a new attribute or appends a value to an existing multi-valued attribute. If the attribute already exists and supports multiple values (for example, `emails`), the new value is added alongside the existing ones.

- `replace`: Updates an attribute by overwriting the existing value. If the attribute already has a value, it will be replaced entirely with the new one.


Use `add` when you want to keep existing values and extend them, and `replace` when you want to fully overwrite the existing attribute value.

## Request Parameters

The request uses the SCIM `Operations` object. Each operation contains an `op`  (operation type) and `value`  (fields to update).






















			````


















| Parameters | Sub-Parameter | Required | Description | Type |
| --- | --- | --- | --- | --- |
| Operations |  | Required | Defines the modification to be performed on the user resource. | Object |
|  | op | Required | The type of operation to perform. Supported values: add,replace. | String |
|  | path | Required | Specify the user attribute you want to update. You can use dot notation for nested attributes. For example, name.givenName. | String |
|  | value | Required | Fields to update. | Object |


### `value`Object





























































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

## Example 1 - Request with Add Operation



 Copy Code



curl -X PATCH \
  'https://api3.sprinklr.com/{env}/api/v2/scim/Users/66016318' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
   "Operations": {
       "op": "add",
       "value": {
           "locale": "EN_GB",
           "active": true,
           "name": {
               "familyName": "Deepak",
               "givenName": "Bala Scim 7"
           }
       }
   }
}'



## Example - Response




{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
    ],
    "id": "66016318",
    "userName": "deepak.bala+scimapi7@sprinklr.com",
    "name": {
        "familyName": "Deepak",
        "givenName": "Bala Scim 7"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png"
        }
    ],
    "active": true,
    "locale": "EN_GB",
    "globalAttributes": {
        "partnerCustomProperties": {
            "_c_65fc4d74687dc60dc84b6076": [
                "bing.com"
            ],
            "spr_availability_status_updation_reason": [
                "User status deactivated"
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
                    "value": "7708675309"
                }
            ],
            "businessCategory": "CORPORATE",
            "clientCustomProperties": {
                "_c_677cdc0a7ba2c7762c92f2ed": [
                    "testing002"
                ]
            },
            "sessionTimeout": 44,
            "customProfileConfigs": [
                {
                    "userId": 66016318,
                    "channelType": "GOOGLE_BUSINESS",
                    "customProfileEnabled": true,
                    "shouldUseDefaultProfile": true,
                    "sprCustomProfileConfigs": [
                        {
                            "id": "67f03fd13622b51e6b600c9b",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f040e23622b51e6b600d4a",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f37a543622b51e6b60a647",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f37a7a3622b51e6b60a67c",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f4c38a77bcaa0e39a11121",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f4c3c377bcaa0e39a11163",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f4c3ee77bcaa0e39a11193",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f4c62a77bcaa0e39a11333",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "305 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f4c63f77bcaa0e39a11375",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "306 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f4c7dd77bcaa0e39a113d7",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "306 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f54facaa81174817329955",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "307 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f5522eaa81174817329acf",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "307 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        },
                        {
                            "id": "67f558ec211d371d59d1af59",
                            "url": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png",
                            "name": "307 Deepak",
                            "enabled": true,
                            "userId": 66016318,
                            "channelType": "GOOGLE_BUSINESS",
                            "accountId": -1
                        }
                    ]
                }
            ],
            "personaViewEnabled": false
        }
    ],
    "meta": {
        "resourceType": "User",
        "createdTime": "2025-01-13 08:33:02",
        "lastModified": "2025-08-20 12:24:04"
    },
    "emails": [
        {
            "value": "deepak.bala+scimapi7@sprinklr.com",
            "primary": true
        }
    ],
    "userAssignmentConfig": {
        "userId": "66016318",
        "capacities": [],
        "proficiencies": {
            "skillVsProficiency": {
                "6757d7c2d8a91704906f5b3b": 100,
                "67691582ceeb6d36a05ffdfb": 100,
                "6757d7c2fe1976763f55220c": 90
            }
        },
        "capacityConfigId": "6526e9d23988ef611671f62d",
        "capacityConfigName": "Shreyas old Capacity1",
        "timeZone": {
            "timeZone": "Asia/Kolkata",
            "country": "IN"
        }
    },
    "userVoiceConfig": {
        "userId": "66016318",
        "autoAnswer": false,
        "useVoipCall": true,
        "sipVoiceAccountId": "64e0aed5b8a380785fa46d89"
    },
    "supervisorTeamIds": [
        "64edac60d8489c6113bd17fe"
    ],
    "recordingShareConfigs": [
        {
            "type": "USER",
            "ids": [
                "66007998",
                "66016241"
            ]
        }
    ]
}

## Example 2 - Request with Replace Operation



 Copy Code



curl -X PATCH \
  'https://api3.sprinklr.com/{env}/api/v2/scim/Users/66016318' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
  "Operations": [
    {
      "op": "replace",
      "value": {
        "locale": "EN_GB",
        "active": true,
        "name": {
          "familyName": "Deepak",
          "givenName": "Bala Scim 7"
        },
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
            }
          }
        ]
      }
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
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
    ],
    "id": "66016318",
    "userName": "deepak.bala+scimapi7@sprinklr.com",
    "name": {
        "familyName": "Deepak",
        "givenName": "Bala Scim 7"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png"
        }
    ],
    "active": true,
    "locale": "EN_GB",
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
            "phoneNumbers": [],
            "businessCategory": "CORPORATE",
            "clientCustomProperties": {},
            "customProfileConfigs": []
        }
    ],
    "meta": {
        "resourceType": "User",
        "createdTime": "2025-01-13 08:33:02",
        "lastModified": "2025-08-20 14:57:57"
    },
    "emails": [
        {
            "value": "deepak.bala+scimapi7@sprinklr.com",
            "primary": true
        }
    ],
    "userAssignmentConfig": {
        "userId": "66016318",
        "capacities": [],
        "proficiencies": {
            "skillVsProficiency": {
                "6757d7c2d8a91704906f5b3b": 100,
                "67691582ceeb6d36a05ffdfb": 100,
                "6757d7c2fe1976763f55220c": 90
            }
        },
        "capacityConfigId": "6526e9d23988ef611671f62d",
        "capacityConfigName": "Shreyas old Capacity1",
        "timeZone": {
            "timeZone": "Asia/Kolkata",
            "country": "IN"
        }
    },
    "userVoiceConfig": {
        "userId": "66016318",
        "autoAnswer": false,
        "useVoipCall": true,
        "sipVoiceAccountId": "64e0aed5b8a380785fa46d89"
    },
    "supervisorTeamIds": [
        "64edac60d8489c6113bd17fe"
    ],
    "recordingShareConfigs": [
        {
            "type": "USER",
            "ids": [
                "66007998",
                "66016241"
            ]
        }
    ]
}

## Example - Request with Dot Notation

This API supports dot notation to update nested attributes. For example, you can update `name.familyName` as shown in the following request.




 Copy Code



curl --location --request PATCH 'https://api3.sprinklr.com/{env}/api/v2/scim/Users/1000300254' \
--header 'Authorization: {token}' \
--header 'Content-Type: application/scim+json' \
--data '{
    "Operations": [
        {
            "op": "add",
            "path": "name.familyName",
            "value": "Rai Abc"
        },
        {
            "op": "add",
            "path": "name.givenName",
            "value": "Rai"
        },
        {
            "op": "add",
            "path": "globalAttributes.partnerCustomProperties._c_65fc4d74687dc60dc84b6076",
            "value": [
                "bing.com"
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
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
    ],
    "id": "1000300254",
    "userName": "abc@sprinklr.com",
    "name": {
        "familyName": "Rai Abc",
        "givenName": "Rai"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
        }
    ],
    "active": true,
    "locale": "EN_US",
    "globalAttributes": {
        "partnerCustomProperties": {
            "5b584ba4e4b085291d4c2e75": [
                "post"
            ],
            "spr_user_is_resource": [
                "false"
            ],
            "_c_6729b97f7380406301edb796": [
                "1730745000000"
            ],
            "spr_user_availability_status": [
                "Available"
            ],
            "_c_6729bb677380406301ee223d": [
                "GW_AUTOMATION"
            ],
            "support_access": [
                "true"
            ],
            "spr_voice_use_voip_call": [
                "No"
            ],
            "spr_user_message_translation_enabled": [
                "false"
            ],
            "_c_6729b9cd7380406301edc994": [
                "
GW_AUTOMATION
"
            ],
            "spr_guest_user": [
                "false"
            ],
            "_c_6729b93d7380406301eda6d1": [
                "3"
            ],
            "schedule_adherence_tracking_mode": [
                "Sprinklr"
            ],
            "spr_influencer_user": [
                "false"
            ]
        },
        "passwordLoginDisabled": false
    },
    "clientAttributes": [
        {
            "clientId": 1000004509,
            "userType": "CLIENT_USER",
            "phoneNumbers": [
                {}
            ],
            "businessCategory": "CORPORATE",
            "customProfileConfigs": [],
            "personaViewEnabled": false
        }
    ],
    "meta": {
        "resourceType": "User",
        "createdTime": "2026-01-08 19:24:00",
        "lastModified": "2026-01-08 19:24:35"
    },
    "emails": [
        {
            "value": "abc@sprinklr.com",
            "primary": true
        }
    ],
    "userAssignmentConfig": {
        "userId": "1000300254",
        "capacities": [],
        "proficiencies": {
            "skillVsProficiency": {
                "682f4a635ab21653a0d84ee4": 70
            }
        }
    },
    "userVoiceConfig": {
        "userId": "1000300254",
        "useVoipCall": true
    },
    "supervisorTeamIds": [],
    "recordingShareConfigs": []
}

### Response Schema












































































| Field | Type | Description |
| --- | --- | --- |
| schemas | array | List of SCIM schemas supported in the response. |
| id | string | Unique identifier for the user. |
| userName | string | User login name (often the email address). |
| name | object | User’s first and last names. |
| photos | array | Profile photo URL(s). |
| active | boolean | Indicates whether the user is active. |
| locale | string | User’s locale setting. |
| globalAttributes | object | Sprinklr-level attributes such as partner properties and login restrictions. |
| clientAttributes | array | Client-specific attributes like role, phone number, business category, etc. |
| meta | object | Contains createdTime and lastModified details. |
| emails | array | List of user email addresses. |
| userAssignmentConfig | object | Contains capacities, proficiencies, and time zone information. |
| userVoiceConfig | object | Contains telephony and voice account settings. |

[](https://dev.sprinklr.com/partial-update-user-scim) 

 

 
[Back to top](https://dev.sprinklr.com/partial-update-user-scim)
