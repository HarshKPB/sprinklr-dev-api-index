---
title: "Apple Business Chat Templates"
slug: apple-business-chat-templates
url: https://dev.sprinklr.com/apple-business-chat-templates
---

# Apple Business Chat Templates

#
POST Apple Business Chat Templates


You can use this API to publish dynamic templates on Apple Business Chat.

- **Rich Link**

- **List Picker**

- **Text/Link**

- **Authentication**

- **Quick Reply**

- **Time Picker**

- **iMessage**

- **Apple Pay**

- **Form**

**Dev Notes: **This API enhancement strictly works for "channelType": `"APPLE_BUSINESS_CHAT"`

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
|  | attachment |  | Required | The attachment object contains the details of the attachment for LIST PICKER and CARD. For more details, check Attachment Description Table below. | String |
| scheduleDate |  |  | Required | Schedule date for the message | Integer |
| taxonomy |  |  | Required | Object containing taxonomy details. |  |
|  | campaignId |  | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties |  | Optional | client custom properties for the message | String |
|  | partnerCustomProperties |  | Optional | partner custom properties for the message | String |
|  | tags |  | Optional | Tags to be added to the message | String |
|  | urlShortenerId |  | Optional | Url shortner identifier to apply to the message | String |
| inReplyToMessageId |  |  | Required | The message id on which the reply is being sent | String |
| approval |  |  | Optional |  |  |
|  | type |  | Optional | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE ] | String |
|  | id |  | Optional | Value for the chosen approval type. | String |
| toProfile |  |  | Required | Current version of the message. | Integer |
|  | channelType |  | Required | Channel Type of the profile | String |
|  | channelId |  | Required | Channel Id of the profile | String |
|  | screenName |  | Optional | The user's screen name on the channel | String |

### Attachment Description Table: RICH LINK







































``




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| link | Optional | Refers to the link where the user will be redirected | Url |
| title | Optional | Refers to the title of the template | String |
| mediaUrl | Required | Refers to the media URL | Url |
| previewUrl | Optional | Refers to the preview media URL | String |
| type | Required | Refers to the type of link.Default: RICH_LINK | String |

### Attachment Description Table: LIST_PICKER


























****

****

| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| multipleSelection |  | Required | If true, multiple selections will be permissible for the attachment | Boolean |
| sections |  | Required | Refers to the array defining section details | Array |
|  | title | Required | Refers to the title of the section | String |
|  | multipleSelection | Required | If true, multiple selections will be permissible for the section | Boolean |
|  | items | Required | Array containing the item details in the sectionRefer to the table below for Items array description | Array |
| receivedMessage |  | Required | Object containing the received message details | Object |
|  | title | Optional | Refers to the title of the received message | String |
|  | style | Optional | Refers to the style of the message.Supported Values: icon, small, large | String |
|  | imageUrl | Optional | Refers to the image url of the received message | Url |
| replyMessage |  | Required | Object containing the reply message details | Object |
|  | title | Optional | Refers to the title of the reply message | String |
|  | style | Optional | Refers to the style of the message.Supported Values: icon, small, large | String |
|  | imageUrl | Optional | Refers to the image url of the reply message | Url |

### Items Array Description Table












****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| title | Optional | Refers to the title of the item | String |
| style | Optional | Refers to the style of the itemSupported Values: icon, small, large | String |
| imageUrl | Optional | Refers to the image url of the item | Url |

### Attachment Description Table: TEXT/LINK












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| text | Required | Refers to the text or the link of the message | String |

### Attachment Description Table: Authentication













| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of the template | String |
|  |  | Optional | Refers to the unique identifier for the social login app | String |
| additionalParameters |  | Optional | Object defining additional parameters (if any) | Object |
| scope |  | Optional | Refers to the list defining the scope of the authentication | List [String] |
| receivedMessage |  | Optional | Object defining the received message details | Object |
|  | title | Optional | Refers to the tile of the received message | String |
|  | subTitle | Optional | Refers to the sub title of the received message | String |
|  | secondarySubtitle | Optional | Refers to the secondary sub title of the received message | String |
|  | tertiarySubtitle | Optional | Refers to the tertiary sub title of the received message | String |
|  | imageUrl | Optional | Refers to the url of the image attachment | Url |
| replyMessage |  | Optional | Object defining the reply message details | Object |
|  | title | Optional | Refers to the title of the reply message | String |
|  | subTitle | Optional | Refers to the sub title of the reply message | String |
|  | secondarySubtitle | Optional | Refers to the secondary sub title of the reply message | String |
|  | tertiarySubtitle | Optional | Refers to the tertiary sub title of the reply message | String |
|  | imageurl | Optional | Refers to the url of the image attachment | Url |

