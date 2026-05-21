---
title: "Create Saved Audience"
slug: create-saved-audience
url: https://dev.sprinklr.com/create-saved-audience
---

# Create Saved Audience

#  POST  Create Saved Audience

 Use the Create Saved Audience API to create Saved Audience Segments in Sprinklr from external systems. Saved audiences can be used for organic social campaigns on supported channels (Facebook and LinkedIn).

**Related Knowledge Base Article: [Saved Audience](https://www.sprinklr.com/help/articles/create-saved-audience/how-to-create-saved-audiences/63f783c19b334f7283b4da89) **

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/audience

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

## Request Body

































````






````````





      ****















| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Display name of the saved audience. |
| description | string | No | Description of the audience segment. |
| partnerCustomProperties | object | No | Partner-specific custom fields (key-value mapping). |
| channelTypes | array<string> | Yes | Target channel(s) for the saved audience.        Supported channels: FACEBOOK or LINKEDIN. |
| accountTypes | array<string> | No | Account type(s) for the audience.        Supported account types: FBPAGE, FBAdAccount, LINKEDIN,             LINKEDIN_AD_ACCOUNT |
| audienceType | string | Yes | Audience type. Use SAVED_AUDIENCE. Any other value returns validation error. |
| channelAudience | object | No | Channel-specific targeting configuration (for channel targeting). |
| attributes | object | No | Additional audience attributes. |

### channelAudience Object














      ``



| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| targetingValues | Map<string, List<TargetingOption>> | Yes | Keys must be valid AudienceTargetField enum values (e.g. GENDER, COUNTRY, AGE_RANGE, INTERESTS, CUSTOM_AUDIENCES). Invalid keys return validation error. Values are lists of targeting options. |

### `TargetingOption` Description




































| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Unique key for the targeting option. |
| label | string | No | Display label for the option. |
| additional | Map<string,string> | No | Extra properties for the option. |
| parentTargetingValues | Map<string, ParentTargetingValue> | No | Defines parent-level targeting criteria. The key represents the targeting field name, and the value specifies the corresponding parent targeting configuration. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/audience' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {API_KEY}'\
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "name": "Shivi Test",
    "description": "Doc test Description",
    "partnerCustomProperties": {
        "_c_61d69e1dfe907519211aadcc": [
            "Email"
        ],
        "_c_65d5bf8fbfa1973eaf812837": [
            "88"
        ],
        "_c_6512721b83353e6f3e80c1c5": [
            "test1"
        ]
    },
    "channelTypes": [
        "FACEBOOK"
    ],
    "accountTypes": [
        "FBPAGE"
    ],
    "audienceType": "SAVED_AUDIENCE",
    "channelAudience": {
        "targetingValues": {
            "MIN_AGE": [
                {
                    "key": "13",
                    "label": "13"
                }
            ],
            "MAX_AGE": [
                {
                    "key": "50",
                    "label": "50"
                }
            ],
            "INTERESTS": [
                {
                    "key": "6005609368513",
                    "label": "Software"
                },
                {
                    "key": "6003380970205",
                    "label": "Software engineering"
                },
                {
                    "key": "6003433461774",
                    "label": "Software design pattern"
                }
            ],
            "GENDER": [
                {
                    "key": 1,
                    "label": "Male"
                }
            ],
            "REGION": [
                {
                    "key": "1728",
                    "label": "Delhi, India"
                },
                {
                    "key": "1730",
                    "label": "Haryana, India"
                }
            ],
            "CITY": [
                {
                    "key": "2678292",
                    "label": "Noida, India"
                }
            ],
            "COUNTRY": [
                {
                    "key": "IN",
                    "label": "India"
                }
            ],
            "RELATIONSHIP_STATUS": [
                {
                    "key": 1,
                    "label": "Single"
                }
            ],
            "INTERESTED_IN": [
                {
                    "key": 2,
                    "label": "Female"
                }
            ],
            "LOCALES": [
                {
                    "key": 6,
                    "label": "English (US)"
                },
                {
                    "key": 46,
                    "label": "Hindi"
                }
            ],
            "EDUCATION_STATUS": [
                {
                    "key": 3,
                    "label": "College Grad"
                }
            ]
        }
    },
    "attributes": {
        "isOrganic": true
    }
}'

