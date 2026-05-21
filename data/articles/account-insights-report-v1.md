---
title: "Account Insights Report v1"
slug: account-insights-report-v1
url: https://dev.sprinklr.com/account-insights-report-v1
---

# Account Insights Report v1

#
  POST - Account Insights Report

This report is used to gather the insights for the accounts.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/reports/query


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

## Available Request Parameters









```

```

| Parameter | Value |
| --- | --- |
| reportingEngine | PLATFORM |
| report | ACCOUNT_INSIGHTS |
| Supported groupBys.dimensionName | ACCOUNT_ID (appears as account name in response) |
| Supported filters.dimensionName | CLIENT_ID SN_TYPE ACCOUNT_ID |
| Supported projections.measurementName | CPM    	   FACEBOOK_PAGE_CHECKINS   FACEBOOK_PAGE_CHECKINS_DAYS_28   FACEBOOK_PAGE_CHECKINS_DAYS_7   FACEBOOK_PAGE_CHECKINS_MOBILE   FACEBOOK_PAGE_CHECKINS_MOBILE_DAYS_28   FACEBOOK_PAGE_CHECKINS_MOBILE_DAYS_7   FACEBOOK_PAGE_CHECKINS_MOBILE_UNIQUE   FACEBOOK_PAGE_CHECKINS_MOBILE_UNIQUE_DAYS_28   FACEBOOK_PAGE_CHECKINS_MOBILE_UNIQUE_DAYS_7   FACEBOOK_PAGE_CHECKINS_UNIQUE   FACEBOOK_PAGE_CHECKINS_UNIQUE_DAYS_28   FACEBOOK_PAGE_CHECKINS_UNIQUE_DAYS_7   FACEBOOK_PAGE_CONSUMPTIONS   FACEBOOK_PAGE_CONSUMPTIONS_DAYS_28   FACEBOOK_PAGE_CONSUMPTIONS_DAYS_7   FACEBOOK_PAGE_CONSUMPTIONS_UNIQUE   FACEBOOK_PAGE_CONSUMPTIONS_UNIQUE_DAYS_28   FACEBOOK_PAGE_CONSUMPTIONS_UNIQUE_DAYS_7   FACEBOOK_PAGE_ENGAGED_USERS   FACEBOOK_PAGE_ENGAGED_USERS_DAYS_28   FACEBOOK_PAGE_ENGAGED_USERS_DAYS_7   FACEBOOK_PAGE_FAN_ADDS   FACEBOOK_PAGE_FAN_ADDS_UNIQUE   FACEBOOK_PAGE_FAN_REMOVES   FACEBOOK_PAGE_FAN_REMOVES_UNIQUE   FACEBOOK_PAGE_FANS   FACEBOOK_PAGE_FANS_ONLINE   FACEBOOK_PAGE_IMPRESSIONS   FACEBOOK_PAGE_IMPRESSIONS_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_DAYS_7   FACEBOOK_PAGE_IMPRESSIONS_ORGANIC   FACEBOOK_PAGE_IMPRESSIONS_ORGANIC_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_ORGANIC_DAYS_7   FACEBOOK_PAGE_IMPRESSIONS_ORGANIC_UNIQUE   FACEBOOK_PAGE_IMPRESSIONS_ORGANIC_UNIQUE_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_ORGANIC_UNIQUE_DAYS_7   FACEBOOK_PAGE_IMPRESSIONS_PAID   FACEBOOK_PAGE_IMPRESSIONS_PAID_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_PAID_DAYS_7   FACEBOOK_PAGE_IMPRESSIONS_PAID_UNIQUE   FACEBOOK_PAGE_IMPRESSIONS_PAID_UNIQUE_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_PAID_UNIQUE_DAYS_7   FACEBOOK_PAGE_IMPRESSIONS_UNIQUE   FACEBOOK_PAGE_IMPRESSIONS_UNIQUE_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_UNIQUE_DAYS_7   FACEBOOK_PAGE_IMPRESSIONS_VIRAL   FACEBOOK_PAGE_IMPRESSIONS_VIRAL_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_VIRAL_DAYS_7   FACEBOOK_PAGE_IMPRESSIONS_VIRAL_UNIQUE   FACEBOOK_PAGE_IMPRESSIONS_VIRAL_UNIQUE_DAYS_28   FACEBOOK_PAGE_IMPRESSIONS_VIRAL_UNIQUE_DAYS_7   FACEBOOK_PAGE_NEGATIVE_FEEDBACK   FACEBOOK_PAGE_NEGATIVE_FEEDBACK_DAYS_28   FACEBOOK_PAGE_NEGATIVE_FEEDBACK_DAYS_7   FACEBOOK_PAGE_NEGATIVE_FEEDBACK_UNIQUE   FACEBOOK_PAGE_NEGATIVE_FEEDBACK_UNIQUE_DAYS_28   FACEBOOK_PAGE_NEGATIVE_FEEDBACK_UNIQUE_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS   FACEBOOK_PAGE_POSTS_IMPRESSIONS_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS_ORGANIC   FACEBOOK_PAGE_POSTS_IMPRESSIONS_ORGANIC_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_ORGANIC_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS_ORGANIC_UNIQUE   FACEBOOK_PAGE_POSTS_IMPRESSIONS_ORGANIC_UNIQUE_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_ORGANIC_UNIQUE_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS_PAID   FACEBOOK_PAGE_POSTS_IMPRESSIONS_PAID_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_PAID_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS_PAID_UNIQUE   FACEBOOK_PAGE_POSTS_IMPRESSIONS_PAID_UNIQUE_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_PAID_UNIQUE_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS_UNIQUE   FACEBOOK_PAGE_POSTS_IMPRESSIONS_UNIQUE_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_UNIQUE_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS_VIRAL   FACEBOOK_PAGE_POSTS_IMPRESSIONS_VIRAL_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_VIRAL_DAYS_7   FACEBOOK_PAGE_POSTS_IMPRESSIONS_VIRAL_UNIQUE   FACEBOOK_PAGE_POSTS_IMPRESSIONS_VIRAL_UNIQUE_DAYS_28   FACEBOOK_PAGE_POSTS_IMPRESSIONS_VIRAL_UNIQUE_DAYS_7   FACEBOOK_PAGE_STORIES   FACEBOOK_PAGE_STORIES_DAYS_28   FACEBOOK_PAGE_STORIES_DAYS_7   FACEBOOK_PAGE_STORYTELLERS   FACEBOOK_PAGE_STORYTELLERS_DAYS_28   FACEBOOK_PAGE_STORYTELLERS_DAYS_7   FACEBOOK_PAGE_VIEWS   FACEBOOK_PAGE_VIEWS_LOGIN   FACEBOOK_PAGE_VIEWS_LOGIN_UNIQUE   FACEBOOK_PAGE_VIEWS_LOGOUT   FACEBOOK_PAGE_VIEWS_UNIQUE   FOLLOWERS_COUNT   FOLLOWING_COUNT   FS_PAGE_LIKES   FS_PAGE_PHOTOS   FS_PAGE_TIPS   FS_VENUE_CHECKINS   FS_VENUE_CHECKINS_SHARED_ON_FACEBOOK   FS_VENUE_CHECKINS_SHARED_ON_TWITTER   FS_VENUE_LIKES   FS_VENUE_NEW_CHECKINS   FS_VENUE_PHOTOS   FS_VENUE_TIPS   FS_VENUE_UNIQUE_VISITORS   GPLUS_CIRCLED   GPLUS_PLUS_ONES   INSTAGRAM_FOLLOWERS   INSTAGRAM_FOLLOWINGS   INSTAGRAM_MEDIA_UPLOADS   LINKEDIN_COMPANY_EMPLOYEE_FOLLOWERS   LINKEDIN_COMPANY_FOLLOWERS   LINKEDIN_COMPANY_NON_EMPLOYEE_FOLLOWERS   LINKEDIN_COMPANY_ORGANIC_FOLLOWERS   LINKEDIN_COMPANY_PAID_FOLLOWERS   LINKEDIN_GROUP_FOLLOWERS   LINKEDIN_STATUS_CLICKS   LINKEDIN_STATUS_COMMENTS   LINKEDIN_STATUS_IMPRESSIONS   LINKEDIN_STATUS_LIKES   LINKEDIN_STATUS_SHARES   MEDIA_VALUE   NET_LIKES   PINTEREST_USER_BOARD_COUNT   PINTEREST_USER_FOLLOWERS   PINTEREST_USER_LIKES   PINTEREST_USER_LOW_ENGAGEMENT_BOARD_COUNT   PINTEREST_USER_PIN_COUNT   RENREN_ALBUMS   RENREN_BLOGS   RENREN_FANS   RENREN_SHARES   SLIDESHARE_SLIDE_SHOWS   TENCENT_WEIBO_FAVORITES   TENCENT_WEIBO_FOLLOWERS   TENCENT_WEIBO_FOLLOWINGS   TENCENT_WEIBO_POSTS   TUMBLR_BLOG_FOLLOWERS   TUMBLR_BLOG_LIKES   TUMBLR_BLOG_POSTS   TUMBLR_USER_FOLLOWING   TUMBLR_USER_LIKES   TWITTER_DMS   TWITTER_FAVORITES   TWITTER_FOLLOWERS_COUNT   TWITTER_LISTED   TWITTER_MENTIONS   TWITTER_NEW_FOLLOWERS   TWITTER_REPLIES   TWITTER_RETWEETS   TWITTER_SENT_DMS   TWITTER_SENT_MENTIONS   TWITTER_SENT_REPLIES   TWITTER_SENT_RETWEETS   TWITTER_SENT_UPDATES   TWITTER_UNFOLLOWERS   TWITTER_UNFOLLOWINGS   VK_GROUP_ALBUMS   VK_GROUP_FOLLOWERS   VK_GROUP_PHOTOS   VK_GROUP_POSTS   VK_GROUP_REACH   VK_GROUP_REACH_SUBSCRIBERS   VK_GROUP_TOPICS   VK_GROUP_VIDEOS   VK_GROUP_VIEWS   VK_GROUP_VISITORS   WEIBO_BI_FOLLOWERS   WEIBO_FAVOURITES   WEIBO_FOLLOWERS   WEIBO_FRIENDS   WEIBO_STATUSES   YOUTUBE_CHANNEL_ANNOTATION_CLICK_THROUGH_RATE   YOUTUBE_CHANNEL_ANNOTATION_CLOSE_RATE   YOUTUBE_CHANNEL_AVERAGE_VIEW_DURATION   YOUTUBE_CHANNEL_AVERAGE_VIEW_PERCENTAGE   YOUTUBE_CHANNEL_COMMENTS   YOUTUBE_CHANNEL_DISLIKES   YOUTUBE_CHANNEL_ESTIMATED_MINUTES_WATCHED   YOUTUBE_CHANNEL_FAVORITES   YOUTUBE_CHANNEL_FAVORITES_ADDED // Deprecated by YouTube   YOUTUBE_CHANNEL_FAVORITES_REMOVED // Deprecated by YouTube   YOUTUBE_CHANNEL_LIKES   YOUTUBE_CHANNEL_SHARES   YOUTUBE_CHANNEL_SUBSCRIBERS   YOUTUBE_CHANNEL_SUBSCRIBERS_GAINED   YOUTUBE_CHANNEL_SUBSCRIBERS_LOST   YOUTUBE_CHANNEL_UNIQUE_VIEWS // Deprecated by YouTube   YOUTUBE_CHANNEL_UNIQUE_VIEWS_30 // Deprecated by YouTube   YOUTUBE_CHANNEL_UNIQUE_VIEWS_7 // Deprecated by YouTube   YOUTUBE_CHANNEL_VIEWS |

