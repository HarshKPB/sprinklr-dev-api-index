---
title: "CFM Survey Responses Webhook"
slug: cfm-survey-responses-webhook
url: https://dev.sprinklr.com/cfm-survey-responses-webhook
---

# CFM Survey Responses Webhook

#   CFM  Survey Responses Webhook

The CFM Survey Response Webhook notifies your system when a new survey response is created. This allows you to capture, process, and analyze survey feedback in real time. This webhook is triggered when a survey response is submitted.

**Survey Response Webhook Subscription:**
Survey Response Created

### Survey Response Webhook




  Copy Code



{
  "id": "68b54b4d20594053401c88e3",
  "type": "survey.response.created",
  "payload": {
    "surveyId": "68416ef298e01519a0b40f53",
    "responseId": "68b4556ecf71bc40fed0e2cd",
    "responseStatus": "COMPLETE_RESPONSES",
    "createdTime": 1756711755000,
    "surveyLanguage": "en",
    "surveyMode": "STANDARD",
    "surveyResponseType": "STANDARD",
    "distributionEntityId": "68416f9198e01519a0b479bc",
    "responderSnId": "tanmay.srivastava+aug31@sprinklr.com",
    "responderSnType": "EMAIL",
    "surveyStartTime": 1756711740077,
    "surveyOpenTime": 1756711736272,
    "browser": "Chrome 13",
    "browserVersion": "139.0.0.0",
    "operatingSystem": "Mac OS X",
    "deviceType": "COMPUTER",
    "responseQuality": "NA",
    "questionResponses": {
      "AS_3_hi": [
        "बीवीजेके"
      ],
      "DB_6_DB_5": [
        "8.0"
      ],
      "AS_3": [
        "bvjk"
      ],
      "ST_7-:-b5c5a9bd-741a-4915-a8fc-aa112f454d25": [
        "2.0"
      ],
      "ST_8": [
        "Option 1"
      ],
      "ST_7-:-bb1c6352-5fde-42d6-b326-58652df66e6c": [
        "1.0"
      ],
      "DB_2": [
        "7.0"
      ],
      "ST_7": [
        "bb1c6352-5fde-42d6-b326-58652df66e6c",
        "b5c5a9bd-741a-4915-a8fc-aa112f454d25"
      ]
    },
    "customProperties": {},
    "transactionCustomProperties": {
      "_c_685bbcea402bb16a007c47ed": [
        "Food 1"
      ]
    }
  },
  "eventTime": 1756711757649,
  "subscriptionDetails": {
    "subscriptionId": "68ad569c4185bb37f2e57a1d"
  }
}







## Response Parameters











      ****





| Parameter | Type | Description |
| --- | --- | --- |
| id | string | Unique identifier of the webhook event. |
| type | string | Event type. For this webhook, the value is survey.response.created. |
| payload | object | Contains detailed survey response information. |
| eventTime | number | Epoch timestamp (in milliseconds) when the event was generated. |
| subscriptionDetails | object | Information about the webhook subscription. |


### `payload` Object












      ********


      ********
      ****************


      ************





      ****************************
      ********************





| Parameter | Type | Description |
| --- | --- | --- |
| surveyId | string | Unique identifier of the survey. |
| responseId | string | Unique identifier of the survey response. |
| responseStatus | string | Status of the survey response. Supported values: COMPLETE_RESPONSES, PARTIAL_RESPONSES. |
| createdTime | number | Epoch timestamp (ms) when the response was created. |
| surveyLanguage | string | Language in which the survey was submitted (ISO code). |
| surveyMode | string | Mode of survey execution. Supported values: STANDARD, CONVERSATIONAL. |
| surveyResponseType | string | Type of survey response. Supported values: ARCHIVED_RESPONSES , IMPORTED_RESPONSES, LIVE_RESPONSES, TEST_RESPONSES. |
| distributionEntityId | string | Identifier of the survey distribution entity. |
| responderSnId | string | Unique identifier for the responder. (for example, email or phone). |
| responderSnType | string | Channel type associated with the response. Supported values: EMAIL, SMS, WHATSAPP_BUSINESS. |
| surveyStartTime | number | Epoch timestamp when the survey started. |
| surveyOpenTime | number | Epoch timestamp when the survey was opened. |
| browser | string | Name of the browser used by the responder. |
| browserVersion | string | Browser version. |
| operatingSystem | string | Operating system of the responder's device. |
| deviceType | string | Device type used to submit the survey. Supported values: COMPUTER, MOBILE, TABLET, GAME_CONSOLE , DMR, WEARABLE, UNKNOWN. |
| responseQuality | string | Indicates the AI generated quality of the survey response. It can be NA(indicates response quality not generated), High, BOT(indicates system has flagged it as bot response) ,Low,  Medium. |
| questionResponses | object | Key-value map of survey questions and responses. Keys represent question IDs; values are the corresponding answers. |
| customProperties | object | Any additional custom properties attached to the survey. |
| transactionCustomProperties | object | Custom properties tied to the transaction entity. |


### `subscription` Object













| Parameter | Type | Description |
| --- | --- | --- |
| subscriptionId | string | Identifier of the webhook subscription that triggered this event. |


## Example Use Cases



- Store responses in a database for further analysis.

- Trigger downstream workflows such as sending confirmation emails or escalating low survey scores.

- Map responses to customer profiles using **responderSnId** and **responderSnType**.


[](https://dev.sprinklr.com/cfm-survey-responses-webhook)

[Back to top](https://dev.sprinklr.com/cfm-survey-responses-webhook)
