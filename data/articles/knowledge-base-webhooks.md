---
title: "Knowledge Base Webhooks"
slug: knowledge-base-webhooks
url: https://dev.sprinklr.com/knowledge-base-webhooks
---

# Knowledge Base Webhooks

#
 Knowledge Base Webhooks

 You can subscribe to the Knowledge Base webhooks using the subscription APIs or Sprinklr UI. Whenever a Knowledge Base action is performed such as creating, updating, or deleting of an article, Sprinklr sends an HTTP request triggered notification to the Webhook URL that you specified while creating the subscription.

	**Knowledge Base Webhook Subscriptions:** Content Created, Content Updated, Content Deleted

The following sections describe the response you get when any Knowlege Base Webhooks are triggered:


- [Knowledge Base Content Created Webhook](https://dev.sprinklr.com/knowledge-base-webhooks#kbContentCreated)

- [Knowledge Base Content Updated Webhook](https://dev.sprinklr.com/knowledge-base-webhooks#kbContentUpdated)

- [Knowledge Base Content Deleted Webhook](https://dev.sprinklr.com/knowledge-base-webhooks#kbContentDeleted)


## Knowledge Base Content Created Webhook


The following response is received when the Knowledge Base Content Created webhook is triggered:

#### JSON Response




  Copy Code

{
    "id": "67a30d1f6ea86f12972f925c",
    "type": "kb.content.created",
    "payload": {
        "content": {
            "id": "67a30d1f6ea86f12972f921c",
            "version": 0,
            "contributors": [
                66014658
            ],
            "content": {
                "contentType": "KNOWN_ISSUE",
                "contentSubType": "KB_ARTICLE"
            },
            "publicContent": false,
            "hasConditionalSection": false,
            "externalContent": false,
            "originType": "SPRINKLR",
            "favourite": false,
            "baseLngContentId": "67a30d1f6ea86f12972f91fd",
            "lngVariants": {},
            "inactiveLngVariants": {},
            "baseCountryContentId": "67a30d1f6ea86f12972f91fd",
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
                "livechatNotHelpfulCount": 0
            },
            "status": "DRAFT",
            "saveInLngVariantEsEnabled": false,
            "locale": "ar",
            "countryCodes": [
                "AF",
                "AU"
            ],
            "countryBaseContent": false,
            "linkedAssets": [],
            "languageSettingId": "6731ca93e7ab56644228905e",
            "grants": [
                "USER/66014658/OWNERSHIP",
                "CLIENT/66000002/OWNERSHIP"
            ],
            "clientId": 66000002,
            "ownerUserId": 66014658,
            "createdTime": "Feb 05, 2025, 07:02:55 AM",
            "modifiedTime": "Feb 05, 2025, 07:02:55 AM",
            "lastModifiedUserId": 66014658,
            "deleted": false,
            "folderMetadata": {
                "folderId": "67a30cff6ea86f12972f8571",
                "confidential": false
            },
            "canEdit": false
        }
    },
    "eventTime": 1738738975589,
    "subscriptionDetails": {
        "subscriptionId": "67a1e5203801371e9ffca308"
    }
}



### Response









































| Field Name | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the event. | String |
| type | Type of event triggered. | String |
| payload | The response payload of the event. | Object |
| content | Includes the details of the content. For more information, see the Content table. | Object |
| eventTime | Timestamp when the event occurred. | Integer |
| subscriptionDetails | ID of the subscription for the event. | String |

#### Content Object




































































































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the content item. | String |
| version | Version of the content. | Integer |
| contributors | List of contributor IDs associated with the content creation. | Array |
| content | Specifies the type and subtype of the content. | Object |
| publicContent | Indicates whether the content is public | Boolean |
| hasConditionalSection | Indicates if the content has any conditional section. | Boolean |
| externalContent | Indicates if the content comes from an external source. | Boolean |
| originType | Indicates the origin of the content. | String |
| favourite | Indicates whether the content is marked as a favorite. | Boolean |
| baseLngContentId | The ID of the base language. | String |
| lngVariants | Language variants for the content. |  |
| inactiveLngVariants | Inactive language variants for the content |  |
| baseCountryContentId | The ID of the base country. | Object |
| countryVariants | The country-specific content ID for different countries. | Object |
| stats | Various statistics about the content such as recommendations, usage count, ratings, view counts, and helpfulness ratings. | Object |
| status | The current status of the Knowledge Base article. | String |
| saveInLngVariantEsEnabled | Indicates whether saving language variants in a specific variant setting is enabled | Boolean |
| locale | The language for the content. | String |
| countryCodes | List of country codes where the content is applicable. | Array |
| countryBaseContent | Indicates if the content is base country content. | Boolean |
| linkedAssets | Any assets linked to the content. | Array |
| languageSettingId | ID for the language setting for the content. | String |
| grants | Shows which users/clients have ownership or access to the content. | Array |
| clientId | ID of the client that owns the content. | Integer |
| ownerUserId | ID of the user who owns the content. | Integer |
| createdTime | The timestamp when the content was created. | String |
| modifiedTime | The timestamp when the content was last modified. | String |
| lastModifiedUserId | ID of the user who last modified the content. | Integer |
| deleted | Indicates if the content is deleted. | Boolean |
| folderMetadata | Metadata for the folder in which the content is stored, such as folder ID and confidentiality status. | Object |
| canEdit | Indicates whether the content is editable. | Boolean |

### Content



















| Parameter | Description | Type |
| --- | --- | --- |
| contentType | Indicates the type of the content. | string |
| contentSubType | Indicates the subtype of the content. | string |

### Stats










































































| Parameter | Description | Type |
| --- | --- | --- |
| recommendCount | Number of times the content was recommended. | Integer |
| usageCount | Total number of times the item was used. | Integer |
| ratingCount | Number of ratings submitted. | Integer |
| ratingAvg | Average rating score based on ratingCount. | Integer |
| agentViewCount | Number of times agents viewed the item. | Integer |
| communityViewCount | Number of times community users viewed the item. | Integer |
| livechatViewCount | Number of views from Live Chat interactions. | Integer |
| helpfulCount | Number of times users marked the item as helpful. | Integer |
| notHelpfulCount | Number of times users marked the item as not helpful. | Integer |
| communityHelpfulCount | Number of helpful votes from community users. | Integer |
| communityNotHelpfulCount | Number of not helpful votes from community users. | Integer |
| livechatHelpfulCount | Number of helpful votes from Live Chat interactions. | Integer |
| livechatNotHelpfulCount | Number of not helpful votes from Live Chat interactions. | Integer |


## Knowledge Base Content Updated Webhook


The following response is received when the Knowledge Base Content Updated webhook is triggered:

#### JSON Response




  Copy Code

{
    "id": "67a30f1d6ea86f12973059e3",
    "type": "kb.content.updated",
    "payload": {
        "content": {
            "id": "67a30d1f6ea86f12972f91fd",
            "version": 3,
            "contributors": [
                66014658
            ],
            "tags": [],
            "content": {
                "contentType": "KNOWN_ISSUE",
                "contentSubType": "KB_ARTICLE",
                "title": "Knowledge Base Created Webhook",
                "markUpText": "
The KB article is now updated.
"
            },
            "publicContent": false,
            "hasConditionalSection": false,
            "externalContent": false,
            "originType": "SPRINKLR",
            "favourite": false,
            "lngVariants": {
                "ar": "67a30d1f6ea86f12972f921c",
                "en": "67a30d1f6ea86f12972f921b"
            },
            "inactiveLngVariants": {},
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
                "livechatNotHelpfulCount": 0
            },
            "status": "DRAFT",
            "saveInLngVariantEsEnabled": false,
            "locale": "en_US",
            "countryCodes": [
                "AF",
                "AU"
            ],
            "countryBaseContent": false,
            "linkedAssets": [],
            "translationProcess": {
                "updateTime": 1738739485736,
                "newContentAvailableForTranslation": true,
                "authorId": 66014658
            },
            "languageSettingId": "6731ca93e7ab56644228905e",
            "denseVectors": {
                "en_KB_STANDARD_v0": [
                    0.023378057,
                    -0.032323185,
                    0.0118803,
                    0.011562509,
                    -0.056214802,
                    -0.040111985,
                    0.006486132,
                    0.011158819,
                    0.06890015,
                    -0.040861987,
                    -0.06601865,
                    -0.00281261,
                    -0.057701945,
                    0.050235964,
                    0.012409062,
                    -0.006532202
                ]
            },
            "eventTime": 1738739669176,
            "subscriptionDetails": {
                "subscriptionId": "67a30f9b6ea86f1297308bbf"
            }
        }
    }
}



### Response









































| Field Name | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the event. | String |
| type | Type of event triggered. | String |
| payload | The response payload of the event. | Object |
| content | Includes the details of the content. For more information, see the Content table. | Object |
| eventTime | Timestamp when the event occurred. | Integer |
| subscriptionDetails | ID of the subscription for the event. | String |

#### Content Object




























































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the content item. | String |
| version | Version of the content. | Integer |
| contributors | List of contributor IDs associated with the content creation. | Array |
| content | Specifies the type and subtype of the content. | Object |
| publicContent | Indicates whether the content is public | Boolean |
| hasConditionalSection | Indicates if the content has any conditional section. | Boolean |
| externalContent | Indicates if the content comes from an external source. | Boolean |
| originType | Indicates the origin of the content. | String |
| favourite | Indicates whether the content is marked as a favorite. | Boolean |
| baseLngContentId | The ID of the base language. | String |
| lngVariants | Language variants for the content. |  |
| inactiveLngVariants | Inactive language variants for the content |  |
| baseCountryContentId | The ID of the base country. | Object |
| countryVariants | The country-specific content ID for different countries. | Object |
| stats | Various statistics about the content such as recommendations, usage count, ratings, view counts, and helpfulness ratings. | Object |
| status | The current status of the Knowledge Base article. | String |
| saveInLngVariantEsEnabled | Indicates whether saving language variants in a specific variant setting is enabled | Boolean |
| locale | The language for the content. | String |
| countryCodes | List of country codes where the content is applicable. | Array |
| countryBaseContent | Indicates if the content is base country content. | Boolean |
| linkedAssets | Any assets linked to the content. | Array |
| translationProcess | Contains details about the translation process. | Object |
| denseVectors | Stores dense vector representations of the content. | Object |

#### Content





























| Parameter | Description | Type |
| --- | --- | --- |
| contentType | Indicates the type of the content. | String |
| contentSubType | Title of the content. | String |
| title | Indicates the subtype of the content. | string |
| markUpText | HTML-formatted text content. | String |

#### Stats










































































| Parameter | Description | Type |
| --- | --- | --- |
| recommendCount | Number of times the content was recommended. | Integer |
| usageCount | Total number of times the item was used. | Integer |
| ratingCount | Number of ratings submitted. | Integer |
| ratingAvg | Average rating score based on ratingCount. | Integer |
| agentViewCount | Number of times agents viewed the item. | Integer |
| communityViewCount | Number of times community users viewed the item. | Integer |
| livechatViewCount | Number of views from Live Chat interactions. | Integer |
| helpfulCount | Number of times users marked the item as helpful. | Integer |
| notHelpfulCount | Number of times users marked the item as not helpful. | Integer |
| communityHelpfulCount | Number of helpful votes from community users. | Integer |
| communityNotHelpfulCount | Number of not helpful votes from community users. | Integer |
| livechatHelpfulCount | Number of helpful votes from Live Chat interactions. | Integer |
| livechatNotHelpfulCount | Number of not helpful votes from Live Chat interactions. | Integer |

#### translationProcess
























| Parameter | Description | Type |
| --- | --- | --- |
| updateTime | Timestamp of the last translation update. | Integer |
| newContentAvailableForTranslation | Indicates if new content is available for translation. | Boolean |
| authorId | User ID of the author. | Integer |

## Knowledge Base Content Deleted Webhook


The following response is received when the Knowledge Base Content Deleted webhook is triggered:

#### JSON Response




  Copy Code

{
    "id": "67a30fd56ea86f129730a4e1",
    "type": "kb.content.deleted",
    "payload": {
        "content": {
            "id": "67a30d1f6ea86f12972f921b",
            "version": 1,
            "contributors": [
                66014658
            ],
            "content": {
                "contentType": "KNOWN_ISSUE",
                "contentSubType": "KB_ARTICLE"
            },
            "publicContent": false,
            "hasConditionalSection": false,
            "externalContent": false,
            "originType": "SPRINKLR",
            "favourite": false,
            "baseLngContentId": "67a30d1f6ea86f12972f91fd",
            "lngVariants": {},
            "inactiveLngVariants": {},
            "baseCountryContentId": "67a30d1f6ea86f12972f91fd",
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
                "livechatNotHelpfulCount": 0
            },
            "status": "DRAFT",
            "saveInLngVariantEsEnabled": false,
            "locale": "en",
            "countryCodes": [
                "AF",
                "AU"
            ],
            "countryBaseContent": false,
            "linkedAssets": [],
            "languageSettingId": "6731ca93e7ab56644228905e",
            "grants": [
                "USER/66014658/OWNERSHIP",
                "CLIENT/66000002/OWNERSHIP"
            ],
            "clientId": 66000002,
            "ownerUserId": 66014658,
            "createdTime": "Feb 05, 2025, 07:02:55 AM",
            "modifiedTime": "Feb 05, 2025, 07:14:29 AM",
            "lastModifiedUserId": 66014658,
            "deleted": true,
            "folderMetadata": {
                "folderId": "67a30cff6ea86f12972f8571",
                "confidential": false
            },
            "canEdit": false
        }
    },
    "eventTime": 1738739669176,
    "subscriptionDetails": {
        "subscriptionId": "67a30f9b6ea86f1297308bbf"
    }
}



