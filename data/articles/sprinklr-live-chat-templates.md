---
title: "Sprinklr Live Chat Templates"
slug: sprinklr-live-chat-templates
url: https://dev.sprinklr.com/sprinklr-live-chat-templates
---

# Sprinklr Live Chat Templates

#
POST Sprinklr Live Chat Templates

You can use this API to publish dynamic templates across supported social and messaging channels. This page specifically lists Sprinklr Live Chat templates that you can publish using the API. Each template type includes its own parameters and example payloads to help you construct and test your requests.

**Dev Notes: **This API enhancement strictly works for ` "channelType": "SPRINKLR_LIVE_CHAT"`.

For Sprinklr Live Chat, you can use this API to publish the following message types:


- [Publishing CARD](https://dev.sprinklr.com/sprinklr-live-chat-templates#card-example)

- [Publishing QUICK_REPLY](https://dev.sprinklr.com/sprinklr-live-chat-templates#quick-reply-example)

- [Publishing CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#carousel-example)

- [Publishing PRODUCT_LIST](https://dev.sprinklr.com/sprinklr-live-chat-templates#product-list-example)

- [Publishing APPOINTMENT](https://dev.sprinklr.com/sprinklr-live-chat-templates#appointment-example)

- [Publishing SURVEY](https://dev.sprinklr.com/sprinklr-live-chat-templates#survey-example)

- [Publishing SECURE_FORM](https://dev.sprinklr.com/sprinklr-live-chat-templates#secure-form-example)

- [Publishing RICH_TEXT_CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#rich-text-carousel-example)

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/publishing/message

## Headers

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
















****``
``````






























****
- ``
- ``
- ``
- ``
- ``
- ``
- ``
- ``[Attachment Object Parameters](https://dev.sprinklr.com/sprinklr-live-chat-templates#attachment-object-parameters)


















































****``
****````````













      ``
































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountId |  | Required | Unique Id of the Live Chat account. Dev Notes: You can derive the accountId from the Live Chat app ID.     For example, if the Live Chat app ID is app_12345, then accountId = 12345. | Integer |
| content |  | Required | Contains message details. | Object |
|  | title | Optional | Title of the message. | String |
|  | text | Optional | Text of the message. | String |
|  | attachment | Required | Attachment object containing type-specific parameters.           Supported Types: 		   			CARD   			QUICK_REPLY   			CAROUSEL   			PRODUCT_LIST   			APPOINTMENT   			SURVEY   			SECURE_FORM         RICH_TEXT_CAROUSEL 		 		For more details on the parameters of each attachment type, refer to the  table below. | Object |
| scheduleDate |  | Optional | Date/time to schedule the message | Integer |
| taxonomy |  | Required | Object containing campaign and custom property details | Object |
|  | campaignId | Required | Campaign identifier to associate the message | String |
|  | clientCustomProperties | Optional | Client custom properties for the message | Object |
|  | partnerCustomProperties | Optional | Partner custom properties for the message | Object |
| inReplyToMessageId |  | Required | The message ID being replied to. | String |
| approval |  | Optional | Type of approval to process.Default Value: NONESupported Values: ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE | Object |
| toProfile |  | Required | Profile details for the recipient. | Object |
|  | channelType | Required | Channel type. In this case, use SPRINKLR_LIVE_CHAT. | String |
|  | channelId | Required | Channel identifier of the profile. | String |
|  | screenName | Required | Screen name of the profile. | String |
| tags |  | Optional | Tags to be added to the message. | String |
| urlShortenerId |  | Optional | URL shortener identifier to apply to the message. | String |

### Attachment Object Parameters

Use the links below to navigate to the parameter tables for each attachment type.


- [CARD](https://dev.sprinklr.com/sprinklr-live-chat-templates#card-parameters)

- [QUICK_REPLY](https://dev.sprinklr.com/sprinklr-live-chat-templates#quick-reply-parameters)

- [CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#carousel-parameters)

- [PRODUCT_LIST](https://dev.sprinklr.com/sprinklr-live-chat-templates#product-list-parameters)

- [APPOINTMENT](https://dev.sprinklr.com/sprinklr-live-chat-templates#appointment-parameters)

- [SURVEY](https://dev.sprinklr.com/sprinklr-live-chat-templates#survey-parameters)

- [SECURE_FORM](https://dev.sprinklr.com/sprinklr-live-chat-templates#secure-form-parameters)

- [RICH_TEXT_CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#rich-text-carousel-parameters)

#### CARD Attachment Parameters

**Example Request: **For complete request, see the [CARD](https://dev.sprinklr.com/sprinklr-live-chat-templates#card-example) example.

Use this attachment to publish a Card message.















      ``





























****``
****````










































``
``````




| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this template, use CARD | String |
| title |  | Required | Title of the card | String |
| description |  | Optional | Description of the Live Chat template | String |
| previewImageUrl |  | Required | Preview image URL | String |
| disableManualResponse |  | Required | Prevents customers from sending free‑form messages while interacting with this template. When enabled, users can only respond using predefined options until the brand sends the next message.           Default: false           Supported Values: true, false | Boolean |
| buttons |  | Required | Array of button objects. | Array |
| buttons[] | id | Required | Unique identifier for the button | String |
|  | title | Required | Title of the button | String |
|  | subtitle | Optional | Subtitle text for the button | String |
|  | payload | Optional | Payload data associated with the button | String |
| buttons[].actionDetail | action | Required | Action type. For CARD, possible actions include:           TEXT           OPEN_URL (requires url property, e.g., "url":"www.google.com") | String |


**Dev Notes:**



-
      `"action" : "OPEN_URL"` is used to redirect the user to another page on the web when they click on it.


-
      For adding bold text in title and description, you can use the following tags:
      `<p style="margin: 0;1"> <strong> Title/Description </strong> </p>`




#### QUICK_REPLY Attachment Parameters

**Example Request: **For complete request, see the [QUICK_REPLY](https://dev.sprinklr.com/sprinklr-live-chat-templates#quick-reply-example) example.

Quick replies in Sprinklr Live Chat let users choose from preset options for faster responses. They’re useful when a bot asks a question and expects an answer. Once a user selects an option, the quick replies disappear, leaving only the chosen response visible.

**Related Knowledge Base Article: **[Quick Replies](https://www.sprinklr.com/help/articles/rich-text-assets/quick-replies/63b83c9df7c92723b10e617b)















      ``






















****``
****````









































      ``




| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this template, use QUICK_REPLY. | String |
| title |  | Required | Title of the quick reply | String |
| previewImageUrl |  | Required | Preview image URL | String |
| disableManualResponse |  | Required | Prevents customers from sending free‑form messages while interacting with this template.           When enabled, users can only respond using predefined options until the brand sends the next message.           Default: false           Supported Values: true, false | Boolean |
| quickReplies |  | Required | Array of quick reply button objects | Array |
| quickReplies[] | id | Required | Unique identifier for the quick reply button | String |
|  | title | Required | Title of the quick reply button | String |
|  | subtitle | Optional | Subtitle text for the quick reply button | String |
|  | payload | Optional | Payload data associated with the quick reply button | String |
| quickReplies[].actionDetail | action | Required | Action type. For QUICK_REPLY, the possible action is TEXT | String |

#### CAROUSEL Attachment Parameters

**Example Request: **For complete request, see the [CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#carousel-example) example.

A carousel is a collection of card assets displayed side by side, allowing horizontal scrolling. Customers can interact with these cards directly in the conversation thread by selecting an option or tapping a button.
























      ``








****``
****````






      ``






      ``























































      ``




| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| attachment |  | Required | Defines the attachment object | Object |
| type |  | Required | Type of attachment. For this template, use CAROUSEL. | String |
| disableManualResponse |  | Required | Prevents customers from sending free‑form messages while interacting with this template.           When enabled, users can only respond using predefined options until the brand sends the next message.           Default: false           Supported Values: true, false | Boolean |
| cardAttachmentList |  | Required | Array of CARD objects. See Card Attachment List table below. | Array |
| cardAttachmentList[].CARD | type | Required | Use CARD for carousel items. | String |
|  | title | Required | Title of the card | String |
|  | previewImageUrl | Optional | Image URL for the card | String |
|  | buttons | Required | Object containing details about the button | Array |
| buttons[] | id | Required | Unique identifier for the button | String |
|  | title | Required | Title of the button | String |
|  | subtitle | Optional | Subtitle text for the button | String |
|  | payload | Optional | Payload data associated with the button | String |
| buttons[].actionDetail | action | Required | Action type. For CAROUSEL, the possible action is TEXT | String |

#### PRODUCT_LIST Attachment Parameters

**Example Request: **For complete request, see the [PRODUCT_LIST](https://dev.sprinklr.com/sprinklr-live-chat-templates#product-list-example) example.















      ``






      ``




















      ``



























      ``






      ``















****````













      ``











| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this template, use PRODUCT_LIST. | String |
| cardAttachmentList |  | Required | Array of CARD objects representing products | Array |
| cardAttachmentList[].CARD | title | Required | Title of the product card | String |
|  | previewImageUrl | Required | Image URL for the product card | String |
|  | type | Required | Always CARD for product list items | String |
| buttons |  | Required | CTA buttons with action details | Array |
| buttons[] | title | Required | Label for the button | String |
| buttons[].actionDetail | url | Required | URL to open when the button is clicked | String |
|  | target | Optional | Target behavior (for example, _blank) | String |
|  | action | Required | Action type (for example, OPEN_URL) | String |
| description |  | Optional | Description of the product list | String |
| disableManualResponse |  | Optional | Prevents customers from sending free‑form messages while interacting with this template.           When enabled, users can only respond using predefined options until the brand sends the next message.           Supported Values: true, false | Boolean |
| otherConfigs |  | Optional | Object containing additional configuration | Object |
|  | layoutType | Optional | Layout type (for example, IMAGE_TOP) | String |
| screenReaderLabel |  | Optional | Accessibility label for screen readers | String |

#### APPOINTMENT Attachment Parameters

**Example Request: **For complete request, see the [APPOINTMENT](https://dev.sprinklr.com/sprinklr-live-chat-templates#appointment-example) example.















      ``









































      ``
































































****````


















| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this template, use APPOINTMENT. | String |
| selectDateTitle |  | Required | Title shown for selecting a date | String |
| selectTimeTitle |  | Required | Title shown for selecting a time | String |
| selectDatePlaceholder |  | Optional | Placeholder text for date selection | String |
| submitDateTitle |  | Optional | Title shown on submit date button | String |
| numDays |  | Optional | Number of days available for selection | Integer |
| dateFormat |  | Optional | Date format to display (for example, MMM D YYYY) | String |
| submit |  | Required | Object containing submit button details | Object |
|  | id | Required | Unique identifier for submit button | String |
|  | title | Required | Title of the submit button | String |
| postSubmit |  | Optional | Object containing post-submit button details | Object |
|  | id | Optional | Unique identifier for post-submit button | String |
|  | title | Optional | Title of the post-submit button | String |
| slotDefinitionConfigId |  | Required | Configuration ID for slot definition | String |
| showSubmittedContent |  | Optional | Flag to show submitted content after submission | Boolean |
| disableManualResponse |  | Optional | Prevents customers from sending free‑form messages while interacting with this template.           When enabled, users can only respond using predefined options until the brand sends the next message.           Supported Values: true, false | Boolean |
| postSubmitTitle |  | Optional | Title shown after submission | String |
| fromFirstAvailableSlot |  | Optional | Flag to start from first available slot | Boolean |

#### SURVEY Attachment Parameters

**Example Request: **For complete request, see the [SURVEY](https://dev.sprinklr.com/sprinklr-live-chat-templates#survey-example) example.















      ``






















****````



































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this template, use SURVEY. | String |
| title |  | Required | Title of the survey | String |
| description |  | Optional | Description text for the survey | String |
| disableManualResponse |  | Optional | Prevents customers from sending free‑form messages while interacting with this template.           When enabled, users can only respond using predefined options until the brand sends the next message.           Supported Values: true, false | Boolean |
| postSubmitTitle |  | Optional | Title shown after submission | String |
| screenReaderLabel |  | Optional | Accessibility label for screen readers | String |
| surveyButton |  | Required | Object containing survey button details | Object |
|  | id | Required | Unique identifier for the survey button | String |
|  | title | Required | Title of the survey button | String |
| postSubmit |  | Optional | Object containing post-submit button details | Object |
|  | id | Optional | Unique identifier for the post-submit button | String |
|  | title | Optional | Title of the post-submit button | String |
| showSubmittedContent |  | Optional | Flag to show submitted content after survey completion | Boolean |

#### SECURE_FORM Attachment Parameters

**Example Request: **For complete request, see the [SECURE_FORM](https://dev.sprinklr.com/sprinklr-live-chat-templates#secure-forms-example) example.

You can send Secure Forms to safely collect sensitive or confidential information from customers. These forms ensure data is shared with agents within a protected, controlled environment.

**Related Knowledge Base Article: **[Secure Forms](https://www.sprinklr.com/help/articles/pci-compliant-secure-forms/configuration-of-secure-forms/63d3ce7f2c015d03d4e7fb3d)















      ``


































      ``



























      ``






      ``




| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this template, use SECURE_FORM. | String |
| form |  | Required | Object containing the form details. | Object |
|  | formTitle | Required | Title of the secure form | String |
|  | fields | Required | Array of field objects | Array |
|  | fields.name | Required | Label or name of the form field | String |
|  | fields.type | Required | Type of the form field (e.g., EMAIL) | String |
| submit |  | Required | Object containing submit button details | Object |
|  | title | Required | Title of the submit button | String |
|  | actionDetail | Required | Object containing action details | Object |
|  | actionDetail.postBackHandlerType | Required | Handler type for secure form post-back (SECURE_FORM_POST_BACK) | String |
|  | actionDetail.action | Required | Action type. For example, POST_BACK. | String |

#### RICH_TEXT_CAROUSEL Attachment Parameters

**Example Request: **For complete request, see the [RICH_TEXT_CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#rich-text-carousel-example) example.















      ``








****``
****````






      ``






      ``























































      ``











| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this template, use RICH_TEXT_CAROUSEL. | String |
| disableManualResponse |  | Required | Prevents customers from sending free‑form messages while interacting with this template.           When enabled, users can only respond using predefined options until the brand sends the next message.           Default: false.           Supported Values: true, false. | Boolean |
| cardAttachmentList |  | Required | Array of CARD objects displayed in the carousel. | Array |
| cardAttachmentList[].CARD | type | Required | Always CARD for carousel items. | String |
|  | title | Required | Title of the card. | String |
|  | previewImageUrl | Optional | Image URL for the card. | String |
|  | buttons | Optional | Array of button objects. | Array |
| buttons[] | id | Required | Unique identifier for the button. | String |
|  | title | Required | Title of the button. | String |
|  | subtitle | Optional | Subtitle text for the button. | String |
|  | payload | Optional | Payload data associated with the button. | String |
| buttons[].actionDetail | action | Required | Action type. For RICH_TEXT_CAROUSEL, the possible action is TEXT. | String |
| screenReaderLabel |  | Optional | Accessibility label for screen readers. | String |

## Examples

The following examples show how to publish dynamic Live Chat templates using the Publishing API.


- [CARD](https://dev.sprinklr.com/sprinklr-live-chat-templates#card-example)

- [QUICK_REPLY](https://dev.sprinklr.com/sprinklr-live-chat-templates#quick-reply-example)

- [CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#carousel-example)

- [PRODUCT_LIST](https://dev.sprinklr.com/sprinklr-live-chat-templates#product-list-example)

- [APPOINTMENT](https://dev.sprinklr.com/sprinklr-live-chat-templates#appointment-example)

- [SURVEY](https://dev.sprinklr.com/sprinklr-live-chat-templates#survey-example)

- [SECURE_FORM](https://dev.sprinklr.com/sprinklr-live-chat-templates#secure-form-example)

- [RICH_TEXT_CAROUSEL](https://dev.sprinklr.com/sprinklr-live-chat-templates#rich-text-carousel-example)

### CARD

#### Example - Request



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
 {
  "accountId": 0,
  "content": {
    "title": "title",
    "text": "text",
    "attachment": {
      "type": "CARD",
      "title" : "title of card",
      "previewImageUrl" : " ",
      "disableManualResponse" : false,
      "buttons" : [
          {
            "id" : "",
            "title" : "title of button",
            "subtitle" : "subtitle",
            "payload" : "payload",
            "actionDetail" : {
              "action" : "TEXT"
            }
          }
      ]
    }
  },
  "scheduleDate": 0,
   "taxonomy": {
    "campaignId": "",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "",
  "toProfile": {
    "channelType": "SPRINKLR_LIVE_CHAT",
    "channelId": "",
    "screenName": ""
  }
}'
 

     
     
   
 

### Example - Response



{
    "data": [
        "POST_3139636177"
    ],
    "errors": []
}
 

     
     
   

### QUICK_REPLY

#### Example - Request



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
 {
  "accountId": 0,
  "content": {
    "title": "",
    "text": "text",
    "attachment": {
      "type": "QUICK_REPLY",
      "message" : "title",
      "disableManualResponse" : false,
      "quickReplies" : [
          {
            "id" : "",
            "title" : "title of button",
            "subtitle" : "subtitle of button",
            "payload" : "payload",
            "actionDetail" : {
              "action" : "TEXT"
            }
          }
      ]
    }
  },
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "",
  "toProfile": {
    "channelType": "SPRINKLR_LIVE_CHAT",
    "channelId": "",
    "screenName": ""
  }
}' 

     
     
 
 

#### Example - Response



{
    "data": [
        "POST_3329636297"
    ],
    "errors": []
}
 

     
     
   

### CAROUSEL

#### Example - Request



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
  "accountId": 300003002,
  "content": {
    "title": "CarouselTest",
    "text": "outside text",
    "attachment": {
      "type" : "CAROUSEL",
      "disableManualResponse" : false,
      "cardAttachmentList" : [
         {
          "type": "CARD",
          "title" : "CARD 1st Option",
          "previewImageUrl" : "",
          "buttons" : [
              {
                "id" : "1234",
                "title" : "Button 1",
                "subtitle" : "",
                "payload" : "",
                "actionDetail" : {
                "action" : "TEXT"
                }
              }
          ]
        },
        {
          "type": "CARD",
          "title" : "Card 2nd Option",
          "previewImageUrl" : "",
          "buttons" : [
              {
                "id" : "8907",
                "title" : "Button3",
                "subtitle" : "",
                "payload" : "",
                "actionDetail" : {
                "action" : "TEXT"
                }
              }
          ]
        }
      ]
    }
  },
  "taxonomy": {
    "campaignId": "132_1",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "ACCOUNT_300003322_1589299597268_SPRINKLR_LIVE_CHAT_313_5ebac98db73d980001c09608",
  "toProfile": {
    "channelType": "SPRINKLR_LIVE_CHAT",
    "channelId": "5df0f97fe00ac94cde5d49a6",
    "screenName": "Sprinklr"
  }
}'
 

     
     
 

#### Example - Response



{
    "data": [
        "POST_3119636127"
    ],
    "errors": []
}
 

     
     
   
 

### PRODUCT_LIST

#### Example - Request



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountId": 66131825,
    "content": {
        "title": "product_list",
        "text": "checl",
        "attachment": {
            "type": "PRODUCT_LIST",
            "cardAttachmentList": [
                {
                    "title": "product_list_image at top",
                    "previewImageUrl": "https://abc.com/https___qa6-std-dam-connector-.png",
                    "type": "CARD"
                }
            ],
            "buttons": [
                {
                    "title": "cta_UPDATE",
                    "actionDetail": {
                        "url": "https://www.sprinklr.com",
                        "target": "_blank",
                        "action": "OPEN_URL"
                    }
                }
            ],
            "description": "message of image top ",
            "disableManualResponse": true,
            "otherConfigs": {
                "layoutType": "IMAGE_TOP"
            },
            "screenReaderLabel": "reader"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_5947",
        "clientCustomProperties": {},
        "partnerCustomProperties": {}
    },
    "inReplyToMessageId": "ACCOUNT_66127966_1770904503130_SPRINKLR_LIVE_CHAT_313_698ddbb7c720c33b56ab3438",
    "toProfile": {
        "channelType": "SPRINKLR_LIVE_CHAT",
        "channelId": "686ce4bdbfc4fe3077951a3c",
        "screenName": "Udyan_20.10"
    }
}'
 

     
     
 

#### Example - Response



{
    "data": [
        "POST_3119636127"
    ],
    "errors": []
}
 

     
     
   
 

### APPOINTMENT

#### Example - Request



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountId": 66001821,
    "content": {
        "title": "appointment",
        "text": "checl",
        "attachment": {
            "type": "APPOINTMENT",
            "selectDateTitle": "appointyment_date",
            "selectTimeTitle": "time_title",
            "selectDatePlaceholder": "placeholder",
            "submitDateTitle": "submit",
            "numDays": 2,
            "dateFormat": "MMM D YYYY",
            "submit": {
                "id": "29c20237-d0de-4bda-b021-e8d17f8f122a",
                "title": "Submit_button"
            },
            "postSubmit": {
                "id": "dba52a3f-865b-4dad-a80c-f8208301f585",
                "title": "Done"
            },
            "slotDefinitionConfigId": "68f755de6cb0171a504bb201",
            "showSubmittedContent": false,
            "disableManualResponse": true,
            "postSubmitTitle": "Thanks",
            "fromFirstAvailableSlot": false
        }
    },
    "taxonomy": {
        "campaignId": "66000002_5947",
        "clientCustomProperties": {},
        "partnerCustomProperties": {}
    },
    "inReplyToMessageId": "ACCOUNT_66127966_1770904503130_SPRINKLR_LIVE_CHAT_313_698ddbb7c720c33b56ab3438",
    "toProfile": {
        "channelType": "SPRINKLR_LIVE_CHAT",
        "channelId": "686ce4bdbfc4fe3077951a3c",
        "screenName": "Udyan_20.10"
    }
}'
 

     
     
 

#### Example - Response



{
    "data": [
        "POST_3119636127"
    ],
    "errors": []
}
 

     
     
   

### SURVEY

#### Example - Request



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountId": 66001821,
    "content": {
        "title": "Survey",
        "text": "Your feedback is important! Please share your valuable feedback.",
        "attachment": {
            "type": "SURVEY",
            "title": "Survey_title",
            "description": "desc_survey",
            "disableManualResponse": true,
            "postSubmitTitle": "Thanks",
            "screenReaderLabel": "screen_reader",
            "surveyButton": {
                "id": "85f7cfd8-4d01-454f-9092-e822c40f61ca",
                "title": "Open Survey_now"
            },
            "postSubmit": {
                "id": "2c611be3-4279-443b-bc80-4c84219195f3",
                "title": "Done"
            },
            "showSubmittedContent": true
        }
    },
    "taxonomy": {
        "campaignId": "66000002_5947",
        "clientCustomProperties": {},
        "partnerCustomProperties": {}
    },
    "inReplyToMessageId": "ACCOUNT_66127966_1770904503130_SPRINKLR_LIVE_CHAT_313_698ddbb7c720c33b56ab3438",
    "toProfile": {
        "channelType": "SPRINKLR_LIVE_CHAT",
        "channelId": "686ce4bdbfc4fe3077951a3c",
        "screenName": "Udyan_20.10"
    }
}'
 

     
     
 

#### Example - Response



{
    "data": [
        "POST_3119636127"
    ],
    "errors": []
}
 

     
     
   

### SECURE_FORM

#### Example - Request



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountId": 66001821,
    "scheduleDate": 0,
    "content": {
        "attachment": {
            "type": "SECURE_FORM",
            "form": {
                "formTitle": "title_of_secure_form",
                "fields": [
                    {
                        "name": "Email_check_label",
                        "type": "EMAIL"
                    }
                ]
            },
            "submit": {
                "title": "Submit",
                "actionDetail": {
                    "postBackHandlerType": "SECURE_FORM_POST_BACK",
                    "action": "POST_BACK"
                }
            }
        }
    },
    "taxonomy": {
        "campaignId": "66000002_5947"
    },
    "inReplyToMessageId": "ACCOUNT_66127966_1770904503130_SPRINKLR_LIVE_CHAT_313_698ddbb7c720c33b56ab3438",
    "toProfile": {
        "channelType": "SPRINKLR_LIVE_CHAT",
        "channelId": "686ce4bdbfc4fe3077951a3c",
        "screenName": "Udyan_20.10"
    }
}'
 

     
     
 

#### Example - Response



{
    "data": [
        "POST_3119636127"
    ],
    "errors": []
}
 

     
     
   

### RICH_TEXT_CAROUSEL

#### Example - Request



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountId": 66001821,
    "content": {
        "attachment": {
            "type": "RICH_TEXT_CAROUSEL",
            "disableManualResponse": true,
            "cardAttachmentList": [
                {
                    "type": "CARD",
                    "title": "CARD 1st Option",
                    "previewImageUrl": "",
                    "buttons": [
                        {
                            "id": "1234",
                            "title": "Button 1",
                            "subtitle": "",
                            "payload": "",
                            "actionDetail": {
                                "action": "TEXT"
                            }
                        }
                    ]
                },
                {
                    "type": "CARD",
                    "title": "Card 2nd Option",
                    "previewImageUrl": "",
                    "buttons": [
                        {
                            "id": "8907",
                            "title": "Button3",
                            "subtitle": "",
                            "payload": "",
                            "actionDetail": {
                                "action": "TEXT"
                            }
                        }
                    ]
                }
            ],
            "screenReaderLabel": "Rich_text"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_5947",
        "clientCustomProperties": {},
        "partnerCustomProperties": {}
    },
    "inReplyToMessageId": "ACCOUNT_66127966_1770904503130_SPRINKLR_LIVE_CHAT_313_698ddbb7c720c33b56ab3438",
    "toProfile": {
        "channelType": "SPRINKLR_LIVE_CHAT",
        "channelId": "686ce4bdbfc4fe3077951a3c",
        "screenName": "Udyan_20.10"
    }
}'
 

     
     
 

#### Example - Response



{
    "data": [
        "POST_3119636127"
    ],
    "errors": []
}
 

     
     
   

	[](https://dev.sprinklr.com/sprinklr-live-chat-templates) 

 

 
[Back to top](https://dev.sprinklr.com/sprinklr-live-chat-templates)
