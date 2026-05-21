---
title: "Apr - Jun, 2022"
slug: apr-jun-2022
url: https://dev.sprinklr.com/apr-jun-2022
---

# Apr - Jun, 2022

# Apr - Jun, 2022

## **Fetch User-Created Content Template Details** - May 25th, 2022

This API helps fetch the user-created content template details using the template Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/contentTemplate/{templateId}



## **Fetch Content Template Details Using Sorting and Filters** - May 25th, 2022

This API helps fetch content template id and name details using sorting and filter values.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/contentTemplate/searchContentTemplates


## **Fetch Content Template Details by Channel Type** - May 25th, 2022

This API helps fetch content template id and name details, which are specific to a channel type.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/contentTemplate/findAll?channelTypes={channelType}


## **Audit API** - May 10th, 2022

Audit API helps track the changes made to an asset over time. In other words, Audit API helps identify and analyze the user actions made to assets, i.e., who made what changes and when.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/audit/fetch


## **Fetch Audit Details by Cursor** - May 10th, 2022

If the Audit API response has additional details that exceed the limit in the request, you can fetch them using cursor ID.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/audit?id={cursorId}


## **Batch Query** - May 10th, 2022

This API call helps extract data from the widget which supports multiple projections or metrics/measurements.

**API Endpoint**

POST  https://api2.sprinklr.com/{env}/api/v2/reports/batchQuery

## **Message Action ** - April 11th, 2022

You can use this API to perform different actions on messages.

**API Endpoint**

POST  https://api2.sprinklr.com/{env}/api/v2/message/action

## **Retrieve Failed Webhook Events** - April 11th, 2022

You can use this API to retrieve failed webhook events for a subscription in a given time.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/webhook-replay

## **Lookup by Dimension** - April 11th, 2022

You can use this API to retrieve data associated with a  dimension such as location and lookup type such as ACCOUNT_ID, CASE_ID, CUSTOM_FIELD, etc.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/lookup/byDimensions

## **Lookup by Id** - April 11th, 2022

You can use this API to retrieve data associated with a lookup type such as ACCOUNT_ID, CASE_ID, CUSTOM_FIELD, and its associated keys.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/lookup


## **Enable Client Credentials Grant Type **- April 11th, 2022

You can use this API to enable client credentials grant type, which, in turn, will help clients request an access token to access their own resources and not the user’s resources.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/oauth/token

## **Profile Conversations **- April 11th, 2022

You can use this API to extract all the conversations related to an account, based on the respective channelType.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/profile/conversations

[](https://dev.sprinklr.com/apr-jun-2022)

[Back to top](https://dev.sprinklr.com/apr-jun-2022)