## Example 1: Weekly Report

Retrieve weekly report with the following metrics along with weekly changes, grouped by accountId.

FACEBOOK_PAGE_FANS

FACEBOOK_PAGE_VIEWS

FACEBOOK_PAGE_IMPRESSIONS




 Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v1/reports/query' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
	-d '{
 "reportingEngine": "PLATFORM",
 "report": "ACCOUNT_INSIGHTS",
 "startTime": 1399852800000,
 "endTime": 1402113599000,
 "page": 0,
 "pageSize": 15,
 "filters": [
   {
     "dimensionName": "SN_TYPE",
     "filterType": "IN",
     "values": [
       "FACEBOOK"
     ],
     "details": null
   },
   {
     "dimensionName": "CLIENT_ID",
     "filterType": "IN",
     "values": [
       "62"
     ],
     "details": {
     }
   },
   {
     "dimensionName": "ACCOUNT_ID",
     "filterType": "IN",
     "values": [
       "3051",
       "553",
       "565"
     ],
	     "details": {
     }
   }
 ],
 "groupBys": [
   {
     "heading": "ACCOUNT_ID",
     "dimensionName": "ACCOUNT_ID",
     "groupType": "FIELD",
     "details": {
     }
   },
	   {
     "heading": "date",
     "dimensionName": "date",
     "groupType": "DATE_HISTOGRAM",
     "details": {
       "interval": "1w"                                                               ←----------- this will provide weekly report
     }
   }
 ],
 "projections": [
   {
     "heading": "FACEBOOK_PAGE_FANS",
     "measurementName": "FACEBOOK_PAGE_FANS",
     "aggregateFunction": "SUM",
     "details": null
   },
	   {
     "heading": "FACEBOOK_PAGE_VIEWS",
     "measurementName": "FACEBOOK_PAGE_VIEWS",
     "aggregateFunction": "SUM",
     "details": null
   },
   {
     "heading": "FACEBOOK_PAGE_IMPRESSIONS",
     "measurementName": "FACEBOOK_PAGE_IMPRESSIONS",
     "aggregateFunction": "SUM",
     "details": null
   }
 ],
 "projectionDecorations": [
   "CHANGE"                                                         ←-------This requests for change from the previous period
 ]
}'