### Attachment Description Table: Quick Reply













| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the template type | String |
| message |  | Required | Refers to the message of the template | String |
| quickReplies |  | Refers to the array defining the quick reply details.You can add two to five customizable choices and the user can select only one from the list | Required | Array |
|  | id | Optional | Refers to the unique identifier for the quick reply | String |
|  | title | Required | Refers to the title of the quick reply | String |
|  | actionDetail | Required | Object defining the action details:{                      "action": "TEXT"} | Object |

### Attachment Description Table: Time Picker













-
-
-

-
-
-

| Parameter | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| receivedMessage |  | Optional | Object defining the received message details | Object |
|  | title | Optional | Refers to the title of the message | String |
|  | subTitle | Optional | Refers to the sub title of the message | String |
|  | secondarySubtitle | Optional | Refers to the secondary title of the message | String |
|  | tertiarySubtitle | Optional | Refers to the tertiary title of the message | String |
|  | style | Optional | Refers to the style of the messageSupported values:Icon (40 X 40)Small (60 X 60)Large (263 X150) | String |
|  | imageUrl | Optional | Refers to the url of the image | Url |
| replyMessage |  | Required | Object defining the reply message details | Object |
|  | title | Optional | Refers to the title of the message | String |
|  | subtitle | Optional | Refers to the sub title of the message | String |
|  | secondarySubtitle | Optional | Refers to the secondary title of the message | String |
|  | tertiarySubtitle | Optional | Refers to the tertiary title of the message | String |
|  | style | Optional | Refers to the style of the messageSupported values:Icon (40 X 40)Small (60 X 60)Large (263 X150) | String |
|  | imageurl | Optional | Refers to the url of the image | Url |
| location |  | Optional | Object defining the location details | Object |
|  | latitude | Optional | Refers to the latitude configuration | number |
|  | longitude | Optional | Refers to the longitude configuration | number |
|  | radius | Optional | Refers to the radius configuration | number |
|  | title | Optional | Refers to the location title | String |
| timeSlots |  | Optional | Array defining the time slot details | Array |
|  | startTime | Optional | Refers to the start time of the event | Integer |
|  | duration | Optional | Refers to the duration of the event | Integer |
| timezone |  | Optional | Refers to the time zone of the event | String |
| title |  | Optional | Refers to the title of the event | String |
| type |  | Required | Refers to the type of the event |  |

### Attachment Description Table: iMessage













-
-
-

-
-
-

| Parameter | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required |  | String |
| appId |  | Optional | Refers to the application Id | String |
| appName |  | Optional | Refers to the app name | String |
| bId |  | Optional |  | String |
| url |  | Optional | Refers to the base url of the imessage | Url |
| useLiveLayout |  | Optional | If yes, the template shows the live app layout in the message | Boolean |
| attachments |  | Required | Refers to the array of attachments associated with the message | Array |
|  | type | Required | Refers to the type of attachment | String |
|  | url | Required | Refers to the url of the attachment | Url |
|  | title | Optional | Refers to the title of the attachment | String |
|  | description | Optional | Refers to the description of the attachment | String |
| receivedMessage |  | Optional | Object containing the received message details | Object |
|  | title | Optional | Refers to the title of the received message | String |
|  | subTitle | Optional | Refers to the sub title of the received message | String |
|  | style | Optional | Refers to the style of the messageSupported values:Icon (40 X 40)Small (60 X 60)Large (263 X150) | String |
|  | imageUrl | Optional | Refers to the url of the image | Url |
| replyMessage |  | Optional | Object containing the reply message details | Object |
|  | title | Optional | Refers to the title of the reply message | String |
|  | subTitle | Optional | Refers to the sub title of the reply message | String |
|  | style | Optional | Refers to the style of the messageSupported values:Icon (40 X 40)Small (60 X 60)Large (263 X150) | String |
|  | imageurl | Optional | Refers to the url of the image | Url |

