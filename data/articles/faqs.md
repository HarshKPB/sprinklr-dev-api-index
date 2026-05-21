---
title: "FAQs"
slug: faqs
url: https://dev.sprinklr.com/faqs
---

# FAQs

#
FAQs


Sprinklr provides robust RESTful web service APIs to integrate data with any external system. The integration uses JSON as a data-interchange format and intuitive resource URLs to run API requests.

Adding new APIs to our [developer portal](https://spr-apigee-prod-apiprodportal.apigee.io/) is an ongoing process. The [changelog section](https://dev.sprinklr.com/changelog) documents all the APIs recently added to the developer portal.

**HTTP REST API Methods**

- **POST**: To create a new resource (includes request body)
- **GET**: To fetch the details associated with a resource
- **PUT**: To update the resource (includes request body)
- **PATCH**: To partially update a resource (includes request body)
- **DELETE**: To delete an existing resource

Before we process further with the FAQs, here’s an overview of common terms used across APIs:

## What is an API?

API stands for application programming interface that allows communication between two software applications. Through an API, a request is sent to the server, which fetches the requested data and returns it as a response.

## What is a REST API?

REST stands for representational state transfer, which is an architectural style for an API (Application Programming Interface) that allows accessing Sprinklr’s data without accessing Sprinklr’s platform.

You can access and use Sprinklr’s resources through simple HTTP requests using required headers such as authentication token, key, and content-type.

## What is JSON?

JavaScript Object Notation is a data-interchange format that uses human-readable code for running API requests consisting of objects, attribute-value pairs, and arrays. JSON is used by Sprinklr to send data from our server to the client’s web page.

The API requests available on the developer portal are JSON requests and responses.

## What is a Webhook?

Webhooks are created to notify the customer about any events that take place on their Sprinklr account. Sprinklr uses webhooks to provide real-time updates regarding any changes in applications.

## API Related FAQs

### 1. Why do we use OAuth Authentication for APIs?

The Sprinklr API is designed with a scalable SaaS model, and we utilize industry-standard OAuth protocol as the authentication/authorization standard. It is the latest and more secure authentication process followed across the industry.

### 2. Is it Necessary to Register an Account on the Developer Portal for Accessing APIs?

To access Sprinklr APIs, the first step is to generate the API key. To get started, you are required to [register](https://dev.sprinklr.com/developer-portal-registration) as a user on the developer portal.

### 3. Is Sprinklr Platform Access Necessary to Use Sprinklr APIs?

Sprinklr’s platform access is required to complete the OAuth flow when generating the authorization token.

### 4. Can you Reset the Password and Email for your Developer Account?

Yes, it is possible to reset the username or password for your dev portal account. To accomplish this sign-in to your dev portal account. Navigate to `My Account` section and click on `Manage Account`. You can chane email or password form here.

### 5. What External Tools can we Use for API Testing?

Postman is a go-to tool that can be used for API testing. Refer to Postman’s learning center for more information on using Postman.

### 6. What is the API rate limit at Sprinklr?

By default, a customer can run up to 1000 calls in an hour and 10 calls per second. This rate limit is defined to control API usage and prevent server overload. If the user exceeds the rate limit, you will receive a 403 “Developer Over Rate” error message. You may also receive alert stating that the API Bundle key has gone over its throttle limit

However, this API call limit can be increased based on the use case and the brand’s contractual limits. Please reach out to your success manager to raise the API call limit increase request.

### 7. How to Generate Key and Authorization Token?

Here’s a link to the resource that lists the step-by-step process to generate a key and a token:

[Generate key and authorization token](https://dev.sprinklr.com/api-key-and-secret-generation)

### 8. What Does it Mean to Refresh the Authorization Token?

The token expires after a given time. To continue running the APIs, refreshing the token is required. Refer to [refreshing access token](https://dev.sprinklr.com/refreshing-access-token) documentation for more details.

### 9. What are the Different Webhook Types Supported by Sprinklr?

The different webhook types supported by Sprinklr can be accessed using the Fetch Webhooks types API.

### 10. What is an API Extension?

An API extension automates the interaction between Sprinklr and any third-party web service. By building an API extension, the third-party web service features get automatically integrated with Sprinklr using the open API specification that defines what the API can do.

### 11. What is a Sandbox Environment?

Sandbox is a testing environment, which is independent of the live production environment. It can be used for implementation, training, development, and testing. Having access to the Sandbox environment prevents human error, and makes it easy to test and try new capabilities and product features. Sprinklr Sandbox supports all the APIs available on the developer portal.

### 12. Why is Twitter Data Not Accessible via APIs?

To access Twitter APIs, developers are required to inform Twitter how they intend to use Twitter APIs and Twitter Content. Twitter has an internal process for evaluating requests to determine whether the corresponding use cases are consistent with Twitter’s policies.

### 13. What is a Production Environment in Sprinklr?

The production environment enlists all the current versions of the application that are accessible to the customers. Every customer is given access to one of the released environments, which include: PROD, PROD2, PROD3, PROD4, PROD8, etc.

Customers need to know their environment as it is an essential parameter for:

- Registering application (key generation)
- Generating access token
- Running API requests

### 14. Can the Generated Key be Used for All the Environments?

No, the key is environment-specific. A key needs to be generated every time a new environment is accessed.

### 15. Can you monitor the number of API calls made Over Time?

Yes, you can monitor the number of API calls made by a customer over time. To request this data, reach out to the integrations team along with following information:

- API Key/s
- The time range for which you need the data

### 16. What are the most prominent status codes received in a response?

- **Status in <200s>**: Success

- **Status in <400s>**: Error associated with the provided information

- **Status in <500s>**: Sprinklr’s server error

For more details refer to [REST API Error and Status Codes](https://dev.sprinklr.com/rest-api-error-and-status-codes) documentation.

### 17. What are the Different Types of Supported Authorization Processes?

The different authorization processes supported by Sprinklr, include:

- **OAuth 2.0 for Customers**: This is the most common type of authentication required to run an API call. This process involves generating an authorization_code before making an API call to generate the authorization token. Refer [here](https://dev.sprinklr.com/oauth-2-0-for-customers) for more details.

- **OAuth 2.0 - For Partners**: If you are a partner, you need to authenticate using the SSO for partners. Refer [here](https://dev.sprinklr.com/oauth-2-0-for-partners) for the step-by-step process.

- **Client Credentials Grant Type**: This type of authentication allows generating the authorization token without generating the code. A default user needs to be set at the backend, and you can create a token using client_id (API key) and client secret (API secret). Refer [here](https://dev.sprinklr.com/client-credentials-get) for more details.

### 18. What are the best practices for migrating from v1 to v2?

Some of the best practices for migrating from v1 to v2 include:

- The same API key and authorization token that you generated for v1, will work fine for all the v2 endpoints

- Refer to the respective v2 documentations for endpoint and payload details that need to be modified.

### 19. How to Fetch the API Request Payload for Reporting APIs?

Here’s the step-by-step process to generate the API request payload for reporting dashboards:

- Create a user-based role and grant the “Generate Widget API Payload” permission.

- Go to the desired reporting dashboard and click on the three dots appearing in the top right corner

- Select the “Generate API v2 Payload” option and copy the code block

- Make the API call using the extracted payload and appropriate headers
For more details, refer to the [Generate API v2 Payload](https://www.sprinklr.com/help/articles/integration-guides/generate-api-v2-payload/633c5ca8a0522e093b06c1a2) knowledge portal article.

### 20. Where Can I learn about Sprinklr’s features?

You can refer to Sprinklr’s [Knowledge portal](https://sprinklr.com/help) articles to understand the use cases and working of different platform features.
  [](https://dev.sprinklr.com/faqs)




[Back to top](https://dev.sprinklr.com/faqs)
