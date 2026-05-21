---
title: "Text Predict"
slug: text-predict
url: https://dev.sprinklr.com/text-predict
---

# Text Predict

#
  POST  Text Predict


The Text Predict API is capable of analyzing the Sentiment and Emotion of a message and can also detect whether a message is a Spam or not. Using the text predict API, you can make a prediction request on a single message i.e., one at a time. Below are the types of analyses that can be performed on a message:


**Note: ** Please reach out to your Success Manager or Sprinklr support to get Intuition API's enabled for your environment.

**Sentiment Analysis: **

- Categorizes data into positive, negative or neutral sentiment based on the language and the context of the text through combined use of Natural Language Processing and Deep Learning techniques.

**Use Case: **


- Sentiment analysis helps gain real-time insight about brand health or monitor customer feedback to your marketing campaigns.

- Sentiment are leveraged across Voice of the Customer, Marketing, Advertising, Research and Support use cases to inform brands of customer experience across a variety of touchpoints. A few of the use cases that sentiment supports include CSAT prediction, hawkeye, skills based routing, etc.

**Emotion Analysis: **

- Sprinklr Emotion Analysis to get emotion-based insights on text data. It uses Machine Learning techniques to read through the messages along with their context, and not just certain combinations of keywords, in order to detect the underlying emotion conveyed by the text. Also, while weighing the dominant emotion conveyed, we take into consideration the emoticons used as well.

**Use Case: **

- Emotion Analysis helps brands effectively manage their customer experience, brand reputation and sales. Imagine a customer writing ‘I am not happy with your brand services’ vs another writing ‘I am highly dissatisfied with the kind of services you offer’. It’s clear from these statements that the second customer is at a higher churn risk. Emotion Analysis helps brands take care of such issues. Also, unlike sentiment analysis, which simply classifies messages into positive, negative, or neutral categories, emotion analysis give a deeper and more granular insight into how the users/ consumers are feeling about a brand.

- Identifies a variety of emotions to inform Unified Insights, Early Warning Systems, and Skills Based Routing for real-time actionability and post-interaction analysis. Can also be utilized by Marketing and Brand teams to analyze response to brand messaging.

**Spam Detection: **

- Spam Detection model enables brands to filter out spam messages and focus on accurate and relevant data.

**Use Case: **

- AI powered models filter out unendorsed advertisements (reseller promos and offers etc.) news ads, and inappropriate content (e.g. obscenity) from the data in order to keep only relevant data.

- Spam Detection is applied to Moderation, Skills Based Routing and Unified Insights to ensure only relevant content is captured for routing and reporting purposes.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/intuition/text/predict

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

## Example: Engine Type - Sentiment















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/text/predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "engineKey": "sentiment",
    "text": "Hello how are you?",
    "language": "en"
}'






## Example - Response





{
    "data": {
        "input": {
            "text": "Hello how are you?",
            "language": "en",
            "engineKey": "sentiment"
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
    "errors": []
}







## Example: Engine Type - Emotion















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/text/predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "engineKey": "emotion",
    "text": "Hello how are you?",
    "language": "en"
}'






## Example - Response





{
    "data": {
        "response": {
            "classDetails": [
                {
                    "label": Uncategorized",
                    "confidence": 1.0
                }
            ]
        },
        "input": {
            "text": "Hello how are you?",
            "language": "en",
            "engineKey": "emotion"
        }
    },
    "errors": []
}







## Example: Engine Type - Spam















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/text/predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "engineKey": "spam",
    "text": "Hello how are you?",
    "language": "en"
}'






## Example - Response





{
 "data": {
   "input":{
      "text":"Hello how are you?",
      "language":"en",
      "engineKey":"spam"
   },
   "response":{
      "classDetails":[
         {
            "label":"Not Spam",
            "confidence":0.915664
         }
      ]
   },
  "errors": []
}






	[](https://dev.sprinklr.com/text-predict)




[Back to top](https://dev.sprinklr.com/text-predict)
