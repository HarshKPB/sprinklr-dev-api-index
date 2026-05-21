---
title: "Consent Analytics Live Chat SDK"
slug: consent-analytics-live-chat-sdk
url: https://dev.sprinklr.com/consent-analytics-live-chat-sdk
---

# Consent Analytics Live Chat SDK

# Enable or Disable Consent Based Analytics

Live Chat supports consent‑based analytics to help organizations respect user choices while they interact with their website or app. Consent‑based analytics can be configured at the application level in the Live Chat embed code.

Any changes in user consent after the chat has been loaded can be updated to Sprinklr Live Chat via the SDK. Based on these updates, analytics tracking will either start or stop dynamically.

## Method

`sprChat('updateCookieConsent', { 'ANALYTICS': true })`

### Parameters








****
****


| Parameter | Description |
| --- | --- |
| ANALYTICS | Controls whether analytics tracking is enabled based on user consent.       Supported Values: true, false       Default: false |

[](https://dev.sprinklr.com/consent-analytics-live-chat-sdk)

[Back to top](https://dev.sprinklr.com/consent-analytics-live-chat-sdk)
