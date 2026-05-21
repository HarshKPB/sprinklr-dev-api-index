---
title: "Update Conversation Context Headless Live Chat SDK"
slug: update-conversation-context-headless-live-chat-sdk
url: https://dev.sprinklr.com/update-conversation-context-headless-live-chat-sdk
---

# Update Conversation Context Headless Live Chat SDK

# Update Conversation Context


The `updateConversationContext()` method dynamically updates the context metadata of a conversation. This method adds or modifies conversation-specific context data that can be used for filtering, categorization, and business logic.

## SDK Method

`updateConversationContext()`

## Example Usage




 Copy Code


try {
  const result = await window.sprinklr.chat.updateConversationContext({
    conversationId: '627b7d2cb1628c58860f962c',
    context: {
      'department': ['engineering'],
      'priority': ['high'],
      'category': ['technical-support'],
      'source': ['website']
    },
    filters: {
      filterType: 'NIN',
      field: 'closed',
      values: [true],
      id: '123'
    },
    includeDeleted: false
  });
  console.log('Updated conversation:', result.conversationId);
} catch (error) {
  console.error("Failed to update conversation context:", error);
}



## Parameters






















- ****
  -
- ****
  - ``
  - ``






      ``














| Parameter | Description | Type | Required/Optional | Example |
| --- | --- | --- | --- | --- |
| context | Context data as key-value pairs where values are arrays of strings | StringTMap<string[]> | Required | { "department": ["engineering"], "priority": ["high"] } |
| conversationId | Specific conversation ID to update. If not provided, updates the last active conversation (the conversation which is not closed or deleted)          With conversationId:            Updates the specific conversation's context           Without conversationId:            If includeDeleted is true: Updates the latest conversation (including deleted ones)       If includeDeleted is false: Updates the last active conversation based on filters | string | Optional | '627b7d2cb1628c58860f962c' |
| filters | Filter criteria to determine which conversation to update when conversationId is not provided | interface Filter {  filterType: string;  filters?: Filter[];  field: string;  values: Array<string \| number \| boolean>;  details?: {    timeToBusinessHours?: number;    noOfAgentsAvailable?: number;    dependentFilter?: Filter;    numSnoozes?: number;    numberOfPendingCases?: number;    callTypes?: Array<'AUDIO' \| 'VIDEO'>;    conversationId?: string;  } & StringAnyMap;  id: string \| number;} | Optional | { filterType: 'AND', field: 'status', values: ['open'], id: 'status-filter' } |
| includeDeleted | Whether to include deleted conversations when finding the target conversation | boolean | Optional | false |

### Context Object Structure


















| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| [key] | string[] | Required | Context key-value pairs where each key is a string and each value is an array of strings. |

## Response Format

The resolved object will look like this:




 Copy Code


{
  conversationId: string;
}



## Response Parameters
















| Parameter | Description | Type |
| --- | --- | --- |
| conversationId | Unique identifier for the conversation. | string |

  **Dev Notes: **


- **Initialization Required:** Always call `init()` before using `updateConversationContext()`. The method will throw `CHAT_NOT_INITIATED` error if called before initialization.

- **Context Sanitization:** The context data is automatically sanitized before being sent to the backend to ensure data integrity.

- **Context Merging:** New context data is merged with existing context rather than replacing it entirely.

- **Context Validation:** Context values must be arrays of strings. Non-string values will be converted or filtered out during sanitization.

- **Conversation Targeting:**


  - Provide `conversationId` for specific conversation updates

  - Omit `conversationId` to update the last active conversation

  - Use `filters` to target conversations based on specific criteria



## Error Types

**Dev Notes: **For robustness, always handle `UNEXPECTED_ERROR` as a catch-all in UI or telemetry.









      ``



      ``



      ``



      ``
      ``````



| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | Occurs when the requested conversation, message, or resource cannot be found. This typically happens when trying to access a conversation that has been deleted or when the conversation ID is invalid. |
| NOT_ACCEPTABLE | Occurs when the data format or content you're trying to send is invalid or cannot be processed. This includes malformed message content, invalid file types, or data that doesn't meet the system requirements. |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| CHAT_NOT_INITIATED | Occurs when chat SDK methods (sendMessage, createConversation, etc.) are called before init(). |


  [](https://dev.sprinklr.com/update-conversation-context-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/update-conversation-context-headless-live-chat-sdk)
