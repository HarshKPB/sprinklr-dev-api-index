---
title: "Unrestricted Search Messages"
slug: unrestricted-search-messages
url: https://dev.sprinklr.com/unrestricted-search-messages
---

# Unrestricted Search Messages

#
Unrestricted Search Messages

Using this API, you can search for messages without applying any filters.

### API Endpoint

https://care-api-`{env}`.sprinklr.com/care/community/rest/authenticated/message/search-messages-unfiltered

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Authenticated token for making API calls that require creating, updating, deleting tasks |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/message/search-messages-unfiltered' \
 -H 'X-Community-Authorization: Bearer {Authenticated Token}' \
 -H 'Content-Type: application/json' \
 -d '{
}'





## Example - Response

      

{
   "data": [
       {
           "id": "60feb30c297245545dca37d7",
           "projId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
           "topics": [
               "60feb208421f9543b73ea190"
           ],
           "snT": "COMMUNITY",
           "mTp": 230,
           "mSTp": 0,
           "m": "
sdcsdcsdcsdcsdcsdcsdcsdcsdcsdcsdcsdc
",
           "pL": "https://95da27b2-8e38-40ea-a2e1-4e0769cd7471.prod-tier2-care.sprinklr.com/conversations/60feb208421f9543b73ea190/sdcsdcsdc/60feb2fefce75c004bfea6df?commentId=60feb30c297245545dca37d7",
           "path": "60feb208421f9543b73ea190/sdcsdcsdc/60feb2fefce75c004bfea6df?commentId=60feb30c297245545dca37d7",
           "fU": "60fe96a697066527fc104cda",
           "fUInfo": {
               "communityUserId": "60fe96a697066527fc104cda",
               "fullName": "hokj hokj",
               "username": "hokj",
               "color": "#25D54B"
           },
           "tU": "60fe96a697066527fc104cda",
           "pMTp": 229,
           "pSnMId": "60feb2fefce75c004bfea6df",
           "psnCTm": 1627304702501,
           "cId": "60feb2fefce75c004bfea6df",
           "locale": "en_US",
           "cTm": 1627304716848,
           "mTm": 1632135727398,
           "lastActivityAt": 1627304716848,
           "indexDisabled": false,
           "iD": false,
           "hConv": true,
           "additional": {},
           "customFields": {},
           "status": "one",
           "brandPost": false,
           "privateMessage": false,
           "archived": false,
           "closed": false,
           "escalated": false,
           "merged": false,
           "spam": false,
           "mUIds": [],
           "accepted": false,
           "official": false,
           "pinned": false,
           "sprUrl": "https://space.sprinklr.com/new?qId=COMMUNITY-:-230-:-60feb30c297245545dca37d7-:-ACCOUNT-:-822932&qTyp=UNIVERSAL",
           "hasAuthorMarkedSolution": false,
           "reminderSent": false,
           "lSContent": {},
           "hasConditionalSection": false,
           "grants": []
       },
       {
           "id": "60feb308c558266f204ca644",
           "projId": "95da27b2-8e38-40ea-a2e1-4e0769cd7471",
           "topics": [
               "60feb208421f9543b73ea190"
           ],
           "snT": "COMMUNITY",
           "mTp": 230,
           "mSTp": 0,
           "m": " \n
sdcsdcsdcsdcsdcsdcsdcsdcsdcsdcsdcsdc
 \n",
           "pL": "https://95da27b2-8e38-40ea-a2e1-4e0769cd7471.prod-tier2-care.sprinklr.com/conversations/60feb208421f9543b73ea190/sdcsdcsdc/60feb2fefce75c004bfea6df?commentId=60feb308c558266f204ca644",
           "path": "60feb208421f9543b73ea190/sdcsdcsdc/60feb2fefce75c004bfea6df?commentId=60feb308c558266f204ca644",
           "fU": "60fe96a697066527fc104cda",
           "fUInfo": {
               "communityUserId": "60fe96a697066527fc104cda",
               "fullName": "hokj hokj",
               "username": "hokj",
               "color": "#25D54B"
           },
           "tU": "60fe96a697066527fc104cda",
           "pMTp": 229,
           "pSnMId": "60feb2fefce75c004bfea6df",
           "psnCTm": 1627304702501,
           "cId": "60feb2fefce75c004bfea6df",
           "locale": "en_US",
           "cTm": 1627304712643,
           "mTm": 1632135727410,
           "lastActivityAt": 1627304723600,
           "indexDisabled": false,
           "iD": false,
           "hConv": true,
           "stats": {
               "numReplies": 2.0
           },
           "additional": {},
           "lastEngagedUser": "60fe96a697066527fc104cda",
           "lastEngagedTime": 1627304723600,
           "customFields": {},
           "status": "one",
           "brandPost": false,
           "privateMessage": false,
           "archived": false,
           "closed": false,
           "escalated": false,
           "merged": false,
           "spam": false,
           "mUIds": [],
           "accepted": false,
           "official": false,
           "pinned": false,
           "sprUrl": "https://space.sprinklr.com/new?qId=COMMUNITY-:-230-:-60feb308c558266f204ca644-:-ACCOUNT-:-822932&qTyp=UNIVERSAL",
           "hasAuthorMarkedSolution": false,
           "reminderSent": false,
           "lSContent": {},
           "hasConditionalSection": false,
           "grants": []
       }
],
   "totalHitCount": 289,
   "hasMore": true,
   "pageNumber": 0
}





**Dev Notes: **

- By default, you’ll be able to fetch 10 records in the runrestricted search messages API response
- To trim the response or to fetch the next set of response, refer to search messages/Posts API for information on required request parameters
- Use user credentials of the user who has permission to search messages
 [](https://dev.sprinklr.com/unrestricted-search-messages)

[Back to top](https://dev.sprinklr.com/unrestricted-search-messages)
