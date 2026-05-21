---
title: "Apr - June, 2024"
slug: apr-june-2024
url: https://dev.sprinklr.com/apr-june-2024
---

# Apr - June, 2024

# Apr - June, 2024

**Developer Note:**We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## Asset Import via URL - 27th June, 2024

Using this API, you can upload an asset to Sprinklr's server using a URL.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/media/upload/url

## Fetch Voice Recording - 27th June, 2024

Using this API, you can access the restricted voice recording URLs.

**API Endpoint**

  GET https://api2.sprinklr.com/{env}/api/v2/voice/recording

## Cancel Callback - 19th June, 2024

Using this API, the scheduled callback can be cancelled.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/voice/cancel-callback

## Update Callback - 19th June, 2024

Using this API, you can update the details of a scheduled callback.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/voice/update-callback

## Schedule Callback - 19th June, 2024

Using this API, brands can schedule callbacks directly from the IVR. This feature is useful when customers face extended wait times or need assistance during off-hours.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/voice/schedule-callback

## Fetch Slot Information - 19th June, 2024

Using this API, you can fetch the available slot information for the given work queue ID.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/work-queue/slot-information

## SCIM APIs (User APIs) - 5th June, 2024

We have introduced new SCIM APIs for creating, updating, reading, and deleting a user from Sprinklr. These APIs strictly adhere to the SCIM protocol and allow secure exchange of data between two systems.

## Upcoming Breaking Change - Media URLs Public to Private Transition

**What You Need to Know**


- Post 19.5 release, the Media URLs (Attachment URLs) generated or fetched using Sprinklr APIs will be valid and accessible for a limited time.

- Once the URL expires, it can be passed in the Secure Media Download or Secure Media Download (Bulk) API. The API will return the accessible URLs in the response with limited time validity (starting from when you make the API call).

- All the existing media URLs will be invalid or inaccessible by mid-June. You can again use [Secure Media Download](https://dev.sprinklr.com/secure-media-download) or [Secure Media Download (Bulk)](https://dev.sprinklr.com/secure-media-download-bulk) API to generate accessible URLs in the response with limited time validity.

- We will keep you posted on the exact timelines and validity of these URLs.

## Secure Media Download - 17th May, 2024

Using this API, you can create an accessible URL (time-bound) from a secure media asset URL.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/secure-assets/fetch/{secureUrl}

## Secure Media Download (Bulk) - 17th May, 2024

Using this API, you can create accessible URLs from the given secure URLs.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/secure-assets/bulk/fetch

## Read Message by UMID - 15th May, 2024

Using this API, you can fetch the message details using the UMID (Universal Message ID).

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/message

## Publishing Reply - 8th May, 2024

The Publishing Reply API now supports publishing a reply to a Yelp review. You can publish a reply only once per review. If you call the API twice, it returns the error: **There is already a reply to review.**

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/publishing/reply

## Fetch Work Queue Stats - 8th May, 2024

Using this API, you can fetch the work queue stats for the given work queue ID.

**API Endpoint**

  GET https://api2.sprinklr.com/{env}/api/v2/work-queue/workQueueStats/{workQueueId}

## User Create/Update Webhook - 1st May, 2024

The user create/update webhook response now supports skills versus proficiency scores of the user added or updated. The response payload includes an object `skillVsProficiency`, which contains the key-value pair of skill ID and proficiency score.

**Webhook Response Payload Details**

  Refer to [User Webhooks](https://dev.sprinklr.com/user-webhooks) documentation.

## Publishing Post - 24th April, 2024

Now you can add alternate text for image attachments while publishing a post.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/publishing/post

## Create Draft - 24th April, 2024

Now you can add alternate text for image attachments while creating a draft.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/publishing/draft

## Create/Update Bulk Leads - 10th April, 2024

Using this API, you can create or update leads in bulk.

**API Endpoint**

  POST https://api2.sprinklr.com/{env}/api/v2/dmp/audience-lead/{partnerName}/bulk
