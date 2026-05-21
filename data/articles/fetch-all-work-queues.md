---
title: "Fetch All Work Queues"
slug: fetch-all-work-queues
url: https://dev.sprinklr.com/fetch-all-work-queues
---

# Fetch All Work Queues

#
  GET  Fetch All Work Queues



All calls that require agent assignment need to pass through a queue in unified routing module. You'll find all the existing work queues within Unified routing that act as a virtual container for unassigned calls. This API helps fetch the work queues' details existing within the unified routing module.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/work-queue/getAllWorkQueues


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

## Example - Request















Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/work-queue/getAllWorkQueues'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
    "data": [
        {
            "id": "60ffcd2f5102d37ec10c3743",
            "workQueueName": "Live Chat - Skill Based",
            "workQueueType": "UNIVERSAL_CASE",
            "assignmentProvider": "SPRINKLR",
            "routingStrategy": "SKILL_BASED_ROUTING",
            "userGroups": [
                "60fab8574a753a69d3adf2b6"
            ],
            "users": [],
            "availableStatuses": [
                "Available"
            ],
            "stickinessStrategy": "CASE_LAST_ENGAGED",
            "stickinessTimeout": 3600000,
            "capacity": 0,
            "maxRejectionCountPerUser": 2,
            "activeConversationTimeout": 1800000,
            "stickinessCapacityCheck": true,
            "stickinessWaitTimeout": 5000,
            "waitForAgentConfirmation": false,
            "deleted": false,
            "sortKey": "WORK_LATEST_ACTIONED_TIME",
            "sortDirection": "ASC",
            "backupAssignmentStrategy": "MANUAL_ORDER",
            "backups": [],
            "lastModifiedUserId": 100148340,
            "createdTime": 1685520087880,
            "modifiedTime": 1685520087880,
            "ruleIds": [
                "6476fe5687a14548a2f323d8"
            ],
            "routingEvaluationMethod": "ALL_SKILL_MATCHING",
            "additional": {
                "stickinessTimeoutUnit": [
                    "HOURS"
                ],
                "activeConversationTimeoutUnit": [
                    "MINUTES"
                ],
                "stickinessWaitTimeoutUnit": [
                    "SECONDS"
                ]
            },
            "shareConfigs": [
                {
                    "type": "GLOBAL"
                }
            ],
            "smartAssignmentEnabled": false,
            "order": 0.0,
            "slaTargetTimeUnit": "SECONDS",
            "slaTargetDuration": 0,
            "slaTargetInTimeRangeDuration": 0,
            "slaTargetPercentage": 0.0,
            "voiceConfigEnabled": false
        }
    ],
    "errors": []
}







## Response Schema














































































































































































































































| Parameter | Sub-Parameter | Data Type | Description |
| --- | --- | --- | --- |
| data |  | Array | Contains the main data objects. |
|  | id | String | Refers to the ID of the workqueue in Sprinklr. |
|  | workQueueName | String | Refers to the name of the work queue. |
|  | workQueueType | String | Refers to the type of the work queue created (Case/Message/Task). Not relevant for Unified routing. |
|  | assignmentProvider | String | Refers to the name of the assignment provider (Sprinklr). |
|  | routingStrategy | String | Refers to the type of routing strategy used (Skill based/Queue based). Not relevant for Unified routing. |
|  | userGroups | Array | Refers to the user groups (IDs) added as the assignees of the work queue. |
|  | users | Array | Refers to the users (IDs) added as the assignees of the work queue. |
|  | availableStatuses | Array | Refers to the status which is considered to assign new cases for the assignees. |
|  | stickinessStrategy | String | Refers to the stickiness strategy in the work queue. |
|  | stickinessTimeout | Number | Refers to the time after the last message, till which the follow-up messages are considered as part of the same case/conversation and preference is given to the same agent (sticky agent) while assignment. |
|  | capacity | Number | Refers to the total cases that can be assigned to an agent in queue based routing work queue. Not relevant for Unified routing. |
|  | maxRejectionCountPerUser | Number | Refers to the maximum number of retries with a user. |
|  | activeConversationTimeout | Number | Refers to the time within the stickiness timeout for which agent (sticky agent) capacity could be breached by incoming sticky cases. |
|  | stickinessCapacityCheck | Boolean | Refers to the enablement of assignee capacity timeout. |
|  | stickinessWaitTimeout | Number | Refers to the time for which a task should wait to be assigned to the sticky agent, if it comes post active conversation timeout but within stickiness timeout. |
|  | waitForAgentConfirmation | Boolean | Not relevant for both unified routing/assignment engine. |
|  | deleted | Boolean | Refers to whether the work queue was deleted. |
|  | sortKey | String | Refers to the “Sort works by” defined in work queue. |
|  | sortDirection | String | Refers to the direction of sorting of cases in the work queue. By default it is ascending. |
|  | backupAssignmentStrategy | String | Refers to the strategy followed in assignment to backup queues. Not relevant for Unified routing. |
|  | backups | Array | Refers to the selected queues and assignees added as backup queues. Not relevant for Unified routing. |
|  | lastModifiedUserId | Number | Refers to the Sprinklr user who made the latest changes in the work queue. |
|  | createdTime | Number | Refers to the creation time of the work queue. |
|  | modifiedTime | Number | Refers to the latest modified time of the work queue. |
|  | ruleIds | Array | Refers to the rules that would be executed upon assignment of the work to a user. |
|  | routingEvaluationMethod | String | Refers to the routing type selected in the work queue. |
|  | additional | Object | Additional configuration details. |
|  | shareConfigs | Array | Refers to the sharing settings of the work queue (Workspace group/Workspace/User group/Users). |
|  | smartAssignmentEnabled | Boolean | Refers to whether smart assignment is enabled in the queue |
|  | smartAssignmentEnabledPercentage | Number | Refers to the percentage value set for smart assignment. |
|  | order | Number | Not relevant for both unified routing/assignment engine. |
|  | slaTargetTimeUnit | String | Refers to the SLA Target time unit in work queue. |
|  | slaTargetDuration | Number | Refers to the SLA Target time value set in work queue. |
|  | slaTargetInTimeRangeTimeUnit | String | Refers to the units of time set for SLA calculation duration. |
|  | slaTargetInTimeRangeDuration | Number | Refers to the value set for SLA calculation duration. |
|  | slaTargetPercentage | Number | Refers to the target % SLA set in work queue. |
|  | voiceConfigEnabled | Boolean | Refers to the enablement of voice in work queue. |
|  | partnerCustomProperties | Object | Custom properties for the partner. |
| errors |  | Array | List of errors, if any. |

[](https://dev.sprinklr.com/fetch-all-work-queues)




[Back to top](https://dev.sprinklr.com/fetch-all-work-queues)
