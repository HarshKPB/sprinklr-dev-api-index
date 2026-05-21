---
title: "Update Topic 2.0"
slug: update-topic-2-0
url: https://dev.sprinklr.com/update-topic-2-0
---

# Update Topic 2.0

#
  PUT - Update Topic


	You can use this API endpoint to update a Listening Topic using the unique Topic Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/listening-topic/{topicId}

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

###  Path Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| topicId | Required | The unique Listening Topic Id. | String |

### Request Body





















































































































































































































































































































































































































****




| Fields | Sub-Fields | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | Listening Topic name. | String |
| displayName |  | Optional | Listening Topic display name | String |
| topicType |  | Required | Listening topic type, possible values : ACCOUNT_LISTENING, PROFILE_LISTENING, QUERY_LISTENING, GEO_LOCATION | String |
| description |  | Optional | Listening Topic description | String |
| topicGroupId |  | Required | Topic Group ID to which this Listening Topic belongs. | String |
| startDate |  | Required | Start date for Listening Topic  to become active. | Epoch |
| endDate |  | Required | End date for Listening Topic  to become in-active | Epoch |
| tags |  | Optional | Tags to group Listening Topic based on use case | List<String> |
| sources |  | Optional | Sources to grab data from | List<String> |
| enabled |  | Optional | Enable live data fetching. | Boolean |
| query |  | Optional | Keyword query to grab messages. | String |
| languageCodes |  | Optional | Languages from which data should be grabbed. | List<String> |
| countryCodes |  | Optional | Countries from which data should be grabbed. | List<String> |
| locations |  | Required | Locations from which data should be grabbed. | List<TopicApiLocation> |
|  | name | Optional | Location name. | String |
|  | latitude | Required | Latitude value for Point Location. | Double |
|  | longitude | Required | Longitude value for Point Location. | Double |
|  | radius | Required | Radius value for Point Location. | Double |
|  | unit | Required | Unit for Point Location, possible values : km for Kilometer and mi for Miles. | String |
| blockedDomains |  | Optional | Domains from which data should be blocked | List<String> |
| blockedDomainsListIds |  | Optional | Domain List IDs to block those Domain data. | List<String> |
| blockedClientProfileLists |  | Optional | Client Profile List IDs from which data should be blocked. | List<String> |
| blockedPartnerProfileLists |  | Optional | Partner Profile List IDs from which data should be blocked. | List<String> |
| blockedCountryCodes |  | Optional | Countries from which data should be blocked. | List<String> |
| blockedLanguageCodes |  | Optional | Languages from which data should be blocked. | List<String> |
| generatingSourceList |  | Optional | Generating Source List IDs from which data should be grabbed. | List<String> |
| generatingSources |  | Optional | Generating Sources from which data should be grabbed. | List<String> |
| blockedGeneratingSourceList |  | Optional | Generating Source List IDs from which data should be blocked. | List<String> |
| blockedGeneratingSources |  | Optional | Generating Sources from which data should be blocked. | List<String> |
| inclusiveDomains |  | Optional | Domains from which data should be grabbed. | List<String> |
| inclusiveDomainsListIds |  | Optional | Domains List IDs from which data should be grabbed. | List<String> |
| inclusiveClientProfileLists |  | Optional | Client Profile List IDs from which data should be grabbed. | List<String> |
| inclusivePartnerProfileLists |  | Optional | Partners Profile List IDs from which data should be grabbed. | List<String> |
| accountIds |  | Optional | Account IDs from which data should be grabbed. | List<Long> |
| accountGroupIds |  | Optional | Account Group List IDs from which data should be grabbed. | List<String> |
| excludeRetweets |  | Optional | Select true in order to exclude all retweets. | boolean |
| matchQuotedRetweets |  | Optional | Select true in order to match quoted retweets. | boolean |
| excludePossiblySensitiveContent |  | Optional | Select true in order to exclude Sensitive tweets. | boolean |
| excludeUrlsInSearch |  | Optional | Select true in order to exclude urls from keyword search. | boolean |
| onlyVerifiedUser |  | Optional | Select true in order to match verified users data. | boolean |
| minimumFollowerCount |  | Optional | Minimum follower count that publishing user should have, to match message. | Long |
| minimumMozRank |  | Optional | Minimum follower count that publishing user should have, to match message. | Long |
| maximumMozSpamScore |  | Optional | Maximum Moz rank to match message. | Integer |
| maximumAlexaRank |  | Optional | Maximum Alexa rank to match message. | Integer |
| dataVolumeThresholdApiConfig |  | Optional | Listening Topic data Volume Threshold Config. |  |
|  | duration | Required | Listening topic grabbing duration. | Integer |
|  | durationUnit | Required | Listening topic grabbing duration unit, possible values :  DAY, MONTH, YEAR, LIFETIME. | String |
|  | maxMentionCount | Required | Threshold on maximum messages that listening topic can grab in above duration. | Long |
|  | resetStartDate | Optional | Listening topic data volume start date in epoch time. | Boolean |
|  | userIdsToNotify | Optional | User ids to notify. | List<Long> |
|  | emailIdsToNotify | Optional | Emails ids to notify. | List<String> |
|  | userGroupIdsToNotify | Optional | User group ids to notify. | List<String> |
| iconUrl |  | Optional | Listening Topic icon url. | String |
| imageUrl |  | Optional | Listening Topic image url. | String |
| color |  | Optional | Listening Topic identification colour. | String |
| clientId |  | Optional | Listening topic client id | Long |
| partnerCustomProperties |  | Optional | Object defining the key-value pair for global level custom properties that needs to be applied on the listening topic.Syntax:"Custom property Id": [         "Value" ], | Object |

