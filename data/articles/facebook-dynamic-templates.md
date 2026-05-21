---
title: "Facebook Dynamic Templates"
slug: facebook-dynamic-templates
url: https://dev.sprinklr.com/facebook-dynamic-templates
---

# Facebook Dynamic Templates

#
POST Facebook Dynamic Templates

You can use this API to publish quick replies on supported social and messaging channels. Within the Request Parameters you will find the fields that you can pass in API payload while calling the API. Once you make a successful call you will get the Post Id of the published message. The API samples for different channel types are given below:


**Dev Notes: **This API enhancement strictly works for ` "channelType": "FACEBOOK"`.

Currently, the API supports the following three Facebook template types:

- **Quick Reply**: This templates helps send in-conversation buttons along with a thumbnail image (optional). You can request text reply from the user. The button selected by the user is then posted back as their reply.

- **Question with Answers (Button Template)**: This template helps send a question and corresponding answers in the form of buttons. The user can select the most suitable answer from the list of given buttons.

- **Multiple Products (Carousel) Template**: This template allows publishing template with carousel and corresponding buttons for each of the items.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/message

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
















































































































































































| Parameters | Sub Parameters | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| accountId |  |  | Required | array of account ids to schedule message to | Integer |
| content |  |  | Required |  |  |
|  | title |  | Optional | Title of the message. | String |
|  | text |  | Optional | Text of the message. | String |
|  | attachment |  | Required | Type of attachment with respect to the template type.Kindly find the attachment object descriptions below for the respective template type. | Object |
| taxonomy |  |  | Required | Object containing taxonomy details. |  |
|  | campaignId |  | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties |  | Optional | client custom properties for the message | String |
|  | partnerCustomProperties |  | Optional | partner custom properties for the message | String |
|  | tags |  | Optional | Tags to be added to the message | String |
|  | urlShortenerId |  | Optional | Url shortner identifier to apply to the message | String |
| inReplyToMessageId |  |  | Required | The message id on which the reply is being sent | String |
| scheduleDate |  |  | Optional | Schedule date for the message | Epoch (Milliseconds) |
| approval |  |  | Optional |  |  |
|  | type |  | Optional | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE ] | String |
|  | id |  | Optional | Value for the chosen approval type. | String |
| toProfile |  |  | Required | Current version of the message. | Integer |
|  | channelType |  | Required | Channel Type of the profile | String |
|  | channelId |  | Required | Channel Id of the profile | String |
|  | screenName |  | Required | Screen name of the profile | String |

## Quick Replies Attachment Object Description Table






































``



| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | QUICK_REPLY | String |
| message |  | Optional | Refers to the message you want to send in the template | String |
| quickReplies |  | Required | Array containing the quick reply details | Array |
|  | title | Required | Refers to the title of the button | String |
|  | subtitle | Optional | Refers to the subtitle of button. | String |
|  | imageUrl | Optional | Refers to the image url you want to send along with quick reply | Url |
|  | actionDetail | Required | In case of  QUICK_REPLY the possible action is:  "actionDetail" : {               "action" : "TEXT"             } | Object |

## Question with Answers Attachment Object Description Table



















-
-

****

| Parameters | Sub Parameters | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| type |  |  | Required | BUTTON_TEMPLATE | String |
| elementList |  |  | Required | Array containing the list of items in the button template | Array |
|  | title |  | Required | Refers to the question you want to ask | string |
|  | elementList |  | Required | Array containing the buttons for the respective answers | Array |
|  |  | title | Required | Refers to the text for the first answer | String |
|  |  | url | OptionalRequired when actionType is “web_url” | Refers to the URL the answer would redirect to when the button is clicked | String |
|  |  | actionType | Required | Refers to the action type that should be performed when the user clicks on the buttonSupported actionType:web_urlno_action | String |
|  |  | type | Optional | Refers to the type of answer formatExample: text | String |

## Multiple Products (Carousel) Attachment Object Description Table






















































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | CAROUSEL | String |
| cardAttachmentList |  | Required | The list containing details for all the items in the carousel | Array |
|  | type | Required | Refers to the type of attachment, i.e., CARD in this case | String |
|  | title | Required | Refers to the title of the item in the carousel | String |
|  | description | Required | Refers to the description of the item in the carousel | String |
|  | previewImageUrl | Required | The image URL of the item in the carousel | String |
|  | buttons | Required | An array of buttons to append to the carousel.Refer to the table below for button array parameters' description | Array |

### Button Array Description Table




























