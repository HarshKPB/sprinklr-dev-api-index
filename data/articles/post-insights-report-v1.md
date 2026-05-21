---
title: "Post Insights Report v1"
slug: post-insights-report-v1
url: https://dev.sprinklr.com/post-insights-report-v1
---

# Post Insights Report v1

#
  POST - Post Insights Report

This report is used to gather the insights for the published brand posts.

## API Endpoint

https://api3.sprinklr.com`/{path}/`api/v1/reports/query


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
| report | POST_INSIGHTS |
| Supported groupBys.dimensionName | POST_ID: this returns a minified Post object POST_TEXT CLIENT_ID SN_TYPE ACCOUNT_ID (appears as account name in response) USER_ID PARENT_POST_ID SN_MESSAGE_TYPE MEDIA_ASSET_ID MEDIA_TYPE CAMPAIGN_ID GEO_TARGETING_ENABLED GEO_TARGET_CITIES GEO_TARGET_COUNTRIES GEO_TARGET_LOCALES GEO_TARGET_REGIONS GEO_TARGET_GENDER GEO_TARGET_RELATIONSHIP_STATUS GEO_TARGET_EDUCATION_STATUS GEO_TARGET_INTERESTED_IN GEO_TARGET_MIN_AGE GEO_TARGET_MAX_AGE ACTUAL_LINK customProperties CLIENT_GROUP_ID ACCOUNT_GROUP_ID USER_GROUP_ID POST_PUBLISHED_DATE  APPROVER_USER_GROUP_ID |
| Supported filters.dimensionName | CLIENT_ID SN_TYPE ACCOUNT_ID SN_MESSAGE_TYPE CAMPAIGN_ID USER_ID customProperties |
| Supported projections.measurementName | CPM    	  POST_REAL_CLICK_COUNT POST_CLICK_COUNT POST_LIKE_COUNT POST_SHARE_COUNT POST_COMMENT_COUNT POST_REACH_COUNT YOUTUBE_VIDEO_LIKES YOUTUBE_VIDEO_DISLIKES YOUTUBE_VIDEO_FAVORITES YOUTUBE_VIDEO_FAVORITES_ADDED // Deprecated by YouTube YOUTUBE_VIDEO_FAVORITES_REMOVED // Deprecated by YouTube YOUTUBE_VIDEO_COMMENTS YOUTUBE_VIDEO_SHARES YOUTUBE_VIDEO_VIEWS YOUTUBE_VIDEO_UNIQUE_VIEWS // Deprecated by YouTube YOUTUBE_VIDEO_ESTIMATED_MINUTES_WATCHED YOUTUBE_VIDEO_AVERAGE_VIEW_DURATION YOUTUBE_VIDEO_AVERAGE_VIEW_PERCENTAGE YOUTUBE_VIDEO_ANNOTATION_CLICK_THROUGH_RATE YOUTUBE_VIDEO_ANNOTATION_CLOSE_RATE WEIBO_POST_COMMENTS_COUNT WEIBO_POST_REPOSTS_COUNT WEIBO_POST_FAVORITES_COUNT RENREN_POST_COMMENTS_COUNT RENREN_POST_LIKES_COUNT LINKEDIN_COMPANY_POST_COMMENTS_COUNT LINKEDIN_COMPANY_POST_LIKES_COUNT LINKEDIN_COMPANY_POST_SHARES_COUNT LINKEDIN_COMPANY_POST_IMPRESSIONS_COUNT LINKEDIN_COMPANY_POST_CLICKS_COUNT LINKEDIN_GROUP_POST_COMMENTS_COUNT LINKEDIN_GROUP_POST_LIKES_COUNT TENCENT_WEIBO_COMMENTS_COUNT TENCENT_WEIBO_REPOSTS_COUNT POST_FB_STREAM_COMMENT_COUNT POST_FB_STREAM_LIKE_COUNT POST_FB_STREAM_SHARE_COUNT POST_FB_IMPRESSIONS_FAN POST_FB_IMPRESSIONS_FAN_UNIQUE POST_FB_IMPRESSIONS_FAN_PAID POST_FB_IMPRESSIONS_FAN_PAID_UNIQUE POST_FB_IMPRESSIONS_ORGANIC POST_FB_IMPRESSIONS_ORGANIC_UNIQUE POST_FB_IMPRESSIONS POST_FB_IMPRESSIONS_UNIQUE POST_FB_IMPRESSIONS_VIRAL POST_FB_IMPRESSIONS_VIRAL_UNIQUE POST_FB_IMPRESSIONS_BY_STORY_TYPE_COMMENT POST_FB_IMPRESSIONS_BY_STORY_TYPE_FAN POST_FB_IMPRESSIONS_BY_STORY_TYPE_LINK POST_FB_IMPRESSIONS_BY_STORY_TYPE_OTHER POST_FB_IMPRESSIONS_BY_STORY_TYPE_UNIQUE_COMMENT POST_FB_CLAIM_COUNT POST_FB_CLAIM_LIMIT POST_FB_IMPRESSIONS_BY_STORY_TYPE_UNIQUE_FAN POST_FB_IMPRESSIONS_BY_STORY_TYPE_UNIQUE_LINK POST_FB_IMPRESSIONS_BY_STORY_TYPE_UNIQUE_OTHER POST_FB_NEGATIVE_FEEDBACK POST_FB_NEGATIVE_FEEDBACK_UNIQUE POST_FB_IMPRESSIONS_PAID POST_FB_IMPRESSIONS_PAID_UNIQUE POST_FB_STORIES POST_FB_CONSUMPTIONS POST_FB_CONSUMPTIONS_UNIQUE POST_FB_STORYTELLERS POST_FB_ENGAGED_USERS POST_FB_STORYTELLERS_BY_ACTION_TYPE_COMMENT POST_FB_STORYTELLERS_BY_ACTION_TYPE_LIKE POST_FB_STORYTELLERS_BY_ACTION_TYPE_SHARE POST_FB_STORYTELLERS_BY_ACTION_TYPE_ANSWER POST_FB_STORYTELLERS_BY_ACTION_TYPE_FOLLOW POST_FB_STORYTELLERS_BY_ACTION_TYPE_CLAIM POST_FB_STORYTELLERS_BY_ACTION_TYPE_OTHER POST_FB_STORYTELLERS_BY_ACTION_TYPE_RSVP POST_FB_STORIES_BY_ACTION_TYPE_COMMENT POST_FB_STORIES_BY_ACTION_TYPE_LIKE POST_FB_STORIES_BY_ACTION_TYPE_SHARE POST_FB_STORIES_BY_ACTION_TYPE_ANSWER POST_FB_STORIES_BY_ACTION_TYPE_FOLLOW POST_FB_STORIES_BY_ACTION_TYPE_CLAIM POST_FB_STORIES_BY_ACTION_TYPE_OTHER POST_FB_STORIES_BY_ACTION_TYPE_RSVP POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_HIDE_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_HIDE_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_HIDE_ALL_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_HIDE_ALL_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNLIKE_PAGE_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_UNLIKE_PAGE_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_REPORT_SPAM_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_REPORT_SPAM_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_XBUTTON POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_XBUTTON POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_XBUTTON_CLICKS POST_FB_NEGATIVE_FEEDBACK_BY_TYPE_UNIQUE_XBUTTON_CLICKS POST_FB_CONSUMPTIONS_BY_TYPE_LINK_CLICKS POST_FB_CONSUMPTIONS_BY_TYPE_UNIQUE_LINK_CLICKS POST_FB_CONSUMPTIONS_BY_TYPE_OTHER_CLICKS POST_FB_CONSUMPTIONS_BY_TYPE_UNIQUE_OTHER_CLICKS POST_FB_CONSUMPTIONS_BY_TYPE_VIDEO_PLAY POST_FB_CONSUMPTIONS_BY_TYPE_UNIQUE_VIDEO_PLAY POST_FB_CONSUMPTIONS_BY_TYPE_PHOTO_VIEW POST_FB_CONSUMPTIONS_BY_TYPE_UNIQUE_PHOTO_VIEW POST_FB_VIDEO_AVG_TIME_WATCHED POST_FB_VIDEO_LENGTH POST_FB_VIDEO_COMPLETE_VIEWS_ORGANIC POST_FB_VIDEO_COMPLETE_VIEWS_ORGANIC_UNIQUE POST_FB_VIDEO_COMPLETE_VIEWS_PAID POST_FB_VIDEO_COMPLETE_VIEWS_PAID_UNIQUE POST_FB_VIDEO_VIEWS_ORGANIC POST_FB_VIDEO_VIEWS_ORGANIC_UNIQUE POST_FB_VIDEO_VIEWS_PAID POST_FB_VIDEO_VIEWS_PAID_UNIQUE POST_FB_REACTIONS_LOVE_TOTAL POST_FB_REACTIONS_WOW_TOTAL POST_FB_REACTIONS_SORRY_TOTAL POST_FB_REACTIONS_HAHA_TOTAL POST_FB_REACTIONS_ANGER_TOTAL POST_FB_STREAM_LOVE_COUNT POST_FB_STREAM_WOW_COUNT POST_FB_STREAM_SAD_COUNT POST_FB_STREAM_HAHA_COUNT POST_FB_STREAM_ANGRY_COUNT FLICKR_PHOTO_COMMENT_COUNT FLICKR_PHOTO_VIEWS_COUNT POST_SS_COMMENT_COUNT POST_SS_VIEW_COUNT POST_SS_FAVORITE_COUNT POST_SS_DOWNLOAD_COUNT POST_GPLUS_SHARE_COUNT POST_GPLUS_COMMENT_COUNT POST_GPLUS_PLUSONE_COUNT INSTAGRAM_POST_COMMENTS_COUNT INSTAGRAM_POST_LIKES_COUNT VK_GROUP_COMMENTS_COUNT VK_GROUP_LIKES_COUNT VK_GROUP_REPOSTS_COUNT TUMBLR_NOTES_COUNT FS_TIP_TODO_COUNT FS_TIP_DONE_COUNT FS_TIP_LIKES_COUNT FOLLOWER_COUNT_AT_POST POST_CLICK_COUNT_WITH_REF_URL PUBLISHED_MESSAGE_COUNT TOTAL_ENGAGEMENT ENGAGEMENT_RATE REACH_RATE POST_FB_VIRILITY POST_COMMENT_COUNT POST_LIKE_COUNT POST_REACH_COUNT |

