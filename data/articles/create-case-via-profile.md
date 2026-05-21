---
title: "Create Case Via Profile"
slug: create-case-via-profile
url: https://dev.sprinklr.com/create-case-via-profile
---

# Create Case Via Profile

#
  POST - Create Case Via Profile


	A case in Sprinklr can be created on top of an External Profile (profile not existing in Sprinklr) using this API call. As response you will receive the complete case details.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/case/profile

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters


























****










































````
















































					``

``











| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| subject |  | Optional | The subject of the case. | String |
| description |  | Optional | The desription of the case. | String |
| status |  | Optional | Refers to the status of the case.Example: New, Open, In Progress, Closed, etc. | String |
| workflow |  | Optional | The object contaning the workflow details. | Object |
|  | customProperties | Optional | The object contaning the custom properties details. | String |
|  | queues | Optional | Partner queue details on the asset, if any. | List |
|  | spaceWorkflows | Optional | List of client level workflows on the entity, if any. | List |
|  | campaignId | Optional | campaign identifier to associate the entity to. | String |
| channelType |  | Required | The channel type associated with profile.Kindly note the channel type is case sensitive and should be passed in uppercase, i.e., SMS for sms channel type and EMAIL for email channel type. | String |
| channelId |  | OptionalRequired for all channels except EMAIL and SMS | Refers to the unique identifier for the customer profile and can be configured from client-side. This will be considered the social native user Id for the user and the primary key for the customer profile, i.e., if you pass the same channelId for 2 consecutive API calls, the first API will create a new case and a new customer profile and the second case will create a new case and associate it with the existing customer profile. | String |
| contactInfo |  | Required | The object of contaning detailed contact information associated with profile. | Object |
|  | email | Required for EMAIL channel typeOptional for SMS channel type | Email id of the profile | String |
|  | firstName | Optional | First name of the profile | String |
|  | lastName | Optional | Last name of the profile. | String |
|  | fullName | Optional | Full name of the profile. | String |
|  | phoneNo | Required for SMS channel typeOptional for EMAIL channel type | The phone number associated with profile. | String |
|  | website | Optional | The list of websites for the profile. | List<String> |
| commentDTO |  | Optional | Object containing the comment details (if any) | Object |
|  | attachments | Optional | Array containing the attachment details.Refer to the table below for array definition | Array |
|  | comment | Optional | Refers to the text of the comment if any | String |

### Attachment Array Definition Table











****

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of attachment.Supported Attachment Types: IMAGE, VIDEO, LINK, DOC, AUDIO | String |
| title | Optional | Refers to the title of the attachment | String |
| url | Required | Refers to the url of the attachment | URL |
| mimeType | Optional | Refers to attachment type and its format.Example: image/jpg | String |

## Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/case/profile' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "subject": "External Profile Case creation",
    "description": "Description of the case",
    "workflow": {
        "customProperties": {
            "spr_uc_status": [
                "New"
            ],
            "spr_uc_priority": [
                "High"
            ],
            "spr_uc_type": [
                "Complaint"
            ]
        },
        "queues": [
        {
            "queueId": 103197,
            "assignmentTime": 1681908874828
        }
     ]
     },
    "channelType": "SMS",
    "channelId": "+12024003935",
    "contactInfo": {
        "email": "abc@xyz.com",
        "firstName": "Sumit",
        "lastName": "K",
        "fullName": "Sumit K",
        "phoneNo":"9123000000",
        "website":["www.sprinklr.com","www.facebook.com"]
   },
    "commentDTO": {
        "attachments": [
            {
                "type": "IMAGE",
                "title": "Sample Image",
                "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg",
                "mimeType": "images/jpg"
           }
        ],
        "comment" : "Testing Comment Here"
    }
}'





## Example - Response




{
    "data": {
        "id": "61dbe8a7cb7b4d55717c0e91",
        "caseNumber": 9451320,
        "subject": "External Profile Case creation",
        "description": "Description of the case",
        "version": 0,
        "status": "New",
        "priority": "High",
        "caseType": "Complaint",
        "workflow": {
            "customProperties": {
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ],
                "spr_uc_status": [
                    "New"
                ],
                "spr_is_profile_case": [
                    "true"
                ]
            },
             "queues": [
           {
                "queueId": 103197,
                "assignmentTime": 1681908874828
          }
        ]
  },
        "channelCustomProperties": [],
        "contact": {
            "id": "SMS_9123121133"
        },
        "createdTime": 1641801895836,
        "modifiedTime": 1641801895843,
        "allEngagedUsersList": []
    },
    "errors": []
}





[](https://dev.sprinklr.com/create-case-via-profile)




[Back to top](https://dev.sprinklr.com/create-case-via-profile)
