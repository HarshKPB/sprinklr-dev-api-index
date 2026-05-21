---
title: "Profile v1"
slug: profile-v1
url: https://dev.sprinklr.com/profile-v1
---

# Profile v1

#
Profile

An enterprise interacts with its prospects, customers, advocates, detractors, etc. These are known as Profiles.

A Sprinklr Global Profile is a single database record for a user that comes into the Sprinklr Platform. This allows brands to ensure they do not have duplicate, conflicting records on users interacting with brand accounts and allows the Sprinklr Platform to display threaded conversations.

**Related Knowledge Base Article:**  **[Sprinklr Global Profiles](https://www.sprinklr.com/help/articles/profile-list/sprinklr-global-profiles/6467a1b48ea3c9635cf37459)**

## AudienceProfile - Table 1

The social profile details.


















































| Fields | Type | Description |
| --- | --- | --- |
| firstName | String | The contact’s first name |
| lastName | String | The contact’s last name |
| fullName | String | The contact’s full name |
| email | String | The contact’s email address |
| phoneNo | String | The contact’s phone number |
**while these fields are available, usually very limited information exists for these attributes of a profile.*



































| Fields | Type | Description |
| --- | --- | --- |
| age | Integer | The contact’s age |
| location | String | The contact’s location |
| gender | String | The contact’s gender |
| ageRange | String | The contact’s age range |


**Demographic details are not available for all Channels*




















							[ChannelType](https://dev.sprinklr.com/channels-v1)





































































| Fields | Type | Description |
| --- | --- | --- |
| name | String | Profile name |
| type | String |  |
| snId | String | Unique ID for the profile |
| userName | String | Screen name |
| bio | String | Biographical information for the profile |
| following | int | The number of users the profile is following |
| followers | int | The fan followers for the profile |
| favCount | int | The favorite count |
| reach | int | The reach count |
| statusCount | int | The number of status updates |
| url | String | The profile url |
| profileImageUrl | String | The profile’s image url |
| snCreatedTime | long | The profile creation time in the social network |
| snModifiedTime | long | The last profile update time in the social network |
| verified | Boolean | The indication of a verified profile, as supported by the social channel |


**Depending on the Channel's data transfer policy, portions of this information above may or may not be available.*






























| Fields | Type | Description |
| --- | --- | --- |
| participationIndex | float | The participation index for the profile |
| influencerIndex | float | The influencer index for the profile |
| spamIndex | float | The spam index for the profile |










| spamIndex | float | The spam index for the profile | The spam index for the profile |
| --- | --- | --- | --- |
| kloutScore | Integer | The klout score of the profile |  |

##  Table 2


























































































| Fields | Type | Description |
| --- | --- | --- |
| id | String | Unique internal ID for the profile |
| contactInfo | ContactInfo | The contact information of the profile |
| demographics | Demographics | The demographic details |
| socialProfiles | List<SocialProfile> | The array of social profiles |
| socialScoreCard | SocialScoreCard | The Sprinklr-defined scorecard for the profile which captures the spam and influencer index |
| profileWorkflowProperties | ProfileWorkflowProperties | ProfileWorkflowProperties object |
| snCreatedTime | long | Profile creation time in channel; Unix time in ms |
| snModifiedTime | long | Profile modified time in channel; Unix time in ms |
| createdTime | long | Profile creation time in Sprinklr; Unix time in ms |
| AudmodifiedTime | long | Profile modified time in Sprinklr; Unix time in ms |
| accountsFollowedByUser | List<Long> | List of accounts followed by user |
| accountsFollowingUser | List<Long> | List of accounts following the user |
| accountsUnFollowedByUser | List<Long> | List of accounts unfollowed by user |
| accountsUnFollowingUser | List<Long> | List of accounts stop following the user |
| accountsBlockingUser | List<Long> | List of accounts blocking the user |
| additional | List<String> | Other properties of the profile |

Note: Social Scoring index currently is mainly for Twitter, but other channels will be covered in the future.

##  Table 3

Sender/Receiver profile inside inbound message




































































































































































































| Fields | Type | Description |
| --- | --- | --- |
| snType | String | Channel Type for the Profile |
| age | Int | Age of the social profile |
| location | String | Location of the social profile |
| gender | String | Gender of the social profile |
| snId | String | Unique message identifier of the message associated with the profile in the given context. |
| name | String | Username of the social profile on channel |
| screenName | String | Screen name for the channel account added in the system |
| email | String | Email of the social profile on channel |
| bio | String | Bio of the social profile on channel |
| following | Integer | Following count of social profile on channel |
| followers | Integer | Followers count of social profile on channel |
| favcount | Integer | Favorite count of social profile on channel |
| statusCount | Integer | Status count of social profile on channel |
| permalink | String | Permalink of profile on channel |
| profileUrl | String | Profile URL from social profile on channel |
| createdTime | String | Creation Time of the social profile in the system |
| modifiedTime | String | Modified Time of the sociak profile in the system |
| profileImgUrl | String | Profile Image URL of the social profile |
| profileWorkflowProperties | ProfileWorkflowProperties | Profile workflow properties for the social profile |
| clientId | Long | ClientId |
| accountId | Long | Unique Identifier for the channel account added in the system |
| universalProfileId | Long | Universal profile Id of the social profile |
| participationIndex | Float | Participation Index of social profile |
| influencerIndex | Float | Influencer Index of social profile |
| spamIndex | Float | Spam Index of social profile |
| spamFlag | Boolean | Is the social profile marked spam? |
| delFlag | Boolean | Is the social profile marked deleted ? |
| isBlocked | Boolean | Is social profile blocked ? |
| accountsFollowedByUser | List<Long> | List of social accounts followed by the social profile |
| accountsFollowingUser | List<Long> | List of social accounts following by the social profile |
| accountsBlockingUser | List<Long> | List of social accounts blocking the social profile |
| profileTags | Collection<ProfileTags> | List of Profile tags associated with the social profile |
| accountsUnFollowedByUser | List<Long> | List of accounts unfollowed by user |
| accountsUnFollowingUser | List<Long> | List of accounts stop following the user |
| snCreatedTime | Long | Created time of the user, when the user started following. |
| snModifiedTime | Long | Modified time of the user. |
| totalPosts | Long | Total post by the user. |

[](https://dev.sprinklr.com/profile-v1)




[Back to top](https://dev.sprinklr.com/profile-v1)
