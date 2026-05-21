---
title: "User Current State Webhook"
slug: user-current-state-webhook
url: https://dev.sprinklr.com/user-current-state-webhook
---

# User Current State Webhook

# User Current State Webhook

**User Current State Webhook Subscriptions:**
User Current State

This webhook provides real time updates for the current user state within Sprinklr.

**Dev Notes: **The webhook requires backend enablement. Kindly reach out your success manager for the feature enablement in your customer instance.

### Example 1: LOGGED_OUT




  Copy Code



{
  "id": "645a6da3cf926577b4e3246c",
  "type": "user.current.state",
  "payload": {
    "id": "1000157828",
    "state": "LOGGED_OUT",
    "lastUpdated": 1683647907903,
    "startTime": 1683647907903
  },
  "eventTime": 1683647907915,
  "subscriptionDetails": {
    "subscriptionId": "645a6d8fcf926577b4e311af"
  }
}





### Example 2: IDLE




  Copy Code



  {
  "id": "645a6db1cf926577b4e32ec0",
  "type": "user.current.state",
  "payload": {
    "id": "1000157828",
    "state": "IDLE",
    "lastUpdated": 1683647921121,
    "startTime": 1683647916539
  },
  "eventTime": 1683647921127,
  "subscriptionDetails": {
    "subscriptionId": "645a6d8fcf926577b4e311af"
  }
}





### Example 3: WORKING_ON_CASE




  Copy Code



{
  "id": "645a718d9c2c8f3094cb2a3d",
  "type": "user.current.state",
  "payload": {
    "id": "1000052950",
    "state": "WORKING_ON_CASE",
    "assetClass": "UNIVERSAL_CASE",
    "assetId": "298",
    "lastUpdated": 1683648909402,
    "startTime": 1683613772308
  },
  "eventTime": 1683648909407,
  "subscriptionDetails": {
    "subscriptionId": "645a6d8fcf926577b4e311af"
  }
}






### Response Parameters

























****

| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Refers to the unique identifier for the webhook triggered | String |
| type |  | Refers to the webhook type "user.current.state" in this case | String |
| payload |  | Object containing the case details details | Object |
|  | id | Refers to the unique identifier for the user, i.e., the user Id | String |
|  | state | Refers to the current state of the agent 					Enum: 					 						[CALL_ASSIGNED, ON_INBOUND_CALL, ON_OUTBOUND_CALL, CUSTOMER_ON_HOLD, AGENT_ON_HOLD, ON_ACW, WORKING_ON_CASE, WORKING_ON_TASK, IDLE, NOT_AVAILABLE, LOGGED_OUT, AGENT_NEVER_LOGGED_IN] | String |
|  | assetClass | Refers to the asset class for the case.Is returned only when the user state is "WORKING_ON_CASE" | String |
|  | assetId | Refers to the case number. Is returned only when the user state is "WORKING_ON_CASE" | String |
|  | lastUpdated | Refers to the time at which the user state was last updated. This timestamp reflects when Sprinklr backend updates the state in the database. | Epoch |
|  | startTime | Refers to the time at which the user state was changed. This timestamp indicates when the UI changes the user’s state.   Dev Notes: Ideally, both timestamps should be identical. However, in rare cases, there might be a difference of a few seconds. For all our reporting and UI calculations (time in the current state), only startTime is used. Therefore, clients should use startTime and disregard lastUpdated. | Epoch |
| eventTime |  | Refers to the time at which the webhook was triggered | Epoch |
| subscriptionDetails |  | Object defining the webhook subscription details | Object |
|  | subscriptionId | Refers to the unique identifier for the webhook subscription | String |

### State Field Descriptions










| Status | Description |
| --- | --- |
| CALL_ASSIGNED | If the call is assigned to the user |
| ON_OUTBOUND_CALL | If the user is currently attending an outbound call |
| ON_INBOUND_CALL | If the user is currently attending an inbound call |
| CUSTOMER_ON_HOLD | If the customer has put the call on hold |
| AGENT_ON_HOLD | If the user (agent) has put the call on hold |
| ON_ACW | If the user is busy with ACW (After-call work) |
| WORKING_ON_CASE | If the user is currently working on a case assigned to them |
| WORKING_ON_TASK | If the user is working on a task |
| IDLE | If the user is in idle state |
| NOT_AVAILABLE | If the user is currently not available |
| LOGGED_OUT | If the user has logged out from Sprinklr |
| AGENT_NEVER_LOGGED_IN | If the user never logged in to Sprinklr |

	[](https://dev.sprinklr.com/user-current-state-webhook)

[Back to top](https://dev.sprinklr.com/user-current-state-webhook)
