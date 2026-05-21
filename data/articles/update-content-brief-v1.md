---
title: "Update Content Brief v1"
slug: update-content-brief-v1
url: https://dev.sprinklr.com/update-content-brief-v1
---

# Update Content Brief v1

#
PUT - Update Content Brief


Using this API, you can update the content brief details using the unique content brief Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/content/brief/create/{Id}

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

### Path Parameters


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The content brief Id. | String |

### Request Parameters












































































































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| contentBriefId | Required | The id of the content brief you want to update. | String |
| name | Optional | The name of the Content Brief. | String |
| description | Optional | The description of the Content Brief. | String |
| assetClass | Required | The asset class, by default CAMPAIGN | String |
| assetId | Required | The campaign id. | String |
| templateId | Required | The templateId to attach with this brief. | String |
| themeId | Optional | The theme Id. | String |
| personaId | Optional | The persona Id. | String |
| customerJourneyId | Optional | The customerJourneyId. | String |
| data | Optional | The data of the content brief. | String |
| type | Optional | The type of message, by default CONTENT_BRIEF | String |
| shareConfigs | Optional | The content brief sharing configuration object. | Object |
| tags | Optional | The tags you want to attach with content brief. | String |
| smartBrief | Optional | It is a boolean field. If kept false, the brief is not a smart brief. | Boolean |
| clientCustomProperties | Optional | The object conataing client custom properties. | Object |
| partnerCustomProperties | Optional | The object conataing partner custom properties. | Object |

### Example - Request

 Copy Code



curl -X PUT

'https://api3.sprinklr.com/{env}/api/v1/content/brief/6214a640c72c085362b89b87'

-H 'Authorization: Bearer {Enter your Access Token}'

-H 'Key: {Enter your API KEY}'

-H 'accept: application/json'

-H 'Content-Type: application/json'

-d '
{
"contentBriefId":"6214a640c72c085362b89b87",
"assetClass": "CAMPAIGN",
"type": "CONTENT_BRIEF",
"assetId": "4706_11131",
"brandId": "6131328746ef964fd8dc7835",
"clientCustomProperties": {
"4706": {
"59ef01e5e4b0e088754c9898": [
"1234"
]
}
},
"customerJourneyId": "599c327ee4b0c11035956966",
"data": "{"object":"value","document":{"object":"document","data":{},"nodes":[{"object":"block","type":"heading-one","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"This is smart editor test check","marks":[{"object":"mark","type":"fontfamily","data":{"value":"Times"}},{"object":"mark","type":"fontsize","data":{"value":48}}]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"This is smart editor test","marks":[{"object":"mark","type":"fontfamily","data":{"value":"Times New Roman"}}]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"this is ","marks":[]}]},{"object":"inline","type":"link","data":{"href":"https://google.com/"},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"content","marks":[]}]}]},{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]},{"object":"block","type":"GRID_NODE_TYPE","data":{"style":{"height":58.013885498046875}},"nodes":[{"object":"block","type":"SECTION_NODE_TYPE","data":{"gridSize":1,"background":{"value":"rgba(245, 245, 245, 1)","type":"color"}},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]}]}]},{"object":"block","type":"GRID_NODE_TYPE","data":{"style":{"height":200}},"nodes":[{"object":"block","type":"SECTION_NODE_TYPE","data":{"gridSize":1,"background":{"value":"rgba(229, 229, 229, 1)","type":"color"}},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]},{"object":"block","type":"GRID_NODE_TYPE","data":{"style":{"height":200}},"nodes":[{"object":"block","type":"SECTION_NODE_TYPE","data":{"gridSize":1,"background":{"value":"rgba(232, 232, 250, 1)","type":"color"}},"nodes":[{"object":"block","type":"heading-two","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"The problem in H2","marks":[]}]}]}]},{"object":"block","type":"SECTION_NODE_TYPE","data":{"gridSize":1,"background":{"value":"rgba(238, 251, 206, 1)","type":"color"}},"nodes":[{"object":"block","type":"heading-two","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"The solution in H2","marks":[]}]}]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"uncaught Error: Unable to find a DOM node for \"1381\". This is often because of forgetting to add `props.attributes` to a custom component. at Pe (vendors~briefBuilder~calendar~","marks":[{"object":"mark","type":"fontsize","data":{"value":16}},{"object":"mark","type":"fontfamily","data":{"value":"Times New Roman"}}]},{"object":"leaf","text":"campaigns","marks":[{"object":"mark","type":"fontsize","data":{"value":16}},{"object":"mark","type":"fontfamily","data":{"value":"Courier"}}]},{"object":"leaf","text":"~contentBrief~contentBuilder~exports~personas~publisher~setti~64a34ff5.pace.en_US.js:1) at t.default (briefBuilder~calendar~campaigns~contentBrief~contentBuilder~exports~personas~publisher~settings.space.en_US.js:1)    at briefBuilder~calendar~campaigns~contentBrief~contentBuilder~exports~personas~publisher~settings.space.en_US.js:1","marks":[{"object":"mark","type":"fontsize","data":{"value":16}},{"object":"mark","type":"fontfamily","data":{"value":"Times New Roman"}}]}]}]},{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"","marks":[{"object":"mark","type":"fontsize","data":{"value":16}},{"object":"mark","type":"fontfamily","data":{"value":"Times New Roman"}}]}]}]}]}}",
"description": "NEW CB Description",
"name": "New CB",
"partnerCustomProperties": {
"_c_61c2bbec04202c0b6f68c6f2": [
"xmas"
]
},
"personaId": "605f5ba84069824ebfd9fbd6",
"shareConfigs": [
{
"shareLevel": "CLIENT",
"sharedWithIds": [
"4706"
]
},
{
"shareLevel": "CLIENT_GROUP",
"sharedWithIds": []
},
{
"shareLevel": "USER",
"sharedWithIds": []
},
{
"shareLevel": "USER_GROUP",
"sharedWithIds": []
}
],
"templateId": "5d1ae770e4b05abb104eadb8"
}




