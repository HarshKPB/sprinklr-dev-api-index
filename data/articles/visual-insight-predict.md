---
title: "Visual Insight Predict"
slug: visual-insight-predict
url: https://dev.sprinklr.com/visual-insight-predict
---

# Visual Insight Predict

#
  POST  Visual Insights Predict



Visual Insight API helps analyze the given image and derives insights such as logo detection, object detection, OCR, visual sentiment,  and gender.  The API can also analyze other custom models developed for partners such as service tags, error codes, etc.

	**Note:**Please reach out to your `**Success Manager or Sprinklr support for enabling visual insights API**` capability and `**respective engines**` for your specific use case. Other custom visual models developed for partner-specific use cases can  also be availed upon request.



**Visual OCR: **
	Leveraging AI and and Deep Learning techniques to recognise text such as Service Tag, Error Code, etc. within an image and creating workflow based on visual input.

	**Use Case: **



- Visual OCR can be used across listening, marketing, sales and support use cases to identify objects within images or text present within an image.



**Visual Logo Detection: **
Leveraging AI and and Deep Learning techniques to query and recognise images containing logos that have been trained within the Sprinklr system.

	**Use Case: **



- Utilized by Marketing, Sales and Support teams to identify brand or competitor logos present within images brought into the platform.

- Can be leveraged to identify moments of (brand) consumption, device detection and event marketing reporting.



**Visual Sentiment: **
Leveraging AI and and Deep Learning techniques to analysis the facial expressions captured within an image to determine the sentiment on a post.

	**Use Case: **



- Unified Insights to determine customer sentiment that can be leveraged across marketing, VOC and support teams.



**Visual Gender: **
Analysis of the gender of people captured in the image.

	**Use Case: **



- To Identify association of gender with brand by combining logo detection with gender identification.


## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/intuition/visual/predict

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















````






















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| engineKey | Required | Engine key refers to the unique identifier of the task that needs to be performed on the given image.                         For example, “logo” for detecting logos in the given image or “ocr” for extracting text from the image. | String |
| resourceUrl | Required | This is a public url of image on which you want to run Visual Insight prediction. | String |
| language | Required | Language of the message. | String |
| details | Optional | Using this field additional details can be passed in key value pair. | Map<String, String> |

## Example - Request and Response for Logo















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/visual/predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
"engineKey": "logo",
"resourceURL": "https://cdn.pixabay.com/photo/2021/10/12/00/56/youtube-6702083_1280.png",
"language": "en"
}'






## Example - Response





		{
    "data": {
        "input": {
            "engineKey": "logo",
            "resourceURL": "https://cdn.pixabay.com/photo/2021/10/12/00/56/youtube-6702083_1280.png",
            "language": "en"
        },
        "response": {
            "classDetails": [
                {
                    "label": "Youtube",
                    "confidence": 0.9421664,
                    "bbox": {
                        "xMin": 119,
                        "yMin": 352,
                        "xMax": 339,
                        "yMax": 500
                    }
                }
            ]
        }
    },
    "errors": []
}







## Example - Request and Response for OCR















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/visual/predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
"engineKey": "ocr",
"resourceURL": "https://cdn.pixabay.com/photo/2021/10/12/00/56/youtube-6702083_1280.png",
"language": "en"
}'






## Example - Response





		{
    "data": {
        "input": {
            "engineKey": "ocr",
            "resourceURL": "https://cdn.pixabay.com/photo/2021/10/12/00/56/youtube-6702083_1280.png",
            "language": "en"
        },
        "response": {
            "classDetails": [
                {
                    "label": "subscribe",
                    "confidence": 0.791439,
                    "bbox": {
                        "xMin": 376,
                        "yMin": 381,
                        "xMax": 853,
                        "yMax": 464
                    }
                }
            ]
        }
    },
    "errors": []
}







## Response Parameters



















































		****




| Parameters | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| Input |  | The object containing the whole API request. | Object |
|  | engineKey | An unique identifier key, which is associated with the brands use case. | String |
|  | resourceUrl | This is a public url of image on which you want to run Visual Insight prediction. | String |
|  | language | Language of the message. | String |
|  | details | Using this field additional details can be passed in key value pair. | Map<String, String> |
| response |  | The object containing API response. | Object |
|  | classDetails | Contains the details related to the object identified in an image. More details below in Class Details Description Table | Array |

## Class Details Description Table






















































| Parameters | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| label |  | The label of the identified object such as bird. | String |
| confidence |  | The confidence score of the identified object. Maximum is 1. | Double |
| bbox |  | The bounding box containing details of the actual position of the identified object | Object |
|  | xMin | The coordinates of bottom left corner of the bounding box/rectangle. | Integer |
|  | yMin | The coordinates of bottom left corner of the bounding box/rectangle. | Integer |
|  | xMax | The coordinates of the top right corner of the bounding box/rectangle. The maximum value of xmax is width of the image. | Integer |
|  | yMax | The coordinates of the top right corner of the bounding box/rectangle. The maximum value of ymax is the height of the image. | Integer |

[](https://dev.sprinklr.com/visual-insight-predict)






[Back to top](https://dev.sprinklr.com/visual-insight-predict)
