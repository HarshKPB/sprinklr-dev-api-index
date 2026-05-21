---
title: "Update Locale Headless Live Chat SDK"
slug: update-locale-headless-live-chat-sdk
url: https://dev.sprinklr.com/update-locale-headless-live-chat-sdk
---

# Update Locale Headless Live Chat SDK

# Update Locale


The `updateLocale()` method dynamically updates the locale (language) of the currently logged-in user.

## SDK Method

`updateLocale()`

## Example Usage




 Copy Code


try {
  const updatedLocale = await window.sprinklr.chat.updateLocale({
    locale: 'es', // Spanish locale code
  });
  console.log('Locale updated to:', updatedLocale); // 'es'
} catch (error) {
  console.error("Failed to update locale:", error);
}



## Parameters













      [Supported Locales table below](https://dev.sprinklr.com/update-locale-headless-live-chat-sdk#supported-locales)






| Parameter | Description | Type | Required/Optional | Sample |
| --- | --- | --- | --- | --- |
| locale | The locale code to set for the user. See . | String | Required | 'es', 'ja', 'zh-CN', 'fr-CA' |


**Dev Notes:** The locale must be a valid **ISO 639‑1 language code** (for example, 'en', 'es', 'fr', 'de'). The method validates the provided locale before processing. See the Supported Locales table below.

## Response Format

The resolved value will be:



string // The updated locale (e.g., 'es', 'ja', 'zh-CN')



## Error Types









      ``



      ``



      ``



      ``



      ``




| Error Type | When It Occurs |
| --- | --- |
| NOT_ACCEPTABLE | When the locale code provided is invalid or not supported by the SDK |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| NETWORK_FALURE | When syncing the locale with the backend fails for network or server reasons. |
| CHAT_NOT_INITIATED | Thrown when chat SDK methods are called before init(). |
| INCORRECT_PAYLOAD | When the backend rejects the locale update, for example when the requested locale is not configured or enabled for your Live Chat application in Sprinklr |

## Supported Locales












































































| Name | Locale Code |
| --- | --- |
| Amharic | am |
| Arabic | ar |
| Bulgarian | bg |
| Bengali | bn |
| Bosnian | bs |
| Kurdish (Sorani) | ckb |
| Czech | cs |
| Czech (CZ) | cs-CZ |
| Danish | da |
| German | de |
| Greek | el |
| English | en |
| English (UK) | en-GB |
| English (Ireland) | en-IE |
| English (US) | en-US |
| Spanish | es |
| Spanish (Latin America and the Caribbean) | es-419 |
| Estonian | et |
| Finnish | fi |
| French | fr |
| French (Canada) | fr-CA |
| Gujarati | gu |
| Hebrew | he |
| Hindi | hi |
| Croatian | hr |
| Croatian (HR) | hr-HR |
| Hungarian | hu |
| Hungarian (HU) | hu-HU |
| Indonesian | id |
| Icelandic | is-IS |
| Italian | it |
| Italian (IT) | it-IT |
| Japanese | ja |
| Kannada | kn |
| Korean | ko |
| Lithuanian | lt |
| Latvian | lv |
| Macedonian | mk |
| Malayalam | ml |
| Marathi | mr |
| Malay | ms |
| Bokmål, Norwegian | nb |
| Dutch | nl |
| Punjabi | pa |
| Polish | pl |
| Polish (PL) | pl-PL |
| Portuguese | pt |
| Portuguese (Brazil) | pt-BR |
| Portuguese (Portugal) | pt-PT |
| Romanian | ro |
| Russian | ru |
| Slovak | sk |
| Slovak (SK) | sk-SK |
| Slovenian | sl |
| Albanian | sq |
| Serbian | sr |
| Swedish | sv |
| Tamil | ta |
| Telugu | te |
| Thai | th |
| Turkish | tr |
| Vietnamese | vi |
| Chinese | zh |
| Chinese (Simplified) | zh-CN |
| Chinese (Hong Kong) | zh-HK |
| Chinese (Traditional) | zh-TW |


  [](https://dev.sprinklr.com/update-locale-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/update-locale-headless-live-chat-sdk)
