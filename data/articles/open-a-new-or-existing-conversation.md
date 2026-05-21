---
title: "Open a New or Existing Conversation"
slug: open-a-new-or-existing-conversation
url: https://dev.sprinklr.com/open-a-new-or-existing-conversation
---

# Open a New or Existing Conversation

# Open a Conversation

When opening a conversation, the user will either open a new conversation or an existing conversation. See the relevant section for the applicable method:


- [Open a New Conversation](https://dev.sprinklr.com/open-a-new-or-existing-conversation#open-new-conversation)

- [Open an Existing Conversation](https://dev.sprinklr.com/open-a-new-or-existing-conversation#open-existing-conversation)

## Open a New Conversation

This method starts a new conversation on behalf of the user. The conversation starts with the welcome messages configured in the Live Chat builder.

**Dev Notes:** A new conversation is only started if the limit defined in the Live Chat builder is not reached. For example, if in the Live Chat builder, you have selected the "Allow only one conversation per user" option, then more than one conversation cannot be started by a customer.

### Method

`sprChat('openNewConversation');`

### Parameters







| Parameter | Type | Required/Optional | Description | Possible value | Default value |
| --- | --- | --- | --- | --- | --- |
| initialMessages | Array<{ isSentByUser?: boolean; message: string \| Partial } \| string> | Optional | Defines the initial messages between the chatbot agent and the customer.  The initial messages override the default welcome messages by the supplied array. | Refer to the following Initial Messages table for the possible values. | None |
| autoInitiateConversation | Boolean | Optional | Defines whether a conversation is automatically initiated between the chatbot and customer. | If true, it creates a case within Sprinklr even when there is no associated user message. | None |
| conversationContext | StringTMap<string[]> | Optional | Specify conversation context/custom fields with new conversation. |  | None |

### Initial messages

The following table describes the `initialMessages` array parameter:







| Parameter | Type | Required/Optional | Description | Values |
| --- | --- | --- | --- | --- |
| message | String | Optional | The messages sent by the chatbot or the customer. | Any string such as “Hello, how can I help you?” |
| isSentbyUser | Boolean | Required | This is used to indicate that the message is a customer message. | true, false |

### Examples

**Example 1**: The following example starts a conversation with welcome messages that you configured in the Live Chat builder:




  Copy Code


sprChat('openNewConversation');





**Example 2**: The following example starts a conversation with one message from chatbot and one message from the customer:




  Copy Code


window.sprChat('openNewConversation', { initialMessages: [{ message: "Hello, How can I help you?" }, { message: 'Audio issue', isSentByUser: true }]
});





**Example 3**: The following example starts a conversation with `_c_abcdef123` custom field and its value `123`:




  Copy Code


window.sprChat('openNewConversation', {
 conversationContext: {
 '_c_abcdef123': ['123']
 }
});





**Example 4**: The following example starts a conversation with a video call:

**Dev Notes:** This applies only when initiating a new conversation with a video call.




  Copy Code


sprChat('openNewConversation', {
  additional: { actionType: 'VIDEO_CALL' },
  silent: true,
});





## Open an Existing Conversation

This method opens the latest active and open conversation of the customer. It opens the conversation that has not been closed or deleted and has the most recently published message.

You can also use it to open a particular conversation if you have the conversation ID captured by listening to some events that declare the ongoing conversation. Use this only if you want to open an active and existing conversation.

### Method

`sprChat('openExistingConversation');`

### Parameters







| Parameter | Type | Required/Optional | Description | Values |
| --- | --- | --- | --- | --- |
| conversationId | String | Optional | Sprinklr defined conversation ID | Latest active and open conversation |

### Examples

**Example 1**: The following example automatically opens the latest active and open conversation:




  Copy Code



window.sprChat('openExistingConversation');






**Example 2**: The following example opens the conversation with the `123` conversation ID:




  Copy Code


window.sprChat('openExistingConversation', '123');





[](https://dev.sprinklr.com/open-a-new-or-existing-conversation)

[Back to top](https://dev.sprinklr.com/open-a-new-or-existing-conversation)
