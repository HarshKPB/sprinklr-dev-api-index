---
title: "Save Knowledge Base Content"
slug: save-knowledge-base-content
url: https://dev.sprinklr.com/save-knowledge-base-content
---

# Save Knowledge Base Content

#
  POST - Save Knowledge Base Content



Using this API, you can create a new knowledge base article content or update an existing one.

**Dev Notes: **For updating an existing article, you can either pass the version and content Id of the article or specify the migration details such as migratedId and migratedFrom.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/save

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












****``

****``

****

****
****
- ``
- ``


****

























****
****
- ``
- ``

[knowledge base article](https://www.sprinklr.com/help/articles/import-and-export/import-external-content-to-sprinklr-knowledge-base-html-import/63d517692c015d03d4e7fed1#aac6e0f0-7373-4497-b1bd-2a0f494f8ba4)

****


****

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| content |  | Required | Object containing the content details of the article | Object |
|  | contentType | Required | Refers to the template of the article.Supported Values: KNOWN_ISSUE | String |
|  | contentSubType | Optional | Refers to the subtype of the contentDefault Value: KB_ARTICLE | String |
|  | title | OptionalNote: It is recommended to add a title to the article to clarify its intent | Refers to the title of the article | String |
|  | markUpText | Required | The content of the article in HTML format | String |
| publicContent |  | Optional | If true, the article will be visible to the end customer | Boolean |
| hasConditionalSection |  | Optional | If true, this shows a particular section of the article only to selected users | Boolean |
| originType |  | OptionalNote: If the originType is not passed in the request payload, it will be set to SPRINKLR by default | Supported Values: EXTERNAL, IMPORTED   EXTERNAL: Articles imported in Sprinklr can only be viewed.IMPORTED: Articles imported in Sprinklr but can be edited. | String |
| favourite |  | Optional | If true, the article is marked as favourite | Boolean |
| lngVariants |  | Optional | Object containing the language code and its respective id | List [string] |
| countryVariants |  | Optional | Object containing the ISO country codes | List [String] |
| stats |  | Optional | Refers to the article stats. Note: Only used when updating an existing article. | Object |
|  | agentViewCount | Optional | Refers to the number of times customer care agents have viewed the article | Integer |
|  | communityViewCount | Optional | The number of times the article has been viewed on the community console | Integer |
|  | helpfulCount | Optional | Refers to the number of times the article has been marked as helpful content | Integer |
|  | notHelpfulCount | Optional | Refers to the number of times the article has been marked as not helpful content | Integer |
|  | communityhelpfulCount | Optional | Refers to the number of times the article has been marked as helpful content on the community forum | Integer |
|  | communityNothelpfulCount | Optional | Refers to the number of times the article has been marked as not helpful content on the community forum | Integer |
|  | liveChatHelpfulCount | Optional | Refers to the number of times the article has been marked as helpful content on live chat | Integer |
|  | liveChatNotHelpfulCount | Optional | Refers to the number of times the article has been marked as not helpful content on live chat | Integer |
|  | recommendCount | Optional | Refers to the number of times the article has been recommended | Integer |
|  | usageCount | Optional | Refers to the number of times the article has been used or accessed | Integer |
|  | ratingCount | Optional | Refers to the number of ratings given to the article | Integer |
|  | ratingAvg | Optional | Refers to the average rating of the article | Integer |
|  | externalViewCount | Optional | Represents the total number of times the content has been viewed by external users. The count increments each time the article is accessed through an external channel, excluding views by internal agents. | Integer |
|  | externalHelpfulCount | Optional | Indicates the number of external users who marked the content as helpful. This value usually reflects positive feedback gathered from public or externally accessible interfaces. | Integer |
|  | externalNotHelpfulCount | Optional | Indicates the number of external users who marked the content as not helpful. This captures negative feedback and helps evaluate content quality or relevance from an external audience. | Integer |
| partnerCustomProperties |  | Optional | Object containing the custom properties applicable at the global level | Object |
| status |  | OptionalNote: If status is not passed in the request payload, it will be automatically set to DRAFT | Supported Values: APPROVED, DRAFT   APPROVED: Articles that are ready for publishing and will be included in ML training for smart recommendations.DRAFT: Articles that need work before publishing and will not be included in ML training for smart recommendations. | String |
| locale |  | Required | Enum: 					 						[JAPANESE - ja_JP, ARABIC_SAUDI_ARABIA - ar_SA, ARABIC_EGYPT - ar_EG, ENGLISH_GREAT_BRITAIN - en_GB, ENGLISH_UNITED_STATES - en_US, ENGLISH_INDIA - en_IN, PORTUGUESE_BRAZIL - pt_BR, CHINESE - zh_CN, HINDI_INDIA - hi_IN, TAMIL_INDIA - ta_IN, TELUGU_INDIA - te_IN, GERMAN_GERMANY - de_DE, SPANISH_SPAIN - es_ES, FRENCH_FRANCE - fr_FR, ITALIAN_ITALY - it_IT, RUSSIAN_RUSSIA - ru_RU, KOREAN_KOREA - ko_KR, DUTCH_NETHERLANDS - nl_NL, DANISH_DENMARK - da_DK, HEBREW_ISRAEL - he_IL, INDO_BAHASA_INDONESIA - id_ID, KANNADA_INDIA - kn_IN, MALAY_BAHASA_MALAYSIA - ms_MY, MALAYALAM_INDIA - ml_IN, TAGALOG_PHILLIPINES - tl_PH, ROMANIAN_ROMANIA - ro_RO, THAI_THAILAND - th_TH, CZECH_CZECH_REPUBLIC - cs_CZ, GREEK_GREECE - el_GR, FINNISH_FINLAND - fi_FI, FRENCH_CANADA - fr_CA, CROATIAN_CROATIA - hr_HR, HUNGARIAN_HUNGARY - hu_HU, NORWEGIAN_BOKMAL_NORWAY - nb_NO, FLEMISH_BELGIUM - nl_BE, POLISH_POLAND - pl_PL, ROMANIAN_MOLDOVA - ro_MD, SWEDISH_SWEDEN - sv_SE, UKRAINIAN_UKRAINE - uk_UA, VIETNAMESE_VIETNAM - vi_VN, TURKISH_TURKEY - tr_TR, ICELANDIC_ICELAND - is_IS, SLOVAK_SLOVAKIA - sk_SK ] | String |
| countryCode |  | Optional | Enum: 					 						[ Afghanistan - AF, Aland Islands - AX, Albania - AL, Algeria - DZ, American Samoa - AS, Andorra - AD, Angola - AO, Anguilla - AI, Antarctica - AQ, Antigua and Barbuda - AG, Argentina - AR, Armenia - AM, Aruba - AW, Ascension Island - AC, Australia - AU, Austria - AT, Azerbaijan - AZ, Bahamas - BS, Bahrain - BH, Bangladesh - BD, Barbados - BB, Belarus - BY, Belgium - BE, Belize - BZ, Benin - BJ, Bermuda - BM, Bhutan - BT, Bolivia - BO, Bonaire - BQ, Bosnia and Herzegovina - BA, Botswana - BW, Bouvet Island - BV, Brazil - BR, British Indian Ocean Territory - IO, British Virgin Islands - VG, Brunei - BN, Bulgaria - BG, Burkina Faso - BF, Burundi - BI, Cambodia - KH, Cameroon - CM, Canada - CA, Cape Verde - CV, Cayman Islands - KY, Central African Republic - CF, Chad - TD, Chile - CL, China - CN, Christmas Island - CX, Cocos Islands - CC, Colombia - CO, Comoros - KM, Cook Islands - CK, Costa Rica - CR, Croatia - HR, Cuba - CU, Curacao - CW, Cyprus - CY, Czech Republic - CZ, Democratic Republic of the Congo - CD, Denmark - DK, Diego Garcia - DG, Djibouti - DJ, Dominica - DM, Dominican Republic - DO, East Timor - TL, Ecuador - EC, Egypt - EG, El Salvador - SV, Equatorial Guinea - GQ, Eritrea - ER, Estonia - EE, Ethiopia - ET, Falkland Islands - FK, Faroe Islands - FO, Fiji - FJ, Finland - FI, France - FR, French Guiana - GF, French Polynesia - PF, French Southern Territories - TF, Gabon - GA, Gambia - GM, Georgia - GE, Germany - DE, Ghana - GH, Gibraltar - GI, Greece - GR, Greenland - GL, Grenada - GD, Guadeloupe - GP, Guam - GU, Guatemala - GT, Guernsey - GG, Guinea - GN, Guinea-Bissau - GW, Guyana - GY, Haiti - HT, Heard Island and McDonald Islands - HM, Honduras - HN, Hong Kong - HK, Hungary - HU, Iceland - IS, India - IN, Indonesia - ID, Iran - IR, Iraq - IQ, Ireland - IE, Isle of Man - IM, Israel - IL, Italy - IT, Ivory Coast - CI, Jamaica - JM, Japan - JP, Jersey - JE, Jordan - JO, Kazakhstan - KZ, Kenya - KE, Kiribati - KI, Kosovo - XK, Kuwait - KW, Kyrgyzstan - KG, Laos - LA, Latvia - LV, Lebanon - LB, Lesotho - LS, Liberia - LR, Libya - LY, Liechtenstein - LI, Lithuania - LT, Luxembourg - LU, Macao - MO, Macedonia - MK, Madagascar - MG, Malawi - MW, Malaysia - MY, Maldives - MV, Mali - ML, Malta - MT, Marshall Islands - MH, Martinique - MQ, Mauritania - MR, Mauritius - MU, Mayotte - YT, Mexico - MX, Micronesia - FM, Moldova - MD, Monaco - MC, Mongolia - MN, Montenegro - ME, Montserrat - MS, Morocco - MA, Mozambique - MZ, Myanmar - MM, Namibia - NA, Nauru - NR, Nepal - NP, Netherlands - NL, Netherlands Antilles - AN, New Caledonia - NC, New Zealand - NZ, Nicaragua - NI, Niger - NE, Nigeria - NG, Niue - NU, Norfolk Island - NF, North Korea - KP, Northern Mariana Islands - MP, Norway - NO, Oman - OM, Pakistan - PK, Palau - PW, Palestinian Territory - PS, Panama - PA, Papua New Guinea - PG, Paraguay - PY, Peru - PE, Philippines - PH, Pitcairn - PN, Poland - PL, Portugal - PT, Puerto Rico - PR, Qatar - QA, Republic of the Congo - CG, Reunion - RE, Romania - RO, Russia - RU, Rwanda - RW, Saint Barthelemy - BL, Saint Helena - SH, Saint Kitts and Nevis - KN, Saint Lucia - LC, Saint Martin - MF, Saint Pierre and Miquelon - PM, Saint Vincent and the Grenadines - VC, Samoa - WS, San Marino - SM, Sao Tome and Principe - ST, Saudi Arabia - SA, Senegal - SN, Serbia - RS, Serbia and Montenegro - CS, Seychelles - SC, Sierra Leone - SL, Singapore - SG, Sint Maarten - SX, Slovakia - SK, Slovenia - SI, Solomon Islands - SB, Somalia - SO, South Africa - ZA, South Georgia and the South Sandwich Islands - GS, South Korea - KR, South Sudan - SS, Spain - ES, Sri Lanka - LK, Sudan - SD, Suriname - SR, Svalbard and Jan Mayen - SJ, Swaziland - SZ, Sweden - SE, Switzerland - CH, Syria - SY, Taiwan - TW, Tajikistan - TJ, Tanzania - TZ, Thailand - TH, Togo - TG, Tokelau - TK, Tonga - TO, Trinidad and Tobago - TT, Tunisia - TN, Turkey - TR, Turkmenistan - TM, Turks and Caicos Islands - TC, Tuvalu - TV, U.S. Virgin Islands - VI, Uganda - UG, Ukraine - UA, United Arab Emirates - AE, United Kingdom - GB, United States - US, United States Minor Outlying Islands - UM, Uruguay - UY, Uzbekistan - UZ, Vanuatu - VU, Vatican - VA, Venezuela - VE, Vietnam - VN, Wallis and Futuna - WF, Western Sahara - EH, Yemen - YE, Zambia - ZM, Zimbabwe - ZW, global - global  ] | String |
| linkedAssets |  | Optional | List containing the linked assets associated with the article | List [String] |
| migrationDetails |  | Optional | Object containing the article migration details. Used when updating an existing article | Object |
|  | migratedFrom | Required | Refers to the source from where the article is migrated | String |
|  | migratedId | Required | Refers to the unique identifier for the migration that was configured when creating the article | String |
| folderMetadata |  | Required | Object containing the details about the folder the article is added to | Object |
|  | folderId | Required | Refers to the unique identifier for the folder where the article will be added.Refer to this  to see how you can fetch the folder Id | String |
|  | confidential | Optional | If true, the article is confidentialDefault Value: false | Boolean |
| tags |  | Optional | Refers to the list of tags you want to apply on the article | List [String] |
| externalPermalink |  | Optional | The external URL of the article. | URL |
| version |  | Optional | The version of the article. Example, 3 | Integer |
| canEdit |  | Optional | Indicates whether the article can be edited. Supported Values: true, false | Boolean |

### Example - Request




 Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/save' \
--header 'Authorization: Bearer {}' \
--header 'Key;' \
--header 'Content-Type: application/json' \
--data '{
  "content": {
    "contentType": "KNOWN_ISSUE",
    "contentSubType": "KB_ARTICLE",
    "title": "Title"
  },
  "publicContent": false,
  "hasConditionalSection": false,
  "externalContent": false,
  "originType": "EXTERNAL",
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
    "_c_62a1cf903df8d74b0e283e57": ["testMigratedId"]
  },
  "status": "APPROVED",
  "locale": "hi_IN",
  "countryCode": "IN",
  "linkedAssets": [],
  "migrationDetails": {
    "migratedFrom": "DELL",
    "migratedId": "locale/TNID"
  },
  "deleted": false,
  "folderMetadata": {
    "folderId": "6826d6f308e6e13731f25c58",
    "confidential": false
  },
  "tags": ["tag1", "tag2"]
}'



