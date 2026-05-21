---
title: "v1 User Update"
slug: v1-user-update
url: https://dev.sprinklr.com/v1-user-update
---

# v1 User Update

#
  PUT - User Update

Using this API, you can update user details for the given user Id.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/scim/v2/Users/update/{userId}

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


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userId | Required | The Id of the user. | String |

## Request Parameters

The following table describes the Request Parameters in use.












































			****





			****






















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userName | Required | The email of the user. | String |
| name | Required | The first and last name of the user. | Name object |
| photos | Optional | The user's avatar. | List of SCIM Objects |
| active | Optional | The status of the user. Default = FALSE | Boolean |
| is SpaceUser | Required | If true, the user will be created in space. | Boolean |
| customGlobalAttributes | Required | The global attributes of the user. Kindly check the Custom Global Attributes Description Table below. | Global Attribute Object |
| clientAttributes | Required | The client-level attributes of the user. Kindly check the Client Attributes Description Table below. | Client Attribute Object |
| locale | Optional | The location of the user. | String |
| createMissingClient | Optional | If true, create user for all the new clients specified in the request payload. | Boolean |
| deleteMissingClient | Optional | If true, delete user from all the clients which are not part of the request payload. | Boolean |

## Custom Global Attributes Sub Parameters

The following table describes the parameters within customGlobalAttributes object that can be used in Request Payload.

























		````



| Sub Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| partnerCustomProperties | Optional | The partner custom properties. | Map<String, List<String>> |
| federationId | Optional | This is required for SSO user | String |
| passwordLoginDisabled | Optional | By default false, In case of SSO user this need to be true along with federationId. | String |

## Client Attributes Sub Parameters

The following table describes the parameters within clientAttributes object that can be used in Request Payload.



















			``





			``








































| Sub Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| clientId | Required | The workspace Id in which you want to add user | Long |
| userType | Required | The type of user you want to create. PARTNER_ADMIN, PARTNER_USER,    CLIENT_ADMIN, CLIENT_USER | String |
| phoneNumbers | Optional | The object containing phone details. "phoneNumbers": [{ 		            "value": "170-807-5009", 		            "type": "work", 		            "primary": true 			}], | List<ScimObject> |
| clientCustomProperties | Optional | The client custom properties. | Map<String, List<String>> |
| businessCategory | Optional | The category of business. | String |
| designation | Optional | The designation of user. | String |
| department | Optional | The department of user. | String |
| userGroupIds | Optional | The user group Id to which you want to add the user you are creating. | Set<String> |
| primaryUserGroupId | Optional | The primary user group. | String |

## Example - Request














Copy Code




curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v1/scim/v2/Users/update/190709' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}' \
  -d '{
   "userName":"rishi.dhar+test@sprinklr.com",
   "id":"190709",
   "name":{
      "familyName":"Rishi",
      "givenName":"Dhar"
   },
   "active":true,
   "photos":[
      {
         "value":"http://vignette2.wikia.nocookie.net/parody/images/3/31/Despicable-me2-disneyscreencaps.com-1091.jpg/revision/latest?cb=20141105224502",
         "type":"work",
         "primary":true
      }
   ],
   "isSpaceUser": true,
   "customGlobalAttributes":{
 "partnerCustomPropertiesUpdateRequest": {
      "partnerCustomProperties": {
             "578c0ba6e4b0e329a48546bd": []
     }
   }
   },
   "clientAttributes":[
      {
         "clientId":5547,
         "userType":"CLIENT_USER",
         "clientCustomPropertiesUpdateRequest":{
         "clientCustomProperties": {
           "5b1e7b98e4b0eeecaf643da0": []
         }
         },
         "phoneNumbers":[
            {
               "value":"555-555-8377",
               "type":"work",
               "primary":true
            }
         ]
      }
   ]
   "createMissingClient": true,
   "deleteMissingClient": false
}'





## Example - Response





{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User"
    ],
    "userName": "rishi.dhar+test@sprinklr.com",
    "name": {
        "familyName": "Rishi",
        "givenName": "Dhar"
    },
    "photos": [
        {
            "value": "http://vignette2.wikia.nocookie.net/parody/images/3/31/Despicable-me2-disneyscreencaps.com-1091.jpg/revision/latest?cb=20141105224502"
        }
    ],
    "active": true,
    "locale": "EN_US",
    "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User": {
        "passwordLoginDisabled": false
    },
    "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User": [
        {
            "clientId": 5547,
            "userType": "CLIUSER",
            "phoneNumbers": [
                {
                    "value": "555-555-8377"
                }
            ],
            "businessCategory": "CORPORATE"
        }
    ],
    "id": "190709",
    "meta": {
        "resourceType": "User",
        "createdTime": "2019-01-07 21:46:34",
        "lastModified": "2019-01-07 22:04:14",
        "location": "/api/v3.1/scim/v2/Users/update/190709190709"
    }
}





[](https://dev.sprinklr.com/v1-user-update)




[Back to top](https://dev.sprinklr.com/v1-user-update)
