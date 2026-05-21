---
title: "Omnichannel Handover Protocol Blueprint"
slug: omnichannel-handover-protocol-blueprint
url: https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint
---

# Omnichannel Handover Protocol Blueprint

#
 Omnichannel Handover Protocol Blueprint

Omnichannel Handover Protocol allows integrating any third-party Bot with Sprinklr. Once integrated, the bot can converse with customers on desired Modern Messaging channels such as Twitter, Whatsapp, Sprinklr LiveChat, etc. This feature enables a brand to pass control between the integrated Bot and agents.

**Dev Notes: **The Bot or a Sprinklr Agent is permissible to participate in the conversation. To set a default participant of your choice, kindly reach out to your success manager.

## Things to Know in Advance

- Generate API Key using the steps mentioned in the [Getting Started](https://dev.sprinklr.com/getting-started) Guide

- Generate an Authentication Token using one of the methods listed in the [Authorize](https://dev.sprinklr.com/authorize) section

- Set up Webhook subscription using the [Create Subscription API](https://dev.sprinklr.com/create-subscription). For more information, refer to the [Create and Manage Webhook Subscription](https://www.sprinklr.com/help/articles/platform-modules/create-and-manage-webhook-subscription-in-sprinklr/633c5c2b59534970b26f96da) Knowledgebase article

- We recommend using an **asynchronous** webhook endpoint that sends `200 OK` within 10 seconds
(default setup for [webhook retries logic](https://dev.sprinklr.com/webhook-retries-logic)). This helps avoid unwanted congestion at either the sender's or receiver's end

**Dev Notes: **For [Facebook channel](https://www.sprinklr.com/help/articles/advanced-capabilities/enabling-handover-protocol-for-instagram-messages/63ee628df6e2cc7d18facbb3), we recommend using native Omnichannel Handover Protocol supported by Facebook.

## Why do we Need Omnichannel Handover Protocol?

- Customers reach out to the brand using different channels such as Instagram, Twitter, Facebook, etc. With omnichannel handover protocol, managing conversations from a centralized platform orchestrates seamless customer experience

- If the customer has a 3rd party bot already trained and deployed at their end, they can consider integrating it with Sprinklr. This eliminates the need to build a dedicated external bot in Sprinklr

- Once the bot is integrated, care agents in Sprinklr can have a centralized view of the bot conversations on the platform’s care console

- Moreover, the conversation statistics can be plotted on the reporting dashboard for further analysis

- Adding additional channel support becomes easy through Sprinklr

For a better understanding, let’s look at the conversation flow at the customer’s, bot’s, and agent’s end.

### Conversation Flow - Customer’s Perspective

- The customer initiates a conversation with the bot

- The bot triggers the first message based on the query

- If the customer wishes to escalate the case and talk to an agent, the conversation gets transferred to the agent

- The case can further get retransferred to the bot once the agent has addressed the query

### Conversation Flow - Bot Perspective

- The bot gets triggered based on the customer’s first message

- The bot receives channel-specific data such as the channel and message type

- Bot prepares the first reply based on AI logic and can also create channel-specific responses

- The first message is then shared by a bot using Sprinklr’s publishing message API

- If required or escalated, the Bot transfers the case using Thread Pass Control API to the care agent

### Conversation Flow - Agent’s Perspective

- Once the conversation is transferred to the agent, they can see the case assigned to them within the live request queue

- Agent reviews the conversation so far and replies to the customer without having them repeat the query

- Once the agent addresses the needs, they can either close the case or retransfer the conversation o the bot

## End-to-End Conversation Management Workflow


- [Message Received in Sprinklr](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#message_received)

- [Case Created](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_created)

- [2.1 Create Case in Sprinklr](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_created_sprinklr)

- [2.2 case.create Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#care_created_webhook)

- [Process Message and Send Reply](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#process_message_reply)

- [3.1 Read Message by Message Id API](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#read_message_id)

- [3.2 Publish Message API](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#publish_message)

- [3.3 message.published Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#publish_message_webhook)

- [New Messages Associated with the Case](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#new_message_case)

- [4.1 message.association.change Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#message_association_webhook)

- [4.2 Read message Content](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#read_message_content)

- [4.2.1 Read Message by Message Id](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#read_message_by_id)

- [Transfer Control - From Bot to Sprinklr](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#transfer_control)

- [5.1 Pass Control API](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#pass_control)

- [5.2 Thread Control Updated Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#thread_control)

- [Agent Assignment](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#agent_assignment)

- [6.1 Assignment Engine](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#assignment_engine)

- [6.2 case.update Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_update_webhook_new)

- [Agent Reply](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#agent_replies_customer)

- [7.1 Sprinklr Agent/Care Console](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#sprinklr_care_console)

- [7.2 Webhooks Triggered](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#webhooks_triggered)

- [7.2.1 message.association.change Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#message_association_change_webhook)

- [7.2.2 case.update Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_update_webhook_new)

- [Case Notes](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_notes)

- [8.1 Add Notes from Sprinklr](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#add_notes_from_sprinklr)

- [8.1.1 Case Macros](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_macros)

- [8.1.2 Message Details Tab](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#message_details_tab)

- [8.2 case.update Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_update_webhook)

- [Transfer Control - Sprinklr to Bot](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#pass_control_to_bot)

- [9.1 Release Control](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#release_control)

- [9.2 Thread Control Updated Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#thread_control_updated_webhook)

- [Case Closed](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#close_case)

- [10.1 Close Case via Bot](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#close_case_via_bot)

- [10.2 Close Case via Sprinklr](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#close_case_via_sprinklr)

- [10.2.1 Close Case Using Macros](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#close_case_using_macros)

- [10.3 case.update Webhook](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint#case_updated_webhook)

## Implementation Workflow

The entire end-to-end conversation worklfow between bot and customer and agent and customer is as follows:

## 1. Message Received

The customer sends the first message, which is received at Sprinklr’s end.

## 2. Case Created

Sprinklr listens to all the brand messages sent on the bot and creates a case using Sprinklr’s case maker.

### 2.1 Case Created in Sprinklr

Automation: Sprinklr’s Case Maker rule aims to simplify new case creation or association with an existing case for channels like voice, social, or email. The [Case Creation rules](https://www.sprinklr.com/help/articles/types-of-rules/case-update-and-case-creation-rules/63f1c7a5e024591337249c7b) are configured in the Rule Engine within the platform UI.

**Related Knowledgebase Article**: [About Case Maker](https://www.sprinklr.com/help/articles/case-maker/case-maker/6404bc887a695d65a1606599)

### 2.2 case.created webhook

Once the case is created in Sprinklr, case.created webhook gets triggered.

**Related Dev Portal Documentation**: [case.create Webhook Response](https://dev.sprinklr.com/case-webhooks)

## 3. Process Message and Send Reply

Once the case.create webhook notifies the case details, the bot processes the message at its end.

### 3.1 Read Message by Message Id

Using this API, the bot can fetch the message’s content from the messageId received in the case.create webhook response. Refer to the firstMessageId in the case.create webhook response and pass it as a query parameter in the Read Message by Id API request.

**Related Dev Portal Documentation**: Read Message by Id API

### 3.2 Publish Message API

Once the bot has the message details using the read message by Id API, a reply can be sent to the customer using publish message API.

**Related Dev Portal Documentation**: Publish Message API

### 3.3 message.published Webhook

If the message is successfully published on the native channel, message.published webhook gets triggered. This validates that the message has been sent successfully and also helps maintain publish message inline.


**Related Dev Portal Documentation**: [message.published Webhook Response](https://dev.sprinklr.com/message-webhooks)

**Dev Notes:**Publish Message API is asynchronous, i.e., the client and the server maintain bidirectional communication even when the server doesn’t respond immediately. Therefore, publish message API uses the message.published webhook to notify the user when the resource is ready.

## 4. New Messages Associated with Case

Every time a new message gets associated with the case, message.association change webhook gets triggered. The associatedMessageIds from the webhook response can be passed through read by Message Id API to grab the message content. This loop continues until there is an active conversation between the bot and the customer.

### 4.1 message.association.change Webhook

Whenever a new message is associated with the case (sent by a customer or bot), message.association.change webhook gets triggered. This notifies of any new messages that are appended to the case.

**Related Dev Portal Documentation**: [message.association.change Webhook Response](https://dev.sprinklr.com/case-webhooks)

### 4.2 Read Message Content

Once a new message is associated with the case, the bot can read its content and reply to the customer.

#### 4.2.1 Read Message by Message Id

Using this API, you can fetch the message’s content from the messageId received in the case.create webhook.


**Related Dev Portal Documentation**: Read Message by Id API

**Dev Notes:** Make the API call listed under 3.2 to reply to the customer.

## 5. Transfer Control - From Bot to Sprinklr

If the customer is unsatisfied with the bot response, they can request live agent support. This can be achieved using pass control API.

### 5.1 Pass Control

The bot can transfer the conversation control to Sprinklr using pass control API.

**Related Dev Portal Documentation**: Pass Control API

### 5.2 Thread Control Updated Webhook

The thread control updated webhook sends real-time updates every time the conversation control has been passed between the bot and the agent. The details of the previous and the current participant are sent in the webhook response.

**Related Dev Portal Documentation**: [Thread.control.updated Webhook Response](https://dev.sprinklr.com/thread-control-webhook)

## 6. Agent Assignment

Once the control is passed to Sprinklr, the case gets assigned to the agent.

### 6.1 Assignment Engine

The Assignment Engine makes assigning cases to all the agents through the work queue easier. Now all agents can have a distributed workload and work more efficiently and effectively.

**Related Knowledgebase Article**: [About Assignment Engine](https://www.sprinklr.com/help/articles/introduction-to-assignment-engine/what-is-the-assignment-engine/645b725e0104980882a5a6f0)

### 6.2 case.update Webhook

When a case is assigned to an agent using the assignment engine, the case.update Webhook gets triggered. You can find the assignee details, such as the assigneeType and assigneeId from the webhook’s response.

## 7. Agent Replies to Customer

Agents can reply to customer messages directly from Sprinklr’s agent/care console.

### 7.1 Sprinklr Agent/Care Console

Agent Console provides an innovative and efficient way for brands to resolve customer issues over social media and messaging platforms.

Agent Console provides a comprehensive view of messages and cases, with full conversation history and details available in a single view. This console allows teams to maintain inbound volume while streamlining message processing workflows. Agents can respond to a message from the Agent Console.

**Related Knowledgebase Article**: [Respond to Messages from Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/introduction-to-agent-consolelegacy/63d7747d468ae80d393476d0)

### 7.2 Webhooks Triggered

The following webhooks are triggered once the agent sends a reply to the customer:

#### 7.2.1 message.association.change Webhook

Whenever a new message is associated with the case, message.association.change webhook gets triggered. This notifies of any new messages that are appended to the case.

**Related Dev Portal Documentation**: [message.association.change Webhook Response](https://dev.sprinklr.com/case-webhooks)

#### 7.2.2 case.update Webhook

When a response is sent to the customer, the agent updates case-related custom properties. This event triggers the case.updated Webhook.

**Related Dev Portal Documentation**: [Case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

## 8. Case Notes

The agent can add notes to the Sprinklr case while they still have conversation control.

### 8.1 Add Notes from Sprinklr

An agent can add notes using case macros or directly from the message details tab.

#### 8.1.1 Case Macros

Macros are used to execute multiple actions on an entity with a single click. Agents often need to perform a series of actions repeatedly in their daily workflow, which can be easily accomplished using case macros. You can use add comment case macro to add a comment on the case.

**Related Knowledgebase Article**: [Case Macros](https://www.sprinklr.com/help/articles/macros-kb/case-macros/63370e48a0522e093b06b442)

#### 8.1.2 Message Details Tab

The Message Details Pane provides a snapshot overview of the Message and allows you to perform Quick Actions by clicking the appropriate action located at the top of the pane. Actions will be available based on the type and state of the Message.


**Related Knowledgebase Article:**[About the Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/introduction-to-agent-consolelegacy/63d7747d468ae80d393476d0)

### 8.2 case.update Webhook

Whenever an agent updates any case level custom property upon adding comment/s, the case.update Webhook gets triggered.

**Related Dev portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

## 9. Pass Control - Sprinklr to Bot

Once the agent has handled the case, they can close it from their end and trigger a survey or pass the control back to the Bot.

**Dev Notes:**The agent can choose to close the case using the steps listed under 10.2

### 9.1 Release Control

The agent can pass the control back to the primary controller, i.e., the Bot, using release control API.


**Related Dev Portal Documentation**: Release Control API

### 9.2 Thread Control Updated Webhook

The thread control updated webhook sends real-time updates every time the conversation control has been passed between the bot and the agent. The details of the previous and the current participant are sent in the webhook response.

**Related Dev Portal Documentation**: Thread.control.updated Webhook Response

## 10. Close Case

Once the customer query is resolved, the case can be closed either by the bot or by the agent when they still have the conversation control.

### 10.1. Close Case via Bot

The bot can close the case at their end and trigger the survey (if any).

### 10.2 Close Case via Sprinklr

If the agent still has control over the conversation, they can choose to close the case from Sprinklr.

#### 10.2.1 Close Case Using Macros

The case can also be closed using the case macros “status” action from Sprinklr. Case status is a case-level custom field that can be updated to closed or any other case status that reflects case closure.

**Related Knowledgebase Article**: [Case Macros](https://www.sprinklr.com/help/articles/macros-kb/case-macros/63370e48a0522e093b06b442)

### 10.3 case.update Webhook

Case.update Webhook notifies the bot that the case status is updated and closed.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks)

## FAQs Related to Omnichannel Handover Protocol

### 1. What is Required to Successfully Setup OHP?

- Webhook subscriptions - `case.create`, `message association change`, `thread control updated`, `message.published`, `case.update`

- Channel Account Setup on Sprinklr

- Enable “CASE_ASSIGN_PRIMARY_PARTICIPANT_FOR_ACCOUNTS” DP (internal). This DP ensures that all the incoming messages will be directly sent to the bot

- Setup a participant Id for the bot. The third-party bot vendor needs to provide a `callback URL`, `bot image`, `authorization token`, and a `unique bot name` to Sprinklr to generate this participant Id

- The newly generated bot participant Id will be set to primary. This ensures that the bot can reply to all incoming messages and pass control to agents when required

### 2. How Many Participant Ids can be Configured for an Account?

- Participant Id is added at the account level and is created using the user’s Authorization token

- For one user, only one participant id gets created for the given account

### 3. Can You Publish Dynamic Templates as Replies?

You can publish dynamic templates based on channel types using publish template APIs. The supported channels and respective templates are provided below:

- Sprinklr Live Chat Templates

- Whatsapp Dynamic Templates

- Instagram Dynamic Templates

- Facebook Dynamic Templates

- Twitter Dynamic Templates

- Apple Business Chat Templates

### 4. Are There any Additional APIs Used in Thread Control Flow?

You can additionally use the following two APIs:

- **Check Control**: Using this API, you can check the primary participant of the conversation at any given time.

- **Acquire Control**: Using this API, you can acquire control of the conversation from the primary participant.

#### Appendix

**Knowledgebase Article**: [Omnichannel Handover Protocol](https://www.sprinklr.com/help/articles/api/omnichannel-handover-protocol/64832193723d925979db8cd4)
 [](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint)




[Back to top](https://dev.sprinklr.com/omnichannel-handover-protocol-blueprint)