### Attachment Description Table: APPLE PAY













-
-
-

| Parameter | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| receivedMessage |  | Optional | Object defining the received message details | Object |
|  | imageUrl | Optional | Refers to the image url of the received message | Url |
|  | title | Optional | Refers to the title of the received message | String |
| replyMessage |  | Optional | Object defining the reply message details | Object |
|  | style | Optional | Refers to the style of the messageSupported values:Icon (40 X 40)Small (60 X 60)Large (263 X150) | String |
|  | title | Optional | Refers to the title of the reply message | String |
| paymentRequest |  | Required | Object defining the payment request details | Object |
|  | lineItems | Optional | Array defining the line item details | Array |
|  | total | Optional | Object defining the total details | Object |
|  | countryCode | Optional | Refers to the country code | String |
|  | currencyCode | Optional | Refers to the currency code | String |
|  | requiredBillingContactFields | Optional | List defining the billing contact details | List [String] |
|  | requiredShippingContactFields | Optional | List defining the shipping contact details | List [String] |
|  | supportedCountries | Optional | List defining the supported country details | List [String] |
|  | shippingMethods | Optional | Array defining the shipping method details | Array |
|  | applePay | Optional | Object defining apple pay details | Object |
|  | type | Required | Refers to the template type | String |
|  | paymentAccountId | Optional | Refers to the account id to which the payment needs to be sent |  |

### Total Object Details












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| amount | Optional | Refers to the total amount of line items | Integer |
| label | Optional | Refer to the label of the total | String |
| type | Optional | Refers to the total type | String |

### Attachment Description Table: Form













-
-
-

-
-
-

| Parameter | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| messageTitle |  | Optional | Refers to the title of the message | String |
| messageSubtitle |  | Optional | Refers to the subtitle of the message | String |
| buttonTitle |  | Optional | Refers to the title of the button | String |
| form |  | Required | Refers to the object containing the form details | Object |
|  | formTitle | Optional | Refers to the title of the form | String |
|  | repeatable | Optional | If true, the form is repeatable | Boolean |
|  | minCount | Optional | Refers to the minimum count of the form | Integer |
|  | maxCount | Optional | Refers to the maximum count of the form | Integer |
|  | fields | Optional | Refers to the array defining the form fields.Refer to the table below for the array details | Array |
| submit |  | Required | Object Defining the submit button details | Object |
|  | title | Optional | Refers to the title of the submit button | String |
| showSummary |  | Optional | If true, the summary of the message is form responses in shown | Boolean |
| receivedMessage |  | Optional | Object defining the received message details | Object |
|  | title | Optional | Refers to the title of the message | String |
|  | subTitle | Optional | Refers to the subtitle of the message | String |
|  | style | Optional | Refers to the style of the messageSupported values:Icon (40 X 40)Small (60 X 60)Large (263 X150) | String |
|  | imageUrl | Optional | Refers to the url of the image | Url |
| replyMessage |  | Optional | Object defining the reply message details | Object |
|  | title | Optional | Refers to the title of the reply message | String |
|  | subTitle | Optional | Refers to the sub title of the reply message | String |
|  | style | Optional | Refers to the style of the messageSupported values:Icon (40 X 40)Small (60 X 60)Large (263 X150) | String |
|  | imageUrl | Optional | Refers to the url of the image | Url |
| type |  | Required | Refers to the type of template | string |

### fields Array Description Table













****````````

| Parameter | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Optional | Refers to the name of the field | String |
| description |  | Optional | Refers to the description of the field | String |
| type |  |  | Refers to the type of the templateSupported Values: Form, Date Picker, Picker, Select | String |
| picklistValues |  | Optional | Refers to the array defining the picklist details | Array |
|  | label | Optional | Refers to the label of the picklist value | String |
|  | value | Optional | Refers to the value of the picklist | String |
| parentChild |  | Optional | If true, the field has a parent child hierarchy | Boolean |
| multiValued |  | Optional | If true, the fields support multiple values | Boolean |
| defaultValue |  | Optional | Refers ton the default value of the field (if any) | String |
| additional |  | Optional | Object containing additional details if any | Object |
|  | maximumDate | Optional | The date till when the field will be available | String |
|  | minimumDate | Optional | The starting time from when the field will be available | String |
|  | dateFormat | Optional | The format of the date | String |

