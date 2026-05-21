---
title: "Create Email"
slug: create-email
url: https://dev.sprinklr.com/create-email
---

# Create Email

#
POST Create Email

The Create Email API allows you to ingest an email within Sprinklr as both a customer and brand message. To view the ingested email details you can create an [Engagement Dashboard](https://www.sprinklr.com/help/articles/getting-started-with-social-engagement/what-can-you-do-with-engagement-dashboards/6450dc2fd85662201933c821) with the Email column and filter based on the account Id.

**Dev Notes: **This API can only be used for ingesting data into Sprinklr.

- [Create Email with Attachment from URL](https://dev.sprinklr.com/create-email#url)

- [Create Email with Attachment from Local](https://dev.sprinklr.com/create-email#local)

## Create Email with Attachment from a URL

Use this API endpoint to create an email with attachment. The attachment is provided as a file URL available on web.

### API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/email/create?aId={emailId}

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

### Query Parameters







| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| aId | Required | This is the email Id associated with the email account within Sprinklr.The email Id should be URL-encoded. | String |

**Dev Notes: **Here `aId` represents the email Id of the Email Account which is added in the Sprinklr Accounts page.


### Request Parameters







****````
``

****

``

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| from |  | Required | Refers to the email id of the sender Dev Notes: The from field is a unique identifier. If the from field has the same email address for every consecutive call, messages will be associated with the same sender profile. A new audience profile gets created for the user details you pass in the from field. | String |
| to |  | Optional | Email Id of the recipient, to whom the brand sent the email. This field is required only when you want to ingest the message as brand message | String |
| cc |  | Optional | Refers to the email id you want to CC in the email | String |
| bcc |  | Optional | Refers to the email id you want to BCC in the email | String |
| brandPost |  | Optional | If true, the message is ingested as brand post | Boolean |
| subject |  | Required | Refers to the subject of the email | String |
| body |  | Required | Refers to the body content of the email | String |
| customProperties |  | Optional | Refers to the key and value pair for the custom properties you want to associate with the email | Object |
| attachments |  | Optional | The object containing the attachment details. | Object |
|  | fileName | Required | The name of the file | String |
|  | contentType | Required | The file type. The supported types are IMAGE, VIDEO, AUDIO, DOC, PDF, SPREADSHEET, HTML, DOCUMENT, PSD, PSB, PRESENTATION, ZIP, BINARY, FONT, CSV, SUBTITLE | String |
|  | url | Required | The URL of the attachment that needs to be added from a link | String |

**Dev Notes: **For sending the body content with line breaks, kindly use the following format within the "body" parameter:

```
<p class=\"export-block__parent\">**Testing**</p><p class=\"export-block__parent\">**Email**</p><p class=\"export-block__parent\">**API**</p><p class=\"export-block__parent\">**With Line Breaks**</p>
```

### Example: To ingest data in Sprinklr as a customer email




 Copy Code


 
curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/email/create?aId={emailId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "from": "abc@sprinklr.com",
    "cc": "test1@sprinklr.com",
    "bcc": "test2@sprinklr.com",
    "subject": "Test Email Query Thread",
    "body": "This api is awesome, I like this API.",
      "attachments": [
        {
            "fileName": "excel",
            "contentType": "SPREADSHEET",
            "url": "https://www.newfile.com/400002/bf8fcd8bf0e8-99344174.xlsx"
        }
    ],
"customProperties": {
"_c_5fc0cb96b0a31e0d4535f447": [
"Value1",
"Value2"
],
"_c_5fcb618ed75d24677df0fd22": ["1"],
"_c_619696a27d40de0ce801f801":["textField"],
"_c_619697007d40de0ce8020268":["1635791400000"],
"_c_619696e57d40de0ce801ff54" :[100]
}
}'





### Example - Response



 
200 OK
SUCCESS




 

### Example - To ingest data in Sprinklr as a Brand email




 Copy Code


curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/email/create?aId={emailId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "from": "abc@sprinklr.com.com",
    "to": "test1@sprinklr.com",
    "cc": "test2@sprinklr.com",
    "bcc": "test3@sprinklr.com",
    "subject": "Test Email Query Thread",
    "brandPost": true,
    "body": "This api is awesome, I like this API.",
      "attachments": [
        {
            "fileName": "excel",
            "contentType": "SPREADSHEET",
            "url": "https://www.newfile.com/400002/bf8fcd8bf0e8-99344174.xlsx"
        }
    ],
"customProperties": {
"_c_5fc0cb96b0a31e0d4535f447": [
"Value1",
"Value2"
],
"_c_5fcb618ed75d24677df0fd22": ["1"],
"_c_619696a27d40de0ce801f801":["textField"],
"_c_619697007d40de0ce8020268":["1635791400000"],
"_c_619696e57d40de0ce801ff54" :[100]
}
}'



   

### Example - Response



 
200 OK
SUCCESS




 

## Create Email with Attachments from Local

Use this API to create an email with or without attachments. Attachments can be added as local files.

### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/email/generate?aId={emailId}

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







| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| aId | Required | This is the account email Id. The Email Id to which you want to send an email and which is available in Account within Sprinklr. | String |

**Dev Notes: **Here `aId` represents the email Id of the Email Account which is added in the Sprinklr Accounts page.


### Request Body Parameters







| From-Data | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| from | Required | Email Id of the sender. | String |
| subject | Required | Subject of the email. | String |
| body | Required | Email body. | String |
| file | Optional | Email attachment upto 100mb. | Attachment address |

**Supported Attachment Types: **
 pdf, excel, mp3, mp4, doc, txt, html, image, csv & zip
**Note: ** Multiple attachments are supported.

### Example - Request




 Copy Code


 
curl --location --request POST
'https://api3.sprinklr.com/{env}/api/v2/email/generate?aId={emailId}' \
--header 'Key: {Enter your API KEY}' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--form 'from=anc@xyz.com' \
--form 'subject=100 mb image ' \
--form 'body=Yeah! test it with attachment' \
--form 'file=@/Users/abc/Desktop/Screenshot 2020-07-30 at 5.49.18 PM.png'



 

### Example - Response



 
200 OK
SUCCESS




 
	[](https://dev.sprinklr.com/create-email) 

 

 
[Back to top](https://dev.sprinklr.com/create-email)