## Example 1: Simple Report

Retrieve the following metrics grouped by campaignId and only for clientId=193.

- POST_REACH_COUNT

- TOTAL_ENGAGEMENT

- PUBLISHED_MESSAGE_COUNT

### Example - Request




 Copy Code



curl -X POST \
   https://api3.sprinklr.com/{env}/api/v1/reports/query \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
 "report": "POST_INSIGHTS",
 "reportingEngine": "PLATFORM",
 "startTime": 1399348800000,
 "endTime": 1402027199000,
 "timeZone": "UTC",
 "filters": [
   {
     "dimensionName": "CLIENT_ID",
     "filterType": "IN",
     "values": [
       "193"
     ],
     "details": {
     }
   }
 ],
 "groupBys": [
   {
     "heading": "CAMPAIGN_ID",
     "dimensionName": "CAMPAIGN_ID",
     "groupType": "FIELD",
     "details": null
   }
 ],
 "projections": [
   {
     "heading": "POST_REACH_COUNT",
     "measurementName": "POST_REACH_COUNT",
     "aggregateFunction": "SUM",
     "details": null
   },
   {
     "heading": "TOTAL_ENGAGEMENT",
     "measurementName": "TOTAL_ENGAGEMENT",
     "aggregateFunction": "SUM",
     "details": null
   },
   {
     "heading": "brandPosts",
     "measurementName": "PUBLISHED_MESSAGE_COUNT",
     "aggregateFunction": "SUM",
     "details": null
   }
 ]
}'





