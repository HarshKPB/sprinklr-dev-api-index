---
title: "Source Agnostic - Send Message"
slug: source-agnostic-send-message
url: https://dev.sprinklr.com/source-agnostic-send-message
---

# Source Agnostic - Send Message

# POST Source Agnostic - Send Message

Source agnostic send message API allows importing third-party messages to Sprinklr. You will need to pass a unique messageId and the conversationId associated with the conversation to facilitate the import. Once the message is received on Sprinklr's platform, a case and a corresponding profile will be created, which can then be further assigned to the respective agent.

This documentation covers the following Use Cases:

	[1. Send Text Message](https://dev.sprinklr.com/source-agnostic-send-message#send-text-message)

[2. Send Image Attachment](https://dev.sprinklr.com/source-agnostic-send-message#send-image-attachment)

[3. Send Video Attachment](https://dev.sprinklr.com/source-agnostic-send-message#send-video-attachment)

[4. Send Document Attachment](https://dev.sprinklr.com/source-agnostic-send-message#send-document-attachment)

[5. Send Audio Attachment](https://dev.sprinklr.com/source-agnostic-send-message#send-audio-attachment)

[6. Send Simple Base 64 Content](https://dev.sprinklr.com/source-agnostic-send-message#send-simple-base-content)

[7. Send Multimedia Attachments](https://dev.sprinklr.com/source-agnostic-send-message#send-multimedia-attachment)

[8. Enrich Case and Message Custom Properties](https://dev.sprinklr.com/source-agnostic-send-message#enrich-case-message-custom-properties)

[9. Send HTML Content](https://dev.sprinklr.com/source-agnostic-send-message#send-html-content)

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/source-agnostic/`{accountId}`/send

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

### Path Parameter












| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Required | Refers to the unique identifier for the source agnostic account | Integer |

**Steps to Extract Account Id from UI: **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on Accounts Icon within "Manage Workspace" module
- Click on the three dots placed alongside the respective account name
- Click on "Details" option from the drop down menu
- Click on copy url icon on the top right corner from the window that appears
- Use any encoder-decoder tool and paste the copied URL
- The account id will be the part of the decoded URL, i.e., if you get `/ACCOUNT/100426226/OVERVIEW` in the decoded URL, your account id is 100426226.

### Request Parameters











































``

[fetch custom field by field name API](https://dev.sprinklr.com/fetch-custom-field-using-field-name)

[fetch custom field by field name API](https://dev.sprinklr.com/fetch-custom-field-using-field-name)

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| messageId |  | Required | The unique identifier for the message that needs to be sent to SprinklrThe messageId needs to be unique every time a message is sent to Sprinklr. | String |
| conversationId |  | Required | The unique identifier that the brand generates each time a new conversation (comosed of several messages) is created within Sprinklr.When sending messages within the same conversation within Sprinklr, the conversationId should remain the same. If a new conversationId will be passed, a new case will be created. | String |
| senderProfile |  | Required | Refers to the profile of the sender. Refer to the table below for sender profile object details. | Object |
| receiverProfile |  | Required | Refers to the profile of the receiver. Refer to the table below for receiver profile object details. | Object |
| content |  | Required | Refers to the content of the message | Object |
|  | text | Optional | Refers to the text of the message | String |
|  | isRichText | OptionalRequired for sending HTML content | If true, the content that is being associated to the case is in rich text format. It is required to pass isRichText value true when sending HTML content | Boolean |
| messageProperties |  | Optional | Object defining the inbound message level custom properties.You can use  for steps to fetch custom field name and check the permissible values for the respective field. | Object |
| conversationProperties |  | Optional | Object defining the case level custom properties.You can use  for steps to fetch custom field name and check the permissible values for the respective field. | Object |
|  | attachment | OptionalRequired for messages with attachment | Object containing the message attachment detailsRefer to the tables below for attachment object parameter descriptions | Object |

### senderProfile and receiverProfile Object Description Table

[fetch custom field by field name API](https://dev.sprinklr.com/fetch-custom-field-using-field-name)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Refers to the profile id of the sender/receiver | Integer |
| screenName | Optional | Refers to the screen name of the sender/receiver | String |
| name | OptionalIt is recommended to pass name parameter as it will be easier to identify the profile on Sprinklr platform | Refers to the full name of the sender/receiver | String |
| firstName | Optional | Refers to the first name of the sender/receiver | String |
| lastName | Optional | Refers to the last name of the sender/receiver | String |
| email | Optional | Refers to the email of the sender/receiver | String |
| phoneNo | Optional | Refers to the phone number of the sender/receiver | String |
| profileURL | Optional | Refers to the profile url of the sender/receiver | String |
| profileImageURL | Optional | Refers to the profile image url for the sender/receiver | String |
| properties | Optional | Object defining the custom properties for the sender/receiver.You can use  for steps to fetch custom field name and check the permissible values for the respective field. | Object |

### 1. Send Text Message

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "messageId": "message_12345674444",
    "conversationId": "case_123",
    "senderProfile": {
        "id": "600055143",
        "properties": {
            "_c_63efc79c48af0b34e3d89633": [
                "test1"
            ]
        }
    },
    "brandMessage": false,
    "receiverProfile": {
        "id": "919810052940",
        "properties": {
            "_c_63efc79c48af0b34e3d89633": [
                "test2"
            ]
        }
    },
    "content": {
        "text": "This is a test message"
    }
}'



### 2. Send Image Attachment

#### attachment Object Description Table

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of attachment | String |
| url | Required | Refers to the url of the attachment | String |
| title | Optional | Refers to the title of the image | String |
| description | Optional | Refers to the description of the image attachment | String |
| previewUrl | Optional | Refers to the preview Url for the image attachment | String |
| mimeType | Optional | Refers to the attachment type and its formatExample: image/jpeg | String |

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "messageId": "Test_23",
   "conversationId": "Test_2_Image",
   "senderProfile": {
       "id": "918410614581"
   },
   "receiverProfile": {
       "id": "19283994232"
   },
   "content": {
       "text": "This is a test message for image",
       "attachment": {
           "type": "IMAGE",
           "url": "https://images.pexels.com/photos/1170986/pexels-photo-1170986.jpeg?auto=compress&cs=tinysrgb&w=1600",
           "title": "Test_image1.png",
           "description": "This is a test image1 for testing",
           "previewUrl": "",
           "mimeType": ""
       }
   }
}'



### 3. Send Video Attachment

#### attachment Object Description Table

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of attachment | String |
| url | Required | Refers to the url of the attachment | String |
| title | Optional | Refers to the title of the video attachment | String |
| description | Optional | Refers to the description of the video attachment | String |
| previewUrl | Optional | Refers to the preview Url for the video attachment | String |
| mimeType | Optional | Refers to the attachment type and its format | String |

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "messageId": "Test_30",
   "conversationId": "Test_3_Video",
   "senderProfile": {
       "id": "918410614581"
   },
   "receiverProfile": {
       "id": "19283994232"
   },
   "content": {
       "text": "This is a test message",
       "attachment": {
           "type": "VIDEO",
           "url": "https://player.vimeo.com/external/372327760.sd.mp4?s=1b5df36319c5d311001b5ac003e69b8840ccb10b&profile_id=164&oauth2_token_id=57447761",
           "title": "Test_video.mp4",
           "description": "This is a test Video for testing",
           "previewUrl": "",
           "mimeType": ""
       }
   }
}'



### 4. Send Document Attachment

#### attachment Object Description Table

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of attachment | String |
| url | Required | Refers to the url of the attachment | String |
| title | Optional | Refers to the title of the document attachment | String |
| description | Optional | Refers to the description of the document attachment | String |
| previewImageUrl | Optional | Refers to the image url for the document (if any) | String |

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "messageId": "Test_4",
   "conversationId": "Test_4_Doc",
   "senderProfile": {
       "id": "918410614581"
   },
   "receiverProfile": {
       "id": "19283994232"
   },
   "content": {
       "text": "This is a test message for doc",
       "attachment": {
           "type": "DOC",
           "url": "https://www.clickdimensions.com/links/TestPDFfile.pdf",
           "title": "",
           "description": "",
           "previewImageUrl": ""
       }
   }
}'



### 5. Send Audio Attachment

#### attachment Object Description Table

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of attachment | String |
| url | Required | Refers to the url of the attachment | String |
| title | Optional | Refers to the title of the audio attachment | String |
| description | Optional | Refers to the description of the audio attachment | String |
| previewImageUrl | Optional | Refers to the preview Url for the audio attachment | String |

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "messageId": "Test_61",
   "conversationId": "Test_6_Audio",
   "senderProfile": {
       "id": "918410614581"
   },
   "receiverProfile": {
       "id": "19283994232"
   },
   "content": {
       "text": "This is a test message for audio",
       "attachment": {
           "type": "AUDIO",
           "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
           "title": "",
           "previewImageUrl": ""
       }
   }
}'



### 6. Send Simple Base64 Content

#### attachment Object Description Table

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of attachment | String |
| base64EncodedContent | Required | Refers to the base64 content for image conversion | String |
| fileName | Required | Refers to the file name of the image to be appended | String |
| title | Optional | Refers to the title of the attachment | String |
| description | Optional | Refers to the description of the attachment | String |

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "messageId": "Test_50",
   "conversationId": "Test_5_Base64_Image",
   "senderProfile": {
       "id": "918410614581"
   },
   "receiverProfile": {
       "id": "19283994232"
   },
   "content": {
       "text": "This is a test message for image conversion in Base64",
       "attachment": {
           "type": "BASE64",
           "base64EncodedContent": "/9j/4AAQSkZJRgABAQEASABIAAD/4gxYSUNDX1BST0ZJTEUAAQEAAAxITGlubwIQAABtbnRyUkdCIFhZWiAHzgACAAkABgAxAABhY3NwTVNGVAAAAABJRUMgc1JHQgAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLUhQICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABFjcHJ0AAABUAAAADNkZXNjAAABhAAAAGx3dHB0AAAB8AAAABRia3B0AAACBAAAABRyWFlaAAACGAAAABRnWFlaAAACLAAAABRiWFlaAAACQAAAABRkbW5kAAACVAAAAHBkbWRkAAACxAAAAIh2dWVkAAADTAAAAIZ2aWV3AAAD1AAAACRsdW1pAAAD",
           "fileName": "Test_image.jpg",
           "title": "",
           "description": ""
       }
   }
}'



### 7. Send Multimedia Attachment

#### attachment Object Description Table

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of attachment | String |

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}} \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "messageId": "message_2",
    "conversationId": "testing_2,
    "senderProfile": {
       "id": "12345678901336",
       "name": "John Doe",
       "email": "johndoe@gmail.com",
       "phoneNo":"98764321387"
    },
    "receiverProfile": {
        "id": "19283994232"
    },
    "content": {
        "text":"Testing",
        "attachment": {
            "type": "MULTI_MEDIA",
            "attachments": [
                {
                    "type": "DOC",
                    "url": "https://www.clickdimensions.com/links/TestPDFfile.pdf",
                    "title": "Test Doc 1"
                },
                {
                    "type": "DOC",
                    "url": "https://www.clickdimensions.com/links/TestPDFfile.pdf",
                    "title": "Test Doc 2"
                }
            ]
        }
    }
}'



**Dev Notes: **Additional parameters for attachment depend on the type of attachment. Refer the following API documentations for attachment object details wrt the chosen attachment type:

- Send Image Message
- Send Video Message
- Send Document
- Send Base64 Content
- Send Audio

### 8. Enrich Case and Message Custom Properties

While sending the message, you can enrich message properties by defining properties under the messageProperties object and case properties by defining properties under the conversationProperties object.



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "messageId": "Test_Properties",
    "conversationId": "test_8_properties",
    "senderProfile": {
        "id": "19283994233"
    },
    "receiverProfile": {
        "id": "91841061431"
    },
    "content": {
        "text": "Test message"
    },
    "messageProperties": {
        "_c_63fdcfded4572f6e1021beff": [
            "Test1"
        ]
    },
    "conversationProperties": {
        "_c_63fdcfded4572f6e1021beff": [
            "Test2"
        ]
    }
}'



### 9. Send HTML Content

**Dev Notes: **

- isRichText should be `"true"` when sending HTML content

- Quotes and slashes should be skipped when passing the HTML content in the text field

#### Example - Request



 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/600050740/send' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "messageId": "message_2",
    "conversationId": "testing_2,
    "senderProfile": {
       "id": "12345678901336",
       "name": "John Doe",
       "email": "johndoe@gmail.com",
       "phoneNo":"98764321387"
    },
    "receiverProfile": {
        "id": "19283994232"
    },
    "content": {
        "text":"\n
**Need assistance? Fill out our [feedback form](\"https://forms.office.com/r/5wTBFPQ7DC\") and we’ll get back to you. **
\n",
        "isRichText" : true
}
}'



### Example - Response





{
   "data": "6906053",
   "errors": []
}



### Response Parameters

| Parameter | Description | Type |
| --- | --- | --- |
| data | Refers to the case number | String |

**Dev Notes: ** If the same messageId is sent twice for a given conversation Id, the API will give a 400 Bad Request error response.

[](https://dev.sprinklr.com/source-agnostic-send-message) 

 

 
[Back to top](https://dev.sprinklr.com/source-agnostic-send-message)