### Example: RICH LINK














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "inReplyToMessageId": "ACCOUNT_600001079_1619085773531_APPLE_BUSINESS_CHAT_317_41b4222d-011b-41aa-a489-f00c6528249c",
    "accountId": 600001079,
    "content": {
        "attachment": {
            "link": "www.google.com",
            "title": "asdas",
            "mediaUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/3334323b-8aaf-4905-9ba8-23804c68b712-1857956781.gif",
            "previewUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/3334323b-8aaf-4905-9ba8-23804c68b712-1857956781.gif",
            "type": "RICH_LINK"
        }
    },
    "taxonomy": {
        "campaignId": "6_-98"
    },
    "toProfile": {
        "channelType": "APPLE_BUSINESS_CHAT",
        "channelId": "urn:mbid:AQAAY3RBepJ6tIWXKLmZBmqUKb6ZYfAdFGI3AEtusg5jrUSYksuK3QeD/MfYLjHDXvv01gfVZDoUKXCObgRsb0HeLHuQz+CiKI4yk/GoAWIPEbJHtJX1Qs/inhySc/XklecIWi4qfcjAyWgzaGtZyaPIJXPxm0Y=",
        "screenName": "Apple User 24"
    },
    "approval": {}
}'





## Example - Response





{
    "data": [
        "POST_3329636297"
    ],
    "errors": []
}





### Example: LIST_PICKER














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "inReplyToMessageId": "ACCOUNT_600001079_1619085773531_APPLE_BUSINESS_CHAT_317_41b4222d-011b-41aa-a489-f00c6528249c",
    "accountId": 600001079,
    "content": {
        "text":"List picker new msg",
        "attachment": {
            "multipleSelection": false,
            "sections": [
                {
                    "title": "as",
                    "multipleSelection": true,
                    "items": [
                        {
                            "title": "asd",
                            "style": "small",
                            "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/3334323b-8aaf-4905-9ba8-23804c68b712-1857956781.gif"
                        }
                    ]
                }
            ],
            "receivedMessage": {
                "title": "asd",
                "style": "small",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/3334323b-8aaf-4905-9ba8-23804c68b712-1857956781.gif"
            },
            "replyMessage": {
                "title": "asd",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/3334323b-8aaf-4905-9ba8-23804c68b712-1857956781.gif",
                "style": "icon"
            },
            "type": "LIST_PICKER"
        }
    },
    "taxonomy": {
        "campaignId": "6_-98"
    },
    "toProfile": {
        "channelType": "APPLE_BUSINESS_CHAT",
        "channelId": "urn:mbid:AQAAY3RBepJ6tIWXKLmZBmqUKb6ZYfAdFGI3AEtusg5jrUSYksuK3QeD/MfYLjHDXvv01gfVZDoUKXCObgRsb0HeLHuQz+CiKI4yk/GoAWIPEbJHtJX1Qs/inhySc/XklecIWi4qfcjAyWgzaGtZyaPIJXPxm0Y=",
        "screenName": "Apple User 24"
    },
    "approval": {}
}'





## Example - Response





{
    "data": [
        "POST_3329638977"
    ],
    "errors": []
}





### Example: TEXT/LINK














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
     "inReplyToMessageId": "ACCOUNT_600001079_1619085773531_APPLE_BUSINESS_CHAT_317_41b4222d-011b-41aa-a489-f00c6528249c",
     "accountId": 600001079,
     "content": {
         "text":"https://www.youtube.com/"
     },
     "taxonomy": {
         "campaignId": "6_-98"
     },
     "toProfile": {
         "channelType": "APPLE_BUSINESS_CHAT",
         "channelId": "urn:mbid:AQAAY3RBepJ6tIWXKLmZBmqUKb6ZYfAdFGI3AEtusg5jrUSYksuK3QeD/MfYLjHDXvv01gfVZDoUKXCObgRsb0HeLHuQz+CiKI4yk/GoAWIPEbJHtJX1Qs/inhySc/XklecIWi4qfcjAyWgzaGtZyaPIJXPxm0Y=",
         "screenName": "Apple User 24"
     },
     "approval": {}
 }'