## Example - Request




 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/listening-topic/{6026124d33bd3d0c37hj7ddc}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'  \
  -d '{
  "name": "CreatedViaApiTest_03",
  "displayName": "Api Topic1",
  "topicType": "QUERY_LISTENING",
  "description": "Created via Listening API",
  "topicGroupId": "641968782b55714117d8bf04",
  "startDate": 1615140543000,
  "endDate": 1680065287000,
  "tags": [
    "API"
  ],
  "sources": [
    "TWITTER"
  ],
  "enabled": false,
  "query": "message: hello",
  "excludeRetweets": false,
  "matchQuotedRetweets": false,
  "excludePossiblySensitiveContent": false,
  "excludeUrlsInSearch": false,
  "onlyVerifiedUser": false,
  "clientId": 1,
  "partnerCustomProperties": {
            "_c_5e1d928a10118d06bce22ad5": [
                "1579026600001"
            ],
            "_c_62b4044cf8b78446db96e0ce": [
                "Topic"
            ],
            "_c_617118e558902477ef06a297": [
                "Test A"
            ]
  }
}'



## Example - Response




 {
    "data": {
        "id": "641e8829760f911a0f69625d",
        "name": "CreatedViaApiTest_03",
        "displayName": "Api Topic1",
        "topicType": "QUERY_LISTENING",
        "description": "Created via Listening API",
        "topicGroupId": "641968782b55714117d8bf04",
        "startDate": 1615140543000,
        "endDate": 1680065287000,
        "tags": [
            "API"
        ],
        "sources": [
            "TWITTER"
        ],
        "enabled": false,
        "query": "message: hello",
        "languageCodes": [],
        "countryCodes": [],
        "blockedDomains": [],
        "blockedDomainsListIds": [],
        "blockedClientProfileLists": [],
        "blockedPartnerProfileLists": [],
        "blockedCountryCodes": [],
        "blockedLanguageCodes": [],
        "blockedGeneratingSourceList": [],
        "blockedGeneratingSources": [],
        "inclusiveDomains": [],
        "inclusiveDomainsListIds": [],
        "inclusiveClientProfileLists": [],
        "inclusivePartnerProfileLists": [],
        "accountIds": [],
        "excludeRetweets": false,
        "matchQuotedRetweets": false,
        "excludePossiblySensitiveContent": false,
        "excludeUrlsInSearch": false,
        "excludeRevItemName": false,
        "onlyVerifiedUser": false,
        "createdTime": 1679722537733,
        "modifiedTime": 1679761075168,
        "ownerUserId": 1000157828,
        "lastModifiedUserId": 1000157828,
        "clientId": 1000004523,
        "partnerCustomProperties": {
            "_c_5e1d928a10118d06bce22ad5": [
                "1579026600001"
            ],
            "_c_62b4044cf8b78446db96e0ce": [
                "Topic"
            ],
            "_c_617118e558902477ef06a297": [
                "Test A"
            ]
  }
    },
    "errors": []
}





### Response Definitions























































































































































































































































































































****







































