### Response









































| Field Name | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the event. | String |
| type | Type of event triggered. | String |
| payload | The response payload of the event. | Object |
| content | Includes the details of the content. For more information, see the Content table. | Object |
| eventTime | Timestamp when the event occurred. | Integer |
| subscriptionDetails | ID of the subscription for the event. | String |

#### Content Object




































































































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the content item. | String |
| version | Version of the content. | Integer |
| contributors | List of contributor IDs associated with the content creation. | Array |
| content | Specifies the type and subtype of the content. | Object |
| publicContent | Indicates whether the content is public | Boolean |
| hasConditionalSection | Indicates if the content has any conditional section. | Boolean |
| externalContent | Indicates if the content comes from an external source. | Boolean |
| originType | Indicates the origin of the content. | String |
| favourite | Indicates whether the content is marked as a favorite. | Boolean |
| baseLngContentId | The ID of the base language. | String |
| lngVariants | Language variants for the content. |  |
| inactiveLngVariants | Inactive language variants for the content |  |
| baseCountryContentId | The ID of the base country. | Object |
| countryVariants | The country-specific content ID for different countries. | Object |
| stats | Various statistics about the content such as recommendations, usage count, ratings, view counts, and helpfulness ratings. | Object |
| status | The current status of the Knowledge Base article. | String |
| saveInLngVariantEsEnabled | Indicates whether saving language variants in a specific variant setting is enabled | Boolean |
| locale | The language for the content. | String |
| countryCodes | List of country codes where the content is applicable. | Array |
| countryBaseContent | Indicates if the content is base country content. | Boolean |
| linkedAssets | Any assets linked to the content. | Array |
| languageSettingId | ID for the language setting for the content. | String |
| grants | Shows which users/clients have ownership or access to the content. | Array |
| clientId | ID of the client that owns the content. | Integer |
| ownerUserId | ID of the user who owns the content. | Integer |
| createdTime | The timestamp when the content was created. | String |
| modifiedTime | The timestamp when the content was last modified. | String |
| lastModifiedUserId | ID of the user who last modified the content. | Integer |
| deleted | Indicates if the content is deleted. | Boolean |
| folderMetadata | Metadata for the folder in which the content is stored, such as folder ID and confidentiality status. | Object |
| canEdit | Indicates whether the content is editable. | Boolean |

