---
title: "Sprinklr Reporting Engines - Fetch Metrics and Dimensions v1"
slug: sprinklr-reporting-engines-fetch-metrics-and-dimensions-v1
url: https://dev.sprinklr.com/sprinklr-reporting-engines-fetch-metrics-and-dimensions-v1
---

# Sprinklr Reporting Engines - Fetch Metrics and Dimensions v1

#
  GET - Sprinklr Reporting Engines - Fetch Metrics and Dimensions

Using this API, you can fetch the available Metrics and Dimensions in Reports from various Reporting Engine available in Sprinklr.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/reports/metadata/{ReportingEngineId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Path Parameters

[Fetch Reporting Engines API](https://dev.sprinklr.com/fetch-reporting-engines)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| reportingEngineId | Required | Refers to the name of the reporting engine.You can fetch supported reporting engines Ids using . | String |

## Available Reporting Engines

You can fetch the available reporting engines using [Fetch Reporting Engines API](https://dev.sprinklr.com/fetch-reporting-engines).




 Copy Code



        {
            "id": "ADOPTION",
            "name": "Adoption"
        },
        {
            "id": "ADOPTION_ENGAGEMENT",
            "name": "Adoption Engagement"
        },
        {
            "id": "AUDIENCE_ACTIVITY",
            "name": "Audience Activity"
        },
        {
            "id": "BENCHMARKING",
            "name": "Benchmarking"
        },
        {
            "id": "SELF_SERVE_BENCHMARKING",
            "name": "Benchmarking"
        },
        {
            "id": "COMMUNITY",
            "name": "Community"
        },
        {
            "id": "CONSUMPTION",
            "name": "Consumption Analytics"
        },
        {
            "id": "GALLERY_AUDIENCE_ACTIVITY",
            "name": "Gallery"
        },
        {
            "id": "INBOUND_MESSAGE",
            "name": "Inbound Analytics"
        },
        {
            "id": "SELF_SERVE_LISTENING",
            "name": "Listening"
        },
        {
            "id": "LISTENING",
            "name": "Listening"
        },
    {
        "id": "LIVE_DATASET",
        "name": "Live Dataset"
    },

    {
        "id": "OUTBOUND_MESSAGE",
        "name": "Outbound Message"
    },
    {
        "id": "PAID",
        "name": "Paid"
    },
    {
        "id": "REAL_TIME",
        "name": "Real Time"
    },
    {
        "id": "SELF_SERVE_MESSAGE",
        "name": "SELF_SERVE_MESSAGE"
    },
    {
        "id": "PLATFORM",
        "name": "Social Analytics"
    },
    {
        "id": "AUDIENCE_INSIGHT",
        "name": "Social DMP"
    },
    {
        "id": "SPR_TASK",
        "name": "Spr Task"
    },
    {
        "id": "SELF_SERVE_STORY_MESSAGE",
        "name": "Story Analytics"
    },
    {
        "id": "STORY_MESSAGE",
        "name": "Story Analytics"
    },
    {
        "id": "TRACK_SITE",
        "name": "Track Sites"
    },
    {
        "id": "UNIVERSAL_COMMERCE_EVENT_ENGINE",
        "name": "UNIVERSAL_COMMERCE_EVENT_ENGINE"
    },
    {
        "id": "UNIFIED_ANALYTICS_REPORTING_ENGINE",
        "name": "Unified Analytics"
    },
    {
        "id": "UNIVERSAL_PROFILE",
        "name": "Universal Profile"
    },
    {
        "id": "VOICE",
        "name": "Voice Analytics"
    },
    {
        "id": "YOUTUBE_REPORTING_ENGINE",
        "name": "YouTube Analytics"
    }





## Example for LISTENING





 Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/reports/metadata/LISTENING' \
 -H 'Authorization: Bearer {Enter your Access_Token}' \
 -H 'Content-Type: application/json' \
 -H 'cache-control: no-cache' \
 -H 'key: {API_Key}'





### Response:

You will get the response as per the request.

## Example for PAID




 Copy Code



curl -X GET \
 https://api3.sprinklr.com/{env}/api/v1/reports/metadata/PAID \
 -H 'Authorization: Bearer {Enter your Access_Token}' \
 -H 'Content-Type: application/json' \
 -H 'cache-control: no-cache' \
 -H 'key: {API_Key}'





### Response:

You will get the response as per the request.

## Example for PLATFORM




 Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/reports/metadata/PLATFORM' \
 -H 'Authorization: Bearer {Enter your Access_Token}' \
 -H 'Content-Type: application/json' \
 -H 'cache-control: no-cache' \
 -H 'key: {API_Key}'





### Response:

You will get the response as per the request.

[](https://dev.sprinklr.com/sprinklr-reporting-engines-fetch-metrics-and-dimensions-v1)




[Back to top](https://dev.sprinklr.com/sprinklr-reporting-engines-fetch-metrics-and-dimensions-v1)