### Example - Response





{
 "headings": [
   "CAMPAIGN_ID",
   "POST_REACH_COUNT",
   "TOTAL_ENGAGEMENT",
   "brandPosts"
 ],
 "rows": [
   [
     "AM_Campaign_1 (Chandrashekhar_J)",              ←---- CAMPAIGN_ID
     6,                                               ←----  POST_REACH_COUNT
     0,                                               ←----  TOTAL_ENGAGEMENT
     12                                               ←----  PUBLISHED_MESSAGE_COUNT
   ],
   [
     "AM_Campaign_2 (Amoon)",
     1,
     0,
     5
   ],
   [
     "[Auto Import] (Amoon)",
     0,
     0,
     4
   ]
 ]
}





## Example 2: With Minified Post Object

Retrieve the following metrics along with minified Post object for the first two posts during the interval and only for clientId=226,186.  And the entries to be sorted by POST_REAL_CLICK_COUNT in descending order:

- TOTAL_ENGAGEMENT

- POST_LIKE_COUNT

- POST_COMMENT_COUNT

- POST_SHARE_COUNT

- POST_REACH_COUNT

- POST_FB_IMPRESSIONS

- POST_FB_ENGAGED_USERS

- POST_FB_NEGATIVE_FEEDBACK

- YOUTUBE_VIDEO_DISLIKES

