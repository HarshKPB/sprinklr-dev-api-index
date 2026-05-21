---
title: "Handshake API - Fetch Application Details"
slug: handshake-api-fetch-application-details
url: https://dev.sprinklr.com/handshake-api-fetch-application-details
---

# Handshake API - Fetch Application Details

#
Handshake API - Fetch Application Details



Using this API, you can fetch the live chat application details for the give application Id.

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/handshake/application/{appId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











      ``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-referer | {Live Chat Application Landing Page Url} | Refers to the landing page url where the live chat application is hosted |

### Path Parameter













****

-
-




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| appId | Required | Refers to the unique identifier for the live chat applicationHow to Extract appId from UI?Navigate to Sprinklr Service on the platform and click on "Live Chat Care" Option under "Brand Care"Search for the desired live chat application and copy and use the "Application ID" from the third column mentioned against the application name | String |

## Example - Request




  Copy Code


curl -X GET \
 'https://{env}-live-chat.sprinklr.com/api/livechat/v1/handshake/application/65015cddb2678b575c01b175_app_1000163501'\
  -H 'x-chat-referer: https://live-chat-static.sprinklr.com/test-html/index.html' \
  -H 'content-type: application/json'





### Example - Response



{
    "id": "app_1000163501",
    "name": "[sj] test appln",
    "description": "[sj] test appln",
    "showBrandProfile": false
}





### Response Parameters































| Parameter | Description | Type |
| --- | --- | --- |
| id | Refers to the unique identifier for the live chat application | Integer |
| name | Refers to the name of the live chat application | String |
| description | Refers to the description of the live chat application | String |
| showBrandProfile | If true, the brand's profile is shown along with the message sent to the user. Else, the agent details are displayed.You can find the toggle to enable this under the "Advanced Settings" section present within the edit live chat application window | String |

[](https://dev.sprinklr.com/handshake-api-fetch-application-details)

[Back to top](https://dev.sprinklr.com/handshake-api-fetch-application-details)
