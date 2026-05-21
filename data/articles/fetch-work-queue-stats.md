---
title: "Fetch Work Queue Stats"
slug: fetch-work-queue-stats
url: https://dev.sprinklr.com/fetch-work-queue-stats
---

# Fetch Work Queue Stats

#
 GET  Fetch Work Queue Stats



All calls that require agent assignment need to pass through a queue in unified routing module. You'll find all the existing work queues within Unified routing that act as a virtual container for unassigned calls. This API helps fetch the work queue stats for the given work queue Id. The stats include the number of available agents, number of idle agents, estimated wait time until next assignment, average wait time, current backlog, and start and end time for business hours.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/work-queue/workQueueStats/{workQueueId}


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

### Path Parameter
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| workQueueId | Required | Refers to the unique identifier for the work queue | String |

## Example - Request















Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/work-queue/workQueueStats/65d8499783a1386f4ef7cabe'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
    "data": {
        "numberOfAvailableAgents": 1,
        "numberOfIdleAgents": 1,
        "numberOfLoggedInAgents": 1,
        "maxIdleAgentTime": 88444043,
        "estimatedWaitTimeMillis": 4681,
        "averageWaitTimeMillis": 0,
        "oldestCustomerWaitTime": 0,
        "currentBackLog": 0
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






| Parameter | Sub-Parameter | Type | Definition |
| --- | --- | --- | --- |
| data |  | Object | Contains the work queue statistics. |
|  | numberOfAvailableAgents | Integer | Refers to the number of active agents in the correct status to take tasks in the queue. |
|  | numberOfIdleAgents | Integer | Refers to the number of agents who are currently available to pick up a task (agents in the right status and no capacity consumed). |
|  | numberOfLoggedInAgents | Integer | Refers to the number of agents currently logged in to the system. |
|  | estimatedWaitTimeMillis | Integer (Time in milliseconds) | Refers to the estimated wait time for the next agent to be available. |
|  | averageWaitTimeMillis | Integer (Time in milliseconds) | Refers to the average wait time for the next agent to be available. Dev Notes: This metric is governed by a Dynamic Property (DP). To retrieve this metric, it must first be enabled in your environment. Reach out to your Success Manager or submit a support ticket at . |
|  | oldestCustomerWaitTime | Integer (Time in milliseconds) | Refers to the wait time in milliseconds for the customer who has been waiting the longest in the queue. Dev Notes: This metric is governed by a Dynamic Property (DP). To retrieve this metric, it must first be enabled in your environment. Reach out to your Success Manager or submit a support ticket at . |
|  | maxIdleTimeOfAgent | Integer (Time in milliseconds) | Displays the maximum idle time among agents who are available and have zero capacity consumed. Dev Notes: This metric is governed by a Dynamic Property (DP). To retrieve this metric, it must first be enabled in your environment. Reach out to your Success Manager or submit a support ticket at . |
|  | currentBackLog | Integer | Number of tasks currently in the backlog queue. |
| errors |  | Array | A list of errors, if any. Empty if the request was successful. |

	[](https://dev.sprinklr.com/fetch-work-queue-stats)




[Back to top](https://dev.sprinklr.com/fetch-work-queue-stats)
