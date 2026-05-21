---
title: "Fetch Metrics and Dimensions"
slug: fetch-metrics-and-dimensions
url: https://dev.sprinklr.com/fetch-metrics-and-dimensions
---

# Fetch Metrics and Dimensions

#
GET Fetch Metrics and Dimensions

This API enables you to retrieve metadata for specific reports within the specified platform. This endpoint provides details such as report fields, types, and any associated dimensions and metrics.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/reports/metadata/{reportingEngineId}?reportNames={reportName}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/'/api-key-and-secret-generation)



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

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| reportingEngineId | Required | String | Refers to the module specific reporting engine Id. You can refer to  to fetch the relevant engine Id |

## Query Parameters







| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| reportNames | Required | string | Report name for which the metadata is requested. |

## Example - Request




 Copy Code



curl -X GET \ 'https://api3.sprinklr.com/{env}/api/v2/reports/metadata/PLATFORM?reportNames=POST_INSIGHTS'
\
 -H 'Authorization: Bearer {Enter your Access_Token}' \
 -H 'Content-Type: application/json' \
 -H 'cache-control: no-cache' \
 -H 'key: {API_Key}'




## Example - Response

	{
    "data": {
        "POST_INSIGHTS": {
            "recordType": "LIFETIME",
            "measurements": [
                {
                    "type": "CUMULATIVE",
                    "measurementGroups": [
                        "FACEBOOK"
                    ],
                    "isShared": false,
                    "filterMeasurement": true,
                    "name": "POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_HIDE_ALL_CLICKS",
                    "fieldName": "POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_HIDE_ALL_CLICKS",
                    "displayName": "Facebook Post Negative Feedback Unique All Hide",
                    "hidden": false,
                    "enabledForAiConcierge": false,
                    "channelTypes": [
                        "FACEBOOK"
                    ]
                },
                {
                    "type": "CUMULATIVE",
                    "measurementGroups": [
                        "VK"
                    ],
                    "isShared": false,
                    "filterMeasurement": true,
                    "name": "VK_GROUP_LIKES_COUNT",
                    "fieldName": "VK_GROUP_LIKES_COUNT",
                    "displayName": "VK MeasurementGroup Likes",
                    "hidden": false,
                    "enabledForAiConcierge": false,
                    "channelTypes": [
                        "VK"
                    ]
                }
	                    "name": "POST_PART_OF_ALBUM",
                    "fieldName": "POST_PART_OF_ALBUM",
                    "displayName": "Is Post Part Of Album",
                    "hidden": false,
                    "enabledForAiConcierge": false,
                    "additional": {
                        "showAsDashbaordFilter": "true",
                        "singleSelect": "true"
                    }
                },
                {
                    "esServerType": "OUTBOUND_FEATURES_DETAIL",
                    "script": "spr-left-join-script",
                    "lang": "native",
                    "internalParams": {
                        "idField": "dimensions.POST_ID",
                        "defaultValue": "Not Classified",
                        "dateField": "modifiedTime",
                        "valueField": "postFeatures.ocr_gcv"
                    },
                    "onlyForAgg": false,
                    "type": "SCRIPT",
                    "sortable": false,
                    "translatable": false,
                    "lookupSupported": true,
                    "hoverable": false,
                    "editable": false,
                    "multiValue": true,
                    "multiValuedBackend": false,
                    "filterDimension": true,
                    "lookupKey": "postFeatures",
                    "name": "postFeatures.ocr_gcv",
                    "fieldName": "postFeatures.ocr_gcv",
                    "displayName": "Creative Insight: All Text in Asset",
                    "hidden": false,
                    "enabledForAiConcierge": false
                }
            ],
            "skipVisibilityFilters": false,
            "oldCustomFieldDimension": {
                "script": "spr-custom-property",
                "isSecureField": false,
                "cacheable": true,
                "internalParams": {},
                "primary": true,
                "type": "CUSTOM",
                "sortable": false,
                "translatable": false,
                "lookupSupported": true,
                "hoverable": false,
                "editable": false,
                "multiValue": false,
                "multiValuedBackend": false,
                "filterDimension": true,
                "dashboardGroups": [
                    "PARTNER_DASHBOARD",
                    "PAID_INITIATIVE_DASHBOARD",
                    "SPLIT_TESTING_DASHBOARD",
                    "FACEBOOK_CAMPAIGN_SPLIT_TESTING_DASHBOARD",
                    "TIKTOK_SPLIT_TESTING_DASHBOARD",
                    "GOOGLE_ANALYTICS_DASHBOARD",
                    "PACING_DASHBOARD",
                    "STRATEGY_GROUP_DASHBOARD",
                    "AD_SET_STRATEGY_GROUP_DASHBOARD",
                    "MEDIA_ASSET_INSIGHTS_DASHBOARD",
                    "OVERALL_DASHBOARD",
                    "BUDGET_DASHBOARD",
                    "ADVERTISING_VALUE_REALIZATION_DASHBOARD",
                    "POE",
                    "BRAND_ANALYTICS_DASHBOARD",
                    "ADS_COMMENT_ANALYSIS_DASHBOARD",
                    "ADS_APPROVAL_AND_REJECTIONS_DASHBOARD",
                    "CAMPAIGN_DASHBOARD",
                    "SOCIAL_ENGAGEMENT_DASHBOARD",
                    "SUPERVISOR_CONSOLE_DASHBOARDS",
                    "COACHING_SESSION_DASHBOARDS",
                    "QM_DASHBOARDS",
                    "CALL_OVERVIEW_DASHBOARD",
                    "AGENT_INSIGHTS_DASHBOARD",
                    "CONVERSATIONAL_ANALYTICS_DASHBOARDS",
                    "CASE_ANALYSIS_DASHBOARDS",
                    "SOCIAL_NATIVE_DASHBOARD",
                    "JOURNEY_EXECUTION_REPORTING",
                    "INFLUENCER_CAMPAIGN_INSIGHTS",
                    "INFLUENCER_PROFILE_ANALYTICS_DASHBOARD",
                    "YOUTUBE_INFLUENCER_PROFILE_ANALYTICS_DASHBOARD",
                    "TIKTOK_INFLUENCER_PROFILE_ANALYTICS_DASHBOARD",
                    "INBOUND_TAG_DASHBOARD",
                    "OUTBOUND_TAG_DASHBOARD",
                    "COMMUNITY_DASHBOARD",
                    "SLA_DASHBOARD",
                    "STAGE_SLA_DASHBOARD",
                    "MACRO_SLA_DASHBOARD",
                    "COMMERCE_STD_DASHBOARD",
                    "PROFILE_DASHBOARD",
                    "SAM_DASHBOARD",
                    "PBUC_VALUE_DASHBOARD",
                    "SMART_TRIAGE_DASHBOARD",
                    "SMART_CONTENT_INTELLIGENCE",
                    "API_REPORT_INSIGHTS",
                    "WEBHOOK_REPORT_INSIGHTS",
                    "EXTENSION_REPORT_INSIGHTS",
                    "MARKETING_VALUE_REALIZATION_DASHBOARD",
                    "FIN_PLAN_DASHBOARD_GROUP",
                    "CFM_TEXT_ANALYTICS_DASHBOARD",
                    "AI_CREATIVE_INSIGHTS_DASHBOARD",
                    "AGENT_PERFORMANCE",
                    "PBUC_CARE_DASHBOARD",
                    "CASE_SMART_THEME_EXPLORER_DASHBOARD",
                    "INBOUND_SMART_THEME_EXPLORER_DASHBOARD",
                    "SURVEY_SMART_THEME_EXPLORER_DASHBOARD",
                    "IVR_DASHBOARD",
                    "SPR_VOICE_MONITORING_DASHBOARD",
                    "GUIDED_PATHS_DASHBOARD",
                    "ACW_DASHBOARD",
                    "SPRINKLR_VALUE_DASHBOARD",
                    "USER_HOMEPAGE_DASHBOARD",
                    "BOT_APPLICATION_REPORTING_DASHBOARD",
                    "GLOBAL_TITLE_BENCHMARKING",
                    "GALLERY_ANALYTICS_DASHBOARD"
                ],
                "name": "OUTBOUND_CUSTOM_PROPERTY",
                "fieldName": "customProperties",
                "displayName": "Outbound Message Custom Property",
                "hidden": false,
                "enabledForAiConcierge": false,
                "additional": {
                    "reportName": "POST_INSIGHTS"
                }
            },
            "oldCustomFieldDimensionName": "OUTBOUND_CUSTOM_PROPERTY_NAME",
            "displayName": "POST_INSIGHTS",
            "dateFieldName": "date"
        }
    },
    "errors": []
}



## Response Schema

The following table focuses on the core structures and the primary arrays and objects that are essential to understanding the API response schema.







``

| Parameter |  | Type | Description |
| --- | --- | --- | --- |
| data |  | object | Contains the core report data, categorized by report name. |
|  | {{report_name}} | object | Represents the specific report data related to the report name sent in the API request. |
|  | recordType | string | Indicates the type of record, e.g., LIFETIME. |
|  | measurements | array | An array of measurement objects providing detailed metrics. |
|  | dimensions | array | An array of dimension objects specifying the dimensions associated with the report. |
|  | filterDimensions | array | An array of filter dimension objects used for filtering the report data. |
|  | oldCustomFieldDimension | object | Represents the old custom field dimension details. |
|  | skipVisibilityFilters | boolean | Indicates if visibility filters are skipped for the report. |
|  | oldCustomFieldDimensionName | string | The name of the old custom field dimension. |
|  | displayName | string | The display name of the report. |
|  | dateFieldName | string | The field name representing the date for the report. |
| errors |  | array | An array containing error objects if any errors occur during the API request processing. |

[](https://dev.sprinklr.com/fetch-metrics-and-dimensions) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-metrics-and-dimensions)
