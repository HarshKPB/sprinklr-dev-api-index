---
title: "Oct - Dec, 2021"
slug: oct-dec-2021
url: https://dev.sprinklr.com/oct-dec-2021
---

# Oct - Dec, 2021

# Oct - Dec, 2021

**Developer Note:** We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.	Please note that the API base endpoint has changed from `api2` to `api3`.

For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## **Delete Post ** - December 3rd, 2021.

You can use this API to delete a post using post Id.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/post/{postId}

## **Delete Draft ** - December 3rd, 2021.

You can use this API to delete a draft using draft Id.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/draft/{draftId}

## **Publishing Dynamic Templates ** - November 16th, 2021.

You can use this API to publish dynamic template on supported social and messaging channels.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/message

## **Create Case Via Profile ** - November 16th, 2021.

A case in Sprinklr can be created on top of a External Profile using this API call. As response you will receive the complete Case Object with Profile details.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/universalcase/profile-case

## **Bootstrap (PARTNER_ACCOUNT) API Endpoint Enhancement** - November 16th, 2021.

Now you will also get Account Custom Fields including Account Created Time and Account Modified Time as response when you call the Bootstrap API.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PARTNER_ACCOUNTS

## **Case Webhook Filters Enhancement** - November 16th, 2021.

Now you can use Source within the Webhook attributes to filter all the Case Webhooks based on account.

[](https://dev.sprinklr.com/oct-dec-2021)

[Back to top](https://dev.sprinklr.com/oct-dec-2021)
