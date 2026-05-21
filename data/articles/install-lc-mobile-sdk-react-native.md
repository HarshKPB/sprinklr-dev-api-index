---
title: "Install LC Mobile SDK - React Native"
slug: install-lc-mobile-sdk-react-native
url: https://dev.sprinklr.com/install-lc-mobile-sdk-react-native
---

# Install LC Mobile SDK - React Native

# Install Live Chat SDK - React Native


To integrate Sprinklr Live Chat Messenger into your project, you must install the Live Chat SDK along with its necessary peer dependencies. This section provides a step-by-step guide to install Live Chat Messenger and its necessary dependencies.


The following are the steps for integrating Sprinklr Messenger. This page covers the **first step: Install**. Use the flow below to navigate through all steps of the integration process.

 **Install** > [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)

**On this page:**



- [Configure Sprinklr Messenger Registry](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#configure-sprinklr-messenger-registry)

- [Install Sprinklr Messenger](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#install-sprinklr-messenger)
- [Install Peer Dependencies](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#install-peer-dependencies)

- [Supported Peer Dependencies](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#supported-peer-dependencies)

- [Customize Peer Dependencies](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#customizing-peer-dependencies) (Optional)


## Configure Sprinklr Messenger Registry

Sprinklr Live Chat Messenger is a restricted package. To install Sprinklr scoped packages, you must configure the appropriate registry and authentication:

### Using npm (.npmrc)

Add the following entries to your `.npmrc` file:




@sprinklrjs:registry=https://prod-nexus-external.sprinklr.com/nexus/repository/npm/
​
always-auth=true
​
//prod-nexus-external.sprinklr.com/nexus/repository/npm/: _auth=








**Dev Notes:**
     ` <SPR_REGISTRY_AUTH_TOKEN>` is the registry token provided by Sprinklr.
    To get the registry token, raise a support ticket at
    [tickets@sprinklr.com](mailto:tickets@sprinklr.com).


### Using yarn (v2 / v3) (.yarnrc.yml)

Add the following configuration to your `.yarnrc.yml` file:




npmScopes:
​
  sprinklrjs:
​
    npmRegistryServer: "https://prod-nexus-external.sprinklr.com/nexus/repository/npm/"
​
     npmAuthToken: ${ SPR_REGISTRY_AUTH_IDEN}




**Dev Notes:**
    ` <SPR_REGISTRY_AUTH_TOKEN>` and
    `<SPR_REGISTRY_AUTH_IDEN>` are the registry tokens provided by Sprinklr.
    To get the registry tokens, raise a support ticket at
    [tickets@sprinklr.com](mailto:tickets@sprinklr.com).


## Install Sprinklr Messenger


**Dev Notes:** The Live Chat package name has been updated from `@sprinklr/chat-native-client` to `@sprinklrjs/chat-native-client`.


Install the Sprinklr Messenger in your project using your preferred package manager, as shown in the following commands:

### Using npm




npm install --save @sprinklrjs/chat-native-client@15.0.0







### Using yarn




yarn add @sprinklrjs/chat-native-client@15.0.0







## Install Sprinklr Messenger Peer Dependencies

Sprinklr Live Chat Messenger supports the peer dependencies listed in the Supported Peer Dependencies table. You can install these dependencies as part of the Sprinklr Messenger installation.


In addition to installing these dependencies, they also need to be linked natively. To properly link them, refer to their official documentation. Additionally, verify that you have all the required dependencies and that their versions meet the specified threshold in the Supported Versions column of the Supported Peer Dependencies table.


If you need to use an alternative to a specific dependency or implement a custom solution, refer to the Customize Peer Dependencies section for guidance.


**Dev Notes:**
    Starting from version `13.0.0`, Sprinklr Messenger has transitioned from using
    `AsyncStorage` to `react-native-keychain`.
    For anonymous users, the chat session token is stored locally on the device.
    To ensure backward compatibility and a smooth migration, we recommend including both dependencies for the next year.


### Install Peer Dependencies

You can use the following yarn or npm command to install the peer dependencies:

#### Using yarn



yarn add







**Example**



yarn add react-native-vector-icons react-native-blob-util react-native-image-picker react-native-video @react-native-community/netinfo react-native-webview react-native-permissions @react-native-camera-roll/camera-roll @react-native-async-storage/async-storage @react-native-clipboard/clipboard react-native-svg react-native-reanimated cobrowse-sdk-react-native @react-native-masked-view/masked-view react-native-keychain







#### Using npm



npm install






**Example**



npm install --save react-native-vector-icons react-native-blob-util react-native-image-picker react-native-video @react-native-community/netinfo react-native-webview react-native-permissions @react-native-camera-roll/camera-roll @react-native-async-storage/async-storage @react-native-clipboard/clipboard react-native-svg react-native-reanimated cobrowse-sdk-react-native react-native-keychain @react-native-masked-view/masked-view







### Supported Peer Dependencies

The following sections provide an overview of the supported peer dependencies and their respective details:

### Peer Dependency Tables


- [State Management](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#state-management)

- [React Native UI Components](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#react-native-ui-components)

- [Utility Libraries](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#utility-libraries)

- [React Native Community Libraries](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#react-native-community-libraries)

- [Additional React Native Features](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native#additional-react-native-features)

#### State Management











    [redux](https://github.com/reduxjs/redux)




    [react-redux](https://github.com/reduxjs/react-redux)




    [redux-saga](https://github.com/redux-saga/redux-saga)




    [reselect](https://github.com/reduxjs/reselect)





| Peer Dependency | Description | Supported Versions |
| --- | --- | --- |
|  | JavaScript library for predictable and maintainable global state management | 4.0.0 or later |
|  | Facilitates the connection between React components and the Redux store | 8.0.0 or later |
|  | Handles side effects in Redux applications, such as data fetching and impure things like accessing the browser cache | 1.0.1 or later |
|  | A library for creating memorized "selector" functions | * |

#### React Native UI Components







    [react-native](https://github.com/facebook/react-native)


****




    [react](https://github.com/facebook/react)




    [react-native-gifted-chat](https://github.com/FaridSafi/react-native-gifted-chat)




    [react-native-render-html](https://github.com/meliorence/react-native-render-html)




    [react-native-svg](https://github.com/software-mansion/react-native-svg)




    [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons)




    [react-native-video](https://github.com/TheWidlarzGroup/react-native-video)




    [react-native-webview](https://github.com/react-native-webview/react-native-webview)




| Peer Dependency | Description | Supported Versions |
| --- | --- | --- |
|  | Core library for building cross-platform mobile applications using React        Dev Notes: If you are upgrading to React Native version 0.78.2 and above, you also need to upgrade React to version 19.0.0. | ≥0.73.0 and ≤0.82.0 |
|  | JavaScript library for building UIs, base for React Native | 18.2.0 or later |
|  | A customizable chat UI library for React Native | * |
|  | Allows rendering of HTML content within a React Native app | * |
|  | Provides SVG support in React Native applications | * |
|  | A library for using vector icons in React Native apps | * |
|  | Enables video playback within React Native applications | * |
|  | A component to render web content in a React Native app | * |

#### Utility Libraries






    [ramda](https://github.com/ramda/ramda)



    [lodash](https://github.com/lodash/lodash)



    [immutability-helper](https://github.com/kolodny/immutability-helper)



    [dayjs](https://github.com/iamkun/dayjs)



    [buffer](https://github.com/feross/buffer)



    [color](https://github.com/Qix-/color)



    [crypto-js](https://github.com/brix/crypto-js)



    [jsencrypt](https://github.com/travist/jsencrypt)



    [mqtt](https://github.com/mqttjs/MQTT.js)



    [process](https://github.com/defunctzombie/node-process)



    [prop-types](https://github.com/facebook/prop-types)



    [events](https://github.com/browserify/events)



| Peer Dependency | Description |
| --- | --- |
|  | A library for JavaScript functional programming |
|  | A modern JavaScript utility library delivering modularity, performance & extras |
|  | A helper library for creating immutable data structures |
|  | A date library that parses, validates, manipulates, and displays dates/times |
|  | Handles binary data within the app |
|  | Immutable color conversion and manipulation |
|  | JavaScript library of crypto standards |
|  | JavaScript library for RSA encryption |
|  | MQTT client library for Node.js and browser |
|  | Provides information about and control over the current node.js process |
|  | Used for type checking React props |
|  | An implementation of the Node.js EventEmitter class |

#### React Native Community Libraries






    [@react-native-async-storage/async-storage](https://github.com/react-native-async-storage/async-storage)



    [@react-native-camera-roll/camera-roll](https://github.com/react-native-cameraroll/react-native-cameraroll)



    [@react-native-clipboard/clipboard](https://github.com/react-native-clipboard/clipboard)



    [@react-native-community/netinfo](https://github.com/react-native-netinfo/react-native-netinfo)



    [@react-native-community/push-notification-ios](https://github.com/react-native-push-notification/ios)



| Peer Dependency | Description |
| --- | --- |
|  | An asynchronous, unencrypted, persistent, key-value storage system for React Native |
|  | It provides access to the local camera roll or photo library |
|  | Allows access to the device's clipboard |
|  | It allows you to get information on Connection type and Connection quality |
|  | Handles push notifications on iOS |

#### Additional React Native Features








    [react-native-blob-util](https://github.com/RonRadtke/react-native-blob-util)





    [react-native-code-push](https://github.com/microsoft/react-native-code-push)





    [react-native-image-picker](https://github.com/react-native-image-picker/react-native-image-picker)





    [react-native-keep-awake](https://github.com/corbt/react-native-keep-awake)





    [react-native-permissions](https://github.com/zoontek/react-native-permissions)





    [react-native-push-notification](https://github.com/zo0r/react-native-push-notification)





    [react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)





    [react-native-maps](https://github.com/react-native-maps/react-native-maps)





    [cobrowse-sdk-react-native](https://github.com/cobrowseio/cobrowse-sdk-react-native)





    [@react-native-masked-view/masked-view](https://github.com/callstack/masked-view)





    [react-native-keychain](https://github.com/oblador/react-native-keychain)





| Peer Dependency | Description | Required/Optional | Supported Versions |
| --- | --- | --- | --- |
|  | Handles data transfer and file system access | * | * |
|  | This plugin provides client-side integration for the CodePush service, allowing you to easily add a dynamic update experience | * | * |
|  | A React Native module that allows you to select a photo/video from the device library or camera | * | * |
|  | This React Native package allows you to prevent the screen from going to sleep while your app is active | * | * |
|  | A unified permissions API for React Native on iOS, Android | Required | 3.6.0 or later |
|  | Manages local and remote notifications | * | * |
|  | React Native Reanimated is a powerful animation library. With Reanimated, you can easily create smooth animations and interactions that run on the UI thread. | Required | * |
|  | This library includes Map components for iOS and Android. Install only if you want to support the location sharing feature in Live Chat. | Optional | * |
|  | This library enables the mobile co-browsing functionality, allowing customers to share their mobile app screens with service agents through the Sprinklr console. | Optional | 3.0.0 or later |
|  | This library provides view masking functionality required to enable the typing indicator feature in Live Chat. | Optional | * |
|  | This library provides access to the Keychain (iOS) and Keystore (Android) for securely storing credentials like passwords, tokens, or other sensitive information in React Native apps. | Required | * |


**Dev Notes:**
    Sprinklr Messenger has transitioned from using `AsyncStorage` to
    `react-native-keychain` to strengthen security.
    For anonymous users, the chat session token is stored locally on the device.
    To ensure backward compatibility and a smooth migration, we recommend including both dependencies for the next year.




    **Important:** Relying solely on `react-native-keychain` as a peer dependency will result in the loss of all existing anonymous user chats.
    Maintaining both dependencies during the transition period balances security with data continuity.


## Customizing Peer Dependencies (Optional)

This section explains which dependencies are mandatory, which can be customized, and how to register or unregister custom implementations for seamless integration.

### Why is Customization Required?

In some cases, your existing codebase may already include specific libraries for functionalities such as SVG rendering, web views, and network information.
If the Sprinklr SDK enforces its own versions of these dependencies, it could lead to conflicts and compatibility issues with your setup.

To maintain consistency and avoid disruptions, the Sprinklr SDK allows you to inject custom implementations for certain dependencies. This ensures a seamless integration process, allowing you to:


- Use your preferred libraries.

- Avoid breaking existing functionality.

- Leverage the full capabilities of the Sprinklr SDK without replacing core dependencies.

### Types of Peer Dependencies

The peer dependencies in the Sprinklr SDK are classified into mandatory and customizable dependencies.

#### 1. Mandatory Peer Dependencies

These dependencies are required for the Sprinklr SDK to function properly. They cannot be replaced, and their versions must be greater than or equal to the specified ones:








    [redux](https://github.com/reduxjs/redux)
    [react-redux](https://github.com/reduxjs/react-redux)

    [react](https://github.com/facebook/react)
    [redux-saga](https://github.com/redux-saga/redux-saga)


| Dependency | Required Version |
| --- | --- |
|  | >= 4.0.0 |
|  | >= 0.70.0 |
| react-redux | >= 8.0.0 |
|  | >= 18.2.0 |
|  | >= 1.0.1 |

#### 2. Customizable Dependencies

The following dependencies can be overridden with your own implementations. Each dependency is identified by a dependency key and an implementation type provided by Sprinklr.









    [react-native-svg](https://github.com/software-mansion/react-native-svg)
    [react-native-webview](https://github.com/react-native-webview/react-native-webview)
    [@react-native-community/netinfo](https://github.com/react-native-netinfo/react-native-netinfo)
    [@react-native-clipboard/clipboard](https://github.com/react-native-clipboard/clipboard)
    [StatusBar from react-native](https://reactnative.dev/docs/statusbar)
    [@react-native-camera-roll/camera-roll](https://github.com/react-native-cameraroll/react-native-cameraroll)
    [react-native-permissions](https://github.com/zoontek/react-native-permissions)
    [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons)
    [react-native-video](https://github.com/TheWidlarzGroup/react-native-video)
    [react-native-image-picker](https://github.com/react-native-image-picker/react-native-image-picker)
    [react-native-blob-util](https://github.com/RonRadtke/react-native-blob-util)
    [@react-native-async-storage/async-storage](https://github.com/react-native-async-storage/async-storage)


| Dependency | Implementation Type | Dependency Key |
| --- | --- | --- |
|  | SPRSvg | SVG |
|  | SPRWebview | WEBVIEW |
|  | SPRNetInfo | NET_INFO |
|  | SPRClipboard | CLIPBOARD |
|  | SPRStatusBar | STATUS_BAR |
|  | SPRCameraRoll | CAMERA_ROLL |
|  | SPRPermissions | PERMISSIONS |
|  | SPRVectorIcons | VECTOR_ICONS |
|  | SPRVideoPlayer | VIDEO_PLAYER |
|  | SPRMediaPicker | MEDIA_PICKER |
|  | SPRFileManager | FILE_MANAGER |
|  | SPRCustomStorage | ASYNC_STORAGE |

### Registering Custom Implementations

To provide a custom implementation, follow these steps:


- **Identify the Dependency Key:** Each dependency corresponds to a dependency key that you will use for registration.

- **Import the Required Modules:** Import the necessary implementation type and MessengerDependenciesManager from the Sprinklr SDK. *Placeholder: Example import statement*

- **Register Multiple Dependencies:** You can register multiple dependencies at once using `registerDependencies()`. *Placeholder: Example registration code*

- **Register a Single Dependency:** If you only need to override a specific dependency, use `registerDependency()`. *Placeholder: Example single dependency registration*

### Unregistering Custom Implementations

If you need to remove a custom implementation, you can unregister a specific dependency or all custom dependencies at once.


- **Unregister a Single Dependency:** *Placeholder: Example unregister single dependency*

- **Unregister All Custom Dependencies:** *Placeholder: Example unregister all dependencies*

## Next Steps

[Setup Live Chat SDK](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native)

## Additional Resources

See **All Integration Steps**
 [Install](https://dev.sprinklr.com/../install-lc-mobile-sdk-react-native) > [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)

  [](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native)




[Back to top](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native)
