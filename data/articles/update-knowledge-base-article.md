---
title: "Update Knowledge Base Article"
slug: update-knowledge-base-article
url: https://dev.sprinklr.com/update-knowledge-base-article
---

# Update Knowledge Base Article

#
  POST - Update Knowledge Base Article


Using this API, you can update a knowledge base article existing within Sprinklr. Once updated with latest information, these articles can then be recommended to customer care agents using AI-powered Smart Comprehend feature. This helps agents solve user queries on the care console or agent console, which, in turn, helps provide on-point and timely solutions to user queries.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/update

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

### Request Parameters













****
-
-
-
-
-
-

****

****

****

****

****

****

****

``
****

``
****

- ****
-
****

````

****

[list of language codes.](https://www.sprinklr.com/help/articles/translating-content/autotranslate-an-article/641adba2a1367f1be7db82d4#fcd36636-ec32-4947-b31f-b9a993825515)
````
****
****

****

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| updateActions |  | Required | Refers to the type of update actionSome of the supported update actions:    CONTENT: Allows you to update the content of Knowledge Base articles.   STATUS: Allows you to update the status of Knowledge Base articles, such as DRAFT, APPROVED, etc.   EXTERNAL_PERMALINK: Allows you to update the external permalink of Knowledge Base articles.   SYNC_TAGS: Allows you to update the tags associated with Knowledge Base articles.   SYNC_SELECTED_CUSTOM_PROPERTIES: Allows you to update the Custom Field values associated with Knowledge Base articles.   ADD_LANGUAGE_VARIANT: Allows you to add language variants/translations to Knowledge Base articles. | List [String] |
| contentIds |  | Required | Refers to the content ids you want to update.You can fetch the content Id from the create knowledge base article API response.If you pass the content id of the base article, the base article will be updated.If you pass the content id of any existing language variant, that particular article variant will get updated. | List [String] |
| content |  | Required | Object containing the content details of the article. Example:          {     "updateActions": [     "CONTENT"     ],   "contentIds": [     "6319eb3f4cfa5258862fd7ec"   ],   "content": {     "contentSubType": "KB_ARTICLE",     "contentType": "KNOWN_ISSUE",     "title": "Hello World",     "markUpText": "qwertyuiop[ertyp"   } }' | Object |
|  | contentSubType | Optional | Refers to the subtype of the content.Default = KB_ARTICLE | String |
|  | contentType | Required | Refers to the template of the article.Supported Values: KNOWN_ISSUE | string |
|  | title | Optional | Refers to the title of the article | String |
|  | markUpText | Required | The update content of the article in html format | String |
| status |  | OptionalNote: If status is not passed in the request payload, it will be automatically set to default | Supported Values: APPROVED, DRAFTAPPROVED => Articles which ready for publishing and will be included in ML training for smart recommendationDRAFT => Articles which needs work before publishing and will not be included in ML training for smart recommendation. Example:          { 	 "updateActions": [    "STATUS"   ],   "contentIds": [    "6319eb3f4cfa5258862fd7ec"  ]  "status": "APPROVED" }' | String |
| externalPermalink |  | Optional | The external URL of the article. Use this parameter with the EXTERNAL_PERMALINK update action. Example:          {   "updateActions": [     "EXTERNAL_PERMALINK"   ],   "contentIds": [     "65604121f29dcf013bfee514"   ],   "externalPermalink": "https://help.sprinklr.com/new-external-permalink" } | URL |
| syncedTags |  | Optional | An array containing the tags you want to associate with the article.Use this parameter with the SYNC_TAGS update action.    Dev Notes:   Consider the following points:        If tags already exist, this field will override the existing tags and will not append new ones.     If the new Tag Manager is enabled for your account, you cannot use this API to add or update tags.     Example:          {     "syncedTags": [         "test manually",         "api test"     ],     "updateActions": [         "SYNC_TAGS"     ],     "contentIds": [         "69170dc6e6c4de634964579d"     ],     ... } | Array |
| selectedCustomProperties |  | Optional | Object containing the custom properties applicable at the global level. Use this parameter with the SYNC_SELECTED_CUSTOM_PROPERTIES update action. Replace value with the actual value for the Custom Field. Example:          {   "contentIds": [     "695d2d10ae6bf8662358a3f7"   ],   "updateActions": [     "SYNC_SELECTED_CUSTOM_PROPERTIES"   ],   "selectedCustomProperties": {     "_c_666c4fe839e2966639eaa2b2": [       "value"     ]   } } | Object |
| lngVariants |  | Optional.Required if you wish to add language variants/translations to the parent Knowledge Base article. | Refer to the Use this parameter with the ADD_LANGUAGE_VARIANT update action. Specify the required language codes in the lngVariants field. Example:          {   "contentIds": [     "695d2d10ae6bf8662358a3f7"   ],   "updateActions": [     "ADD_LANGUAGE_VARIANT"   ],   "lngVariants": ["en", "ar"] }         Note: When adding new language variants, specify only the language codes for the new variants you want to add. | List [String] |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/update' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
	 "updateActions": [
   "CONTENT",
   "STATUS"
  ],
 "contentIds": [
   "6319eb3f4cfa5258862fd7ec"
 ],
 "content": {
   "contentSubType": "KB_ARTICLE",
   "contentType": "KNOWN_ISSUE",
   "title": "Hello World",
   "markUpText": "
qwertyuiop[ertyp
"
 },
 "status": "APPROVED"
}'






## Example - Response





{
   "data": [
       {
           "id": "6319eb3f4cfa5258862fd7ec",
           "version": 4,
           "contributors": [
               600004599,
               600038885
           ],
           "tags": [
               "hello"
           ],
           "content": {
               "contentType": "KNOWN_ISSUE",
               "contentSubType": "KB_ARTICLE",
               "title": "Hello World",
               "markUpText": "
qwertyuiop[ertyp
"
           },
           "publicContent": true,
           "hasConditionalSection": false,
           "externalContent": false,
           "originType": "EXTERNAL",
           "favourite": false,
           "lngVariants": {
               "de_DE": "6319eb3f4cfa5258862fd7f7",
               "fr_FR": "6319eb3f4cfa5258862fd7f6"
           },
           "externalPermalink": "",
           "stats": {
               "recommendCount": 0,
               "usageCount": 0,
               "ratingCount": 0,
               "ratingAvg": 0.0,
               "agentViewCount": 0,
               "communityViewCount": 0,
               "helpfulCount": 0,
               "notHelpfulCount": 0,
               "communityHelpfulCount": 0,
               "communityNotHelpfulCount": 0,
               "livechatHelpfulCount": 0,
               "livechatNotHelpfulCount": 0,
               "externalViewCount": 0,
               "externalHelpfulCount": 0,
               "externalNotHelpfulCount": 0
           },
           "status": "APPROVED",
           "saveInLngVariantEsEnabled": false,
           "locale": "ar_SA",
           "grants": [
               "USER/600038885/OWNERSHIP",
               "CLIENT/2/OWNERSHIP"
           ],
           "clientId": 2,
           "ownerUserId": 600038885,
           "createdTime": "Sep 8, 2022 1:16:47 PM",
           "modifiedTime": "Sep 8, 2022 2:04:56 PM",
           "lastModifiedUserId": 600004599,
           "deleted": false,
           "folderMetadata": {
               "folderId": "62b5279ad7d5fb6f9cdb2d89",
               "confidential": false
           },
           "canEdit": false
       }
   ],
   "errors": []
}







### Response Parameters












****

**
**

****

****

****

****

****

****

| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | The unique identifier for the knowledge base article updated in Sprinklr | String |
| version |  | Refers to the current version of the articleDefault= 0 | Integer |
| contributors |  | Refers to the list of user ids of users who have edited the article | List [integer] |
| tags |  | Refers to the list of tags applied to the article | List [String] |
| content |  | Object containing the content details of the article | Object |
|  | contentType | Refers to the template of the articleSupported Values: KNOWN_ISSUE | String |
|  | contentSubType | Refers to the subtype of the contentDefault = KB_ARTICLE | String |
|  | title | Refers to the title of the article | String |
|  | markUpText | The content of the article in HTML format | String |
| publicContent |  | If true, the article will be visible to the end customer | Boolean |
| hasConditionalSection |  | If true, this shows a particular section of the article only to selected users | Boolean |
| originType |  | There are two supported values for origin type,i.e.,EXTERNAL => articles imported in sprinklr can only be viewedIMPORTED => articles imported in sprinklr but can be edited | String |
| favourite |  | If true, the article is marked as favourite | Boolean |
| lngVariants |  | Object containing the language code and its respective id | Object |
| externalPermalink |  | The public url of the article imported | Url |
| stats |  | Refers to the article stats | Object |
|  | agentViewCount | Refers to the number of times customer care agents have viewed the article | Integer |
|  | communityViewCount | The number of times the article has been viewed on the community console | Integer |
|  | helpfulCount | Refers to the number of times the article has been marked as helpful content | Integer |
|  | notHelpfulCount | Refers to the number of times the article has been marked as not helpful content | Integer |
|  | communityhelpfulCount | Refers to the number of times the article has been marked as helpful content on the community forum | Integer |
|  | communityNothelpfulCount | Refers to the number of times the article has been marked as not helpful content on the community forum | Integer |
|  | liveChatHelpfulCount | Refers to the number of times the article has been marked as helpful content on live chat | Integer |
|  | liveChatNotHelpfulCount | Refers to the number of times the article has been marked as not helpful content on live chat | Integer |
|  | externalViewCount | Represents the total number of times the content has been viewed by external users. The count increments each time the article is accessed through an external channel, excluding views by internal agents. | Integer |
|  | externalHelpfulCount | Indicates the number of external users who marked the content as helpful. This value usually reflects positive feedback gathered from public or externally accessible interfaces. | Integer |
|  | externalNotHelpfulCount | Indicates the number of external users who marked the content as not helpful. This captures negative feedback and helps evaluate content quality or relevance from an external audience. | Integer |
| status |  | Supported Values: APPROVED, DRAFTAPPROVED => Articles which ready for publishing and will be included in ML training for smart recommendationDRAFT => Articles which needs work before publishing and will not be included in ML training for smart recommendation | String |
| locale |  | Refers to the language code of the article | String |
| clientId |  | The workspace id where the article has been added and updated | Integer |
| ownerUserId |  | User id of the Sprinklr user who created the article | Long |
| createdTime |  | The time at which the article was created | String |
| modifiedTime |  | The time at which the article was last modified | String |
| lastModifiedUserId |  | User id of the Sprinklr user who last modified the article | Long |
| deleted |  | If true, the article has been deleted | Boolean |
| folderMetaData |  | Object containing the details about the folder the article is added to | Object |
|  | folderId | Refers to the unique identifier for the folder where the article is added | String |
|  | confidential | If true, the article is confidentialDefault = false | Boolean |
| canEdit |  | If true, the article can be edited | Boolean |

[](https://dev.sprinklr.com/update-knowledge-base-article) 

 

 
[Back to top](https://dev.sprinklr.com/update-knowledge-base-article)
