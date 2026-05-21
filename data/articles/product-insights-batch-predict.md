---
title: "Product Insights Batch Predict"
slug: product-insights-batch-predict
url: https://dev.sprinklr.com/product-insights-batch-predict
---

# Product Insights Batch Predict

#
  POST  Product Insights Batch Predict


The Product Insights Batch Predict API is capable of identifying common trends within unstructured data to apply structure and drive analysis based on modeling structure of respective business. Using this API, you can make a prediction request on a list of messages.

**Note: ** Please reach out to your Success Manager or Sprinklr support to get Intuition API's enabled for your environment.

   **Use Case: **



- Insights can be leveraged for any unstructured data; flat text files (Clavis data), social data, online surveys, voice transcripts etc. These insights can be unified for analysis. Examples of deployment include Sentiment Analysis, CX insights, Product Insights, Verticalised Insights and Competitor Insights.

- Ability to identify common trends within unstructured data to apply structure and drive analysis.



## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/intuition/product-insights/batch-predict

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generatio)



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
'https://api3.sprinklr.com`/{env}/`api/v2/intuition/product-insights/batch-predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '[
  {
    "text": "string",
    "language": "string",
    "engineKey": "string"
  }
]'






## Example - Response





{
    "data": [
  {
    "input": {
      "text": "string",
      "language": "string",
      "engineKey": "string"
    },
    "response": [
      {
        "sentiment": {
          "name": "string",
          "start": 0,
          "end": 0,
          "phrase": "string",
          "confidence": 0
        },
        "category": {
          "name": "string",
          "start": 0,
          "end": 0,
          "phrase": "string",
          "confidence": 0,
          "l1": "string",
          "l2": "string",
          "l3": "string"
        },
        "brand": {
          "name": "string",
          "start": 0,
          "end": 0,
          "phrase": "string",
          "confidence": 0
        }
      }
    ]
  }
],
"errors": []
}







## Response Parameters










































































































































| Parameters | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| sentiment |  | Describes the schema for phrase detected. | Object |
|  | name | Name of the category detected phrase belongs to. | String |
|  | start | Starting position of the detected phrase in passed text. | Integer |
|  | end | Ending position of the detected phrase in passed text. | Integer |
|  | phrase | Detected phrase. | String |
|  | confidence | Confidence of the prediction, value ranges between 0-1. | Double |
| category |  | Describes the schema for phrase detected. | Object |
|  | name | Name of the category detected phrase belongs to. | String |
|  | start | Starting position of the detected phrase in passed text. | Integer |
|  | end | Ending position of the detected phrase in passed text. | Integer |
|  | phrase | Detected phrase. | String |
|  | confidence | Confidence of the prediction, value ranges between 0-1. | Double |
|  | l1 | L1 category of the detected product. | String |
|  | l2 | L2 category of the detected product. | String |
|  | l3 | L3 category of the detected product. | String |
| brand |  | Describes the schema for phrase detected. | Object |
|  | name | Name of the category detected phrase belongs to. | String |
|  | start | Starting position of the detected phrase in passed text. | Integer |
|  | end | Ending position of the detected phrase in passed text. | Integer |
|  | phrase | Detected phrase. | String |
|  | confidence | Confidence of the prediction, value ranges between 0-1. | Double |

[](https://dev.sprinklr.com/product-insights-batch-predict)




[Back to top](https://dev.sprinklr.com/product-insights-batch-predict)
