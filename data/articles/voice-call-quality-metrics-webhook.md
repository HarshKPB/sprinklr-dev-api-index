---
title: "Voice Call Quality Metrics Webhook"
slug: voice-call-quality-metrics-webhook
url: https://dev.sprinklr.com/voice-call-quality-metrics-webhook
---

# Voice Call Quality Metrics Webhook

# Voice Call Quality Metrics Webhook

**Voice Call Webhook Subscriptions:**
Voice Call Quality Event

This webhook notifies when a voice call quality event occurs. It provides participant details, call identifiers, and real-time quality metrics such as MOS, jitter, packet loss, round-trip time, and network speed. These metrics help monitor audio performance and diagnose issues affecting call experience.

### Voice Call Quality Metrics Webhook Payload




  Copy Code



{
  "id": "68a456d990d54b04df104abb",
  "type": "voice.call.quality.event",
  "payload": {
    "conversationId": "00000198c1ee235ae4b093ad1e84dea1",
    "participantId": "00000198c1ee23d4e4b093ad1e84dea2",
    "participantType": "AGENT",
    "eventSource": "SPRINKLR",
    "callId": "4e9199a3-c298-4c19-ba4b-e0e8c97ba5a9",
    "direction": "Outbound",
    "eventTime": 1755600601261,
    "metrics": {
      "mos": 4.145,
      "outAverageRTT": 220.45899999999997,
      "outMos": 4.05,
      "avgNetworkSpeed": 5.5,
      "inMos": 4.24,
      "outAverageJitter": 17.374999999999996,
      "inAverageJitter": 3,
      "callSetupTime": 8.538,
      "inPacketLossPercent": 0,
      "outPacketLossPercent": 0.19157088122605362
    }
  },
  "eventTime": 1755600601261,
  "subscriptionDetails": {
    "subscriptionId": "6889a6fa5209b100ff4d2fe0"
  }
}



## Response Parameters











      ``





      ``


      ``


      ``






      ``





      ``





      ``

      ````



      ``

      ``````````



      ``





      ``

      ````



      ``





      ``




      ``





      ``





      ``
      ``





| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| id | — | String | Unique identifier for the webhook event. |
| type | — | String | Type of the event. For this webhook, the value is voice.call.quality.event. |
| payload | — | Object | Contains details about the call, participant, and quality metrics. |
|  | conversationId | String | Unique identifier of the conversation associated with the call. |
|  | participantId | String | Unique identifier of the participant in the call. |
|  | participantType | String | Type of participant. Possible values: AGENT, CUSTOMER. |
|  | eventSource | String | Source system reporting the event. Possible values: SPRINKLR, TWILIO, SIGNALWIRE, EXOTEL, PROVIDER. |
|  | callId | String | Unique identifier of the call. |
|  | direction | String | Direction of the call. Possible values: Inbound, Outbound. |
|  | eventTime | Integer | Epoch timestamp (in milliseconds) of when the event occurred. |
|  | metrics | Object | This object provides detailed call quality indicators captured during the voice call. These values measure the overall audio experience for both inbound and outbound streams. |
| eventTime | — | Integer | Epoch timestamp (in milliseconds) when the webhook event was generated. |
| subscriptionDetails | — | Object | Contains subscription information for the webhook event. |
|  | subscriptionId | String | Identifier of the subscription through which this webhook was triggered. |










      ``




      ``




      ``




      ``




      ``




      ``




      ``




      ``




      ``




      ``





| Parameter | Type | Description |
| --- | --- | --- |
| mos | Float | Mean Opinion Score (1–5): Subjective quality score estimating how users perceive overall call quality. Higher = better. |
| outAverageRTT | Float | Outbound Average Round Trip Time (ms): Average time for packets to travel from sender to receiver and back. |
| outMos | Float | Outbound MOS (1–5): Quality score for the outbound audio stream. |
| avgNetworkSpeed | Float | Average Network Speed (Mbps): Average bandwidth available during the call. |
| inMos | Float | Inbound MOS (1–5): Quality score for the inbound audio stream. |
| outAverageJitter | Float | Outbound Jitter (ms): Variation in packet arrival time for outbound traffic. Affects smoothness of audio. |
| inAverageJitter | Float | Inbound Jitter (ms): Variation in packet arrival time for inbound traffic. |
| callSetupTime | Float | Call Setup Time (s): Time taken to establish the call from initiation to connection. |
| inPacketLossPercent | Float | Inbound Packet Loss (%): Percentage of inbound packets lost during transmission. Range: 0–100. |
| outPacketLossPercent | Float | Outbound Packet Loss (%): Percentage of outbound packets lost during transmission. Range: 0–100. |

[](https://dev.sprinklr.com/voice-call-quality-metrics-webhook)

[Back to top](https://dev.sprinklr.com/voice-call-quality-metrics-webhook)
