---
title: "Recommendation Webhooks"
slug: recommendation-webhooks
url: https://dev.sprinklr.com/recommendation-webhooks
---

# Recommendation Webhooks

# Recommendation Webhooks

**Recommendation Webhook Subscriptions:**
 Created Event

Recommendation webhooks subscription allows receiving nudges for Agent Assist widget in real-time. Nudge is an alert for an agent to act on the escalated user query/issue on a priority basis. By subscribing to a recommendation webhook, you ensure reminders are sent to the agents that help them resolve customer queries effectively and in a timely manner. Here are some example scenarios for recommendation.created webhooks:

- [recommendation.created Webhook - Escalated Alert](https://dev.sprinklr.com/recommendation-webhooks#EA)

- [recommendation.created Webhook - Guided Path](https://dev.sprinklr.com/recommendation-webhooks#GP)

- [recommendation.created Webhook - Reminder](https://dev.sprinklr.com/recommendation-webhooks#RE)

### recommendation.created Webhook - Escalated Alert

For instance, a user sends a message over live chat with keywords such as, ”manager”, “poor”, “bad”, “escalation”, or “supervisor”, escalation nudge is triggered through webhooks, which is directly communicated to the respective agent. Apart from the keyword detection, escalated alert can also be intent-driven.




  Copy Code



{
	"id": "62ea490fca48d6715a2cdbb7",
	"type": "recommendation.created",
	"payload": {
		"title": "On Demand Alert",
		"description": "manager escalation",
		"recipientType": "CASE",
		"recipientId": "320385",
		"payload": {
			"type": "ESCALATED_ALERT",
			"tags": ["manager escalation"],
			"metadata": {}
		},
		"createdTime": 1659521295095
	},
	"eventTime": 1659521295171,
	"subscriptionDetails": {
		"subscriptionId": "62ea459b21cef80d5b3ed705"
	}
}
















[Fetch Webhook Types API](https://dev.sprinklr.com/webhook-types)

``

``````

| Parameters | Sub-Param | Sub-Param | Description | Type |
| --- | --- | --- | --- | --- |
| id |  |  | Id of the webhook triggered event | String |
| type |  |  | Refers to the type of webhook eventUse  to get a list of supported webhook events | String |
| payload |  |  | Object containing the details of the triggered event | Object |
|  | title |  | Defines the alert category | String |
|  | description |  | The description of the alert created | String |
|  | recipientType |  | Entities on which the recommendation is createdCurrently only the CASE entity supports nudges | String |
|  | recipientId |  | The unique identifier w.r.t to the recipient type | Integer |
|  | payload |  | Object defining the details of the alert type/td> | Object |
|  |  | type | Refers to type of alertExample: ESCALATED_ALERT, GP_DETECTED_ALERT, FOLLOW_UP_ALERT | String |
|  |  | tags | The tag related to the alert type | String |
|  |  | metadata | Object defining additional details w.r.t alert typeRefer to the table below for metadata object description | Object |
|  | createdTime |  | The time at which the user message was created | Epoch |
| eventTime |  |  | The time at which the webhook was triggered | Epoch |
| subscriptionDetails |  |  | Object containing webhook subscription details | Object |
|  | subscriptionId |  | The unique identifier for the webhook subscription | String |

### recommendation.created Webhook - Guided Path

Whenever a user interacts with self-serve guided workflows, the webhook gets triggered and a guided path CTA (call-to-action) appears in the agent nudges section. The helps agents resolve customer queries/issues quickly and effectively.




  Copy Code



{
	"id": "62ea6290e7eb1706e528281e",
	"type": "recommendation.created",
	"payload": {
		"title": "On Demand Alert",
		"description": "Guided path detected",
		"recipientType": "CASE",
		"recipientId": "320411",
		"payload": {
			"type": "GP_DETECTED_ALERT",
			"tags": ["Guided path detected"],
			"metadata": {
				"detectedIntents": "Insurance Query",
				"guidedPath": {
					"key": "61a6123060afb249a02c3097"
				}
			}
		},
		"createdTime": 1659527824426
	},
	"eventTime": 1659527824539,
	"subscriptionDetails": {
		"subscriptionId": "62ea459b21cef80d5b3ed705"
	}
}






### metadata Object Description - Guided Path











| Parameters | Sub-Param | Description | Type |
| --- | --- | --- | --- |
| detectedIntents |  | Defines the intent of the customer query | String |
| guidedPath |  | Object containing the guided path details | Object |
|  | key | The unique identifier for the guided path | String |

### recommendation.created Webhook - Reminder

Let's assume that an agent commits to call back by 13:00, a reminder nudge will get triggered through webhooks. The agent will be reminded that they need to call back the user along with an option to create a task for it.




  Copy Code



{
	"id": "62ea4b741e318c349c7a7361",
	"type": "recommendation.created",
	"payload": {
		"title": "On Demand Alert",
		"description": "Customer wants a followup",
		"recipientType": "CASE",
		"recipientId": "320389",
		"payload": {
			"type": "FOLLOW_UP_ALERT",
			"tags": ["Customer wants a follow up"],
			"metadata": {
				"followupTime": 1659646800000
			}
		},
		"createdTime": 1659521907804
	},
	"eventTime": 1659521908216,
	"subscriptionDetails": {
		"subscriptionId": "62ea459b21cef80d5b3ed705"
	}
}





### metadata Object Description - Reminder










| Parameters | Description | Type |
| --- | --- | --- |
| followupTime | Metadata for the reminderIn this case the metadata describes the followup time with the user | Epoch |

**Dev Notes: **The JSON response parameters remains the same for all the three payloads. Only the `alert type` and `metadata object description`will differ.

[](https://dev.sprinklr.com/recommendation-webhooks)

[Back to top](https://dev.sprinklr.com/recommendation-webhooks)
