---
title: "Search Survey Response"
slug: search-survey-response
url: https://dev.sprinklr.com/search-survey-response
---

# Search Survey Response

#
  POST Search Survey Response

This API allows you to search a survey response for a specific survey.


**Dev Notes: **To use this API, you will need values for the parameters mentioned below. To obtain these values, reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/survey-response/survey/`{survey-id}`/search

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

### Path Parameters



















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| {survey-id} | Required | String | Unique identifier of the survey. |


### Request Parameters

























****

-
-
-







****
- ****
- ****

****























****


























| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| filters |  | Required | Defines the conditions used to search survey responses. Each filter specifies a field, the type of filter, the values to match, and any additional details required to apply the filter correctly. | Array |
|  | field | Required | The type of field to apply the filter on.Supported Values:   SURVEY_CUSTOM_PROPERTY   TRANSACTIONS_CUSTOM_PROPERTY   PROFILE_CUSTOM_PROPERTY | String |
|  | filterType | Required | Type of filter to apply.Supported Filter Types:   Text Value: IN, NIN, EQUALS, NOT_EQUALS   Date Value: LT, LTE, GT, GTE   See the Filter Type table below for descriptions. | String |
|  | values | Required | List of values to match against. | Array |
|  | details | Required | Specifies the custom field value. | Object |
|  | details.fieldName | Required | Specifies the ID of the custom field being filtered. See Steps to Copy Field Name given below. | String |
| page |  | Optional | An object that controls pagination of the search results. | Number |
|  | start | Optional | The index of the first result to return for the current page. | Number |
|  | size | Optional | Number of results to return per page. | Number |

**Steps to Retrieve Survey and Transaction Custom Field Name from the Sprinklr UI**


- Open the **Customer Feedback Management (CFM)** persona app in Sprinklr.

- Navigate to the **Programs** tab and locate the survey for which you want to access custom fields.

- Hover over the survey to reveal the **View** button.

- Click **View** to open the survey details.

- From the top navigation bar, click **Settings**.

- Scroll to the **Survey Custom Fields** section. This section includes two options:


  - **Transaction Fields**

  - **Response Custom Fields**



- Click the **View Fields** button next to **Transaction Fields** if you're looking for transaction-related custom fields, or next to **Response Custom Fields** if you're looking for response-related custom fields.

- This opens a list of all the custom fields under the selected category.

- Find the specific field you're interested in. Click the three-dot menu (**⋮**) next to it.

- Select **Copy Field Name** to copy the internal field ID, which is used in API requests.


### Filter Types - Description

















      ****









      ****




      ****




      ****




      ****




      ****



| Search Value Type | Filter Type | Description |
| --- | --- | --- |
| Text | IN | Returns resources where the key matches any of the values mentioned in the list of values. |
| Text | NIN | Returns resources where the key does not match any of the values mentioned in the list of values. |
| Text | EQUALS | Returns resources where the key is equal to the value mentioned. |
| Text | NOT_EQUALS | Returns resources where the key is not equal to the value mentioned. |
| Date | GT (Greater Than) | Returns resources where the key is greater than the specified value. |
| Date | GTE (Greater Than or Equal To) | Returns resources where the key is greater than or equal to the specified value. |
| Date | LT (Less Than) | Returns resources where the key is less than the specified value. |
| Date | LTE (Less Than or Equal To) | Returns resources where the key is less than or equal to the specified value. |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/survey-response/survey/689349d8659af54b3dfe74c5/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: {Enter Your Access Token}' \
--data '{
    "filters": [
        {
            "field": "SURVEY_CUSTOM_PROPERTY",
            "filterType": "IN",
            "values": [
                "5"
            ],
            "details": {
                "fieldName": "_c_67cb50793cae6f06c0c41de0"
            }
        }
    ],
    "page": {
        "start":0
        "size": 10
    }
}'



## Example - Response




