---
title: "Search User (SCIM)"
slug: search-user-scim
url: https://dev.sprinklr.com/search-user-scim
---

# Search User (SCIM)

#  GET  Search User (SCIM)



Using this API, you can search user by passing filters and sorting details

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/Users

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``




| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/scim+json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Query Parameters



****

-
-
-
-

****

****

****

****

****

****

- `****`
-

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sortBy | Optional | Refers to the field you want to sort the results with.Supported Values:idnamemeta.createdTimemeta.lastModified | String |
| startIndex | Optional | Refers to the row from which you want to fetch the results. For example, there are 10 results and you specify startIndex as 2, the API would return 9 users.Default: 1 and non-positive value of startIndex would also default to 1 | Integer |
| count | Optional | Refers to the number of results you want to fetch in the response.Default::100Note:: Non-positive value of count will result in empty response | Integer |
| sortOrder | Optional | Refers to the order in which you want the results.Supported Values: ascending, descendingDefault: ascending | String |
| filter | Optional | Refers to the filters you want to apply to the user search.Notes:The filters can only be combined by "and" operator. Any other operator will throw an error.Filters supporting "eq" can support multiple eq statements like id eq "a" and id eq "b" and id eq "c", etc.Refer to the table below for supported filters | String |

## Supported Filter Types and Operations












``````

``

****``
``````

| Filter Type | Description | Supported Operations | Type |
| --- | --- | --- | --- |
| id | Refers to the user Id associated with the user | eq (equal to), le (larger than), ge (greater than) | Integer |
| userName | Refers to the name of the user | eq (equal to) | String |
| meta.lastModified | Refers to the last time the user was modified.Format: yyyy-MM-ddTHH:mm:ssZ | eq (equal to), le (larger than), ge (greater than) | String |

**Syntax Examples for Filter Field:**

- **With id and meta.lastModified:**`id le "1000052905" and meta.lastModified le "2023-07-05T06:16:48Z`
- **With User Ids:**`id eq "1" and id eq "2" and id eq "3"`
- **With meta.lastModified:**`meta.lastModified le "2023-07-05T06:16:48Z" and meta.lastModified ge "2023-05-05T06:16:48Z"`

## Example 1: Sample Request



 Copy Code


curl -X GET \
  'https://api3.sprinklr.com/{{env}}/api/v2/scim/Users?startIndex=1&count=2&sortBy=id&sortOrder=descending&filter=id ge "1" and meta.lastModified le "2023-07-05T06:16:48Z' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: Content-Type: application/scim+json' \
  -H 'key: {apikey}'



## Example - Response




{
    "schemes": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
            ],
            "id": "1",
            "userName": "test.1+test@sprinklr.com",
            "name": {
                "familyName": "1",
                "givenName": "test"
            },
            "photos": [
                {
                    "value": "https://qa4-sprcdn-assets.sprinklr.com/400002/a1ff0e18-a58e-45ea-a354-19ff1aa4df76-924555875/Headline_0_2022-01-12_17_06_58_p.jpg"
                }
            ],
            "active": true,
            "locale": "EN_US",
            "globalAttributes": {
                "federationId": "febId12",
                "passwordLoginDisabled": false
            },
            "clientAttributes": [
                {
                    "clientId": 2,
                    "userType": "PARTNER_USER",
                    "phoneNumbers": [
                        {
                            "value": "9880393854"
                        }
                    ],
                    "businessCategory": "CORPORATE",
                    "primaryUserGroupId": "621883eb0ba544387d2d5b24",
                    "userGroupIds": [
                        "642185c6f63bee0f15b3333f"
                    ],
                    "designation": "Test update desg"
                }
            ],
            "meta": {
                "resourceType": "User",
                "createdTime": "2019-04-09 10:43:38.0",
                "lastModified": "2023-07-18 08:16:33"
            },
            "emails": [
                {
                    "value": "user.1+test@sprinklr.com",
                    "primary": true
                }
            ]
        },
        {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
            ],
            "id": "2",
            "userName": "user.2+test@sprinklr.com",
            "name": {
                "familyName": "2",
                "givenName": "User"
            },
            "photos": [
                {
                    "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
                }
            ],
            "active": false,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {
                    "_c_6153242d7d77c36c5118cf89": [
                        "2"
                    ],
                    "_c_61b046970928a269c83ab2a0": [
                        "2"
                    ]
                },
                "passwordLoginDisabled": false
            },
            "clientAttributes": [
                {
                    "clientId": 5,
                    "userType": "CLIENT_USER",
                    "phoneNumbers": [
                        {}
                    ],
                    "businessCategory": "CORPORATE",
                    "userGroupIds": [
                        "5f88574ad61f971e1496c23d"
                    ]
                }
            ],
            "meta": {
                "resourceType": "User",
                "createdTime": "2023-02-10 22:00:00.0",
                "lastModified": "2023-07-18 08:15:19"
            },
            "emails": [
                {
                    "value": "user.2+test@sprinklr.com",
                    "primary": true
                }
            ]
        }
    ],
    "totalResults": 4114,
    "startIndex": 1,
    "itemsPerPage": 2
}

