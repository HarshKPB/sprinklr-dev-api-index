---
title: "User Create"
slug: v1-user-create
url: https://dev.sprinklr.com/v1-user-create
---

# User Create

#
  POST - User Create

You can create a User via this API call and you will get the Response as Id after making the Request. Creating users in Sprinklr allows you to onboard your team, providing new users with the access and permissions they need to get started in Sprinklr. To create a user, you must be an admin of the Customer or Workspace environment in which you want to create a user. You cannot create a user with a higher user level permission than yourself.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/scim/v2/Users

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

## Request Body Parameters

The following table describes the Request Parameters in use.







****

****

| Request Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| userName | Required | The email of the user. | String |
| name | Required | The first and last name of the user. | Name object |
| photos | Optional | The status of the user. Default = FALSE | Boolean |
| active | Optional | Description of the custom field. Not exceeding 500 characters. | String |
| is SpaceUser | Required | If true, the user will be created in space. | Boolean |
| customGlobalAttributes | Required | The global attributes of the user. Kindly check the Custom Global Attributes Description Table below. | Global Attribute Object |
| clientAttributes | Required | The client-level attributes of the user. Kindly check the Client Attributes Description Table below. | Client Attribute Object |
| locale | Optional | The location of the user. | String |

## Custom Global Attributes Sub Parameters

The following table describes the parameters within customGlobalAttributes object that can be used in Request Payload.







````

| Sub Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| partnerCustomProperties | Optional | The partner custom properties. | Map<String, List<String>> |
| productSeat | Optional | The seat for which you want to create user, e.g. MARKETING_CLOUD | String |
| federationId | Optional | This is required for SSO user | String |
| passwordLoginDisabled | Optional | By default false, In case of SSO user this need to be true along with federationId. | String |

**Notes: ** The available product seats are `SOCIAL_CLOUD, MARKETING_CLOUD, SERVICE_CLOUD, DISTRIBUTED`.

## Client Attributes Sub Parameters

The following table describes the parameters within clientAttributes object that can be used in Request Payload.







``

``

| Sub Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| clientId | Required | The workspace Id in which you want to add user | Long |
| userType | Required | The type of user you want to create. PARTNER_ADMIN, PARTNER_USER,    CLIENT_ADMIN, CLIENT_USER |  |
| phoneNumbers | Optional | The object containing phone details. "phoneNumbers": [{ 		            "value": "170-807-5009", 		            "type": "work", 		            "primary": true 			}], | List<ScimObject> |
| clientCustomProperties | Optional | The client custom properties. | Map<String, List<String>> |
| businessCategory | Optional | The category of business. | String |
| designation | Optional | The designation of user. | String |
| department | Optional | The department of user. | String |
| userGroupIds | Optional | The user group Id to which you want to add the user you are creating. | Set<String> |
| primaryUserGroupId | Optional | The primary user group. | String |

## Example - Request














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/scim/v2/Users' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "userName": "ben.turner+scimapi@sprinklr.com",
    "name": {
        "familyName": "Ben",
        "givenName": "Turner"
    },
    "active": true,
    "photos": [{
        "value": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png"
    }],
   "isSpaceUser": true,
    "customGlobalAttributes": {	"partnerCustomProperties": {},	"productSeat": "MARKETING_CLOUD"},
    "clientAttributes": [{
        "clientId": "5547",
        "clientCustomProperties": {
        },
        "phoneNumbers": [{
            "value": "770-867-5309",
            "type": "work",
            "primary": true
        }]
    }]
}'





## Example - Response





{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User"
    ],
    "userName": "ben.turner+scimapi@sprinklr.com",
    "name": {
        "familyName": "Ben",
        "givenName": "Turner"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/1090/IMG_3988-a4533d4a-f875-4069-8746-50d9287be4e1-1676689091.png"
        }
    ],
    "active": true,
    "locale": "EN_US",
    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User": {
        "partnerCustomProperties": {},
        "passwordLoginDisabled": false,
         "productSeat": "MARKETING_CLOUD",
    },
    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User": [
        {
            "clientId": 5547,
            "userType": "CLIENT_USER",
            "phoneNumbers": [
                {
                    "value": "770-867-5309",
                    "type": "work",
                    "primary": true
                }
            ],
            "businessCategory": "CORPORATE",
            "clientCustomProperties": {}
        }
    ],
    "id": "190630",
    "meta": {
        "resourceType": "User",
        "createdTime": "2019-01-07 16:55:10",
        "lastModified": "2019-01-07 16:55:10",
        "location": "/api/v3.1/scim/v2/Users190630"
    }
}





[](https://dev.sprinklr.com/v1-user-create)




[Back to top](https://dev.sprinklr.com/v1-user-create)
