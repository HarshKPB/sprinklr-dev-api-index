---
title: "Source Agnostic Message"
slug: source-agnostic-message
url: https://dev.sprinklr.com/source-agnostic-message
---

# Source Agnostic Message

# Source Agnostic Message

Source agnostic APIs allow importing messages from any third-party source within Sprinklr and creating a corresponding profile for the sender. This message can be associated to an existing or a new case based on the conversation Id passed in the API request.

**Dev Notes: **For setting up Source Agnostic Account in your Sprinklr environment, contact your Success Manager for enabling `source.agnostic.channel.enabled.partnerid` Dynamic Property (DP).

To Add a Source Agnostic Account, please navigate to [Accounts](https://www.sprinklr.com/help/articles/account/get-familiar-with-actions-you-can-perform-on-accounts-account-groups/6467ccf830f12540268fb93c) section.

Using Source Agnostic APIs, you can:

- Import third-party messages to Sprinklr. Once the message is received on Sprinklr's platform, a case will be created, which can be further assigned to the respective agent.

- Close the conversation for the given conversation Id.

## Source Agnostic APIs: Corner Cases

| Sr No | Message Id | Conversation Id | Sender id | Sender Name | Case Created | Profile Created |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Unique | Unique | Unique | Unique | New Case | New Profile |
| 2 | Unique | Same as 1 | Unique | Unique | Same Case as 1 | Same Profile as 1 |
| 3 | Unique | Unique | Same as 2 | Unique | New Case | Same Profile as 1 |
| 4 | Unique | Same as 3 | Unique | Same as 3 | Same Case as 3 | Same Profile as 1 |
| 5 | Same as 4 | Unique | Unique | Same as 4 | New Case | New Profile |
| 6 | Unique | Same as 5 | Same as 5 | Unique | Same Case as 5 | Same Profile as 5 |

[](https://dev.sprinklr.com/source-agnostic-message) 

 

 
[Back to top](https://dev.sprinklr.com/source-agnostic-message)