### Example - Response




 {
 "headings": [
   "ACCOUNT_ID",
   "date",
   "FACEBOOK_PAGE_FANS",
   "FACEBOOK_PAGE_FANS_CHANGE",
   "FACEBOOK_PAGE_VIEWS",
   "FACEBOOK_PAGE_VIEWS_CHANGE",
   "FACEBOOK_PAGE_IMPRESSIONS",
   "FACEBOOK_PAGE_IMPRESSIONS_CHANGE"
 ],
"rows": [
   [
     "Nanny",                                          ←-------Account Name
     "05/12/2014",                               ←-------start of the week
     108,                                                 ←-------FACEBOOK_PAGE_FANS
     19,                                                   ←-------FACEBOOK_PAGE_FANS_CHANGE
     77,                                                   ←-------FACEBOOK_PAGE_VIEWS
     68,                                                   ←-------FACEBOOK_PAGE_VIEWS_CHANGE
     205185,                                          ←-------FACEBOOK_PAGE_IMPRESSIONS
     203999                                           ←-------FACEBOOK_PAGE_IMPRESSIONS_CHANGE
   ],
	 [
     "Nanny",
     "05/19/2014",
     304,
     196,
     59,
     -18,
     326164,
     120979
   ],
   [
     "Nanny",
     "05/26/2014",
     300,
     -4,
     1,
     -58,
     8899,
     -317265
   ],
   [
     "Nanny",
     "06/02/2014",
     293,
     -7,
     6,
     5,
     5726,
     -3173
   ],
   [
     "DreamMalar",
     "05/12/2014",
     58,
     0,
     0,
     -1,
     192,
     -285
   ],
   [
     "DreamMalar",
     "05/19/2014",
     58,
     0,
     6,
     6,
     121,
     -71
   ],
   [
     "DreamMalar",
     "05/26/2014",
     58,
     0,
     0,
     -6,
     44,
     -77
   ],
   [
     "DreamMalar",
     "06/02/2014",
     58,
     0,
     1,
     1,
     40413,
     40369
   ],
   [
     "SprinklrMalar",
     "05/12/2014",
     0,
     0,
     0,
     0,
     431,
     -1789
   ],
   [
     "SprinklrMalar",
     "05/19/2014",
     0,
     0,
     0,
     0,
     250,
     -181
   ],
   [
     "SprinklrMalar",
     "05/26/2014",
     0,
     0,
     0,
     0,
     72,
     -178
   ],
   [
     "SprinklrMalar",
     "06/02/2014",
     8,
     8,
     0,
     0,
     57,
     -15
   ]
 ]
}





