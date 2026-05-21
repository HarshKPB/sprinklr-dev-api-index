---
title: "Campaign Webhooks"
slug: campaign-webhooks
url: https://dev.sprinklr.com/campaign-webhooks
---

# Campaign Webhooks

# Campaign Webhooks

**Campaign Webhook Subscriptions:**
 Campaign Created, Campaign Updated and Campaign Deleted

Whenever an action is performed on Campaign either via Sprinklr UI or API, the webhook notification are triggered with the details that are described in the following documents:


- [Campaign.Created Webhook](https://dev.sprinklr.com/campaign-webhooks#campaignCreate)

- [Campaign.Updated Webhook](https://dev.sprinklr.com/campaign-webhooks#campaignUpdate)

- [Campaign.Deleted Webhook](https://dev.sprinklr.com/campaign-webhooks#campaignDelete)

### Campaign.Created Webhook





  Copy Code



{
  "id": "5f64dd6f8da9504494f77987",
  "type": "campaign.created",
  "payload": {
    "id": "4700_669",
    "name": "Private Campaign SAM",
    "createdTime": 1600445807446,
    "modifiedTime": 1600445807445,
    "startDate": 1600445790370,
    "owner": 93487,
    "partnerCustomProperties": {},
    "clientCustomProperties": {
      "5ad47904e4b09fb8b0324df7": [
        "a"
      ]
    },
    "status": "APPROVED",
    "archived": false
  },
  "eventTime": 1600445807642,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Campaign.Updated Webhook




  Copy Code



{
  "id": "5f6482719d0ae36ae1886898",
  "type": "campaign.updated",
  "payload": {
    "id": "4700_680",
    "name": "Com",
    "createdTime": 1547748785789,
    "modifiedTime": 1547748785787,
    "startDate": 1547748780381,
    "owner": 96465,
    "partnerCustomProperties": {
      "spr_campaign_goal": [
        "Increase awareness"
      ],
      "5932d3cbe4b0521fb6f6b8b2": [
        "-19800000"
      ],
      "580df8d9e4b03733055538c8": [
        "Option1"
      ]
    },
    "clientCustomProperties": {
      "564a81aa3da2a01af2000000": [
        "1447785000000"
      ],
      "58838ca3e4b0b25c5781adb8": [
        "57e4f7cfe4b01a6425a24a95"
      ]
    },
    "status": "APPROVED",
    "archived": false
  },
  "eventTime": 1600422513690,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Campaign.Deleted Webhook




  Copy Code



{
  "id": "5f64826f9d0ae36ae18859ed",
  "type": "campaign.deleted",
  "payload": "4700_1",
  "eventTime": 1600422511077,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





## Response Definition













































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id of the campaign. | String |
| name | Name of the campaign. | String |
| description | Description of campaign. | String |
| createdTime | Campaign created time in Sprinklr. | Integer |
| modifiedTime | last modified time of campaign in Sprinklr. | Integer |
| startDate | Start date of campaign. | integer |
| endDate | End date of campaign. | integer |
| tags | Tags on the campaign. | String |
| owner | User Id of the campaign owner. | Integer |
| status | Status of the campaign. e.g. Draft, Approved. | String |
| archived | True if campaign is archived. 			default: false | Boolean |
| partnerCustomFields | Partner level custom fields on the campaign. | String |
| clientCustomFields | Partner level custom fields on the campaign. | String |

[](https://dev.sprinklr.com/campaign-webhooks)

[Back to top](https://dev.sprinklr.com/campaign-webhooks)
