---
title: "Validate OTP"
slug: validate-otp
url: https://dev.sprinklr.com/validate-otp
---

# Validate OTP

#
Validate OTP


Using this API, you can validate the user using the OTP received in the email after making the Generate OTP API call.

### API Endpoint

https://care-api-`{{env}}`.sprinklr.com/care/community/rest/authenticated/user/verify-user-via-otp

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Aauthenticated token for making API calls that require creating, updating, deleting tasks |
| Accept | application/json | Determines the acceptable response type from the server |

### Query Parameters

| Parameter | Required/Optional | Decsription | Type |
| --- | --- | --- | --- |
| otp | Required | Refers to the one-time PIN received in the email using the generate OTP API | String |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/verify-user-via-otp?otp=096516' \
 -H 'X-Community-Authorization: Bearer {Authenticated Token}' \
  -H 'accept: application/json'  \






## Example - Response




{
    "success": true
}





## Response Parameters
















| Parameters | Description | Type |
| --- | --- | --- |
| success | If true, the OTP has been successfully generated and shared over email | Boolean |

**Dev Notes: **Please, remember that the OTP is only valid for a few minutes. It is recommended to validate the OTP as soon as receive it. Else, you’ll receive “OTP_EXPIRED” error message.

[](https://dev.sprinklr.com/validate-otp)

[Back to top](https://dev.sprinklr.com/reporting-blueprints)
