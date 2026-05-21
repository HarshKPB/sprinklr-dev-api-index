---
title: "Case Update"
slug: case-update
url: https://dev.sprinklr.com/case-update
---

# Case Update

#
  PUT - Case Update

Using this API, you can update the case level standard and custom properties based on the update action defined in the API payload.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/case

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


























				``







| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| caseIds | OptionalRequired if case number is not passed in the request body | Case ids of cases that you need to updateYou can add multiple case Ids separated by comma. Please note that the properties added in the payload will be commonly updated for all the mentioned case Ids | List [String] |
| caseNumbers | OptionalRequired if case Id is not passed in the request body | Case numbers of cases that you need to updateYou can add multiple case numbers separated by comma. Please note that the properties added in the payload will be commonly updated for all the mentioned case numbers | List[Integer] |
| updateActions - To learn more about different updateActions, refer to the table below. | Required | Enum: 					 						[ SET_DUE_DATE, ASSIGN_TO_USER, ADD_PROPERTIES, SYNC_PROPERTIES, SYNC_SELECTED_PROPERTIES, REMOVE_PROPERTIES, ADD_QUEUES, SYNC_QUEUES, REMOVE_QUEUES, EDIT_SUBJECT, EDIT_DESCRIPTION, UPDATE_CHANNEL_DETAILS, UPDATE_CHANNEL_CASE_ID, SYNC_CHANNEL_CUSTOM_PROPERTIES, UPDATE_INSTALLED_APP_DETAILS, INCREMENT_PROPERTIES ] | Array |
| {updateField} | Required | Field/object containing the property name with respect to the provided update action along with the value you want to update it for | String/Object |

### UpdateActions and Corresponding Update Field










[Example 4](https://dev.sprinklr.com/case-update#example4)

| updateAction | Corresponding Update Field | Description | Type |
| --- | --- | --- | --- |
| EDIT_SUBJECT | subject | Refers to the updated subject of the case | String |
| EDIT_DESCRIPTION | description | Refers to the updated description of the case | String |
| ASSIGN_TO_USER | assignedTo | Refers to the user Id associated with the agent to whom you want to assign the case | Integer |
| SET_DUE_DATE | dueDate | Sets the due date by when the case should be resolved/closed | Epoch (Milliseconds) |
| ADD_PROPERTIES | addedCustomProperties | Adds a new property while also retaining the existing ones | Object |
| SYNC_SELECTED_PROPERTIES | syncedSelectedCustomProperties | Updates the custom field passed in the request payload, while also retain the existing ones | Object |
| SYNC_PROPERTIES | syncedCustomProperties | Only the custom field values passed in the request payload will be treated as final. If the existing custom fields are not added to the payload, those values will get overridden | Object |
| REMOVE_PROPERTIES | removedCustomProperties | Removes the custom properties added in the payload | Object |
| ADD_QUEUES | addedQueues | Adds new queue and associates it with the case | List [String] |
| REMOVE_QUEUES | removedQueues | Removes existing queue and disassociates it from the case | List [String] |
| SYNC_QUEUES | syncedQueues | The queues passed in the payload will be associated with the case. If any existing queue id is not passed in the case, it will get overridden | List [String] |
| SET_EXTERNAL_CASES | externalCases (Object) | Updates the external case channel propertiesKindly refer to the table below for externalCases object details | String |
| SYNC_CHANNEL_CUSTOM_PROPERTIES | syncedChannelCustomProperties | Syncs channel custom properties. Note that the properties not passed in the payload will get overridden | Object |
| UPDATE_INSTALLED_APP_DETAILS | installedAppUserId, installedAppId, installedAppOrgId | Updates installed app details such as user id, app id, or org Id | String |
| INCREMENT_PROPERTIES | incrementCustomProperties | Increments the value of a numeric custom property for a specified case. See . | Number |

## externalCases Object Description Table










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Optional | Refers to the external case Id | String |
| caseNumber | Optional | Refers to the external case number | String |
| channelType | Optional | Refers to the external case channel type | String |
| permalink | Optional | Refers to the permalink for the external case | String |
| createdTime | Optional | Refers to the time at which the case was created on the external platform | Integer (Epoch) |

## Example 1 - Request for Sync Selected Custom Properties




 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/case \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -d '{
    "caseNumbers": [
        "25636792"
    ],
    "syncedSelectedCustomProperties": {
        "_c_6915c1fcbcc3d050f77b9943": [
            "test1"
        ],
        "_c_6917174fcc00a8338f9fba67": [
            "nntest"
        ]
    },
    "updateActions": [
        "SYNC_SELECTED_PROPERTIES"
    ]
}'





