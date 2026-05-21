---
title: "User Search"
slug: v1-user-search
url: https://dev.sprinklr.com/v1-user-search
---

# User Search

#
  POST - User Search

You can use this API call to search users within Sprinklr. As a response, you will get the list of users' objects that match your search request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/scim/v2/Users/search

**Dev Notes: **By default, the API will return only 100 rows of data irrespective of number of email addresses the are put into the request payload

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




































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userNames | Required | Users email list. | List <String> |
| federationIds | Optional | List of federation Ids of users. | List <String> |
| Ids | Optional | List of sprinklr user IDs. | List <String> |
| rows | Optional | This parameter can be used to expand the by default limit of 100 rows. Enter the value according to email Id used in the request payload | Integer |

## Example - Request














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/scim/v2/Users/search' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
    "userNames": [
        "ben.turner+fedID@sprinklr.com",
        "bill.mcdaniel+GKC@sprinklr.com",
        "aubrey.jones+GKC@sprinklr.com"
    ],
    "federationIds": [],
    "ids": []
}'





## Example - Response





[
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
    },
    {
        "schemas": [
            "urn:ietf:params:scim:schemas:core:2.0:User",
            "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
            "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User"
        ],
        "userName": "aubrey.jones+GKC@sprinklr.com",
        "name": {
            "familyName": "Jones",
            "givenName": "Aubrey"
        },
        "photos": [
            {
                "value": "http://prod.cdata.app.sprinklr.com/DAM/1090/Aubrey_crop-8150dc53-91e9-41a9-8e83-91ebac29b935-2129848458.jpg"
            }
        ],
        "active": true,
        "locale": "EN_US",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User": {
            "partnerCustomProperties": {
                "spr_user_availability_status": [
                    "Not Available"
                ]
            },
            "passwordLoginDisabled": false
        },
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User": [
            {
                "clientId": 5547,
                "userType": "PRTADMN",
                "phoneNumbers": [
                    {
                        "value": ""
                    }
                ],
                "businessCategory": "CORPORATE",
                "userGroupIds": [
                    "5ad5d51de4b071a3ec2c4b67",
                    "57101edae4b0ff003ffd4daa"
                ]
            }
        ],
        "id": "97769",
        "meta": {
            "resourceType": "User",
            "createdTime": "2016-09-29 05:47:19.0",
            "lastModified": "2018-12-28 15:05:34.0"
        }
    },
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
]





[](https://dev.sprinklr.com/v1-user-search)




[Back to top](https://dev.sprinklr.com/v1-user-search)
