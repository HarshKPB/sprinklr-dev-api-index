---
title: "Jan - Mar, 2021"
slug: jan-mar-2021
url: https://dev.sprinklr.com/jan-mar-2021
---

# Jan - Mar, 2021

# Jan - Mar, 2021

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## **Listening API Endpoints ** - March 12, 2021

Introduction of new Listening API endpoints. We’re exposing new set of Listening API endpoints by which you can programmatically perform CRUD operation over Listening Topic, Listening Topic Group, Listening Keyword Lists, Listening Themes and, Listening Backfill within Sprinklr.

**Listening Topic API Endpoints**

Sprinklr Listening Topic APIs empowers you to programmatically Create, Read, Update and, Delete listening topics.
POST https://api2.sprinklr.com/{env}/api/v2/listening-topic
GET https://api2.sprinklr.com/{env}/api/v2/listening-topic/{topicId}
PUT https://api2.sprinklr.com/{env}/api/v2/listening-topic/{topicId}
DELETE https://api2.sprinklr.com/{env}/api/v2/listening-topic/{topicId}

**Listening Topic Group API Endpoints**

Sprinklr Listening Topic Group APIs empowers you to programmatically Create, Read, Update and, Delete listening topics groups.
POST https://api2.sprinklr.com/{env}/api/v2/listening-group
GET https://api2.sprinklr.com/{env}/api/v2/listening-group/{Id}
PUT https://api2.sprinklr.com/{env}/api/v2/listening-group/{Id}
DELETE https://api2.sprinklr.com/{env}/api/v2/listening-group/{Id}

**Listening Keyword List API Endpoints**

Sprinklr Listening Keyword List APIs empowers you to programmatically Create, Read, Update and, Delete listening keyword lists.
POST https://api2.sprinklr.com/{env}/api/v2/keyword-list
GET https://api2.sprinklr.com/{env}/api/v2/keyword-list/{Id}
PUT https://api2.sprinklr.com/{env}/api/v2/keyword-list/{Id}
DELETE https://api2.sprinklr.com/{env}/api/v2/keyword-list/{Id}

**Listening Theme API Endpoints**

Sprinklr Listening Theme APIs empowers you to programmatically Create, Read, Update and, Delete listening themes.
POST https://api2.sprinklr.com/{env}/api/v2/listening-theme
GET https://api2.sprinklr.com/{env}/api/v2/listening-theme/{Id}
PUT https://api2.sprinklr.com/{env}/api/v2/listening-theme/{Id}
DELETE https://api2.sprinklr.com/{env}/api/v2/listening-theme/{Id}

**Listening Topic Backfill API Endpoints**

The Sprinklr Backfill APIs programmatically allows you to Create, Read, Accept and, Cancel backfill.
POST https://api2.sprinklr.com/{env}/api/v2/listening-topic-backfill
GET https://api2.sprinklr.com/{env}/api/v2/listening-topic-backfill/{Id}
PUT https://api2.sprinklr.com/{env}/api/v2/listening-theme/accept/{Id}
PUT https://api2.sprinklr.com/{env}/api/v2/listening-theme/cancel/{Id}

## **Data Ingestion API Endpoint ** - March 12, 2021

Introduction of new Data Ingestion API endpoints. We’re exposing new set of Data Ingestion API endpoints by which you can ingest Bulk Profile and Message within Sprinklr.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/data-ingestion/ingest

## **Read Dashboard List API Endpoint ** - March 12, 2021

Introduction of new Read Dashboard List API endpoint. You can use this API to pull a list of Sprinklr reporting and listening dashboards and can view the metadata including dashboard tags, listening topic IDs, and other metadata including the external dashboard link if enabled within Sprinklr UI.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/entity/{entityType}/filter

## **Bulk Import Entity API Endpoints ** - March 12, 2021

Introduction of new Bulk Import Entity API endpoints. You can use this API to import supported entities in bulk within Sprinklr.

`Supported Entity Types`: USER,
UNIVERSAL_PRODUCT,
UNIVERSAL_MESSAGE_STATUS,
MEDIA_ASSET,
ROLES_AND_PERMISSIONS,
PARTNER_QUEUE,
CLIENT_QUEUE,
PROFILE_LIST,
PROFILE_TAGGING_RULE,
CUSTOM_FIELD,
CAMPAIGN,
USER_GROUP,
ACCOUNT_GROUP,
ACCOUNT.

**API Endpoints**

GET https://api2.sprinklr.com/{env}/api/v2/file-import/download/template
POST https://api2.sprinklr.com/{env}/api/v2/file-import/entity

## **Stream API Endpoints ** - March 12, 2021

Introduction of new Stream API endpoints. We’re exposing new set of Stream API endpoints by which you can programmatically fetch the stream data of `Outbound Column` and `Inbound Column` from Sprinklr and can use Stream Cursor to fetch next set of data.

**API Endpoints**

POST https://api2.sprinklr.com/{env}/api/v2/stream/{streamId}/feed
GET https://api2.sprinklr.com/{env}/api/v2/stream/cursor/{nextPageCursor}

## **Media Upload API Endpoint ** - March 12, 2021

Introduction of new Media Upload API endpoints. You can use this API call to upload media, as well as to upload media as an input-stream in the content store.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/media/upload

## **Dashboard Stream Read API Enhancement** - March 12, 2021

To improve the efficiency and performance of Sprinlkr Dashboard Stream Read API, we have added a new sort parameter i.e `snModifiedTime`. Now you can sort response based on modified time.

**API Endpoints**

GET https://api2.sprinklr.com/{env}/api/v1/stream/{stream id}/feed

[](https://dev.sprinklr.com/jan-mar-2021)

[Back to top](https://dev.sprinklr.com/jan-mar-2021)