{
    "data": {
        "hasMore": false,
        "responses": [
            {
                "surveyId": "689349d8659af54b3dfe74c5",
                "responseId": "689ac8b558fcc0135712ea3e",
                "responseStatus": "COMPLETE_RESPONSES",
                "createdTime": 1754906674000,
                "surveyLanguage": "en",
                "surveyMode": "STANDARD",
                "surveyResponseType": "STANDARD",
                "responderSnId": "689ac8b558fcc0135712ea3d",
                "responderSnType": "EXTERNAL_APPLICATION",
                "responseQuality": "NA",
                "questionResponses": {
                    "689349d8659af54b3dfe74e9": [
                        "4.0"
                    ],
                    "689349d9659af54b3dfe74ef": [
                        "Via API again"
                    ],
                    "689349d8659af54b3dfe74dd": [
                        "No"
                    ]
                },
                "customProperties": {
                    "_c_67cb50793cae6f06c0c41de0": [
                        "5"
                    ]
                },
                "profileCustomProperties": {
                    "_c_64cbf526fd8b0e259d72470a": [
                        "20"
                    ]
                },
                "transactionCustomProperties": {
                    "_c_685e452216e5014e48fea656": [
                        "1730970932000"
                    ]
                }
            }
        ],
        "metadata": {
            "customFieldLookup": {
                "_c_685e452216e5014e48fea656": "test date1",
                "_c_64cbf526fd8b0e259d72470a": "profile rule debugging cf",
                "_c_67cb50793cae6f06c0c41de0": "num cf"
            },
            "questionLookup": {
                "689349d8659af54b3dfe74e9": "Based on your experience, how likely are you to recommend [ACME Mart] to your friends and family?",
                "689349d9659af54b3dfe74ef": "Please share any other feedback about your experience with us.",
                "689349d8659af54b3dfe74dd": "Would you like to answer a few more questions about your experience? It will take only 2-3 minutes."
            }
        }
    },
    "errors": []
}





## Response Parameters


### Data


























****






****




| Parent Parameter | Sub-parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Root object containing survey responses and metadata | Object |
|  | hasMore | Indicates if more responses are available | Boolean |
|  | responses | Array of individual survey responsesSee the Responses table below | Array |
|  | metadata | Metadata describing questions and custom fieldsSee the Metadata table below | Object |

### Responses






















****















****








































****





****
- ****
- ****
























| Parameter | Description | Type |
| --- | --- | --- |
| surveyId | Unique identifier for the survey | String |
| responseId | Unique identifier for the specific response | String |
| responseStatus | Indicates the status of the response. Expected Values: COMPLETE_RESPONSES, ARCHIVED_RESPONSES, IMPORTED_RESPONSES, LIVE_RESPONSES, TEST_RESPONSES | String |
| createdTime | Timestamp when the response was created (epoch milliseconds) | Number |
| surveyLanguage | Language in which the survey was taken | String |
| surveyMode | Mode of the survey. Expected Values: STANDARD, CONVERSATIONAL | String |
| surveyResponseType | Type of the survey response (for example, STANDARD) | String |
| distributionEntityId | ID of the distribution entity | String |
| responderSnId | ID of the responder | String |
| responderSnType | Type of responder (for example, EXTERNAL_APPLICATION) | String |
| browser | Browser used by the respondent | String |
| browserVersion | Version of the browser | String |
| operatingSystem | Operating system of the responder | String |
| deviceType | Type of device used. Expected Values: COMPUTER, MOBILE, TABLET, GAME_CONSOLE, DMR, WEARABLE, UNKNOWN | String |
| responseQuality | AI-generated quality assessment of the response. Expected Values : N/A, High, Bot, Low, Medium    NA means quality assessment has not been generated yet   Bot means the system flags it as a bot response | String |
| questionResponses | Object mapping question IDs to answers | Object |
| customProperties | Additional custom metadata for the response | Object |
| profileCustomProperties | Custom profile metadata for the responder | Object |
| transactionCustomProperties | Transactional metadata associated with the response | Object |

### Metadata





















| Parameter | Description | Type |
| --- | --- | --- |
| customFieldLookup | Mapping of custom field IDs to their display names | Object |
| questionLookup | Mapping of question IDs to question text | Object |


  [](https://dev.sprinklr.com/search-survey-response)




[Back to top](https://dev.sprinklr.com/search-survey-response)
