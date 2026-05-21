---
title: "WhatsApp Dynamic Templates"
slug: whatsapp-dynamic-templates
url: https://dev.sprinklr.com/whatsapp-dynamic-templates
---

# WhatsApp Dynamic Templates

#
POST WhatsApp Dynamic Templates

You can use this API to publish dynamic templates across supported social and messaging channels. This page specifically lists WhatsApp templates that you can publish using the API. Each template type includes its own parameters and example payloads to help you construct and test your requests.

**Dev Notes: **This API enhancement strictly works for ` "channelType": "WHATSAPP_BUSINESS"`.

For WhatsApp, you can use this API to publish the following message types:



- [Publishing List Picker](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-list-picker)

- [Publishing Card](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card)

- [Publishing Card With Image](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-image)

- [Publishing Card With Video](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-video)

- [Publishing Card With Document](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-document)

- [Publishing Geolocation](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-geolocation)

- [Publishing Request Location Message](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-request-location-message)

- [Publishing Address Message](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-address-message)

- [Publishing CTA URL](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-cta-url)

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




































****
-
-
-
-
-
- [Attachment Description Tables](https://dev.sprinklr.com/whatsapp-dynamic-templates#attachment-type)

















































































****





































| Parameters | Sub Parameters | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| accountId |  |  | Required | The unique Id of the account added in the Sprinklr | Integer |
| content |  |  | Required |  |  |
|  | attachment |  | Required | Object containing attachment details.     Supported Types:            LIST_PICKER       CARD       GEO_LOCATION       REQUEST_LOCATION       ADDRESS       CTA_URL          For more details on the parameters of each attachment type, refer to the  below. | String |
| scheduleDate |  |  | Required | Schedule date for the message | Integer |
| taxonomy |  |  | Required | Object containing taxonomy details. |  |
|  | campaignId |  | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties |  | Optional | client custom properties for the message | String |
|  | partnerCustomProperties |  | Optional | partner custom properties for the message | String |
|  | tags |  | Optional | Tags to be added to the message | String |
|  | urlShortenerId |  | Optional | Url shortner identifier to apply to the message | String |
| inReplyToMessageId |  |  | Required | The message id on which the reply is being sent | String |
| approval |  |  | Optional |  |  |
|  | type |  | Optional | Type of approval to process. defaults to NONE 				 				Supported Values: ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE | String |
|  | id |  | Optional | Value for the chosen approval type. | String |
| toProfile |  |  | Required | Object containing profile details. | Object |
|  | channelType |  | Required | Channel Type of the profile | String |
|  | channelId |  | Required | Channel Id of the profile | String |

### Attachment Description Tables

Use the links below to navigate to the parameter tables for each attachment type.


- [LIST_PICKER](https://dev.sprinklr.com/whatsapp-dynamic-templates#list-picker-table)

- [CARD](https://dev.sprinklr.com/whatsapp-dynamic-templates#card-table)

- [GEO_LOCATION](https://dev.sprinklr.com/whatsapp-dynamic-templates#geolocation-table)

- [REQUEST_LOCATION](https://dev.sprinklr.com/whatsapp-dynamic-templates#request-location-table)

- [ADDRESS](https://dev.sprinklr.com/whatsapp-dynamic-templates#address-table)

- [CTA_URL](https://dev.sprinklr.com/whatsapp-dynamic-templates#cta-url-table)

#### LIST_PICKER















			``













```

```

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this message template, use LIST_PICKER. | String |
| header |  | Required | The object contains header test details | object |
|  | text | Required | The header text for list picker. | String |
| body |  | Required | The body text of list picker. | String |
| footerText |  | Required | The footer text of list picker. | String |
| buttonTitle |  | Required | The list picker button title. | String |
| sections |  | Required | The object containing the details of the list you want to send. | object |
|  | title | Required | The title of the list. | String |
|  | items | Required | The object contains the details of items    {   "id" : " ",   "title" : "",   "subtitle" : "" } | String |

See the [List Picker Example](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-list-picker).

#### CARD















			``










****











```

```





| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this message template, use CARD. | String |
| header |  | Required | The object contains header details. | Object |
|  | document/image/text | Required | Refers to the card details based on the card type.Refer to the image/video/document Object Description Table below for object details. | Object |
| footerText |  | Required | The footer text of card if any | String |
| buttons |  | Required | The array containing button details. {     "id" : " ",     "title" : "",     "subtitle" : "" } | Array |

**image/video/document Object Description Table**












****``````

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of card attachment.Supported Values: IMAGE, VIDEO,DOC | String |
| title | Optional | Refers to the title of the card attachment | String |
| url | Required for publishing Image and document cards | Refers to the url of the image/document that needs to be sent as attachment | String |

See the Card examples:


- [Publishing Card](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card)

- [Publishing Card With Image](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-image)

- [Publishing Card With Video](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-video)

- [Publishing Card With Document](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-document)

#### GEO_LOCATION













      ``




























| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Type of attachment. For this message template, use GEO_LOCATION. | String |
| latitude | Required | The latitude of the location. | Number |
| longitude | Required | The longitude of the location. | Number |
| name | Optional | The name of the location. | String |
| address | Optional | The complete address of the location. | String |

See the [Geolocation Example](https://dev.sprinklr.com/whatsapp-dynamic-templates#geo-location).

#### REQUEST_LOCATION

This template allows you to create a Location request message that includes:


- A body text

- A send location button

When a WhatsApp user taps the button, a location sharing screen appears which the user can then use to share their location.











    ``









| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Type of attachment. For this message template, use REQUEST_LOCATION. | String |
| message | Optional | Message text displayed when requesting location. | String |

See the [Request Location Example](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-request-location-message).

#### ADDRESS

This template allows you to publish an message that allows customers to share their address. The template contains a call-to-action (CTA) button that prompts the users to interact with the message, providing a convenient and streamlined way for them to share their shipping addresses.













    ``



































****``














****``
























| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this message template, use ADDRESS. | String |
| header |  | Optional | Header text for the attachment. | String |
| message |  | Optional | Main message body text. | String |
| footer |  | Optional | Footer text for the attachment. | String |
| addressFields |  | Optional | List of address field objects. | Array |
|  | fieldName | Required | Name of the address field. Supported Values: CITY | String |
|  | prefilledValuePlaceHolder | Optional | Placeholder object for prefilled values. | Object |
|  | prefilledValuePlaceHolder.assetClass | Required | Asset class for the placeholder. Supported Values: MESSAGE | String |
|  | prefilledValuePlaceHolder.customFieldName | Required | Custom field identifier | String |
|  | prefilledValuePlaceHolder.displayName | Required | Display name for the field | String |
|  | copyResponseToCustomField | Optional | Object used to map response to a custom field | Object |

See the [Address Example](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-address-message).

#### Call-To-Action URL Button (CTA_URL)

Your customers might hesitate to click on raw URLs that contain lengthy or obscure strings when they receive text messages. In such cases, you may prefer to send an interactive message with body text and a CTA URL button.

These CTA URL buttons enable you to link any URL to a button, eliminating the need to include the raw URL in the interactive message body.













    ``





















****``










































****``



| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of attachment. For this message template, use CTA_URL. | String |
| header |  | Optional | Header section of the attachment | Object |
| header | image | Optional | Image object inside the header | Object |
| image.type |  | Required | Type of image. Supported Values: IMAGE | String |
| image.url |  | Required | URL of the image resource | String |
| body |  | Optional | Main body text of the attachment | String |
| footerText |  | Optional | Footer text displayed in the attachment | String |
| ctaUrl |  | Required | URL that the CTA button points to | String |
| displayText |  | Required | Text displayed on the CTA button | String |
| urlType |  | Required | Type of URL. Supported Values: STATIC | String |

See the [CTA URL Button Example](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-cta-url).

## Examples

  The following examples show how to publish dynamic WhatsApp templates using the Publishing API.


- [LIST_PICKER](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-list-picker)

- [CARD](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card)

- [CARD with Image](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-image)

- [CARD with Video](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-video)

- [CARD with Document](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-card-with-document)

- [GEO_LOCATION](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-geolocation)

- [REQUEST_LOCATION](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-request-location-message)

- [ADDRESS](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-address-message)

- [CTA_URL](https://dev.sprinklr.com/whatsapp-dynamic-templates#publishing-cta-url)

### LIST_PICKER

#### Request




 Copy Code



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
    "attachment": {
      "type": "LIST_PICKER",
      "header" : {
          "text" : "header text"
      },
      "body" : "list picker body",
      "footerText" : "list picker footer text",
      "buttonTitle": "button title",
      "sections" : [
          {
              "title" : "section title 10",
              "items" : [
                  {
                      "id" : "ad4c0739-jdkskj4c-4ef2-a055-c71e41c33da0",
                      "title" : "item title 10",
                      "subtitle" : "item subtitle 100"
                  },
                  {
                      "id" : "ad4c0739-jdsjnxzmj4c-4ef2-a055-c71e41c33da0",
                      "title" : "item title 20",
                      "subtitle" : "item subtitle 200"
                  }
              ]
          },
          {
              "title" : "section title 20",
              "items" : [
                  {
                      "id" : "ad4c0739-jdkskjsnzm97-ef2-a055-c71e41c33da0",
                      "title" : "item title 210",
                      "subtitle" : "item subtitle 2100"
                  },
                  {
                      "id" : "ad4c0jnsxbjsazmj4c-4ef2-a055-c71e41c33da0",
                      "title" : "item title 220",
                      "subtitle" : "item subtitle 2200"
                  }
              ]
          }
      ]
    }
  },
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "campaign-id",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "ACCOUNT_16848_1630938983000_WHATSAPP_BUSINESS_316_ABEGkZiGKVRZAhBU-gyq6wRu931SHImC9If4",
  "toProfile": {
    "channelType": "WHATSAPP_BUSINESS",
    "channelId": "channel-user-id-of-the-recipient"
  }
}'


 

#### Response



{
    "data": [
        "POST_3329636297"
    ],
    "errors": []
}



#### Example List Picker Message
 

### CARD

#### Request




 Copy Code


 
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
    "attachment": {
      "type": "CARD",
      "header" : {
          "text" : "card header text"
      },
      "title" : "card body",
      "footerText" : "card footer text",
      "buttons" : [
          {
              "id" : "ad4c0739-jdkskjsnzm9dshxzjnm1c33da0",
              "title" : "Sports",
              "subtitle" : "Cricket"
          },
          {
              "id" : "ad4c0739-sdhjzm9dshxzjnm1c33da0",
              "title" : "Animals",
              "subtitle" : "Tiger"
          }
      ]
    }
  },
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "campaign-id",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "ACCOUNT_16848_1630938983000_WHATSAPP_BUSINESS_316_ABEGkZiGKVRZAhBU-gyq6wRu931SHImC9If4",
  "toProfile": {
    "channelType": "WHATSAPP_BUSINESS",
    "channelId": "channel-user-id-of-the-recipient"
  }
}'
 

     
     
   

#### Response



 
{
    "data": [
        "POST_3329638977"
    ],
    "errors": []
}
 

     
     
   

#### Example Card Message
 

### CARD with Image

#### Request




 Copy Code


 
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
    "attachment": {
      "type": "CARD",
      "header" : {
          "image" : {
            "type" : "IMAGE",
            "url" : "https://qa4-sprcdn-assets.sprinklr.com/400002/a6ee05dd-4833-49df-9a4b-7381a37ebb4f-2215371048.jpg"
          }
      },
      "title" : "card body",
      "footerText" : "card footer text",
      "buttons" : [
          {
              "id" : "ad4c0739-jdkskjsnzm9dshxzjnm1c33da0",
              "title" : "Animal 01",
              "subtitle" : "Dogs"
          },
          {
              "id" : "ad4c0739-sdhjzm9dshxzjnm1c33da0",
              "title" : "Animal 02",
              "subtitle" : "Cats"
          }
      ]
    }
  },
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "campaign-id",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "ACCOUNT_16848_1630938983000_WHATSAPP_BUSINESS_316_ABEGkZiGKVRZAhBU-gyq6wRu931SHImC9If4",
  "toProfile": {
    "channelType": "WHATSAPP_BUSINESS",
    "channelId": "channel-user-id-of-the-recipient"
  }
}'
 

     
     
 

#### Response




{
    "data": [
        "POST_3329608771"
    ],
    "errors": []
}
 

     
     
   

#### Example Card with Image Message
 

### CARD with Video

#### Request




 Copy Code


 
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
    "attachment": {
      "type": "CARD",
      "header" : {
          "video" : {
            "type" : "VIDEO",
            "url" : "https://qa4-sprcdn-assets.sprinklr.com/400002/95599f4d-4d99-4647-8fae-cce53ab66f31-1227345726/creating_direct_publishing_vid.mp4"
          }
      },
      "title" : "card body",
      "footerText" : "card footer text",
      "buttons" : [
          {
              "id" : "ad4c0739-jdkskjsnzm9dshxzjnm1c33da0",
              "title" : "Light 01",
              "subtitle" : "Colourful"
          },
          {
              "id" : "ad4c0739-sdhjzm9dshxzjnm1c33da0",
              "title" : "Light 02",
              "subtitle" : "Bright"
          }
      ]
    }
  },
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "campaign-id",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "ACCOUNT_16848_1630938983000_WHATSAPP_BUSINESS_316_ABEGkZiGKVRZAhBU-gyq6wRu931SHImC9If4",
  "toProfile": {
    "channelType": "WHATSAPP_BUSINESS",
    "channelId": "channel-user-id-of-the-recipient"
  }
}'
 

     
     
   

#### Response



 
{
    "data": [
        "POST_3329600771"
    ],
    "errors": []
}
 

     
     
   

#### Example Card with Video Message
 

### CARD with Document

#### Request




 Copy Code


 
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
    "attachment": {
      "type": "CARD",
      "header" : {
          "document" : {
            "type" : "DOC",
            "title": "Test Document",
            "url" : "https://qa4-sprcdn-assets.sprinklr.com/400002/855b1bc8-9bc5-4631-84e8-91d413b56ab0-452842416/Document_-_Word_DOCX.docx"
          }
      },
      "footerText" : "card footer text",
      "buttons" : [
          {
              "id" : "ad4c0739-jdkskjsnzm9dshxzjnm1c33da0",
              "title" : "Documents 01",
              "subtitle" : "Layouts"
          },
          {
              "id" : "ad4c0739-sdhjzm9dshxzjnm1c33da0",
              "title" : "Documents 02",
              "subtitle" : "Numbers"
          }
      ]
    }
  },
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "campaign-id",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "inReplyToMessageId": "ACCOUNT_16848_1630938983000_WHATSAPP_BUSINESS_316_ABEGkZiGKVRZAhBU-gyq6wRu931SHImC9If4",
  "toProfile": {
    "channelType": "WHATSAPP_BUSINESS",
    "channelId": "channel-user-id-of-the-recipient"
  }
}'
 

     
     
 

