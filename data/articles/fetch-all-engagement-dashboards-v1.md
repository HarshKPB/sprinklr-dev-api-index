---
title: "Fetch All Engagement Dashboards v1"
slug: fetch-all-engagement-dashboards-v1
url: https://dev.sprinklr.com/fetch-all-engagement-dashboards-v1
---

# Fetch All Engagement Dashboards v1

#
  GET Fetch All Engagement Dashboards



Using this API, you can fetch all the existing Monitoring Dashboards along their columns and respective IDs.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/dashboards

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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


	**Note:**
- If you cannot see all of the dashboards that you need, make sure that the Authenticated Sprinklr User has permission to see the dashboard in the Sprinklr UI.
- You can use this endpoint to find the stream id & the stream name.

## Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/dashboards' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}'






## Example - Response





      [

{
"id":"5c7bdaf7e4b03d655cf612ca",
"name":"Social Channel Inbox",
"shareConfigs":[
{
"shareLevel":"CLIENT",
"sharedWithIds":[

        ]
     },
     {
        "shareLevel":"CLIENT_GROUP",
        "sharedWithIds":[

        ]
     },
     {
        "shareLevel":"USER",
        "sharedWithIds":[
           "185370",
           "188984",
           "189145"
        ]
     },
     {
        "shareLevel":"USER_GROUP",
        "sharedWithIds":[

        ]
     }
  ],
  "columnOrder":[
     "5c7c8914e4b0b25907ef1937",
     "5c7c8930e4b0b25907ef1bb5",
     "5c7e76c6e4b03d655d46a739",
     "5cbf8089e4b0704c5cdf2c03"
  ],
  "columns":[
     {
        "id":"5c7c8914e4b0b25907ef1937",
        "dashboardId":"5c7bdaf7e4b03d655cf612ca",
        "channel":"TWITTER",
        "type":"RECEIVED_DIRECT_MESSAGES",
        "tags":[

        ],
        "properties":{
           "SORT_ENABLED":[
              "true"
           ],
           "ACCOUNT":[
              "255156"
           ],
           "SOURCE_ID":[
              "255156"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "CATEGORY":[
              "5"
           ],
           "POST_TYPE":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{
           "5bd6c0c6e4b03983d42572d1":[
              "English"
           ]
        },
 "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[

        ],
        "sortField":{
           "fieldName":"snCreatedTime",
           "displayName":"Created Time",
           "inboundMessageFilterKey":"snCreatedTime",
           "order":"DESC"
        },
        "name":"Facebook Inbox",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "ownerUserId":185370,
        "createdTime":"2019-03-04 02:10:56",
        "modifiedTime":"2019-03-04 02:22:37",
        "deleted":false
     },
     {
        "id":"5c7e76c6e4b03d655d46a739",
        "dashboardId":"5c7bdaf7e4b03d655cf612ca",
        "channel":"FACEBOOK",
        "type":"SHARES",
        "tags":[

        ],
        "properties":{
           "SORT_ENABLED":[
              "true"
           ],
           "ACCOUNT":[
              "257708"
           ],
           "SOURCE_ID":[
              "257708"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "CATEGORY":[
              "227"
           ],
           "POST_TYPE":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[

        ],
        "sortField":{
           "fieldName":"snCreatedTime",
           "displayName":"Created Time",
           "inboundMessageFilterKey":"snCreatedTime",
           "order":"DESC"
        },
        "name":"Shared posts",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "ownerUserId":196648,
        "createdTime":"2019-03-05 13:16:54",
        "modifiedTime":"2019-03-05 13:16:54",
        "deleted":false
     },
     {
        "id":"5cbf8089e4b0704c5cdf2c03",
        "dashboardId":"5c7bdaf7e4b03d655cf612ca",
        "channel":"TWITTER",
        "type":"CHANNEL_SEARCH",
        "tags":[

        ],
        "properties":{
           "LANGUAGE":[
              "en"
           ],
           "SORT_ENABLED":[
              "false"
           ],
           "ACCOUNT":[
              "255156"
           ],
           "SOURCE_ID":[
              "-1"
           ],
           "QUERY":[
              "ubisoft"
           ],
           "SHOW_COUNT":[
              "false"
           ],
           "SEARCH_ENABLED":[
              "false"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"PERSISTENT_SEARCH",
        "clientQueues":[

        ],
        "partnerQueues":[

        ],
        "sortField":{
           "fieldName":"snCreatedTime",
           "displayName":"Created Time",
           "inboundMessageFilterKey":"snCreatedTime",
           "order":"DESC"
        },
        "name":"Twitter search",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "ownerUserId":189145,
        "createdTime":"2019-04-23 21:15:53",
        "modifiedTime":"2019-04-23 21:15:53",
        "deleted":false
     }
  ],
  "tags":[

  ],
  "locked":false,
  "shared":false

},
{
"id":"5ce55d2fe4b0b370325bbd29",
"name":"AG_Inbound",
"shareConfigs":[
{
"shareLevel":"GLOBAL"
}
],
"columnOrder":[
"5ce55d2fe4b0b370325bbd2c",
"5ce55d2fe4b0b370325bbd2f",
"5ce55d2fe4b0b370325bbd32",
"5ce55d2fe4b0b370325bbd35",
"5ce55d2fe4b0b370325bbd38",
"5ce55d2fe4b0b370325bbd3b",
"5ce55d2fe4b0b370325bbd3e",
"5ce55d2fe4b0b370325bbd41",
"5ce55d6ce4b0b370325bd217"
],
"columns":[
{
"id":"5ce55d2fe4b0b370325bbd2c",
"dashboardId":"5ce55d2fe4b0b370325bbd29",
"channel":"WORKFLOW",
"type":"ASSIGNED_TO_ME",
"tags":[

        ],
        "properties":{
           "OUTBOUND_SORT_BY":[
              "assignedToTime"
           ],
           "SORT_ENABLED":[
              "true"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "ASSIGNED_TO_ME":[
              "assigned_to_me"
           ],
           "POST_TYPE":[
              "all"
           ],
           "SORT_ORDER":[
              "desc"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "DELETED":[
              "all"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[

        ],
        "sortField":{
           "fieldName":"assignedToTime",
           "order":"DESC"
        },
        "name":"Assigned to Me",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"30",
           "refreshTimeUnit":"s"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d2fe4b0b370325bbd2f",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"WORKFLOW",
        "type":"ENHANCED_PARTNER_QUEUES",
        "tags":[

        ],
        "properties":{
           "OUTBOUND_SORT_BY":[
              "snCreatedTime"
           ],
           "WITH_BRAND_COMMENTS":[
              "all"
           ],
           "AUTO_RESPONSE":[
              "all"
           ],
           "POST_TYPE":[
              "all"
           ],
           "DELETED":[
              "all"
           ],
           "SORT_ENABLED":[
              "true"
           ],
           "SHOW_ONLY_UNASSIGNED":[
              "all"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "CATEGORY":[
              "14",
              "15",
              "97"
           ],
           "AUTO_RESPONDED":[
              "all"
           ],
           "SORT_ORDER":[
              "asc"
           ],
           "IS_PARENT_BRAND_POST":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
"partnerQueues":[
           2,
           13
        ],
        "sortField":{
           "fieldName":"partnerQueueAssignedTime",
           "order":"DESC"
        },
        "refreshTime":1,
        "name":"Facebook Public",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"1"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d2fe4b0b370325bbd32",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"WORKFLOW",
        "type":"ENHANCED_PARTNER_QUEUES",
        "tags":[

        ],
        "properties":{
           "OUTBOUND_SORT_BY":[
              "snCreatedTime"
           ],
           "WITH_BRAND_COMMENTS":[
              "all"
           ],
           "AUTO_RESPONSE":[
              "all"
           ],
           "POST_TYPE":[
              "all"
           ],
           "DELETED":[
              "all"
           ],
           "SORT_ENABLED":[
              "true"
           ],
           "SHOW_ONLY_UNASSIGNED":[
              "all"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "CATEGORY":[
              "38"
           ],
           "AUTO_RESPONDED":[
              "all"
           ],
           "SORT_ORDER":[
              "asc"
           ],
           "IS_PARENT_BRAND_POST":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[
           2,
           13
        ],
        "sortField":{
           "fieldName":"partnerQueueAssignedTime",
           "order":"DESC"
        },
        "refreshTime":1,
        "name":"Facebook Messenger",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"1"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d2fe4b0b370325bbd35",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"WORKFLOW",
        "type":"ENHANCED_PARTNER_QUEUES",
        "tags":[

        ],
        "properties":{
           "OUTBOUND_SORT_BY":[
              "snCreatedTime"
           ],
           "WITH_BRAND_COMMENTS":[
              "all"
           ],
           "AUTO_RESPONSE":[
              "all"
           ],
           "POST_TYPE":[
              "all"
           ],
           "DELETED":[
              "all"
           ],
           "SORT_ENABLED":[
              "true"
           ],
           "SHOW_ONLY_UNASSIGNED":[
              "all"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "CATEGORY":[
              "4",
              "7"
           ],
           "AUTO_RESPONDED":[
              "all"
           ],
           "SORT_ORDER":[
              "asc"
           ],
           "IS_PARENT_BRAND_POST":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[
           2,
           13
        ],
        "sortField":{
           "fieldName":"partnerQueueAssignedTime",
           "order":"DESC"
        },
        "refreshTime":1,
        "name":"Twitter Public",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"1"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d2fe4b0b370325bbd38",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"WORKFLOW",
        "type":"ENHANCED_PARTNER_QUEUES",
        "tags":[

        ],
        "properties":{
           "OUTBOUND_SORT_BY":[
              "snCreatedTime"
           ],
           "WITH_BRAND_COMMENTS":[
              "all"
           ],
           "AUTO_RESPONSE":[
              "all"
           ],
           "POST_TYPE":[
              "all"
           ],
           "DELETED":[
              "all"
           ],
           "SORT_ENABLED":[
              "true"
           ],
"SHOW_ONLY_UNASSIGNED":[
              "all"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "CATEGORY":[
              "5"
           ],
           "AUTO_RESPONDED":[
              "all"
           ],
           "SORT_ORDER":[
              "asc"
           ],
           "IS_PARENT_BRAND_POST":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[
           2,
           13
        ],
        "sortField":{
           "fieldName":"partnerQueueAssignedTime",
           "order":"DESC"
        },
        "refreshTime":1,
        "name":"Twitter DMs",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"1"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d2fe4b0b370325bbd3b",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"WORKFLOW",
        "type":"ENHANCED_PARTNER_QUEUES",
        "tags":[

        ],
        "properties":{
           "OUTBOUND_SORT_BY":[
              "snCreatedTime"
           ],
           "WITH_BRAND_COMMENTS":[
              "all"
           ],
           "AUTO_RESPONSE":[
              "all"
           ],
           "POST_TYPE":[
              "all"
           ],
           "DELETED":[
              "all"
           ],
           "SORT_ENABLED":[
              "true"
           ],
           "SHOW_ONLY_UNASSIGNED":[
              "all"
           ],
           "CATEGORY":[
              "44",
              "88",
              "37",
              "137",
              "70",
              "42",
              "307",
              "316"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "AUTO_RESPONDED":[
              "all"
           ],
           "IS_PARENT_BRAND_POST":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[
           13
        ],
        "sortField":{
           "fieldName":"partnerQueueAssignedTime",
           "inboundMessageFilterKey":"snCreatedTime",
           "order":"DESC"
        },
 "refreshTime":1,
        "name":"Other",
        "description":"Instagram, YouTube, Google+, LinkedIn, Pinterest",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"1"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d2fe4b0b370325bbd3e",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"WORKFLOW",
        "type":"ENHANCED_PARTNER_QUEUES",
        "tags":[

        ],
        "properties":{
           "OUTBOUND_SORT_BY":[
              "partnerQueueAssignedTime"
           ],
           "WITH_BRAND_COMMENTS":[
              "all"
           ],
           "AUTO_RESPONSE":[
              "all"
           ],
           "POST_TYPE":[
              "all"
           ],
           "DELETED":[
              "all"
           ],
           "SORT_ENABLED":[
              "true"
           ],
           "SHOW_ONLY_UNASSIGNED":[
              "all"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "AUTO_RESPONDED":[
              "all"
           ],
           "SORT_ORDER":[
              "desc"
           ],
           "IS_PARENT_BRAND_POST":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[
           1,
           20
        ],
        "sortField":{
           "fieldName":"partnerQueueAssignedTime",
           "order":"DESC"
        },
        "refreshTime":1,
        "name":"Closed",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"1"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d2fe4b0b370325bbd41",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"WORKFLOW",
        "type":"ENHANCED_PARTNER_QUEUES",
        "tags":[

        ],
"properties":{
           "OUTBOUND_SORT_BY":[
              "partnerQueueAssignedTime"
           ],
           "WITH_BRAND_COMMENTS":[
              "all"
           ],
           "AUTO_RESPONSE":[
              "all"
           ],
           "POST_TYPE":[
              "all"
           ],
           "DELETED":[
              "all"
           ],
           "SORT_ENABLED":[
              "true"
           ],
           "SHOW_ONLY_UNASSIGNED":[
              "all"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "AUTO_RESPONDED":[
              "all"
           ],
           "SORT_ORDER":[
              "desc"
           ],
           "IS_PARENT_BRAND_POST":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "WITH_LIKED_POSTS":[
              "all"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[
           8,
           21
        ],
        "sortField":{
           "fieldName":"partnerQueueAssignedTime",
           "order":"DESC"
        },
        "refreshTime":1,
        "name":"No Response",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "additional":{
           "refreshTime":"1"
        },
        "ownerUserId":188981,
        "deleted":false
     },
     {
        "id":"5ce55d6ce4b0b370325bd217",
        "dashboardId":"5ce55d2fe4b0b370325bbd29",
        "channel":"FACEBOOK",
        "type":"FB_INSTA_AD_COMMENT",
        "tags":[

        ],
        "properties":{
           "SORT_ENABLED":[
              "true"
           ],
           "ACCOUNT":[
              "257859"
           ],
           "SOURCE_ID":[
              "257859"
           ],
           "CATEGORY":[
              "197"
           ],
           "SHOW_COUNT":[
              "true"
           ],
           "POST_TYPE":[
              "all"
           ],
           "TIME_RANGE_FILTER_KEY":[
              "LIFETIME"
           ],
           "SEARCH_ENABLED":[
              "true"
           ]
        },
        "clientCustomProperties":{

        },
        "partnerCustomProperties":{

        },
        "spaceCustomProperties":{

        },
        "userCustomProperties":{

        },
        "profileClientCustomProperties":{

        },
        "profilePartnerCustomProperties":{

        },
        "channelCustomProperties":{

        },
        "sourceType":"ACCOUNT",
        "clientQueues":[

        ],
        "partnerQueues":[

        ],
        "sortField":{
           "fieldName":"snCreatedTime",
           "displayName":"Created Time",
           "inboundMessageFilterKey":"snCreatedTime",
           "order":"DESC"
        },
        "name":"Instagram Paid Comments",
        "columnColor":"#ccc",
        "autoRender":true,
        "locked":false,
        "ownerUserId":188981,
        "createdTime":"2019-05-22 14:32:12",
        "modifiedTime":"2019-05-22 14:32:12",
        "deleted":false
     }
  ],
  "tags":[

  ],
  "locked":false,
  "shared":true

}
]







	[](https://dev.sprinklr.com/fetch-all-engagement-dashboards-v1)






[Back to top](https://dev.sprinklr.com/fetch-all-engagement-dashboards-v1)
