---
title: "Create Case"
slug: create-case
url: https://dev.sprinklr.com/create-case
---

# Create Case

#
  POST - Create Case

Using this API, you can create a case in Sprinklr and associate a message using the first message Id. Please note that a message should exist in Sprinklr for associating it with a case.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/case

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


























[Bootstrap Resources](https://dev.sprinklr.com/bootstrap-resources-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| firstMessageId | Required | Message id for the first message to be associated with the case | String |
| subject | Optional | The subject of the case. | String |
| description | Optional | The desription of the case. | String |
| priority | Optional | The Urgency of the case with which case should be addressed | String |
| caseType | Optional | The type of the case. e.g. Problem, Incident, Task | String |
| externalCase | Optional | Object defining the schema for third party cases linked to universal case in Sprinklr. External case description table given below. | Object |
| workflow | Required | Object describing the schema of partner level workflow in message/case. Workflow description table given below | Object |
| contact | Optional | Describes the schema of contact in Case. Contact description table given below. | Object |
| dueDate | Optional | If case needs to be resolved within time limit then it has a due date | Epoch |
| summary | Optional | Refers to the summary of the case | Integer |
| queues | Optional | A list of queues to which to send the case. Queues are used to store cases based on like conditions that can be configured and automated in the Rule Engine. You can think of queues as invisible folders that house and organise your cases.To fetch the queue ids, you can refer to  API documentation. | List [String] |

## External Case Description Table











| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id |  | Refers to the unique identifier for the external case | String |
| caseNumber |  | Refers to the case number associated with the external case | Integer |
| channelType |  | Refers to the external case source type, i.e., Zendesk, Salesforce, RightNow, etc. | String |
| permalink |  | Refers to the link to the external case | String |
| createdTime |  | Refers to the time at which the case was created on the external channel | Epoch |
| modifiedTime |  | Refers to the time at which the case was modified on the external channel | Epoch |

## workflow Object Description Table












| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| assignment |  | Optional | Object containing the case assignment details | Object |
|  | assigneeId | Required | The user Id of the user you want to assign the case to | Integer |
|  | assigneeType | Optional | Refers to the assignee type | String |
|  | assignedById | Optional | The user id of the user who assigned the case | Integer |
|  | assignmentTime | Optional | Refers to the time at which the case was assigned | Epoch |
| customProperties |  | Required | Refers to the custom properties of the case | Object containing the key and values' pair for custom field name and the respective values |

## Contact Parameters' Description Table











| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Unique identifier for the contact | String |
| name | Optional | Name of the contact | String |

## Example - Request




 Copy Code



 curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/case' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "subject": "API3.0 Case creation",
    "description": "This case is created with API3.012",
    "firstMessageId": "ACCOUNT_600001824_1582817880350_TWITTER_2_1233053677281304578",
    "priority": "high",
    "summary": "Urgent Case",
    "caseType": "Incident",
    "dueDate": 0,
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
        "queues": []
    }
}'





## Example - Response




"data": {
        "id": "633a9f1ce980b61e49f80adb",
        "caseNumber": 18005076,
        "subject": "API3.0 Case creation",
        "description": "This case is created with API3.012",
        "version": 0,
        "status": "New",
        "priority": "high",
        "caseType": "Incident",
        "externalCaseInfo": {
            "externalCases": []
        },
        "workflow": {
            "customProperties": {
                "spr_uc_type": [
                    "Incident"
                ],
                "spr_uc_priority": [
                    "high"
                ],
                "spr_uc_status": [
                    "New"
                ]
            },
            "queues": []
        },
        "channelCustomProperties": [],
        "contact": {},
        "attachment": {
            "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
            "previewUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
            "type": "IMAGE"
        },
        "dueDate": 0,
        "summary": "Urgent case",
        "createdTime": 1664786204436,
        "modifiedTime": 1664786204517,
        "firstMessageId": "ACCOUNT_600001824_1582817880350_TWITTER_2_1233053677281304578",
        "latestProfileMessageAssociatedTime": 0,
        "firstMessageAssociatedTime": 1582817880350,
        "latestMessageAssociatedTime": 1582817880350,
        "totalProcessingClockTime": 0,
        "allEngagedUsersList": []
    },
    "errors": []
}





## Response Parameters










****

| Parameter | Description | Type |
| --- | --- | --- |
| id | Refers to the unique identifier for the case created | String |
| caseNumber | Refers to the case number assigned to the case created | Integer |
| subject | Refers to the subject of the issue for which the case has been created | String |
| description | Refers to the description of the issue highlighted in the case | String |
| version | Refers to the version number of the case | Integer |
| status | Refers to the status of the case.Example: New, Open, Closed, etc. | String |
| priority | The Urgency of the case with which case should be addressed | String |
| caseType | The type of the case. e.g. Problem, Incident, Task | String |
| externalCase | Object describing the schema for third party cases linked to universal case in Sprinklr.External case description table given below. | Object |
| workflow | Object describing the schema of partner level workflow in message/case.Workflow description table given below. | Object |
| queues | A list of queues to which to case is added.Queues are used to store cases based on like conditions that can be configured and automated in the Rule Engine. | List [Long] |
| channelCustomProperties | Refers to the custom properties associated with the channel |  |
| contact | Describes the schema of contact in Case. Contact description table given below | Object |
| dueDate | If case needs to be resolved within time limit then it has a due date | Epoch |
| summary | Refers to the case summary | String |
| createdTime | Refers to the time at which the case got created in Sprinklr | Epoch |
| modifiedTime | Refers to the time at which the case was last modified | Epoch |
| firstMessageId | Refers to the unique identifier for the message that got associated with the case | String |
| latestProfileMessageAssociatedTime | The last profile level message associated with the case. This could be the last message in the conversation. | Epoch |
| firstMessageAssociatedTime | The time at which the first message was associated with the case | Epoch |
| latestMessageAssociatedTime | The latest time at which the message was associated with the case | Epoch |
| totalProcessingClockTime | Whenever the agent opens the case, the processing clock time starts.This stores the total time taken from opening the case to closing it. | Epoch |
| allEngagedUsersList | List of users (corresponding userIds) involved in resolving the case | List [String] |

## External Case Response Parameters










| Parameter | Description | Type |
| --- | --- | --- |
| id | Refers to the external case's unique identifier for the case | String |
| caseNumber | Refers to the external case number | Integer |
| channelType | Refers to the source channel of the case. e.g Salesforce, Zendesk, Rightnow | String |
| permalink | Refers to the link of the external case | String |
| createdTime | Refers to the time at which the case was created on the channel | Epoch |
| modifiedTime | Refers to the time at which the case was lastmodified | Epoch |

## Contact Response Parameters










| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of contact | String |
| name | Name of the contact | String |

[](https://dev.sprinklr.com/create-case)




[Back to top](https://dev.sprinklr.com/create-case)
