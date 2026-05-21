---
title: "Text Batch Predict"
slug: text-batch-predict
url: https://dev.sprinklr.com/text-batch-predict
---

# Text Batch Predict

#
  POST Text Batch Predict



The Text Batch Predict API is capable of analyzing the Sentiment and Emotion of messages and can also detect whether a batch of message is having a spam or not. Using the text batch predict API, you can make a prediction request on a list of messages. Below are the types of analyses that can be performed on list of messages:



**Note: ** Please reach out to your Success Manager or Sprinklr support to get Intuition API's enabled for your environment.

**Sentiment Analysis: **


- Categorizes data into positive, negative or neutral sentiment based on the language and the context of the text through combined use of Natural Language Processing and Deep Learning techniques.

**Emotion Analysis: **


- Sprinklr Emotion Analysis to get emotion-based insights on text data. It uses Machine Learning techniques to read through the messages along with their context, and not just certain combinations of keywords, in order to detect the underlying emotion conveyed by the text. Also, while weighing the dominant emotion conveyed, we take into consideration the emoticons used as well.

**Spam Detection: **


- Spam Detection model enables brands to filter out spam messages and focus on accurate and relevant data.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/intuition/text/batch-predict

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

## Request Body Parameters













			``````
















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| engineKey | Required | You can select the engine type from sentiment, emotion, spam. | String |
| text | Required | Message text on which you want to perform the analysis. | String |
| language | Required | Language of the message. | String |

**Note: ** Currently the deployed engine types include: `sentiment`, `emotion`, and `spam`

## Example - Request















Copy Code



curl -X POST \
  'https://api3.sprinklr.com`/{env}/`api/v2/intuition/text/batch-predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '[
    {
        "engineKey": "{engine-key}",
        "text": "Hello how are you?",
        "language": "en"
    },
    {
        "engineKey": "{engine-key}",
        "text": "Hello how are you?",
        "language": "en"
    },
    {
        "engineKey": "{engine-key}",
        "text": "Hello how are you?",
        "language": "en"
    }
]'






## Example - Response





	{
    "data": [
        {
            "input": {
                "text": "Hello how are you?",
                "language": "en",
                "engineKey": "{engine-key}"
            },
            "response": {
                "classDetails": [
                    {
                        "label": "Uncategorized",
                        "confidence": 1.0
                    }
                ]
            }
        },
        {
            "input": {
                "text": "Hello how are you?",
                "language": "en",
                "engineKey": "{engine-key}"
            },
            "response": {
                "classDetails": [
                    {
                        "label": "Neutral",
                        "confidence": 0.91458714
                    }
                ]
            }
        },
        {
            "input": {
                "text": "Hello how are you?",
                "language": "en",
                "engineKey": "{engine-key}"
            },
            "response": {
                "classDetails": [
                    {
                        "label": "Not Spam",
                        "confidence": 0.915664
                    }
                ]
            }
        }
    ],
    "errors": []
}







[](https://dev.sprinklr.com/text-batch-predict)




[Back to top](https://dev.sprinklr.com/text-batch-predict)
