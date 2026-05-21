---
title: "Read Case by Case Number"
slug: read-case-by-case-number
url: https://dev.sprinklr.com/read-case-by-case-number
---

# Read Case by Case Number

#
  GET - Read Case by Case Number

You can read a case through case number with this API call. This call allows you to get case data in JSON.
## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/case/case-numbers


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

### Query Parameters















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| case-number | Required | Case number of the case you want to fetch. | String |

## Example - Request




 Copy Code



curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/case/case-numbers?case-number=123 \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \





## Example - Response




{
  "id": "string",
  "caseNumber": 0,
  "subject": "string",
  "description": "string",
  "version": 0,
  "status": "string",
  "priority": "string",
  "caseType": "string",
  "externalCase": {
    "id": "string",
    "caseNumber": "string",
    "channelType": "string",
    "permalink": "string",
    "createdTime": 0,
    "modifiedTime": 0
  },
  "workflow": {
    "assignment": {
      "assigneeId": "string",
      "assigneeType": "string",
      "assignedById": 0,
      "assignmentTime": 0
    },
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
    "spaceWorkflows": [
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
        ]
      }
    ],
    "campaignId": "string"
  },
  "contact": {
    "id": "string",
    "name": "string"
  },
  "attachment": {
    "type": "IMAGE",
    "attachmentOptions": [
      {
        "channelType": "FACEBOOK",
        "accountId": 0
      }
    ]
  },
  "dueDate": 0,
  "summary": "string",
  "createdTime": 0,
  "modifiedTime": 0,
  "firstMessageId": "string"
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

[](https://dev.sprinklr.com/read-case-by-case-number)




[Back to top](https://dev.sprinklr.com/read-case-by-case-number)
