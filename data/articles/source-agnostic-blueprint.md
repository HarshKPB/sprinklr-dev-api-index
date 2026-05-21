---
title: "Source Agnostic Blueprint"
slug: source-agnostic-blueprint
url: https://dev.sprinklr.com/source-agnostic-blueprint
---

# Source Agnostic Blueprint

# Source Agnostic Blueprint


Source-Agnostic is a Modern Care feature where users can import a third-party message to Sprinklr and link it to an existing or a new case. Once the message is successfully imported, agents can view the imported messages within the engagement dashboards/care console and take further actions.

Source-agnostic APIs cover the following use cases:

- Import third-party messages to Sprinklr and link them to existing or new cases

- Use the “Source Agnostic Message Created” webhook to receive message details when an agent replies

- Close a conversation associated with the case

**Dev Note: ** Kindly contact your success manager to enable a Source-Agnostic Account in your Sprinklr environment

Once the source agnostic is enabled for your environment, the first step would be to set up a source-agnostic account. The steps for this setup are listed below:


- Log in to your Sprinklr instance. Click the **New Page** (**+**) icon to open the Launchpad.

- Under **Platform Modules**, click **All Settings**.

- Under **Manage Workspace**, click the **Accounts** icon. You will be redirected to the Accounts home page

- Click **Add Account**, placed in the top right corner.

- Search and select “Source Agnostic”.

- Add a unique name for the Source Agnostic account and click **Save**.

- You will be redirected to the Account details update page, where you can configure permissions, channel type, organization, shareability, custom properties, etc.

- Click **Save** to complete the setup for your source agnostic account

## Things to Know in Advance

