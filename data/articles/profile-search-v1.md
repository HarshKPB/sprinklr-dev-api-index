---
title: "Profile Search v1"
slug: profile-search-v1
url: https://dev.sprinklr.com/profile-search-v1
---

# Profile Search v1

#
  POST - Profile Search

You can search for profile details with this API call. In response, you will get all the details of profile in json format.

## API Endpoint

https://api3.sprinklr.com`/{path}/`api/v1/profile/search


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

## Request Parameters















```

```







```

```








```

```








```

```







```

```







```

```







```

```







```

```







```

```




| Parameter | Type | Description | Required / Optional |
| --- | --- | --- | --- |
| filters | Map < Enum, List < String > > | List of profile types: Probably should break into a different page: 				"SN_TYPE": Social Network 				"PROFILE_LIST": Sprinklr Client Profile List ID 				"PARTNER_PROFILE_LIST": Sprinklr Partner Profile List ID 				"TAGS": Tags associated with profile in Sprinklr 				Example: 				"filters": { 	"SN_TYPE": ["INSTAGRAM"], 	"PROFILE_LIST": [2, 4],         "TAGS": ["france"] } | Required |
| sortInfo | List < Object > | You can sort based on any attribute of the profile object, the parameters are either "ASC" or "DESC" 				Example: 				"sortInfo": { 	"CREATED_TIME": "DESC", } | Optional |
| clientCustomProperties | Map < Enum, List < String > > | Search for profile with certain Client level custom properties. The key to each property is the numerical custom property id. 				Example: 				"clientCustomProperties": {         "5516cf616687eb42b1000000": ["Male"] } | Optional |
| partnerCustomProperties | Map < Enum, List < String > > | Search for profile with certain Partner level custom properties. The key to each property is the numerical custom property id. 				Example: 				"partnerCustomProperties": {         "5516cf616687eb42b1000000": ["Male"] } | Optional |
| snTypeVsSnIds | Search Object | You can search a profile using snType and snId. 				Example: 				"snTypeVsSnIds": {     "FACEBOOK": [       1053541818117227     ]   } | Optional |
| since | Object | You can set a time bound based on time-related properties in the profile, e.g. created time, modified time. 				Example: 				"since": { 	"CREATED_TIME": 1483228800000 } | Optional |
| until | Object | You can set a time bound based on time-related properties in the profile, e.g. created time, modified time. 				Example: 				"until": { 	"CREATED_TIME": 1483228800000 } | Optional |
| start | Integer | The start offset 				Start offset example: "A" as an array of characters containing "abcdef", the fourth element containing the character "D" has an offset of three from the start of "A". 				Default = 0 				Example: 				"start": 0 | Optional |
| rows | Integer | The number of rows (profiles) to fetch from the start offset 				Default = 20 rows (profiles) 				Example: 				"rows": 3 | Optional |


## Example - Request





 Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v1/profile/search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
	"filters":{
		"SN_TYPE": ["FACEBOOK"],
		"PROFILE_LIST": [1],
		"PARTNER_PROFILE_LIST": [2],
		"TAGS": ["france"]
	},
	"sortInfo":{
		"CREATED_TIME":"DESC"
	},
	"clientCustomProperties":{
	},
	"partnerCustomProperties": {
	   "5516cf616687eb42b1000000": ["Male"]
	},
	"since":{
		"CREATED_TIME": 1430160163000
	},
	"until":{
		"CREATED_TIME": 1430160164000
	},
	"start":0,
	"rows":100
}'





## Example - Response




