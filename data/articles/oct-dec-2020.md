---
title: "Oct - Dec, 2020"
slug: oct-dec-2020
url: https://dev.sprinklr.com/oct-dec-2020
---

# Oct - Dec, 2020

# Oct - Dec, 2020

**Developer Note:**We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.	Please note that the API base endpoint has changed from `api2` to `api3`.

For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## **Sprinklr API Updates for Facebook Europe** - December 16, 2020

	**Upcoming Breaking Change for Europe:**
Note that this includes a breaking changes to the API and may require a code change on your side. See below for more details.

As part of Facebook's efforts to comply with new privacy rules in Europe, they are making API updates which will impact developers and businesses that use Sprinklr Publishing API for direct messaging.

[Checkout Messenger API Updates for Europe](https://developers.facebook.com/docs/messenger-platform/europe-updates)

As part of Sprinklr's efforts to best serve its customers, we are updating the support for the affected Facebook features so that there is minimum impact on the live operations of our customers.

[Checkout Sprinklr Mitigation Plan](https://help.sprinklr.com/Knowledge_Base/Experience_Cloud_User_Guides/Channel_Guides/Facebook_Channel_Overview/Facebook_Messenger_API_Updates_and_Sprinklr_Mitigation_Plan_for_Europe#Feature_4_-_Typing_Indicator.2FRead_Receipts)

**API Endpoint Impacted**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/message
GET https://api2.sprinklr.com/{env}/api/v2/message/byMessageId
GET https://api2.sprinklr.com/{env}/api/v2/profile
GET https://api2.sprinklr.com/{env}/api/v2/profile/{profileId}
POST https://api2.sprinklr.com/{env}/api/v2/reports/query
POST https://api2.sprinklr.com/{env}/api/v1/listening/query/stream
POST https://api2.sprinklr.com/{env}/api/v1/listening/topics
POST https://api2.sprinklr.com/{env}/api/v1/conversations/new/message-details
GET https://api2.sprinklr.com/{env}/api/v1/message/{umId}
GET https://api2.sprinklr.com/{env}/api/v1/profile/conversations
GET https://api2.sprinklr.com/{env}/api/v1/profile
POST https://api2.sprinklr.com/{path}/api/v1/profile/search
POST https://api2.sprinklr.com/{path}/api/v1/reports/query
**API Capabilities Impacted**






















| API Capability Impacted | Description |
| --- | --- |
| Media Attachment | The media files would not be rendered visually within the chat. Customers would receive a link to access the media file. Brand’s customers would click on the URL and it would load the media in the in-app browser of the Messenger. |
| Fan Profile | The Sender Profile object will not come in response when you fetch the Message by MessageId. Facebook Messenger would not share profile information of the brand’s customer, for example, Profile name, Profile image but would send a unique identifier for a profile |
| Interactive Template | Brands cannot send these interactive templates. API would not support Generic Template (Carousel Template) and Button Template |

	**Webhook Capabilities Impacted**






















| Webhook Impacted | Description |
| --- | --- |
| Message Received | Brand would not get detailed sender profile in webhook. |
| Profile Created | Brand would not get profile details in webhook. |
| Message Read | Brand would not get message read webhook. |

## **Listening Topic Cluster API - Enhancement ** - November 8, 2020

You can use this API to fetch the Topic Cluster widget details in Json. Now you can even use `TOPIC`, `THEMES` and` KEYWORD_LIST` Ids in filters to fetch the required response.


**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/listening/query/widget

## **User Search API ** - November 7, 2020

	**Upcoming Breaking Change:**
 Note that this includes breaking changes to the API and may require a code change on your side. See below for more details.

As of November 7, a new governance feature is being put in place to ensure that only the API keys with appropriate access to the Sprinklr Users section are able to take necessary actions using the SCIM API.

We recommend ensuring that the API users have access to appropriate Users under Platform Settings within Sprinklr, prior to the launch of this feature on November 7, 2020.


**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/scim/v2/Users/search

## ** Listening Topic API - Enhancement ** - November 1, 2020

You will get the query in the response along with topics. The query contains the they keywords that you have used while creating the topic.




  Copy Code



{
                "id": "5f9beabd6fcf2b678hg4fefe",
                "name": "locationBased",
                "topicGroup": "5f9beabd6fcf2b678hg4fefe",
                "tags": [],
                "modifiedTime": 1604050813052,
                "createdTime": 1604053034382,
                "enabled": false,
                "query": “((\”new\” OR (\”brand\” AND \”bikes\” AND \”launch\”) AND  NOT \"asfsdv\")",
                "dataSources": [
                    "TWITTER",
                    "FACEBOOK",
                    "INSTAGRAM",
                    "YOUTUBE
                ],
                "languageCodes": [],
                "countryCodes": []
            }





**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/listening/topics

## **Publishing Post API - Enhancement ** - October 16, 2020

You can use the publishing post API to send SMS to users/fans.


**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/post

## **Add Comment API - Enhancement ** - October 16, 2020

You can use the Add Comment API to add comment in different entity types with attachment using the response from Media Upload API.

 The Media Upload API endpoint is specific to creating attachment in comments.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/media/upload

## **Link Shortener ** - October 4, 2020

You can use this api to create vanity and non vanity short links and in response you will get the shortened URL and other related objects after making the Request.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/link/shorten

## **Read URL Shorteners ** - October 4, 2020

You can use this api to read the available URL Shorteners and their Ids and can check the availability of VanityUrl for an Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/link/shortners

[](https://dev.sprinklr.com/oct-dec-2020)

[Back to top](https://dev.sprinklr.com/oct-dec-2020)