## Example 2: Sample Request



 Copy Code


curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/scim/Users?startIndex=1&count=3&sortBy=id&sortOrder=descending&filter=id eq "1" and id eq "2" and id eq "3" ' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: Content-Type: application/scim+json' \
  -H 'key: {apikey}'



## Example - Response




{
    "schemes": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
            ],
            "id": "1",
            "userName": "test.1+test@sprinklr.com",
            "name": {
                "familyName": "1",
                "givenName": "test"
            },
            "photos": [
                {
                    "value": "https://qa4-sprcdn-assets.sprinklr.com/400002/a1ff0e18-a58e-45ea-a354-19ff1aa4df76-924555875/Headline_0_2022-01-12_17_06_58_p.jpg"
                }
            ],
            "active": true,
            "locale": "EN_US",
            "globalAttributes": {
                "federationId": "febId12",
                "passwordLoginDisabled": false
            },
            "clientAttributes": [
                {
                    "clientId": 2,
                    "userType": "PARTNER_USER",
                    "phoneNumbers": [
                        {
                            "value": "9880393854"
                        }
                    ],
                    "businessCategory": "CORPORATE",
                    "primaryUserGroupId": "621883eb0ba544387d2d5b24",
                    "userGroupIds": [
                        "642185c6f63bee0f15b3333f"
                    ],
                    "designation": "Test update desg"
                }
            ],
            "meta": {
                "resourceType": "User",
                "createdTime": "2019-04-09 10:43:38.0",
                "lastModified": "2023-07-18 08:16:33"
            },
            "emails": [
                {
                    "value": "user.1+test@sprinklr.com",
                    "primary": true
                }
            ]
        },
        {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
            ],
            "id": "2",
            "userName": "user.2+test@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User2"
            },
            "photos": [
                {
                    "value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
                }
            ],
            "active": false,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {
                    "_c_6153242d7d77c36c5118cf89": [
                        "2"
                    ],
                    "_c_61b046970928a269c83ab2a0": [
                        "2"
                    ]
                },
                "passwordLoginDisabled": false
            },
            "clientAttributes": [
                {
                    "clientId": 5,
                    "userType": "CLIENT_USER",
                    "phoneNumbers": [
                        {}
                    ],
                    "businessCategory": "CORPORATE",
                    "userGroupIds": [
                        "5f88574ad61f971e1496c23d"
                    ]
                }
            ],
            "meta": {
                "resourceType": "User",
                "createdTime": "2023-02-10 22:00:00.0",
                "lastModified": "2023-07-18 08:15:19"
            },
            "emails": [
                {
                    "value": "user.2+test@sprinklr.com",
                    "primary": true
                }
            ]
        },
        {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
                "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
            ],
            "id": "3",
            "userName": "user.3+test@sprinklr.com",
            "name": {
                "familyName": "Test",
                "givenName": "User3"
            },
            "photos": [
                {
                    "value": "https://qa4-cdata-app.sprinklr.com/DAM/400002/c7a45625-cce3-4f28-98d8-9d802015a16a-1897976821/https___qa4-3m-dam-tier1.sprin_p.jpg"
                }
            ],
            "active": true,
            "locale": "EN_US",
            "globalAttributes": {
                "partnerCustomProperties": {
                    "_c_61926a395f0ec315174a39fe": [
                        "All Users"
                    ]
                },
                "federationId": "#85091",
                "passwordLoginDisabled": false
            },
            "clientAttributes": [
                {
                    "clientId": 2,
                    "userType": "PARTNER_ADMIN",
                    "phoneNumbers": [
                        {
                            "value": "916234562314"
                        }
                    ],
                    "businessCategory": "CORPORATE",
                    "primaryUserGroupId": "621883eb0ba544387d2d5b24",
                    "userGroupIds": [],
                    "clientCustomProperties": {
                        "_c_6192831d5f0ec315174a7750": [
                            "4"
                        ]
                    },
                    "designation": "QA Lead",
                    "department": "QA"
                }
            ],
            "meta": {
                "resourceType": "User",
                "createdTime": "2018-09-11 07:54:49.0",
                "lastModified": "2023-07-24 11:14:32"
            },
            "emails": [
                {
                    "value": "user.3+test@sprinklr.com",
                    "primary": true
                }
            ]
        }
    ],
    "totalResults": 3,
    "startIndex": 1,
    "itemsPerPage": 3
}

