---
title: "Users Widget"
slug: v1-users-widget
url: https://dev.sprinklr.com/v1-users-widget
---

# Users Widget

# POST Users Widget

For the USERS Widget, populating the secondary widgetType via `subType` is required.

**Dev Notes: **Currently supported subType values are:


`TOP_ADVOCATES`, `TOP_DETRACTORS`, `TOP_PROLIFIC_USERS`, `USERS_BY_KLOUT_SCORE`

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/listening/query/widget

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

### Top Advocates

This returns the daily volume of mentions grouped by Topic.

 Copy Code


curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/listening/query/widget' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "sinceTime": 1488034511000,
    "untilTime": 1490972111000,
    "details": {
        "widgetType": "USERS",
        "subType": "TOP_ADVOCATES"
    },
    "filters": [
        {
            "dimension": "TOPIC",
            "filterValues": [
                "595c50dbe4b064e21f85d074"
            ]
        }
    ],
    "metric": "MENTIONS"
}'

### Example - Response

{
    "status": "SUCCESS",
    "response": [
        {
            "id": "5ae09f8ce4b02190134c124c",
            "contactInfo": {
            },
            "demographics": {
            },
            "socialProfiles": [
                {
                    "type": "WEB",
                    "snId": "15035f4b45263b2a9cd02c2be024ed9c",
                    "following": 0,
                    "followers": 0,
                    "favCount": 0,
                    "reach": 0,
                    "statusCount": 0,
                    "snCreatedTime": 1524670227457,
                    "snModifiedTime": 1524670227457,
                    "verified": false,
                    "additional": {
                    },
                    "deleted": false
                }
            ],
            "socialScoreCard": {
                "participationIndex": 0,
                "influencerIndex": 0,
                "spamIndex": 0
            },
            "profileWorkflowProperties": {
                "tags": [
                ],
                "comments": [
                ],
                "notifyUserIds": [
                ],
                "partnerProfileLists": [
                ],
                "clientProfileLists": [
                ],
                "partnerCustomProperties": {
                },
                "clientCustomProperties": {
                },
                "spaceCustomProperties": {
                },
                "userCustomProperties": {
                },
                "clientTags": [
                ]
            },
            "snCreatedTime": 0,
            "snModifiedTime": 0,
            "createdTime": 1524670348489,
            "modifiedTime": 1524670348489,
            "accountsFollowedByUser": [
            ],
            "accountsFollowingUser": [
            ],
            "accountsUnFollowingUser": [
            ],
            "accountsUnFollowedByUser": [
            ],
            "accountsBlockingUser": [
            ],
            "accountsSuspendingUser": [
            ],
            "engagedAccountIds": [
            ],
            "additional": {
            },
            "exactMatch": true,
            "positivePosts": 2
        },
        {
            "id": "5875da71e4b005e7ffdd46b1",
            "contactInfo": {
                "fullName": "Mydex CIC"
            },
            "demographics": {
                "location": "London"
            },
            "socialProfiles": [
                {
                    "name": "Mydex CIC",
                    "type": "TWITTER",
                    "snId": "130563149",
                    "username": "MydexCIC",
                    "bio": "A person-centred, live and certified platform for personal data, consent and identity management. The tools for transparent, safe and streamlined data flow.",
                    "following": 665,
                    "followers": 1255,
                    "favCount": 114,
                    "reach": 0,
                    "statusCount": 3984,
                    "url": "http://www.twitter.com/MydexCIC",
                    "profileImageUrl": "https://pbs.twimg.com/profile_images/618379733617766400/cEr0oa30_normal.png",
                    "largeProfileImageUrl": "https://pbs.twimg.com/profile_images/618379733617766400/cEr0oa30.png",
                    "snCreatedTime": 1270660644000,
                    "snModifiedTime": 1270660644000,
                    "verified": false,
                    "additional": {
                    },
                    "deleted": false
                }
            ],
            "socialScoreCard": {
                "participationIndex": 0,
                "influencerIndex": 54,
                "spamIndex": 0
            },
            "profileWorkflowProperties": {
                "tags": [
                ],
                "comments": [
                ],
                "notifyUserIds": [
                ],
                "partnerProfileLists": [
                ],
                "clientProfileLists": [
                ],
                "partnerCustomProperties": {
                },
                "clientCustomProperties": {
                },
                "spaceCustomProperties": {
                },
                "userCustomProperties": {
                },
                "clientTags": [
                ]
            },
            "snCreatedTime": 0,
            "snModifiedTime": 1270660644000,
            "createdTime": 1484118641789,
            "modifiedTime": 1504620955547,
            "accountsFollowedByUser": [
            ],
            "accountsFollowingUser": [
            ],
            "accountsUnFollowingUser": [
            ],
            "accountsUnFollowedByUser": [
            ],
            "accountsBlockingUser": [
            ],
            "accountsSuspendingUser": [
            ],
            "engagedAccountIds": [
            ],
            "additional": {
                "LST_INFLUENCER_SCORE_UPDATED": [
                    "1496220068157"
                ]
            },
            "exactMatch": true,
            "positivePosts": 1
        },
        {
            "id": "5875db59e4b0c3bd6f84dd4b",
            "contactInfo": {
                "fullName": "Andrew Fowkes"
            },
            "demographics": {
                "location": "United Kingdom",
                "gender": "M",
                "language": "en",
                "additional": {
                    "LOCATION_DETAILS": "United Kingdom"
                }
            },
            "socialProfiles": [
                {
                    "name": "Andrew Fowkes",
                    "type": "TWITTER",
                    "snId": "153327541",
                    "username": "andrewfowkes",
                    "bio": "Passionate about helping #Retail get smart through #analytics, working with #SAS - ideas are my own !",
                    "following": 94,
                    "followers": 74,
                    "favCount": 92,
                    "reach": 0,
                    "statusCount": 847,
                    "url": "https://twitter.com/andrewfowkes",
                    "profileImageUrl": "http://pbs.twimg.com/profile_images/950327939488468992/N5lh87NR_normal.jpg",
                    "largeProfileImageUrl": "http://pbs.twimg.com/profile_images/950327939488468992/N5lh87NR.jpg",
                    "snCreatedTime": 1275982655000,
                    "snModifiedTime": 1275982655000,
                    "verified": false,
                    "additional": {
                    },
                    "deleted": false
                }
            ],
            "socialScoreCard": {
                "participationIndex": 0,
                "influencerIndex": 37,
                "spamIndex": 0
            },
            "profileWorkflowProperties": {
                "tags": [
                ],
                "comments": [
                ],
                "notifyUserIds": [
                ],
                "partnerProfileLists": [
                ],
                "clientProfileLists": [
                ],
                "partnerCustomProperties": {
                },
                "clientCustomProperties": {
                },
                "spaceCustomProperties": {
                },
                "userCustomProperties": {
                },
                "clientTags": [
                ]
            },
            "snCreatedTime": 0,
            "snModifiedTime": 1275982655000,
            "createdTime": 1484118873093,
            "modifiedTime": 1545214434844,
            "accountsFollowedByUser": [
            ],
            "accountsFollowingUser": [
            ],
            "accountsUnFollowingUser": [
            ],
            "accountsUnFollowedByUser": [
            ],
            "accountsBlockingUser": [
            ],
            "accountsSuspendingUser": [
            ],
            "engagedAccountIds": [
            ],
            "additional": {
                "LST_INFLUENCER_SCORE_UPDATED": [
                    "1544698871995"
                ]
            },
            "exactMatch": true,
            "positivePosts": 1
        }
    ]
}



[](https://dev.sprinklr.com/v1-users-widget) 

 

 
[Back to top](https://dev.sprinklr.com/v1-users-widget)