## Example 2: DAY_OF_WEEK

Retrieve DAY_OF_WEEK report with the following metrics grouped by accountId:

FACEBOOK_PAGE_VIEWS

FACEBOOK_PAGE_VIEWS_UNIQUE

FACEBOOK_PAGE_VIEWS_LOGIN

FACEBOOK_PAGE_VIEWS_LOGIN_UNIQUE

FACEBOOK_PAGE_VIEWS_LOGOUT




 Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v1/reports/query' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
 "reportingEngine": "PLATFORM",
 "report": "ACCOUNT_INSIGHTS",
 "startTime": 1399435200000,
 "endTime": 1402113599000,
 "pageSize": 10,
 "filters": [
   {
     "dimensionName": "SN_TYPE",
     "filterType": "IN",
     "values": [
       "FACEBOOK"
     ],
     "details": null
   },
   {
     "dimensionName": "CLIENT_ID",
     "filterType": "IN",
     "values": [
       "62"
     ],
     "details": {
     }
   },
   {
     "dimensionName": "ACCOUNT_ID",
     "filterType": "IN",
     "values": [
       "3051",
       "553",
       "565"
     ],
     "details": {
     }
   }
 ],
 "groupBys": [
   {
     "heading": "ACCOUNT_ID",
     "dimensionName": "ACCOUNT_ID",
     "groupType": "FIELD",
     "details": {
     }
   },
   {
     "heading": "DAY_OF_WEEK",
     "dimensionName": "DAY_OF_WEEK",
     "groupType": "FIELD"
   }
 ],
 "projections": [
   {
     "heading": "FACEBOOK_PAGE_VIEWS",
     "measurementName": "FACEBOOK_PAGE_VIEWS",
     "aggregateFunction": "SUM",
     "details": null
   },
   {
     "heading": "FACEBOOK_PAGE_VIEWS_UNIQUE",
     "measurementName": "FACEBOOK_PAGE_VIEWS_UNIQUE",
     "aggregateFunction": "SUM",
     "details": null
   },
   {
     "heading": "FACEBOOK_PAGE_VIEWS_LOGIN",
     "measurementName": "FACEBOOK_PAGE_VIEWS_LOGIN",
     "aggregateFunction": "SUM",
     "details": null
   },
   {
     "heading": "FACEBOOK_PAGE_VIEWS_LOGIN_UNIQUE",
     "measurementName": "FACEBOOK_PAGE_VIEWS_LOGIN_UNIQUE",
     "aggregateFunction": "SUM",
     "details": null
   },
   {
     "heading": "FACEBOOK_PAGE_VIEWS_LOGOUT",
     "measurementName": "FACEBOOK_PAGE_VIEWS_LOGOUT",
     "aggregateFunction": "SUM",
     "details": null
   }
 ]
}'





