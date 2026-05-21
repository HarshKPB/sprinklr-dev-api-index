---
title: "Case Webhooks"
slug: case-webhooks
url: https://dev.sprinklr.com/case-webhooks
---

# Case Webhooks

#
 Case Webhooks

 Sprinklr offers a variety of robust, convenient, and simple Webhooks Subscriptions to get event updates instantaneously. You can subscribe for Case Webhooks via API or Sprinklr UI. Whenever a case action is performed on a customer message, the Sprinklr will send an HTTP POST request triggered notification to the Webhook URL that you have provided while creating the subscription.

	**Case Webhook Subscriptions:** Create, Update, Delete, Message Association Change

Whenever a case action is performed either via Sprinklr UI or API, webhook notification are triggered with the details that are described in the following documents:


- [Case.Create Webhook](https://dev.sprinklr.com/case-webhooks#caseCreate)

- [Case.Update Webhook](https://dev.sprinklr.com/case-webhooks#caseUpdate)

- [Case.Delete Webhook](https://dev.sprinklr.com/case-webhooks#caseDelete)

- [Message.Association.Change Webhook](https://dev.sprinklr.com/case-webhooks#caseMAC)


## Case.Create Webhook

#### JSON Response




  Copy Code

{
  "id": "5ed48fad70906b72b8184d67",
  "type": "case.create",
  "payload": {
    "id": "5ed48fac70906b72b8184d62",
    "caseNumber": 25233207,
    "subject": "Sumit Kaushik",
    "description": "hello",
    "version": 0,
    "status": "New",
    "priority": "Medium",
    "workflow":{
      "customProperties": {},
      "queues": []
    },
    "contact": {
      "id": "WHATSAPP_BUSINESS_917974027750",
      "name": "Sumit Kaushik"
    },
    "createdTime": 1590988716926,
    "modifiedTime": 1590988716977,
    "firstMessageId": "ACCOUNT_269798_1590988688000_WHATSAPP_BUSINESS_316_ABEGkXl0AndQAhCqytzBsB3GKJ9zBb30-lhH",
    "sentiment": 0,
    "latestProfileAUMSnCreatedTime": 1590988688000
  },
  "eventTime": 1590988717020,
  "subscriptionDetails": {
    "subscriptionId": "5ed48f2d70906b72b8183917"
  }
}



**Dev Notes: **In most of the cases (exception: create case via API), the assignment object is not included in the case.create webhook response. Because when the case gets created, the assignment engine follows pre-configured criteria to assign the case to the available agent. Once assigned, the assignment object details can be fetched from the case.update webhook response.

### Business Object Response Definitions














































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| subject | The value of the subject field for this case | String |
| description | Description of the case | String |
| version | version number |  |
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
| sentiment | Sentiment of the message on which case is created. | String |
| eventTime | Event occuring time in Epoch. | String |
| subscriptionId | Webhook subscription Id. | String |

### External Case







































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| channelType | channel type. e.g salesforce, zendesk, rightnow | String |
| permalink | link to the case on channel | String |
| createdTime | created time of the case on channel | Integer |
| modifiedTime | last modified time of the case on channel | Integer |

### Workflow











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
| assignment | description:Assignment details of Workflow on message/case 				 					assigneeId(string):  Describes the id of assignee. 					assigneeType(string): Describes the assignee type. e.g. USER, BOT  					assignedById(Integer): Describes the assigned by user id. 					assignmentTime(Integer): Assignment time. | String, Integer |
| modifiedTime | Last modified time of the workflow | Integer |
| customFields | Partner custom properties on the asset, if any. | String |
| queues | Partner queue details on the asset, if any. 				 queueId(Integer):queue identifier to add the message to queue. 				assignmentTime(Integer): assignment time of the queue to the message. | String, Integer |
| spaceWorkflows | List of client level workflows on the asset, if any.        					  				 					spaceId(string):  client id 					 modifiedTime(Integer): Last modified time of the space workflow.  					customFields(String):Client custom properties on the asset, if any. 					 queues(Integer): As defined above. | String, Integer |
| campaignId | campaign identifier to associate the message to | String |

### Contact



















| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of contact | string |
| name | Name of the contact | string |

### Attachment















-

-




| Parameter | Description | Type |
| --- | --- | --- |
| type | Type of attachment [ IMAGE, VIDEO ] | String |
| attachmentOptions | Array of attachment properties per channel and/or account.  					  				 					 channelType(String): ChannelType for media options. Enum: [ FACEBOOK, TWITTER ]  					 accountId(Integer): If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | String, Integer |


## Case.Update Webhook

#### JSON Response




  Copy Code

{
  "id": "5ed48fd770906b72b8185453",
  "type": "case.update",
  "payload": {
    "id": "5ed48fac70906b72b8184d62",
    "caseNumber": 25233207,
    "subject": "Sumit Kaushik",
    "description": "hello",
    "version": 3,
    "status": "New",
    "priority": "Medium",
    "workflow": {
      "assignment": {
        "assigneeId": "242077",
        "assigneeType": "USER",
        "assignedById": 242077,
        "assignmentTime": 1590988716926
      },
      "customProperties": { },
      "queues": []
    },
    "contact": {
      "id": "WHATSAPP_BUSINESS_917974027750",
      "name": "Sumit Kaushik"
    },
    "summary": "new case",
    "createdTime": 1590988716926,
    "modifiedTime": 1590988759397,
    "firstMessageId": "ACCOUNT_269798_1590988688000_WHATSAPP_BUSINESS_316_ABEGkXl0AndQAhCqytzBsB3GKJ9zBv30-lhH",
    "sentiment": 0,
    "latestProfileAUMSnCreatedTime": 1590988688000
  },
  "eventTime": 1590988759433,
  "subscriptionDetails": {
    "subscriptionId": "5ed48f2d70906b72b8183917"
  }
}



 **Business Object Response Definitions:**














































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| subject | The value of the subject field for this case | String |
| description | Description of the case | String |
| version | version number |  |
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
| sentiment | Sentiment of the message on which case is created. | String |
| eventTime | Event occuring time in Epoch. | String |
| subscriptionId | Webhook subscription Id. | String |

### External Case







































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| channelType | channel type. e.g salesforce, zendesk, rightnow | String |
| permalink | link to the case on channel | String |
| createdTime | created time of the case on channel | Integer |
| modifiedTime | last modified time of the case on channel | Integer |

### Workflow











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
| assignment | description:Assignment details of Workflow on message/case 				 					assigneeId(string):  Describes the id of assignee. 					assigneeType(string): Describes the assignee type. e.g. USER, BOT  					assignedById(Integer): Describes the assigned by user id. 					assignmentTime(Integer): Assignment time. | String, Integer |
| modifiedTime | Last modified time of the workflow | Integer |
| customFields | Partner custom properties on the asset, if any. | String |
| queues | Partner queue details on the asset, if any. 				 queueId(Integer):queue identifier to add the message to queue. 				assignmentTime(Integer): assignment time of the queue to the message. | String, Integer |
| spaceWorkflows | List of client level workflows on the asset, if any.        					  				 					spaceId(string):  client id 					 modifiedTime(Integer): Last modified time of the space workflow.  					customFields(String):Client custom properties on the asset, if any. 					 queues(Integer): As defined above. | String, Integer |
| campaignId | campaign identifier to associate the message to | String |

### Contact



















| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of contact | string |
| name | Name of the contact | string |

### Attachment















-

-




| Parameter | Description | Type |
| --- | --- | --- |
| type | Type of attachment [ IMAGE, VIDEO ] | String |
| attachmentOptions | Array of attachment properties per channel and/or account.  					  				 					 channelType(String): ChannelType for media options. Enum: [ FACEBOOK, TWITTER ]  					 accountId(Integer): If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | String, Integer |

## Case.Delete Webhook

#### JSON Response




  Copy Code

{
  "id": "5ed490d870906b72b8188354",
  "type": "case.delete",
  "payload": {
    "id": "5ed48fac70906b72b8184d62",
    "caseNumber": 25233207,
    "subject": "Sumit Kaushik",
    "description": "hello",
    "version": 10,
    "status": "New",
    "priority": "Medium",
    "workflow": {
      "assignment": {
        "assigneeId": "242077",
        "assigneeType": "USER",
        "assignedById": 242077,
        "assignmentTime": 1590988716926
      },
      "customProperties": { },
      "queues": []
    },
    "contact": {
      "id": "WHATSAPP_BUSINESS_917974027750"
    },
    "summary": "new case",
    "createdTime": 1590988716926,
    "modifiedTime": 1590989016535,
    "firstMessageId": "ACCOUNT_269798_1590988688000_WHATSAPP_BUSINESS_316_ABEGkXl0AndQAhCqytzBsB3GKJ9zBv30-lhH",
    "sentiment": 0,
    "latestProfileAUMSnCreatedTime": 1590988894000
  },
  "eventTime": 1590989016569,
  "subscriptionDetails": {
    "subscriptionId": "5ed48f2d70906b72b8183917"
  }
}



### Business Object Response Definitions














































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| subject | The value of the subject field for this case | String |
| description | Description of the case | String |
| version | version number |  |
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
| sentiment | Sentiment of the message on which case is created. | String |
| eventTime | Event occuring time in Epoch. | String |
| subscriptionId | Webhook subscription Id. | String |

### External Case







































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| channelType | channel type. e.g salesforce, zendesk, rightnow | String |
| permalink | link to the case on channel | String |
| createdTime | created time of the case on channel | Integer |
| modifiedTime | last modified time of the case on channel | Integer |

### Workflow











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
| assignment | description:Assignment details of Workflow on message/case 				 					assigneeId(string):  Describes the id of assignee. 					assigneeType(string): Describes the assignee type. e.g. USER, BOT  					assignedById(Integer): Describes the assigned by user id. 					assignmentTime(Integer): Assignment time. | String, Integer |
| modifiedTime | Last modified time of the workflow | Integer |
| customFields | Partner custom properties on the asset, if any. | String |
| queues | Partner queue details on the asset, if any. 				 queueId(Integer):queue identifier to add the message to queue. 				assignmentTime(Integer): assignment time of the queue to the message. | String, Integer |
| spaceWorkflows | List of client level workflows on the asset, if any.        					  				 					spaceId(string):  client id 					 modifiedTime(Integer): Last modified time of the space workflow.  					customFields(String):Client custom properties on the asset, if any. 					 queues(Integer): As defined above. | String, Integer |
| campaignId | campaign identifier to associate the message to | String |

### Contact



















| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of contact | string |
| name | Name of the contact | string |

### Attachment















-

-




| Parameter | Description | Type |
| --- | --- | --- |
| type | Type of attachment [ IMAGE, VIDEO ] | String |
| attachmentOptions | Array of attachment properties per channel and/or account.  					  				 					 channelType(String): ChannelType for media options. Enum: [ FACEBOOK, TWITTER ]  					 accountId(Integer): If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | String, Integer |

## Message.Association.Change Webhook

#### JSON Response




  Copy Code

{
  "id": "5ed490a370906b72b8187817",
  "type": "message.association.change",
  "payload": {
    "uCase": {
      "id": "5ed48fac70906b72b8184d62",
      "caseNumber": 25233207,
      "subject": "Sumit Kaushik",
      "description": "hello",
      "version": 7,
      "status": "New",
      "priority": "Medium",
      "workflow": {
        "assignment": {
          "assigneeId": "242077",
          "assigneeType": "USER",
          "assignedById": 242077,
          "assignmentTime": 1590988716926
        },
        "customProperties": { },
        "queues": []
      },
      "contact": {
        "id": "WHATSAPP_BUSINESS_917974027750",
        "name": "Sumit Kaushik"
      },
      "summary": "new case",
      "createdTime": 1590988716926,
      "modifiedTime": 1590988963223,
      "firstMessageId": "ACCOUNT_269798_1590988688000_WHATSAPP_BUSINESS_316_ABEGkXl0AndQAhCqytzBsB3GKJ9zBv30-lhH",
      "sentiment": 0,
      "latestProfileAUMSnCreatedTime": 1590988894000
    },
    "associatedMessageIds": [
      "ACCOUNT_269798_1590988894000_WHATSAPP_BUSINESS_316_ABEGkXl0AndQAhDxSfWTZYSwEbcIx3eIZT-1"
    ]
  },
  "eventTime": 1590988963223,
  "subscriptionDetails": {
    "subscriptionId": "5ed48f2d70906b72b8183917"
  }
}



### Business Object Response Definitions



















































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| subject | The value of the subject field for this case | String |
| description | Description of the case | String |
| version | version number |  |
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
| sentiment | Sentiment of the message on which case is created. | String |
| associatedMessageIds | Message ID of the message that gets associated message | String |
| eventTime | Event occuring time in Epoch. | String |
| subscriptionId | Webhook subscription Id. | String |

## External Case







































| Parameter | Description | Type |
| --- | --- | --- |
| id | Case id. | String |
| caseNumber | case number of the case | Integer |
| channelType | channel type. e.g salesforce, zendesk, rightnow | String |
| permalink | link to the case on channel | String |
| createdTime | created time of the case on channel | Integer |
| modifiedTime | last modified time of the case on channel | Integer |

### Workflow











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
| assignment | description:Assignment details of Workflow on message/case 				 					assigneeId(string):  Describes the id of assignee. 					assigneeType(string): Describes the assignee type. e.g. USER, BOT  					assignedById(Integer): Describes the assigned by user id. 					assignmentTime(Integer): Assignment time. | String, Integer |
| modifiedTime | Last modified time of the workflow | Integer |
| customFields | Partner custom properties on the asset, if any. | String |
| queues | Partner queue details on the asset, if any. 				 queueId(Integer):queue identifier to add the message to queue. 				assignmentTime(Integer): assignment time of the queue to the message. | String, Integer |
| spaceWorkflows | List of client level workflows on the asset, if any.        					  				 					spaceId(string):  client id 					 modifiedTime(Integer): Last modified time of the space workflow.  					customFields(String):Client custom properties on the asset, if any. 					 queues(Integer): As defined above. | String, Integer |
| campaignId | campaign identifier to associate the message to | String |

### Contact



















| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier of contact | string |
| name | Name of the contact | string |

### Attachment















-

-




| Parameter | Description | Type |
| --- | --- | --- |
| type | Type of attachment [ IMAGE, VIDEO ] | String |
| attachmentOptions | Array of attachment properties per channel and/or account.  					  				 					 channelType(String): ChannelType for media options. Enum: [ FACEBOOK, TWITTER ]  					 accountId(Integer): If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | String, Integer |

	 [](https://dev.sprinklr.com/case-webhooks)

[Back to top](https://dev.sprinklr.com/case-webhooks)
