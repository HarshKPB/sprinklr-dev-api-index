---
title: "Remove Contact from Suppression List"
slug: remove-contact-from-suppression-list
url: https://dev.sprinklr.com/remove-contact-from-suppression-list
---

# Remove Contact from Suppression List

#
 POST  Remove Contact from Suppression List



Using this API, you can remove a contact from an existing suppression list.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/suppressionList/removeContact/`{suppressionListId}`/`{contactValue}`

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| suppressionListId | Required | The unique identifier for the suppression list from which you want to remove the contact | String |
| contactValue | Required | The contact number that you want to remove from the suppression list | String |

**Steps to Extract Suppression Id from UI: **

- Click on the "Voice Care" within Sprinklr Service module
- From the "Voice Settings" menu placed in extreme left, select "Suppression List" option.
- Click on three dots beside the suppression list where you want to add the contact.
- Now click on "View" option from the drop-down menu that appearsThe suppression list Id would be the ID appended in the page URL. Example: https://space.sprinklr.com/care/voice/settings/suppression-list/64f5b17998d2340e005c38a1/contact-list. Here "64f5b17998d2340e005c38a1" is the suppression list Id.

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/suppressionList/removeContact/64f5b17998d2340e005c38a1/+918447380993'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \






## Example - Response





204 No Content







**Dev Notes: **204 No Content Implies that the contact has been successfully removed from the given suppression list.

	[](https://dev.sprinklr.com/remove-contact-from-suppression-list)




[Back to top](https://dev.sprinklr.com/remove-contact-from-suppression-list)