{
  "start": 0,
  "totalFound": 1,
  "profiles": [
    {
      "id": "553e8323e4b08aba446cc934",
      "contactInfo": {
        "firstName": "Jacob",
        "lastName": "Anthony",
        "fullName": "Jacob Anthony"
      },
      "demographics": {
        "gender": "male",
        "language": "en_US"
      },
      "socialProfiles": [
        {
          "name": "Jacob Anthony",
          "type": "FACEBOOK",
          "snId": "100005318647352",
          "username": "Jacob Anthony",
          "bio": "",
          "following": 18,
          "followers": 0,
          "favCount": 0,
          "reach": 0,
          "statusCount": 0,
          "url": "https://www.facebook.com/app_scoped_user_id/100005318647352/",
          "profileImageUrl": "https://scontent.xx.fbcdn.net/v/t1.0-1/c16.16.194.194/s50x50/522620_104953299691958_1265691187_n.jpg?oh=66d42df087b8e8b9d8bd8c7ed6d2031f&oe=5989F955",
          "snCreatedTime": 0,
          "snModifiedTime": 1493865401367,
          "snStats": {
            "spamCount": 0,
            "messageCount": 31,
            "nonSpamCount": 31
          },
          "verified": false,
          "additional": {
            "appId": [
              "443975059026016"
            ],
            "pType": [
              "USER"
            ]
          }
        }
      ],
      "socialScoreCard": {
        "participationIndex": 100,
        "influencerIndex": 0,
        "spamIndex": 0
      },
      "profileWorkflowProperties": {
        "tags": [],
        "comments": [],
        "notifyUserIds": [],
        "partnerProfileLists": [
          1,
          2
        ],
        "clientProfileLists": [
          2,
          1
        ],
        "partnerCustomProperties": {
          "563ce415913fb41e61000000": [
            ""
          ],
          "5516cf616687eb42b1000000": [
            "Male"
          ]
        },
        "clientCustomProperties": {
          "5515eca06687eb6f94000000": [
            ""
          ]
        },
        "spaceCustomProperties": {},
        "userCustomProperties": {},
        "clientTags": [
          "marlboro",
          "france"
        ]
      },
      "snCreatedTime": 0,
      "snModifiedTime": 1493865401367,
      "createdTime": 1430160163909,
      "modifiedTime": 1493865401367,
      "accountsFollowedByUser": [],
      "accountsFollowingUser": [],
      "accountsUnFollowingUser": [],
      "accountsUnFollowedByUser": [],
      "accountsBlockingUser": [],
      "engagedAccountIds": [],
      "additional": {}
    }
  ],
  "facets": [
    {
      "facetField": {
        "id": "SN_TYPE",
        "displayName": "Social Network",
        "fieldType": "FILTER",
        "rangeFacet": false,
        "priority": 100
      },
      "values": [
        {
          "name": "FACEBOOK",
          "count": 1,
          "selected": true
        }
      ]
    },
    {
      "facetField": {
        "id": "PROFILE_LIST",
        "displayName": "Client Profile list",
        "fieldType": "FILTER",
        "rangeFacet": false,
        "priority": 99
      },
      "values": [
        {
          "name": "1",
          "count": 1,
          "selected": true
        },
        {
          "name": "2",
          "count": 1,
          "selected": false
        }
      ]
    },
    {
      "facetField": {
        "id": "PARTNER_PROFILE_LIST",
        "displayName": "Partner Profile list",
        "fieldType": "FILTER",
        "rangeFacet": false,
        "priority": 98
      },
      "values": [
        {
          "name": "1",
          "count": 1,
          "selected": false
        },
        {
          "name": "2",
          "count": 1,
          "selected": true
        }
      ]
    },
    {
      "facetField": {
        "id": "TAGS",
        "displayName": "Tags",
        "fieldType": "FILTER",
        "rangeFacet": false,
        "priority": 97
      },
      "values": [
        {
          "name": "france",
          "count": 1,
          "selected": true
        },
        {
          "name": "marlboro",
          "count": 1,
          "selected": false
        }
      ]
    },
    {
      "facetField": {
        "id": "5516cf616687eb42b1000000",
        "displayName": "ProfileInfo",
        "fieldType": "PARTNER_CUSTOM_FIELD",
        "rangeFacet": false,
        "priority": 2
      },
      "values": [
        {
          "name": "Male",
          "count": 1,
          "selected": true
        }
      ]
    }
  ]
}





## Response Parameters











































































































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the profile in Sprinklr. | String |
| contactInfo |  | The object containing contant information. | Object |
|  | fullName | The full name of the profile. | String |
| demographics |  | The object containing profile demographic information. | Object |
|  | gender | The gender of the profile | String |
| socialProfiles |  | The object containing native profile information. | Object |
|  | name | The name displayed in the profile. | String |
|  | type | The type of profile based on social network. e.g. FACEBOOK | String |
|  | snId | The social network Id of the profile from native. | Long |
|  | snIdWithSnType | The social network Id and social netwok for the profile. | String |
|  | username | The profile username. | String |
|  | following | The following count. | Integer |
|  | followers | The followers count. | Integer |
|  | favCount | The favourite count. | Integer |
|  | reach | The reach of the profile. | Integer |
|  | statusCount | The status count. | Integer |
|  | url | The profile url. | String |
|  | snCreatedTime | The profile created time. | Long |
|  | snModifiedTime | The profile modified time. | Long |
|  | snStats | The object containing social netwok stats. | Object |
| socialScoreCard |  | The Object contaning score card information of the profile. | String |
|  | participationIndex | The participation index of the profile. | Integer |
|  | influencerIndex | The influencer index of the profile. | Integer |
|  | spamIndex | The spam index of the profile. | Integer |
| profileWorkflowProperties |  | The profile workflow properties within Sprinklr. | Object |
| accountsFollowedByUser |  | The account followed by user. | Object |
| accountsFollowingUser |  | The account following user. | Object |
| accountsUnFollowingUser |  | The account unfollowing user. | Object |
| accountsUnFollowedByUser |  | The account unfollowed by user. | Object |
| accountsBlockingUser |  | The account blocking user. | Object |
| accountsSuspendingUser |  | The account suspending user. | Object |
| engagedAccountIds |  | The engaged account Ids. | Object |

[](https://dev.sprinklr.com/profile-search-v1)




[Back to top](https://dev.sprinklr.com/profile-search-v1)
