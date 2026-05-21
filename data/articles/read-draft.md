---
title: "Read Draft"
slug: read-draft
url: https://dev.sprinklr.com/read-draft
---

# Read Draft

#
GET Read Draft


This API allows you to retrieve a drafted message by using message id.

### Use Cases:

- **Review Drafts Before Sending: **Retrieve drafted messages to review and ensure accuracy before finalizing and sending them out.

- **Edit and Update Drafted Messages: **Use the API to fetch a drafted message, make necessary edits, and then save or resend the updated draft.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/drafts?messageIds={message_id}

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

### Query Parameters







| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| messageId | Required | Integer | The id of the drafted post |

### Response Schema







````

| Parameter |  |  | Type | Description |
| --- | --- | --- | --- | --- |
| data |  |  | Array of Objects | Contains an array of objects representing individual entities with detailed information. |
|  | id |  | Integer | Unique identifier for the entity. |
|  | accountIds |  | Array of Integers | List of account IDs associated with the entity. |
|  | accountGroupIds |  | Array of Integers | List of account group IDs associated with the entity. |
|  | version |  | Integer | Version number of the entity. |
|  | contentTemplateIds |  | Array of Strings | List of content template IDs associated with the entity. |
|  | accountTypes |  | Array of Strings | List of account types associated with the entity. |
|  | variantDetails |  | Object | Contains information about the variant details of the entity. |
|  |  | variant | Boolean | Indicates whether the entity is a variant. |
|  |  | variantParentMessageId | String | ID of the parent message if the entity is a variant. |
|  |  | hasVariants | Boolean | Indicates if the entity has variants. |
|  | content |  | Object | Contains details about the content associated with the entity. |
|  |  | isRichText | Boolean | Indicates whether the content is in rich text format. |
|  | channelOptions |  | Array | List of options related to the channels. Typically an empty array if no options are specified. |
|  | scheduleDate |  | Integer | The scheduled date and time for the entity, represented as a Unix timestamp. |
|  | taxonomy |  | Object | Contains taxonomical information related to the entity. |
|  |  | name | String | The name or title of the entity. |
|  |  | campaignId | String | The ID of the associated campaign. |
|  |  | partnerCustomProperties | Object | Contains custom properties associated with the entity, typically with dynamic keys and values. |
|  |  | urlShortenerId | String | ID of the URL shortener associated with the entity. |
|  | status |  | String | The current status of the entity, such as DRAFT, PUBLISHED, etc. |
|  | sourceLocale |  | String | The locale of the source content. |
|  | contentLocale |  | String | The locale of the content. |
|  | autoResponse |  | Boolean | Indicates whether auto-response is enabled for the entity. |
|  | createdTime |  | Integer | The timestamp when the entity was created, represented as a Unix timestamp. |
|  | modifiedTime |  | Integer | The timestamp when the entity was last modified, represented as a Unix timestamp. |
|  | authorId |  | Integer | ID of the author who created or last modified the entity. |
| errors |  |  | Array of Objects | Contains an array of error objects if any errors occurred during the API call. Typically an empty array if there are no errors. |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/drafts?messageIds=78377'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

## Example - Response

 
 
     
 
	{
    "data": [
        {
            "id": 9929918,
            "accountIds": [
                600055045
            ],
            "accountGroupIds": [],
            "version": 0,
            "contentTemplateIds": [
                "harshil"
            ],
            "accountTypes": [
                "CONTENTFUL"
            ],
            "variantDetails": {
                "variant": false,
                "variantParentMessageId": "MESSAGE_9929918",
                "hasVariants": false
            },
            "content": {
                "isRichText": false
            },
            "channelOptions": [],
            "scheduleDate": 1697806791388,
            "taxonomy": {
                "name": "Test message",
                "campaignId": "66000002_461",
                "partnerCustomProperties": {
                    "_c_64ecf116d8489c6113a9d3da": [
                        "Not Started"
                    ],
                    "_c_64eda9b3d8489c6113bc5658": [
                        "val 1"
                    ],
                    "_c_64c0a65922941712edb471fb": [
                        "Default Value : joeyTextArea edited by shubham qa6"
                    ],
                    "_c_651d40f632761f7445702777": [
                        "AAA 🟢"
                    ],
                    "_c_64c0a62222941712edb470e3": [
                        "Monica"
                    ],
                    "_c_64c0a63922941712edb47142": [
                        "777"
                    ],
                    "_c_64c0a5c822941712edb46f77": [
                        "Default Value : joeyText"
                    ],
                    "_c_6523df73a7c00325fad61e66": [
                        "qw",
                        "w",
                        "123",
                        "9099\n121\n1212\n1212"
                    ],
                    "_c_64c0a5fc22941712edb4703d": [
                        "Joey"
                    ],
                    "_c_64f5b1b5ab3b344a0b89f1f1": [
                        "Wednesday"
                    ],
                    "_c_64f88d21fc92780c1f2bc9ea": [
                        "India"
                    ],
                    "_c_6523e211a7c00325fad6b947": [
                        "12",
                        "w232",
                        "32332",
                        "4545",
                        "c eeefe",
                        "fef"
                    ],
                    "_c_6513ee89dd524250c33335a2": [
                        "1"
                    ],
                    "_c_64dc83bf0cfbc0371edd879b": [
                        "default value"
                    ],
                    "_c_64ddb90bcb585b4896fee93a": [
                        "def"
                    ],
                    "_c_64c0a64a22941712edb471a0": [
                        "1672511400000"
                    ]
                },
                "urlShortenerId": "64e86a16beb7386194c3d8c8"
            },
            "status": "DRAFT",
            "sourceLocale": "ar_EG",
            "contentLocale": "ar_EG",
            "autoResponse": false,
            "createdTime": 1697806791388,
            "modifiedTime": 1697806791388,
            "authorId": 66000017
        }
    ],
    "errors": []
} 

     
     
   
 

	[](https://dev.sprinklr.com/read-draft) 

 

 
[Back to top](https://dev.sprinklr.com/read-draft)
