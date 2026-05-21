---
title: "Read Case by Case Id"
slug: read-case-by-case-id
url: https://dev.sprinklr.com/read-case-by-case-id
---

# Read Case by Case Id

#
  GET - Read Case by Case Id

You can fetch a case details through case id with this API call. This call allows you to get case data in JSON.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/case/{caseId}


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

### Path Parameters















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| caseId | Required | Case Id of the case for which you want to fetch details. | String |

## Example - Request




 Copy Code



curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/case/00000197203b3fe5e4b0324aec609fcf \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example - Response




{
    "data": {
        "id": "00000197203b3fe5e4b0324aec609fcf",
        "caseNumber": 7030591,
        "subject": "#7030591 Sprinklr_voice ",
        "version": 350,
        "status": "Archived",
        "priority": "High",
        "externalCase": {
            "channelType": "SPRINKLR_VOICE",
            "modifiedTime": 1748592443434
        },
        "externalCaseInfo": {
            "externalCases": []
        },
        "workflow": {
            "assignment": {
                "assigneeId": "66007905",
                "assigneeType": "USER",
                "assignedById": 66008059,
                "assignmentTime": 1749111272934
            },
            "customProperties": {
                "is_tx_av": [
                    "true"
                ],
                "_c_64ed7c341456042a0261991f": [
                    "2078"
                ],
                "_c_68482905885675304d93e596": [
                    "87951dad-8241-f011-b4cb-6045bd038581"
                ],
                "_c_67f4ff429f46e2633754991c": [
                    "test12345"
                ],
                "spr_uc_priority": [
                    "High"
                ],
                "_c_68380cdb8fe7d60d4e624d83": [
                    "Salesforce"
                ],
                "_c_64defe8a59f4f4171e2ee5c7": [
                    "fr"
                ],
                "spr_uc_tag": [
                    "test123"
                ],
                "_c_64e3a126ef3e953c1abde084": [
                    "asd"
                ],
                "_c_682337c8200a494ab9bec5c9": [
                    "null"
                ],
                "spr_uc_status": [
                    "Archived"
                ],
                "_c_6846cddb8768e47afed36e66": [
                    "2"
                ],
                "spr_uc_last_assigned_agent": [
                    "66007905"
                ]
            },
            "queues": []
        },
        "channelCustomProperties": [],
        "contact": {
            "id": "SPRINKLR_VOICE___SPR_DEFAULT_PROFILE__",
            "channelType": "SPRINKLR_VOICE",
            "channelId": "__SPR_DEFAULT_PROFILE__",
            "fromSnUserId": "__SPR_DEFAULT_PROFILE__"
        },
        "createdTime": 1870316100000,
        "modifiedTime": 1749644307104,
        "firstMessageId": "VOICE_66124440_1870316106825_SPRINKLR_VOICE_384_00000197203b3fe5e4b0324aec609fcf_recording_2048c2432c24b3d7e1464b7a273d202387ca104f875f6086b067aa0d2cdc9d55",
        "latestProfileMessageAssociatedTime": 0,
        "conversationId": "0000019720ef0af5e4b08d974f6611e8",
        "firstMessageAssociatedTime": 1870316106825,
        "latestMessageAssociatedTime": 1748604239691,
        "firstUserBrandResponseCreationTime": 1870316106825,
        "avgCaseResponseSLA": 2113,
        "totalProcessingClockTime": 254565126,
        "allEngagedUsersList": [
            "66064014",
            "66007905"
        ],
        "associatedFanMessageCount": 1,
        "associatedBrandMessageCount": 5,
        "associatedUserBrandMessageCount": 4,
        "deleted": false
    },
    "errors": []
}





## Response Parameters






| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| subject | The value of the subject field for this case | String |
| description | Description of the case | String |
| version | version number | Integer |
| status | The state of the case. e.g. Open, Pending, Closed | String |
| priority | The Urgency of the case with which case should be addressed | String |
| caseType | The type of the case. e.g. Problem, Incident, Task | String |
| externalCase | Describes the schema for third party cases linked to universal case in sprinklr. External case description table given below. | String, Integer |
| workflow | Describes the schema of partner level workflow in message/case. Workflow description table given below. | String, Integer |
| contact | Describes the schema of contact in Case. Contact description table given below. | String |
| attachment | Type of attachment. Attachment description table given below. | String, Integer |
| dueDate | If case needs to be resolved within time limit then it has a due date. | Integer |
| summary | Case summary | Integer |
| createdTime | created time of the case | Integer |
| modifiedTime | last modified time of the case | Integer |
| firstMessageId | message key for the first messages associated to the case. | String |
| latestMessageAssociatedTime | Timestamp of latest message associated with the case. | Integer |
| firstUserBrandResponseCreationTime | Timestamp of the first user-brand response. | Integer |
| avgCaseResponseSLA | Average case response SLA in milliseconds. | Integer |
| totalProcessingClockTime | Total processing time for the case in milliseconds. | Integer |
| allEngagedUsersList | List of user IDs engaged with the case. | Array of Strings |
| associatedFanMessageCount | Number of fan messages associated with the case. | Integer |
| associatedBrandMessageCount | Number of brand messages associated with the case. | Integer |
| associatedUserBrandMessageCount | Number of user-brand messages associated with the case. | Integer |
| deleted | Indicates if the case has been deleted. | Boolean |

##  External Case



| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| channelType | channel type. e.g salesforce, zendesk, rightnow | String |
| permalink | link to the case on channel | String |
| createdTime | created time of the case on channel | Integer |
| modifiedTime | last modified time of the case on channel | Integer |

##  Workflow



-
-
-
-

-
-

-
-
-
-

| Parameter | Description | Type |
| --- | --- | --- |
| assignment | description:Assignment details of Workflow on message/case  assigneeId(string):  Describes the id of assignee. assigneeType(string): Describes the assignee type. e.g. USER, BOT  assignedById(Integer): Describes the assigned by user id. assignmentTime(Integer): Assignment time. | String, Integer |
| modifiedTime | Last modified time of the workflow | Integer |
| customFields | Partner custom properties on the asset, if any. | String |
| queues | Partner queue details on the asset, if any.  queueId(Integer):queue identifier to add the message to queue. assignmentTime(Integer): assignment time of the queue to the message. | String, Integer |
| spaceWorkflows | List of client level workflows on the asset, if any.         spaceId(string):  client id  modifiedTime(Integer): Last modified time of the space workflow.  customFields(String):Client custom properties on the asset, if any.  queues(Integer): As defined above. | String, Integer |
| campaignId | campaign identifier to associate the message to | String |

##  Contact



| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of contact | string |
| name | Name of the contact | string |

##  Attachment



-

-

| Parameter | Description | Type |
| --- | --- | --- |
| type | Type of attachment [ IMAGE, VIDEO ] | String |
| attachmentOptions | Array of attachment properties per channel and/or account.    channelType(String): ChannelType for media options.  Enum: [ FACEBOOK, TWITTER ]  accountId(Integer): If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | String, Integer |

[](https://dev.sprinklr.com/read-case-by-case-id)






[Back to top](https://dev.sprinklr.com/read-case-by-case-id)
