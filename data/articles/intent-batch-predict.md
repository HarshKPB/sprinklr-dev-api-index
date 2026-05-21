---
title: "Intent Batch Predict"
slug: intent-batch-predict
url: https://dev.sprinklr.com/intent-batch-predict
---

# Intent Batch Predict

#
  POST Intent Batch Predict


	The Intent Batch Predict API is capable of identifying issue types in a list of messages and this helps in routing the messages or cases according to the identified intent. Using this API, you can make a prediction request on a list of messages

**Note: ** Please reach out to your Success Manager or Sprinklr support to get Intuition API's enabled for your environment.

   **Use Case: **



- Once intent modeling occurs then intents can be utilized across a variety of message types to identify the purpose behind the message. Once the intent is captured it is then it is leveraged to inform Unified Insights, Skills Based Routing, Community Crowdsourcing, Smart Responses, etc.

- The intents can be trained to be very granular if sufficient data is available. For an example of intents trained for Brand not only identify that a message references a battery issue but more specifically a battery bulging issue.


## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/intuition/intent/batch-predict

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






























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| engineKey | Required | The engine type. | String |
| text | Required | Message text on which you want to perform the analysis. | String |
| language | Required | Language of the message. | String |

## Example - Request















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/intent/batch-predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '[
  "text": "string",
  "language": "string",
  "engineKey": "string"
]'






## Example - Response





{
    "data":[
{
  "input": {
    "text": "string",
    "language": "string",
    "engineKey": "string"
  },
  "response": [
    {
      "type": "string",
      "classDetails": [
        {
          "label": "string",
          "confidence": 0
        }
      ],
      "insights": [
        {
          "name": "string",
          "start": 0,
          "end": 0,
          "phrase": "string",
          "confidence": 0
        }
      ]
    }
  ]
}
],
 "errors": []
}







## Response Parameters








































































| Parameters | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| type |  | Insight type. | String |
| classDetails |  | Describes the schema of category class details. | Object |
|  | label | The detected category. | String |
|  | confidence | Confidence of the prediction, value ranges between 0-1. | Double |
| insights |  | Describes the schema for phrase detected. | Object |
|  | name | Name of the category detected phrase belongs to. | String |
|  | start | Starting position of the detected phrase in passed text. | Integer |
|  | end | Ending position of the detected phrase in passed text. | Integer |
|  | phrase | Detected phrase. | String |
|  | confidence | Confidence of the prediction, value ranges between 0-1. | Double |

[](https://dev.sprinklr.com/intent-batch-predict)




[Back to top](https://dev.sprinklr.com/intent-batch-predict)
