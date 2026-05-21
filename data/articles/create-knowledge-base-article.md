---
title: "Create Knowledge Base Article"
slug: create-knowledge-base-article
url: https://dev.sprinklr.com/create-knowledge-base-article
---

# Create Knowledge Base Article

#
  POST - Create Knowledge Base Article


Using this API, you can create a knowledge base article within Sprinklr. These articles can then be recommended to customer care agents using AI-powered Smart Comprehend feature. This helps agents solve user queries on the care console or agent console, which, in turn, helps provide on-point and timely solutions to user queries.

**Dev Notes: **AI model training is required for enabling Smart Comprehend Recommendation feature. Please reach out to your success manager to enable this feature once the article has been added to your Sprinklr’s environment.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/create

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

****``

[list of language codes.](https://www.sprinklr.com/help/articles/translating-content/autotranslate-an-article/641adba2a1367f1be7db82d4#fcd36636-ec32-4947-b31f-b9a993825515)

[Update API](https://dev.sprinklr.com/update-knowledge-base-article)

****

****

****

****

****

****

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| tags |  | Optional | Refers to the list of tags you want to apply on the article | List [String] |
| folderMetadata |  | Required | Object containing the details about the folder the article is added to | Object |
|  | folderId | Required | Refers to the unique identifier for the folder where the article will be added.Refer to the note below for the steps to finding the folder Id from the Sprinklr's UI platform. | String |
| content |  | Required | Object containing the content details of the article | Object |
|  | title | OptionalNote: it is recommended to add a title to the article to clarify its intent | Refers to the title of the article | String |
|  | contentType | Required | Refers to the template of the article.Supported Values: KNOWN_ISSUE | String |
|  | markUpText | Required | The content of the article in HTML format | String |
| locale |  | Required | Refers to the language code of the article | String |
| lngVariants |  | OptionalRequired if you wish to translate the article in other languages | Refers to the  Empty placeholder articles are generated for the specified language codes and linked to the parent article. You can then use the  to add content to these articles by referencing their corresponding variant content IDs. | List [String] |
| publicContent |  | Optional | If true, the article will be visible to the end customer | Boolean |
| originType |  | OptionalNote: If the originType is not passed in the request payload, it will be set to SPRINKLR by default | There are two supported values for origin type,i.e.,EXTERNAL => articles imported in Sprinklr can only be viewedIMPORTED => articles imported in Sprinklr but can be edited | String |
| externalPermalink |  | Optional | Refers to the article’s URL | URL |
| status |  | OptionalNote: If status is not passed in the request payload, it will be automatically set to DRAFT | Supported Values: APPROVED, DRAFTAPPROVED => Articles which ready for publishing and will be included in ML training for smart recommendationDRAFT => Articles which needs work before publishing and will not be included in ML training for smart recommendation | String |

**Steps to Extract Folder Id from UI: **

- Search "Knowledge Base" from the universal search bar on the Sprinklr's homepage.
- Click on the knowledbase category/folder you need the Id for
- The category/folder Id will be part of the browser URL
- For example, if the browser URL is this "`https://sprinklr.com/care/knowledge-base/categories/65aa485c36fd937eb0a1d815` then "`65aa485c36fd937eb0a1d815`" is the folder Id.

## Example - Request




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/create' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
	  "tags": ["hello"],
   "folderMetadata": {
       "folderId": "62b5279ad7d5fb6f9cdb2d89"
   },
   "content": {
       "title": "Article 1",
       "contentType": "KNOWN_ISSUE",
       "markUpText":  "
Hello world
"
   },
   "locale": "en_US",
   "lngVariants":["fr_FR", "de_DE"],
   "publicContent": true,
   "originType": "EXTERNAL",
   "externalPermalink": "",
   "status": "APPROVED"
}'



## Example - Response





{
   "data": {
       "id": "63173f4a4cfa5258862f2af0",
       "version": 0,
       "contributors": [
           600038885
       ],
       "tags": [
           "hello"
       ],
       "content": {
           "contentType": "KNOWN_ISSUE",
           "contentSubType": "KB_ARTICLE",
           "title": "Article 1",
           "markUpText": "
Hello world
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
       "locale": "en_US",
       "grants": [
           "USER/600038885/OWNERSHIP",
           "CLIENT/2/OWNERSHIP"
       ],
       "clientId": 2,
       "ownerUserId": 600038885,
       "createdTime": "Sep 6, 2022 12:38:33 PM",
       "modifiedTime": "Sep 6, 2022 12:38:33 PM",
       "lastModifiedUserId": 600038885,
       "deleted": false,
       "folderMetadata": {
          "folderId": "62b5279ad7d5fb6f9cdb2d89",
           "confidential": false
       },
       "canEdit": false
   },
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
| id |  | The unique identifier for the knowledge base article created in Sprinklr | String |
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
| clientId |  | The workspace id where the article has been added | Integer |
| ownerUserId |  | User id of the Sprinklr user who created the article | Long |
| createdTime |  | The time at which the article was created | String |
| modifiedTime |  | The time at which the article was last modified | String |
| lastModifiedUserId |  | User id of the Sprinklr user who last modified the article | Long |
| deleted |  | If true, the article has been deleted | Boolean |
| folderMetaData |  | Object containing the details about the folder the article is added to | Object |
|  | folderId | Refers to the unique identifier for the folder where the article is added | String |
|  | confidential | If true, the article is confidentialDefault = false | Boolean |
| canEdit |  | If true, the article can be edited | Boolean |

[](https://dev.sprinklr.com/create-knowledge-base-article)




[Back to top](https://dev.sprinklr.com/create-knowledge-base-article)