- YOUTUBE_VIDEO_VIEWS

- POST_REAL_CLICK_COUNT

**Dev Notes: **Twitter content in the response does not show the message text or the post metrics.


### Example - Request





 Copy Code



curl -X POST \
   https://api3.sprinklr.com/{env}/api/v1/reports/query \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "report": "POST_INSIGHTS",
  "reportingEngine": "PLATFORM",
  "startTime": 1400126340000,
  "endTime": 1424563200000,
  "timeZone": "UTC",
  "page": 0,
  "pageSize": 2,
  "filters": [
    {
      "dimensionName": "SN_TYPE",
      "filterType": "IN",
      "values": [
           "GOOGLE_PLUS",
        "FACEBOOK"
      ],
      "details": null
    },
    {
      "dimensionName": "CLIENT_ID",
      "filterType": "IN",
      "values": [
        "226"
      ],
      "details": {
      }
    }
  ],
  "groupBys": [
    {
      "heading": "POST_ID",
      "dimensionName": "POST_ID",
      "groupType": "FIELD",
      "details": null
    }
  ],
  "projections": [
    {
      "heading": "TOTAL_ENGAGEMENT",
      "measurementName": "TOTAL_ENGAGEMENT",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_LIKE_COUNT",
      "measurementName": "POST_LIKE_COUNT",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_COMMENT_COUNT",
      "measurementName": "POST_COMMENT_COUNT",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_SHARE_COUNT",
      "measurementName": "POST_SHARE_COUNT",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_REACH_COUNT",
      "measurementName": "POST_REACH_COUNT",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_FB_IMPRESSIONS",
      "measurementName": "POST_FB_IMPRESSIONS",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_FB_ENGAGED_USERS",
      "measurementName": "POST_FB_ENGAGED_USERS",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_FB_NEGATIVE_FEEDBACK",
      "measurementName": "POST_FB_NEGATIVE_FEEDBACK",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "YOUTUBE_VIDEO_DISLIKES",
      "measurementName": "YOUTUBE_VIDEO_DISLIKES",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "YOUTUBE_VIDEO_VIEWS",
      "measurementName": "YOUTUBE_VIDEO_VIEWS",
      "aggregateFunction": "SUM",
      "details": null
    },
    {
      "heading": "POST_REAL_CLICK_COUNT",
      "measurementName": "POST_REAL_CLICK_COUNT",
      "aggregateFunction": "SUM",
      "details": null
    }
  ],
  "sorts": [
    {
      "heading": "POST_REAL_CLICK_COUNT",
      "order": "DESC"
    }
  ]
}'





### Example - Response





