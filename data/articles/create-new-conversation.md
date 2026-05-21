---
title: "Create New Conversation"
slug: create-new-conversation
url: https://dev.sprinklr.com/create-new-conversation
---

# Create New Conversation

# Create New Conversation

This API allows creating a new conversation once the user has been authenticated.

**Dev Notes: **

- The welcome messages that you configure in the live chat application will reflect in the create conversation API response

- The default messages in the conversation can be either be text or template assets

- The following assets can be sent in a live chat conversation: `Rich text`, `Feedback Asset`, `Survey Asset`, `Contact Details Form Asset`, `Card Asset`, `Product Show Case Card`, `Carousel Asset`, `Product Card`, `Rich Text Carousel`, `Info Card`

- Card and carousel templates can have buttons. The supported button action types include: Text, Url

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/new

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters












[article](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| startedByContext | Optional | Refers to the object containing the key and value pair for case custom field name and corresponding value | Object |
| pageTitle | Optional | Refers to the live chat application page title | String |
| pageUrl | Optional | Refers to the landing page url where the live chat application exists | String |
| userAgent | Optional | Refers to the device and browser that the customer is using.Refer to this  for more information | String |
| timeZone | Optional | Refers to the time zone in which the live chat conversation is happening | String |
| locale | Optional | Refers to the language code for live chat conversation | String |

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation/new \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "startedByContext": {
        "_c_6512d347d8b5f43fd91f7fb4" : ["Example case custom field value"]
    },
    "pageTitle": "Sprinklr Live Chat",
    "pageUrl": "https://live-chat-static.sprinklr.com/test-html/index.html?appId=65015cddb2678b575c01b175_app_1000163501&env=prod0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "timeZone": "Asia/Calcutta",
    "locale": "en"
}'



### Example - Response