## Example - Response





{
    "data": [
        "POST_3329608771"
    ],
    "errors": []
}





### Example: AUTHENTICATION














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
     "inReplyToMessageId": "ACCOUNT_600028667_1675417733748_APPLE_BUSINESS_CHAT_317_c23d7936-2f15-4eb5-ab30-d5a09bb2077b",
     "accountId": 600028667,
     "content": {
         "attachment": {
             "type": "AUTHENTICATION",
             "loginAppConfigId": "62ff0c3c5a2bf53a1bcf1bca",
             "additionalParameters":{},
             "scope": [
                     "scope1"
             ],
             "receivedMessage": {
                 "title": "title of Auth Temp",
                 "subtitle": "msg subtite",
                 "secondarySubtitle": "sec subtitle Auth Temp ",
                 "tertiarySubtitle": "ter subtitle msg",
                 "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/b400057d-5dfe-4ecf-86ee-85c05a7efe1d-1643163501/Alienware_Defy_Boundaries_2.0__p.jpg"
             },
             "replyMessage": {
                 "title": "title val Auth Temp",
                 "subtitle": "subtitle",
                 "secondarySubtitle": "sec subtitle",
                 "tertiarySubtitle": "ter subtitle",
                 "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/b400057d-5dfe-4ecf-86ee-85c05a7efe1d-1643163501/Alienware_Defy_Boundaries_2.0__p.jpg"
             }
         }
         },
     "taxonomy": {
         "campaignId": "6_-98"
     },
     "toProfile": {
         "channelType": "APPLE_BUSINESS_CHAT",
         "channelId": "urn:mbid:AQAAY8Aa3+Spi5oJR9cO4V69HgReZG2oOJHvjBjRM4TWJW+IFxLMKClh322LdBGwy9I9msHFHyT17PSUR9+WaRdpo0fmh9mq1mduAVUmdYDyfON23npvSOTXA9B9CvP43onOHnCidad+RdG7avJU7qEjLwWol9c=",
         "screenName": "Apple User 56"
     },
     "approval": {}
}'





## Example - Response





{
    "data": [
        "POST_600000019355335"
    ],
    "errors": []
}





### Example: QUICK REPLY














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountId": 600028667,
    "content": {
        "text": "Quick Reply Test3",
        "attachment": {
            "type": "QUICK_REPLY",
            "message": "Question 1",
            "quickReplies": [
                {
                    "id": "123",
                    "title": "Option 1",
                    "actionDetail": {
                        "action": "TEXT"
                   }
                }
        ]
        }
    },
    "taxonomy": {
        "campaignId": "6_-98"
    },
    "inReplyToMessageId": "ACCOUNT_600028667_1675850276305_APPLE_BUSINESS_CHAT_317_1693d544-c3a0-456f-b42c-54f46f5bbee5",
    "toProfile": {
        "channelType": "APPLE_BUSINESS_CHAT",
        "channelId": "urn:mbid:AQAAY8Aa3+Spi5oJR9cO4V69HgReZG2oOJHvjBjRM4TWJW+IFxLMKClh322LdBGwy9I9msHFHyT17PSUR9+WaRdpo0fmh9mq1mduAVUmdYDyfON23npvSOTXA9B9CvP43onOHnCidad+RdG7avJU7qEjLwWol9c=",
        "screenName": "Apple User 56"
    }
}'





## Example - Response





{
    "data": [
        "POST_600000019355337"
    ],
    "errors": []
}





