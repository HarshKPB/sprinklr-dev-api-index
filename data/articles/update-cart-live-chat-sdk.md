---
title: "Update Cart Live Chat SDK"
slug: update-cart-live-chat-sdk
url: https://dev.sprinklr.com/update-cart-live-chat-sdk
---

# Update Cart Live Chat SDK

#
Update Cart Live Chat SDK

The Update Cart SDK allows brands to track customer interactions with their shopping cart in real-time and associate those interactions with Live Chat conversations. With this SDK, brands can monitor potential leads and identify completed purchases. You can call this SDK whenever the cart page is loaded, or the cart is updated on the cart page.

## Method

`sprChat('updateCart', {})`

## Parameters






































































































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sku | Required | The Stock Keeping Unit (SKU) of the product. | String |
| standardPrice | Required | The standard price of the product. | Double |
| quantity | Required | The quantity of the product in the cart. Default value is 1. | Integer |
| standardCurrency | Optional | The currency used for the product price. For example, SGD for Singapore dollars. | String |
| title | Optional | The title or name of the product. | String |
| description | Optional | A description of the product. | String |
| productSpecification | Optional | A map containing the specifications of the product. For example, size, color. | Map<String, String> |
| discount | Optional | The discount applied to the product. | Double |
| productCategory | Optional | The category of the product. For example, electronics, clothing. | String |
| modifiedTime | Optional | The timestamp when the cart was last modified. | Long |
| purchased | Optional | Indicates whether the product has been purchased. | Boolean |
| cartDiscount | Optional | The discount applied to the entire cart. | Double |
| shippingAmount | Optional | The shipping cost for the cart | Double |
| taxAmount | Optional | The tax applied to the cart. | Double |
| orderId | Optional | The unique identifier for the order. | String |

## Example


The following example shows the details captured when a product is purchased by a customer:





 Copy Code


window.sprChat('updateCart', {
  productItems: [{
    sku: 'XXX',
    quantity: 2,
    standardPrice: 500.0,
    discount: 5,
    standardCurrency: 'SGD',
    title: 'SRF5700BD French Door Refrigerator',
    description: 'XXX',
    productCategory: 'XXX',
    productSpecification: {
      pviSubType: 'yyy',
      modelCode: 'yyy',
      skuTitle: 'yyy',
      pviType: 'zzz'
},
}, ],
  purchased: true,
  cartDiscount: 12,
  orderId: 9611502,
  shippingAmount: 30,
  taxAmount: 4,
  modifiedTime: 1737528378000
})
 

     
     
   

	[](https://dev.sprinklr.com/update-cart-live-chat-sdk) 

 

 
[Back to top](https://dev.sprinklr.com/update-cart-live-chat-sdk)