| Field | Sub-Field | Description | Type |
| --- | --- | --- | --- |
| id |  | The unique Listening Topic Id. | String |
| name |  | Listening Topic name. | String |
| displayName |  | Listening Topic display name | String |
| topicType |  | Listening topic type, possible values : ACCOUNT_LISTENING, PROFILE_LISTENING, QUERY_LISTENING, GEO_LOCATION | String |
| description |  | Listening Topic description | String |
| topicGroupId |  | Topic Group ID to which this Listening Topic belongs. | String |
| startDate |  | Start date for Listening Topic  to become active. | Epoch |
| endDate |  | End date for Listening Topic  to become in-active | Epoch |
| tags |  | Tags to group Listening Topic based on use case | List<String> |
| sources |  | Sources to grab data from | List<String> |
| enabled |  | Enable live data fetching. | Boolean |
| query |  | Keyword query to grab messages. | String |
| languageCodes |  | Languages from which data should be grabbed. | List<String> |
| countryCodes |  | Countries from which data should be grabbed. | List<String> |
| locations |  | Locations from which data should be grabbed. | List<TopicApiLocation> |
|  | name | Location name. | String |
|  | latitude | Latitude value for Point Location. | Double |
|  | longitude | Longitude value for Point Location. | Double |
|  | radius | Radius value for Point Location. | Double |
|  | unit | Unit for Point Location, possible values : km for Kilometer and mi for Miles. | String |
| blockedDomains |  | Domains from which data should be blocked | List<String> |
| blockedDomainsListIds |  | Domain List IDs to block those Domain data. | List<String> |
| blockedClientProfileLists |  | Client Profile List IDs from which data should be blocked. | List<String> |
| blockedPartnerProfileLists |  | Partner Profile List IDs from which data should be blocked. | List<String> |
| blockedCountryCodes |  | Countries from which data should be blocked. | List<String> |
| blockedLanguageCodes |  | Languages from which data should be blocked. | List<String> |
| generatingSourceList |  | Generating Source List IDs from which data should be grabbed. | List<String> |
| generatingSources |  | Generating Sources from which data should be grabbed. | List<String> |
| blockedGeneratingSourceList |  | Generating Source List IDs from which data should be blocked. | List<String> |
| blockedGeneratingSources |  | Generating Sources from which data should be blocked. | List<String> |
| inclusiveDomains |  | Domains from which data should be grabbed. | List<String> |
| inclusiveDomainsListIds |  | Domains List IDs from which data should be grabbed. | List<String> |
| inclusiveClientProfileLists |  | Client Profile List IDs from which data should be grabbed. | List<String> |
| inclusivePartnerProfileLists |  | Partners Profile List IDs from which data should be grabbed. | List<String> |
| accountIds |  | Account IDs from which data should be grabbed. | List<Long> |
| accountGroupIds |  | Account Group List IDs from which data should be grabbed. | List<String> |
| excludeRetweets |  | Select true in order to exclude all retweets. | boolean |
| matchQuotedRetweets |  | Select true in order to match quoted retweets. | boolean |
| excludePossiblySensitiveContent |  | Select true in order to exclude Sensitive tweets. | boolean |
| excludeUrlsInSearch |  | Select true in order to exclude urls from keyword search. | boolean |
| onlyVerifiedUser |  | Select true in order to match verified users data. | boolean |
| minimumFollowerCount |  | Minimum follower count that publishing user should have, to match message. | Long |
| minimumMozRank |  | Minimum follower count that publishing user should have, to match message. | Long |
| maximumMozSpamScore |  | Maximum Moz rank to match message. | Integer |
| maximumAlexaRank |  | Maximum Alexa rank to match message. | Integer |
| createdTime |  | Listening topic created time | Long |
| modifiedTime |  | Listening topic last modified time | Long |
| ownerUserId |  | Listening topic owner user id | Long |
| lastModifiedUserId |  | Listening topic last modified user id | Long |
| clientId |  | Listening topic client id | Long |
| partnerCustomProperties |  | Object defining the key-value pair for global level custom properties that needs to be applied on the listening topic.Syntax:"Custom property Id": [         "Value" ], | Object |
| dataVolumeThresholdApiConfig |  | Listening Topic data Volume Threshold Config. |  |
|  | duration | Listening topic grabbing duration. | Integer |
|  | durationUnit | Listening topic grabbing duration unit, possible values :  DAY, MONTH, YEAR, LIFETIME. | String |
|  | maxMentionCount | Threshold on maximum messages that listening topic can grab in above duration. | Long |
|  | resetStartDate | Listening topic data volume start date in epoch time. | Boolean |
|  | userIdsToNotify | User ids to notify. | List<Long> |
|  | emailIdsToNotify | Emails ids to notify. | List<String> |
|  | userGroupIdsToNotify | User group ids to notify. | List<String> |
| iconUrl |  | Listening Topic icon url. | String |
| imageUrl |  | Listening Topic image url. | String |
| color |  | Listening Topic identification colour. | String |

[](https://dev.sprinklr.com/update-topic-2-0)




[Back to top](https://dev.sprinklr.com/update-topic-2-0)
