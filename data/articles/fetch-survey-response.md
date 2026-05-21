---
title: "Fetch Survey Response"
slug: fetch-survey-response
url: https://dev.sprinklr.com/fetch-survey-response
---

# Fetch Survey Response

#
  GET Fetch Survey Response

This API allows you to retrieve detailed information about a specific survey response using its unique ID.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/survey-response/`{survey-response-id}`

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
| {survey-response-id} | Required | String | Unique identifier of the survey response. |



**Steps to Retrieve Survey Response Id from Sprinklr UI**


- Open Customer Feedback Management (CFM) persona app in Sprinklr.

- In the **Programs** tab, locate the survey of which you want to fetch the responses.

- Hover over the survey. A **View** button is displayed.

- Click **View**.

- On the top bar, click **Responses**.

The **Response Id** column values correspond to `survey-response-id`.

## Example - Request




 Copy Code


curl --location --request GET 'https://api3.sprinklr.com/{env}/api/v2/survey-response/68b6bd55ccda6f5475acf933' \
--header 'Authorization: Bearer {Enter Your Access Token}'



## Example - Response




{
    "data": {
        "hasMore": false,
        "responses": [
            {
                "surveyId": "688c8ef57b0c1b5aaaa6e0e7",
                "responseId": "68b6bd55ccda6f5475acf933",
                "responseStatus": "COMPLETE_RESPONSES",
                "createdTime": 1756806486060,
                "surveyLanguage": "en",
                "surveyMode": "STANDARD",
                "surveyResponseType": "STANDARD",
                "responderSnId": "68b6bd55ccda6f5475acf932",
                "responderSnType": "EXTERNAL_APPLICATION",
                "responseQuality": "NA",
                "questionResponses": {
                    "c958057e-19a4-4b6a-b935-98ad750a1a93_778dcad1-c9f3-4ee9-adaa-394aa96c4382": [
                        "Neutral"
                    ]
                },
                "customProperties": {},
                "profileCustomProperties": {},
                "transactionCustomProperties": {}
            }
        ],
        "metadata": {
            "customFieldLookup": {},
            "questionLookup": {
                "c958057e-19a4-4b6a-b935-98ad750a1a93_778dcad1-c9f3-4ee9-adaa-394aa96c4382": "Question - Statement Item 1"
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


  [](https://dev.sprinklr.com/fetch-survey-response)




[Back to top](https://dev.sprinklr.com/fetch-survey-response)
