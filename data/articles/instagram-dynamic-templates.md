---
title: "Instagram Dynamic Templates"
slug: instagram-dynamic-templates
url: https://dev.sprinklr.com/instagram-dynamic-templates
---

# Instagram Dynamic Templates

#
POST Instagram Dynamic Templates

	You can use this API to publish dynamic template on Instagram. Within the Request Parameters you will find the fields that you can pass in API payload while calling the API. Once you make a successful call you will get the Post Id of the published message.


**Dev Notes: **This API enhancement strictly works for ` "channelType": "INSTAGRAM"`.

  Supported Dynamic Templates :`Quick Replies` and `Carousel`

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |


##  Request Parameters

The API request payload would be same other than the ` attachment object` that will be different for Quick Reply and Carousel. The API attachment object samples for both dynamic templates are given below:

- Instagram Quick Replies

- Instagram Carousel
























































































































































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountId |  | Required | The account id to schedule/sent message. | Integer |
| content |  | Required | The object containing content details. | Object |
|  | attachment | Required | The attachment object contains the details of the attachment for QUICK_REPLY and CAROUSEL. For more details, check Attachment Description Table below. | String |
| scheduleDate |  | Optional | The schedule date for the message. | Integer |
| taxonomy |  | Required | The object containing taxonomy details. | Object |
|  | campaignId | Required | The unique campaign identifier to associate the message. | String |
|  | clientCustomProperties | Optional | The client custom properties for the message. | String |
|  | partnerCustomProperties | Optional | The partner custom properties for the message. | String |
|  | tags | Optional | Tags to be added to the message. | String |
|  | urlShortenerId | Optional | The URL shortner identifier to apply to the message. | String |
| inReplyToMessageId |  | Required | The message id on which the reply is being sent. | String |
| approval |  | Optional | The object containing approval details. | Object |
|  | type | Optional | Type of approval to process. defaults to NONE 			Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE ]. | String |
|  | id | Optional | Value for the chosen approval type. | String |
| toProfile |  | Required | The object containing profile details of the user to whom you are replying. | Object |
|  | channelType | Required | Channel Type of the profile. | String |
|  | channelId | Required | Channel Id of the profile. | String |
|  | screenName | Required | Name of the profile. | String |

###  Quick Replies:



### Attachment Description Table












































```

```




| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| message |  | Required | The message to display above quick reply. | String |
| type |  | Required | The type of attachment i.e. QUICK_REPLY. | String |
| quickReplies |  | Required | An array of objects. | Array |
|  | title | Required | Text to display within quick reply. | String |
|  | actionDetails | Required | The object containing click action details.              "actionDetail": {                         "action": "TEXT"                     } | object |

## Example: Quick Reply

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountId": 1171002,
    "content": {
        "attachment": {
            "message": "Quick reply text",
            "type": "QUICK_REPLY",
            "quickReplies": [
                {
                    "title": "quick reply title 1",
                    "actionDetail": {
                        "action": "TEXT"
                    }
                },
                {
                    "title": "quick reply title 2",
                    "actionDetail": {
                        "action": "TEXT"
                    }
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "4706_750"
    },
    "allowDuplicateMessages": true,
    "inReplyToMessageId": "ACCOUNT_1171002_1644480334000_INSTAGRAM_320_aWdfZAG1faXRlbToxOklHTWVzc2FnZA2Njg0MTcxMDMwMDk0OTEyODI0NTg0Mzg1OTc1MTk5MUlEOjE3ODQxNDUwODEwMzAzMTcyOjM0MDI4MjMjozMDMzNTMwNzg2MzIyMDQxNTYxNTgyOTc1NjYwMjIyMDU0NAZDZD",
    "toProfile": {
        "screenName": "XYZ",
        "channelType": "INSTAGRAM",
        "channelId": "5116428976785642"
    },
    "approval": {}
}'
 

     
     
   

## Example - Response

 
 
     

{
    "data": [
        "POST_6311894861"
    ],
    "errors": []
}
 

     
     
   
 

## Carousel:

### Attachment Description Table






























































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| Type |  | Required | The type of attachment i.e. CAROUSEL | String |
| CardAttachmentList |  | Required | The list of images/cards in a carousel | Array |
|  | Type | Required | The type of attachment | String |
|  | Title | Required | The title of the attachment | String |
|  | Description | Required | The description of the attachment | String |
|  | previewImageUrl | Required | The URL of the attachment | String |
|  | Buttons | Required | An array of buttons to append to the carousel. | Array |


### Button Array Description




















`
`




| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Title | Required | Title of button | String |
| ActionDetail | Required | In case of  CAROUSEL post the possible action is:  "actionDetail" : {               "action" : "TEXT","Data ": "TEXT_POST_BACK"      } | Object |


## Example: Carousel

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountId": 1171002,
  "content": {
        "attachment": {
            "type": "CAROUSEL",
            "cardAttachmentList": [
                {
                    "type": "CARD",
                    "title": "CARD 1",
                    "description": "CARD description",
                    "previewImageUrl": "https://qa4-cdata-secure.sprinklr.com/DAM/400002/2ab9bde4-781c-4d4b-ae75-733bdad77daf-1032962294/GULFSTREAM-450-EXTERIOR-FINAL-_p.jpg",
                    "buttons": [
                        {
                            "title": "button 1",
                            "actionDetail": {
                                "action": "TEXT",
                                 "data": "TEXT_POST_BACK"
                            }
                        }
                    ],
                    "defaultButton": {
                        "actionDetail": {
                            "url": "http://www.google.com",
                            "action": "OPEN_URL"
                        }
                    }
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
                                "action": "TEXT",
                                 "data": "TEXT_POST_BACK"
                            }
                        }
                    ],
                    "defaultButton": {
                        "actionDetail": {
                            "url": "http://www.google.com",
                            "action": "OPEN_URL"
                        }
                    }
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "4706_750"
    },
    "allowDuplicateMessages": true,
    "inReplyToMessageId": "ACCOUNT_1171002_1644480334000_INSTAGRAM_320_aWdfZAG1faXRlbToxOklHTWVzc2FnZA2Njg0MTcxMDMwMDk0OTEyODI0NTg0Mzg1OTc1MTk5MUlEOjE3ODQxNDUwODEwMzAzMTcyOjM0MDI4MjMjozMDMzNTMwNzg2MzIyMDQxNTYxNTgyOTc1NjYwMjIyMDU0NAZDZD",
    "toProfile": {
        "screenName": "XYZ",
        "channelType": "INSTAGRAM",
        "channelId": "5116428976785642"
    },
    "approval": {}
}'
 

     
     
 

## Example - Response

 
 
     
 
{
    "data": [
        "POST_6311898541"
    ],
    "errors": []
}
 

     
     
   
 

[](https://dev.sprinklr.com/instagram-dynamic-templates) 

 

 
[Back to top](https://dev.sprinklr.com/instagram-dynamic-templates)
