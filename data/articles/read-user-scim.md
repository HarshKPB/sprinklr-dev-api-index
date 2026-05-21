---
title: "Read User (SCIM)"
slug: read-user-scim
url: https://dev.sprinklr.com/read-user-scim
---

# Read User (SCIM)

#  GET  Read User (SCIM)

Using this API, you can fetch a user for the given user Id (unique identifier for the user existing on the Sprinklr platform).

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/Users/{userId}

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

The following table describes the Request Parameters in use.















[search by entity](https://dev.sprinklr.com/search-by-entity)[read user by User Name](https://dev.sprinklr.com/fetch-user-by-email-id)[bootstrap API](https://dev.sprinklr.com/v1-bootstrap-resources)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userId | Required | Refers to the unique identifier for the user whose details need to be fetched.You can use ,  API, or  to fetch the user Id details | Integer |

**Steps to Extract User Id from UI: **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on Users Icon within "Manage Workspace" module
- Search the user you are want the details for
- Click on "Details" icon palced beside the three dots
- The user Id will be part of the web URL
- Example: https://space.sprinklr.com/social/governance/users/1000211373/overview. Thus the user will be: 1000211373

## Example - Request



 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/scim/Users/66008750' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}'



## Example - Response




{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
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
            "designation": "test",
            "department": "test"
        }
    ],
    "meta": {
        "resourceType": "User",
        "createdTime": "2024-05-28 08:03:01",
        "lastModified": "2024-05-28 08:03:05"
    },
    "emails": [
        {
            "value": "testuser3612@sprinklr.com",
            "primary": true
        }
    ]
}

**Dev Notes: ** When making a request to the API to retrieve user information, if the specified user is not found in the database, the API will return a 404 error.

[](https://dev.sprinklr.com/read-user-scim) 

 

 
[Back to top](https://dev.sprinklr.com/read-user-scim)