{
  "headings": [
    "POST_ID",
    "TOTAL_ENGAGEMENT",
    "POST_LIKE_COUNT",
    "POST_COMMENT_COUNT",
    "POST_SHARE_COUNT",
    "POST_REACH_COUNT",
    "POST_FB_IMPRESSIONS",
    "POST_FB_ENGAGED_USERS",
    "POST_FB_NEGATIVE_FEEDBACK",
    "YOUTUBE_VIDEO_DISLIKES",
    "YOUTUBE_VIDEO_VIEWS",
    "POST_REAL_CLICK_COUNT"
  ],
  "rows": [
    [
      {
        "postId": 3803311,
        "messageId": 3803312,
        "accountId": 2827,
        "authorId": 0,
        "clientId": 186,
        "messageType": 2,
        "channelType": "FACEBOOK",
        "accountType": "FBPAGE",
        "content": {
          "message": "the sky is clear 2014-11-24 05:45:18.563 ; Now http://on.fndgo.us/AutoLink20141124054509775",
          "attachment": {
            "type": "LINK",
            "mediaList": [
              {
                "type": "LINK",
                "imageUrl": "https://fbexternal-a.akamaihd.net/safe_image.php?d\u003dAQCVH_sOH0KNH2Az\u0026w\u003d158\u0026h\u003d158\u0026url\u003dhttps%3A%2F%2Fs.yimg.com%2Fdh%2Fap%2Fdefault%2F130909%2Fy_200_a.png",
                "previewImageUrl": "https://fbexternal-a.akamaihd.net/safe_image.php?d\u003dAQCVH_sOH0KNH2Az\u0026w\u003d158\u0026h\u003d158\u0026url\u003dhttps%3A%2F%2Fs.yimg.com%2Fdh%2Fap%2Fdefault%2F130909%2Fy_200_a.png",
                "title": "Yahoo India",
                "description": "A new welcome to Yahoo. The new Yahoo experience makes it easier to discover the news and information that you care about most. It\u0027s the web ordered for you.",
                "source": "http://on.fndgo.us/AutoLink20141124054509775"
              }
            ]
          },
          "languageCode": "en"
        },
        "taxonomy": {
          "campaignId": "186_3"
        },
        "approval": {
          "approvalOption": "NONE"
        },
        "status": "SENT",
        "createdDate": 1416798620000,
        "scheduleDate": 1416788197000,
        "version": 0,
        "deleted": false,
        "publishedDate": 1416788197000,
        "statusID": "328023460668217_526548187482409",
        "permalink": "https://www.facebook.com/permalink.php?story_fbid\u003d526548187482409\u0026id\u003d328023460668217",
        "additional": {
          "links": [
            "http://on.fndgo.us/AutoLink20141124054509775"
          ]
        }
      },
	      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      14.0
    ],
    [
      {
        "postId": 3951064,
        "messageId": 3951063,
        "accountId": 2616,
        "authorId": 2026,
        "clientId": 186,
        "messageType": 2,
        "channelType": "FACEBOOK",
        "accountType": "FBPAGE",
        "content": {
          "message": "back to work 2015-02-04 04:25:17.719 ; Now http://www.ndtv.com",
          "attachment": {
            "type": "LINK",
            "mediaList": [
              {
                "type": "LINK",
                "previewImageUrl": "http://cdn.ndtv.com/static/images/ndtv_default_image_500x500.jpg",
                "title": "NDTV.com",
                "description": "NDTV.com: India, Business, Bollywood, Cricket, Video and Breaking News",
                "source": "http://www.ndtv.com",
                "additional": {
                  "providerName": [
                    "www.ndtv.com"
                  ],
                  "thumbnails": [
                    "http://cdn.ndtv.com/static/images/ndtv_default_image_500x500.jpg",
                    "http://i.ndtvimg.com/video/images/vod/medium/2015-02/big_355412_1422981875.jpg",
                    "http://i.ndtvimg.com/video/images/vod/medium/2015-02/big_355409_1422979746.jpg",
                    "http://i.ndtvimg.com/video/images/vod/medium/2015-02/big_355438_1422997656.jpg",
                    "http://i.ndtvimg.com/video/images/vod/medium/2015-02/big_355290_1422944736.jpg"
                  ],
                  "currIndex": [
                    "0"
                  ],
                  "originalThumbs": [
                    null
                  ]
                }
              }
            ],
            "title": "NDTV.com",
            "description": "NDTV.com: India, Business, Bollywood, Cricket, Video and Breaking News"
          },
          "linkDetails": [
            {
              "link": "http://www.ndtv.com",
              "queryParams": {
              },
	             "originalLink": "http://r.sdg.me/6184nUlK",
              "twitterCardLink": false,
              "isShortLink": false,
              "redirectedLink": true,
              "domain": "www.ndtv.com"
            },
            {
              "link": "http://NDTV.com",
              "queryParams": {
              },
              "twitterCardLink": false,
              "isShortLink": false,
              "redirectedLink": false,
              "domain": "ndtv.com"
            },
            {
              "link": "http://www.ndtv.com/",
              "queryParams": {
              },
              "originalLink": "http://NDTV.com",
              "twitterCardLink": false,
              "isShortLink": false,
              "redirectedLink": true,
              "domain": "www.ndtv.com"
            },
            {
              "link": "http://www.ndtv.com/us",
              "queryParams": {
              },
              "originalLink": "http://r.sdg.me/6184nUlK",
              "twitterCardLink": false,
              "isShortLink": false,
              "redirectedLink": true,
              "domain": "www.ndtv.com"
            },
            {
              "link": "http://r.sdg.me/6184nUlK",
              "queryParams": {
              },
              "twitterCardLink": false,
              "isShortLink": false,
              "redirectedLink": false,
              "domain": "r.sdg.me"
            }
          ],
          "languageCode": "en"
        },
        "taxonomy": {
          "campaignId": "186_2",
          "clientCustomProperties": {
            "Automation_": [
              "0"
            ],
            "O_MULTI": [
              "50"
            ],
            "O_PICKLIST": [
              "6"
            ],
            "O_NUM": [
              "5"
            ]
          },
          "partnerCustomProperties": {
            "O_Automation_Field": [
              "Auto"
            ]
          },
          "tags": [
          ],
          "urlShortnerDomain": "54d151c3e4b0c6edef57733a"
        },
        "approval": {
          "approvalOption": "NONE",
          "comment": ""
        },
        "status": "SENT",
        "createdDate": 1423004200000,
        "scheduleDate": 1423004230000,
        "version": 2,
        "deleted": false,
        "publishedDate": 1423004231000,
        "statusID": "215244391952058_543445359131958",
        "permalink": "https://www.facebook.com/215244391952058/posts/543445359131958",
        "additional": {
          "links": [
            "http://www.ndtv.com"
          ]
        }
      },
      1.0,
      0.0,
      1.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      5.0
    ]
  ]
}





