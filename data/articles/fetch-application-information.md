---
title: "Fetch Application Information"
slug: fetch-application-information
url: https://dev.sprinklr.com/fetch-application-information
---

# Fetch Application Information

#   POST Fetch Application Information
 

This API allows you to get the application information for a given ad account on a specific channel.


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/appInfos/`{app_id}`

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

## Path Parameter
















| Parameter | Description | Type |
| --- | --- | --- |
| {app_id} | Id of the application associated with the ads account. | String |

### Steps to Retrieve the Application Id

You can retrieve the Application Id by using your browser’s developer tools to inspect the Sprinklr UI.

Follow these steps to retrieve the Application Id:


- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Marketing** > **Advertising** tab.

- Under **Execute** > **Ads Compositions**, click **Ads Composer**. This opens the Create New Paid Initiative page.

- On the Create New Paid Initiative tab, select a Facebook Ads account.

- On the configuration page, choose the **App Promotion** objective.

- Select the app whose application Id you want to retrieve.

- Open your browser’s developer tools and go to the **Network** tab to observe network activity.


## Request Parameters














****






[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-application-information#account_user_id)







****

- [Facebook Ad Objectives](https://dev.sprinklr.com/fetch-application-information#fb_ad_objective)
- [LinkedIn Ad Objectives](https://dev.sprinklr.com/fetch-application-information#linkedinAdObjectives)
- [X Ad Objectives](https://dev.sprinklr.com/fetch-application-information#xAdObjectives)






****










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| channelType | Required | The type of channel         Supported Values: FACEBOOK, LINKEDIN, X | String |
| accountUserId | Required | Id for the ad account 				See | String |
| adObjective | Optional | The objective of the advertisement campaign.Supported Values: | String |
| storeType | Optional | The type of app store. Supported Values: GOOGLE_PLAY, ITUNES, FB_CANVAS, AMAZON_APP_STORE, ITUNES_IPAD, WINDOWS_10_STORE, FB_INSTANT_GAME | String |
| isIOS14Campaign | Optional | Indicates if the campaign is targeted for iOS 14 | Boolean |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

### Facebook Channel Ad Objectives

The following table lists the supported ad objectives for Facebook (value for `adObjective` parameter):


















































| Enum | Label |
| --- | --- |
| OUTCOME_AWARENESS | Facebook Awareness |
| OUTCOME_TRAFFIC | Facebook Traffic |
| OUTCOME_ENGAGEMENT | Facebook Engagement |
| OUTCOME_LEADS | Facebook Leads |
| OUTCOME_SALES | Facebook Sales |
| OUTCOME_APP_PROMOTION | Facebook App Promotion |
| MESSAGES | Facebook Messages |
| CONVERSIONS | Facebook Conversions |
| CATALOG_SALES | Facebook Catalog Sales |
| STORE_VISITS | Facebook Store Visits |


### LinkedIn Channel Ad Objectives

The following table lists the supported ad objectives for LinkedIn (value for adObjective parameter).






































| Ad Objective | Label |
| --- | --- |
| LINKEDIN_WEBSITE_VISIT | Website Visit |
| LINKEDIN_BRAND_AWARENESS | Brand Awareness |
| LINKEDIN_LEAD_GENERATION | Lead Generation |
| LINKEDIN_ENGAGEMENT | Engagement |
| LINKEDIN_VIDEO_VIEWS | Video Views |
| LINKEDIN_JOB_APPLICANT | Job Applicant |
| LINKEDIN_WEB_CONVERSION | Web Conversion |

### X (Twitter) Channel Ad Objectives

The following table lists the supported ad objectives for X (value for adObjective parameter).










































| Ad Objective | Label |
| --- | --- |
| PROMOTED_TWEETS | X Engagements |
| TWITTER_AWARENESS | X Reach |
| TWITTER_WEBSITE_CLICKS | X Website Traffic |
| PROMOTED_ACCOUNTS | X Followers |
| TWITTER_VIDEO_VIEWS | X Video Views |
| TWITTER_PREROLL_VIEWS | X Preroll Views |
| TWITTER_APP_INSTALLS | X App Installs |
| TWITTER_APP_ENGAGEMENTS | X App Re Engagements |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/appInfos/66122206' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}'\
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "channelType": "FACEBOOK",
    "accountUserId": "394232028806869",
    "adObjective": "OUTCOME_TRAFFIC"
}'



## Example - Response





{
    "data": {
        "responseEntities": [
            {
                "id": "FACEBOOK_APPLICATION_3665041457091301_66122206",
                "appId": "3665041457091301",
                "adChannelAppId": "3665041457091301",
                "storeUrl": "http://www.facebook.com/gaming/play/3665041457091301/",
                "sellerName": "Sprinklr QA ads 2.0",
                "sellerUrl": "https://www.facebook.com/games/?app_id=3665041457091301",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_699784085061770_66122206",
                "appId": "699784085061770",
                "adChannelAppId": "699784085061770",
                "storeUrl": "http://www.facebook.com/gaming/play/699784085061770/",
                "sellerName": "spr_app_acme",
                "sellerUrl": "http://www.sprinklr.com/",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_493673020768393_66122206",
                "appId": "493673020768393",
                "adChannelAppId": "493673020768393",
                "storeUrl": "http://www.facebook.com/gaming/play/493673020768393/",
                "sellerName": "Sprinklr QA Ads",
                "sellerUrl": "https://space-qa4.sprinklr.com/",
                "sellerIconImageUrl": "https://scontent-bom1-1.xx.fbcdn.net/v/t39.2081-6/12057046_678054898996870_1536711862_n.png?stp=c0.0.129.129a_dst-png_p128x128&_nc_cat=104&ccb=1-7&_nc_sid=ed3f67&_nc_ohc=ZSrMZVBu5nAQ7kNvwGruxei&_nc_oc=AdkYUvP_g7GBp8ztZtkzaDt4xl1qanJAGikjL9pgzZgUaTy7Fv0ax1GjYBGB-Nn6ykc&_nc_zt=14&_nc_ht=scontent-bom1-1.xx&edm=ABE7cloEAAAA&_nc_gid=qu0erlR140sVeW_G00H7jg&oh=00_AfVhDo_oUUonUObZ4q_kv6FMaK2VWs-WyA9FiL8l1qEgQw&oe=689A7F01",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_493673020768393_66122206",
                "appId": "493673020768393",
                "adChannelAppId": "493673020768393",
                "storeUrl": "http://itunes.apple.com/app/id1369693945",
                "sellerName": "Sprinklr QA Ads",
                "sellerUrl": "https://space-qa4.sprinklr.com/",
                "sellerIconImageUrl": "https://scontent-bom1-1.xx.fbcdn.net/v/t39.2081-6/12057046_678054898996870_1536711862_n.png?stp=c0.0.129.129a_dst-png_p128x128&_nc_cat=104&ccb=1-7&_nc_sid=ed3f67&_nc_ohc=ZSrMZVBu5nAQ7kNvwGruxei&_nc_oc=AdkYUvP_g7GBp8ztZtkzaDt4xl1qanJAGikjL9pgzZgUaTy7Fv0ax1GjYBGB-Nn6ykc&_nc_zt=14&_nc_ht=scontent-bom1-1.xx&edm=ABE7cloEAAAA&_nc_gid=qu0erlR140sVeW_G00H7jg&oh=00_AfVhDo_oUUonUObZ4q_kv6FMaK2VWs-WyA9FiL8l1qEgQw&oe=689A7F01",
                "store": "itunes"
            },
            {
                "id": "FACEBOOK_APPLICATION_422187154197303_66122206",
                "appId": "422187154197303",
                "adChannelAppId": "422187154197303",
                "storeUrl": "http://www.facebook.com/gaming/play/422187154197303/",
                "sellerName": "palash test",
                "sellerUrl": "https://www.facebook.com/games/?app_id=422187154197303",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_442881388253546_66122206",
                "appId": "442881388253546",
                "adChannelAppId": "442881388253546",
                "storeUrl": "http://www.facebook.com/gaming/play/442881388253546/",
                "sellerName": "SysApp",
                "sellerUrl": "https://www.facebook.com/games/?app_id=442881388253546",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_1352383449198993_66122206",
                "appId": "1352383449198993",
                "adChannelAppId": "1352383449198993",
                "storeUrl": "http://www.facebook.com/gaming/play/1352383449198993/",
                "sellerName": "Sprinklr Android App",
                "sellerUrl": "https://www.facebook.com/games/?app_id=1352383449198993",
                "sellerIconImageUrl": "https://scontent-bom1-1.xx.fbcdn.net/v/t39.2081-6/503477887_1352386859198652_604851243039913503_n.jpg?stp=c0.0.129.129a_dst-jpg_p128x128_tt6&_nc_cat=107&ccb=1-7&_nc_sid=ed3f67&_nc_ohc=IIn2ZTNzMWgQ7kNvwHe0u2i&_nc_oc=Adk0PLkYsXp2W_1rpTPzTo6AnYn6jXWPMRN9IM5oa8argZ-UeL5UOmcrSakCDmEJJEY&_nc_zt=14&_nc_ht=scontent-bom1-1.xx&edm=ABE7cloEAAAA&_nc_gid=qu0erlR140sVeW_G00H7jg&oh=00_AfUCMHAiwTrHqXT1BhvgrVp-OAEh4DIkPZ9KDeKe3j9_rQ&oe=689A9F64",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_1352383449198993_66122206",
                "appId": "1352383449198993",
                "adChannelAppId": "1352383449198993",
                "storeUrl": "http://play.google.com/store/apps/details?id=com.sprinklr.SprinklrAndroidApp",
                "sellerName": "Sprinklr Android App",
                "sellerUrl": "https://www.facebook.com/games/?app_id=1352383449198993",
                "sellerIconImageUrl": "https://scontent-bom1-1.xx.fbcdn.net/v/t39.2081-6/503477887_1352386859198652_604851243039913503_n.jpg?stp=c0.0.129.129a_dst-jpg_p128x128_tt6&_nc_cat=107&ccb=1-7&_nc_sid=ed3f67&_nc_ohc=IIn2ZTNzMWgQ7kNvwHe0u2i&_nc_oc=Adk0PLkYsXp2W_1rpTPzTo6AnYn6jXWPMRN9IM5oa8argZ-UeL5UOmcrSakCDmEJJEY&_nc_zt=14&_nc_ht=scontent-bom1-1.xx&edm=ABE7cloEAAAA&_nc_gid=qu0erlR140sVeW_G00H7jg&oh=00_AfUCMHAiwTrHqXT1BhvgrVp-OAEh4DIkPZ9KDeKe3j9_rQ&oe=689A9F64",
                "store": "google_play"
            },
            {
                "id": "FACEBOOK_APPLICATION_1449437989616482_66122206",
                "appId": "1449437989616482",
                "adChannelAppId": "1449437989616482",
                "storeUrl": "http://www.facebook.com/gaming/play/1449437989616482/",
                "sellerName": "spr ios app",
                "sellerUrl": "https://www.facebook.com/games/?app_id=1449437989616482",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_716218757712157_66122206",
                "appId": "716218757712157",
                "adChannelAppId": "716218757712157",
                "storeUrl": "http://www.facebook.com/gaming/play/716218757712157/",
                "sellerName": "Sprinklr IOS ADD",
                "sellerUrl": "https://www.facebook.com/games/?app_id=716218757712157",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_733601259832278_66122206",
                "appId": "733601259832278",
                "adChannelAppId": "733601259832278",
                "storeUrl": "http://www.facebook.com/gaming/play/733601259832278/",
                "sellerName": "Sprinklr IOS APP",
                "sellerUrl": "https://www.facebook.com/games/?app_id=733601259832278",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_2505127933219497_66122206",
                "appId": "2505127933219497",
                "adChannelAppId": "2505127933219497",
                "storeUrl": "http://www.facebook.com/gaming/play/2505127933219497/",
                "sellerName": "Sprinklr IOS APP",
                "sellerUrl": "https://www.facebook.com/games/?app_id=2505127933219497",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_715494248105295_66122206",
                "appId": "715494248105295",
                "adChannelAppId": "715494248105295",
                "storeUrl": "http://www.facebook.com/gaming/play/715494248105295/",
                "sellerName": "Sprinklr IOS APP",
                "sellerUrl": "https://www.facebook.com/games/?app_id=715494248105295",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_1160392825849688_66122206",
                "appId": "1160392825849688",
                "adChannelAppId": "1160392825849688",
                "storeUrl": "http://www.facebook.com/gaming/play/1160392825849688/",
                "sellerName": "spr ios app",
                "sellerUrl": "https://www.facebook.com/games/?app_id=1160392825849688",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_996135769001598_66122206",
                "appId": "996135769001598",
                "adChannelAppId": "996135769001598",
                "storeUrl": "http://www.facebook.com/gaming/play/996135769001598/",
                "sellerName": "Sprinklr Android App",
                "sellerUrl": "https://www.facebook.com/games/?app_id=996135769001598",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            },
            {
                "id": "FACEBOOK_APPLICATION_1395289801087006_66122206",
                "appId": "1395289801087006",
                "adChannelAppId": "1395289801087006",
                "storeUrl": "http://www.facebook.com/gaming/play/1395289801087006/",
                "sellerName": "Self App",
                "sellerUrl": "https://www.facebook.com/games/?app_id=1395289801087006",
                "sellerIconImageUrl": "https://scontent-bom2-1.xx.fbcdn.net/v/t1.30497-1/85141356_2619750468133430_1265219897076482048_n.png?stp=dst-png_s130x130&_nc_cat=105&ccb=1-7&_nc_sid=7565cd&_nc_ohc=6hdZkgypb1AQ7kNvwHWCfmG&_nc_oc=Adn7YKCsagAwHuS22ip6W1XyZ_TLW0JcteIsYEi5TI5ehCa_FkvLo8J1pVxUA4FWRto&_nc_zt=24&_nc_ht=scontent-bom2-1.xx&edm=ABE7cloEAAAA&oh=00_AfVoegtNFwvlvrnLinOe5g3OZX276Kldxy7Bma0bbRK9IQ&oe=68BC1677",
                "store": "instant_game"
            }
        ]
    },
    "errors": []
}




### Response Parameters































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. | Object |
|  | responseEntities | Object containing response entities.         See Response Entities object table below. | Array |
| errors |  | Array containing error details, if any. | Array |


### Response Entities




















































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id of the application entity | String |
| appId | Application Id | String |
| adChannelAppId | Ad channel-specific application Id | String |
| storeUrl | URL to the app store or game page | String |
| sellerName | Name of the seller | String |
| sellerUrl | URL to the seller’s profile or website | String |
| sellerIconImageUrl | URL to the seller’s icon/image | String |
| store | Type of app store (for example, instant_game) | String |

[](https://dev.sprinklr.com/fetch-application-information) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-application-information)
