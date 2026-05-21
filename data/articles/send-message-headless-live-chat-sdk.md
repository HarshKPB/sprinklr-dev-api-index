---
title: "Send Message Headless Live Chat SDK"
slug: send-message-headless-live-chat-sdk
url: https://dev.sprinklr.com/send-message-headless-live-chat-sdk
---

# Send Message Headless Live Chat SDK

# Send Message


    The `sendMessage()` method is used to publish messages in Live Chat. It supports two main scenarios:




- **Send a message within an existing conversation:** Deliver text or media into an ongoing, open conversation.

- **Create a new conversation and send the first message:** Initialize a conversation and immediately post the opening message.



    Messages can originate from either the **end user** or the **system/bot**.




    In addition to plain text, this method supports **media attachments** such as images, videos, documents, and audio files.
    The SDK automatically handles file uploads, extending the basic `sendMessage()` functionality to enable rich content delivery alongside text messages.


## SDK Method

`sendMessage()`

## Examples

### Send Message



try {
  const message = await window.sprinklr.chat.sendMessage({
    id,
    conversationId,
    message: {
      text,
    },
    isSentByUser,
    messageContext,
  });
} catch (error) {
  // catch error
}



### Send Message with an Attachment



try {
  const result = await window.sprinklr.chat.sendMessage({
    id: 'msg-123',
    conversationId: '627b7d2cb1628c58860f962c',
    message: {
      text: 'Check out this image!',
      mediaAttachments: [
        {
          file: File,
          id: 'MEDIA_421a9f6f-a42e-4ba5-9627-c7af17050716',
          title: 'Screenshot 2025-06-06 at 13.20.02.png',
          type: 'IMAGE',
        },
      ],
    },
  });
  console.log('Message sent:', result);
} catch (error) {
  console.error("Failed to send message:", error);
}



### Handle File Input Dynamically



// Example: Handle file input and create media attachments
const fileInput = document.querySelector('input[type="file"]');
fileInput.addEventListener('change', async (event) => {
  const files = Array.from(event.target.files);
  const mediaAttachments = files.map((file) => {
    // Determine attachment type based on file type
    if (file.type.startsWith('image/')) {
      return {
        file: file,
        id: `MEDIA_${Date.now()}_${Math.random()}`,
        title: file.name,
        type: 'IMAGE',
      };
    } else if (file.type.startsWith('video/')) {
      return {
        file: file,
        id: `MEDIA_${Date.now()}_${Math.random()}`,
        title: file.name,
        type: 'VIDEO',
      };
    } else if (file.type.startsWith('audio/')) {
      return {
        file: file,
        id: `MEDIA_${Date.now()}_${Math.random()}`,
        title: file.name,
        type: 'AUDIO',
        mimeType: file.type,
      };
    } else {
      // Document type
      const documentTypeMap = {
        'application/pdf': 'PDF',
        'application/vnd.ms-excel': 'EXCEL',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'EXCEL',
        'application/vnd.ms-powerpoint': 'PRESENTATION',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'PRESENTATION',
      };
      return {
        file: file,
        id: `MEDIA_${Date.now()}_${Math.random()}`,
        title: file.name,
        type: 'DOCUMENT',
        documentType: documentTypeMap[file.type] || 'DOCUMENT',
      };
    }
  });
  // Send message with attachments
  try {
    const result = await window.sprinklr.chat.sendMessage({
      id: `msg-${Date.now()}`,
      conversationId: 'your-conversation-id',
      message: {
        text: 'Here are the files',
        mediaAttachments: mediaAttachments,
      },
    });
    console.log('Message sent:', result);
  } catch (error) {
    console.error("Failed to send message:", error);
  }
});



## Parameters














****






****
****






****