## Example 3: With Minified Post Object for twitter


### Example - Request





 Copy Code



curl -X POST \
   https://api3.sprinklr.com/{env}/api/v1/reports/query \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "endTime": 1423506350545,
  "groupBys": [
    {
      "groupType": "FIELD",
      "dimensionName": "POST_ID",
      "heading": "POST_ID"
    }
  ],
  "reportingEngine": "PLATFORM",
  "page": 0,
  "report": "POST_INSIGHTS",
  "pageSize": 2,
  "projections": [
    {
      "measurementName": "ENGAGEMENT_RATE",
      "aggregateFunction": "SUM",
      "heading": "ENGAGEMENT_RATE"
    },
    {
      "measurementName": "POST_LIKE_COUNT",
      "aggregateFunction": "SUM",
      "heading": "POST_LIKE_COUNT"
    },
    {
      "measurementName": "POST_SHARE_COUNT",
      "aggregateFunction": "SUM",
      "heading": "POST_SHARE_COUNT"
    },
    {
      "measurementName": "POST_REACH_COUNT",
      "aggregateFunction": "SUM",
      "heading": "POST_REACH_COUNT"
    },
    {
      "measurementName": "POST_COMMENT_COUNT",
      "aggregateFunction": "SUM",
      "heading": "POST_COMMENT_COUNT"
    },
    {
      "measurementName": "POST_CLICK_COUNT",
      "aggregateFunction": "SUM",
      "heading": "POST_CLICK_COUNT"
    },
    {
      "measurementName": "POST_REAL_CLICK_COUNT",
      "aggregateFunction": "SUM",
      "heading": "POST_REAL_CLICK_COUNT"
    },
    {
      "measurementName": "FOLLOWER_COUNT_AT_POST",
      "aggregateFunction": "SUM",
      "heading": "FOLLOWER_COUNT_AT_POST"
    },
    {
      "measurementName": "POST_CLICK_COUNT_WITH_REF_URL",
      "aggregateFunction": "SUM",
      "heading": "POST_CLICK_COUNT_WITH_REF_URL"
    },
    {
      "measurementName": "PUBLISHED_MESSAGE_COUNT",
      "aggregateFunction": "SUM",
      "heading": "PUBLISHED_MESSAGE_COUNT"
    },
    {
      "measurementName": "TOTAL_ENGAGEMENT",
      "aggregateFunction": "SUM",
      "heading": "TOTAL_ENGAGEMENT"
    },
    {
      "measurementName": "REACH_RATE",
      "aggregateFunction": "SUM",
      "heading": "REACH_RATE"
    }
  ],
  "timeZone": "Asia/Kolkata",
  "sorts": [
    {
      "order": "DESC",
      "heading": "POST_CLICK_COUNT"
    }
  ],
  "filters": [
    {
      "values": [
        "208",
        "287",
        "186"
      ],
      "filterType": "IN",
      "dimensionName": "CLIENT_ID"
    },
    {
      "values": [
          2612,2613,4202, 3988,3993
      ],
      "filterType": "IN",
      "dimensionName": "ACCOUNT_ID"
    }
  ]
}'





