---
title: "REST API Error AND Status Codes"
slug: rest-api-error-and-status-codes
url: https://dev.sprinklr.com/rest-api-error-and-status-codes
---

# REST API Error AND Status Codes

#
 REST API Errors and Status Codes

This is an error and status code documentation guide. The objective of this guide is to familiarize you with the all possible REST API response codes that you might come across when making API calls.

Refer to the quick links below to get further insight into the status codes, their corresponding status, description, and recommended solutions (if any).

### `200s - Success`











| Status Code | Status | Description |
| --- | --- | --- |
| 200 | OK | Success, i.e., the API call was successful and performed the intended action |
| 201 | Created | Success, i.e., the API call was successful and the resource has been created |
| 202 | Accepted | The request has been accepted. However, processing will take some time |
| 204 | No Content | The API call was a successful but didn't have a associated response |

### `400s - Client-Related Errors`











-
-
-
-
-

****[refresh the token](https://dev.sprinklr.com/refreshing-access-token)

[MY ACCOUNT](https://dev.sprinklr.com/my-apps)

-
-
-

-
-
-

-
-
-

-
-
-



``
````

-
- ****



| Status Code | Status | Possible Reasons | Recommended Solution |
| --- | --- | --- | --- |
| 400 | Bad Request | Bad syntax. A probable issue with the request payload. Look for the following issues:Missing or wrong keyMissing access tokenWrong method type, i.e., GET, POST, PUT, DELETEPerforming an invalid action. For example, if a resource is already deleted, performing a DELETE API call will return 400 bad requestInvalid request/response | Please recheck the documentation and update the requestIf getting the same response after making the changes, reach out to the integration support team |
| 400 | Access to resource is forbidden | Issue with UI permission for the assigned workspace | Reach out to your admin or success manager for assigning required roles and permissions |
| 401 | Unauthorized | The bearer token may be invalid, expired, or may lack the necessary permissions | Refresh the authorization tokenNote: Access token is valid for 30 days. The user needs to  post that |
| 401 | Unauthorized | Invalid consumer key | Check whether the key is associated with the right environmentYou can find key related information under  section on the developer portal. |
| 403 | Developer Inactive | Probable issue with the headers | Recheck headers such as:KeyAuthorization TokenContent_TypeIf the issue still persists, check whether you have access to the requested endpoint |
| 403 | Forbidden | This is a client-side errorThe API call is correctly made. However, the user is forbidden to access the requested resource for some reason. | Cross check the requested endpoint URIClear cookies if anyRequest for the required file permissions |
| 403 | Developer Over Rate | If the API calls made per second or hour exceed the set call limit | Retry after some time to get a successful response |
| 404 | Resource Not Found | The requested resource could not be found | Cross check the requested endpoint URLRecheck the headers, method type, and request body (if any)Consult the integration support team if the issue persists |
| 405 | Method Not Allowed | Issue with the method type. That is, the method type (GET, POST, PUT, DELETE) are incorrect | Please check the documentation for the the correct method type |
| 409 | Conflict | This error occurs when there is a conflict with the current version/status of the targeted resource.For Instance, If you are updating a record that is older compared to the one existing on the server, you'll receive a 409 Conflict.This is a common error that can occur when updating dynamic content using PUT method type | Recheck the requested URLClear cookies (if any)Reach out to integration support team if the other recommended solutions don't work |
| 411 | Length Required | This error occurs when a POST/PUT request is made without Content-Length header. | Add Content-Length header if missing. If no request body is present, send Content-Length as 0. |
| 415 | Unsupported Media Type | Incorrect/unsupported payload format | Check the following header information:Content-TypeAcceptNote: Refer to the respective API documentation on the developer portal for the correct header information |
| 421 | Misdirected Request | The API key and the environment do not match. | Check the API key and the environment it is mapped against. For instance, a key issued for Prod2, won't work for Prod3 product |
| 429 | Too Many Requests | The request cannot be processed due to too many requests jamming the serverThis is mainly due to exceeding the set call rate limit | It is recommended to wait for the rate limit to reset |

### `500s - Server-Related Errors`











| Status Code | Status | Possible Reasons | Recommended Solution |
| --- | --- | --- | --- |
| 500 | Internal Server error | Server related issue. Generally, this issue gets resolved on its own with time | Reach out to integration support  team if the issue persists after multiple attempts |
| 503 | Service Unavailable | The server is not ready to process the requestScheduled maintenance could be one of the reasons | Retry after some time. If the issue persists after multiple attempts, consult the integration support team |
| 504 | Gateway Timeout | The server, which is acting as a gateway is unable to fetch a timely response | Retry after some time. If the issue persists after multiple attempts, consult the integration support team |

 [](https://dev.sprinklr.com/rest-api-error-and-status-codes)




[Back to top](https://dev.sprinklr.com/rest-api-error-and-status-codes)
