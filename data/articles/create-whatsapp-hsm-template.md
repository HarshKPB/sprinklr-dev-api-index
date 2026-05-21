---
title: "Create WhatsApp HSM Template"
slug: create-whatsapp-hsm-template
url: https://dev.sprinklr.com/create-whatsapp-hsm-template
---

# Create WhatsApp HSM Template

#   POST Create WhatsApp HSM Template
 

This API allows you to create a WhatsApp HSM template using dynamic content and customizable headers. An HSM template message is a special message type that must be used for any business-initiated or re-engagement conversations via the WhatsApp channel.

HSM is mainly created for sending notifications to customers. Notifications are business-initiated templated messages that can be sent anytime. They enable you to:


- Deliver important, timely messages during your customer’s path to purchase.

- Send messages anytime without any 24 hours' time restriction.

- Continue the conversation with the customers who respond to your notifications.

**Related Knowledge Base Article: **[Create an HSM Template for WhatsApp Business](https://www.sprinklr.com/help/articles/hsm-templates/create-an-hsm-template-for-whatsapp-business/63d6694a468ae80d39346ac5)

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/sam/template

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









****``




















































****``








****``








[attachment Object](https://dev.sprinklr.com/create-whatsapp-hsm-template#attachment-object)




| Parameter | Sub-Parameter | Required/Optional | Description | Type | Field Character Length |
| --- | --- | --- | --- | --- | --- |
| name |  | Required | Refers to the unique name of the template | String | 50 |
| description |  | Optional | Refers to the description of the template | String | 100 |
| assetType |  | Required | Refers to the type of templateDefault Value for HSM: TEMPLATE_ASSET | String | NA |
| status |  | Required | Refers to the status of the templateDefault Value for HSM: Approved | String | NA |
| taxonomy |  | Optional | Refers to the object containing the taxonomy details | Object | NA |
|  | campaignId | Optional | Refers to the unique identifier for the campaign you want to group the HSM template | String | NA |
|  | tags | Optional | Refers to the list of tags you want to associate with the HSM template | List [String] | NA |
| templateAsset |  | Required | Refers to the object containing the template asset details | Object | NA |
|  | name | Required | Refers to asset name | String | 50 |
|  | channelType | Required | Refers to the channel type associated with the assetDefault Value for HSM Template: WHATSAPP_BUSINESS | String | NA |
|  | templateType | Required | Refers to the type of templateDefault Value for HSM Template: HSM | String | NA |
|  | attachment | Required | Refers to the object containing the template attachment detailsFor more details, see the  table below. | Object | NA |

### `attachment` Object















****``






































****````




























****``




































****````````























































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type | Character Length |
| --- | --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of templateDefault Value for HSM Template: HSM | String | NA |
| wabaId |  | Required | Unique identifier for the WhatsApp Business AccountHelps authenticate and associate the HSM template to the WhatsApp Business Account added to Sprinklr | String | NA |
| namespace |  | Required | String passed for unique identification | String | NA |
| elementName |  | Required | Unique identifier for your HSM templateOnly lowercase characters, underscores, and numbers allowed | String | 50 |
| category |  | Required | Template category to group the HSM templateSupported Values: UTILITY, MARKETING | String | NA |
| langCode |  | Required | Template language codeRefer to appendix for supported codes | String | NA |
| allowCategoryChange |  | Required | If true, category auto‑changes based on template content during validation | Boolean | NA |
| wabaTemplateStatus |  | Required | Status of the WhatsApp templateDefault Value: PENDING | String | NA |
| message |  | Required | Message content of the templateUp to 1024 characters | String | 100 |
| footer |  | Optional | Footer text at the end of the template | String | 60 |
| header |  | Optional | Object containing header component details | Object | 20 |
|  | headerType | Required | Type of headerSupported Values: IMAGE, VIDEO, TEXT, DOCUMENT | String | NA |
|  | message | Required | Header content (text or URL) | String | 100 |
| placeholders |  | Optional | Header content details using custom fields | Array | NA |
|  | example | Required | Value assigned to custom property | List [String/integer] | 50 |
| placeholders |  | Optional | Message content details using custom fields | Array | NA |
|  | assetClass | Required | Asset class of the custom field | String | NA |
|  | customFieldName | Required | Custom field name to pick value from | String | NA |
|  | displayName | Required | Value assigned to custom property | String | NA |
|  | example | Required | Value assigned to custom property | List [String/integer] | 50 |
| buttons |  | Optional | Array containing button details (max 3, text up to 20 chars) | Array | NA |
|  | title | Required | Label of the button | String | 50 |
|  | payload | Optional | Postback message when action is “TEXT” | String | 100 |
|  | actionDetail | Required | Object containing type of action on button click | Object | NA |
|  | placeholders | Optional | Required if action is “OPEN_URL” and urlType is “DYNAMIC” | Array | NA |
|  | example | Required | Value assigned to custom property | List [String/integer] | 50 |

### `placeHolders` Object




















[Fetch Custom Field Using Field Name](https://dev.sprinklr.com/fetch-custom-field-using-field-name)

[Bootstrap API](https://dev.sprinklr.com/bootstrap-api-v1)










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetClass | Required | Refers to the asset class of the custom field you want to pick the header/button content from | String |
| customFieldName | Required | Refers to the custom field name of the custom field you want to pick the header/button value from       Refer to documentation for steps to extract custom field name ().       You can also use the  for extracting custom field names with respect to different asset types. | String |
| displayName | Optional | Refers to the display name of the custom field | String |

### `actionDetail` Object Description Table














****

- ``
- ``
- ``







    ``








****

- ``
- ``





















| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| action |  | Required | Refers to the action type that needs to be performed when a customer clicks on the button       Supported Values:          TEXT: for quick reply   DIAL: for call-to-action button having action type “Call”   OPEN_URL: for call-to-action button having action type “Open Url” | String |
| url |  | Optional | Required when action is set as OPEN_URL. Refers to the base URL or complete URL of the page that the customer will be redirected to when they click on the button. | String |
| urlType |  | Required | Refers to the type of the URL       Supported Values:          STATIC: Refers to the static URL that the customer should be redirected to   DYNAMIC: Refers to the dynamic URL that the customer will be redirected to (Refer to description below for details on how to define dynamic URL) | String |
| countryCode |  | Optional | Required only when the button type is “call-to-action” and action type is “DIAL”. Refers to the country code for the phone line extension.Syntax: ISO Country Code_Phone Country Code | String |
| phoneNumber |  | Optional | Required only when the button type is “call-to-action” and action type is “DIAL”. Refers to the phone number the call will be placed on.Note: The phone number should also include the phone country code in the prefix. | String |


**Dev Notes: How to Add Dynamic URLs in Buttons?**



- Dynamic URLs can be added for "Call to Action" button types and Action "OPEN_URL".

- You need to define the base domain along with a placeholder `{{1}}` within the "url" parameter.

        Syntax Example: `https://www.google.com/{{1}}`

- For defining the value of `{{1}}`, you need to pass the custom field details
        (custom field name, custom field asset class, display name, and custom field value) within the placeholder array.


### Template Category











-
-
-
-
-
-




-
-
-
-
-



| Category | Description |
| --- | --- |
| MARKETING | Most commonly used category which covers the following objectives:                    Driving sales           Increasing reach           Creating awareness           Retargeting           Brand Promotion           Build customer relationships |
| UTILITY | These are templates triggered when a customer initiates a conversation or performs an action. The objectives covered include:                    Opt-In Management           Managing orders           Account and Update Alerts           Feedback Surveys           Continue communication on WhatsApp from a different channel |

### Sample API Request Body by Category Types































































| Category | Type | Sample Request |
| --- | --- | --- |
| Header | Text | "header": {   "headerType": "TEXT",   "message": "Hi" } |
| Header | Image | "header": {   "headerType": "IMAGE",   "message": "",   "example": [""] } |
| Header | Video | "header": {   "headerType": "VIDEO",   "message": "",   "example": [""] } |
| Header | Document | "header": {   "headerType": "DOCUMENT",   "message": "",   "example": [""] } |
| Button | Quick Reply | "buttons": [   {     "title": "",     "payload": "",     "actionDetail": {       "action": "TEXT"     }   } ] |
| Button | CTA - Call | "buttons": [   {     "title": "",     "actionDetail": {       "countryCode": "IN_+91",       "phoneNumber": "",       "action": "DIAL"     }   } ] |
| Button | CTA - Static URL | "buttons": [   {     "title": "",     "actionDetail": {       "url": "",       "urlType": "STATIC",       "action": "OPEN_URL"     }   } ] |
| Button | CTA - Dynamic URL | "buttons": [   {     "title": "",     "actionDetail": {       "url": "{{1}}",       "urlType": "DYNAMIC",       "action": "OPEN_URL"     },     "placeholders": [       {         "assetClass": "PROFILE",         "customFieldName": "PROFILE.",         "displayName": ""       }     ],     "example": [       ""     ]   } ] |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/sam/template' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--data '{
  "name": "WhatsApp HSM template",
  "description": "Description for the template",
  "assetType": "TEMPLATE_ASSET",
  "status": "APPROVED",
  "taxonomy": {
    "campaignId": "66000002_401",
    "tags": [
      "apiImport"
    ]
  },
  "templateAsset": {
    "name": "Customer Welcome HSM",
    "channelType": "WHATSAPP_BUSINESS",
    "templateType": "HSM",
    "attachment": {
      "type": "HSM",
      "wabaId": "384946199920777",
      "namespace": "b9791533d_82c6_485b_83a08_7436ac8ad65e",
      "elementName": "welcome_message_template",
      "category": "UTILITY",
      "langCode": "en",
      "allowCategoryChange": true,
      "wabaTemplateStatus": "PENDING",
      "message": "Welcome {{1}}! \nHow can we assist you today? I hope you are having a good day",
      "footer": "Thank you for choosing us",
      "header": {
        "headerType": "TEXT",
        "message": "Hi"
      },
      "placeholders": [
        {
          "assetClass": "PROFILE",
          "customFieldName": "PROFILE.firstName",
          "displayName": "John"
        }
      ],
      "example": [
        "John"
      ],
      "buttons": [
        {
          "title": "Get Help",
          "payload": "HELP_REQUEST",
          "actionDetail": {
            "action": "TEXT"
          }
        }
      ]
    }
  }
}'



## Example - Response




{
    "data": {
        "assetType": "TEMPLATE_ASSET",
        "templateAsset": {
            "channelType": "WHATSAPP_BUSINESS",
            "templateType": "HSM",
            "elementList": [],
            "buttons": [],
            "attachment": {
                "wabaTemplateId": 940030808839756,
                "namespace": "4d7410c8_5208_4fc5_af91_59111a420022",
                "wabaId": "384946199920777",
                "elementName": "welcome_message_template",
                "category": "UTILITY",
                "langCode": "en",
                "buttons": [
                    {
                        "id": "69efaad06357c2c9885dc076",
                        "title": "Get Help",
                        "payload": "HELP_REQUEST",
                        "actionDetail": {
                            "postBackHandlerType": "TEXT_POST_BACK",
                            "action": "POST_BACK"
                        },
                        "placeholders": []
                    }
                ],
                "wabaTemplateStatus": "PENDING",
                "message": "Welcome {{1}}! \nHow can we assist you today? I hope you are having a good day",
                "footer": "Thank you for choosing us",
                "header": {
                    "headerType": "TEXT",
                    "message": "Hi",
                    "placeholders": []
                },
                "allowCategoryChange": true,
                "placeholders": [
                    {
                        "assetClass": "PROFILE",
                        "customFieldName": "PROFILE.firstName",
                        "displayName": "John"
                    }
                ],
                "example": [
                    "John"
                ],
                "carouselCards": [],
                "type": "HSM"
            }
        },
        "id": "69efaad06357c2c9885dc070",
        "name": "WhatsApp HSM template",
        "description": "Description for the template",
        "status": "Approved",
        "taxonomy": {
            "campaignId": "66000002_401",
            "tags": [
                "apiimport"
            ]
        },
        "insights": {},
        "validity": {
            "expiryTime": 2208988800000,
            "availableFrom": 1777248000000,
            "neverExpire": false,
            "visibleFrom": 1777248000000
        },
        "actionStats": {},
        "shareConfigs": [],
        "restricted": false,
        "locked": false,
        "createdTime": 1777314517702,
        "modifiedTime": 1777314517702,
        "langVsTranslatedFieldValues": {},
        "approvedByUser": 66014658,
        "createdByUser": 66014658
    },
    "errors": []
}



## Response Parameters



















































































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| assetType |  | Refers to the type of templateDefault Value for HSM: TEMPLATE_ASSET | String |
| templateAsset |  | Object containing the template asset details | Object |
|  | channelType | Channel type associated with the assetDefault: WHATSAPP_BUSINESS | String |
|  | templateType | Type of templateDefault: HSM | String |
|  | elementList | List of elements in the template | List [String, Integer] |
|  | buttons | Array containing button details | Array |
|  | attachments | Object containing attachment details | Object |
| id |  | Template Id used for backend tracking | String |
| name |  | Name of the template | String |
| description |  | Description of the template | String |
| status |  | Status of the template | String |
| taxonomy |  | Object containing taxonomy details | Object |
|  | campaignId | Campaign Id under which template is created | String |
|  | tags | Tags associated with the template | List [String] |
| insights |  | Object containing insights details | Object |
| validity |  | Object containing validity details | Object |
|  | expiryTime | Time at which template expires | Epoch |
|  | availableFrom | Time from which template is available | Epoch |
|  | neverExpire | If true, template never expires | Boolean |
|  | visibleFrom | Time from which template is visible on Sprinklr | Epoch |
| actionStats |  | Object containing actionable insights | Object |
| shareConfigs |  | Template share details (visibility) | List [String] |
| restricted |  | If true, template is restricted | Boolean |
| createdTime |  | Time template was created | Epoch |
| modifiedTime |  | Time template was last modified | Epoch |
| langVsTranslatedFieldValues |  | Sprinklr internal field (ignore) | Object |
| approvedByUser |  | User ID of approver | Integer |
| createdByUser |  | User ID of creator | Integer |

### `attachment` Object































































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| wabaTemplateId |  | WhatsApp template id | Integer |
| namespace |  | Unique identification string | String |
| wabaId |  | Unique identifier for WhatsApp Business Account (used to authenticate and associate the HSM template) | String |
| elementName |  | Element name for the attachment | String |
| category |  | Template categoryEnum: [UTILITY, MARKETING] | String |
| langCode |  | Language code for template | String |
| buttons |  | Array defining button details | Array |
|  | title | Title of the button | String |
|  | payload | Content of the button | String |
|  | actionDetail | Object containing actions performed when user clicks the button | Object |
| wabaTemplateStatus |  | Status of WhatsApp templateDefault: PENDING | String |
| message |  | Message posted back when button type is Text Post Back | String |
| footer |  | Footer text of the message | String |
| header |  | Object containing header details | Object |
|  | headerType | Type of header | String |
|  | message | Message of the header | String |
|  | placeHolders | Array containing dynamic content details for the header | Array |
| allowCategoryChange |  | If true, category auto‑changes based on template content during validation | Boolean |
| placeHolders |  | Array containing dynamic content details for the button | Array |
|  | assetClass | Asset class of the custom field used for header/button content | String |
|  | customFieldName | Custom field name used for header/button valueCan be fetched using Bootstrap API or field name doc | String |
|  | displayName | Display name of the custom field | String |
|  | example | Value assigned to the custom property | List [String/integer] |
| type |  | Type of templateDefault: HSM | String |

### `actionDetail` Object


















| Parameter | Description | Type |
| --- | --- | --- |
| postBackhandlerType | Type of action that needs to be performed | String |
| action | Action type performed when customer clicks the button       Supported Values:       • TEXT: Quick reply       • DIAL: Call‑to‑action button (Call)       • OPEN_URL: Call‑to‑action button (Open URL) | String |

## Sample Error Response




{
  "data": [],
  "errors": [
    {
      "id": "65ba175b48a0e416f2869387",
      "code": 400,
      "message": "Invalid parameter. Content in This Language Already Exists. There is already English content for this template. You can create a new template and try again."
    }
  ]
}




**Dev Notes:**



- Once the template is created, you’ll get notified through the *template created webhook*. This will be a real-time notification.

- You can refer to this document for sample webhook response payloads:
      [Template Asset Webhooks](https://developer.sprinklr.com/docs/read/webhooks/webhook_response_payload/Template_Asset_Webhooks)


- You can create and configure webhook subscriptions on the Sprinklr platform. Steps are mentioned here:
      [Create and Manage Webhook Subscription](https://www.sprinklr.com/help/articles/platform-modules/create-and-manage-webhook-subscription-in-sprinklr/633c5c2b59534970b26f96da)



## Appendix: Supported Language Codes

















































































| Language | Language Code |
| --- | --- |
| Afrikaans | af |
| Albanian | sq |
| Arabic | ar |
| Azerbaijani | az |
| Bengali | bn |
| Bulgarian | bg |
| Catalan | ca |
| Chinese (CHN) | zh_CN |
| Chinese (HKG) | zh_HK |
| Chinese (TAI) | zh_TW |
| Croatian | hr |
| Czech | cs |
| Danish | da |
| Dutch | nl |
| English | en |
| English (UK) | en_GB |
| English (US) | en_US |
| Estonian | et |
| Filipino | fil |
| Finnish | fi |
| French | fr |
| Georgian | ka |
| German | de |
| Greek | el |
| Gujarati | gu |
| Hausa | ha |
| Hebrew | he |
| Hindi | hi |
| Hungarian | hu |
| Indonesian | id |
| Irish | ga |
| Italian | it |
| Japanese | ja |
| Kannada | kn |
| Kazakh | kk |
| Kinyarwanda | rw_RW |
| Korean | ko |
| Kyrgyz (Kyrgyzstan) | ky_KG |
| Lao | lo |
| Latvian | lv |
| Lithuanian | lt |
| Macedonian | mk |
| Malay | ms |
| Malayalam | ml |
| Marathi | mr |
| Norwegian | nb |
| Persian | fa |
| Polish | pl |
| Portuguese (BR) | pt_BR |
| Portuguese (POR) | pt_PT |
| Punjabi | pa |
| Romanian | ro |
| Russian | ru |
| Serbian | sr |
| Slovak | sk |
| Slovenian | sl |
| Spanish | es |
| Spanish (ARG) | es_AR |
| Spanish (SPA) | es_ES |
| Spanish (MEX) | es_MX |
| Swahili | sw |
| Swedish | sv |
| Tamil | ta |
| Telugu | te |
| Thai | th |
| Turkish | tr |
| Ukrainian | uk |
| Urdu | ur |
| Uzbek | uz |
| Vietnamese | vi |
| Zulu | Zu |

## Response, Status and Error Codes































| Status Code | Description |
| --- | --- |
| 200 (OK) | Indicates the request was successful |
| 400 Bad Request | General client-side error |
| 400 Bad Request | Unsupported Parameter |
| 400 Bad Request | Missing Required Consumer Key |
| 400 Bad Request | Missing Required Request Token |
| 400 Bad Request | Missing Required Access Token |
| 504 Bad Request | Duplicated OAuth Protocol Parameter |
| 401 Unauthorized | Invalid Or Expired Token |
| 401 Unauthorized | Invalid Consumer Key |
| 403 Forbidden | Not Authorized |
| 403 Forbidden | Account Inactive |
| 403 Forbidden | Account Over Queries Per Second Limit |
| 403 Forbidden | Account Over Rate Limit |
| 403 Forbidden | Invalid Referer |
| 403 Forbidden | Rate Limit Exceeded |
| 403 Forbidden | Service Requires SSL |
| 414 Request-URI Too Long | Request URI exceeds length limit |
| 500 Internal Server Error | Server encountered an unexpected condition |
| 502 Bad Gateway | Invalid response from upstream server |
| 503 Service Unavailable | Scheduled Maintenance |
| 504 Gateway Timeout | Upstream server failed to respond in time |

[](https://dev.sprinklr.com/create-whatsapp-hsm-template) 

 

 
[Back to top](https://dev.sprinklr.com/create-whatsapp-hsm-template)