### Example - Response





{
  "apiStatus": "Removed fields because of resyndication policy",
  "headings": [
    "POST_ID",
    "ENGAGEMENT_RATE",
    "POST_LIKE_COUNT",
    "POST_SHARE_COUNT",
    "POST_REACH_COUNT",
    "POST_COMMENT_COUNT",
    "POST_CLICK_COUNT",
    "POST_REAL_CLICK_COUNT",
    "FOLLOWER_COUNT_AT_POST",
    "POST_CLICK_COUNT_WITH_REF_URL",
    "PUBLISHED_MESSAGE_COUNT",
    "TOTAL_ENGAGEMENT",
    "REACH_RATE"
  ],
  "rows": [
    [
      {
        "postId": 3906517,
        "messageId": 3906506,
        "accountId": 3988,
        "accountGroupId": "53314ef4e4b0fd1d8b9898ff",
        "authorId": 2026,
        "clientId": 186,
        "messageType": 2,
        "channelType": "TWITTER",
        "accountType": "TWITTER",
        "taxonomy": {
          "campaignId": "186_2",
          "clientCustomProperties": {
            "Automation_": [
              "0"
            ],
            "O_MULTI": [
              "50"
            ],
            "O_PICKLIST": [
              "6"
            ],
            "O_NUM": [
              "5"
            ]
          },
          "partnerCustomProperties": {
            "O_Automation_Field": [
              "Auto"
            ]
          },
          "tags": [
          ],
          "urlShortnerDomain": "5463d55ae4b02308f7da87f6"
        },
        "approval": {
          "approvalOption": "NONE"
        },
        "status": "SENT",
        "createdDate": 1421277153000,
        "scheduleDate": 1421277125000,
        "version": 0,
        "deleted": false,
        "publishedDate": 1421277154000,
        "statusID": "555502765196468225",
        "permalink": "https://twitter.com/ronald_hoo/status/555502765196468225",
        "additional": {
          "links": [
          ]
        }
      },
      -1,
      -1,
      -1,
      -1,
      -1,
      27.0,
      6.0,
      -1,
      0.0,
      -1,
      -1,
      -1
    ],
    [
      {
        "postId": 3913009,
        "messageId": 3913004,
        "accountId": 3988,
        "accountGroupId": "53314ef4e4b0fd1d8b9898ff",
        "authorId": 2026,
        "clientId": 186,
        "messageType": 2,
        "channelType": "TWITTER",
        "accountType": "TWITTER",
        "taxonomy": {
          "campaignId": "186_2",
          "clientCustomProperties": {
            "Automation_": [
              "0"
            ],
            "O_MULTI": [
              "50"
            ],
            "O_PICKLIST": [
              "6"
            ],
            "O_NUM": [
              "5"
            ]
          },
          "partnerCustomProperties": {
            "O_Automation_Field": [
              "Auto"
            ]
          },
          "tags": [
          ],
          "urlShortnerDomain": "5463d55ae4b02308f7da87f6"
        },
        "approval": {
          "approvalOption": "NONE"
        },
        "status": "SENT",
        "createdDate": 1421622451000,
        "scheduleDate": 1421622408000,
        "version": 0,
        "deleted": false,
        "publishedDate": 1421622452000,
        "statusID": "556951049479946240",
        "permalink": "https://twitter.com/ronald_hoo/status/556951049479946240",
        "additional": {
          "links": [
          ]
        }
      },
      -1,
      -1,
      -1,
      -1,
      -1,
      20.0,
      3.0,
      -1,
      0.0,
      -1,
      -1,
      -1
    ]
  ]
}





[](https://dev.sprinklr.com/post-insights-report-v1)




[Back to top](https://dev.sprinklr.com/post-insights-report-v1)
