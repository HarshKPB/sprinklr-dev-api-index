---
title: "Fetch Reporting Engines"
slug: fetch-reporting-engines
url: https://dev.sprinklr.com/fetch-reporting-engines
---

# Fetch Reporting Engines

#
GET Fetch Reporting Engines


With this API, you can fetch all the supported reporting engines for reporting insights. The Reporting Insights module in Sprinklr centralizes data from all your social channels and accounts and helps customize, expand, and drill into metrics by creating dashboards and widgets.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/reports/engines

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

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
curl -X GET \
'https://api3.sprinklr.com/{env}/api/v2/reports/engines' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

## Example - Response

 
 
     

{
    "data": [
        {
            "id": "AUDIENCE_LEAD",
            "name": "AUDIENCE_LEAD"
        },
        {
            "id": "ADOPTION",
            "name": "Adoption"
        },
        {
            "id": "ADOPTION_ENGAGEMENT",
            "name": "Adoption Engagement"
        },
        {
            "id": "AUDIENCE",
            "name": "Audience"
        },
        {
            "id": "AUDIENCE_ACTIVITY",
            "name": "Audience Activity"
        },
        {
            "id": "AUDIENCE_INSIGHTS",
            "name": "Audience Insights"
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
            "id": "CUSTOM_ENTITY",
            "name": "Custom Entity"
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
            "id": "LYEARN_REPORTING_ENGINE",
            "name": "LYEARN_REPORTING_ENGINE"
        },
        {
            "id": "LISTENING",
            "name": "Listening"
        },
        {
            "id": "RDB_FIREHOSE",
            "name": "Listening Explorer"
        },
        {
            "id": "SELF_SERVE_RDB_FIREHOSE",
            "name": "Listening Explorer"
        },
        {
            "id": "LIVE_DATASET",
            "name": "Live Dataset"
        },
        {
            "id": "MONITORING_LOG",
            "name": "Monitoring Log"
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
            "id": "PLATFORM_HEALTH",
            "name": "Platform Health"
        },
        {
            "id": "REAL_TIME",
            "name": "Real Time"
        },
        {
            "id": "SELF_SERVE_MESSAGE",
            "name": "Self Serve"
        },
        {
            "id": "SELF_SERVE_LISTENING",
            "name": "Self Serve"
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
            "id": "STORE_FRONT_AUDIENCE_ACTIVITY",
            "name": "Store"
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
            "id": "SPR_TASK",
            "name": "Task"
        },
        {
            "id": "UNIFIED_ANALYTICS_REPORTING_ENGINE",
            "name": "Unified Analytics"
        },
        {
            "id": "UNIVERSAL_COMMERCE_EVENT_ENGINE",
            "name": "Universal Commerce"
        },
        {
            "id": "UNIVERSAL_PROFILE",
            "name": "Universal Profile"
        },
        {
            "id": "VOICE_SEGMENT_ACTIVATION_CONFIG",
            "name": "VOICE_SEGMENT_ACTIVATION_CONFIG"
        },
        {
            "id": "VOICE",
            "name": "Voice Analytics"
        },
        {
            "id": "YOUTUBE_REPORTING_ENGINE",
            "name": "YouTube Analytics"
        },
        {
            "id": "wfm_reporting",
            "name": "wfm_reporting"
        }
    ],
    "errors": []
}
 

     
     
   
 

### Response Parameters





























| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| data |  | Array describing the id and name of the reporting engine | Array |
|  | id | The unique identifier for the reporting engine | String |
|  | name | The name of the reporting engine | String |

**Dev Notes: **Use [fetch metrics and dimensions API](https://dev.sprinklr.com/sprinklr-reporting-engines-fetch-metrics-and-dimensions-v1) to get all the metrics and dimensions associated for the given reporting engine.

	[](https://dev.sprinklr.com/fetch-reporting-engines) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-reporting-engines)
