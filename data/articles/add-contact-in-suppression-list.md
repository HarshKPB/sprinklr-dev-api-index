---
title: "Add Contact in Suppression  List"
slug: add-contact-in-suppression-list
url: https://dev.sprinklr.com/add-contact-in-suppression-list
---

# Add Contact in Suppression  List

#
 POST  Add Contact in Supression  List



Using this API, you can add customer phone numbers to a list that should not be contacted by the brand. This list could include phone numbers of individuals who have requested to be placed on the "do not call" list, those who have previously asked to be removed from the calling list, those who do not match the targeted persona anymore, or those who are considered ineligible for certain types of calls (e.g., for regulatory or compliance reasons).

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/suppressionList/addContact

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

### Request Parameters









































| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Optional | Refers to the name of the customer | String |
| contactValue | Required | Refers to the phone number of the customer | String |
| suppressionListId | Required | Refers to the unique identifier for the suppression list where you want to add the contact | String |
| expiryTime | Optional | Refers to the expiration time of the contact | Epoch |
| createdTime | Optional | Refers to the time at which the contact was first created | Epoch |

**Steps to Extract Suppression Id from UI: **

- Click on the "Voice Care" within Sprinklr Service module
- From the "Voice Settings" menu placed in extreme left, select "Suppression List" option.
- Click on three dots beside the suppression list where you want to add the contact.
- Now click on "View" option from the drop-down menu that appearsThe suppression list Id would be the ID appended in the page URL. Example: https://space.sprinklr.com/care/voice/settings/suppression-list/64f5b17998d2340e005c38a1/contact-list. Here "64f5b17998d2340e005c38a1" is the suppression list Id.

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/suppressionList/addContact' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "supress 1",
    "contactValue": "+917213452341",
    "suppressionListId": "64117baaw2de445fecbe3e80",
    "expiryTime": "1686053410000",
    "createdTime": "1676630765000"
}






## Example - Response





{
    "data": {
        "name": "supress 1",
        "contactValue": "+917213452341",
        "suppressionListId": "64117baaw2de445fecbe3e80",
        "expiryTime": 1693912368000,
        "createdTime": 1676630765000
    },
    "errors": []
}







	[](https://dev.sprinklr.com/add-contact-in-suppression-list)




[Back to top](https://dev.sprinklr.com/add-contact-in-suppression-list)
