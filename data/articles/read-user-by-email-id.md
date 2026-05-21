---
title: "Read User by Email ID"
slug: read-user-by-email-id
url: https://dev.sprinklr.com/read-user-by-email-id
---

# Read User by Email ID

#
  GET - Read User by Email ID

	You can fetch a user through Email Id via this API call. After making the GET request, you will get the user details in JSON format as Response.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/email/{Email Id}

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

## Path Parameters

The following table describes the Request Parameters in use.


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| emailId | Required | The email id of the user on which you want to make a Read API call. | String |

**Dev Notes: **“userName” in Sprinklr is the user’s email address. This must be encoded in the request.

## Example - Request




 Copy Code


 
curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/scim/email/{emailId}' \
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
    "userName": "Sumit@sprinklr.com",
    "name": {
        "familyName": "Kaushik",
        "givenName": "Sumit"
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



 
**Dev Notes: ** When making a request to the API to retrieve user information, if the specified user email is not found in the database, the API will return a 404 error.
[](https://dev.sprinklr.com/read-user-by-email-id) 

 

 
[Back to top](https://dev.sprinklr.com/read-user-by-email-id)
