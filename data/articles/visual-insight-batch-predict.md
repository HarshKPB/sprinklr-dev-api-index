---
title: "Visual Insight Batch Predict"
slug: visual-insight-batch-predict
url: https://dev.sprinklr.com/visual-insight-batch-predict
---

# Visual Insight Batch Predict

#
  POST  Visual Insights Batch Predict



The Visual Insight Batch Predict API is capable of analyzing multiple images for the same engine type or a single image with multiple engine types.

This API helps predict different objects that are present in the image such as text objects like Service Tag, Error Code, etc.

	**Note: ** Please reach out to your Success Manager or Sprinklr support to get Intuition API's enabled for your environment.

Below are the types of analysis that can be performed on image/s w.r.t use cases:

**Visual OCR: **
	Leveraging AI and and Deep Learning techniques to recognise text such as Service Tag, Error Code, etc. within image/images and creating workflow based on visual input.

	**Use Case: **



- Visual OCR can be used across listening, marketing, sales and support use cases to identify objects within images or text present within an image.



**Visual Logo Detection: **
Leveraging AI and and Deep Learning techniques to query and recognise images containing logos that have been trained within the Sprinklr system.

	**Use Case: **



- Utilized by Marketing, Sales and Support teams to identify brand or competitor logos present within images brought into the platform.

- Can be leveraged to identify moments of (brand) consumption, device detection and event marketing reporting.



**Visual Sentiment: **
Leveraging AI and and Deep Learning techniques to analyze the facial expressions captured within an image to determine the sentiment on a post.

	**Use Case: **



- Unified Insights to determine customer sentiment that can be leveraged across marketing, VOC and support teams.



**Visual Gender: **
Analysis of the gender of people captured in the image.

	**Use Case: **



- To Identify association of gender with brand by combining logo detection with gender identification.


## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/intuition/visual/batch-predict

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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



























``










| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| engineKey | Required | A unique identifier key, which is associated with the brands use case | String |
| resourceUrl | Required | This is a public url of image on which you want to run Visual Insight prediction | String |
| language | Required | Language of the message                         DEFAULT: "en" | String |
| details | Optional | Using this field additional details can be passed in key value pair. | Map<String, String> |

## Example - Request















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/intuition/visual/batch-predict' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '[{
"engineKey": "{engine_key}",
"resourceURL": "https://new.wikiidia.com/wikicommons/2/900/Hooded.jpg",
"language": "en",
"details": {"key1": "value1", "key2": "value2"}
},
{
"engineKey": "{engine_key}",
"resourceURL": "https://new.wikiidia.com/wikicommons/2/900/Hooded.jpg",
"language": "en",
"details": {"key3": "value3", "key4": "value4"}
}]'






## Example - Response





		{
    "data": [
    {
        "input": {
            "engineKey": "{engine_key}",
            "resourceURL": "https://new.wikiidia.com/wikicommons/2/900/Hooded.jpg",
            "language": "en",
            "details": {"key1": "value1", "key2": "value2"}
        },
        "response": {
            "classDetails": [
                {
                	"label": "bird",
                    "confidence": 0.91458714,
                    "bbox": {
                    	"xMin": 10,
                    	"yMin": 100,
                    	"xMax": 20,
                    	"yMax": 120
                    }
                }
            ]
        }
    },
    {
        "input": {
            "engineKey": "{engine_key}",
            "resourceURL": "https://new.wikiidia.com/wikicommons/2/900/Hooded.jpg",
            "language": "en",
            "details": {"key3": "value3", "key4": "value4"}
        },
        "response": {
            "classDetails": [
                {
                    "label": "bird",
                    "confidence": 0.952,
                    "bbox": {
                        "xMin": 10,
                        "yMin": 100,
                        "xMax": 25,
                        "yMax": 220
                    }
                }
            ]
        }
    }],
    "errors": []
}







## Response Parameters

































``

















			****




| Parameters | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| Input |  | The object comprising the request payload | Object |
|  | engineKey | A unique identifier key, which is associated with the brand's use case. | String |
|  | resourceUrl | This is a public url of image on which you want to run Visual Insight prediction. | String |
|  | language | Language of the message                         DEFAULT: "en" | String |
|  | details | Using this field additional details can be passed in key value pair. | Map<String, String> |
| response |  | The object comprising the API response | Object |
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

[](https://dev.sprinklr.com/visual-insight-batch-predict)




[Back to top](https://dev.sprinklr.com/visual-insight-batch-predict)