- Generate API Key using the steps mentioned in the [Getting Started Guide](https://dev.sprinklr.com/getting-started).

- Generate an Authentication Token using one of the methods listed in the [Authorize](https://dev.sprinklr.com/authorize) section.

- Set up Webhook subscription using the steps mentioned in [Create and Manage Webhook Subscription](https://www.sprinklr.com/help/articles/platform-modules/create-and-manage-webhook-subscription-in-sprinklr/633c5c2b59534970b26f96da) Knowledgebase article.

- The "`source.agnostic.channel.enabled.partnerid`" DP (internal) need to be enabled from the backend for adding support for setting up "Source Agnostic" account within Sprinklr.



## End-to-End Source Agnostic Workflow

1. Message Pushed to Sprinklr

2. Case Created

2.1 case.create Webhook

3. Case Assignment

3.1 Assignment Engine

3.2 Case Update Webhook

4. Configure Care Dashboard

5. Respond to Message

5.1 Send Reply from Care Console

5.2 Webhooks Triggered

5.2.1 case.update Webhook

5.2.2 Source Agnostic Message Created Webhook

6. Add Case Notes

6.1 Add Notes from Sprinklr

6.1.1 Case Macros

6.1.2 Message Details Tab

7. Case Closed

7.1 Close Case via API

7.2 case.update Webhook

8. Update Message Status

## 1. Message Pushed to Sprinklr

You can import a third-party message to Sprinklr using Source Agnostic - Send Message API. The new message can be linked to a new case or an existing source-agnostic conversation. This API can also link the case to a profile using the information passed in the senderProfile object.

You can send the following message types using this API:

- Text Message

- Image Attachment

- Video Attachment

- Document Attachment

- Audio Attachment

- Simple Base64

- Multimedia Attachment

**Steps to Extract Account Id from UI (to be passed as path parameter in Source Agnostic Send Message API) **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on Accounts Icon within "Manage Workspace" module
- Click on the three dots placed alongside the respective account name
- Click on "Details" option from the drop down menu
- Click on copy url icon on the top right corner from the window that appears
- Use any encoder-decoder tool and paste the copied URL
- The account id will be the part of the decoded URL, i.e., if you get `/ACCOUNT/100426226/OVERVIEW` in the decoded URL, your account id is 100426226.

## 2. Case Created

Sprinklr imports the message sent through API and creates a new case or tags the message to the existing case for the given conversation Id.

### 2.2 case.created webhook

Once the case is created in Sprinklr, case.created webhook gets triggered.

 **Related Dev Portal Documentation**: [case.create Webhook Response](https://dev.sprinklr.com/case-webhooks)

## 3. Case Assignment

Once the case is created in Sprinklr, the case gets assigned to the agent using the assignment engine

### 3.1 Assignment Engine

The Assignment Engine assigns cases to all the agents using work queues. With this assignment method, all agents can have a distributed workload and work more efficiently and effectively.

**Related Knowledgebase Article**: [About Assignment Engine](https://www.sprinklr.com/help/articles/introduction-to-assignment-engine/what-is-the-assignment-engine/645b725e0104980882a5a6f0)

### 3.2 case.update Webhook

When a case is assigned to an agent using the assignment engine, the case.update Webhook gets triggered. You can find the assignee details, such as the assigneeType and assigneeId from the webhook’s response.   **Related Dev Portal Documentation**: [Case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

### 4. Configure Source Agnostic Care Dashboard

To view the imported message within the care dashboard, follow the steps mentioned below:

- Click to add a new tab on the headers menu

- Hover and click on the Modern Care module

- From the menu of options, hover and click on “Engagement Dashboards”

- Click on “Create Dashboard” option placed in the top right corner

- Give your dashboard a unique name and click on save. You can optionally select a Folder where you want to store your dashboard and tag that dashboard.

- Click on the “New Column” option from within the dashboard

- Search and Select “Case Management” from the window that appears

- Under the type of column, click on the “Search” option

- Give a unique name to the column and other required information such as sorting, the brand responded status, due date, and custom properties (if any)

- In the case source field, select “Source Agnostic” and “Channel Agnostic” from the drop-down menu

- Click on Create Column button, placed in the bottom right corner of the screen

- You can now visualize all the messages imported using Source Agnostic - Send Message API

 **Related Knowledge Portal Documentation**: [Create Engagement Dashboard](https://www.sprinklr.com/help/articles/getting-started-with-social-engagement/actions-in-engagement-dashboards/6450f6ac516411445be3ff72#64bf2343-160b-4c62-bf26-0384e4e5e38f)

## 5. Agent Replies to Customer

### 5.1 Using Platform - Respond to Messages from Care Console

Agent Console provides an innovative and efficient way for brands to resolve customer issues over social media and messaging platforms.

Agent Console provides a comprehensive view of messages and cases, with full conversation history and details available in a single view. This console allows teams to maintain inbound volume while streamlining message processing workflows. Agents can respond to a message from the Agent Console.

**Related Knowledgebase Article**: [Respond to Messages from Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/introduction-to-agent-consolelegacy/63d7747d468ae80d393476d0)

### 5.2 Webhooks Triggered

The following webhooks are triggered once the agent sends a reply to the customer:

#### 5.2.1 Source Agnostic Message Created Webhook

Source Agnostic Message Created webhook is triggered every time an agent replies on a case.

 **Related Dev Portal Documentation**: [Source Agnostic Message Webhook](https://dev.sprinklr.com/source-agnostic-message-webhook)

#### 5.2.2 case.update Webhook

When a response is sent to the customer, the agent updates case-related custom properties. This event triggers the case.updated Webhook.

**Related Dev Portal Documentation**: [Case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

## 6. Case Notes

The agent can add notes to the Sprinklr case while they still have conversation control.

### 6.1 Add Notes from Sprinklr

An agent can add notes using case macros or directly from the message details tab.

#### 6.1.1 Case Macros

Macros are used to execute multiple actions on an entity with a single click. Agents often need to perform a series of actions repeatedly in their daily workflow, which can be easily accomplished using case macros. You can use add comment case macro to add a comment on the case.

**Related Knowledgebase Article**: [Case Macros](https://www.sprinklr.com/help/articles/macros-kb/case-macros/63370e48a0522e093b06b442)

#### 6.1.2 Message Details Tab

The Message Details Pane provides a snapshot overview of the Message and allows you to perform Quick Actions by clicking the appropriate action located at the top of the pane. Actions will be available based on the type and state of the Message.

**Related Knowledgebase Article:**

- [Message Details Tab](https://www.sprinklr.com/help/articles/case-third-pane/new-third-pane/63d68fb52c015d03d4e8020e)

- [About the Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/introduction-to-agent-consolelegacy/63d7747d468ae80d393476d0)

## 7. Close Conversation

For source-agnostic accounts, cases can be closed using close conversation API.

### 7.1 Using Close Conversation API

With Close conversation API, you can close an existing conversation within Sprinklr. Currently, you can close a conversation only using this API.    **Related Dev Portal Documentation**: Close Conversation

### 7.2 case.update Webhook

Whenever the conversation is closed using close conversation API, the case.update Webhook gets triggered.

**Related Dev portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

## 8. Update Message Status

With the Update Status API, you can update the message status or read receipts such as sent, delivered, read, failed. You can also specify the error messages in case of an error.


**Related Dev Portal Documentation**: [Update Status](https://dev.sprinklr.com/source-agnostic-update-status)

## FAQs

### 1. What are Best Practices for Using Source Agnostic APIs?

- messageId needs to be different for every message imported in Sprinklr

- Use a unique conversationId when importing the message for the first time. For every consecutive message associated with the same conversation, keep the conversation Id constant. Else, a new case will be created

- The account used for importing messages to Sprinklr must be a source-agnostic account type

- The Source Agnostic - Send Message API will create a new profile for the sender

- The sender and receiver profiles can be different (from what was previously used) when importing the message for an existing conversation

## Appendix: Related APIs







[Create and Manage Webhook Subscription](https://www.sprinklr.com/help/articles/platform-modules/create-and-manage-webhook-subscription-in-sprinklr/633c5c2b59534970b26f96da)

| API | Description |
| --- | --- |
| Fetch Account Details | Fetch details for the respective source agnostic account using the account id |
|  | Knowledgebase article that walks you through the process for creating webhooks in detail |
| Fetch All Engagement Dashboards | This API helps fetch all the existing engagement dashboards along with the columns and respective Ids |
| Fetch Engagement Dashboard | This API helps fetch the engagement dashboard details for the given dashboard name |

	[](https://dev.sprinklr.com/source-agnostic-blueprint)

[Back to top](https://dev.sprinklr.com/source-agnostic-blueprint)
