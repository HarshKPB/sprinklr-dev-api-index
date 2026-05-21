---
title: "Install Headless Live Chat SDK"
slug: install-headless-live-chat-sdk
url: https://dev.sprinklr.com/install-headless-live-chat-sdk
---

# Install Headless Live Chat SDK

# Install Headless Live Chat SDK

To install the headless Live Chat SDK, you need to inject a script into your web page. The embed script below exposes a method in the window. When this method is called, it loads the Live Chat SDK into the window. After the script has executed, this method can be accessed using `window.sprinklr.chat`.

## Prerequisites

Before you begin, create a Live Chat application in Sprinklr to get the app ID. For steps, see [Creating a Live Chat Application](https://www.sprinklr.com/help/articles/create-live-chat-application/creating-a-live-chat-application/63bc490c3fece76798a38d99).

## Embed Script

Embed this script into your web page. This code exposes the `window.sprinklr.chat.load` function that injects the SDK script.




 Copy Code


!function () {
  var r = window,
      e = document,
      n = "script";
  if (!r.sprinklr || !r.sprinklr.chat || !r.sprinklr.chat.load) {
    var t = new Promise(function (a, s) {
      r.sprinklr = r.sprinklr || {};
      var i = 0;
      r.sprinklr.chat = {
        load() {
          if (r.sprinklr.chat.loaded) {
            a();
          } else {
            var o = function ({ detail: r }) {
              r.error ? s(r.error) : a();
              e.removeEventListener("@spr/CHAT_LOADED", o);
            };
            e.addEventListener("@spr/CHAT_LOADED", o);
            var p = e.createElement(n);
            p.type = "text/javascript";
            p.async = true;
            p.src = "{CDN_HOST_URL}/sdk/{env}/{appId}";
            p.onerror = function (r) {
              e.removeEventListener("@spr/CHAT_LOADED", o);
              if (++i < 3) {
                l.parentNode.removeChild(p);
                setTimeout(window.sprinklr.chat.load, 250);
              } else {
                i = 0;
                s(r);
              }
            };
            var l = e.getElementsByTagName(n)[0];
            l.parentNode.insertBefore(p, l);
          }
          return t;
        }
      };
    });
  }
}();



## Parameters

In the above code snippet, fill in the following details:























| Parameter | Description |
| --- | --- |
| {CDN_HOST_URL} | The CDN host URL provided by Sprinklr. |
| {env} | The Sprinklr environment on which your Live Chat application is present. For example, prod3. |
| {appId} | Live Chat application ID. You can get this from the Sprinklr UI. See Steps to Retrieve the {appId} in Sprinklr given below. |

### Steps to Retrieve the {appId} from Sprinklr:


- Click the **New Page** (**+**) icon to open the **Launchpad**.

- Go to **Listen > Live Chat Care**.

- Find your **Live Chat application** in the list.

The **Application ID** column contains the value for `{appId}`.

## Command to Load the SDK

  The following injected command can be called dynamically to fetch the SDK bundle and inject the SDK into `window.parent.chat`.




 Copy Code


window.sprinklr.chat.load()
  .then(() => {
    // SDK loaded successfully
  })
  .catch((e) => {
    // SDK loading failed
    console.error('Failed to load SDK:', e);
  });



## Original Code and Explanation

Below is the complete code required to load the Live Chat SDK on your web page, along with an explanation of how it works.




 Copy Code


(function () {
  var _window = window;
  var _document = document;
  var _script = 'script';
  // Check if SDK is already loaded or has a load method
  if (
    !_window.sprinklr ||
    !_window.sprinklr.chat ||
    !_window.sprinklr.chat.load
  ) {
    var loadPromise = new Promise(function (resolve, reject) {
      _window.sprinklr = _window.sprinklr || {};
      var retry = 0;
      _window.sprinklr.chat = {
        load() {
          if (_window.sprinklr.chat.loaded) {
            resolve();
          } else {
            var onEvent = function ({ detail }) {
              if (detail.error) {
                reject(detail.error);
              } else {
                resolve();
              }
              _document.removeEventListener('@spr/CHAT_LOADED', onEvent);
            };
            _document.addEventListener('@spr/CHAT_LOADED', onEvent);
            var script = _document.createElement(_script);
            script.type = 'text/javascript';
            script.async = true;
            script.src = '{CDN_HOST_URL}/sdk/{env}/{appId}';
            script.onerror = function (err) {
              _document.removeEventListener('@spr/CHAT_LOADED', onEvent);
              retry++;
              if (retry < 3) {
                existingScript.parentNode.removeChild(script);
                setTimeout(window.sprinklr.chat.load, 250);
              } else {
                retry = 0;
                reject(err);
              }
            };
            var existingScript = _document.getElementsByTagName(_script)[0];
            existingScript.parentNode.insertBefore(script, existingScript);
          }
          return loadPromise;
        },
      };
    });
  }
})();
window.sprinklr.chat
  .load()
  .then(() => {
    // SDK loaded successfully
    console.log('Live Chat SDK loaded.');
  })
  .catch((e) => {
    // SDK loading failed
    console.error('Failed to load Live Chat SDK:', e);
  });



**Explanation of the SDK loading code:**


- If `window.sprinklr.chat.loaded` is undefined, then it creates a new <script> element, sets its type to `'text/javascript'`, and makes it load asynchronously. The script's source URL is set to `{CDN_HOST_URL}/sdk/{env}/{appId}` and the new script element is inserted before the first existing <script> tag in the document. If an error occurs while loading the script, the promise is rejected.

- If the SDK bundle is loaded, a custom event `@spr/CHAT_LOADED` is dispatched. If any error occurs while fetching, the same event `@spr/CHAT_LOADED` with `error: true` is dispatched.

- An event listener is attached to the document which listens to the `@spr/CHAT_LOADED` event. Upon successfully receiving the event, the promise is resolved. Otherwise, the promise is rejected.

- If there is a network error that prevents the bundle from being fetched, the system will automatically retry up to 3 times at intervals of 250 milliseconds.

- You can call `window.sprinklr.loadSDK()` to load the script whenever needed.

## Next Step

Explore [Headless Live Chat SDK Quick Reference](https://dev.sprinklr.com/headless-live-chat-sdk-quick-reference)


  [](https://dev.sprinklr.com/install-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/install-headless-live-chat-sdk)