| Parameters | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| title |  | Required | Refers to the title of button | String |
| actionDetail |  | Required | Object containing the action details that need to be performed once the user clicks on the button | Object |
|  | action | Required | Refers to the action that will be performed once the user clicks on the buttonPossible actions for carousel post include: OPEN_URL, POST_BACK | String |
|  | url | OptionalRequired if the action type is OPEN_URL | Refers to the URL the user needs to be redirected to when they click on the button | String |
|  | data | OptionalRequired if the action type is TEXT | Refers to the text you want to display once the user clicks on the button | String |

## Example 1: Publish Quick Reply Template

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountId": 600001490,
    "content": {
        "text": "FB replying 01",
    "attachment": {
        "type": "QUICK_REPLY",
        "message": "Sports",
        "quickReplies": [
            {
                "title": "Cricket",
                "subtitle": "Flower",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/510adab7-9d1f-4fb1-83d4-56d28615c36a-738970249/headline_firstimage11_p.jpg",
                "actionDetail": {
                    "action": "TEXT"
                }
            }
        ]
    }
    },
    "taxonomy": {
        "campaignId": "4_4041"
    },
    "inReplyToMessageId": "ACCOUNT_600001490_1632369029837_FACEBOOK_38_m_aJdkZiqkpy06rf1WYB7Kcm9MHfoQTXbiSGK3P7q073mh7no0RqvmSX5c1MTUFtHEOGQrzaAeh0Iy1ZcFCzsSEA",
    "toProfile": {
        "channelType": "FACEBOOK",
        "channelId": "2964116967457583",
        "screenName" : "Sanity Test"
    }
}'
 

     
     
   

## Example - Response





{
    "data": [
        "POST_600000006300138"
    ],
    "errors": []
}
 

     
     
   
 

## Example 2: Publish Question with Answers Template

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "inReplyToMessageId": "ACCOUNT_473209_1683975928000_FACEBOOK_39_m_XQcYwfJFL8R_VUczEimxzAIyztlWnuT6EVnspd1zZpQY5n3NZfYAbTygkoJvbpmdmfZF2QNDEvdnjaP8zvTq3g",
    "accountId": 473209,
    "content": {
        "attachment": {
            "type": "BUTTON_TEMPLATE",
            "elementList": [
                {
                    "title": "What is your Favorite Channel?",
                    "elementList": [
                        {
                            "title": "Option 1",
                            "url": "https://www.google.com",
                            "actionType": "web_url",
                            "type": "text"
                        },
                        {
                            "title": "Option 2",
                            "url": "https://www.google.com",
                            "actionType": "web_url",
                            "type": "text"
                        },
                        {
                            "title": "Option 3",
                            "url": "https://www.google.com",
                            "actionType": "web_url",
                            "type": "text"
                        }
                    ]
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "4706_11345"
    },
    "toProfile": {
        "channelType": "FACEBOOK",
        "channelId": "3625508374175097"
    },
    "approval": {}
}'
 

     
     
 

## Example - Response





{
    "data": [
        "POST_600000006300139"
    ],
    "errors": []
}
 

     
     
   
 

## Example 3: Publish Carousel with Buttons

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "inReplyToMessageId": "ACCOUNT_1000123885_1683042814000_FACEBOOK_38_m_6wh1YCmZChg7C58skWbr-gP4HMIYYTGsbnEOZ3GiiASY9x_y8BsTDgw03hUgVbU1FYHq0BAf3HazF5GkbAjqPQ",
    "accountId": 1000123885,
    "content": {
        "attachment": {
            "type": "CAROUSEL",
            "cardAttachmentList": [
                {
                    "type": "CARD",
                    "title": "CARD 1",
                    "description": "CARD description",
                    "previewImageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
                    "buttons": [
                        {
                            "title": "button 1",
                            "actionDetail": {
                                "action": "OPEN_URL",
                                "url": "http://www.google.com"
                            }
                        }
                    ]
                },
                {
                    "type": "CARD",
                    "title": "CARD 2",
                    "description": "CARD description 2",
                    "previewImageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
                    "buttons": [
                        {
                            "title": "button 1",
                            "actionDetail": {
                                "url": "http://www.google.com",
                                "action": "OPEN_URL"
                            }
                        }
                    ]
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "1000004509_1653"
    },
    "toProfile": {
        "channelType": "FACEBOOK",
        "channelId": "5803051299812515",
        "screenName": "Test User"
    },
    "approval": {}
}'
 

     
     
   

## Example - Response





{
    "data": [
        "POST_600000006300140"
    ],
    "errors": []
}
 

     
     
   
 


**Dev Notes: **You can use [Read Post by Post Id](https://dev.sprinklr.com/read-post-by-post-ids) API to fetch the post details or you can also search the Post Id in the Universal Search Option on Sprinklr Platform's home page.

	[](https://dev.sprinklr.com/facebook-dynamic-templates) 

 

 
[Back to top](https://dev.sprinklr.com/facebook-dynamic-templates)
