---
title: "User Webhooks"
slug: user-webhooks
url: https://dev.sprinklr.com/user-webhooks
---

# User Webhooks

# User Webhooks

**User Webhook Subscriptions:**
 User Create, User Update, User Delete

Whenever a user is added, their details are updated, or they are deleted from the Sprinklr platform, the user respective user webhook get triggered.

- [User.Created Webhook](https://dev.sprinklr.com/user-webhooks#UC)

- [User.Updated Webhook](https://dev.sprinklr.com/user-webhooks#UU)

- [User.Deleted Webhook](https://dev.sprinklr.com/user-webhooks#UD)

### User.Created Webhook




  Copy Code



{
  "id": "65dc42a0324fd745712f0437",
  "type": "user.created",
  "payload": {
    "schemas": [
      "urn:ietf:params:scim:schemas:core:2.0:User",
      "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
      "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
      "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
      "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "id": "1474307",
    "externalId": "",
    "lyearnId": "",
    "userPermissions": [],
    "accessibleClientIds": [
      4706
    ],
    "userName": "testuser@sprinklr.com",
    "name": {
      "familyName": "User",
      "givenName": "Test"
    },
    "photos": [
      {
        "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png",
        "primary": true
      }
    ],
    "active": true,
    "locale": "en_US",
    "globalAttributes": {
      "partnerCustomProperties": {
        "spr_guest_user": [
          "false"
        ],
        "spr_user_message_translation_enabled": [
          "false"
        ],
        "spr_user_availability_status": [
          "DND"
        ],
        "5cc9a7d0e4b01904c8dfc93a": [
          "All Users"
        ],
        "_c_6572e90cb5feff31fac33d57": [
          "Sprinklr Care ",
          "Sprinklr Service ",
          "Sprinklr Social ",
          "Sprinklr Insights ",
          "Sprinklr Marketing ",
          "Sprinklr Ads"
        ],
        "_c_64ca67477e04c63f69c28663": [
          "USA"
        ]
      },
      "productSeat": "SOCIAL_CLOUD",
      "passwordLoginDisabled": false
    },
    "clientAttributes": [
      {
        "clientId": 4706,
        "userType": "CLIENT_USER",
        "phoneNumbers": [
          {
            "primary": true
          }
        ],
        "businessCategory": "CORPORATE"
      }
    ],
    "meta": {
      "resourceType": "User",
      "createdTime": "2024-02-26 07:49:51",
      "lastModified": "2024-02-26 07:49:52"
    },
    "userAssignmentConfig": {
      "proficiencies": {
        "skillVsProficiency": {
          "5e53b1dc94035d05b5a8ae49": 50,
          "5fa0ebd9ac5eb848b166f37f": 60
        }
      }
    }
  },
  "eventTime": 1714648753890,
  "subscriptionDetails": {
    "subscriptionId": "66337548ae5e77745b29aa33"
  }
}





## Response Parameters

The following table describes the Request Parameters in use.






















































			****





			****



| Parameters | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Refers to the unique Id of the user | String |
| externalId |  |  | String |
| lyearnId |  |  | String |
| userPermissions |  |  | String |
| accessibleClients |  |  | List [String] |
| userName |  | The email Id of the user.The email of the user needs to be unique every time you hit the create user API | String |
| name |  | Object that specifies the familyName and givenName | Object |
|  | familyName | Refers to the last name of the user | String |
|  | givenName | Refers to the first name of the user | String |
| photos |  | Array of photos, but Sprinklr will use the first one only. | Array |
|  | value | Refer to the url for the photo | URL |
| active |  | If true, the user will be set to active state | Boolean |
| isSpaceUser |  | If true, the user can access Space UI only | Boolean |
| locale |  | Refers to the language code of the userRefer to the table below for common language codes | String |
| globalAttributes |  | The global attributes of the user. Kindly check the Custom Global Attributes Description Table below. | Object |
| clientAttributes |  | The client-level attributes of the user. Kindly check the Client Attributes Description Table below. | Array |

## Global Attributes Object - Description Table

The following table describes the parameters within globalAttributes object that can be used in Request Payload.


















****











			````




| Parameter | Description | Type |
| --- | --- | --- |
| partnerCustomProperties | Refers to the global-level custom properties. | Object |
| productSeat | Refers to the product seat you want to assign to the userSupported Product Seats:Modern Engagement, Modern Marketing, Modern Care, Modern Marketing Lite, DistributedBy default, the user falls under the Modern Engagement product seat | String |
| federationId | Assigning a Federation ID helps with unique identification. You cannot assign the same federation identity to more than one user The federation ID is additionally used by Customer Environments for attaching extra SSO Login information | String |
| passwordLoginDisabled | By default false, In case of SSO user this need to be true along with federationId. | Boolean |

## Client Attributes Array - Description Table

The following table describes the parameters within clientAttributes object that can be used in Request Payload.























****``














































| Parameter | Sub-Parameter | Description | Type |  |
| --- | --- | --- | --- | --- |
| clientId |  | Required | Refers to the workspace Id where you want to add the user | Integer |
| userType |  | Required | The type of user you want to create.Supported user types:PARTNER_ADMIN, PARTNER_USER,    CLIENT_ADMIN, CLIENT_USER | String |
| phoneNumbers |  | Array containing phone details. | Array |  |
|  | value | Refers to the phone number of the user | String |  |
|  | type | Refers to the type of phone number, i.e., whether it is for work or personal | String |  |
|  | primary | If true, the phone number is primary to the user | Boolean |  |
| clientCustomProperties |  | The workspace level custom properties. | Object |  |
| businessCategory |  | The category of business.Either CORPORATE or DISTRIBUTED | String |  |
| designation |  | Refers to the designation of user. | String |  |
| department |  | Refers to the department of user. | String |  |
| userGroupIds |  | The user group Ids where you want to add the user | List [String] |  |
| primaryUserGroupId |  | The primary user group id where you want to add the user | String |  |

### User.Updated Webhook




  Copy Code



{
  "id": "65dc42a0324fd745712f041a",
  "type": "user.updated",
  "payload": {
    "schemas": [
      "urn:ietf:params:scim:schemas:core:2.0:User",
      "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
      "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
      "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
      "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "id": "1474307",
    "externalId": "",
    "lyearnId": "",
    "userPermissions": {
[
        "entityType": "CASE_MANAGEMENT",
        "permissions": [
          "CREATE_CASE",
          "CREATE_TASK",
          "DELETE_CASE",
          "CREATE_LEAD",
          "CREATE_CONTACT",
          "CREATE_ACCOUNT",
          "CREATE_OPPORTUNITY"
        ]
      }
],
    "accessibleClientIds": [
      4706
    ],
    "userName": "testuser@sprinklr.com",
    "name": {
      "familyName": "User",
      "givenName": "Test"
    },
    "photos": [
      {
        "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png",
        "primary": true
      }
    ],
    "active": true,
    "locale": "en_US",
    "globalAttributes": {
      "partnerCustomProperties": {
        "spr_guest_user": [
          "false"
        ],
        "spr_user_message_translation_enabled": [
          "false"
        ],
        "spr_user_availability_status": [
          "DND"
        ],
        "_c_6572e90cb5feff31fac33d57": [
          "Sprinklr Care ",
          "Sprinklr Service "
        ],
        "_c_64ca67477e04c63f69c28663": [
          "USA"
        ]
      },
      "productSeat": "SOCIAL_CLOUD",
      "passwordLoginDisabled": false
    },
    "clientAttributes": [
      {
        "clientId": 4706,
        "userType": "CLIENT_USER",
        "phoneNumbers": [
          {
            "primary": true
          }
        ],
        "businessCategory": "CORPORATE"
      }
    ],
    "meta": {
      "resourceType": "User",
      "createdTime": "2024-02-26 07:49:51",
      "lastModified": "2024-02-26 07:49:52"
    },
    "userAssignmentConfig": {
      "proficiencies": {
        "skillVsProficiency": {
          "5e53b1dc94035d05b5a8ae49": 50,
          "5fa0ebd9ac5eb848b166f37f": 60
        }
      }
    }
  },
  "eventTime": 1714648753875,
  "subscriptionDetails": {
    "subscriptionId": "66337548ae5e77745b29aa33"
  }
}





### User.Deleted Webhook




  Copy Code



{
  "id": "65dc6e08324fd7457167cc87",
  "type": "user.deleted",
  "payload": "1474307",
  "eventTime": 1474307,
  "subscriptionDetails": {
    "subscriptionId": "65dc420e324fd745712e7deb"
  }
}





[](https://dev.sprinklr.com/user-webhooks)

[Back to top](https://dev.sprinklr.com/user-webhooks)