## Example - Response




{
    "data": [
        {
            "id": "65490621c776c51f01e5a14d",
            "caseNumber": 7217797,
            "subject": "External Profile Case creation",
            "description": "Description of the case",
            "version": 13,
            "status": "Closed",
            "externalCaseInfo": {
                "externalCases": []
            },
            "workflow": {
                "assignment": {
                    "assigneeId": "1000157828",
                    "assigneeType": "USER",
                    "assignedById": 1000157828,
                    "assignmentTime": 1699284513821
                },
                "customProperties": {
                    "_c_64f1cdb57dd05e1c829ddcb1": [
                        "Yes"
                    ],
                    "_c_64dc855cfcb3587c7633bc5b": [
                        "No"
                    ]
                },
                "queues": [
                    {
                        "queueId": 103197,
                        "assignmentTime": 1699284513821
                    }
                ]
            },
            "channelCustomProperties": [],
            "contact": {
                "id": "EMAIL_searching123@gmail.com",
                "channelType": "EMAIL",
                "channelId": "searching123@gmail.com",
                "fromSnUserId": "searching123@gmail.com"
            },
            "createdTime": 1699284513821,
            "modifiedTime": 1699284638466,
            "totalProcessingClockTime": 54133200,
            "allEngagedUsersList": [
                "1000157828"
            ],
            "associatedFanMessageCount": 0,
            "associatedBrandMessageCount": 0,
            "deleted": false
        }
    ],
    "errors": []
}





## Example 2 - Request for Assigning/Reassigning Case




 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/case \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -d '{
    "caseNumbers": [
        "6917385"
    ],
    "updateActions": [
        "ASSIGN_TO_USER"
    ],
    "assignedTo": 1000157828
}'





## Example - Response




{
    "data": [
        {
            "id": "64425277bd07c65f76ce0eaf",
            "caseNumber": 6917385,
            "subject": "External Profile Case creation",
            "description": "64425277bd07c65f76ce0eaf",
            "version": 44,
            "status": "Assigned",
            "externalCase": {
                "id": "5002w00000oOMjEAAW",
                "caseNumber": "00001907",
                "channelType": "SALESFORCE",
                "permalink": "https://sprinklr-2a-dev-ed.develop.my.salesforce.com/5002w00000oOMjEAAW",
                "createdTime": 1700052987000
            },
            "externalCaseInfo": {
                "externalCases": []
            },
            "workflow": {
                "assignment": {
                    "assigneeId": "1000157828",
                    "assigneeType": "USER",
                    "assignedById": 1000157828,
                    "assignmentTime": 1700052619891
                },
                "customProperties": {
                    "_c_6195e9767cd7e5662ca10b71": [
                        "Test"
                    ]
                },
                "queues": [
                    {
                        "queueId": 105092,
                        "assignmentTime": 1682492108873
                    }
                ]
            },
            "channelCustomProperties": [],
            "contact": {
                "id": "EMAIL_searching123@gmail.com",
                "channelType": "EMAIL",
                "channelId": "searching123@gmail.com",
                "fromSnUserId": "searching123@gmail.com"
            },
            "createdTime": 1682068087426,
            "modifiedTime": 1700053001072,
            "totalProcessingClockTime": 14053710,
            "allEngagedUsersList": [
                "1000201223",
                "1000157828",
                "1000201224",
                "1000257762"
            ],
            "associatedFanMessageCount": 0,
            "associatedBrandMessageCount": 0,
            "deleted": false
        }
    ],
    "errors": []
}





## Example 3 - Request for Removing Queues




 Copy Code


curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/case \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -d '{
    "caseNumbers": [
        14462
    ],
    "updateActions": [
        "REMOVE_QUEUES"
    ],
    "removedQueues":["100073"]
}'



## Example - Response




