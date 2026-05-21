---
title: "Media Asset Security v1"
slug: media-asset-security-v1
url: https://dev.sprinklr.com/media-asset-security-v1
---

# Media Asset Security v1

#  GET Media Asset Security v1

This API call helps generate a publicly accessible URL for facilitating asset download. You can use the url received in the API response to download and access secure media content.

**Dev Notes: **The default expiry time for the publicly accessible URL is 90 minutes. However, the expiry time can be configured based on one's requirements.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/secure-assets/fetch/{url}

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

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| url | Required | Refers to the secure url for Sprinklr media asset (image, video, PDFs, etc.)Note: The url should be url-encoded. | url |

**Dev Notes: **Kindly reach out to [Sprinklr support](mailto:tickets@sprinklr.com) for enabling the media asset security feature.

### Example - Request




 Copy Code


curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/secure-assets/fetch/https%3A%2F%2Fprod-cdata-secure.sprinklr.com%2FDAM%2F787%2Fced2570c-a621-4f1e-ad47-3934af631d81-1620971477%2Fpreview_image_0-8401e0c2-0d8d-.png' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



### Example - Response




"https://s3.amazonaws.com/prod-cdata-secure.sprinklr.com/DAM/787/ced2570c-a621-4f1e-ad47-3934af631d81-1620971477/preview_image_0-8401e0c2-0d8d-.png?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLWVhc3QtMSJGMEQCIDJ%2FRmw8sAcb7wjksRw8REyxGkJYYYodBOKPGuii8r3pAiBaUTBIMKmitxneAG37QvahAxGeN8Ouy06kw2%2FKD2VyAirMBAh2EAAaDDg2OTM2NzQ3MTY3NCIMWZzg6FjjR1tkaMaDKqkESuHaE68OWuwlUcAxHq0YJwA82eEhE3YKQrNz6t%2BlI%2B3UamT%2BtRP3KT97yrtLbzocbP3zFBpWQ3mhiTSBsG3n92sufYAix9pEnl3ZRzlUHOK80xxpET1QNyygPyMtACz4luU2x7M%2FzDWFZ52Ru13PuAOcxUvxxa6q6UxGKZztMod4GtvdxtbjBqibog458AwuwSlH1CsejDNRWc%2B3%2B6aM5GuIMs%2B5MEBxp9NBk62QuM6nsV6eQ1PkwSXwBSbrX7W2CWsNevhoCMW0vtnLjcWcbiJ%2BV6fsYgaXgbehg0QsDLz7SSXaIBq%2FzH6TxkcMWjt1Kez9MKH6j3a6o4juOINblv5fvtro%2F58Rd4MkQG0F%2F4B65SVuM5eZIXKRuHSnANpLCCI%2FoG5z8g0X8Dqj6oQKpYqjEFcp%2B86tmolVr7aLnqHnVzalBtda8pKZfWB%2FeNPZ%2BF7Y3npcotTCD2g14GXkH%2BSpB79UOCbRfAIsTaQ3i%2BRXLP2Bq%2Ff8mrvpw6UmQPFHKNRtvQW%2BmPGZdPSsoAGNiK3OAmBi4pifMU5nEh3ijd8CPSU2LBIbHpk6El2nyglyPOxBikj3qBrwiFFpgXQWvbKodkuyctrN4I35osPIjsub6b4SIv3Pr7aJwEl%2FCOTWTrNOwV%2FGGp%2Bx5ZbGkVr5wpr8MTtBJtEL%2BfKfKXxD%2BjVy8wt0PEE3MUfQkJk1FclcxerhsRJxn1aNsZwExb8%2ByKW2N2XcVML2KDDQ4LObBjqqAdapebVBDqeTeWrJHQ1bx%2BHXhCaX%2FJh18Gppj7nT0gmdRvZ9JQ67hRdE3WVdq%2FzsErTpYHuOHpzRItoSjmj2UD%2BG7%2FmxQuz10XXbFw%2Bf0ay24P4IJgl88mBJyO8L9YAMnvoJW8u9wxL64wgfEjI6cia8iwiwX5LccfL98awVUngff%2FNeUSzY18LooQ4p7PHzKwk4zhZ1nEdjqdjUGKJJOKNJrqClOynhcTnN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221110T134222Z&X-Amz-SignedHeaders=host&X-Amz-Expires=5400&X-Amz-Credential=ASIA4U2SW3Y5LYJFNQVT%2F20221110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=642328d0d3d7394357d90e9cc8ee17bd6bcd4d6b967d12d4e60ddc806d31d927"



[](https://dev.sprinklr.com/media-asset-security-v1) 

 

 
[Back to top](https://dev.sprinklr.com/media-asset-security-v1)
