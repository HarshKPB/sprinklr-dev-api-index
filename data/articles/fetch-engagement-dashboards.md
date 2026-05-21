---
title: "Fetch Engagement Dashboards"
slug: fetch-engagement-dashboards
url: https://dev.sprinklr.com/fetch-engagement-dashboards
---

# Fetch Engagement Dashboards

#
  GET Fetch Engagement Dashboards




Using this API, you can fetch all the existing engagement dashboards available in the partner environment/workspace.

**Use Cases:**

- Fetch the names and column ids of all the engagement dashboards available in the Sprinklr environment

- Fetch column Ids, which then can be used in stream read API

- Fetch up-to-date information on all the engagement dashboards existing in the environment

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/monitoring/dashboard

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

	**Note:** This API will only fetch the engagement dashboards that are accessible to the user with whom the authorization token is associated.

## Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/monitoring/dashboard' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}'






## Example - Response





{
            "id": "657beaee15c40a1c3deb805a",
            "name": "DS2K Twitter",
            "shareConfigs": [
                {
                    "type": "PERSONA_APP",
                    "ids": [
                        "SOCIAL_PLANNING_AND_PUBLISHING_CLONE_5"
                    ]
                },
                {
                    "type": "GLOBAL"
                }
            ],
            "columnOrder": [
                "66421b5e4dd96877ecf3456b"
            ],
            "columns": [
                {
                    "id": "66421b5e4dd96877ecf3456b",
                    "name": "my posts",
                    "dashboardId": "657beaee15c40a1c3deb805a",
                    "channel": "TWITTER",
                    "type": "MY_TWEETS",
                    "properties": {
                        "SORT_ENABLED": [
                            "true"
                        ],
                        "ACCOUNT": [
                            "66000936",
                            "600037525",
                            "66013027",
                            "66005497",
                            "66001308"
                        ],
                        "SOURCE_ID": [
                            "66000936",
                            "600037525",
                            "66013027",
                            "66005497",
                            "66001308"
                        ],
                        "SHOW_COUNT": [
                            "true"
                        ],
                        "CATEGORY": [
                            "2",
                            "13",
                            "11",
                            "12",
                            "3"
                        ],
                        "POST_TYPE": [
                            "true"
                        ],
                        "TIME_RANGE_FILTER_KEY": [
                            "LIFETIME"
                        ],
                        "SEARCH_ENABLED": [
                            "true"
                        ],
                        "SPONSORED_POST_TYPE": [
                            "all"
                        ],
                        "QUOTED_RETWEET_TYPE": [
                            "all"
                        ],
                        "PROMOTED_POST_TYPE": [
                            "all"
                        ]
                    },
                    "clientCustomProperties": {},
                    "partnerCustomProperties": {},
                    "upfrontFilterKeys": [],
                    "sourceType": "ACCOUNT",
                    "clientQueues": [],
                    "partnerQueues": [],
                    "sortField": "snCreatedTime",
                    "columnColor": "#ccc",
                    "autoRender": true,
                    "locked": false,
                    "order": 0.0,
                    "versionId": 0
                }
            ],
            "tags": [],
            "locked": false,
            "shared": false
        }
    ],
    "errors": []
}







[](https://dev.sprinklr.com/fetch-engagement-dashboards)




[Back to top](https://dev.sprinklr.com/fetch-engagement-dashboards)
