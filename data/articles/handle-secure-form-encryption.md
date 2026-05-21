---
title: "Handle Secure Form Encryption"
slug: handle-secure-form-encryption
url: https://dev.sprinklr.com/handle-secure-form-encryption
---

# Handle Secure Form Encryption

# Handle Secure Form Encryption

You can create [secure forms](https://www.sprinklr.com/help/articles/pci-compliant-secure-forms/configuration-of-secure-forms/63d3ce7f2c015d03d4e7fb3d#fd964d21-0620-4fe9-b069-99f14ce47140) to be sent in Live Chat conversations. Secure forms provide agents a way to collect sensitive data confidentially and securely during a Live Chat conversation. For example, customers might need to enter their credit card details for a case.

The captured data can then be sent to Sprinklr in either encrypted or unencrypted format using the **handleSecureFormEncryption** SDK method. The method takes a response object and a callback function as parameters. Within the callback, you can return a map of field names and their encrypted or unencrypted values.

## Method




  Copy Code



function handleSecureFormEncryption({ response: { data }, cb) => {
/*
* data: {
* actionId: string; // configure it in submit button to uniquely identify which form is submitted
* actionPayload: {
* fields: {}; // all configured field come here
* values: {}; // map of fieldName vs values
* },
* contextId: string; // conversationId
* }
*/
if (data) {
// here run the encryption logic & then call callback with required structure
// if encryption is run successfully then call with -
cb({
encryptedData: {
// map of fieldName vs encrypted values
},
unencryptedData: {
// map of fieldName vs unencrypted values
// values that are not being encrypted should be returned as it is
}
});
// if encryption is failed then call with -
cb(null, error);
}
}
sprChat('subScriberToUpdate', {
topic: 'externalCallback',
subscriber: handleSecureFormEncryption,
});






In the code snippet above, the **data** block contains the information captured from the secure form. This is the data that you need to capture and process.




  Copy Code



/*
* data: {
* actionId: string; // configure it in submit button to uniquely identify which form is submitted
* actionPayload: {
* fields: {}; // all configured field come here
* values: {}; // map of fieldName vs values
* },
* contextId: string; // conversationId
* }
*/






## Parameters





































| Parameter | Type | Description |
| --- | --- | --- |
| actionId | String | A unique identifier for the submitted form. Configure it in the Submit button. |
| actionPayload | Object | Contains form-related data, including configured fields and submitted values. |
| fields | Object | A collection of all configured form fields. |
| values | Object | A key-value map of field names and their corresponding submitted values. |
| contextId | String | A unique identifier representing the conversation or session in which the form was submitted. |


In the **if** block, define the logic that will determine when the callback should be triggered. In the **callback** function, pass a map of field names and their corresponding encrypted or unencrypted values.





  Copy Code



function handleSecureFormEncryption({ response: { data }, cb) => {
if (data) {
// here run the encryption logic & then call callback with required structure
// if encryption is run successfully then call with -
cb({
encryptedData: {
// map of fieldName vs encrypted values
},
unencryptedData: {
// map of fieldName vs unencrypted values
// values that are not being encrypted should be returned as it is
}
});
// if encryption is failed then call with -
cb(null, error);
}
}
sprChat('subScriberToUpdate', {
topic: 'externalCallback',
subscriber: handleSecureFormEncryption,
});






## Parameters
































| Parameter | Type | Description |
| --- | --- | --- |
| encryptedData | Object | A map containing field names and their corresponding encrypted values. |
| unencryptedData | Object | A map containing field names and their original values (values that are not encrypted remain unchanged). |
| topic | String | The event name for which the subscriber is registered. |
| subscriber | Function | The function (`handleSecureFormEncryption`) to which you are subscribed. |


## Example




  Copy Code



function onEventTriggered(event, cb) {
   console.log('external event =>', event);
   cb({
       encryptedData: {"361bbc15-dff2-4864-b177-5b9b0e6ed4a9": 'euhfbhvj',
"928a90cd-2d19-479f-8410-817e58af33ed":'twedfsdf@xycs.dfsd'},
unencryptedData: {"85cf5fb9-7738-47ef-9616-7da4566f01dc":'Bengaluru'}
   }, null)
}
window.sprChat('subscribeToUpdate', {
   topic: 'externalCallback',
   subscriber: onEventTriggered,
});





[](https://dev.sprinklr.com/handle-secure-form-encryption)

[Back to top](https://dev.sprinklr.com/handle-secure-form-encryption)