## Example - Response


{
    "data": {
        "id": "69ca1ca30067c932d4c41033",
        "name": "Shivi Test",
        "description": "Doc test Description",
        "audienceType": "SAVED_AUDIENCE",
        "channelTypes": [
            "FACEBOOK"
        ],
        "accountTypes": [
            "FBPAGE"
        ],
        "channelAudience": {
            "targetingValues": {
                "EDUCATION_STATUS": [
                    {
                        "key": "3",
                        "label": "College Grad"
                    }
                ],
                "RELATIONSHIP_STATUS": [
                    {
                        "key": "1",
                        "label": "Single"
                    }
                ],
                "INTERESTED_IN": [
                    {
                        "key": "2",
                        "label": "Female"
                    }
                ],
                "COUNTRY": [
                    {
                        "key": "IN",
                        "label": "India"
                    }
                ],
                "INTERESTS": [
                    {
                        "key": "6003380970205",
                        "label": "Software engineering"
                    },
                    {
                        "key": "6003433461774",
                        "label": "Software design pattern"
                    },
                    {
                        "key": "6005609368513",
                        "label": "Software"
                    }
                ],
                "CITY": [
                    {
                        "key": "2678292",
                        "label": "Noida, India"
                    }
                ],
                "GENDER": [
                    {
                        "key": "1",
                        "label": "Male"
                    }
                ],
                "MIN_AGE": [
                    {
                        "key": "13",
                        "label": "13"
                    }
                ],
                "MAX_AGE": [
                    {
                        "key": "50",
                        "label": "50"
                    }
                ],
                "LOCALES": [
                    {
                        "key": "46",
                        "label": "Hindi"
                    },
                    {
                        "key": "6",
                        "label": "English (US)"
                    }
                ],
                "REGION": [
                    {
                        "key": "1728",
                        "label": "Delhi, India"
                    },
                    {
                        "key": "1730",
                        "label": "Haryana, India"
                    }
                ]
            }
        },
        "partnerCustomProperties": {
            "_c_61d69e1dfe907519211aadcc": [
                "Email"
            ],
            "_c_65d5bf8fbfa1973eaf812837": [
                "88"
            ],
            "_c_6512721b83353e6f3e80c1c5": [
                "test1"
            ]
        },
        "createdTime": 1774853283341,
        "modifiedTime": 1774853283342,
        "attributes": {
            "isOrganic": "true"
        }
    },
    "errors": []
}

## Response Schema






































      ****



















































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | object | This is the primary container in the API response that encapsulates the payload returned by the API. |
|  | id | string | Unique identifier of the saved audience. |
|  | name | string | Name of the saved audience. |
|  | description | string | Description of the saved audience. |
|  | audienceType | string | Type of audience. For saved audiences, the value is SAVED_AUDIENCE. |
|  | channelTypes | array<string> | Social channels on which the audience can be used (for example, FACEBOOK). |
|  | accountTypes | array<string> | Account types associated with the channel (for example, FBPAGE). |
|  | channelAudience | object | Channel-specific targeting configuration for the audience. |
|  | partnerCustomProperties | map<string, array<string>> | Partner-defined custom properties associated with the audience.         Each key maps to one or more values. |
|  | createdTime | number (long) | Time when the audience was created, in epoch milliseconds. |
|  | modifiedTime | number (long) | Time when the audience was last modified, in epoch milliseconds. |
|  | attributes | object | Additional metadata associated with the audience. |
| errors |  | array | List of errors (if any). |

[](https://dev.sprinklr.com/create-saved-audience)

[Back to top](https://dev.sprinklr.com/create-saved-audience)
