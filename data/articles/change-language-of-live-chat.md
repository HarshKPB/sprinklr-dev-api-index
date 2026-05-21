---
title: "Change Language of Live Chat"
slug: change-language-of-live-chat
url: https://dev.sprinklr.com/change-language-of-live-chat
---

# Change Language of Live Chat

# Change Locale of Live Chat

This method is used to change the language of the Live Chat app. You can pass the BCP 47 language code to this SDK method.

## Method

`sprChat('updateLocale','locale');`

## Parameters







| Parameter | Type | Required/Optional | Description | Possible values | Default value |
| --- | --- | --- | --- | --- | --- |
| locale | String | Required | The language you want to set for Live Chat. | Language codes. | English |

**Dev Notes: **

The following is a list of supported languages along with their corresponding language codes:


- Amharic - am

- Arabic - ar

- Bulgarian - bg

- Bengali - bn

- Bosnian - bs

- Czech - cs

- Danish - da

- German - de

- Greek - el

- English - en

- English (US) - en-US

- Spanish - es

- Estonian - et

- Finnish - fi

- French - fr

- French (Canada) - fr-CA

- Gujarati - gu

- Hebrew - he

- Hindi - hi

- Croatian - hr

- Hungarian - hu

- Indonesian - id

- Icelandic - is

- Italian - it

- Japanese - ja

- Kannada - kn

- Korean - ko

- Lithuanian - lt

- Latvian - lv

- Macedonian - mk

- Malayalam - ml

- Marathi - mr

- Malay - ms

- Norwegian Bokmål - nb

- Dutch - nl

- Punjabi - pa

- Polish - pl

- Portuguese - pt

- Portuguese (Portugal) - pt-PT

- Romanian - ro

- Russian - ru

- Slovak - sk

- Slovenian - sl

- Albanian - sq

- Serbian - sr

- Swedish - sv

- Tamil - ta

- Telugu - te

- Thai - th

- Turkish - tr

- Vietnamese - vi

- Chinese - zh

- Chinese (Simplified) - zh-CN

- Chinese (Hong Kong) - zh-HK

- Chinese (Traditional) - zh-TW

## Example


The following example sets the Live Chat language to French:




  Copy Code



sprChat('updateLocale','fr');





[](https://dev.sprinklr.com/change-language-of-live-chat)

[Back to top](https://dev.sprinklr.com/change-language-of-live-chat)