### Example: TIME PICKER














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountId": 600028667,
    "content": {
        "text": "Time Picker",
        "attachment": {
            "receivedMessage": {
                "title": "Pick From Available Slots",
                "subtitle": "msg subtite",
                "secondarySubtitle": "sec subtitle Auth Temp ",
                "tertiarySubtitle": "ter subtitle msg",
                 "style": "large",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/510adab7-9d1f-4fb1-83d4-56d28615c36a-738970249/headline_firstimage11_p.jpg"
            },
            "replyMessage": {
                "secondarySubtitle": "sec subtitle",
                "tertiarySubtitle": "ter subtitle",
                 "style": "large",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/510adab7-9d1f-4fb1-83d4-56d28615c36a-738970249/headline_firstimage11_p.jpg"
            },
            "location": {
                "longitude": 0.001,
                "radius": 5000,
                "title": "BLR"
            },
            "timeslots": [
                {
                    "startTime": 1672755451528,
                    "duration": 0
                }
            ],
            "timezone": "Asia/Kolkata",
            "title": "Eevnt title",
            "type": "TIME_PICKER"
        }
    },
    "taxonomy": {
        "campaignId": "6_-98"
    },
    "inReplyToMessageId": "ACCOUNT_600028667_1675417733748_APPLE_BUSINESS_CHAT_317_c23d7936-2f15-4eb5-ab30-d5a09bb2077b",
    "toProfile": {
        "channelType": "APPLE_BUSINESS_CHAT",
        "channelId": "urn:mbid:AQAAY8Aa3+Spi5oJR9cO4V69HgReZG2oOJHvjBjRM4TWJW+IFxLMKClh322LdBGwy9I9msHFHyT17PSUR9+WaRdpo0fmh9mq1mduAVUmdYDyfON23npvSOTXA9B9CvP43onOHnCidad+RdG7avJU7qEjLwWol9c=",
        "screenName": "Apple User 56"
    }
}'





## Example - Response





{
    "data": [
        "POST_600000019355338"
    ],
    "errors": []
}





### Example: iMessage














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "inReplyToMessageId": "ACCOUNT_600028667_1675417733748_APPLE_BUSINESS_CHAT_317_c23d7936-2f15-4eb5-ab30-d5a09bb2077b",
    "accountId": 600028667,
    "content": {
        "text": "",
        "attachment": {
            "type": "APP_LINK",
            "appId": "123",
            "appName": "sampleApp",
            "bId": "com.apple.messages.MSMessageExtensionBalloonPlugin:{team-id}:{ext-bundle-id}",
            "url": "aa",
            "useLiveLayout": false,
            "attachments": [
                {
                    "type": "IMAGE",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/b400057d-5dfe-4ecf-86ee-85c05a7efe1d-1643163501/Alienware_Defy_Boundaries_2.0__p.jpg",
                    "title": "attachment title",
                    "description": "desc"
                }
            ],
            "receivedMessage": {
                "title": "testi1",
                "subtitle": "test1",
                "style": "large",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/510adab7-9d1f-4fb1-83d4-56d28615c36a-738970249/headline_firstimage11_p.jpg"
            },
            "replyMessage": {
                "title": "testi1",
                "subtitle": "test1",
                "style": "icon",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/b400057d-5dfe-4ecf-86ee-85c05a7efe1d-1643163501/Alienware_Defy_Boundaries_2.0__p.jpg"
            }
        }
    },
    "taxonomy": {
        "campaignId": "2_-98"
    },
    "toProfile": {
        "channelType": "APPLE_BUSINESS_CHAT",
        "channelId": "urn:mbid:AQAAY8Aa3+Spi5oJR9cO4V69HgReZG2oOJHvjBjRM4TWJW+IFxLMKClh322LdBGwy9I9msHFHyT17PSUR9+WaRdpo0fmh9mq1mduAVUmdYDyfON23npvSOTXA9B9CvP43onOHnCidad+RdG7avJU7qEjLwWol9c=",
        "screenName": "Apple User 56"
    },
    "approval": {}
}'





## Example - Response





{
    "data": [
        "POST_600000019755398"
    ],
    "errors": []
}