#### Content



















| Parameter | Description | Type |
| --- | --- | --- |
| contentType | Indicates the type of the content. | string |
| contentSubType | Indicates the subtype of the content. | string |

#### Stats










































































| Parameter | Description | Type |
| --- | --- | --- |
| recommendCount | Number of times the content was recommended. | Integer |
| usageCount | Total number of times the item was used. | Integer |
| ratingCount | Number of ratings submitted. | Integer |
| ratingAvg | Average rating score based on ratingCount. | Integer |
| agentViewCount | Number of times agents viewed the item. | Integer |
| communityViewCount | Number of times community users viewed the item. | Integer |
| livechatViewCount | Number of views from Live Chat interactions. | Integer |
| helpfulCount | Number of times users marked the item as helpful. | Integer |
| notHelpfulCount | Number of times users marked the item as not helpful. | Integer |
| communityHelpfulCount | Number of helpful votes from community users. | Integer |
| communityNotHelpfulCount | Number of not helpful votes from community users. | Integer |
| livechatHelpfulCount | Number of helpful votes from Live Chat interactions. | Integer |
| livechatNotHelpfulCount | Number of not helpful votes from Live Chat interactions. | Integer |

 [](https://dev.sprinklr.com/knowledge-base-webhooks)

[Back to top](https://dev.sprinklr.com/knowledge-base-webhooks)
