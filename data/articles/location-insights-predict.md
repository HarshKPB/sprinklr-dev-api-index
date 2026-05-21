---
title: "Location Insights Predict"
slug: location-insights-predict
url: https://dev.sprinklr.com/location-insights-predict
---

# Location Insights Predict

#
  POST Location Insights Predict




The Location Insights Predict API is capable of identifying common trends within unstructured data to apply structure and drive analysis based on location and modeling structure of respective business. Using this API, you can make a prediction request on a single message i.e., one at a time.

**Note: ** Please reach out to your Success Manager or Sprinklr support to get Intuition API's enabled for your environment.

   **Use Case: **



- Insights can be leveraged for any unstructured data; flat text files (Clavis data), social data, online surveys, voice transcripts etc. These insights can be unifed for analysis. Examples of deployment include Sentiment Analysis, CX insights, Location Insights, Verticalised Insights and Competitor Insights.

- Ability to identify common trends within unstructured data to apply structure and drive analysis.

- Large brands need data driven analytics to take better informed business decisions. Sprinklr Insights model uses Artificial Intelligence and Machine Learning techniques to convert massive volumes of unstructured data into easy to use structured interactive insights and enable brands to make prompt, confident and impactful business decisions.

- In-depth analysis on which insight categories of a product are drawing negative sentiments and which categories are getting appreciation and positive sentiment. It provides a much granular summary of Brand Health by classifying all text data into phrase level insights.


## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/intuition/location-insights/predict

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

## Request - Parameters






























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| engineKey | Required | The engine type. | String |
| text | Required | Message text on which you want to perform the analysis. | String |
| language | Required | Language of the message. | String |

## Example - Request















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/location-insights/predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "string",
  "language": "string",
  "engineKey": "string"
}'






## Example - Response





{
"data": {
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
        "confidence": 0
      },
      "subject": {
        "name": "string",
        "start": 0,
        "end": 0,
        "phrase": "string",
        "confidence": 0
      }
    }
  ]
},
"errors": []
}







## Response Parameters
























































































































| Parameters | Sub Parameter | Description | Type |
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
| subject |  | Describes the schema for phrase detected. | Object |
|  | name | Name of the category detected phrase belongs to. | String |
|  | start | Starting position of the detected phrase in passed text. | Integer |
|  | end | Ending position of the detected phrase in passed text. | Integer |
|  | phrase | Detected phrase. | String |
|  | confidence | Confidence of the prediction, value ranges between 0-1. | Double |

	[](https://dev.sprinklr.com/location-insights-predict)




[Back to top](https://dev.sprinklr.com/location-insights-predict)
