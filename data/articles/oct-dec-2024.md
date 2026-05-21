---
title: "Oct - Dec, 2024"
slug: oct-dec-2024
url: https://dev.sprinklr.com/oct-dec-2024
---

# Oct - Dec, 2024

# Oct - Dec, 2024

**Developer Note:** We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.	Please note that the API base endpoint has changed from `api2` to `api3`.

For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.


## ****Read Messages (Bulk) using the POST method  -  15th Nov, 2024

You can now fetch messages in bulk that are associated with the respective message Ids using the POST method.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/message/bulk-fetch


## ****Read Asset API supports more asset types  -  8th Oct, 2024

You can now fetch additional asset types using the Read Asset V2 API, including PRESENTATION, PHOTO, VIDEO, AUDIO, and more.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/sam/{assetId}

## ****Fetch All Topic Groups -  8th Oct, 2024

Introducing Fetch All Topic Groups endpoint that allows you to retrieve all the available configured topic groups and topics.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/listening-topic-group/all

## ****Fetch UGC Stream Data - 8th Oct, 2024

Introducing Fetch UGC Stream Data endpoint that allows you to retrieve UGC stream data from the respective dashboard using the column stream Id.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/stream/{streamId}/feed


## ****Custom Controlling Field support in Create Custom Field - 8th Oct, 2024

Introducing Controlling Field support in Create Custom Field endpoint that allows you to define and manage custom fields with controlling logic.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-field


## ****Filtering Profile Based on Client and Partner Profile Lists - 8th Oct, 2024

Introducing support for filtering Profile based on Client and Partner Profile Lists in Search by Entity endpoint that allows you to filter profiles based on specific client and partner lists.
**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/search/{entityType}

[](https://dev.sprinklr.com/oct-dec-2024)

[Back to top](https://dev.sprinklr.com/oct-dec-2024)
