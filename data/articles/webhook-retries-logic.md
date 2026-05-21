---
title: "Webhook Retries Logic"
slug: webhook-retries-logic
url: https://dev.sprinklr.com/webhook-retries-logic
---

# Webhook Retries Logic

#
Webhook Retries Logic


Sprinklr offers a Webhook Retries Logic that works on a count of 10 seconds. Once the webhook is triggered, the Sprinklr waits for 10 seconds to receive an HTTP 200 status code. If a webhook cannot be delivered successfully, it will be retried three times with different queues till the request receives a 200 HTTP status code in the response. Otherwise, they will be stored in Deleted Queue. All the events that are failed to deliver will enter Queue 1 and will be retried. If some events fail again in Queue 1, they will join Queue 2 and will be tried again for a successful 200 HTTP status code. If the events were unable to deliver in Queue 2, they would be moved to Queue 3 for a delivery retry. All the events that failed to return 200 status code in the three consecutive tries will be stored in Deleted Queue.

**Dev Notes: **

- Webhook Retries logic works on a count of 10 seconds by default. This default time is unalterable as all the webhooks in the queue will likely get delayed, which might lead to a considerable lag.
- We recommend using an **asynchronous** webhook endpoint that sends `200 OK` within 10 seconds. This helps avoid unwanted congestion at either the sender's or receiver's end
[](https://dev.sprinklr.com/webhook-retries-logic)

[Back to top](https://dev.sprinklr.com/webhook-retries-logic)
