---
title: "Thread Control Webhook"
slug: thread-control-webhook
url: https://dev.sprinklr.com/thread-control-webhook
---

# Thread Control Webhook

# Thread Control Webhook

**Thread Control Webhook Subscriptions:**
 Thread Control Updated

Whenever the control of thread is being passed between Sprinklr and Chatbot a webhook notification is triggered with the details of pervious and current participant with other details.

### Thread.Control.Updated Webhook




  Copy Code



{
  "id": "5ee8bcd75111d30b62ea14c0",
  "type": "thread.control.updated",
  "payload": {
    "entityType": "CASE",
    "entityId": "5ee8nj7f9ss0ef394b29b7d4",
    "previousParticipant": "Sprinklr",
    "controllingParticipant": "5ee1r7bh36088djf5gdv3810"
  },
  "eventTime": 1592310999076,
  "subscriptionDetails": {
    "subscriptionId": "5ee35ea5c54eaace5b06d95f"
  }
}





## Response definitions



















































| Parameters | Description | Type |
| --- | --- | --- |
| id | Unique Id of the thread webhook. | String |
| type | The type of webhook. | String |
| entityType | Entity type on which the action is performed. | String |
| entityId | Id of the entity. | String |
| previousParticipant | The pervious controlling participant of the conversation thread. | String |
| controllingParticipant | The current controlling participant of the conversation thread. | String |
| eventTime | The time in epoch at which the action took place. | Epoch |
| subscriptionId | The webhook subscription Id. | String |

	[](https://dev.sprinklr.com/thread-control-webhook)

[Back to top](https://dev.sprinklr.com/thread-control-webhook)
