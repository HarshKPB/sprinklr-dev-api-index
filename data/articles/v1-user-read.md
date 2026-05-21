---
title: "User Read"
slug: v1-user-read
url: https://dev.sprinklr.com/v1-user-read
---

# User Read

#
  GET - User Read

Using this API, you can fetch an existing user details using:

- Unique user Id

- Unique user name (encoded email address)

- Unique federation Id

## 1. Read User by User Id

Using this API endpoint, you can fetch user details using the unique user Id.

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/scim/v2/Users/{userId}

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


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userId | Required | Refers to the unique Sprinklr user Id | String |

## Example - Request














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/scim/v2/Users/189367' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}'






## Example - Response





{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User"
    ],
    "userName": "bill.mcdaniel+GKC@sprinklr.com",
    "name": {
        "familyName": "McDaniel",
        "givenName": "Bill"
    },
    "photos": [
        {
            "value": ""
        }
    ],
    "active": true,
    "locale": "EN_US",
    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User": {
        "partnerCustomProperties": {},
        "passwordLoginDisabled": false
    },
    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User": [
        {
            "clientId": 5547,
            "userType": "PRTADMN",
            "phoneNumbers": [
                {}
            ],
            "businessCategory": "CORPORATE",
            "userGroupIds": [
                "5ad5d51de4b071a3ec2c4b67",
                "57101edae4b0ff003ffd4daa"
            ]
        }
    ],
    "id": "189367",
    "meta": {
        "resourceType": "User",
        "createdTime": "2018-12-17 20:37:46.0",
        "lastModified": "2018-12-18 19:16:46.0"
    }
}





## 2. Read User by User Name

Using this API, you can fetch an existing user details using the user name.

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/scim/v2/Users/userName/{userName}

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



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userName | Required | The email id of an existing user.User Name of the user would be their email address. Email address of the user should be URL encoded.Example: bill.mcdaniel%40sprinklr.com | String |

## Example - Request














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/scim/v2/Users/userName/bill.mcdaniel%40sprinklr.com' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}'






## Example - Response





{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User"
    ],
    "userName": "bill.mcdaniel+GKC@sprinklr.com",
    "name": {
        "familyName": "McDaniel",
        "givenName": "Bill"
    },
    "photos": [
        {
            "value": ""
        }
    ],
    "active": true,
    "locale": "EN_US",
    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User": {
        "partnerCustomProperties": {},
        "passwordLoginDisabled": false
    },
    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User": [
        {
            "clientId": 5547,
            "userType": "PRTADMN",
            "phoneNumbers": [
                {}
            ],
            "businessCategory": "CORPORATE",
            "userGroupIds": [
                "57101edae4b0ff003ffd4daa",
                "5ad5d51de4b071a3ec2c4b67"
            ]
        }
    ],
    "id": "189367",
    "meta": {
        "resourceType": "User",
        "createdTime": "2018-12-17 20:37:46.0",
        "lastModified": "2018-12-18 19:16:46.0"
    }
}





## 3. Read User by Federation ID

Using this API, you can fetch user details using the unique Federation Id. A user within a workspace may have registered with more than one email address. Assigning a federation ID helps in unique identification. You cannot assign the same federation identity to more than one user across the client within the same workspace.

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/scim/v2/Users/federationId/{federationId}

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


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| federationId | Required | The federation id of the user. | String |

## Example - Request














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/scim/v2/Users/federationId/764301' \
  -H 'Authorization: Bearer {token}' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}'






## Example - Response





{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User"
    ],
    "userName": "ben.turner+fedID@sprinklr.com",
    "name": {
        "familyName": "Turner",
        "givenName": "Ben"
    },
    "photos": [
        {
            "value": "https://sprcdn-assets.sprinklr.com/1090/avatar-default-bbab64be-284f-4f8e-9cee-1cb8bc436a1d-456917368_p.png"
        }
    ],
    "active": true,
    "locale": "EN_US",
    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User": {
        "partnerCustomProperties": {},
        "federationId": "764301",
        "passwordLoginDisabled": false
    },
    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User": [
        {
            "clientId": 5547,
            "userType": "CLIUSER",
            "phoneNumbers": [
                {}
            ],
            "businessCategory": "CORPORATE",
            "primaryUserGroupId": "5ad5d51de4b071a3ec2c4b67",
            "userGroupIds": [
                "5ad5d51de4b071a3ec2c4b67"
            ]
        }
    ],
    "id": "190660",
    "meta": {
        "resourceType": "User",
        "createdTime": "2019-01-07 18:57:55.0",
        "lastModified": "2019-01-07 18:57:55.0"
    }
}





[](https://dev.sprinklr.com/v1-user-read)




[Back to top](https://dev.sprinklr.com/v1-user-read)