#### Response



 
{
    "data": [
        "POST_3329056743"
    ],
    "errors": []
}
 

     
     
   

#### Example Card with Document Message
 

### GEO_LOCATION

#### Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '
{
  "accountId": 66076311,
   "content": {
    "attachment": {
        "type": "GEO_LOCATION",
        "latitude":21.2,
        "longitude":22.0,
        "name":"Shivang Test",
        "address":"ggn, haryana"
    }
  },
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "66000002_2155",
    "clientCustomProperties": {},
    "partnerCustomProperties": {}
  },
  "toProfile": {
    "channelType": "WHATSAPP_BUSINESS",
    "channelId": "+918728071386"
  }
}'
 

     
     
 

#### Response



{
    "data": [
        "POST_478638774"
    ],
    "errors": []
}
 

     
     
   
 

### REQUEST_LOCATION

#### Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '
{
    "accountId": 66074089,
    "content": {
        "attachment": {
            "type": "REQUEST_LOCATION",
            "message": "Testing message of location"
        }
    },
    "scheduleDate": 0,
    "taxonomy": {
        "campaignId": "66000002_5947"
    },
    "inReplyToMessageId": "ACCOUNT_66076311_1766498771000_WHATSAPP_BUSINESS_316_wamid.HBgMOTE3ODgwOTAxODMzFQIAEhgUM0FFOEVDOTFDNEE2NTg0M0IxMjEA",
    "toProfile": {
        "channelType": "WHATSAPP_BUSINESS",
        "channelId": "19283994232"
    }
}'
 

     
     
 

