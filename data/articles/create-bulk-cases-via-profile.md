---
title: "Create Bulk Cases Via Profile"
slug: create-bulk-cases-via-profile
url: https://dev.sprinklr.com/create-bulk-cases-via-profile
---

# Create Bulk Cases Via Profile

#
  POST - Create Bulk Cases Via Profile


Using this API, you can create cases along with audience profiles in bulk. A maximum of 10 cases and associated profiles can be created using this API.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/case/bulk/profile

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
























































































					``

``











| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| subject |  | Optional | The subject of the case. | String |
| description |  | Optional | The desription of the case. | String |
| status |  | Optional | Refers to the status of the case.Example: New, Open, In Progress, Closed, etc. | String |
| workflow |  | Optional | The object contaning the workflow details. | Object |
|  | customProperties | Optional | The object contaning the custom properties details.. | String |
|  | queues | Optional | Partner queue details on the asset, if any. | Array |
|  | spaceWorkflows | Optional | List of client level workflows on the entity, if any. | List |
|  | campaignId | Optional | campaign identifier to associate the entity to. | String |
| channelType |  | Required | The channel type associated with profile (SMS, EMAIl,.etc). | String |
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

### Queue Array Definition Table











| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| queueId | OptionalRequired if you want to add the case to an existing queue | Refers to the unique identifier for the queue where the case needs to be added for assignment | Integer |

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
  'https://api3.sprinklr.com/{env}/api/v2/case/bulk/profile' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
    {
        "subject": "Subject 1",
        "description": "Description 1",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100090
                },
                {
                    "queueId": 100045
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test1@gmail.com",
            "fullName": "Test 1"
        }
    },
    {
        "subject": "Subject 2",
        "description": "Subject 2",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100087
                },
                {
                    "queueId": 100053
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test2@gmail.com",
            "fullName": "Test 2"
        }
    },
    {
        "subject": "Test 3",
        "description": "Subject 3",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100085
                },
                {
                    "queueId": 100058
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test3@gmail.com",
            "fullName": "Test 3"
        }
    },{
        "subject": "Test 4",
        "description": "Subject 4",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100085
                },
                {
                    "queueId": 100058
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test4@gmail.com",
            "fullName": "Test 4"
        }
    },{
        "subject": "Subject 5",
        "description": "Description 5",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100085
                },
                {
                    "queueId": 100058
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test5@gmail.com",
            "fullName": "Test 5"
        }
    },{
        "subject": "Subject 6",
        "description": "Description 6",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100085
                },
                {
                    "queueId": 100058
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test6@gmail.com",
            "fullName": "Test 6"
        }
    },{
        "subject": "Subject 7",
        "description": "Description 7",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100085
                },
                {
                    "queueId": 100058
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test7@gmail.com",
            "fullName": "Test 7"
        }
    },{
        "subject": "Subject 8",
        "description": "Description 8",
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_type": [
                    "Complaint"
                ],
                "spr_uc_priority": [
                    "High"
                ]
            },
            "queues": [
                {
                    "queueId": 100085
                },
                {
                    "queueId": 100058
                }
            ]
        },
        "channelType": "EMAIL",
        "contactInfo": {
            "email": "test8@gmail.com",
            "fullName": "Test 8"
        }
    }
]'



## Example - Response




{
    "data": {
        "Cases": [
            {
                "snUserId": "test2@gmail.com",
                "caseNumber": 6926006,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac47799e"
            },
            {
                "snUserId": "test3@gmail.com",
                "caseNumber": 6926009,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac4779a5"
            },
            {
                "snUserId": "test5@gmail.com",
                "caseNumber": 6926011,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac4779b9"
            },
            {
                "snUserId": "test4@gmail.com",
                "caseNumber": 6926007,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac47799f"
            },
            {
                "snUserId": "test6@gmail.com",
                "caseNumber": 6926012,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac4779ba"
            },
            {
                "snUserId": "test8@gmail.com",
                "caseNumber": 6926010,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac4779a6"
            },
            {
                "snUserId": "test1@gmail.com",
                "caseNumber": 6926008,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac4779a0"
            },
            {
                "snUserId": "test7@gmail.com",
                "caseNumber": 6926013,
                "snType": "EMAIL",
                "caseId": "64552edf0343ff15ac4779bb"
            }
        ]
    },
    "errors": []
}



### Response Parameters










| Parameter | Description | Type |
| --- | --- | --- |
| caseNumber | Refer to the case number for the newly created case | Integer |
| caseId | Refer to the unique identifier for the case | String |
| snType | Refers to the channel type for the created profile | String |
| snUserId | Refers to the unique profile id of the user | String |

[](https://dev.sprinklr.com/create-bulk-cases-via-profile)




[Back to top](https://dev.sprinklr.com/create-bulk-cases-via-profile)
