---
title: "Update Channel Case Details"
slug: update-channel-case-details
url: https://dev.sprinklr.com/update-channel-case-details
---

# Update Channel Case Details

#
 BETA!  PUT - Update Channel Case Details


Using this API call, the 3rd party platform channel case Id can be stored within a Sprinklr case. The external case will have the channel case details. The case-level properties that are passed within the external case object will get updated on a Sprinklr case.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/case/channel-case-details

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

### Request Parameters











































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| installedAppId |  | Optional | Refers to the unique identifier for the app where the case is being handled | String |
| caseNumbers |  | Required | Refers to the list of case numbers you want to update the channel details for | List [Integer] |
| externalCase |  | Required | Object containing the external case details | Object |
|  | id | Optional | Refers to the external case Id | String |
|  | caseNumber | Optional | Refers to the external case number | String |
|  | channelType | Optional | Refers to the channel type where the external case exists | String |
|  | createdTime | Optional | Refers to the time at which the case was created in the external system | Epoch |
|  | modifiedTime | Optional | Refers to the time at which the case was last modified in the external system | Epoch |
|  | permalink | Optional | Refers to the url where the case exists in the external system | Url |

## Example - Request




 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/case/channel-case-details \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -d '{
    "installedAppId": "62fcb247d3fd352ae1272854",
    "caseNumbers": [
        18194237
    ],
    "externalCase": {
        "id": "5002v0000375CFXAA2",
        "caseNumber": "00005108",
        "channelType": "SALESFORCE",
        "createdTime": 1669379757000,
        "modifiedTime": 1669379757000,
        "permalink": "https://lalithsf231-dev-ed.my.salesforce.com/5002v0000375CFXAA2"
    }
} '



## Example - Response




{
    "data": [
        {
            "id": "63848452d5a15757a16229f7",
            "caseNumber": 18194237,
            "subject": "OAuth Test Account",
            "description": "text content from api",
            "version": 20,
            "status": "New",
            "priority": "Medium",
            "externalCase": {
                "channelType": "SALESFORCE",
                "permalink": "https://lalithsf231-dev-ed.my.salesforce.com/5002v0000375CFXAA2",
                "modifiedTime": 1669379757000
            },
            "externalCaseInfo": {
                "externalCases": []
            },
            "workflow": {
                "assignment": {
                    "assigneeId": "600004599",
                    "assigneeType": "USER",
                    "assignedById": 600004599,
                    "assignmentTime": 1669629010301
                },
                "customProperties": {
                    "_c_62d69d939852bf5aaf25e973": [
                        "SPRINKLR"
                    ],
                    "_c_62d69e3e9852bf5aaf25f323": [
                        "en"
                    ],
                    "spr_uc_status": [
                        "New"
                    ]
                },
                "queues": []
            },
            "channelCustomProperties": [],
            "contact": {
                "id": "APPLE_BUSINESS_CHAT_48290695-6464-4e3a-8b36-65a0e31a40e5",
                "name": "TestAccount",
                "channelType": "APPLE_BUSINESS_CHAT",
                "channelId": "48290695-6464-4e3a-8b36-65a0e31a40e5",
                "fromSnUserId": "48290695-6464-4e3a-8b36-65a0e31a40e5"
            },
            "createdTime": 1669629010302,
            "modifiedTime": 1673594976583,
            "firstMessageId": "ACCOUNT_600001079_1621513311635_APPLE_BUSINESS_CHAT_317_f374eea0-64e7-4031-9347-185803f62bef",
            "sentiment": 0,
            "latestProfileMessageAssociatedTime": 1621513311635,
            "conversationId": "48290695-6464-4e3a-8b36-65a0e31a40e5_urn:mbid:AQAAY3RBepJ6tIWXKLmZBmqUKb6ZYfAdFGI3AEtusg5jrUSYksuK3QeD/MfYLjHDXvv01gfVZDoUKXCObgRsb0HeLHuQz+CiKI4yk/GoAWIPEbJHtJX1Qs/inhySc/XklecIWi4qfcjAyWgzaGtZyaPIJXPxm0Y=",
            "firstMessageAssociatedTime": 1621513311635,
            "latestMessageAssociatedTime": 1621513311635,
            "firstUserBrandResponseCreationTime": 1621513311635,
            "totalProcessingClockTime": 118026,
            "allEngagedUsersList": [
                "600004599"
            ]
        }
    ],
    "errors": []
}





[](https://dev.sprinklr.com/update-channel-case-details)




[Back to top](https://dev.sprinklr.com/update-channel-case-details)