{
    "id": "652feba889398c15c9d245bf",
    "appId": "app_1000163501",
    "conversationType": "SUPPORT",
    "participants": [
        "A_65113c865395ae2da5646b4b"
    ],
    "defaultMessages": [
        {
            "id": "652feba889398c15c9d245c0",
            "creationTime": 1697639336167,
            "sender": "P_0",
            "conversationId": "652feba889398c15c9d245bf",
            "messagePayload": {
                "messageType": "MESSAGE",
                "disableManualResponse": false,
                "textEntities": [],
                "attachment": {
                    "type": "CONTACT_DETAILS_FORM",
                    "otherConfigs": {
                        "postSubmitHideImage": false
                    },
                    "templateType": true,
                    "disableManualResponse": true,
                    "hideAttachment": false,
                    "expired": false,
                    "submitted": false,
                    "reSubmittable": false,
                    "showSubmittedContent": true,
                    "showContentPostSubmit": false,
                    "reCaptchaValidated": false,
                    "title": "Registration Details",
                    "form": {
                        "formId": "a3ef5ea1-62a9-4a69-b007-7042714f2e24",
                        "fields": [
                            {
                                "id": "NAME",
                                "fieldName": "NAME",
                                "name": "S1. Full Name",
                                "type": "TEXT",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "FIRST_NAME",
                                "fieldName": "FIRST_NAME",
                                "name": "S2 First Name",
                                "type": "TEXT",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "LAST_NAME",
                                "fieldName": "LAST_NAME",
                                "name": "S3 Last Name",
                                "type": "TEXT",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "EMAIL",
                                "fieldName": "EMAIL",
                                "name": "S4 Email Address",
                                "type": "EMAIL",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "PHONE_NO",
                                "fieldName": "PHONE_NO",
                                "name": "S5 Phone Number",
                                "type": "PHONE",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "d6c3259c-9e99-4e33-aa3e-2eefeabd518f",
                                "fieldName": "d6c3259c-9e99-4e33-aa3e-2eefeabd518f",
                                "name": "G1 Check box",
                                "type": "CHECKBOX",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "1f8ff9f8-5d95-4a4c-b555-776b8471f4f7",
                                "fieldName": "1f8ff9f8-5d95-4a4c-b555-776b8471f4f7",
                                "name": "G2. Check Box Group",
                                "type": "CHECKBOX_GROUP",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": [
                                    {
                                        "label": "check group question 1",
                                        "value": "question 1",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "समूह प्रश्न 1 की जाँच करें"
                                            }
                                        }
                                    },
                                    {
                                        "label": "check group question 2",
                                        "value": "question 2",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "समूह प्रश्न 2 की जाँच करें"
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "0c56c6fe-ee84-4887-9300-c0ffc8d6de89",
                                "fieldName": "0c56c6fe-ee84-4887-9300-c0ffc8d6de89",
                                "name": "G3. Email",
                                "type": "EMAIL",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "dcec37ec-17af-442a-8246-969124d26044",
                                "fieldName": "dcec37ec-17af-442a-8246-969124d26044",
                                "name": "G4. Pick List",
                                "type": "PICKLIST",
                                "mandatory": false,
                                "constraints": [],
                                "defaultValue": "option 2",
                                "picklistValues": [
                                    {
                                        "label": "Pick List Option 1",
                                        "value": "option 1",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "सूची विकल्प 1 चुनें"
                                            }
                                        }
                                    },
                                    {
                                        "label": "Pick List Option 2",
                                        "value": "option 2",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "सूची विकल्प 2 चुनें"
                                            }
                                        }
                                    },
                                    {
                                        "label": "Pick List Option 3",
                                        "value": "option 3",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "सूची विकल्प 3 चुनें"
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "41f00be6-85b8-47e3-9d07-5dae41360a4b",
                                "fieldName": "41f00be6-85b8-47e3-9d07-5dae41360a4b",
                                "name": "G5. Text",
                                "type": "TEXT",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "636a7e7f-28b6-4f36-8f7c-eff6a0856d68",
                                "fieldName": "636a7e7f-28b6-4f36-8f7c-eff6a0856d68",
                                "name": "G6. Number",
                                "type": "NUMBER",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "a4df2c84-8c86-43db-bfa1-ab1215b6f05d",
                                "fieldName": "a4df2c84-8c86-43db-bfa1-ab1215b6f05d",
                                "name": "G7. Date",
                                "type": "DATE",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": [],
                                "format": "DD/MM/YYYY"
                            },
                            {
                                "id": "eb552d2f-ca6a-4bf3-a40e-8d0f82d5929c",
                                "fieldName": "eb552d2f-ca6a-4bf3-a40e-8d0f82d5929c",
                                "name": "G8. Multi pick list",
                                "type": "MULTI_PICKLIST",
                                "mandatory": false,
                                "constraints": [],
                                "defaultValue": [
                                    "m1",
                                    "m2"
                                ],
                                "picklistValues": [
                                    {
                                        "label": "MultiPickList Option 1",
                                        "value": "m1",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "मल्टीपिकलिस्ट विकल्प 1"
                                            }
                                        }
                                    },
                                    {
                                        "label": "MultiPickList Option 2",
                                        "value": "m2",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "मल्टीपिकलिस्ट विकल्प 2"
                                            }
                                        }
                                    },
                                    {
                                        "label": "MutliPickList Option 3",
                                        "value": "m3",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "MutliPickList विकल्प 3"
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "3fbd2b27-1bee-4e78-ae94-81bea5de67cf",
                                "fieldName": "3fbd2b27-1bee-4e78-ae94-81bea5de67cf",
                                "name": "G9. Pick List Open",
                                "type": "PICKLIST_OPEN",
                                "mandatory": false,
                                "constraints": [],
                                "defaultValue": "po 2",
                                "picklistValues": [
                                    {
                                        "label": "po 1",
                                        "value": "po 1",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "1 के बाद"
                                            }
                                        }
                                    },
                                    {
                                        "label": "po 2",
                                        "value": "po 2",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "विगत 2"
                                            }
                                        }
                                    },
                                    {
                                        "label": "po 3",
                                        "value": "po 3",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "3 के बाद"
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "fe0bb2f4-7038-41e5-a509-991b2733dee7",
                                "fieldName": "fe0bb2f4-7038-41e5-a509-991b2733dee7",
                                "name": "G10. Multi Pick List Open",
                                "type": "MULTI_PICKLIST_OPEN",
                                "mandatory": false,
                                "constraints": [],
                                "defaultValue": [
                                    "mpo 2",
                                    "mpo 3"
                                ],
                                "picklistValues": [
                                    {
                                        "label": "mpo 1",
                                        "value": "mpo 1",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "के लिए"
                                            }
                                        }
                                    },
                                    {
                                        "label": "mpo 2",
                                        "value": "mpo 2",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "के लिए"
                                            }
                                        }
                                    },
                                    {
                                        "label": "mpo 3",
                                        "value": "mpo 3",
                                        "langVsTranslatedFieldValues": {
                                            "hi": {
                                                "label": "के लिए"
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "cb76aee8-2e6d-4d8b-9771-62655105a2b2",
                                "fieldName": "cb76aee8-2e6d-4d8b-9771-62655105a2b2",
                                "name": "G11. Password",
                                "type": "PASSWORD",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "a89336d9-c1cc-4329-9af0-ade3a4ec11ce",
                                "fieldName": "a89336d9-c1cc-4329-9af0-ade3a4ec11ce",
                                "name": "G12. Text Area",
                                "type": "TEXT_AREA",
                                "mandatory": false,
                                "constraints": [],
                                "picklistValues": []
                            },
                            {
                                "id": "5789d5b4-e86a-4c34-a8f6-507ff071cd0b",
                                "fieldName": "5789d5b4-e86a-4c34-a8f6-507ff071cd0b",
                                "name": "C1. Equality",
                                "type": "TEXT",
                                "mandatory": false,
                                "constraints": [
                                    {
                                        "type": "EQUALITY",
                                        "constraintValues": {},
                                        "fieldName": "41f00be6-85b8-47e3-9d07-5dae41360a4b"
                                    }
                                ],
                                "picklistValues": []
                            },
                            {
                                "id": "bda6f75f-764b-4d8f-a43c-9ee8f245b882",
                                "fieldName": "bda6f75f-764b-4d8f-a43c-9ee8f245b882",
                                "name": "C2. Regex",
                                "type": "TEXT",
                                "mandatory": false,
                                "constraints": [
                                    {
                                        "type": "REGEX",
                                        "constraintValues": {},
                                        "regex": "[a-z]+[0-9]*"
                                    }
                                ],
                                "picklistValues": []
                            }
                        ]
                    },
                    "submit": {
                        "id": "fd30b28e-618d-4f3c-9177-8819b3f3a837",
                        "type": "POST_BACK",
                        "title": "Submit",
                        "makeExternalCall": false,
                        "postBackHandlerType": "CONTACT_DETAILS_POST_BACK"
                    },
                    "reCaptchaEnabled": false
                }
            }
        },
        {
            "id": "652feba889398c15c9d245c1",
            "creationTime": 1697639336168,
            "sender": "P_0",
            "conversationId": "652feba889398c15c9d245bf",
            "messagePayload": {
                "messageType": "MESSAGE",
                "disableManualResponse": true,
                "text": "Heading 2\nparagraph",
                "richText": true,
                "textEntities": []
            }
        },
        {
            "id": "652feba889398c15c9d245c2",
            "creationTime": 1697639336169,
            "sender": "P_0",
            "conversationId": "652feba889398c15c9d245bf",
            "messagePayload": {
                "messageType": "MESSAGE",
                "disableManualResponse": false,
                "textEntities": [],
                "attachment": {
                    "type": "CAROUSEL",
                    "templateType": true,
                    "disableManualResponse": true,
                    "hideAttachment": false,
                    "expired": false,
                    "submitted": false,
                    "reSubmittable": true,
                    "showSubmittedContent": false,
                    "showContentPostSubmit": false,
                    "reCaptchaValidated": false,
                    "cardAttachmentList": [
                        {
                            "type": "CARD",
                            "templateType": true,
                            "expired": false,
                            "submitted": false,
                            "reSubmittable": true,
                            "showSubmittedContent": false,
                            "showContentPostSubmit": false,
                            "reCaptchaValidated": false,
                            "title": "Clock",
                            "description": "Description of clock",
                            "previewImageUrl": "https://sprcdn-prod0-sam.sprinklr.com/9178/fbb6d516-bffb-4643-9fb0-5a948c71eca2-1194044180/https___fastly.picsum.photos_i_p.jpg",
                            "buttons": [
                                {
                                    "id": "6d0c4376-7245-4834-a981-4d9ec84b86ff",
                                    "type": "POST_BACK",
                                    "title": "Clock Button",
                                    "makeExternalCall": false,
                                    "postBackHandlerType": "TEXT_POST_BACK"
                                }
                            ],
                            "reCaptchaEnabled": false
                        },
                        {
                            "type": "CARD",
                            "templateType": true,
                            "expired": false,
                            "submitted": false,
                            "reSubmittable": true,
                            "showSubmittedContent": false,
                            "showContentPostSubmit": false,
                            "reCaptchaValidated": false,
                            "title": "Building",
                            "description": "Description of building",
                            "previewImageUrl": "https://sprcdn-prod0-sam.sprinklr.com/9178/3399fe23-db04-4748-98e8-8d6248b4cef0-275663491/https___fastly.picsum.photos_i_p.jpg",
                            "buttons": [
                                {
                                    "id": "6a3ec9b3-5117-4a36-a4be-67e6f7ad2698",
                                    "type": "POST_BACK",
                                    "title": "Building button",
                                    "makeExternalCall": false,
                                    "postBackHandlerType": "TEXT_POST_BACK"
                                }
                            ],
                            "reCaptchaEnabled": false
                        }
                    ],
                    "buttons": [],
                    "reCaptchaEnabled": false
                }
            }
        },
        {
            "id": "652feba889398c15c9d245c3",
            "creationTime": 1697639336170,
            "sender": "P_0",
            "conversationId": "652feba889398c15c9d245bf",
            "messagePayload": {
                "messageType": "MESSAGE",
                "disableManualResponse": false,
                "textEntities": [],
                "attachment": {
                    "type": "CARD",
                    "templateType": true,
                    "disableManualResponse": true,
                    "hideAttachment": false,
                    "expired": false,
                    "submitted": false,
                    "reSubmittable": true,
                    "showSubmittedContent": false,
                    "showContentPostSubmit": false,
                    "reCaptchaValidated": false,
                    "buttons": [
                        {
                            "id": "b015c31a-1b8f-4a91-ba30-93330b87d912",
                            "type": "POST_BACK",
                            "title": "Text Button",
                            "makeExternalCall": false,
                            "postBackHandlerType": "TEXT_POST_BACK"
                        },
                        {
                            "id": "5720de75-da40-4cc8-9801-421ee1295745",
                            "type": "OPEN_URL",
                            "title": "Url button",
                            "makeExternalCall": false,
                            "url": "google.com",
                            "target": "_self"
                        }
                    ],
                    "reCaptchaEnabled": false
                }
            }
        },
        {
            "id": "652feba889398c15c9d245c4",
            "creationTime": 1697639336171,
            "sender": "P_0",
            "conversationId": "652feba889398c15c9d245bf",
            "messagePayload": {
                "messageType": "MESSAGE",
                "disableManualResponse": false,
                "textEntities": [],
                "attachment": {
                    "type": "FEEDBACK_FORM",
                    "templateType": true,
                    "disableManualResponse": true,
                    "hideAttachment": false,
                    "expired": false,
                    "submitted": false,
                    "reSubmittable": false,
                    "postSubmitTitle": "Thanks! Your feedback helps improve our service.",
                    "showSubmittedContent": false,
                    "showContentPostSubmit": false,
                    "reCaptchaValidated": false,
                    "questionTitle": "How satisfied were you with your support?",
                    "feedbackRating": 0,
                    "feedbackLabels": [
                        {
                            "label": "Dissatisfied"
                        },
                        {
                            "label": "Satisfied"
                        }
                    ],
                    "feedbackType": "nps",
                    "submit": {
                        "id": "SUBMIT",
                        "type": "POST_BACK",
                        "title": "Submit",
                        "makeExternalCall": false,
                        "postBackHandlerType": "FEEDBACK_POST_BACK"
                    },
                    "ruleId": "60f1350c4ac6d5652c3cd7a2",
                    "reverseOrder": false,
                    "reCaptchaEnabled": false
                }
            }
        },
        {
            "id": "652feba889398c15c9d245c5",
            "creationTime": 1697639336172,
            "sender": "P_0",
            "conversationId": "652feba889398c15c9d245bf",
            "messagePayload": {
                "messageType": "MESSAGE",
                "disableManualResponse": false,
                "text": "Hello",
                "textEntities": []
            }
        }
    ],
    "creationTime": 1697639336167,
    "startedByContext": {
        "_c_6512d347d8b5f43fd91f7fb4": [
            "Example case custom field value"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπinitiator": [
            "User"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπbrowser": [
            "Chrome 11"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπdevice": [
            "Computer"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπpageTitle": [
            "Sprinklr Live Chat"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπpageUrl": [
            "https://live-chat-static.sprinklr.com/test-html/index.html?appId=65015cddb2678b575c01b175_app_1000163501&env=prod0"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπipAddress": [
            "54.86.50.139"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπtimeZone": [
            "Asia/Calcutta"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπconversationClosed": [
            "No"
        ],
        "CHANNELπSPRINKLR_LIVE_CHATπuserAgent": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        ]
    },
    "participantsByStatus": {}
}






		 [](https://dev.sprinklr.com/create-new-conversation)

[Back to top](https://dev.sprinklr.com/create-new-conversation)