#### Response



{
    "data": [
        "POST_545622579"
    ],
    "errors": []
}
 

     
     
   

### ADDRESS

#### Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '
{
    "accountId": 12345678987,
    "content": {
        "attachment": {
            "type": "ADDRESS",
            "header": "Address head",
            "message": "Address is valid\n",
            "footer": "end",
            "addressFields": [
                        {
                            "fieldName": "CITY",
                            "prefilledValuePlaceHolder": {
                                "assetClass": "MESSAGE",
                                "customFieldName": "_c_64fae608cf9529693818a170",
                                "displayName": "BMK Text"
                            },
                            "copyResponseToCustomField": {}
                        }
                    ]
        }
    },
    "scheduleDate": 0,
    "taxonomy": {
        "campaignId": "66000002_5947"
    },
    "inReplyToMessageId": "ACCOUNT_66076311_1766498771000_WHATSAPP_BUSINESS_316_wamid.HBgMOTE3ODgwOTAxODMzFQIAEhgUM0FFOEVDOTFDNEE2NTg0M0IxMjEA",
    "toProfile": {
        "channelType": "WHATSAPP_BUSINESS",
        "channelId": "19283994232"
    }
}'
 

     
     
 

#### Response



{
    "data": [
        "POST_545623756"
    ],
    "errors": []
}
 

     
     
   

