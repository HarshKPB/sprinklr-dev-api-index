---
title: "Voice Call Event Updates Webhook"
slug: voice-call-event-updates-webhook
url: https://dev.sprinklr.com/voice-call-event-updates-webhook
---

# Voice Call Event Updates Webhook

# Voice Call Event Updates Webhook

**Voice Call Webhook Subscriptions:**
Voice Call Event Updates

This webhook provides real-time updates for changes in call status associated with Sprinklr Voice cases.

### Voice Call Event Updates Webhook




  Copy Code


{
  "id": "69afc01f287c834624f2b473",
  "type": "voice.call.event.updates",
  "payload": {
    "conversationId": "0000019d684848be4b0a7f7dff8836",
    "caseId": "0000019cbe3fd5b6e4b070ff3053adea",
    "caseNumber": 13144357,
    "direction": "Outbound",
    "from": "+12078035808",
    "to": "TO&TOENephoneNumbersphoneNumber&43bed7fb-6451-48ab-ae4c-91591ac01c80",
    "status": "ACW_TRIGGERED",
    "agentId": "66071272",
    "agentName": "shubham 2026",
    "dialerProfileType": "PREVIEW",
    "segmentId": "69a988d6cf5ca2469126c22d",
    "dialerProfile": "SHUBHAM AMD POLICY - PREVIEW - SW",
    "outboundCallSource": "LEAD",
    "campaignCallAttemptNumber": 16,
    "campaignName": "shubham webhook test camp",
    "segmentName": "seg new",
    "acwId": "7b544ba3-9a1d-43e-8882-eb3937ce7ca1",
    "awName": "Anisha Normal ACW"
  },
  "eventTime": 1773125663614,
  "subscriptionDetails": {
    "subscriptionId": "67a32c075b4dd22c585fc16e"
  }
}





### Response Parameters

























[Status Field Descriptions](https://dev.sprinklr.com/voice-call-event-updates-webhook#status_field)

****

****

``

``

****

| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Refers to the unique identifier for the webhook triggered. | String |
| type |  | Refers to the webhook type "voice.call.event.updates" in this case. | String |
| payload |  | Object containing the case level details. | Object |
|  | conversationId | Refers to the unique identifier for the conversation. | String |
|  | participantId | Refers to the unique identifier for the participant. | String |
|  | caseId | Refers to the unique identifier for the case. | String |
|  | caseNumber | Refers to the Sprinklr case number. | Integer |
|  | direction | Refers to whether the call was outbound or inbound. | String |
|  | from | The caller’s phone number. | String |
|  | to | The business phone number. | String |
|  | status | Refers to status of the call. For more details, see  Values:  [SKIPPED_TO_ACW, OFFER_MISSED, OFFER_CANCELLED, OFFER_REJECTED, RINGING, FAILED, ANSWERED, MUTE, UNMUTE, HOLD, UNHOLD, REJECTED, IVR_START, IVR_TRANSFER_START, LISTEN_TO_BARGE_IN, WHISPER_TO_BARGE_IN, LISTEN_TO_WHISPER, DISCONNECTED, VOICE_CALL_ENDED, VOICE_CALL_STATUS_UPDATE, CONVERSATION_STATUS_UPDATED, RECORDING_STATUS_UPDATED, CONVERSATION_STARTED, CUSTOMER_ENTERED_WORK_QUEUE, CALL_OFFERED_TO_AGENT, CONVERSATION_ENDED, CUSTOMER_ENTERED_WORK_QUEUE, CUSTOMER_ENTERED_WORK_QUEUE, ACW_TRIGGERED, ACW_SUBMITTED ] | String |
|  | participantType | Refers to the type of participant, i.e., either AGENT or CUSTOMER | String |
|  | workQueueEntryReason | Refers to the reason why the call entered a work queueValues:[INCOMING_CALL, WARM_TRANSFER, ADD_TO_CALL] | String |
|  | agentId | Refers to the unique identifier for the agent.This field will only be returned when the participant type is AGENT. | String |
|  | agentName | Refers to the name of the agentThis field will only be returned when the participant type is AGENT. | String |
|  | dialerProfileType | The type of the dialer profile. | String |
|  | dialerProfile | The dialer configuration/profile used to initiate the call. | String |
|  | outboundCallSource | The source of the outbound call.Values:[MANUAL, LEAD, SCHEDULED_CALLBACK] | String |
|  | segmentId | ID of the segment (if the call was triggered via a campaign). | String |
|  | segmentName | Name of the segment (if the call was triggered via a campaign). | String |
|  | campaignId | ID of the campaign. | String |
|  | campaignName | Name of the campaign. | String |
|  | acwId | ID of the ACW. | String |
|  | acwName | Name of the ACW. | String |
| eventTime |  | Refers to the time at which the webhook was triggered. | Epoch |
| subscriptionDetails |  | Object defining the webhook subscription details. | Object |
|  | subscriptionId | Refers to the unique identifier for the webhook subscription. | String |

### Status Field Descriptions











-
-
-












        **
        **













| Status | Description |
| --- | --- |
| SKIPPED_TO_ACW | If the agent chooses the "Skip to ACW" (After-call work) option in the preview dialer |
| OFFER_MISSED | If the call is missed by the agent |
| OFFER_CANCELLED | Can happen due to either of the following reasons:Call reaches the agent but gets disconnected by the customerAssign to agent node timeoutTransfer/invite is cancelled by agent |
| OFFER_REJECTED | If the call reaches the agent but they reject the call |
| RINGING | If the call is in the ringing state |
| FAILED | If there is an API or a connection failure |
| ANSWERED | If the call is answered by the customer/agent after the IVR transfer |
| MUTE | If the call is on mute mode |
| UNMUTE | If the call is on unmute mode |
| HOLD | If the call is on Hold mode |
| UNHOLD | If the call is on Unhold mode |
| REJECTED | If the call is rejected |
| IVR_START | If the Inbound IVR is initiated |
| IVR_TRANSFER_START | If the IVR transfer to the agent has started |
| LISTEN_TO_BARGE_IN | If the supervisor who has been listening to the call between the agent and the customer, decides to talk to the customer directly |
| WHISPER_TO_BARGE_IN | If the supervisor who was guiding the agent on the next steps (in this case, customer can't hear the conversation between the agent and the supervisor), decides to talk to the customer directly |
| LISTEN_TO_WHISPER | If the supervisor who has been listening to the call between the agent and the customer, decides to talk to the agent to guide them on the next steps (in this case, customer can't hear the conversation between the agent and the supervisor) |
| DISCONNECTED | If the call is disconnected/ended |
| VOICE_CALL_ENDED | Indicates that the voice call has ended |
| VOICE_CALL_STATUS_UPDATE | Represents an update in the status of the ongoing voice call |
| CONVERSATION_STATUS_UPDATED | Indicates that the conversation status has been updated |
| RECORDING_STATUS_UPDATED | Represents an update in the recording status of the call |
| CONVERSATION_STARTED | Marks the beginning of a conversation between agent and customer |
| CUSTOMER_ENTERED_WORK_QUEUE | Indicates that the customer has entered the work queue for routing |
| CALL_OFFERED_TO_AGENT | Represents that the call has been offered to an agent |
| CONVERSATION_ENDED | Marks the end of a conversation between agent and customer |
| ACW_TRIGGERED | Indicates that After Call Work (ACW) has been triggered for the agent |
| ACW_SUBMITTED | Represents that the agent has submitted their After Call Work (ACW) |

[](https://dev.sprinklr.com/voice-call-event-updates-webhook)

[Back to top](https://dev.sprinklr.com/voice-call-event-updates-webhook)
