---
title: "Fetch Skill Based Work Queue Statistics"
slug: fetch-skill-based-work-queue-statistics
url: https://dev.sprinklr.com/fetch-skill-based-work-queue-statistics
---

# Fetch Skill Based Work Queue Statistics

#
 POST  Fetch Skill Based Work Queue Statistics



The Fetch Skill Based Work Queue Statistics API provides real-time insights into the availability and workload of agents assigned to skill-specific queues. This endpoint allows clients to evaluate queue performance based on skill, proficiency and task priority. By specifying skills and their minimum required proficiency, organizations can effectively route tasks and optimize resource allocation.

You can use this API for the following use cases:

- **Fetch Work Queue Statistics**: Retrieve metrics such as available agents, idle agents, logged-in agents, and more.

- **Channel Assignment Check**: Validate whether a case can be assigned to the specified work queue.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/work-queue/workQueueStatsSkillBased


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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Body Parameters












      ``



****

- ****
-
- ****
-
[Fetch All Work Queues](https://dev.sprinklr.com/fetch-all-work-queues)




      ``




****``
****``




      ``






      ``








| Parameter | Required/Optional | Type | Description | Applicable Use Case |
| --- | --- | --- | --- | --- |
| workQueueId | Required | String | Unique identifier for the work queue.                    Dev Notes: To obtain the work queue ID:                        Open Unified Routing > Queues.             Locate the work queue for which you want the ID.             Click Monitor Queue.             The ID is displayed at the end of the URL.                      You can also use  to get details of all work queues. Then search by name to find the desired ID. | Both use cases (statistics and channel assignment) |
| skillNameVsProficiency | Optional | Object | Key-value pairs where the key is the skill name and the value is the minimum required proficiency level.         Proficiency score refers to the proficiency level of the agent in the specified skill.         Proficiency score range: 1 - 100.         Example: "skillNameVsProficiency": { "English": 50 }         Multiple skills can be added as comma-separated values. | Fetch work queue statistics |
| priority | Optional | Integer | Priority level of the task. | Fetch work queue statistics |
| channelForAssignmentCheck | Optional | String | Specifies the channel through which assignment eligibility or validation should be evaluated.         Use standard Sprinklr channel names or a custom channel ID if applicable. | Channel assignment check |


**Dev Notes:** To get the flag **canAssignNewCase** in response, we need **workQueueId** and **channelForAssignmentCheck** as mandatory field, otherwise for skill based work queue stats, **channelForAssignmentCheck** is optional.



## Examples


### Example - Fetch Work Queue Statistics

#### Request















Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/work-queue/workQueueStatsSkillBased' \
--header 'Authorization: Bearer {access_token}’\
--header 'Key: {Api_Key} \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "skillNameVsProficiency":{
        "ABCTelekom_English":0
        }, "priority" : 100,
        "workQueueId":"6686e9e65b4c220b0b022079"
}'






#### Response




{
    "data": {
        "numberOfAvailableAgents": 1,
        "numberOfIdleAgents": 1,
        "numberOfLoggedInAgents": 1,
        "maxIdleAgentTime": 4298493,
        "estimatedWaitTimeMillis": 1806459560,
        "averageWaitTimeMillis": 0,
        "oldestCustomerWaitTime": 43540762475,
        "currentBackLog": 0,
        "canAssignNewCase": true
    },
    "errors": []
}






### Example - Channel Assignment Check

#### Request















Copy Code



curl --location 'https://api3.sprinklr.com/{env}/api/v2/work-queue/workQueueStatsSkillBased' \
--header 'Authorization: Bearer {access_token}’\
--header 'Key: {Api_Key} \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
        "workQueueId":"6686e9e65b4c220b0b022079",
        "channelForAssignmentCheck":"Sprinklr Voice"
}'






#### Response




{
    "data": {
        "numberOfAvailableAgents": 1,
        "numberOfIdleAgents": 1,
        "numberOfLoggedInAgents": 1,
        "maxIdleAgentTime": 14205,
        "estimatedWaitTimeMillis": 528016,
        "averageWaitTimeMillis": 0,
        "oldestCustomerWaitTime": 43536478178,
        "currentBackLog": 1,
        "canAssignNewCase": true
    },
    "errors": []
}







### Response Parameters











      ``






      ``





      ``





      ``





      ``





      ``


****
[tickets@sprinklr.com](mailto:tickets@sprinklr.com)




      ``



****
[tickets@sprinklr.com](mailto:tickets@sprinklr.com)




      ``


****
[tickets@sprinklr.com](mailto:tickets@sprinklr.com)




      ``





      ``




      ``






| Parameter | Sub-Parameter | Type | Definition |
| --- | --- | --- | --- |
| data |  | Object | Contains the skill-based work queue statistics. |
|  | numberOfAvailableAgents | Integer | Refers to the number of active agents in the correct status to take tasks in the queue. |
|  | numberOfIdleAgents | Integer | Refers to the number of agents who are currently available to pick up a task (agents in the right status and no capacity consumed). |
|  | numberOfLoggedInAgents | Integer | Refers to the number of agents currently logged in to the system. |
|  | estimatedWaitTimeMillis | Integer (Time in milliseconds) | Refers to the estimated wait time for the next agent to be available. |
|  | averageWaitTimeMillis | Integer (Time in milliseconds) | Refers to the average wait time for the next agent to be available. Dev Notes: This metric is governed by a Dynamic Property (DP). To retrieve this metric, it must first be enabled in your environment. Reach out to your Success Manager or submit a support ticket at . |
|  | oldestCustomerWaitTime | Integer (Time in milliseconds) | Refers to the wait time in milliseconds for the customer who has been waiting the longest in the queue.Skill-based filtering is not supported for oldest customer wait time. The API always returns the oldest customer of the work queue, not just within a skill bucket. Dev Notes: This metric is governed by a Dynamic Property (DP). To retrieve this metric, it must first be enabled in your environment. Reach out to your Success Manager or submit a support ticket at . |
|  | maxIdleTimeOfAgent | Integer (Time in milliseconds) | Displays the maximum idle time among agents who are available and have zero capacity consumed. Dev Notes: This metric is governed by a Dynamic Property (DP). To retrieve this metric, it must first be enabled in your environment. Reach out to your Success Manager or submit a support ticket at . |
|  | currentBackLog | Integer | Number of tasks currently in the backlog queue. |
|  | canAssignNewCase | Boolean | Indicates whether a user or system is permitted to assign a new case based on the current assignment rules, capacity, or eligibility criteria. Possible Values: true or false. |
| errors |  | Array | A list of errors, if any. Empty if the request was successful. |

	[](https://dev.sprinklr.com/fetch-skill-based-work-queue-statistics)




[Back to top](https://dev.sprinklr.com/fetch-skill-based-work-queue-statistics)
