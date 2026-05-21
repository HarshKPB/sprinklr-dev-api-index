---
title: "IVR Deflection - Blueprint"
slug: ivr-deflection-blueprint
url: https://dev.sprinklr.com/ivr-deflection-blueprint
---

# IVR Deflection - Blueprint

# IVR Deflection - Blueprint


Handling high inbound calls can be challenging for call centre agents, which will likely hamper customer experience owing to the longer resolution times. Sprinklr’s Modern Care module has introduced the “IVR Deflection” feature to address this issue.

[IVR Deflection](https://www.sprinklr.com/help/articles/ivr-use-cases/deflection-to-other-channel/63d7c434468ae80d39347af2) allows customers to switch to preferred social and messaging accounts like live chat or Whatsapp to continue the conversation with a live support agent.

## What is IVR Deflection?

IVR Deflection is Sprinklr’s Modern Care feature that helps reduce the number of inbound calls in the call center by redirecting customers to continue conversations on modern channels such as Whatsapp and Live chat. This, in turn, helps reduce the customer’s waiting time and thus enhances customer experience.

## Prominent IVR Deflection Channels

The two most common channels for IVR deflection include - `Whatsapp` and `Livechat`.

### 1. Live Chat

To deflect the conversation to Sprinklr’s live chat, an SMS with a live chat link is sent to the customer (from the phone number they are calling from).

### 2. Whatsapp

To deflect the conversation to Whatsapp, a predefined template is sent to the Whatsapp number (linked with the phone number customer is calling from).

**Related Knowledgebase Article**: [Deflection to Whatsapp/Livechat](https://www.sprinklr.com/help/articles/advanced-use-cases/sprinklr-live-chat-deflection-to-smswhatsapp-business/63d73632468ae80d39347365)

## Benefits of IVR Deflection

- Reduces the resolution time

- Reduces call centre expenditures

- Improves customer agent work experience

- Offers orchestrated customer experience

- Provides omnichannel reporting

- Ability to manage conversations from Sprinklr’s unified platform

## Things to Know in Advance

- Generate API Key using the steps mentioned in the [Getting Started Guide](https://dev.sprinklr.com/getting-started)

- Generate an Authentication Token using one of the methods listed within the [Authorize section](https://dev.sprinklr.com/authorize)

- Set up Webhook subscription using the steps mentioned in [Create and Manage Webhook Subscription](https://www.sprinklr.com/help/articles/platform-modules/create-and-manage-webhook-subscription-in-sprinklr/633c5c2b59534970b26f96da) Knowledgebase article

1. Create Social Account

1.1 Create Account Within Sprinklr

2. Create Template

2.1 Asset Create API

2.2 Create Asset Using UI

3. IVR Deflection

3.1 Deflection API

3.2 Deflect Node

4. Create Case

4.1 Case Creation in Sprinklr

4.2 case.create Webhook

5. Case Assignment

5.1 Case Assignment Using Assignment Engine

5.2 case.update Webhook

6. Agent Replies to Customer

6.1 Sprinklr Agent/Care Console

6.2 Webhooks Triggered

6.2.1 message.association.change Webhook

6.2.2 case.update Webhook

7. Case Notes

7.1 Add Notes from Sprinklr

7.1.1 Case Macros

7.1.2 Message Details Tab

7.2 case.update Webhook

8. Close Case

8.1 Close Case via Sprinklr

8.2 case.update Webhook

## IVR Deflection - End-to-End Workflow

### 1. Create Social Account

You should have active and verified accounts on Whatsapp and SMS for implementing IVR deflection. You can add social and messaging accounts from Sprinklr’s UI.

### 1.1 Create Account Within Sprinklr

Adding and verifying SMS and Whatsapp accounts is imperative for implementing Live chat and Whatsapp deflection.

**Related Knowledgebase Article**:

[Add Account](https://www.sprinklr.com/help/articles/manage-accounts/add-an-account/63ef4a7fef1b447d6c631c60)

[Configure Live Chat Application](https://www.sprinklr.com/help/articles/create-live-chat-application/creating-a-live-chat-application/63bc490c3fece76798a38d99)

### 2. Create Template

A template must be created to initiate the chat with the customer on the chosen channel. This predefined template will be posted on Whatsapp/Livechat as soon as the customer selects the option in IVR.

You can create a template using API or from the Sprinklr platform.

### 2.1 Asset Create API

A template can be created using asset create API. Once created, this asset will be visible in `Modern Engagement` -> `Digital Asset Management` -> `Assets`.

**Related Dev Portal Documentation**: [Asset Create API](https://dev.sprinklr.com/asset-create-v1)

### 2.2 Create Asset Using UI

You can create templates using Sprinklr’s UI. Once created, the asset Id of the template can be used to send it to the customer using IVR Deflection API.

**Related Knowledgebase Article**:

[Create Omnichannel Chat Template](https://www.sprinklr.com/help/articles/image-editor/create-an-omni-chat-template/645566d70104980882a5498a)

[Add Simple Text Asset Template](https://www.sprinklr.com/help/articles/manage-assets/create-a-text-template/645566be0104980882a54989)

### 3. IVR Deflection

Deflection ensures the pre-defined template is sent to the customer on the desired modern channel. You can implement IVR Deflection using the following two methods:

### 3.1 Deflection API

Using Deflection API, you can deflect an IVR call to the customer’s desired channel for communication.

**Related Dev Portal Documentation**: Deflection API

### 3.2 Deflect Node

You can configure the deflections in the dialogue tree to redirect the user chat from one channel to another while the case will remain the same throughout the conversation.

**Related Knowledgebase Article**: [Create Deflection Dialogue Node](https://www.sprinklr.com/help/articles/nodes-in-a-dialogue-tree/deflect-node/63da632a3f309f1308e8c106)

### 4. Create Case

Once the customer responds on the live chat/Whatsapp channel, the message is received in Sprinklr, and a case gets created using automation.

### 4.1 Case Creation in Sprinklr

Sprinklr’s Case Maker rule aims to simplify and automate new case creation or association with an existing case for channels like voice, social, or email. [Case Creation rules](https://www.sprinklr.com/help/articles/types-of-rules/case-update-and-case-creation-rules/63f1c7a5e024591337249c7b) are configured in the Rule Engine within the platform UI.

**Related Knowledgebase Article**: [About Case Maker](https://www.sprinklr.com/help/articles/case-maker/case-maker/6404bc887a695d65a1606599)

### 4.2 case.create Webhook

Once the case is created in Sprinklr, case.created webhook gets triggered. This webhook helps notify the CRM system that a new case has been created in Sprinklr.

**Related Dev Portal Documentation**: [case.create Webhook Response](https://dev.sprinklr.com/case-webhooks)

###  5. Case Assignment

When a case is created, it gets assigned to the next available agent, depending on the routing configuration set up in Sprinklr.

### 5.1 Case Assignment Using Assignment Engine

Assignment Engine makes assigning cases to all the agents through the work queue easier. With this queue-based case assignment, agents have a distributed workload, which allows them to work more efficiently and effectively.

**Related Knowledgebase Article**: [About Assignment Engine](https://www.sprinklr.com/help/articles/introduction-to-assignment-engine/what-is-the-assignment-engine/645b725e0104980882a5a6f0)

### 5.2 case.update Webhook

When a case is assigned to an agent using the assignment engine or through case update API, the Case.Update Webhook gets triggered. You can find the assignee details, such as the assigneeType and assigneeId, from the webhook’s response.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

### 6. Agent Replies to Customer

Agents can reply to customer messages directly from Sprinklr’s agent/care console.

### 6.1 Sprinklr Agent/Care Console

Agent Console provides an innovative and efficient way for brands to resolve customer issues over social media and messaging platforms.

Agent Console provides a comprehensive view of messages and cases, with the entire conversation history and details available in a single view. This console allows teams to maintain inbound volume while streamlining message processing workflows. Agents can respond to a message from the Agent Console.

**Related Knowledgebase Article**: [Respond to Messages from Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/introduction-to-agent-consolelegacy/63d7747d468ae80d393476d0)

### 6.2 Webhooks Triggered

The following webhooks are triggered once the agent sends a reply to the customer:

### 6.2.1 message.association.change Webhook

Whenever a new message is associated with the case, message.association.change webhook gets triggered. This notifies the customer whenever a new message is appended to the case.

**Related Dev Portal Documentation**: [message.association.change Webhook](https://dev.sprinklr.com/case-webhooks)

### 6.2.2 case.update Webhook

If an agent updates case-related custom properties when a response is sent to the customer. This event triggers the case.update Webhook.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

### 7. Case Notes

The agent can add notes to the Sprinklr case for collaborating internally.

### 7.1 Add Notes from Sprinklr

An agent can add notes using case macros or directly from the message details tab.

### 7.1.1 Case Macros

Macros are used to execute multiple actions on an entity with a single click. Agents often need to perform a series of actions repeatedly in their daily workflow, which can be easily accomplished using case macros. You can use add comment case macro to add a comment on the case.

**Related knowledgebase Article**: [Case Macros](https://www.sprinklr.com/help/articles/macros-kb/case-macros/63370e48a0522e093b06b442)

### 7.1.2 Message Details Tab

The Message Details Pane provides a snapshot overview of the message and allows you to perform Quick Actions by clicking the appropriate action from the pane. Actions will be available based on the type and state of the Message.

**Related Knowledgebase Articles**:

[Message Details Tab](https://www.sprinklr.com/help/articles/message-third-pane/message-third-pane/6400b59f7a695d65a1605d38)

[About the Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/introduction-to-agent-consolelegacy/63d7747d468ae80d393476d0)

### 7.2 case.update Webhook

Whenever an agent updates any case level custom property upon adding comment/s, the case.update Webhook gets triggered.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

### 8. Close Case

Once the customer query is resolved, the case can be closed directly from within Sprinklr.

### 8.1 Close Case via Sprinklr

The case can be closed using the case macros “status” action from Sprinklr. Case status is a case-level custom field that can be updated to closed or any other case status that reflects case closure.

**Related knowledgebase Article**: [Case Macros](https://www.sprinklr.com/help/articles/macros-kb/case-macros/63370e48a0522e093b06b442)

### 8.2 case.update Webhook

Case.update Webhook notifies the bot that the case status is updated and closed.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

## FAQs - IVR Deflection

### 1. Are There any Other Use Cases for IVR Deflection API?

Publishing HSM templates for Whatsapp can also be achieved using Defelection API. You can create an [HSM template](https://www.sprinklr.com/help/articles/hsm-templates/create-an-hsm-template-for-whatsapp-business/63d6694a468ae80d39346ac5) on Sprinklr’s UI and post it to Whatsapp using Deflection API.

[](https://dev.sprinklr.com/ivr-deflection-blueprint)

[Back to top](https://dev.sprinklr.com/ivr-deflection-blueprint)
