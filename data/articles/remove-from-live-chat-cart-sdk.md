---
title: "Remove from Live Chat Cart SDK"
slug: remove-from-live-chat-cart-sdk
url: https://dev.sprinklr.com/remove-from-live-chat-cart-sdk
---

# Remove from Live Chat Cart SDK

# Remove from Live Chat Cart SDK

The Remove from Cart SDK allows brands to track when customers remove products from their shopping cart. This interaction can be linked to Live Chat sessions, enabling brands to identify potential drop-off points, trigger timely interventions, or personalize future engagements based on cart behavior.


You can call this SDK method whenever an item is removed from the cart, to ensure the system reflects an accurate cart state.

## Method

`sprChat('removeFromCart', {});`

## Parameters
































| Parameter | Type | Description |
| --- | --- | --- |
| productItems | Array | List of products currently in the cart. Each item contains product details. |
| sku | String | Title or name related to the SKU. |
| quantity | Number | Count of the product. |
| modifiedTime | Epoch (Unix Timestamp) | The timestamp of the last cart update in epoch format (milliseconds). |

## Example

The following example captures the product details purchased by a customer:




  Copy Code



window.sprChat('removeFromCart', {
	productItems: [{
		sku: 'SKU2',
		quantity: 1,
	}],
	modifiedTime: 1623907882055 // timestamp when cart was modified
})





[](https://dev.sprinklr.com/remove-from-live-chat-cart-sdk)

[Back to top](https://dev.sprinklr.com/remove-from-live-chat-cart-sdk)