### Example: Apple Pay














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountId": 600028667,
    "content": {
        "attachment": {
            "receivedMessage": {
                "imageUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/a91ed3d8-5bfc-4847-bacf-bf1192deeda2-1350917364/https___prod0-media-proxy.spri_p.jpg",
                "title": "Payment"
            },
            "replyMessage": {
                "style": "icon",
                "title": "Pay Here"
            },
            "paymentRequest": {
                "lineItems": [
                    {
                        "label": "keyboard",
                        "amount": 50
                    }
                ],
                "total": {
                    "amount": 50,
                    "label": "",
                    "type": "final"
                },
                "countryCode": "US",
                "currencyCode": "USD",
                "requiredBillingContactFields": [
                    "postalAddress"
                ],
                "requiredShippingContactFields": [
                    "postalAddress"
                ],
                "shippingMethods": [
                    {
                        "amount": 50,
                        "label": "Ship"
                    }
                ],
                "applePay": {
                    "supportedNetworks": [
                        "masterCard"
                    ],
                    "merchantCapabilities": [
                        "supportsDebit"
                    ]
                }
            },
            "type": "APPLE_PAY",
            "paymentAccountId":"5c87581cc7f9c5183b60df87"
        }
    },
    "taxonomy": {
        "campaignId": "6_-98"
    },
   "inReplyToMessageId": "ACCOUNT_600028667_1675417733748_APPLE_BUSINESS_CHAT_317_c23d7936-2f15-4eb5-ab30-d5a09bb2077b",
    "toProfile": {
        "channelType": "APPLE_BUSINESS_CHAT",
        "channelId": "urn:mbid:AQAAY8Aa3+Spi5oJR9cO4V69HgReZG2oOJHvjBjRM4TWJW+IFxLMKClh322LdBGwy9I9msHFHyT17PSUR9+WaRdpo0fmh9mq1mduAVUmdYDyfON23npvSOTXA9B9CvP43onOHnCidad+RdG7avJU7qEjLwWol9c=",
         "screenName": "Apple User 56"
    }
}'





## Example - Response





{
    "data": [
        "POST_600000019777398"
    ],
    "errors": []
}





### Example: FORM














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "inReplyToMessageId": "ACCOUNT_600028667_1675417733748_APPLE_BUSINESS_CHAT_317_c23d7936-2f15-4eb5-ab30-d5a09bb2077b",
    "accountId": 600028667,
    "content": {
        "text": "",
        "attachment": {
            "messageTitle": "Message Title",
            "messageSubtitle": "messageSubtitle",
            "buttonTitle": "Click",
            "form": {
                "formTitle": "testForm",
                "repeatable": true,
                "minCount": 1,
                "maxCount": 10,
                "fields": [
                    {
                        "name": "fieldtest1",
                        "description": "firstdes1",
                        "type": "input",
                        "picklistValues": [
                            {
                                "label": "Click",
                                "value": "1"
                            }
                        ],
                        "parentChild": false,
                        "multivalued": false,
                        "defaultValue": "2023/02/03",
                        "additional": {}
                    }
                ]
            },
            "submit": {
                "title": "submit1"
            },
            "showSummary": true,
            "receivedMessage": {
                "title": "rMTitle",
                "subtitle": "rMSubtitle",
                "style": "icon",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/b400057d-5dfe-4ecf-86ee-85c05a7efe1d-1643163501/Alienware_Defy_Boundaries_2.0__p.jpg"
            },
            "replyMessage": {
                "title": "ReplyTitle",
                "subtitle": "ReplySubtitle",
                "style": "icon",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/b400057d-5dfe-4ecf-86ee-85c05a7efe1d-1643163501/Alienware_Defy_Boundaries_2.0__p.jpg"
            },
            "type": "FORM"
        }
    },
    "taxonomy": {
        "campaignId": "2_-98"
    },
    "toProfile": {
        "channelType": "APPLE_BUSINESS_CHAT",
        "channelId": "urn:mbid:AQAAY8Aa3+Spi5oJR9cO4V69HgReZG2oOJHvjBjRM4TWJW+IFxLMKClh322LdBGwy9I9msHFHyT17PSUR9+WaRdpo0fmh9mq1mduAVUmdYDyfON23npvSOTXA9B9CvP43onOHnCidad+RdG7avJU7qEjLwWol9c=",
        "screenName": "Apple User 56"
    },
    "approval": {}
}'





## Example - Response





{
    "data": [
        "POST_600000019777347"
    ],
    "errors": []
}





	[](https://dev.sprinklr.com/apple-business-chat-templates) 

 

 
[Back to top](https://dev.sprinklr.com/apple-business-chat-templates)
