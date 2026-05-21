---
title: "Webhook Replay"
slug: webhook-replay
url: https://dev.sprinklr.com/webhook-replay
---

# Webhook Replay

#
POST - Webhook Replay


Webhook replay API helps you in getting the stream of webhooks for a given time duration. To replay the webhook stream for a given time duration, you need to make the below given call. You can use the first `Webhook Replay` API call to get the webhook for a given time range and if there is more data you get a Cursor at the end of API response. Now you can use this Cursor in `Cursor - To Replay Further` API call to replay the stream of webhook. Here are the steps that you need to follow:


- [Webhook Replay](https://dev.sprinklr.com/webhook-replay/)

- [Cursor - To Replay Further](https://dev.sprinklr.com/webhook-replay/)

**Note: ** Please reach out to your Success Manager or Sprinklr Support to get Webhook Replay API's enabled for your environment.

## Webhook Replay

### API Endpoint

`POST`
https://api3.sprinklr.com/{env}/api/v2/webhook-replay

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

## Body Parameters

The following table describes the Body Parameters in use.





































			****``




| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| subscriptionId | Required | Webhook Subscription Id | String |
| startTime | Required | The time from which you want to replay webhook. | Epoch |
| endTime | Required | The time to which you want to replay webhook. | Epoch |
| size | Required | The number of webhooks you want to fetch in one request. | Integer |
| statuses | Optional | Specifies the webhook status values to filter in the response. Use this parameter to fetch only webhooks that match the selected status. Supported values: Active, Inactive | String |

### Example - Request

 Copy Code


curl --location 'https://api3.sprinklr.com/qa6/api/v2/webhook-replay' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {apikey}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "subscriptionId": "68e8b905b41c1503d0d6a4d7",
    "startTime": "1763052611460",
    "endTime": "1763054149143",
    "size": 10,
    "statuses": [
        "ACTIVE","INACTIVE"
    ]
}'





### Example - Response




{
    "data": {
        "results": [
            "{\"id\":\"60a4e34aeb8f1e2030704a8a\",\"type\":\"message.created\",\"payload\":{\"sourceType\":\"PERSISTENT_SEARCH\",\"sourceId\":-1,\"content\":{\"text\":\"Minted my first  NFT : The White Panther #CR7\\nA small Tribute to Thalaiva @Cristiano\\nThanks for organising this NFT Competition @dotmoovs \\n#dotmoovs \\nhttps://t.co/hRs4Ue9Fg8\",\"attachment\":{\"url\":\"https://app.airnfts.com/nft/The_White_Panther_CR_1621418544206\",\"title\":\"The White Panther CR7 - AirNFTs - NFT Marketplace on BSC\",\"description\":\"The guy in the picture doesn't require any introduction. He is a white panther of the Soccer world. Many Sports Fans talk about him, some carry his autographs, some selfies. Everyone has his own way of showing respect, love, and affection to this God. This is also the single NFT with his memorable e\",\"type\":\"LINK\"}},\"channelMessageId\":\"1394957142998781953\",\"channelType\":\"TWITTER\",\"channelCreatedTime\":1621418674598,\"senderProfile\":{\"name\":\"Kshitij 🇮🇳\",\"channelType\":\"TWITTER\",\"channelId\":\"1660608522\",\"permalink\":\"https://twitter.com/thanoskefufa\",\"avatarUrl\":\"https://twitter.com/thanoskefufa/profile_image?size=original\",\"bio\":\"Software Engg | Blockchain Fanatic | Crypto Trader | $BNB Hodler | CZ Fan |\\nhttps://www.binance.com/en/register?ref=YHR5Q79Z\\nhttp://bitmex.com/register/yp3wBn\",\"followers\":161,\"following\":408,\"username\":\"thanoskefufa\",\"verified\":false,\"unSubscribed\":false,\"deleted\":false,\"snCreatedTime\":0,\"snModifiedTime\":0},\"receiverProfile\":{\"name\":\"Cristiano Ronaldo\",\"channelType\":\"TWITTER\",\"channelId\":\"155659213\",\"permalink\":\"https://twitter.com/Cristiano\",\"avatarUrl\":\"https://pbs.twimg.com/profile_images/1157313327867092993/a09TxL_1.jpg\",\"bio\":\"This Privacy Policy addresses the collection and use of personal information - https://t.co/Jp6yh1T58c\",\"followers\":92207288,\"following\":56,\"username\":\"Cristiano\",\"verified\":true,\"unSubscribed\":false,\"deleted\":false,\"snCreatedTime\":0,\"snModifiedTime\":0},\"permalink\":\"https://twitter.com/thanoskefufa/status/1394957142998781953\",\"language\":\"en\",\"messageId\":\"PERSISTENT_SEARCH_-1_1621418674598_TWITTER_4_1394957142998781953\",\"brandPost\":false,\"createdTime\":1621418825965,\"modifiedTime\":1621418826029,\"textEntities\":{\"message\":[{\"indices\":[41,45],\"hashtag\":\"CR7\"},{\"indices\":[74,84],\"screenName\":\"Cristiano\"},{\"indices\":[128,137],\"screenName\":\"dotmoovs\"},{\"indices\":[139,148],\"hashtag\":\"dotmoovs\"},{\"indices\":[150,173],\"url\":\"https://t.co/hRs4Ue9Fg8\"}]},\"location\":{\"text\":\"India\",\"lat\":20.0,\"lon\":77.0,\"additional\":{\"country\":\"India\",\"code\":\"IN\",\"locText\":\"India\"}},\"insights\":{\"FOLLOWER_COUNT_AT_POST\":161.0,\"POST_REACH_COUNT\":161.0},\"workflow\":{\"modifiedTime\":1621418826127,\"customProperties\":{},\"queues\":[{\"queueId\":102944,\"assignmentTime\":1621418826127}],\"spaceWorkflows\":[]},\"enrichments\":{\"sentiment\":0},\"conversationId\":\"1394957142998781953\",\"autoImported\":false},\"eventTime\":1621418825965,\"subscriptionDetails\":{\"subscriptionId\":\"60a4e334db614859a3d2524f\"}}",
            "{\"id\":\"60a4e34a0e2bec6ac70a8b79\",\"type\":\"message.created\",\"payload\":{\"sourceType\":\"PERSISTENT_SEARCH\",\"sourceId\":-1,\"content\":{\"text\":\"نتنياهو: \\n- إذا اعتقدت #حماس أنها تنتصر فهذه هزيمة لنا كلنا وللغرب بأسره\\n- حماس أنشأت بنية تحتية كاملة تحت الأرض في قطاع #غزة\\n- لا نستبعد أي شيء ونأمل استعادة الهدوء بسرعة ونعمل على تجنب المدنيين\\n- نحن نواجه منظمة إرهابية إسلامية لديها قطعة أرض https://t.co/ukvwuKruMM\",\"attachment\":{\"url\":\"https://pbs.twimg.com/media/E1va4BaXMAAfRw9.jpg\",\"previewUrl\":\"https://pbs.twimg.com/media/E1va4BaXMAAfRw9.jpg\",\"type\":\"IMAGE\"}},\"channelMessageId\":\"1394957255217401856\",\"channelType\":\"TWITTER\",\"channelCreatedTime\":1621418701353,\"senderProfile\":{\"name\":\"دخان ياسين\",\"channelType\":\"TWITTER\",\"channelId\":\"930552926455652353\",\"permalink\":\"https://twitter.com/dakhanartagal\",\"avatarUrl\":\"http://pbs.twimg.com/profile_images/932437009607593984/lfbDs37g.jpg\",\"followers\":87,\"following\":159,\"username\":\"dakhanartagal\",\"verified\":false,\"unSubscribed\":false,\"deleted\":false,\"snCreatedTime\":0,\"snModifiedTime\":0},\"receiverProfile\":{\"name\":\"قناة الجزيرة\",\"channelType\":\"TWITTER\",\"channelId\":\"5536782\",\"permalink\":\"https://twitter.com/AJArabic\",\"avatarUrl\":\"https://pbs.twimg.com/profile_images/1057294709280788480/nKrtTjSc.jpg\",\"bio\":\"الجزيرة.. الرأي والرأي الآخر.. تابع أخبارنا العاجلة على @AJABreaking\",\"followers\":16404928,\"following\":28,\"username\":\"AJArabic\",\"verified\":true,\"unSubscribed\":false,\"deleted\":false,\"snCreatedTime\":0,\"snModifiedTime\":0},\"permalink\":\"https://twitter.com/dakhanartagal/status/1394957255217401856\",\"language\":\"ar\",\"messageId\":\"PERSISTENT_SEARCH_-1_1621418701353_TWITTER_8_1394957255217401856\",\"brandPost\":false,\"createdTime\":1621418826496,\"modifiedTime\":1621418826579,\"textEntities\":{\"message\":[{\"indices\":[23,28],\"hashtag\":\"حماس\"},{\"indices\":[121,125],\"hashtag\":\"غزة\"},{\"indices\":[245,268],\"url\":\"https://t.co/ukvwuKruMM\"}]},\"location\":{\"text\":\"Algeria\",\"lat\":28.0,\"lon\":3.0,\"additional\":{\"country\":\"Algeria\",\"code\":\"DZ\",\"locText\":\"Algeria\"}},\"insights\":{\"FOLLOWER_COUNT_AT_POST\":1070.0,\"POST_REACH_COUNT\":1070.0},\"workflow\":{\"modifiedTime\":1621418826679,\"customProperties\":{},\"queues\":[{\"queueId\":102944,\"assignmentTime\":1621418826679}],\"spaceWorkflows\":[]},\"enrichments\":{\"sentiment\":1},\"conversationId\":\"1394957255217401856\",\"autoImported\":false},\"eventTime\":1621418826496,\"subscriptionDetails\":{\"subscriptionId\":\"60a4e334db614859a3d2524f\"}}"
        ],
        "cursor": "60a50efebc622348f58a975f"
    },
    "errors": []
}





## Cursor - To Replay Further

We will use the Cursor from the above call response to fetch further data.

### API Endpoint

`GET`
https://api3.sprinklr.com/{env}/api/v2/webhook-replay?cursor={Cursor from above call}

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

## Query Parameters

The following table describes the Query Parameters in use.

















| Query Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| cursor | Required | Webhook Cursor from Webhook Replay API call. | String |

### Example - Request

 Copy Code



curl -X GET \
'https://api3.sprinklr.com/{{env}}/api/v2/webhook-replay?cursor=60a507a2bc622348f58a8023 \
-H 'Authorization: Bearer {token}' \
-H 'Content-Type: application/json' \
-H 'key: {apikey}'




### Example - Response




{
    "data": {
        "results": [
            "{\"id\":\"60a4e348de466710d503feff\",\"type\":\"message.created\",\"payload\":{\"sourceType\":\"LISTENING\",\"sourceId\":-1,\"content\":{\"text\":\"𝐃𝐞𝐥𝐡𝐢 \\n\\n𝐈𝐂𝐔 𝐁𝐞𝐝𝐬\\n\\nLocation: Jana Shree Hospital\\nContact: 9953882204\\nVerified at 12:57 pm on 19th May.\\n\\n#Delhi #ICU #Beds #ICUBeds #Covid19Helpers #Covid19IndiaHelpers\\n#beatthevirus @CaraForte_com\"},\"channelMessageId\":\"1394957533350178816\",\"channelType\":\"TWITTER\",\"channelCreatedTime\":1621418767665,\"senderProfile\":{\"name\":\"Vinay Choudhary\",\"channelType\":\"TWITTER\",\"channelId\":\"158117402\",\"permalink\":\"https://twitter.com/vinay_choudhary\",\"avatarUrl\":\"https://twitter.com/vinay_choudhary/profile_image?size=original\",\"bio\":\"Vinay Chaudhary is a serial entraprenuer, who has a knack of converting dreams to realities. Views are personal. https://www.linkedin.com/in/choudharyvinay\",\"followers\":314,\"following\":83,\"username\":\"vinay_choudhary\",\"verified\":false,\"unSubscribed\":false,\"deleted\":false,\"snCreatedTime\":0,\"snModifiedTime\":0},\"permalink\":\"https://twitter.com/vinay_choudhary/status/1394957533350178816\",\"language\":\"en\",\"messageId\":\"LISTENING_-1_1621418767665_TWITTER_4_1394957533350178816\",\"brandPost\":false,\"createdTime\":1621418819528,\"modifiedTime\":1621418819528,\"textEntities\":{\"message\":[{\"indices\":[69,79]},{\"indices\":[115,121],\"hashtag\":\"Delhi\"},{\"indices\":[122,126],\"hashtag\":\"ICU\"},{\"indices\":[127,132],\"hashtag\":\"Beds\"},{\"indices\":[133,141],\"hashtag\":\"ICUBeds\"},{\"indices\":[142,157],\"hashtag\":\"Covid19Helpers\"},{\"indices\":[158,178],\"hashtag\":\"Covid19IndiaHelpers\"},{\"indices\":[179,192],\"hashtag\":\"beatthevirus\"},{\"indices\":[193,207],\"screenName\":\"CaraForte_com\"}]},\"location\":{\"text\":\"Greater Noida, Uttar Pradesh, India\",\"lat\":28.49615,\"lon\":77.53601,\"additional\":{\"country\":\"India\",\"code\":\"IN\",\"city\":\"Greater Noida\",\"locText\":\"Greater Noida, Uttar Pradesh, India\",\"state\":\"Uttar Pradesh\"}},\"insights\":{\"FOLLOWER_COUNT_AT_POST\":317.0,\"POST_REACH_COUNT\":317.0},\"workflow\":{\"modifiedTime\":1621418824764,\"customProperties\":{\"_c_6084602a73c88a500f505ab3\":[\"ICU + Ventilators\",\"Hospital Beds\"],\"_c_6087adee90493e372720bee7\":[\"49\"],\"_c_6085684fa4d13958db6288c1\":[\"Less Than 24 Hours\"],\"_c_60844fc273c88a500f4dd79d\":[\"Pass\"],\"_c_608bf684b7cd1c7c44938b17\":[\"U_ICUBeds\"],\"_c_6086a233b915547f66a3e4bc\":[\"Delhi\"],\"_c_60857f4061f0ac1735f549d9\":[\"9953882204\"],\"_c_6084505273c88a500f4deb00\":[\"Done\"]},\"queues\":[{\"queueId\":102947,\"assignmentTime\":1621418824439},{\"queueId\":102986,\"assignmentTime\":1621418824439}],\"spaceWorkflows\":[]},\"enrichments\":{\"sentiment\":0,\"lstTopicIds\":[\"6084433c58837f538d7127ed\",\"5efeb467d7e1d718a801d221\",\"602e63532919257d8fb6b2e2\",\"5d5e89b28a479815db077610\",\"5dd7a2c23fa1d42ebd5068cf\",\"5ef4bbeb70906b5aebcaf21a\",\"5e78511c70b48d5e0554714f\",\"5f034eaebee2bc63eb4fa061\",\"5f03dee466c37f53d33b2b1f\",\"5fbe07891275e91776ce0f54\"],\"lstThemeIds\":[\"5f492ff0b9c6b360a39cc6f3\",\"6091380650a2a455262919cc\",\"5f456416fad1711378b52023\",\"5ef5bc02f4ea0c05c70157f9\",\"5b7e5e25e4b07c39d4e67512\",\"6084658173c88a500f5135b1\",\"5e9bfa78f573152e1fefdc70\",\"6084661e73c88a500f514d28\",\"5f456349fad1711378b4fcbd\",\"5f4562a2fad1711378b4ce14\",\"5f45640efad1711378b51d3b\",\"5f45630dfad1711378b4eb46\",\"5f07f5ac78df9b627b5a9851\",\"60897f4e81b8c80c6ac00953\",\"5ef4d5b7b9e8c12de69627ca\",\"5f4563e8fad1711378b51585\",\"60241231c6c2563309559742\",\"5f2cf07d26bc45059bb07265\",\"5ef57cefe473d948611bffae\",\"5bd06e6ee4b0fd91c8c18f8f\",\"5f456268fad1711378b4b822\",\"5f45625efad1711378b4b4ec\",\"5f45625ffad1711378b4b50d\",\"608ba29f38a147325b4d3989\",\"60844862cd87fd6b62bdf41d\",\"5ef9810dc5f41c2290788165\"]},\"conversationId\":\"1394957533350178816\",\"autoImported\":false},\"eventTime\":1621418819528,\"subscriptionDetails\":{\"subscriptionId\":\"60a4e334db614859a3d2524f\"}}",
            "{\"id\":\"60a4e348de466710d503fe4d\",\"type\":\"message.created\",\"payload\":{\"sourceType\":\"LISTENING\",\"sourceId\":-1,\"content\":{\"text\":\"🎉🎉ついに二ノ国：Cross Worlds\\n2021年6月10日配信開始決定🎉🎉\\n\\nこれを記念してフォロー＆RTキャンペーンを\\n実施！！参加者から抽選で6名様に、\\nAmazonギフト券10万円分を🎁！！\\n\\n▼参加方法\\n①＠NinoKuniCWをフォロー\\n②この投稿をRT（5/19 23:59まで）\\n③抽選で6名様に当選DMが届く！\\n\\n＃ニノクロ https://t.co/eeyZI4V8cI\",\"attachment\":{\"url\":\"https://video.twimg.com/ext_tw_video/1394570264885690372/pu/vid/720x720/dpu6yRmKDmzuibGN.mp4?tag=12\",\"previewUrl\":\"https://pbs.twimg.com/ext_tw_video_thumb/1394570264885690372/pu/img/_uvTTdxjT-U8YWc4.jpg\",\"type\":\"VIDEO\"}},\"channelMessageId\":\"1394957586521280516\",\"channelType\":\"TWITTER\",\"channelCreatedTime\":1621418780342,\"senderProfile\":{\"name\":\"nao\",\"channelType\":\"TWITTER\",\"channelId\":\"728586677019496448\",\"permalink\":\"https://twitter.com/nao10_9191\",\"avatarUrl\":\"https://twitter.com/nao10_9191/profile_image?size=original\",\"followers\":5,\"following\":43,\"username\":\"nao10_9191\",\"verified\":false,\"unSubscribed\":false,\"deleted\":false,\"snCreatedTime\":0,\"snModifiedTime\":0},\"permalink\":\"https://twitter.com/nao10_9191/status/1394957586521280516\",\"language\":\"ja\",\"messageId\":\"LISTENING_-1_1621418780342_TWITTER_8_1394957586521280516\",\"brandPost\":false,\"createdTime\":1621418819493,\"modifiedTime\":1621418819493,\"textEntities\":{\"message\":[{\"indices\":[115,126],\"screenName\":\"NinoKuniCW\"},{\"indices\":[173,178],\"hashtag\":\"ニノクロ\"},{\"indices\":[179,202],\"url\":\"https://t.co/eeyZI4V8cI\"}]},\"insights\":{\"FOLLOWER_COUNT_AT_POST\":5.0,\"POST_REACH_COUNT\":5.0},\"workflow\":{\"modifiedTime\":1621418824504,\"customProperties\":{},\"queues\":[],\"spaceWorkflows\":[]},\"enrichments\":{\"sentiment\":0,\"lstTopicIds\":[\"5efeb467d7e1d718a801d221\",\"5eb297d0c5f41c1bcb66ff67\",\"5d5e89b28a479815db077610\",\"5e00be185abe657dbe18fb4b\",\"60a3d15e6d3dc878891328f3\"],\"lstThemeIds\":[\"6091380650a2a455262919cc\",\"5f4563eafad1711378b515db\",\"5b7e5e25e4b07c39d4e67512\",\"60241231c6c2563309559742\",\"5f2cf07d26bc45059bb07265\",\"5e9bfa78f573152e1fefdc70\",\"5f456268fad1711378b4b822\",\"5f45625efad1711378b4b4ec\",\"5f456349fad1711378b4fcbd\",\"5f456264fad1711378b4b5d6\",\"5f4562a2fad1711378b4ce14\",\"5ef2de9b3690bd5b54365261\",\"5f45625ffad1711378b4b50d\",\"5f45640efad1711378b51d3b\",\"5f456271fad1711378b4bbb7\",\"5eea389fbc5ff23793e86795\",\"5fce3b34c64aa443ce9edf53\",\"5f45630dfad1711378b4eb46\"]},\"conversationId\":\"1394957586521280516\",\"autoImported\":false},\"eventTime\":1621418819493,\"subscriptionDetails\":{\"subscriptionId\":\"60a4e334db614859a3d2524f\"}}"
        ],
        "cursor": "60a51013bc622348f58a9a66"
    },
    "errors": []
}





[](https://dev.sprinklr.com/webhook-replay)




[Back to top](https://dev.sprinklr.com/webhook-replay)
