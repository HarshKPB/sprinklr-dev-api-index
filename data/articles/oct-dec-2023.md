---
title: "Oct - Dec, 2023"
slug: oct-dec-2023
url: https://dev.sprinklr.com/oct-dec-2023
---

# Oct - Dec, 2023

# Oct - Dec, 2023

**Developer Note:** We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.	Please note that the API base endpoint has changed from `api2` to `api3`.

For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****Live Chat APIs -  12thd Dec, 2023

We have introduced [Live Chat APIs](https://dev.sprinklr.com/live-chat-application-apis) for initiating and managing live chat conversations from the backend.


## ****Asset Read API -  3rd Dec, 2023

You can now fetch details for SUBTITLE type asset using Asset Read read API.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/sam/{assetId}



## ****Column Stream Read API -  3rd Dec, 2023

You can now fetch TikTok video posts using Stream Read API.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/stream/{streamId}/feed



## ****Email API -  3rd Dec, 2023

Email API now supports adding "cc" and "bcc" fields in the API request. The message ingested in Sprinklr would reflect the email addresses added in "cc" and "bcc" upon calling the API. Also, the image attachments now support `HEIC`, `HEIF`, `TIFF`, `JFIF` formats.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/email/create



## ****Reporting API -  3rd Dec, 2023

Reporting API now supports hasMore flag which helps determine when to stop calling the API. If hasMore is true, it implies that more data rows are present; if false, it means the end of results.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/reports/query

**More Details**

Refer to the FAQs section within [Reporting Blueprint](https://dev.sprinklr.com/reporting-blueprints)



## ****Case Update API -  30th Nov, 2023

Case Update API now supports updating case queues. The three supported update actions include — ADD_QUEUES, SYNC_QUEUES, REMOVE_QUEUES.

**API Endpoint**

	PUT https://api2.sprinklr.com/{env}/api/v2/case



## ****Source Agnostic API -  6th Nov, 2023

Source agnostic API now supports sending HTML content and associating it with the case.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/source-agnostic/{accountId}/send

[](https://dev.sprinklr.com/oct-dec-2023)

[Back to top](https://dev.sprinklr.com/oct-dec-2023)