### Example - Response




{
    "id": "6214a640c72c085362b89b87",
    "name": "New CB",
    "description": "NEW CB Description",
    "assetClass": "CAMPAIGN",
    "assetId": "4706_11131",
    "templateId": "5d1ae770e4b05abb104eadb8",
    "brandId": "6131328746ef964fd8dc7835",
    "personaId": "605f5ba84069824ebfd9fbd6",
    "customerJourneyId": "599c327ee4b0c11035956966",
    "data":"{\"object\":\"value\",\"document\":{\"object\":\"document\",\"data\":{},\"nodes\":[{\"object\":\"block\",\"type\":\"heading-one\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"This is smart editor test check\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Times\"}},{\"object\":\"mark\",\"type\":\"fontsize\",\"data\":{\"value\":48}}]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"This is smart editor test\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Times New Roman\"}}]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"this is \",\"marks\":[]}]},{\"object\":\"inline\",\"type\":\"link\",\"data\":{\"href\":\"https://google.com/\"},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"content\",\"marks\":[]}]}]},{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]},{\"object\":\"block\",\"type\":\"GRID_NODE_TYPE\",\"data\":{\"style\":{\"height\":58.013885498046875}},\"nodes\":[{\"object\":\"block\",\"type\":\"SECTION_NODE_TYPE\",\"data\":{\"gridSize\":1,\"background\":{\"value\":\"rgba(245, 245, 245, 1)\",\"type\":\"color\"}},\"nodes\":[{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]}]}]},{\"object\":\"block\",\"type\":\"GRID_NODE_TYPE\",\"data\":{\"style\":{\"height\":200}},\"nodes\":[{\"object\":\"block\",\"type\":\"SECTION_NODE_TYPE\",\"data\":{\"gridSize\":1,\"background\":{\"value\":\"rgba(229, 229, 229, 1)\",\"type\":\"color\"}},\"nodes\":[{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]},{\"object\":\"block\",\"type\":\"GRID_NODE_TYPE\",\"data\":{\"style\":{\"height\":200}},\"nodes\":[{\"object\":\"block\",\"type\":\"SECTION_NODE_TYPE\",\"data\":{\"gridSize\":1,\"background\":{\"value\":\"rgba(232, 232, 250, 1)\",\"type\":\"color\"}},\"nodes\":[{\"object\":\"block\",\"type\":\"heading-two\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"The problem in H2\",\"marks\":[]}]}]}]},{\"object\":\"block\",\"type\":\"SECTION_NODE_TYPE\",\"data\":{\"gridSize\":1,\"background\":{\"value\":\"rgba(238, 251, 206, 1)\",\"type\":\"color\"}},\"nodes\":[{\"object\":\"block\",\"type\":\"heading-two\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"The solution in H2\",\"marks\":[]}]}]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"uncaught Error: Unable to find a DOM node for \\\"1381\\\". This is often because of forgetting to add `props.attributes` to a custom component. at Pe (vendors~briefBuilder~calendar~\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontsize\",\"data\":{\"value\":16}},{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Times New Roman\"}}]},{\"object\":\"leaf\",\"text\":\"campaigns\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontsize\",\"data\":{\"value\":16}},{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Courier\"}}]},{\"object\":\"leaf\",\"text\":\"~contentBrief~contentBuilder~exports~personas~publisher~setti~64a34ff5.pace.en_US.js:1) at t.default (briefBuilder~calendar~campaigns~contentBrief~contentBuilder~exports~personas~publisher~settings.space.en_US.js:1)    at briefBuilder~calendar~campaigns~contentBrief~contentBuilder~exports~personas~publisher~settings.space.en_US.js:1\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontsize\",\"data\":{\"value\":16}},{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Times New Roman\"}}]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontsize\",\"data\":{\"value\":16}},{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Times New Roman\"}}]}]}]}]}}",
    "clientCustomProperties": {
        "4706": {
            "59ef01e5e4b0e088754c9898": [
                "1234"
            ]
        }
    },
    "partnerCustomProperties": {
        "_c_61c2bbec04202c0b6f68c6f2": [
            "xmas"
        ],
        "_c_61c336e07aa45221a63a0c6f": [
            "Dec 25th"
        ],
        "_c_61c337277aa45221a63a14f6": [
            "Dec 25th"
        ],
        "_c_61c3377c7aa45221a63a1e58": [
            "Dec 25th"
        ],
        "_c_61c337bf7aa45221a63a276d": [
            "25"
        ],
        "_c_61c337ee7d20aa6f24553919": [
            "1640370600000"
        ],
        "_c_61c3381d7d20aa6f24553f40": [
            "
Dec 25th
"
        ],
        "_c_61c3384a7d20aa6f24554307": [
            "Dec 25th"
        ]
    },
    "type": "CONTENT_BRIEF",
    "clientId": 4706,
    "ownerUserId": 429501,
    "createdTime": 1645520448911,
    "modifiedTime": 1645520448911,
    "dueDate": 1647334848911,
    "shareConfigs": [
        {
            "shareLevel": "CLIENT",
            "sharedWithIds": [
                "4706"
            ]
        },
        {
            "shareLevel": "CLIENT_GROUP",
            "sharedWithIds": []
        },
        {
            "shareLevel": "USER",
            "sharedWithIds": []
        },
        {
            "shareLevel": "USER_GROUP",
            "sharedWithIds": []
        }
    ],
    "grants": [
        "USER/429501/OWNERSHIP",
        "CLIENT/4706/OWNERSHIP"
    ],
    "version": 0,
    "locked": false,
    "canEdit": false,
    "canCollaborate": false
}





**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

 [](https://dev.sprinklr.com/update-content-brief-v1)




[Back to top](https://dev.sprinklr.com/update-content-brief-v1)
