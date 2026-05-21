---
title: "Outbound Messages (Posts) v1"
slug: outbound-messages-posts-v1
url: https://dev.sprinklr.com/outbound-messages-posts-v1
---

# Outbound Messages (Posts) v1

# Outbound Messages (Posts) v1

## Post Object

The Post object is used in [Post Insights Reporting](https://dev.sprinklr.com/post-insights-report-v1).







[ChannelType](https://dev.sprinklr.com/channels-v1)

[AccountType](https://dev.sprinklr.com/accounts-v1)

[MessageType](https://dev.sprinklr.com/message-v1)

[See Content object details below](https://dev.sprinklr.com/outbound-messages-posts-v1#post_content_object)

[See Taxonomy object details below](https://dev.sprinklr.com/outbound-messages-posts-v1#taxonomy_table)

[See Approval object details below](https://dev.sprinklr.com/outbound-messages-posts-v1#approval_table)

**

[UniversalMessageKey](https://dev.sprinklr.com/outbound-messages-posts-v1#universal_message_key)

[UniversalMessageKey](https://dev.sprinklr.com/outbound-messages-posts-v1#universal_message_key)

| Fields | Type | Description |
| --- | --- | --- |
| postId | long | Sprinklr internal id uniquely identifying the post |
| messageId | long | Sprinklr internal id uniquely identifying the associated message |
| accountId | long | Sprinklr internal id uniquely identifying the account for the post |
| accountGroupId | long | Sprinklr internal id uniquely identifying the accountGroup for the post |
| authorId | long | author of the post |
| clientId | long | client in which the post was created |
| channelType |  | channel type |
| accountType |  | account type |
| messageType |  | message type |
| content | Content object | Content of the post. Includes message text, images etc. |
| taxonomy | Taxonomy Object | Taxonomy of the post. |
| approval | Approval object | Approval information. |
| status | Status | status of the post = {SENT, SCHEDULED, DRAFT, APPROVAL, REJECTED(true), REJECTED_BY_RULE, FAILED, NATIVELY_SCHEDULED, QUEUED, CONVERTED_TO_POSTS, DRAFT_CONVERTED_TO_POSTS, RECALLED_FROM_APPROVAL, RECALLED, GROUP_POST_COMPLETED} *QUEUED: the message has been picked up for sending |
| createdDate | long | Post created time in Unix time in ms |
| scheduleDate | long | Post scheduled time in Unix time in ms |
| version | int | version of the post |
| deleted | boolean | whether the post is deleted |
| statusID | String | id as represented on the channel. Valid only when the post is published |
| parentUniversalMessageKey |  | UniversalMessageKey identifying the parent message |
| inReplyToUniversalMessageKey |  | UniversalMessageKey identifying the message this post is replying to |
| publishedDate | long | date value in milliseconds. It is UNIX time in UTC*1000. Valid only when the post is published. |
| permalink | String | permalink on the channel.Valid only if the post is published |
| additional | List<<String>> | any additional data including list of links |

## UniversalMessageKey







| Fields | Type | Description |
| --- | --- | --- |
| snType | String | ChannelType |
| msgType | Integer | Queue id |
| snMsgId | String | Social network channel message id |
| snCreatedTime | Long | Unix time in ms for message creation time at the channel |
| sourceType | String | SourceType |
| sourceId | Long | accountId for ACCOUNT; searchId for PERSISTENT_SEARCH |
| universalMessageId | String | Unique internal message Id |
| snCreatedTimeYearMonth | String |  |

## Sub-Object Details

### Content Object







[See Attachment object details below](https://dev.sprinklr.com/outbound-messages-posts-v1#attachment_table)

[See Link object details below](https://dev.sprinklr.com/outbound-messages-posts-v1#link_details_table)

| Fields | Type | Description |
| --- | --- | --- |
| message* | String | Message description |
| title | String | Message title |
| attachment | attachment Object | Attachments to the post. |
| languageCode | String | Language code of message |
| annotations | String |  |
| subject | String |  |
| textAssetIds | List<String> |  |
| linkAssetIds | Map<String, String> |  |
| twitterCardAssetDetails | List<TwitterCardAssetDetail> |  |
| linkDetails | List<OutboundLinkDetails> |  |
| templateId | Long |  |
| contentType | String | text or html |
| postName | String | post description |
| postDescription | String | post description |
| urlEntities | Map<String,List<URLRntity>> |  |
| textEntities | Map<String,List<TextEntity>> |  |
| additional | Map<String,List<String>> |  |

### Taxonomy Object







| Fields | Type | Description |
| --- | --- | --- |
| campaignId* | String | Unique Identifier for campaign |
| urlShortnerDomain | String | Urlshortnerdomain to be used for publishing. Example: spr.ly |
| tags | List<String> | Object storing value of tags to message |
| clientCustomProperties | Map<String, List<String>> | A map of client custom properties key, values pair that message is assigned to. |
| partnerCustomProperties | Map<String, List<String>> | A map of partner custom properties key, values pair that message is assigned to. |
| assetVisibility | Map<String,List<Long>> | Getting this field post schedule response |

### Approval Object







| Fields | Type | Description |
| --- | --- | --- |
| approvalOption* | String | Must be one of {NONE, USER, APPROVAL_PATH, ACCOUNT_USER} |
| approverUserId | Long | Unique userId of the approver, it is required field if option=USER |
| approvalPathId | String | Unique id of the approval path, it is required field if option= APPROVAL_PATH |
| comment | String | Any comments for the approver |

### Attachment Object







[See Media object details below](https://dev.sprinklr.com/outbound-messages-posts-v1#media_objects_table)

****
```

```
****
```

```
****
```

```

| Fields | Type | Description |
| --- | --- | --- |
| type* | String | Attachment type: One of {PHOTO, VIDEO, LINK, ALBUM, PRESENTATION} |
| mediaList* | List<mediaObject> | Media objects associated with the post.  Examples for mediaProperties: Example 1: Youtube(2828), for post insights                      mediaProperties: { playlistId: "", playlistPosition: "TOP", visibility: "UNLISTED", category: "1", tags: [0], channelType: "YOUTUBE" }                                          Example 2: SLIDESHARE(2682), for post insights                      mediaProperties: { downloadable: false, makePrivate: false, shareable: false, embedable: false, secret: false, tags: [0], channelType: "SLIDESHARE" }                               Example 3 : FLICKR(2793), for post insights                  mediaProperties: { publicVisibility: true, friendVisibility: false, familyVisibility: false, channelType: "FLICKR" } |
| title | String | Title of attachment |
| description | string | Description of attachment |

### Media Object







| Fields | Type | Description |
| --- | --- | --- |
| type* | String | Media type: One of {PHOTO, VIDEO, LINK, PRESENTATION} |
| source* | String | URL of the media |
| previewImageUrl | String | Preview URL of the media |
| title | String | Title of attached media object |
| description | String | Description of attached media object |
| imageUrl | String | Url of the image |
| sourceType | String | sourceType of the media (raw, html) |
| mediaAssetId | String |  |
| mediaProperties | MediaProperties | JSON element with name/properties for different channels |
| additional | Map<String, List<String>> |  |

### Link Object







| Fields | Type | Description |
| --- | --- | --- |
| link | String |  |
| <queryParams> | Map<String,String> |  |
| originalLink | String |  |
| twitterCardLink | boolean |  |
| isShortLink | boolean |  |
| redirectedLink | boolean |  |
|  | String |  |

[](https://dev.sprinklr.com/outbound-messages-posts-v1)