****
****

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | A unique identifier sent and received back upon publish success or failure of this event. Example: "61264609aeb0544d614" | string |
| conversationId | Optional | The conversation ID to publish the message in. If omitted, the latest active/open conversation is used. Example: "6126460410867e4d6f54".Default: latest active/open conversation | string |
| message | Required | The message content. Example: { text: "Sample message" } | { text: string } |
| isSentByUser | Optional | Indicates if the message is sent by the user or the brand. Supported Values: true or false Default Value: false | boolean |
| messageContext | Optional | Map of custom field IDs and their values to update on the conversation. Example: {}. Default: {} | StringTMap<string[]> |
| mediaAttachments | Optional | Array of media files (images, videos, audio, documents) attached to the message. Example: see MediaAttachment table below | MediaAttachment[] |

### Media Attachment Object Table














``````


































| Field | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| file | Required | The actual file object selected from input or blob. To upload files, you must provide the file property in each mediaAttachment. The file can be a Blob or File object. The url property is optional and can be a blob URL created from the file. | File |
| id | Required | Unique identifier for the attachment. Example: "MEDIA_421a9f6f-a42e-4ba5-9627-c7af17050716" | string |
| title | Optional | Display name or file name of the attachment. Example: "Screenshot.png" | string |
| type | Required | Type of media file. Example: "IMAGE". Allowed values: "IMAGE" \| "VIDEO" \| "AUDIO" \| "DOCUMENT" | string |
| mimeType | Optional (for audio) | MIME type of the audio file. Example: "audio/mpeg" | string |
| documentType | Optional (for documents) | Subtype of document (e.g., PDF, Excel, Presentation). Example: "PDF" | string |


**Dev Notes:**



- The maximum number of attachments per message is controlled by `maxAttachmentCount` in the Live Chat app configuration. By default, this is set to 1.

- All uploaded files must comply with the maximum content length defined in the Live Chat app configuration. Files exceeding this limit will be rejected.


### Supported File Types


























| Category | Supported Formats |
| --- | --- |
| Images | JPEG, PNG, GIF, WebP, and other common image formats |
| Videos | MP4, WebM, and other common video formats |
| Documents | PDF, Excel, PowerPoint, Word documents |
| Audio | MP3, AMR, WAV, AIFF, AAC |

## Response Format

The resolved message object will look like this:



{
  externalId: string; // The message ID provided in the request
  message: {
    id: string;
    conversationId: string;
    creationTime: number;
    deleted?: boolean;
    sender: string;
    additionalContext?: Record;
    messagePayload?: {
      text?: string;
      textEntities?: TextEntity[];
      quickReplies?: QuickReplies;
      events?: MessageEvent[];
      richText?: boolean;
      markdownText?: boolean;
      mediaAttachments?: MediaAttachment[]; // Updated with file tokens after upload
    };
  };
}



## Response Parameters






































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| externalId |  | The message ID provided in the request. Example: "msg-123" | string |
| id |  | Unique ID for the message. Example: "61264609aeb0544d614" | string |
| conversationId |  | ID of the conversation this message belongs to. Example: "6126460410867e4d6f54" | string |
| creationTime |  | Epoch timestamp (ms) when the message was created. Example: 1712928000000 | number |
| deleted |  | Flag indicating if the message was deleted. Example: true or false | boolean |
| sender |  | User ID or system ID of the message sender. Example: "user-456" | string |
| additionalContext |  | Extra metadata related to the message. Example: { "tags": ["priority", "internal"] } | Record<string, string[]> |
| messagePayload |  | Detailed content of the message. Contains sub‑parameters listed below. | chatMessage |
|  | text | Plain text content of the message. Example: "Hello world" | string |
|  | textEntities | Structured text entities for formatting or metadata. Example: [ { type: "mention", value: "@user" } ] | TextEntity[] |
|  | quickReplies | Quick reply options for interactive messages. Example: { options: ["Yes", "No"] } | QuickReplies |
|  | events | Message events such as delivery or read receipts. Example: [ { type: "DELIVERED" } ] | MessageEvent[] |
|  | richText | Flag indicating if the message uses rich text formatting. Example: true | boolean |
|  | markdownText | Flag indicating if the message uses markdown formatting. Example: true | boolean |
|  | mediaAttachments | Array of media files attached to the message. Updated with file tokens after upload. Example: see MediaAttachment table | MediaAttachment[] |


  [](https://dev.sprinklr.com/send-message-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/send-message-headless-live-chat-sdk)
