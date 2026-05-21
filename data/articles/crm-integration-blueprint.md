---
title: "CRM Integration Blueprint"
slug: crm-integration-blueprint
url: https://dev.sprinklr.com/crm-integration-blueprint
---

# CRM Integration Blueprint

#
 CRM Integration Blueprint

Offering an orchestrated and seamless customer support experience is a top priority for businesses today. With Sprinklr’s bi-directional integration capabilities, you can manage cases and customer-agent interactions, natively from within your desired CRM system.
This article walks you through the complete case management workflow between Sprinklr and an external CRM system.

Sprinklr supports 35+ social and messaging channels and millions of listening sources from where new messages are ingested. Once the message is received on Sprinklr’s end, a case management workflow is initiated, which allows businesses to handle the end-to-end flow from their CRM system.

## Use Cases

- Create customer support cases within the CRM system from messages received on digital channels

- Respond and engage with your customers on digital channels natively from the CRM system

- 360-degree view of the case interactions from the CRM platform

- Real-time Bidirectional sync of Metadata from Sprinklr to the CRM system using webhooks and APIs

- Ability to triage and collaborate on cases using comment(notes) APIs and webhooks

## Things to Know in Advance



- Generate API Key using the steps mentioned in the [Getting Started Guide](https://dev.sprinklr.com/getting-started)

- Generate an Authentication Token using one of the methods listed in the [Authorize](https://dev.sprinklr.com/authorize) section

- Set up Webhook subscription using the steps mentioned in [Create and Manage Webhook Subscription](https://www.sprinklr.com/help/articles/platform-modules/create-and-manage-webhook-subscription-in-sprinklr/633c5c2b59534970b26f96da) Knowledgebase article

## End-to-End Case Management Workflow


- **Message Received in Sprinklr**

      The system receives an inbound message and begins processing it.


- **Case Creation**


  - **2.1 Create Case in Sprinklr**

          A new case is created in Sprinklr using predefined configurations.


  - **2.2 case.create Webhook**

          The webhook triggers and sends case creation details to the integrated CRM.


  - **2.3 Case Created in CRM**

          The CRM system receives the webhook payload and creates a corresponding case.


  - **2.4 Channel Case Details API**

          Sprinklr sends the complete case data through the API for further processing or enrichment.




- **Case Assignment**


  - **3.1 Case Assignment from Sprinklr**

          Sprinklr assigns the case to an agent or team based on configured rules.


  - **3.2 Case Assignment from CRM**

          The CRM can reassign or update case ownership.


  - **3.3 case.update Webhook**

          The webhook communicates any updates back to Sprinklr.


  - **3.4 Case Update API**

          This API ensures both systems reflect the latest assignment information.




- **Reply to Message on Case**


  - **4.1 Reply from Sprinklr**

          Agents reply through the Sprinklr interface.


    - **4.1.1 Sprinklr Agent/Care Console**

              Agents compose and send replies from the Agent or Care Console.




  - **4.2 Reply from CRM**

          CRM users can also reply to the customer.


    - **4.2.1 Read Message by Message ID API**

              Retrieves the original message for context.


    - **4.2.2 Publish Message API**

              Sends the response back to the customer.




  - **4.3 Webhooks Triggered**


    - **4.3.1 message.published Webhook**

              Notifies the systems when a message is published.


    - **4.3.2 case.update Webhook**

              Updates case information based on message activity.






- **New Messages Associated with the Case**


  - **5.1 message.association.change Webhook**

          Triggers when a new message is linked to the case.


  - **5.2 Read Message Content**


    - **5.2.1 Read Message by Message ID**

              Retrieves individual messages for review.


    - **5.2.2 Bulk Read Message API (Optional)**

              Optionally fetches multiple messages in a single request.




  - **5.3 Message Properties Update API**

          Updates metadata such as message type or classification.




- **Case Updated**


  - **6.1 case.update Webhook**

          Captures changes to case status or fields.


  - **6.2 Case Update API**

          Syncs updates across systems to maintain consistency.




- **Case Notes**


  - **7.1 Add Notes from Sprinklr**

          Users can add internal notes to the case.


    - **7.1.1 Case Macros**

              Applies pre-defined macros that include notes.


    - **7.1.2 Message Details Tab**

              Users can add comments from the message tab.




  - **7.2 Comment API**

          Allows programmatic addition of comments.


  - **7.3 comment.create Webhook**

          Notifies the CRM when a comment is added.




- **Case Closed**


  - **8.1 Close Case Using Sprinklr**

          Agents can close the case directly in Sprinklr.


    - **8.1.1 Close Case Using Macros**

              Macros can automate the case closure process.




  - **8.2 Close Case Through CRM**

          CRM can also close the case, which updates Sprinklr.


    - **8.2.1 Case Update API**

              Sends the closure update from CRM to Sprinklr.




  - **8.3 Webhooks Triggered**


    - **8.3.1 case.update Webhook**

              Notifies Sprinklr about the closure and final updates.






## Case Management - The 8-Step Workflow

The end-to-end case management flow involves the following APIs and webhooks:

## 1. Message received in Sprinklr

Brands receive 10s of 1000s of messages per day. This could be people mentioning their brands or products, a news story that mentions a product, or even reviews or blog articles.

Once a message is received, case is created within Sprinklr using rule automation. The entire case management flow  is described below.

## 2. Case Creation

Sprinklr listens to all the brand messages and uses patented AI technology to add metadata to these messages in real-time. This metadata can then be used to filter out messages that are engageable. Furthermore, pre-configured rules decide and create a case if support is needed.

### 2.1 Case Creation in Sprinklr

Cases are created in Sprinklr using Sprinklr’s Case Maker rule, which aims to simplify new case creation or association with an existing case for channels like voice, social, or email. Case Creation rules are configured in the Rule Engine within the platform UI.

**Related Knowledgebase Article**: [About Case Maker](https://www.sprinklr.com/help/articles/case-maker/case-maker/6404bc887a695d65a1606599)

### 2.2 case.create Webhook

Once the case is created in Sprinklr, case.created webhook gets triggered. This webhook helps notify the CRM system that a new case has been created in Sprinklr.

**Related Dev Portal Documentation**: [case.create Webhook Response](https://dev.sprinklr.com/case-webhooks#caseCreate)

### 2.3 Case Created in CRM

Once the case.create webhook is triggered, the CRM agent can use the webhook response to create a Sprinklr case-equivalent (let’s call it a ticket) in the 3rd party platform.

### 2.4 Channel Case Details API

Using this API, the 3rd party platform can update the Sprinklr case with the 3rd party platform case Id for reference. The external case will have the channel case details. The case-level properties that are passed within the external case object will get updated on a Sprinklr case.

**Related Dev Portal Documentation**: [Channel Case Details API](https://dev.sprinklr.com/update-channel-case-details)

## 3. Case Assignment

When a case is created, it gets assigned to the next available agent depending on the routing configuration already set up in Sprinklr.

### 3.1 Case Assignment Using Sprinklr

**Assignment Engine:** Assignment Engine makes assigning cases to all the agents through the work queue easier. Now all agents can have a distributed workload and work more efficiently and effectively.

**Related Knowledgebase Article**: [About Assignment Engine](https://www.sprinklr.com/help/articles/introduction-to-assignment-engine/what-is-the-assignment-engine/645b725e0104980882a5a6f0)

### 3.2 Assign Case from CRM

**Case Update API**: You can assign a case to the agent using the `assignedTo` parameter available in the case update API request parameters. Pass `SYNC_SELECTED_PROPERTIES` as the updateAction when using this API.

**Related Dev Portal Documentation**: [Case Update API](https://dev.sprinklr.com/case-update)

### 3.3 case.update Webhook

When a case is assigned to an agent using the assignment engine or through case update API, the Case.Update Webhook gets triggered. You can find the assignee details such as the assigneeType and assigneeId from the webhook’s response.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks#caseUpdate)

### 3.4 Case Update API

The CRM system can update case details existing within Sprinklr using Case Update API. Once updated, the case details will reflect within Sprinklr.

**Related Dev Portal Documentation**: [Case Update API](https://dev.sprinklr.com/case-update)

## 4. Reply to Message on Case

The agent can reply to the customer directly from Sprinklr or through CRM. Both scenarios are discussed below:

### 4.1 Reply from Sprinklr

Agents can reply to customer messages directly from Sprinklr’s agent/care console.

#### 4.1.1 Sprinklr Agent/Care Console

Agent Console provides a smart and efficient way for brands to resolve customer issues over social media and messaging platforms.

Agent Console provides a comprehensive view of messages and cases, with full conversation history and details available in a single view. This console allows teams to maintain inbound volume while streamlining message processing workflows. Agents can respond to a message from the Agent Console.

**Related Knowledgebase Article**: [Respond to Messages from Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/sending-canned-responses-from-agent-console/63d8c508405d8861d65a9c81)

### 4.2 Reply from CRM

To reply to messages, agents can reply from CRM using the following APIs:

#### 4.2.1  Read Message by Message Id API

Using this API, you can fetch the message’s content from the messageId received in the case.create webhook response. Refer to the firstMessageId in the case.create webhook response and pass it as a query parameter in the Read Message by Id API request.

**Related Dev Portal Documentation**: [Read Message by Id](https://dev.sprinklr.com/read-message-by-id)

#### 4.2.2 Publish Message API

Once the agent has the message details, a reply is sent to the customer on the native platform using publish Message API.

**Dev Notes: **Publish Message API is asynchronous, i.e., the client and the server maintain bidirectional communication even when the server doesn’t respond immediately. Therefore, publish message API uses the message.published webhook to notify the user when the resource is ready.

**Related Dev Portal Documentation**: [Publish Message API](https://dev.sprinklr.com/publishing-message)

### 4.3 Webhooks Triggered

The webhooks that get triggered upon successfully publishing the agent reply, include:

#### 4.3.1 message.published Webhook

If the message is successfully published on the native channel, message.published webhook gets triggered. This validates that the message has been sent successfully and also helps maintain publish message inline.

**Related Dev Portal Documentation**: [message.published Webhook Response](https://dev.sprinklr.com/message-webhooks#MP)

#### 4.3.2 case.update Webhook

When a response is sent to the customer, case-related custom properties are updated. This update triggers the case.updated Webhook.

**Related Dev Portal Documentation**: [Case.update Webhook Response](https://dev.sprinklr.com/case-webhooks#caseUpdate)

## 5. New Messages Associated with the Case

Whenever a new message is associated with the case, the steps mentioned in Step 4 need to be repeated for publishing replies.

### 5.1 message.association.change Webhook

Whenever a new message is associated with the case (sent by a customer or agent), message.association.change webhook gets triggered. This notifies the CRM system that a new message has been appended to the case.

**Related Dev Portal Documentation**: [message.association.change Webhook Response](https://dev.sprinklr.com/case-webhooks#caseMAC)

### 5.2 Read message Content

Messages can be read using the following APIs:

#### 5.2.1 Read Message by Message Id

Using this API, you can fetch the message’s content from the messageId received in the case.create webhook. If message.create webhook is subscribed, you can ignore calling this API as the message’s content will be available within the webhook’s response itself.

**Related Dev Portal Documentation**: [Read Message by Id](https://dev.sprinklr.com/read-message-by-id)

#### 5.2.2 Bulk Read Message API (Optional)

Using this API, you can fetch the message content details for the given associated message Ids.

**Related Dev Portal Documentation**: [Read Message (Bulk)](https://dev.sprinklr.com/read-messages-bulk)

**Dev Notes: **Once you have the message's content, repeat the steps listed in 4.2.2 for publishing the message.

### 5.3 Message Properties Update API

Using this API, the CRM agent can update the message workflow custom properties (if required). Once the API call is made, the updated message properties will reflect Within Sprinklr.

**Related Dev Portal Documentation**: [Message Properties Update API](https://dev.sprinklr.com/update-message-properties)

## 6. Case Update

Whenever any of the case custom properties are updated by the agent, the respective case gets updated within Sprinklr.

**Related Knowledgebase Article**: [Case Creation and Update Rules](https://www.sprinklr.com/help/articles/types-of-rules/case-update-and-case-creation-rules/63f1c7a5e024591337249c7b)

### 6.1 case.update Webhook

Once the case is updated in Sprinklr, the corresponding changes are notified to the CRM using the case.update webhook.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks#caseUpdate)

### 6.2 Case Update API

Using case update API, the Sprinklr case can be updated from the CRM system.

**Related Dev Portal Documentation**: [Case Update API](https://dev.sprinklr.com/case-update)

## 7. Add Case Notes

Case Notes are used for internal collaboration between agents and systems. The agent can add notes to cases directly from Sprinklr or though CRM. Both the scenarios are mentioned below:

### 7.1 Add Notes from Sprinklr

An agent can add notes using case macros or directly from the message details tab.

#### 7.1.1 Case Macros

Macros are used to execute multiple actions on an entity with a single click. Agents often need to perform a series of actions repeatedly in their daily workflow, which can be easily accomplished using case macros. You can use add comment case macro to add a comment on the case.

**Related Knowledgebase Article**: [Case Macros](https://www.sprinklr.com/help/articles/macros-kb/case-macros/63370e48a0522e093b06b442)

#### 7.1.2 Message Details Tab

The Message Details Pane provides a snapshot overview of the Message and allows you to perform Quick Actions by clicking the appropriate action located at the top of the pane. Actions will be available based on the type and state of the Message.

**Related Knowledgebase Articles:**

- [Message Details Tab](https://www.sprinklr.com/help/articles/message-third-pane/message-third-pane/6400b59f7a695d65a1605d38)

- [About the Agent Console](https://www.sprinklr.com/help/articles/agent-console-legacy/introduction-to-agent-consolelegacy/63d7747d468ae80d393476d0)

### 7.2 Add Notes From CRM

If the CRM agent wants to add any comments (internal notes) to the case, they can accomplish it using Sprinklr’s comment APIs.

**Related Dev Portal Documentations:**

- [Add Comment](https://dev.sprinklr.com/add-comment)

#### 7.3 comment.create Webhook

Whenever a new comment is added at the case level within Sprinklr, the case.comment webhook notifies the comment details to CRM using this webhook.

**Related dev Portal Documentation**: [comment.create Webhook Response](https://dev.sprinklr.com/comment-webhooks#commentCreate)

## 8. Case Closed

Once the case is resolved, it can be closed from Sprinklr or through CRM. Both scenarios are described below:

### 8.1 Close Case Using Sprinklr

Cases can be closed from Sprinklr using case macros. Alternatively, the case gets auto-closed if there are no further conversations for a pre-configured time.

#### 8.1.1 Close Case Using Macros

The case can also be closed using case macros “status” action from Sprinklr. Case status is a case-level custom field that can be updated to closed or any other case status that reflects case closure.

Case closure time can also be pre-configured using a processing clock. This helps auto-close the case whenever the agent doesn’t hear back from the customer within a pre-defined time frame.

**Related Knowledgebase Article**: [Case Macros](https://www.sprinklr.com/help/articles/macros-kb/case-macros/63370e48a0522e093b06b442)

### 8.2 Close Case Through CRM

Cases can be closed through CRM using case update API. The API details are listed below:

#### 8.2.1 Case Update API

The CRM agent can also choose to close the close case or update any other case-related property using the case update API. The case update API allows closing a case by updating the `spr_uc_status` (available by default for all partners) custom field to “`Closed`”.



#### Sample Request Body Snippet




```

{
   "caseNumbers": [
21157
],
   "updateActions": [
       "SYNC_SELECTED_PROPERTIES"
   ],
   "syncedSelectedCustomProperties": {
           "spr_uc_status": "Closed"
       }
}
```

### 8.3 Webhooks Triggered

Webhooks triggered upon case closure include:

#### 8.3.1 case.update Webhook

Case.update Webhook notifies the CRM system that the case status has been updated and closed.

**Related Dev Portal Documentation**: [case.update Webhook Response](https://dev.sprinklr.com/case-webhooks#caseUpdate)

  [](https://dev.sprinklr.com/crm-integration-blueprint)




[Back to top](https://dev.sprinklr.com/crm-integration-blueprint)
