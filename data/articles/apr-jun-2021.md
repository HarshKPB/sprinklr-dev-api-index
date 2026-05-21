---
title: "Apr - Jun 2021"
slug: apr-jun-2021
url: https://dev.sprinklr.com/apr-jun-2021
---

# Apr - Jun 2021

# Apr - Jun 2021

## **Visual Insight Predict API Endpoint** - June 22, 2021.

The Visual Insight API is capable of analyzing an image and can predict different objects that are present in the image such as text objects like Service Tag, Error Code, and more. Using the Visual Insight API, you can make a prediction request on a single image, that is, one at a time.

**API Endpoint**

POST https://api2.sprinklr.com/{{env}}/api/v2/intuition/visual/predict

## **Webhook Replay API Endpoint** - May 12, 2021

To boost the API response time and to be consistant with the Sprinklr API structure, we have implemented a change in Webhook Replay APIs, now you can pass time range as query parameter along with the size of data you want to fetch in one call and can use Cursor API call to fetch further data.
**Breaking Change in API Endpoint**
 Note that this includes a breaking changes to the API and may require a code change on your side. See below for more details.

**Changed API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/webhook-replay
GET https://api2.sprinklr.com/{env}/api/v2/webhook-replay

[](https://dev.sprinklr.com/apr-jun-2021)

[Back to top](https://dev.sprinklr.com/apr-jun-2021)
