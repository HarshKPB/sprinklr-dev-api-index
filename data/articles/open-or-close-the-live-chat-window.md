---
title: "Open or Close the Live Chat Window"
slug: open-or-close-the-live-chat-window
url: https://dev.sprinklr.com/open-or-close-the-live-chat-window
---

# Open or Close the Live Chat Window

# Open or Close the Live Chat Window

The Live Chat SDK includes methods for opening and closing the chat window:

- [Open Chat Window](https://dev.sprinklr.com/open-or-close-the-live-chat-window#open-the-chat-window)

- [Close Chat Window](https://dev.sprinklr.com/open-or-close-the-live-chat-window#close-the-chat-window)

## Open Chat Window

This method opens the chat window so that the customer can start a conversation or continue with an ongoing conversation. It shows the home page or the last page that the customer was on before minimizing the chat window. You can also configure this method to show a list of the knowledge base articles.

### Method

`sprChat(‘open’);`

### Example

**Example 1**: In the following example, the open method opens the chat window:




  Copy Code


window.sprChat('open');





**Example 2**: In the following example, the open method opens the chat window with a list of preconfigured knowledge base articles:

**Dev Notes: **To configure the knowledge base articles, see [Knowledge Base Widget in Sprinklr Live Chat](https://www.sprinklr.com/help/articles/self-service-in-live-chat/knowledge-base-widget-in-sprinklr-live-chat/641376fa2680c35a78bc4c5d).




  Copy Code



window.sprChat('open', {
 landingScreen: "KNOWLEDGE_BASE_LIST"
});





## Close Chat Window

This method closes the chat window on the web page the customer is currently on.

**Dev Notes: **This method will only close the chat window and not the chat trigger. If in Live Chat builder, you have configured the Chat Trigger setting to show the chat trigger icon, then the chat trigger will be visible.

### Method

`sprChat(‘close’);`

### Example




  Copy Code



window.sprChat('close');





[](https://dev.sprinklr.com/open-or-close-the-live-chat-window)

[Back to top](https://dev.sprinklr.com/open-or-close-the-live-chat-window)
