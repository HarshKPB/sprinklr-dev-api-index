---
title: "Secure Media Download - Bulk"
slug: secure-media-download-bulk
url: https://dev.sprinklr.com/secure-media-download-bulk
---

# Secure Media Download - Bulk

#
  POST - Secure Media Download - Bulk

Using this API, you can create accessible URLs from the given secure URLs. The use-case of this API is two-fold:

- Going forward, all the secure URLs received in the API can be passed in the API to generate time-bound accessible URLs

- The existing media URLs at your end that are no longer accessible can be passed in the API to generate the time-bound accessible URLs

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/secure-assets/bulk/fetch

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

### Request Parameters - List of URLs

| Required/Optional | Description | Type |
| --- | --- | --- |
| Required | Refers to the list of secure urls for Sprinklr media assets (image, video, audio, PDFs, etc.) | List [String] |

### Example - Request




 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/secure-assets/bulk/fetch' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
  -d '[
    "https://storage.googleapis.com/spr-qa6-cdata/66000000/SALESFORCE/6634956c939a1270cef75e2b/LEAD",
    "https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/e8795230-6404-4d01-a7cd-16b21da894a1-2032016103/36f1061b-b2da-4c4f-9598-7628a9.jpg"
]'
 

     
     
   

### Example - Response




{
    "data": {
        "https://storage.googleapis.com/spr-qa6-cdata/66000000/SALESFORCE/6634956c939a1270cef75e2b/LEAD": "https://storage.googleapis.com/spr-qa6-cdata/66000000/SALESFORCE/6634956c939a1270cef75e2b/LEAD",
        "https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/e8795230-6404-4d01-a7cd-16b21da894a1-2032016103/36f1061b-b2da-4c4f-9598-7628a9.jpg": "https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/e8795230-6404-4d01-a7cd-16b21da894a1-2032016103/36f1061b-b2da-4c4f-9598-7628a9.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gke-worker%40gc-qa6.iam.gserviceaccount.com%2F20240507%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240507T133728Z&X-Goog-Expires=5400&X-Goog-SignedHeaders=host&X-Goog-Signature=0f899d6ebddbc361f944963cfa28b34ae620e00d5a730cbf597078833e1d339a2d5334144bfe23692df4276380819a02264abaff2b5a2b770832393eb252704df76f0bb051703a40eb3daa1b78076568f6cd4bbbc4a1844ebf7d01f5b4c26d264b663bfc6383e148bf1753ba42adf0fe1138285c8a0a36a2a1c463a2bde82e34addc7d70ccbb041445f47a1820541bb751b95ecd891aad8be4f0ac737e16285a7f286a4c78caad7088f88f66702e3c0626177063e875f67b111e53f1db851c50b809e1d26686a474e6da44980844f74b0f1310fbd1f9b08fb29ed3979b55ae20d2f434d2de6b2181815e2c1a25463d15dd5d0545e8cca482fd52124f66d69c8a"
    },
    "errors": []
}
 

     
     
   

**Dev Notes: **The url generated in the response will be accessible for a limited time period. Once the above link expires, you can either regenerate the accessible URL by calling the API mentioned above.

[](https://dev.sprinklr.com/secure-media-download-bulk) 

 

 
[Back to top](https://dev.sprinklr.com/secure-media-download-bulk)