{
    "data": [
        {
            "id": "6523e901edb45b580403fde9",
            "caseNumber": 14462,
            "subject": "Test",
            "description": "Test API",
            "version": 107,
            "status": "New",
            "priority": "Medium",
            "externalCase": {
                "id": "5002w00000nBfuGAAS",
                "caseNumber": "00004374",
                "channelType": "SALESFORCE",
                "permalink": "https://sprinklr-1d-dev-ed.develop.my.salesforce.com/5002w00000nBfuGAAS",
                "createdTime": 1696852224000,
                "modifiedTime": 1696852225554
            },
            "externalCaseInfo": {
                "externalCases": []
            },
            "workflow": {
                "assignment": {
                    "assigneeId": "66000020",
                    "assigneeType": "USER",
                    "assignedById": 100934542,
                    "assignmentTime": 1697091217738
                },
                "customProperties": {
                    "spr_uc_priority": [
                        "Medium"
                    ],
                    "spr_uc_status": [
                        "New"
                    ]
                },
                "queues": [
                    {
                        "queueId": 100072,
                        "assignmentTime": 1697089838743
                    }
                ]
            },
            "channelCustomProperties": [],
            "contact": {
                "id": "TWITTER_1402509033337024516",
                "name": "Test User",
                "channelType": "TWITTER",
                "channelId": "1402509033337024516",
                "fromSnUserId": "1402509033337024516"
            },
            "createdTime": 1696852225546,
            "modifiedTime": 1697450340249,
            "firstMessageId": "ACCOUNT_600046533_1696531224000_TWITTER_7_1710002013122044372",
            "sentiment": 0,
            "latestProfileMessageAssociatedTime": 1697198018000,
            "firstMessageAssociatedTime": 1696531224000,
            "latestMessageAssociatedTime": 1697197830000,
            "firstUserBrandResponseCreationTime": 1696856154000,
            "avgCaseResponseSLA": 99875500,
            "totalProcessingClockTime": 426950570,
            "allEngagedUsersList": [
                "66000020"
            ],
            "associatedFanMessageCount": 0,
            "associatedBrandMessageCount": 0,
            "deleted": true
        }
    ],
    "errors": []
}




## Example 4 - Increment Value of a Numeric Custom Property




 Copy Code


curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v2/case' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "caseNumbers": [
        "11495814"
    ],
    "incrementCustomProperties": {
        "_c_68d21dc38c11b11325833399": "10"
    },
    "updateActions": [
        "INCREMENT_PROPERTIES"
    ]
}'



## Example - Response



{
    "data": [
        {
            "id": "68d4d9cc65393f2a8efd25fb",
            "caseNumber": 11495814,
            "subject": "#11495814 Sprinklr_live_chat HELLO",
            "description": "HELLO",
            "version": 117,
            "status": "New",
            "externalCaseInfo": {
                "externalCases": []
            },
            "workflow": {
                "assignment": {
                    "assigneeId": "66008019",
                    "assigneeType": "USER",
                    "assignedById": 66008019,
                    "assignmentTime": 1758779891982
                },
                "customProperties": {
                    "spr_uc_predicted_csat_rating": [
                        "50"
                    ],
                    "spr_uc_status": [
                        "New"
                    ],
                    "spr_uc_last_assigned_agent": [
                        "66008019"
                    ],
                    "_c_68d21dc38c11b11325833399": [
                        "80"
                    ]
                },
                "queues": []
            },
            "channelCustomProperties": [
                {
                    "browser": "Chrome 14",
                    "device": "Computer",
                    "pageTitle": "Sprinklr Live Chat",
                    "pageUrl": "https://live-chat-static.sprinklr.com/test-html/index.html?appId=6824843755ae4842ffa40287_app_66123542&env=qa6",
                    "initiator": "User",
                    "ipAddress": "15.206.255.190",
                    "locale": "en",
                    "timeZone": "Asia/Calcutta",
                    "conversationClosed": "No",
                    "country": "IN",
                    "language": "en",
                    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
                    "channelType": "SPRINKLR_LIVE_CHAT"
                }
            ],
            "contact": {
                "id": "SPRINKLR_LIVE_CHAT_A_68d4d9b49eb1595a9bb0329c",
                "channelType": "SPRINKLR_LIVE_CHAT",
                "channelId": "A_68d4d9b49eb1595a9bb0329c",
                "fromSnUserId": "A_68d4d9b49eb1595a9bb0329c"
            },
            "createdTime": 1758779856426,
            "modifiedTime": 1759818468605,
            "firstMessageId": "ACCOUNT_66123542_1758779852783_SPRINKLR_LIVE_CHAT_313_68d4d9cc65393f2a8efd25fc",
            "sentiment": -1,
            "latestProfileMessageAssociatedTime": 1758779856300,
            "conversationId": "68d4d9cc65393f2a8efd25fb",
            "firstMessageAssociatedTime": 1758779852783,
            "latestMessageAssociatedTime": 1758779856300,
            "totalProcessingClockTime": 914541,
            "allEngagedUsersList": [
                "66008019"
            ],
            "associatedFanMessageCount": 1,
            "associatedBrandMessageCount": 12,
            "associatedUserBrandMessageCount": 0,
            "deleted": false,
            "conversationIntentIds": []
        }
    ],
    "errors": []
}




[](https://dev.sprinklr.com/case-update)






[Back to top](https://dev.sprinklr.com/case-update)
