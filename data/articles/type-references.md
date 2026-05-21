---
title: "Type References"
slug: type-references
url: https://dev.sprinklr.com/type-references
---

# Type References

# Type References

You can send simple text message in Live Chat. Additionally, you can also attach images, videos, audios, and documents to the messages.

The following code snippet shows the format of the message that can be sent by the user:




  Copy Code



        Message: {
            text?: string;
            textEntities?: {
                indices: [number, number];
                url?: string;
                phoneNumber?: string;
            };
            attachment?: ImageAttachment | VideoAttachment | AudioAttachment | DocumentAttachment;
            quickReplies?: {
                quickReplies: [{
                    id: string;
                    type: 'TEXT';
                    title: string;
                    imageUrl?: string;
                    payload?: string;
                }, {
                    id: string;
                    type: 'PHONE_NUMBER';
                    payload?: string;
                }];
                disableManualResponse?: boolean;
            };
            disableManualResponse?: boolean;
        }
    ImageAttachment: {
        type: 'IMAGE';
        url: string;
        height: number;
        width: number;
    }

    VideoAttachment: {
        type: 'VIDEO';
        previewImageUrl?: string;
        url: string;
        height: number;
        width: number;
    }

    AudioAttachment: {
        type: 'AUDIO';
        mimeType: 'audio/mp3' | 'audio/amr' | 'audio/x-wav' | 'audio/x-aiff' | 'audio/aac';
        title: string;
        url: string;
    }

    DocumentAttachment: {
        type: 'DOCUMENT';
        documentType: 'DOCUMENT' | 'PDF' | 'EXCEL' | 'PRESENTATION';
        title: string;
        url: string;
    }





[](https://dev.sprinklr.com/type-references)

[Back to top](https://dev.sprinklr.com/type-references)
