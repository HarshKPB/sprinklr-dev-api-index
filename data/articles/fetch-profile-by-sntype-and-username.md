---
title: "Fetch Profile by sntype and username"
slug: fetch-profile-by-sntype-and-username
url: https://dev.sprinklr.com/fetch-profile-by-sntype-and-username
---

# Fetch Profile by sntype and username

#
  GET Fetch Profile by sntype and username


	Using this API, you can fetch the data and metadata (stored in Sprinklr) associated with a profile for the given snType (channel type) and username (profile's user name).

## API Endpoint

https://api3.sprinklr.com/{env}api/v2/profile/search


### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```







[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |

### Query Parameters










[Channel Type](https://dev.sprinklr.com/channels-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| snType | Required | for the message. | String |
| userName | Required | User name of the profile.You can fetch the user name from the "Audience Profile" module on Sprinklr platform.For user name with spaces, kindly url-encode the username before passing it in the query parameters. | String |

## Example - Request















Copy Code


 curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/profile/search?snType=FACEBOOK&userName=Quick%20Test' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: application/json' \
  -H 'key: {apikey}'






## Example - Response





{
  "id": "string",
  "contact": {
    "firstName": "string",
    "maidenName": "string",
    "lastName": "string",
    "fullName": "string",
    "email": "string",
    "phoneNo": "string",
    "address": {
      "street1": "string",
      "street2": "string",
      "city": "string",
      "state": "string",
      "country": "string",
      "postalCode": "string"
    },
    "website": [
      "string"
    ]
  },
  "demographics": {
    "age": 0,
    "location": "string",
    "gender": "string",
    "language": "string"
  },
  "profiles": [
    {
      "name": "string",
      "channelType": "string",
      "channelId": "string",
      "permalink": "string",
      "avatarUrl": "string",
      "bio": "string",
      "followers": 0,
      "username": "string",
      "verified": false,
      "unSubscribed": false,
      "deleted": false,
      "snCreatedTime": 0,
      "snModifiedTime": 0,
      "accountSpecificInfos": [
        {
          "accountId": 0,
          "externalId": "string",
          "lastBrandEngagedTime": 0,
          "lastFanEngagedTime": 0,
          "optIn": false,
          "fanSubscriptionState": "string",
          "activeUser": false,
          "invited": false
        }
      ]
    }
  ],
  "profileWorkflow": {
    "profileLists": [
      0
    ],
    "customFields": {
      "additionalProp1": [
        "string"
      ],
      "additionalProp2": [
        "string"
      ],
      "additionalProp3": [
        "string"
      ]
    },
    "profileSpaceWorkflows": [
      {
        "spaceId": "string",
        "modifiedTime": 0,
        "customFields": {
          "additionalProp1": [
            "string"
          ],
          "additionalProp2": [
            "string"
          ],
          "additionalProp3": [
            "string"
          ]
        },
        "queues": [
          {
            "queueId": 0,
            "assignmentTime": 0
          }
        ],
        "profileLists": [
          0
        ]
      }
    ]
  },
  "createdTime": 0,
  "modifiedTime": 0
}







### Response Parameters











| Parameter | Sub Parameter | Description | Type |  |
| --- | --- | --- | --- | --- |
| id |  | Unique identifier of the unified profile. | String |  |
| contact |  | Contact information of the profile. |  |  |
|  | firstName | First name of the profile. | String |  |
|  | maidenName | Maiden name of the profile. | String |  |
|  | lastName | Last Name of the profile. | String |  |
|  | fullName | Full name of the profile. | String |  |
|  | email | Email id of the profile. | String |  |
|  | phoneNo | Phone number of the profile. | String |  |
|  | address | Address of the profile.Schema for Address Table given below. | String |  |
|  | website | List of websites for the profile. | String |  |
| demographics |  | Demographic Information of the client. |  |  |
|  | age | Age of the profile. | Integer |  |
|  | location | Location of the profile. | String |  |
|  | gender | Gender of the profile. | String |  |
|  | language | Language of the profile. | String |  |
| profiles |  |  | List of social identities linked to the profile. |  |
|  | name | Name of the person. | String |  |
|  | channelType | Channel type of the profile. e.g. facebook. | String |  |
|  | channelId | Unique id of the profile on channel. | String |  |
|  | permalink | Link of the profile on social channel. | String |  |
|  | avatarUrl | Profile image link. | String |  |
|  | bio | Detailed description about the user. | String |  |
|  | followers | Followers count of the user. | Integer |  |
|  | username | Unique identifier of the user. | String |  |
|  | verified | True if the user is verified by the channel. default: false | Boolean |  |
|  | unSubscribed | True if the user is subscribed for email and other activities.default: false | Boolean |  |
|  | deleted | True if profile is deleted natively.default: false | Boolean |  |
|  | snCreatedTime | Social Channel created time. | Integer |  |
|  | snModifiedTime | Social Channel modified time. | Integer |  |
|  | accountSpecificInfos | Account Specific Info like accountId, externalId, etc.Account Specific Info Table given below. |  |  |
| profileWorkflow |  |  |  |  |
|  | profileLists | Partner profile lists on the profile, if any. | Integer |  |
|  | customFields | Partner custom properties on the profile, if any. | Map<String, List<String>> |  |
|  | profileSpaceWorkflows | List of client level workflows on the profile, if any.ProfileSpaceWorkflow Table given below. |  |  |
| createdTime |  | Created time of the profile in sprinklr. | Integer |  |
| modifiedTime |  | Last modified time of the profile in sprinklr. | Integer |  |

 

### Address Parameter Description Table








| Parameter | Description | Type |
| --- | --- | --- |
| street1 | First line of the user's address. | String |
| street2 | Second line of the user's address. | String |
| city | The city of the user's address to help identify the location. | String |
| state | The state of the user's address. | String |
| country | The country of the user's address. | String |
| postalCode | ZIP Code of the address. | String |

### Account Specific Parameter Description Table








| Parameter | Description | Type |
| --- | --- | --- |
| accountId | Account id of the profile. | Integer |
| externalId | External id of the profile. | String |
| lastBrandEngagedTime | Last brand engagement time. | Integer |
| lastFanEngagedTime | Last fan engagement time. | Integer |
| optIn | If True, optin.default: false | Boolean |
| fanSubscriptionState | Subscription state of fan. | String |
| activeUser | If True, user id active.default: false | Boolean |
| invited | If True, invited.default: false | Boolean |

### Profile Space Workflow Parameter Description Table









| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| spaceId |  | Client Id. | String |
| modifiedTime |  | Last modified time of the space workflow | Integer |
| customFields |  | Client custom properties on the asset, if any. | String |
| queues |  | Client queue details of the message, if any. | Integer |
|  | queueId | Queue identifier to add the message to queue. | Integer |
|  | assignmentTime | Assignment time of the queue to the message. | Integer |
| profileLists |  | Client profile lists on the profile, if any. | Integer |

[](https://dev.sprinklr.com/fetch-profile-by-sntype-and-username)






[Back to top](https://dev.sprinklr.com/fetch-profile-by-sntype-and-username)
