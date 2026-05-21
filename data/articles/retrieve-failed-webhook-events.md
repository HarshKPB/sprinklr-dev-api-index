---
title: "Retrieve Failed Webhook Events"
slug: retrieve-failed-webhook-events
url: https://dev.sprinklr.com/retrieve-failed-webhook-events
---

# Retrieve Failed Webhook Events

#
POST - Retrieve Failed Webhook Events


The API call will help you retrieve failed webhooks for a subscription in a given time.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/webhook-replay

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

**Dev Notes: **Failed Webhooks are available for retrieval for 7 days

## Request Parameters
































| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| subscriptionId | Required | Id of the webhook subscription | String> |
| startTime (in milliseconds) | Required | The starting time from when you want to analyze webhook statuses | Integer |
| endTime (in milliseconds) | Required | The end time up till when you want to analyze webhook statuses | Integer |
| size | Optional | The expected size of the response | Integer |
| statuses | Required | The state of the webhook case. For example:  FAILED or DELIVERED | String |

### Example - Request

 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/webhook-replay' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'Content-Type: application/json' \
-d '
{
"subscriptionId":"6230a3b4215cc62878dbfe58",
"startTime":"1644992475000",
"endTime":"1649238046000",
"size":1,
"statuses": ["FAILED"]

}'




### Example - Response




	{
   "results": [
           "{\"id\":\"624427519d643560ccbc0a15\",\"type\":\"draft.created\",\"payload\":{\"id\":2090356330,\"accountIds\":[1000074852],\"accountGroupIds\":[],\"version\":0,\"contentTemplateIds\":[\"6155704d6debf231f0a72ad8\"],\"accountTypes\":[\"PHONE\"],\"variantDetails\":{\"variant\":false,\"variantParentMessageId\":\"MESSAGE_2090356330\",\"hasVariants\":false},\"content\":{\"attachment\":{\"url\":\"https://sprcdn-prod0-sam.sprinklr.com/9004/86fad510-7858-49f7-9e13-b88eab80d09f-183422575.jpg\",\"title\":\"06.30.14 - Point of View-Firew.jpg\",\"previewUrl\":\"https://sprcdn-prod0-sam.sprinklr.com/9004/c0bf3d4b-9328-40c3-87ff-419a7cf86549-1075408478/06.30.14_-_Point_of_View-Firew_p.jpg\",\"type\":\"IMAGE\"}},\"channelOptions\":[],\"scheduleDate\":1648633681319,\"taxonomy\":{\"name\":\"Message name 20220330151657711\",\"campaignId\":\"1000004509_1821\",\"clientCustomProperties\":{\"57039704abd0343421000005\":[\"hello\"],\"58076529e4b027d61cf75600\":[\"Hello\"]},\"partnerCustomProperties\":{\"_c_61c2b16cd1e4704b9b693e53\":[\"Dec 25th XMAS\"],\"_c_6198ae81e0007e552d8ad0a4\":[\"check\\nnew\\nline\"],\"_c_61968fed92d9691cfc2c775e\":[\"946665000000\"],\"5f2e94e28dd919311a96cce3\":[\"1596825000000\"],\"586626a4e4b0c0e65c1233ef\":[\"0\"],\"_c_61c0ac0f35c836231e0aee51\":[\"val1\"],\"5a056a34e4b05d59a02b1ded\":[\"1000069599\"],\"_c_61c2b416d1e4704b9b699e6b\":[\"1000004510\"],\"_c_61c2b12fd1e4704b9b6928d0\":[\"Dec 25th XMAS\"],\"5eddd70b06a9f4445a1a9377\":[\"N/A\"],\"_c_61968f9292d9691cfc2c663a\":[\"FRIENDS\"],\"_c_61968fd592d9691cfc2c71dd\":[\"777\"],\"_c_612744250b2fce56e77a4ddd\":[\"Request\"],\"_c_6196900b92d9691cfc2c7d09\":[\"
Joey Doesn't Share Food
\"],\"_c_61c2b2bbd1e4704b9b697beb\":[\"Dec 25th XMAS\"],\"_c_60beeecf7ab71f4a61da0802\":[\"
Defaults
\"],\"_c_61c2b233d1e4704b9b696a9b\":[\"25\"],\"5f046165535c7922654fa187\":[\"No\"],\"_c_5f744157b0b802338c55d380\":[\"80\"],\"_c_61b32f3231bdc058c7442086\":[\"message\"],\"5e45193e10118d31971fc958\":[\"French\"],\"_c_60324c4728fec025e0cdf5e5\":[\"1609439400000\"],\"_c_61c2b4d8d1e4704b9b69b454\":[\"pp@gmail.com\"],\"5f8825f7a9e122666755ff21\":[\"No\"],\"_c_61968e1592d9691cfc2c25d5\":[\"joey\"],\"5f3b6a854c93195ce6052707\":[\"1000004510\"],\"_c_61968fc392d9691cfc2c6fc3\":[\"Joey\"],\"5ecb6f164089f07923ac4866\":[\"C33\"],\"_c_61965ba8fc7b2705b9dd9952\":[\"
Dinesh textarea
\"],\"586627b0e4b0c0e65c12340b\":[\"testing\"],\"5e31a0784d0a201425a9b49f\":[\"None\"],\"5e00369158eed644fb19b2e3\":[\"10\"],\"_c_60dd698892282518cb236dbe\":[\"hi\"],\"_c_61c2b28dd1e4704b9b697753\":[\"
Dec 25th XMAS
\"],\"5ecd11501834900fa981a215\":[\"https://www.google.com\"],\"_c_61c2b259d1e4704b9b696f41\":[\"1640370600000\"],\"5f9c4c29ff7313172751af27\":[\"No\"],\"_c_61c2b494d1e4704b9b69aaa7\":[\"1000124837\"],\"5f2e936a8dd919311a96bc09\":[\"1596825000000\"],\"_c_61bacf7d6726a318813ee6c8\":[\"Textarea default\"],\"_c_61c2b1cfd1e4704b9b695adc\":[\"Dec 25th XMAS\"],\"_c_6179077f13550944fe041cc1\":[\"Test1\"],\"_c_60f0166becf2506f242b673f\":[\"2\"],\"5ebb1f21ad762a5cd6e263ee\":[\"5\"],\"_c_61bacde96726a318813ed275\":[\"Text Default value\"],\"5b3f6a8ee4b0df2023c53017\":[\"Profile\"],\"_c_61c0cc9e35c836231e0d462f\":[\"val1D\"]},\"urlShortenerId\":\"\"},\"status\":\"DRAFT\",\"sourceLocale\":\"en_GB\",\"contentLocale\":\"en_GB\",\"autoResponse\":false,\"createdTime\":1648633681319,\"modifiedTime\":1648633681319,\"authorId\":1000069599},\"eventTime\":1648633681578,\"subscriptionDetails\":{\"subscriptionId\":\"6230a3b4215cc62878dbfe58\"}}"
       ],
       "cursor": "624d6111811f63194273b055"
   },
   "errors": []
}





[](https://dev.sprinklr.com/retrieve-failed-webhook-events)




[Back to top](https://dev.sprinklr.com/retrieve-failed-webhook-events)
