---
title: "Apr - Jun, 2020"
slug: apr-jun-2020
url: https://dev.sprinklr.com/apr-jun-2020
---

# Apr - Jun, 2020

# Apr - Jun, 2020

## **New API Endpoint** - May 22nd, 2020

Introduction of Thread Control in Omni Channel Integrations. We’re exposing new set of API endpoints by which you can Pass, Release, Acquire and Check control of the thread between Participants and Sprinklr (vice-versa).

**API Endpoints**

POST  https://api2.sprinklr.com/{env}/api/v2/thread/pass-control

POST  https://api2.sprinklr.com/{env}/api/v2/thread/release-control

POST  https://api2.sprinklr.com/{env}/api/v2/thread/acquire-control

POST  https://api2.sprinklr.com/{env}/api/v2/thread/get-controlling-participant

## **New API Endpoint** - May 20nd, 2020

To improve the efficiency and performance of Sprinlkr APIs in terms of Omni Channel Integrations and reducing the working cost of customers towards Modern Care. We’re exposing a new API endpoint by which you can deflect the customer's calls to Modern Engagement channels via giving options in IVR. Now the developer can also use this endpoint to deflect the Customer Call.

**API Endpoint**

POST  https://api2.sprinklr.com/{env}/api/v2/deflect

## **Deprecation of API Endpoint** - April 25th, 2020

** Breaking Change**
 Note that this includes a breaking changes to the API and may require a code change of your side. See below for more details.

Fetch Message by umId and sourceType

To improve performance, we’re making changes to our databases and models, and as a result, this API endpoint will no longer be available across all environment. After the introduction of this change, developer can't fetch message data attributes using this endpoint.

**Deprecating API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/message?id=123&sourceType=ACCOUNT

The Fetch Message by umId and sourceType API is used to fetch the messages details that includes sender and receiver profile along with message information. If you are using this API endpoint in any implementation/integration you need to make code changes before April 25, 2020.

** Alternate Solution**
 To fetch the message details along with sender and receiver profile you can use the Fetch Message by MessageId endpoint.

messageId = sourceType + “_” + sourceId + “_” + “snCreatedTime” + “_” + umId.

## **New API Endpoint** - April 5th, 2020.

To improve performance of APIs, we’re exposing a new API endpoint that will be available across all environment. Now developers can use this endpoint to fetch message data attributes.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/message/byMessageId

[](https://dev.sprinklr.com/apr-jun-2020)

[Back to top](https://dev.sprinklr.com/apr-jun-2020)