### CTA_URL Button

#### Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '
{
    "accountId": 66074089,
    "content": {
        "attachment": {
            "type": "CTA_URL",
            "header": {
                "image": {
                    "type": "IMAGE",
                    "url": "https://storage.googleapis.com/spr-qa6-cdn-secure/PAID/66000000/f94027a8-e756-423e-a136-343ecca1f98f-879294258/image.jpg"
                }
            },
            "body": "Tap the button below to know more",
            "footerText": "Know More",
            "ctaUrl": "https://www.sprinklr.com",
            "displayText": "Buy",
            "urlType": "STATIC"
        }
    },
    "scheduleDate": 0,
    "taxonomy": {
        "campaignId": "66000002_5947",
        "clientCustomProperties": {},
        "partnerCustomProperties": {}
    },
    "inReplyToMessageId": "ACCOUNT_66076311_1766498771000_WHATSAPP_BUSINESS_316_wamid.HBgMOTE3ODgwOTAxODMzFQIAEhgUM0FFOEVDOTFDNEE2NTg0M0IxMjEA",
    "toProfile": {
        "channelType": "WHATSAPP_BUSINESS",
        "channelId": "19283994232"
    }
}'
 

     
     
 

#### Response



{
    "data": [
        "POST_545624040"
    ],
    "errors": []
}
 

     
     
   
  

[](https://dev.sprinklr.com/whatsapp-dynamic-templates) 

 

 
[Back to top](https://dev.sprinklr.com/whatsapp-dynamic-templates)
