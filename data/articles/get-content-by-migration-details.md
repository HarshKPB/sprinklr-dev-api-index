---
title: "Get Content by Migration Details"
slug: get-content-by-migration-details
url: https://dev.sprinklr.com/get-content-by-migration-details
---

# Get Content by Migration Details

#
  GET - Get Content by Migration Details



Using this API, you can fetch the migration details for an existing and migrated knowledge base article. Please note that you can use [create knowledge base API](https://dev.sprinklr.com/create-knowledge-base-article) to set migration details for an article.

## API Endpoint


https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/find-content-by-migration-details

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
| migratedId | Required | Refers to the unique identifier for migration Id that was configured while creating the article. | String |
| migratedFrom | Required | Refers to the source from where the article is migrated and is configured while creating the article. | String |

## Example - Request




 Copy Code



curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/knowledgebase/find-content-by-migration-details?migratedId=hi_IN_test_migrated_id_api3&migratedFrom=SPRINKLR' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

## Example - Response




{
    "data": [
        {
            "id": "643ef350a56aae2db6e83b36",
            "version": 0,
            "contributors": [
                600038885
            ],
            "content": {
                "contentType": "KNOWN_ISSUE",
                "contentSubType": "KB_ARTICLE",
                "title": "testing for migratedId api",
                "markUpText": "
# The 75 Best Manga of All Time

Many Western readers understand the term “manga” to simply mean “Japanese comic books” — but in fact, manga has an incredibly rich history that stretches all the way back to the *12th century*. While the Western literary canon was largely confined to prose-centric novels until the rise of comics in the 1930s, Japanese storytellers have been embracing the power of combining pictures and words for centuries.

With all that history to pull from, it’s no wonder the world of manga is such a varied literary landscape. From fantasy adventure to autobiographical comics to historical fiction to, yes, superheroes and monsters, manga has stories for readers of every genre and age.

But if you’re new to manga, the sheer number of stories available can feel overwhelming. That’s where we come in — we’ve taken this huge field and narrowed it down to the 75 best manga stories. There’s still an incredible amount of choice within our list, but with this guide in hand, you’ll be able to find the stories that suit your tastes, and get started with this incredible form of storytelling. Let’s get reading!

*If you're feeling overwhelmed by the number of great manga out there, you can also take our 10-second quiz below to narrow it down quickly and get a personalized manga recommendation *😉

​

​

Many Western readers understand the term “manga” to simply mean “Japanese comic books” — but in fact, manga has an incredibly rich history that stretches all the way back to the *12th century*. While the Western literary canon was largely confined to prose-centric novels until the rise of comics in the 1930s, Japanese storytellers have been embracing the power of combining pictures and words for centuries.

With all that history to pull from, it’s no wonder the world of manga is such a varied literary landscape. From fantasy adventure to autobiographical comics to historical fiction to, yes, superheroes and monsters, manga has stories for readers of every genre and age.

But if you’re new to manga, the sheer number of stories available can feel overwhelming. That’s where we come in — we’ve taken this huge field and narrowed it down to the 75 best manga stories. There’s still an incredible amount of choice within our list, but with this guide in hand, you’ll be able to find the stories that suit your tastes, and get started with this incredible form of storytelling. Let’s get reading!

*If you're feeling overwhelmed by the number of great manga out there, you can also take our 10-second quiz below to narrow it down quickly and get a personalized manga recommendation *😉

​

​

​

Many Western readers understand the term “manga” to simply mean “Japanese comic books” — but in fact, manga has an incredibly rich history that stretches all the way back to the *12th century*. While the Western literary canon was largely confined to prose-centric novels until the rise of comics in the 1930s, Japanese storytellers have been embracing the power of combining pictures and words for centuries.

With all that history to pull from, it’s no wonder the world of manga is such a varied literary landscape. From fantasy adventure to autobiographical comics to historical fiction to, yes, superheroes and monsters, manga has stories for readers of every genre and age.

But if you’re new to manga, the sheer number of stories available can feel overwhelming. That’s where we come in — we’ve taken this huge field and narrowed it down to the 75 best manga stories. There’s still an incredible amount of choice within our list, but with this guide in hand, you’ll be able to find the stories that suit your tastes, and get started with this incredible form of storytelling. Let’s get reading!

*If you're feeling overwhelmed by the number of great manga out there, you can also take our 10-second quiz below to narrow it down quickly and get a personalized manga recommendation *😉
"
            },
            "publicContent": false,
            "hasConditionalSection": false,
            "externalContent": false,
            "originType": "SPRINKLR",
            "favourite": false,
            "lngVariants": {},
            "countryVariants": {},
            "stats": {
                "recommendCount": 0,
                "usageCount": 0,
                "ratingCount": 0,
                "ratingAvg": 0.0,
                "agentViewCount": 0,
                "communityViewCount": 0,
                "livechatViewCount": 0,
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
            "partnerCustomProperties": {
                "_c_62a1cf903df8d74b0e283e57": [
                    "hi_IN_test_migrated_id_api3"
                ]
            },
            "status": "DRAFT",
            "saveInLngVariantEsEnabled": false,
            "locale": "hi_IN",
            "countryBaseContent": false,
            "migrationDetails": {
                "migratedFrom": "NETFLIX",
                "migratedId": "hi_IN_test_migrated_id_api3"
            },
            "linkedAssets": [],
            "grants": [
                "USER/600038885/OWNERSHIP",
                "CLIENT/2/OWNERSHIP"
            ],
            "clientId": 2,
            "ownerUserId": 600038885,
            "createdTime": "Apr 18, 2023, 7:45:19 PM",
            "modifiedTime": "Apr 18, 2023, 7:45:19 PM",
            "lastModifiedUserId": 600038885,
            "deleted": false,
            "folderMetadata": {
                "folderId": "643ec1b969de7c6231e8ee7b",
                "confidential": false
            },
            "canEdit": false
        }
    ],
    "errors": []
}
 

     
     
   

[](https://dev.sprinklr.com/get-content-by-migration-details) 

 

 
[Back to top](https://dev.sprinklr.com/get-content-by-migration-details)
