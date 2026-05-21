---
title: "Profile Webhooks"
slug: profile-webhooks
url: https://dev.sprinklr.com/profile-webhooks
---

# Profile Webhooks

# Profile Webhooks

**Profile Webhook Subscriptions:**
 Profile Created, Profile Updated, Profile Deleted and Profile Merged

Whenever an action is performed in profile either via Sprinklr UI or API, the webhook notification are triggered with the details that are described in the following documents:


- [Profile.Created Webhook](https://dev.sprinklr.com/profile-webhooks#profileCreate)

- [Profile.Updated Webhook](https://dev.sprinklr.com/profile-webhooks#profileUpdate)

- [Profile.Deleted Webhook](https://dev.sprinklr.com/profile-webhooks#profileDelete)

- [Profile.Merged Webhook](https://dev.sprinklr.com/profile-webhooks#profileMerged)

### Profile.Created Webhook




  Copy Code



{
  "id": "5f606d11b5922823f4f2942d",
  "type": "profile.created",
  "payload": {
    "id": "5f606d0eb5922823f4f28eb8",
    "contact": {
      "fullName": "Kugy!"
    },
    "demographics": {},
    "profiles": [
      {
        "name": "Kugy!",
        "channelType": "TWITTER",
        "channelId": "1299404062832631808",
        "permalink": "https://twitter.com/kugy",
        "avatarUrl": "https://twitter.com/kugy/profile_image?size=original",
        "bio": "@new  😼|| 𝙸𝚄; 𝙱𝚃𝚂 ♡︎ || ",
        "followers": 73,
        "username": "kugy",
        "verified": false,
        "unSubscribed": false,
        "deleted": false,
        "snCreatedTime": 0,
        "snModifiedTime": 0
      }
    ],
    "profileWorkflow": {
      "profileLists": [],
      "customProperties": {},
      "profileSpaceWorkflows": []
    },
    "createdTime": 1600154894960,
    "modifiedTime": 1600154894960
  },
  "eventTime": 1600154897788,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Profile.Updated Webhook




  Copy Code



{
  "id": "5f606d68b5922823f4f310c3",
  "type": "profile.updated",
  "payload": {
    "id": "5e67044225c7e60c708cf690",
    "contact": {
      "fullName": "agnes sintia"
    },
    "profiles": [
      {
        "name": "agnes sintia",
        "channelType": "TWITTER",
        "channelId": "1192609899244478464",
        "permalink": "https://twitter.com/agnessintia7",
        "avatarUrl": "https://twitter.com/agnessintia7/profile_image?size=original",
        "bio": "OT7",
        "followers": 23,
        "username": "agnessintia7",
        "verified": false,
        "unSubscribed": false,
        "deleted": false,
        "snCreatedTime": 0,
        "snModifiedTime": 0
      }
    ],
    "profileWorkflow": {
      "profileLists": [],
      "customProperties": {},
      "profileSpaceWorkflows": []
    },
    "createdTime": 1583809602614,
    "modifiedTime": 1600154984635
  },
  "eventTime": 1600154984640,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Profile.Deleted Webhook




  Copy Code



{
    "id": "5fc884059d9a9d1c370c3d0c",
    "type": "profile.deleted",
    "payload": "5e4d1c127ed020773da90ebc",
    "eventTime": 1606976517107,
    "subscriptionDetails": {
      "subscriptionId": "5f44bc2e2d94082a44ed7cae"
    }
  }






### Profile.Merged Webhook




  Copy Code



{
  "id": "5f68af04f8f1f2407d205506",
  "type": "profiles.merged",
  "payload": {
    "retainedProfileId": "5f55cfbd867ce40207fa151e",
    "deletedProfileIds": [
      "5e95a74962635048488da69e"
    ]
  },
  "eventTime": 1600696068302,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Response Definition


















































































































































































































































| Parameter | Sub Parameter | Description | Type |  |
| --- | --- | --- | --- | --- |
| id |  | Unique identifier of the unified profile. | String |  |
| contact |  | Contact information of the profile. |  |  |
|  | firstName | First name of the profile. | String |  |
|  | maidenName | Maiden name of the profile. | String |  |
|  | lastName | Last Name of the profile. | String |  |
|  | fullName | Full name of the profile. | String |  |
|  | email | Email id of the profile. | String |  |
|  | phoneNo | Phone number of the profile. | String |  |
|  | address | Address of the profile.Schema for Address Table given below. | String |  |
|  | website | List of websites for the profile. | String |  |
| demographics |  | Demographic Information of the client. |  |  |
|  | age | Age of the profile. | Integer |  |
|  | location | Location of the profile. | String |  |
|  | gender | Gender of the profile. | String |  |
|  | language | Language of the profile. | String |  |
| profiles |  |  | List of social identities linked to the profile. |  |
|  | name | Name of the person. | String |  |
|  | channelType | Channel type of the profile. e.g. facebook. | String |  |
|  | channelId | Unique id of the profile on channel. | String |  |
|  | permalink | Link of the profile on social channel. | String |  |
|  | avatarUrl | Profile image link. | String |  |
|  | bio | Detailed description about the user. | String |  |
|  | followers | Followers count of the user. | Integer |  |
|  | username | Unique identifier of the user. | String |  |
|  | verified | True if the user is verified by the channel. 					default: false | Boolean |  |
|  | unSubscribed | True if the user is subscribed for email and other activities.default: false | Boolean |  |
|  | deleted | True if profile is deleted natively.default: false | Boolean |  |
|  | snCreatedTime | Social Channel created time. | Integer |  |
|  | snModifiedTime | Social Channel modified time. | Integer |  |
|  | accountSpecificInfos | Account Specific Info like accountId, externalId, etc.Account Specific Info Table given below. |  |  |
| profileWorkflow |  |  |  |  |
|  | profileLists | Partner profile lists on the profile, if any. | Integer |  |
|  | customFields | Partner custom properties on the profile, if any. | String |  |
|  | profileSpaceWorkflows | List of client level workflows on the profile, if any.ProfileSpaceWorkflow Table given below. |  |  |
| createdTime |  | Created time of the profile in sprinklr. | Integer |  |
| modifiedTime |  | Last modified time of the profile in sprinklr. | Integer |  |


 


### Address Parameter Description Table










































| Parameter | Description | Type |
| --- | --- | --- |
| street1 | First line of the user's address. | String |
| street2 | Second line of the user's address. | String |
| city | The city of the user's address to help identify the location. | String |
| state | The state of the user's address. | String |
| country | The country of the user's address. | String |
| postalCode | ZIP Code of the address. | String |


### Account Specific Info Parameter Description Table























































| Parameter | Description | Type |
| --- | --- | --- |
| accountId | Account id of the profile. | Integer |
| externalId | External id of the profile. | String |
| lastBrandEngagedTime | Last brand engagement time. | Integer |
| lastFanEngagedTime | Last fan engagement time. | Integer |
| optIn | If True, optin.default: false | Boolean |
| fanSubscriptionState | Subscription state of fan. | String |
| activeUser | If True, user id active.default: false | Boolean |
| invited | If True, invited.default: false | Boolean |


 


### Profile Space Workflow Parameter Description Table
























































| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| spaceId |  | Client Id. | String |  |
| modifiedTime |  | Last modified time of the space workflow | Integer |  |
| customFields |  | Client custom properties on the asset, if any. | String |  |
| queues |  | Client queue details of the message, if any. | Integer |  |
|  | queueId | Queue identifier to add the message to queue. | Integer |  |
|  | assignmentTime | Assignment time of the queue to the message. | Integer |  |
| profileLists |  | Client profile lists on the profile, if any. | Integer |  |

[](https://dev.sprinklr.com/profile-webhooks)

[Back to top](https://dev.sprinklr.com/profile-webhooks)
