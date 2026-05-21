---
title: "Import Survey Response"
slug: import-survey-response
url: https://dev.sprinklr.com/import-survey-response
---

# Import Survey Response

#
  POST Import Survey Response

This API enables you to import survey responses from any external source into Sprinklr CFM.

**Dev Notes: **To use this API, you will need values for the parameters mentioned below. To obtain these values, reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/survey-response/survey/`{survey-id}`

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


### Request Body






















****












****
-
-
-
-
-
-
-
-
-

































| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| questionResponses | Required | Object | A map of question IDs to an array of response values. |
| responseTime | Required | String | Timestamp indicating when the response was recorded. Format: YYYY-MM-DD HH:mm:ss |
| tags | Optional | Array | An array of tags associated with the response. |
| distributionChannel | Required | String | The source of the response.Supported Values:    QR_CODE   EXTERNAL_APPLICATION   WEBSITE   EMAIL   SMS   WHATSAPP_BUSINESS   IN_APP   SOCIAL   PERSONALISED_LINK |
| customFields | Optional | Object | Custom metadata fields with dynamic keys and values. |
| responderSnId | Optional | String | Identifier for the responder (if available). |
| responderSnType | Optional | String | Type of responder ID (if applicable). |
| surveyLanguage | Optional | String | Language in which the survey was answered. |
| elapsedTime | Optional | String | Time taken to complete the survey. |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/qa6/api/v2/survey-response/survey/68b7c75b46cb0008f47d8508' \
--header 'Content-Type: application/json' \
--header 'Authorization: {Enter Your Access Token}' \
--data '{
    "questionResponses": {
        "68b7c75b46cb0008f47d8526": [
            "9"
        ],
        "68b7c75b46cb0008f47d852c": [
            "Response Text"
        ],
        "68b7c75b46cb0008f47d851a": [
            "Yes"
        ],
        "68b7c75b46cb0008f47d8529": [
            "9"
        ],
        "68b7c75b46cb0008f47d8523_68b7c75b46cb0008f47d850e": [
            "5"
        ],
        "68b7c75b46cb0008f47d8523_68b7c75b46cb0008f47d850b": [
            "5"
        ],
        "68b7c75b46cb0008f47d8523_68b7c75b46cb0008f47d8514": [
            "5"
        ],
        "68b7c75b46cb0008f47d8523_68b7c75b46cb0008f47d8517": [
            "5"
        ],
        "68b7c75b46cb0008f47d8523_68b7c75b46cb0008f47d8511": [
            "5"
        ],
        "68b7c75b46cb0008f47d851d": [
            "Yes"
        ],
        "68b7c75b46cb0008f47d8520": [
            "Email"
        ],
        "68b7c75b46cb0008f47d852f": [
            "Response Text"
        ],
        "68b7c75b46cb0008f47d8532": [
            "Response Text"
        ]
    },
    "responseTime": 1738281600000,
    "tags": [
        "tag1"
    ],
    "distributionChannel": "EXTERNAL_APPLICATION",
    "responseCustomFields": {},
    "profileCustomFields": {},
    "transactionCustomFields": {},
    "responderSnId": null,
    "responderSnType": null,
    "surveyLanguage": null,
    "elapsedTime": null,
    "allCustomFields": {}
}'



## Example - Response




{
    "data": "68b82250ea9c8863e4942650",
    "errors": []
}





  [](https://dev.sprinklr.com/import-survey-response)




[Back to top](https://dev.sprinklr.com/import-survey-response)