### Example - Response





{
 "headings": [
   "ACCOUNT_ID",
   "DAY_OF_WEEK",
   "FACEBOOK_PAGE_VIEWS",
   "FACEBOOK_PAGE_VIEWS_UNIQUE",
   "FACEBOOK_PAGE_VIEWS_LOGIN",
   "FACEBOOK_PAGE_VIEWS_LOGIN_UNIQUE",
   "FACEBOOK_PAGE_VIEWS_LOGOUT"
 ],
 "rows": [
   [
     "Nanny",
     "Sunday",
     27,
     16,
     27,
     16,
     0
   ],
   [
     "Nanny",
     "Monday",
     19,
     15,
     19,
     15,
     0
   ],
   [
     "Nanny",
     "Tuesday",
     8,
     7,
     8,
     7,
     0
   ],
   [
     "Nanny",
     "Wednesday",
     25,
     16,
     25,
     16,
     0
   ],
   [
     "Nanny",
     "Thursday",
     21,
     21,
     21,
     21,
     0
   ],
   [
     "Nanny",
     "Friday",
     27,
     23,
     27,
     23,
     0
   ],
   [
     "Nanny",
     "Saturday",
     18,
     16,
     18,
     16,
     0
   ],
   [
     "DreamMalar",
     "Sunday",
     0,
     0,
     0,
     0,
     0
   ],
   [
     "DreamMalar",
     "Monday",
     5,
     1,
     5,
     1,
     0
   ],
   [
     "DreamMalar",
     "Tuesday",
     0,
     0,
     0,
     0,
     0
   ]
 ]
}





[](https://dev.sprinklr.com/account-insights-report-v1)




[Back to top](https://dev.sprinklr.com/account-insights-report-v1)