### Example - Response




{
    "data": {
        "id": "68270040f057782a59b72f30",
        "version": 1,
        "contributors": [
            66014658
        ],
        "tags": [
            "tag1",
            "tag2"
        ],
        "content": {
            "contentType": "KNOWN_ISSUE",
            "contentSubType": "KB_ARTICLE",
            "title": "Title"
        },
        "publicContent": false,
        "hasConditionalSection": false,
        "externalContent": false,
        "originType": "EXTERNAL",
        "favourite": false,
        "lngVariants": {},
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
            "livechatNotHelpfulCount": 0,
            "externalViewCount": 0,
            "externalHelpfulCount": 0,
            "externalNotHelpfulCount": 0
        },
        "partnerCustomProperties": {
            "_c_62a1cf903df8d74b0e283e57": [
                "testMigratedId"
            ]
        },
        "customProperties": {
            "flatCustomProperties": [
                "ALL"
            ],
            "customPropertyNames": [],
            "mappedCustomProperties": {},
            "mappedControllingCustomPropertyList": []
        },
        "status": "APPROVED",
        "saveInLngVariantEsEnabled": false,
        "locale": "hi_IN",
        "countryBaseContent": false,
        "migrationDetails": {
            "migratedFrom": "DELL",
            "migratedId": "locale/TNID"
        },
        "linkedAssets": [],
        "translationProcess": {
            "updateTime": 1747387234973,
            "newContentAvailableForTranslation": false,
            "authorId": 66014658
        },
        "grants": [
            "USER/66014658/OWNERSHIP",
            "CLIENT/66000002/OWNERSHIP"
        ],
        "clientId": 66000002,
        "ownerUserId": 66014658,
        "createdTime": "May 16, 2025, 09:07:11 AM",
        "modifiedTime": "May 16, 2025, 09:20:34 AM",
        "lastModifiedUserId": 66014658,
        "deleted": false,
        "folderMetadata": {
            "folderId": "6826d6f308e6e13731f25c58",
            "confidential": false
        },
        "canEdit": false
    },
    "errors": []
}



[](https://dev.sprinklr.com/save-knowledge-base-content)




[Back to top](https://dev.sprinklr.com/save-knowledge-base-content)