## Example 3: Sample Request



 Copy Code


curl -X GET \
  'https://api2.sprinklr.com/{{env}}/api/v2/scim/Users?startIndex=1&count=1&sortBy=id&sortOrder=descending&filter=meta.lastModified le "2023-07-05T06:16:48Z" and meta.lastModified ge "2023-05-05T06:16:48Z"' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: Content-Type: application/scim+json' \
  -H 'key: {apikey}'



## Example - Response




{
	"schemes": [
		"urn:ietf:params:scim:api:messages:2.0:ListResponse"
	],
	"Resources": [
		{
			"schemas": [
				"urn:ietf:params:scim:schemas:core:2.0:User",
				"urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
				"urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
				"urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
				"urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User"
			],
			"id": "4",
			"userName": "user.4+test@sprinklr.com",
			"name": {
				"familyName": "Test",
				"givenName": "User4"
			},
			"photos": [
				{
					"value": "https://sprcdn-assets.sprinklr.com/787/profile-15ea76bd-9f28-47a3-83e7-dff01011834e-176564324.png"
				}
			],
			"active": false,
			"locale": "EN_US",
			"globalAttributes": {
				"partnerCustomProperties": {
					"_c_61b337f95680c31e7cef1ff5": [
						"Sprinklr Employee"
					]
				},
				"passwordLoginDisabled": false
			},
			"clientAttributes": [
				{
					"clientId": 2,
					"userType": "PARTNER_ADMIN",
					"phoneNumbers": [
						{}
					],
					"businessCategory": "CORPORATE",
					"userGroupIds": [
					],
					"clientCustomProperties": {
						"_c_6192831d5f0ec315174a7750": [
							"4"
						]
					}
				},
				{
					"clientId": 34,
					"userType": "CLIENT_USER",
					"phoneNumbers": [
						{}
					],
					"businessCategory": "CORPORATE"
				}
			],
			"meta": {
				"resourceType": "User",
				"createdTime": "2018-10-08 05:31:59.0",
				"lastModified": "2023-07-18 08:15:12"
			},
			"emails": [
				{
					"value": "user.4+test@sprinklr.com",
					"primary": true
				}
			]
		}
	],
	"totalResults": 343,
	"startIndex": 1,
	"itemsPerPage": 1
}

[](https://dev.sprinklr.com/search-user-scim) 

 

 
[Back to top](https://dev.sprinklr.com/search-user-scim)
