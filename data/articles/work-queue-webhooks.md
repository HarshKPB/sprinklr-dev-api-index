---
title: "Work Queue Webhooks"
slug: work-queue-webhooks
url: https://dev.sprinklr.com/work-queue-webhooks
---

# Work Queue Webhooks

# Work Queue Webhooks

**Work Queue Webhook Subscriptions:**
 Work Queue Create, Work Queue Update, Work Queue Delete

Whenever a work queue is added, updated, or deleted from the Sprinklr platform, the respective webhooks get triggered.

- [work.queue.created Webhook](https://dev.sprinklr.com/work-queue-webhooks#WC)

- [work.queue.updated Webhook](https://dev.sprinklr.com/work-queue-webhooks#WU)

- [work.queue.deleted Webhook](https://dev.sprinklr.com/work-queue-webhooks#WD)

### Work Queue Create Webhook




  Copy Code



{
  "id": "668297cc1c5a642e983b6b16",
  "type": "work.queue.created",
  "payload": {
    "id": "668297c91c5a642e983b699c",
    "workQueueName": "Test Work Queue",
    "workQueueType": "UNIVERSAL_CASE",
    "assignmentProvider": "SPRINKLR",
    "routingStrategy": "SKILL_BASED_ROUTING",
    "users": [
      "66006268"
    ],
    "availableStatuses": [
      "Test Status"
    ],
    "stickinessStrategy": "CASE_LAST_ENGAGED",
    "stickinessTimeout": 86400000,
    "capacity": 0,
    "maxRejectionCountPerUser": 1,
    "activeConversationTimeout": 3600000,
    "stickinessCapacityCheck": true,
    "stickinessWaitTimeout": 0,
    "waitForAgentConfirmation": false,
    "deleted": false,
    "sortKey": "WORK_CREATION_TIME",
    "sortDirection": "ASC",
    "backupAssignmentStrategy": "MANUAL_ORDER",
    "backups": [],
    "ownerUserId": 66006268,
    "lastModifiedUserId": 66006268,
    "createdTime": 1719834569390,
    "modifiedTime": 1719834569390,
    "clientId": 66000002,
    "ruleIds": [
      "64f1dd656439ca188acffc33"
    ],
    "routingEvaluationMethod": "ALL_SKILL_MATCHING",
    "businessHoursId": "655e11bbe9abbe37dd2f3ce6",
    "shareConfigs": [
      {
        "type": "CLIENT",
        "ids": [
          "66000002"
        ]
      },
      {
        "type": "CLIENT_GROUP",
        "ids": []
      },
      {
        "type": "USER",
        "ids": []
      },
      {
        "type": "USER_GROUP",
        "ids": []
      }
    ],
    "description": "Work Queue Test",
    "smartAssignmentEnabled": false,
    "order": 0,
    "slaTargetTimeUnit": "SECONDS",
    "slaTargetDuration": 0,
    "slaTargetInTimeRangeDuration": 0,
    "slaTargetPercentage": 0
  },
  "eventTime": 1719834571958,
  "subscriptionDetails": {
    "subscriptionId": "668296fa1c5a642e983ae937"
  }
}





### Work Queue Update Webhook




  Copy Code



{
  "id": "6682990a1c5a642e983c330e",
  "type": "work.queue.updated",
  "payload": {
    "oldWorkQueue": {
      "workQueueId": "668297c91c5a642e983b699c",
      "workQueueName": "Test Work Queue 1",
      "lcName": "test work queue 1",
      "workQueueType": "UNIVERSAL_CASE",
      "assignmentProvider": "SPRINKLR",
      "routingStrategy": "SKILL_BASED_ROUTING",
      "users": [
        "66006268"
      ],
      "availableStatuses": [
        "Test Status"
      ],
      "stickinessAvailableStatuses": [],
      "stickinessStrategy": "CASE_LAST_ENGAGED",
      "stickinessTimeout": 86400000,
      "capacity": 0,
      "maxRejectionCountPerUser": 1,
      "maxRejectionCount": 3,
      "activeConversationTimeout": 3600000,
      "stickinessCapacityCheck": true,
      "stickinessWaitTimeout": 0,
      "waitForAgentConfirmation": false,
      "deleted": false,
      "sortKey": "WORK_CREATION_TIME",
      "sortDirection": "ASC",
      "backupAssignmentStrategy": "MANUAL_ORDER",
      "ownerUserId": 66006268,
      "lastModifiedUserId": 66006268,
      "createdTime": 1719834569390,
      "modifiedTime": 1719834569390,
      "clientId": 66000002,
      "ruleIds": [
        "64f1dd656439ca188acffc33"
      ],
      "routingEvaluationMethod": "ALL_SKILL_MATCHING",
      "businessHoursId": "655e11bbe9abbe37dd2f3ce6",
      "shareConfigs": [
        {
          "shareLevel": "CLIENT",
          "sharedWithIds": [
            "66000002"
          ]
        },
        {
          "shareLevel": "CLIENT_GROUP",
          "sharedWithIds": []
        },
        {
          "shareLevel": "USER",
          "sharedWithIds": []
        },
        {
          "shareLevel": "USER_GROUP",
          "sharedWithIds": []
        }
      ],
      "workQueueStats": {
        "totalAgents": 1,
        "totalCapacity": 100,
        "availableCapacity": 0,
        "pendingWorks": 0,
        "inProgressWorks": 0,
        "loadFactor": 0,
        "estimatedWorkQueueWaitTime": 0,
        "noOfAgentsAvailable": 0,
        "agentsOnCase": 0,
        "abandonmentRate": 0,
        "averageWaitTime": 0,
        "oldestAssignmentTime": 0,
        "totalCallsAnswered": 0,
        "totalCallsAbandoned": 0,
        "totalCalls": 0,
        "idleAgents": 0,
        "voiceAverageHandleTime": 0,
        "additionalStats": {
          "NUMBER_OF_AGENTS_LOGGED_IN_135": 1,
          "AUX_152": 100,
          "USER_CURRENT_STATE_COUNT": 1,
          "NUMBER_OF_AGENTS_IN_AUX_STATUS141": 1
        }
      },
      "description": "Work Queue Test",
      "smartAssignmentEnabled": false,
      "defaultWorkQueue": false,
      "order": 0,
      "slaTargetDuration": 0,
      "slaTargetInTimeRangeDuration": 0,
      "slaTargetPercentage": 0,
      "voiceConfigEnabled": false,
      "acdMigrated": false,
      "partnerCustomProperties": {
        "_c_66684620e08e057901a17d69": [
          "A"
        ]
      }
    },
    "newWorkQueue": {
      "workQueueId": "668297c91c5a642e983b699c",
      "workQueueName": "Test Work Queue",
      "lcName": "test work queue 1",
      "workQueueType": "UNIVERSAL_CASE",
      "assignmentProvider": "SPRINKLR",
      "routingStrategy": "SKILL_BASED_ROUTING",
      "users": [
        "66006268"
      ],
      "availableStatuses": [
        "Test Status"
      ],
      "stickinessAvailableStatuses": [],
      "stickinessTimeout": 86400000,
      "capacity": 0,
      "maxRejectionCountPerUser": 1,
      "maxRejectionCount": 3,
      "activeConversationTimeout": 3600000,
      "stickinessCapacityCheck": true,
      "stickinessWaitTimeout": 0,
      "waitForAgentConfirmation": false,
      "deleted": false,
      "sortKey": "WORK_CREATION_TIME",
      "sortDirection": "ASC",
      "backupAssignmentStrategy": "MANUAL_ORDER",
      "ownerUserId": 66006268,
      "lastModifiedUserId": 66006268,
      "modifiedTime": 1719834890046,
      "clientId": 66000002,
      "ruleIds": [
        "64f1dd656439ca188acffc33"
      ],
      "routingEvaluationMethod": "BEST_SKILL_MATCHING",
      "agentAvailabilityDetails": {
        "estimatedWaitTimeForWorkQueue": 0,
        "averageWaitTimeForWorkQueue": 0,
        "availableCapacityForWorkQueue": 0
      },
      "businessHoursId": "655e11bbe9abbe37dd2f3ce6",
      "shareConfigs": [
        {
          "shareLevel": "CLIENT",
          "sharedWithIds": [
            "66000002"
          ]
        },
        {
          "shareLevel": "CLIENT_GROUP",
          "sharedWithIds": []
        },
        {
          "shareLevel": "USER",
          "sharedWithIds": []
        },
        {
          "shareLevel": "USER_GROUP",
          "sharedWithIds": []
        }
      ],
      "workQueueStats": {
        "totalAgents": 0,
        "totalCapacity": 0,
        "availableCapacity": 0,
        "pendingWorks": 0,
        "inProgressWorks": 0,
        "loadFactor": 0,
        "estimatedWorkQueueWaitTime": 0,
        "noOfAgentsAvailable": 0,
        "agentsOnCase": 0,
        "abandonmentRate": 0,
        "averageWaitTime": 0,
        "oldestAssignmentTime": 0,
        "totalCallsAnswered": 0,
        "totalCallsAbandoned": 0,
        "totalCalls": 0,
        "voiceAverageHandleTime": 0,
        "additionalStats": {}
      },
      "routingConfigurations": [],
      "description": "Work Queue Test",
      "smartAssignmentEnabled": false,
      "defaultWorkQueue": false,
      "order": 0,
      "slaTargetTimeUnit": "SECONDS",
      "slaTargetDuration": 0,
      "slaTargetInTimeRangeDuration": 0,
      "slaTargetPercentage": 0,
      "voiceConfigEnabled": false,
      "acdMigrated": false,
      "partnerCustomProperties": {
        "_c_66684620e08e057901a17d69": [
          "A"
        ]
      }
    }
  },
  "eventTime": 1719834890219,
  "subscriptionDetails": {
    "subscriptionId": "668296fa1c5a642e983ae937"
  }
}





### Work Queue Delete Webhook




  Copy Code



{
  "id": "6682995b1c5a642e983c63fb",
  "type": "work.queue.deleted",
  "payload": {
    "id": "668297c91c5a642e983b699c",
    "workQueueName": "Test Work Queue",
    "workQueueType": "UNIVERSAL_CASE",
    "assignmentProvider": "SPRINKLR",
    "routingStrategy": "SKILL_BASED_ROUTING",
    "users": [
      "66006268"
    ],
    "availableStatuses": [
      "Test Status"
    ],
    "stickinessTimeout": 86400000,
    "capacity": 0,
    "maxRejectionCountPerUser": 1,
    "activeConversationTimeout": 3600000,
    "stickinessCapacityCheck": true,
    "stickinessWaitTimeout": 0,
    "waitForAgentConfirmation": false,
    "deleted": true,
    "sortKey": "WORK_CREATION_TIME",
    "sortDirection": "ASC",
    "backupAssignmentStrategy": "MANUAL_ORDER",
    "backups": [],
    "ownerUserId": 66006268,
    "lastModifiedUserId": 66006268,
    "modifiedTime": 1719834890046,
    "clientId": 66000002,
    "ruleIds": [
      "64f1dd656439ca188acffc33"
    ],
    "routingEvaluationMethod": "BEST_SKILL_MATCHING",
    "businessHoursId": "655e11bbe9abbe37dd2f3ce6",
    "shareConfigs": [
      {
        "type": "CLIENT",
        "ids": [
          "66000002"
        ]
      },
      {
        "type": "CLIENT_GROUP",
        "ids": []
      },
      {
        "type": "USER",
        "ids": []
      },
      {
        "type": "USER_GROUP",
        "ids": []
      }
    ],
    "description": "Work Queue Test",
    "smartAssignmentEnabled": false,
    "order": 0,
    "slaTargetTimeUnit": "SECONDS",
    "slaTargetDuration": 0,
    "slaTargetInTimeRangeDuration": 0,
    "slaTargetPercentage": 0
  },
  "eventTime": 1719834971319,
  "subscriptionDetails": {
    "subscriptionId": "668296fa1c5a642e983ae937"
  }
}





[](https://dev.sprinklr.com/work-queue-webhooks)

[Back to top](https://dev.sprinklr.com/work-queue-webhooks)
