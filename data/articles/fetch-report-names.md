---
title: "Fetch Report Names"
slug: fetch-report-names
url: https://dev.sprinklr.com/fetch-report-names
---

# Fetch Report Names

#
GET Fetch Report Names


Using this API, you can fetch the report name associated with the given reporting engine Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/reports/reports/{reportingEngineId}

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Path Parameters

[Fetch Reporting Engine API](https://dev.sprinklr.com/fetch-reporting-engines)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| reportingEngineId | Required | Refers to the unique identifier for the reporting engine.You can fetch reporting engine Id using . | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
curl -X GET \
'https://api3.sprinklr.com/{env}/api/v2/reports/reports/PLATFORM' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



## Example - Response

{
    "data": [
        {
            "id": "ACCOUNT_INBOUND_VOLUME",
            "name": "ACCOUNT_INBOUND_VOLUME"
        },
        {
            "id": "ACCOUNT_INSIGHTS",
            "name": "ACCOUNT_INSIGHTS"
        },
        {
            "id": "AGENT_PERFORMANCE_AGGREGATED_REPORT",
            "name": "AGENT_PERFORMANCE_AGGREGATED_REPORT"
        },
        {
            "id": "AGENT_SESSION_AGGREGATE_REPORT",
            "name": "AGENT_SESSION_AGGREGATE_REPORT"
        },
        {
            "id": "AGENT_STATUS_REPORT",
            "name": "AGENT_STATUS_REPORT"
        },
        {
            "id": "ALLOCATE_TIME",
            "name": "ALLOCATE_TIME"
        },
        {
            "id": "ANALYTICS",
            "name": "ANALYTICS"
        },
        {
            "id": "ANALYTICS_DEMOGRAPHIC",
            "name": "ANALYTICS_DEMOGRAPHIC"
        },
        {
            "id": "ANALYTICS_PAGE",
            "name": "ANALYTICS_PAGE"
        },
        {
            "id": "APPOINTMENT",
            "name": "APPOINTMENT"
        },
        {
            "id": "APPROVAL_STATS",
            "name": "APPROVAL_STATS"
        },
        {
            "id": "ASSET_APPROVAL",
            "name": "ASSET_APPROVAL"
        },
        {
            "id": "ASSET_PROPERTIES",
            "name": "ASSET_PROPERTIES"
        },
        {
            "id": "ASSIGNMENT_ENGINE",
            "name": "ASSIGNMENT_ENGINE"
        },
        {
            "id": "ASSIGNMENT_ENGINE_BACKLOG",
            "name": "ASSIGNMENT_ENGINE_BACKLOG"
        },
        {
            "id": "ASSIGNMENT_ENGINE_CURRENT_STATS_REPORTING",
            "name": "ASSIGNMENT_ENGINE_CURRENT_STATS_REPORTING"
        },
        {
            "id": "AUDIT_CHECKLIST",
            "name": "AUDIT_CHECKLIST"
        },
        {
            "id": "AUDIT_CHECKLIST_CALIBRATION",
            "name": "AUDIT_CHECKLIST_CALIBRATION"
        },
        {
            "id": "AUDIT_CHECKLIST_RESPONSE",
            "name": "AUDIT_CHECKLIST_RESPONSE"
        },
        {
            "id": "CAMPAIGN_AGENT_PERFORMANCE_REPORT",
            "name": "CAMPAIGN_AGENT_PERFORMANCE_REPORT"
        },
        {
            "id": "CASE_MACRO_USAGE",
            "name": "CASE_MACRO_USAGE"
        },
        {
            "id": "CASE_STAGE_SLA",
            "name": "CASE_STAGE_SLA"
        },
        {
            "id": "CHANNEL_MESSAGE_ACTION_STATS",
            "name": "CHANNEL_MESSAGE_ACTION_STATS"
        },
        {
            "id": "CLICKS_ACTIVITY",
            "name": "CLICKS_ACTIVITY"
        },
        {
            "id": "CLICKS_ACTIVITY_BY_CITY",
            "name": "CLICKS_ACTIVITY_BY_CITY"
        },
        {
            "id": "CLICKS_ACTIVITY_BY_COUNTRY",
            "name": "CLICKS_ACTIVITY_BY_COUNTRY"
        },
        {
            "id": "CLICKS_ACTIVITY_BY_DEVICE_TYPE",
            "name": "CLICKS_ACTIVITY_BY_DEVICE_TYPE"
        },
        {
            "id": "CLICKS_ACTIVITY_BY_PLATFORM",
            "name": "CLICKS_ACTIVITY_BY_PLATFORM"
        },
        {
            "id": "CLICKS_ACTIVITY_BY_USER_AGENT",
            "name": "CLICKS_ACTIVITY_BY_USER_AGENT"
        },
        {
            "id": "CLIENT_QUEUE_MESSAGE",
            "name": "CLIENT_QUEUE_MESSAGE"
        },
        {
            "id": "CONTENT_SUGGESTION_STATS",
            "name": "CONTENT_SUGGESTION_STATS"
        },
        {
            "id": "CO_BROWSE_MODE_REPORT",
            "name": "CO_BROWSE_MODE_REPORT"
        },
        {
            "id": "CO_BROWSING",
            "name": "CO_BROWSING"
        },
        {
            "id": "CURRENT_ASSIGNMENT_REPORT",
            "name": "CURRENT_ASSIGNMENT_REPORT"
        },
        {
            "id": "CaseCustomPropertyAccessDetailsReport",
            "name": "CaseCustomPropertyAccessDetailsReport"
        },
        {
            "id": "CaseProcessingSLAReport",
            "name": "CaseProcessingSLAReport"
        },
        {
            "id": "CaseSLAReport",
            "name": "CaseSLAReport"
        },
        {
            "id": "CaseWorkflowSnapshotReport",
            "name": "CaseWorkflowSnapshotReport"
        },
        {
            "id": "ComprehensiveCaseSLAReport",
            "name": "ComprehensiveCaseSLAReport"
        },
        {
            "id": "DATAHUB_ORDER",
            "name": "DATAHUB_ORDER"
        },
        {
            "id": "DEVICE_ATLAS_ANALYSIS",
            "name": "DEVICE_ATLAS_ANALYSIS"
        },
        {
            "id": "DOMAIN_INSIGHTS_REPORT",
            "name": "DOMAIN_INSIGHTS_REPORT"
        },
        {
            "id": "FACEBOOK_HOURLY_INSIGHTS",
            "name": "FACEBOOK_HOURLY_INSIGHTS"
        },
        {
            "id": "FACEBOOK_PAGE_FANS_ONLINE_BY_HOUR",
            "name": "FACEBOOK_PAGE_FANS_ONLINE_BY_HOUR"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_AGE_GENDER",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_AGE_GENDER"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_CITY",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_CITY"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_CONSUMPTION_TYPE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_CONSUMPTION_TYPE"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_COUNTRY",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_COUNTRY"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_FREQUENCY_DISTRIBUTION",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_FREQUENCY_DISTRIBUTION"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_LIKE_SOURCE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_LIKE_SOURCE"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_LOCALE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_LOCALE"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_NEGATIVE_FEEDBACK_TYPE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_NEGATIVE_FEEDBACK_TYPE"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_POSITIVE_FEEDBACK_TYPE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_POSITIVE_FEEDBACK_TYPE"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_PROFILE_TAB",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_PROFILE_TAB"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_REFERRALS",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_REFERRALS"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_SITE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_SITE"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_STORY_TYPE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_STORY_TYPE"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_TAB",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_TAB"
        },
        {
            "id": "FACEBOOK_PAGE_INSIGHTS_BY_UNLIKE_SOURCE",
            "name": "FACEBOOK_PAGE_INSIGHTS_BY_UNLIKE_SOURCE"
        },
        {
            "id": "FACEBOOK_PAGE_TAB_INSIGHTS",
            "name": "FACEBOOK_PAGE_TAB_INSIGHTS"
        },
        {
            "id": "FACEBOOK_PAGE_VIDEO_AD_CPM_BY_DISTRIBUTION_TYPE",
            "name": "FACEBOOK_PAGE_VIDEO_AD_CPM_BY_DISTRIBUTION_TYPE"
        },
        {
            "id": "FACEBOOK_PAGE_VIDEO_AD_EARNINGS_BY_DISTRIBUTION_TYPE",
            "name": "FACEBOOK_PAGE_VIDEO_AD_EARNINGS_BY_DISTRIBUTION_TYPE"
        },
        {
            "id": "FACEBOOK_PAGE_VIDEO_AD_IMPRESSIONS_BY_DISTRIBUTION_TYPE",
            "name": "FACEBOOK_PAGE_VIDEO_AD_IMPRESSIONS_BY_DISTRIBUTION_TYPE"
        },
        {
            "id": "FACEBOOK_PAGE_VIEWS_BY_DEVICE",
            "name": "FACEBOOK_PAGE_VIEWS_BY_DEVICE"
        },
        {
            "id": "FACEBOOK_POST_BY_ACTION_TYPE_REPORT",
            "name": "FACEBOOK_POST_BY_ACTION_TYPE_REPORT"
        },
        {
            "id": "FACEBOOK_POST_BY_AGE_GENDER_REPORT",
            "name": "FACEBOOK_POST_BY_AGE_GENDER_REPORT"
        },
        {
            "id": "FACEBOOK_POST_BY_COUNTRY_REPORT",
            "name": "FACEBOOK_POST_BY_COUNTRY_REPORT"
        },
        {
            "id": "FACEBOOK_POST_BY_DISTRIBUTION_TYPE_REPORT",
            "name": "FACEBOOK_POST_BY_DISTRIBUTION_TYPE_REPORT"
        },
        {
            "id": "FACEBOOK_POST_BY_REGION_REPORT",
            "name": "FACEBOOK_POST_BY_REGION_REPORT"
        },
        {
            "id": "FACEBOOK_POST_BY_TYPE_REPORT",
            "name": "FACEBOOK_POST_BY_TYPE_REPORT"
        },
        {
            "id": "FACEBOOK_VIDEO_RETENTION_GRAPH",
            "name": "FACEBOOK_VIDEO_RETENTION_GRAPH"
        },
        {
            "id": "FEEDBACK_REPORT",
            "name": "FEEDBACK_REPORT"
        },
        {
            "id": "FOURSQUARE_LOCATION_STATS",
            "name": "FOURSQUARE_LOCATION_STATS"
        },
        {
            "id": "FOURSQUARE_PAGE_INSIGHT_BY_VENUE",
            "name": "FOURSQUARE_PAGE_INSIGHT_BY_VENUE"
        },
        {
            "id": "FOURSQUARE_VENUE_INSIGHT_BY_AGE",
            "name": "FOURSQUARE_VENUE_INSIGHT_BY_AGE"
        },
        {
            "id": "FOURSQUARE_VENUE_INSIGHT_BY_GENDER",
            "name": "FOURSQUARE_VENUE_INSIGHT_BY_GENDER"
        },
        {
            "id": "GENERIC_SLA",
            "name": "GENERIC_SLA"
        },
        {
            "id": "GOOGLE_ANALYTICS_BULK_REPORT",
            "name": "GOOGLE_ANALYTICS_BULK_REPORT"
        },
        {
            "id": "INBOUND_CASE",
            "name": "INBOUND_CASE"
        },
        {
            "id": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_AGE_GENDER",
            "name": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_AGE_GENDER"
        },
        {
            "id": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_CITY",
            "name": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_CITY"
        },
        {
            "id": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_COUNTRY",
            "name": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_COUNTRY"
        },
        {
            "id": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_LOCALE",
            "name": "INSTAGRAM_BUSINESS_PAGE_INSIGHTS_BY_LOCALE"
        },
        {
            "id": "INSTAGRAM_BUSINESS_PAGE_ONLINE_FOLLOWERS",
            "name": "INSTAGRAM_BUSINESS_PAGE_ONLINE_FOLLOWERS"
        },
        {
            "id": "INSTAGRAM_HOURLY_INSIGHTS",
            "name": "INSTAGRAM_HOURLY_INSIGHTS"
        },
        {
            "id": "INTERCEPT_ACTIVITY",
            "name": "INTERCEPT_ACTIVITY"
        },
        {
            "id": "INTUITION_FEEDBACK",
            "name": "INTUITION_FEEDBACK"
        },
        {
            "id": "KB_CONTENT_REPORT",
            "name": "KB_CONTENT_REPORT"
        },
        {
            "id": "KB_EVENT_REPORT",
            "name": "KB_EVENT_REPORT"
        },
        {
            "id": "LINKEDIN_INSIGHTS_BY_COMPANYSIZE",
            "name": "LINKEDIN_INSIGHTS_BY_COMPANYSIZE"
        },
        {
            "id": "LINKEDIN_INSIGHTS_BY_COUNTRY",
            "name": "LINKEDIN_INSIGHTS_BY_COUNTRY"
        },
        {
            "id": "LINKEDIN_INSIGHTS_BY_FUNCTION",
            "name": "LINKEDIN_INSIGHTS_BY_FUNCTION"
        },
        {
            "id": "LINKEDIN_INSIGHTS_BY_INDUSTRY",
            "name": "LINKEDIN_INSIGHTS_BY_INDUSTRY"
        },
        {
            "id": "LINKEDIN_INSIGHTS_BY_REGION",
            "name": "LINKEDIN_INSIGHTS_BY_REGION"
        },
        {
            "id": "LINKEDIN_INSIGHTS_BY_SENIORITIES",
            "name": "LINKEDIN_INSIGHTS_BY_SENIORITIES"
        },
        {
            "id": "MACRO_USAGE_REPORT",
            "name": "MACRO_USAGE_REPORT"
        },
        {
            "id": "MEDIA_ASSET_STATS",
            "name": "MEDIA_ASSET_STATS"
        },
        {
            "id": "OMNITURE_SITE_CATALYST",
            "name": "OMNITURE_SITE_CATALYST"
        },
        {
            "id": "OPERATIONAL_KPI",
            "name": "OPERATIONAL_KPI"
        },
        {
            "id": "OUTBOUND_MACRO_USAGE_REPORT",
            "name": "OUTBOUND_MACRO_USAGE_REPORT"
        },
        {
            "id": "OUTBOUND_STATS",
            "name": "OUTBOUND_STATS"
        },
        {
            "id": "PAID_ORGANIC_EXECUTABLE_REPORT",
            "name": "PAID_ORGANIC_EXECUTABLE_REPORT"
        },
        {
            "id": "PARTNER_QUEUE_INSIGHTS",
            "name": "PARTNER_QUEUE_INSIGHTS"
        },
        {
            "id": "PEOPLE_PROFILED_INSIGHTS",
            "name": "PEOPLE_PROFILED_INSIGHTS"
        },
        {
            "id": "PINTEREST_BOARD_INSIGHTS",
            "name": "PINTEREST_BOARD_INSIGHTS"
        },
        {
            "id": "POST_INSIGHTS",
            "name": "POST_INSIGHTS"
        },
        {
            "id": "POST_INSIGHTS_TREND",
            "name": "POST_INSIGHTS_TREND"
        },
        {
            "id": "POST_RESOLUTION_TIME",
            "name": "POST_RESOLUTION_TIME"
        },
        {
            "id": "POST_RESPONSE_TIME",
            "name": "POST_RESPONSE_TIME"
        },
        {
            "id": "PROFILE_OPPORTUNITY_REPORT",
            "name": "PROFILE_OPPORTUNITY_REPORT"
        },
        {
            "id": "ProfileCustomPropertyChangeReport",
            "name": "ProfileCustomPropertyChangeReport"
        },
        {
            "id": "REDDIT_ACCOUNT_HOURLY_INSIGHTS",
            "name": "REDDIT_ACCOUNT_HOURLY_INSIGHTS"
        },
        {
            "id": "REMINDER_FOLLOW_UP_REPORT",
            "name": "REMINDER_FOLLOW_UP_REPORT"
        },
        {
            "id": "RULE_ENGINE_ACTION_TRACKER",
            "name": "RULE_ENGINE_ACTION_TRACKER"
        },
        {
            "id": "SIMILAR_CASE_EVENT_REPORT",
            "name": "SIMILAR_CASE_EVENT_REPORT"
        },
        {
            "id": "SIMILAR_GUIDED_PATH_EVENT_REPORT",
            "name": "SIMILAR_GUIDED_PATH_EVENT_REPORT"
        },
        {
            "id": "SMART_COMPOSE_ADOPTION_REPORT",
            "name": "SMART_COMPOSE_ADOPTION_REPORT"
        },
        {
            "id": "SMART_PARAPHRASE_REPORT",
            "name": "SMART_PARAPHRASE_REPORT"
        },
        {
            "id": "SOCIAL_APPS_TAB_INSIGHTS",
            "name": "SOCIAL_APPS_TAB_INSIGHTS"
        },
        {
            "id": "SOCIAL_APPS_WIDGET_INSIGHTS",
            "name": "SOCIAL_APPS_WIDGET_INSIGHTS"
        },
        {
            "id": "SOCIAL_ASSET_TERMS_AND_CONDITIONS",
            "name": "SOCIAL_ASSET_TERMS_AND_CONDITIONS"
        },
        {
            "id": "SOCIAL_STREAM_INSIGHTS",
            "name": "SOCIAL_STREAM_INSIGHTS"
        },
        {
            "id": "SPR_TASK_SLA",
            "name": "SPR_TASK_SLA"
        },
        {
            "id": "STAGE_SLA",
            "name": "STAGE_SLA"
        },
        {
            "id": "STANDARD_SLA",
            "name": "STANDARD_SLA"
        },
        {
            "id": "SUBDOMAIN_INSIGHT_REPORT",
            "name": "SUBDOMAIN_INSIGHT_REPORT"
        },
        {
            "id": "SUGGESTED_RESPONSES_REPORT",
            "name": "SUGGESTED_RESPONSES_REPORT"
        },
        {
            "id": "SURVEY_CLICK_TRACKER_REPORT",
            "name": "SURVEY_CLICK_TRACKER_REPORT"
        },
        {
            "id": "SURVEY_QUESTION_RESPONSE",
            "name": "SURVEY_QUESTION_RESPONSE"
        },
        {
            "id": "SURVEY_REPORT",
            "name": "SURVEY_REPORT"
        },
        {
            "id": "SURVEY_RESPONSE_INSTANCE",
            "name": "SURVEY_RESPONSE_INSTANCE"
        },
        {
            "id": "TIKTOK_BUSINESS_ACCOUNT_BY_COUNTRY_REPORT",
            "name": "TIKTOK_BUSINESS_ACCOUNT_BY_COUNTRY_REPORT"
        },
        {
            "id": "TIKTOK_BUSINESS_ACCOUNT_BY_GENDER_REPORT",
            "name": "TIKTOK_BUSINESS_ACCOUNT_BY_GENDER_REPORT"
        },
        {
            "id": "TIKTOK_BUSINESS_ACCOUNT_BY_HOUR_REPORT",
            "name": "TIKTOK_BUSINESS_ACCOUNT_BY_HOUR_REPORT"
        },
        {
            "id": "TIKTOK_VIDEO_BY_COUNTRY_REPORT",
            "name": "TIKTOK_VIDEO_BY_COUNTRY_REPORT"
        },
        {
            "id": "TIKTOK_VIDEO_BY_SOURCE_REPORT",
            "name": "TIKTOK_VIDEO_BY_SOURCE_REPORT"
        },
        {
            "id": "TWITCH_GAME_INSIGHTS_REPORT",
            "name": "TWITCH_GAME_INSIGHTS_REPORT"
        },
        {
            "id": "TWITTER_HOURLY_INSIGHTS",
            "name": "TWITTER_HOURLY_INSIGHTS"
        },
        {
            "id": "TWITTER_HOURLY_INSIGHTS_TREND",
            "name": "TWITTER_HOURLY_INSIGHTS_TREND"
        },
        {
            "id": "TWITTER_INSIGHTS_TRACK",
            "name": "TWITTER_INSIGHTS_TRACK"
        },
        {
            "id": "USER_ASSIGNMENT",
            "name": "USER_ASSIGNMENT"
        },
        {
            "id": "USER_AVAILABILITY_REPORT",
            "name": "USER_AVAILABILITY_REPORT"
        },
        {
            "id": "USER_AVAILABILITY_SLA_REPORT",
            "name": "USER_AVAILABILITY_SLA_REPORT"
        },
        {
            "id": "USER_CURRENT_STATE",
            "name": "USER_CURRENT_STATE"
        },
        {
            "id": "USER_LOGIN_ACTIVITIES",
            "name": "USER_LOGIN_ACTIVITIES"
        },
        {
            "id": "USER_OCCUPANCY",
            "name": "USER_OCCUPANCY"
        },
        {
            "id": "USER_PROPERTIES",
            "name": "USER_PROPERTIES"
        },
        {
            "id": "USER_SLA",
            "name": "USER_SLA"
        },
        {
            "id": "VANITY_URL_CLICKS_ACTIVITY",
            "name": "VANITY_URL_CLICKS_ACTIVITY"
        },
        {
            "id": "VIDEO_CHAT",
            "name": "VIDEO_CHAT"
        },
        {
            "id": "VK_GROUP_POST_REACH_BY_AGE_RANGE_AND_GENDER",
            "name": "VK_GROUP_POST_REACH_BY_AGE_RANGE_AND_GENDER"
        },
        {
            "id": "VK_GROUP_POST_REACH_BY_CITY",
            "name": "VK_GROUP_POST_REACH_BY_CITY"
        },
        {
            "id": "VK_GROUP_POST_REACH_BY_COUNTRY",
            "name": "VK_GROUP_POST_REACH_BY_COUNTRY"
        },
        {
            "id": "VK_GROUP_VISITOR_AGE_RANGE",
            "name": "VK_GROUP_VISITOR_AGE_RANGE"
        },
        {
            "id": "VK_GROUP_VISITOR_BY_AGE_RANGE_AND_GENDER",
            "name": "VK_GROUP_VISITOR_BY_AGE_RANGE_AND_GENDER"
        },
        {
            "id": "VK_GROUP_VISITOR_BY_CITIES",
            "name": "VK_GROUP_VISITOR_BY_CITIES"
        },
        {
            "id": "VK_GROUP_VISITOR_BY_COUNTRY",
            "name": "VK_GROUP_VISITOR_BY_COUNTRY"
        },
        {
            "id": "VK_GROUP_VISITOR_BY_GENDER",
            "name": "VK_GROUP_VISITOR_BY_GENDER"
        },
        {
            "id": "VK_POLL",
            "name": "VK_POLL"
        },
        {
            "id": "VOICE",
            "name": "VOICE"
        },
        {
            "id": "VOICE_AGENT_PERFORMANCE",
            "name": "VOICE_AGENT_PERFORMANCE"
        },
        {
            "id": "VOICE_SEGMENT_ACTIVATION_CONFIG",
            "name": "VOICE_SEGMENT_ACTIVATION_CONFIG"
        },
        {
            "id": "VOICE_SUPERVISOR_MONITOR_REPORT",
            "name": "VOICE_SUPERVISOR_MONITOR_REPORT"
        },
        {
            "id": "VOICE_TRUNK",
            "name": "VOICE_TRUNK"
        },
        {
            "id": "WECHAT_ACCOUNT_INSIGHTS_BY_CITY",
            "name": "WECHAT_ACCOUNT_INSIGHTS_BY_CITY"
        },
        {
            "id": "WECHAT_ACCOUNT_INSIGHTS_BY_COUNTRY",
            "name": "WECHAT_ACCOUNT_INSIGHTS_BY_COUNTRY"
        },
        {
            "id": "WECHAT_ACCOUNT_INSIGHTS_BY_LANGUAGE",
            "name": "WECHAT_ACCOUNT_INSIGHTS_BY_LANGUAGE"
        },
        {
            "id": "WECHAT_ACCOUNT_INSIGHTS_BY_STATE",
            "name": "WECHAT_ACCOUNT_INSIGHTS_BY_STATE"
        },
        {
            "id": "WE_CHAT_MESSAGE",
            "name": "WE_CHAT_MESSAGE"
        },
        {
            "id": "WE_CHAT_MESSAGE_TREND",
            "name": "WE_CHAT_MESSAGE_TREND"
        },
        {
            "id": "WHATSAPP_BUSINESS_ACCOUNT_INSIGHTS",
            "name": "WHATSAPP_BUSINESS_ACCOUNT_INSIGHTS"
        },
        {
            "id": "WORKFORCE_SCHEDULE_REPORT",
            "name": "WORKFORCE_SCHEDULE_REPORT"
        },
        {
            "id": "WORKFORCE_STAFFING_DIFFERENCE_REPORT",
            "name": "WORKFORCE_STAFFING_DIFFERENCE_REPORT"
        },
        {
            "id": "YOUTUBE_ACCOUNT_INSIGHTS_BY_AGE_GENDER",
            "name": "YOUTUBE_ACCOUNT_INSIGHTS_BY_AGE_GENDER"
        },
        {
            "id": "YOUTUBE_ACCOUNT_INSIGHTS_BY_COUNTRY",
            "name": "YOUTUBE_ACCOUNT_INSIGHTS_BY_COUNTRY"
        },
        {
            "id": "YOUTUBE_BULK_API_INSIGHTS",
            "name": "YOUTUBE_BULK_API_INSIGHTS"
        },
        {
            "id": "YOUTUBE_VIDEO_HOURLY_INSIGHTS_TREND_REPORT",
            "name": "YOUTUBE_VIDEO_HOURLY_INSIGHTS_TREND_REPORT"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_BY_AGE_GENDER",
            "name": "YOUTUBE_VIDEO_INSIGHTS_BY_AGE_GENDER"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_BY_COUNTRY",
            "name": "YOUTUBE_VIDEO_INSIGHTS_BY_COUNTRY"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_BY_DEVICE",
            "name": "YOUTUBE_VIDEO_INSIGHTS_BY_DEVICE"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_BY_PLAYER_LOCATION",
            "name": "YOUTUBE_VIDEO_INSIGHTS_BY_PLAYER_LOCATION"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_BY_REFERRER",
            "name": "YOUTUBE_VIDEO_INSIGHTS_BY_REFERRER"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_TREND",
            "name": "YOUTUBE_VIDEO_INSIGHTS_TREND"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_TREND_BY_DEVICE",
            "name": "YOUTUBE_VIDEO_INSIGHTS_TREND_BY_DEVICE"
        },
        {
            "id": "YOUTUBE_VIDEO_INSIGHTS_TREND_BY_REFERRER",
            "name": "YOUTUBE_VIDEO_INSIGHTS_TREND_BY_REFERRER"
        }
    ],
    "errors": []
}
 

     
     
   

### Response Parameters





























| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| data |  | Array describing the id and name of the reporting engine | Array |
|  | id | The unique identifier for the reporting name | String |
|  | name | Refers to the report name | String |

	[](https://dev.sprinklr.com/fetch-report-names) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-report-names)
