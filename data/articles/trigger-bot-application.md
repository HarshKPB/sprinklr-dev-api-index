---
title: "Trigger Bot Application"
slug: trigger-bot-application
url: https://dev.sprinklr.com/trigger-bot-application
---

# Trigger Bot Application

#
 POST  Trigger Bot Application



This API is part of Sprinklr’s [Conversational AI](https://www.sprinklr.com/help/categories/conversational-ai/63a32b81acb01e67d8b8eca9), which is an automated AI-powered virtual assistant that can engage with customers. By running this API call, you will be able to trigger the bot application and gather insights into the current flow of the conversation in the [dialogue tree](https://www.sprinklr.com/help/categories/dialogue-trees-overview/63f0b6c0ead12b20fb281b82),  associated with an application.

**Dev Notes: **For enabling Conversational AI capability in your environment, please work with your Success Manager.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/triggerBotApplication

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



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| applicationId | Required | The unique Id of bot application | String |
| text | Required | The message sent  by the user | String |
| conversationId | Required | The unique id of the conversationNote:You can enter a random conversation id for triggering a new conversation. And, the exact conversation Id for gathering context of an existing conversation | String |
| language | Required | Example:“en” for English“all” for all languages | string |

## Example - Request















Copy Code



curl -X POST \
 https://api3.sprinklr.com/{env}/api/v2/triggerBotApplication\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
  "applicationId": "62ac484807936f269bd4548b",
  "text": "Test Bot App",
  "conversationId": "TRIGGER_BOT_APPLICATION_2",
  "language": "en"
}'






## Example - Response





{
"data": {
       "response": {
           "responseDTOList": [
               {
                   "responseDetails": [
                       {
                           "responseType": "TEXT",
                           "detail": {
                               "text": "Hey",
                               "responseDelay": 0
                           }
                       }
                   ],
                   "botParameters": {
                       "CURRENT_APPLICATION_DETECTED_SLOT": {},
                       "BOT_CONTEXT_ID": "62ac5b1707936f269bd4b404",
                       "NUM_DETECTED_ISSUE_TYPES_ON_CURRENT_MESSAGE": 0,
                       "SUBSEQUENT_ISSUE_TYPE_CONTEXT": "false",
                       "UPDATED_FIELDS": [],
                       "NUM_PENDING_ISSUE_TYPES": 0,
                       "INLINE_PUBLISH": false,
                       "ROOT_BOT": "a2738202-ba09-4bbc-8280-2c3fd40ea181",
                       "FALLBACK_BOT": false,
                       "DISABLE_TRANSITION_ON_LOCAL_FALLBACK": false,
                       "Language": "en",
                       "NUM_DETECTED_ISSUE_TYPES": 0,
                       "DETECTED_INTENTS": [],
                       "BOT_APPLICATION_ID": "62ac484807936f269bd4548b",
                       "USER_SAYS_TEXT": "This134",
                       "TYPING_INDICATOR_ENABLED": false
                   },
                   "accumulatedMessages": [
                       {
                           "assetCreatedTime": 1655462679383,
                           "messageText": "This134",
                           "matchedThemes": []
                       }
                   ],
                   "endOfConversation": false,
                   "endOfApplication": false,
                   "reTrigger": false,
                   "currentBotActivityId": "node-d1052330-dd70-48c7-948d-1b12953a64c2",
                   "fallbackResponse": false,
                   "routeToAgent": false,
                   "waitForAsyncResponse": false,
                   "routedToIVR": false,
                   "botGatherDTMF": false,
                   "accumulated": false,
                   "waitForAccumulation": false,
                   "ignored": false,
                   "retryOnFallback": false,
                   "triggerFilterMatched": true,
                   "processDefinitionId": "a2738202-ba09-4bbc-8280-2c3fd40ea170",
                   "error": false,
                   "lastBotReplyTime": 1655462679434,
                   "transition": false
               }
           ],
           "conversationContext": {
               "id": "62ac5b1707936f269bd4b404",
               "conversationId": "TRIGGER_BOT_APPLICATION_2",
               "applicationId": "62ac484807936f269bd4548b",
               "detectedIssueTypes": [],
               "pendingIssueTypes": [],
               "completedIssueTypes": [],
               "botVsConversationStatus": {
                   "a2738202-ba09-4bbc-8280-2c3fd40ea170": "WAITING_FOR_RESPONSE"
               },
               "botVsTriggeredByIssueType": {},
               "finished": false,
               "createdTime": 1655462679412,
               "modifiedTime": 1655462679443,
               "detectedSlots": {},
               "anyTriggerFilterMatched": true,
               "processedAssetIds": [],
               "lastApplicationReplyTime": 1655462679434,
               "issueTypeVsTriggeredByIntents": {},
               "detectedIntents": [],
               "currentDetectedIssueTypes": [],
               "currentPendingIssueTypes": [],
               "currentDetectedIntents": [],
               "intentsToDiscover": [],
               "entitiesToDiscover": [],
               "buttonsToDiscover": [],
               "replay": false,
               "ignoreTransition": false
           },
           "repeatedIssueTypeFallback": false
       },
       "botStatus": "WAITING_FOR_RESPONSE"
   },
   "errors": []
}






[](https://dev.sprinklr.com/trigger-bot-application)




[Back to top](https://dev.sprinklr.com/trigger-bot-application)
