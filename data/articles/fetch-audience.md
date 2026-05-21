---
title: "Fetch Audience"
slug: fetch-audience
url: https://dev.sprinklr.com/fetch-audience
---

# Fetch Audience

#  GET  Fetch Audience

 Use the Fetch Audience API to get the details of Audience Segments in Sprinklr from external systems.

**Related Knowledge Base Article: [Audience in Sprinklr](https://www.sprinklr.com/help/categories/audience/63eddb85fbb4dd3e50d47ebf) **

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/audience?id={audience_id}

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

## Query Parameter


















| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Unique identifier of the audience. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/qa6/api/v2/audience?id=69d68a20c92a526a87b51a02' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'

## Example - Response


{
    "data": {
        "id": "69d758232183518349c5abde",
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
                "RELATIONSHIP_STATUS": [
                    {
                        "key": "1",
                        "label": "Single"
                    }
                ],
                "EDUCATION_STATUS": [
                    {
                        "key": "3",
                        "label": "College Grad"
                    }
                ],
                "INTERESTED_IN": [
                    {
                        "key": "2",
                        "label": "Female"
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
                "COUNTRY": [
                    {
                        "key": "IN",
                        "label": "India"
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
                        "key": "13"
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
        "createdTime": 1775720483216,
        "modifiedTime": 1775720484109,
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

[](https://dev.sprinklr.com/fetch-audience)

[Back to top](https://dev.sprinklr.com/fetch-audience)
