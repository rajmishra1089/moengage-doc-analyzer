# MoEngage Dashboard Overview
`https://help.moengage.com/hc/en-us/articles/206559303-Dashboard-Overview`

MoEngage Dashboard provides quick access to:

* Create user segments
* Send targeted campaigns for your app or website
* Discover exciting analytics such as uninstalls, acquisitions, retention cohorts, and insights through campaign performance, user conversion data, and more


# First-Time Setup

The first time you log in to MoEngage, the Dashboard is available as a Test environment. You can integrate MoEngage with your app or web and get user or event data.  It's crucial to understand the difference between the Test and Live environments.  The Test environment allows you to safely experiment with configurations and integrations without impacting your live user data.  The Live environment is for your production app or website, where your actual user data is processed and campaigns are delivered to your real audience. Using the wrong environment can lead to unexpected results or data loss.  Make your environment Live after integration or tracking of events is complete and your app is released or your website is live. For more information on the test and live environments, refer to [Live and Test Environments](https://help.moengage.com/hc/en-us/articles/210845683-Understand-LIVE-TEST-environments).


# Configure Workspace Language

The MoEngage workspace language is set to English by default, but you can change it to any language supported by MoEngage.

info |  **Information** MoEngage currently supports Japanese and will soon support Brazilian Portuguese, Spanish, and German.  
---|---  
  
|  **Early Access** This is an Early Access feature. To enable it for your account, contact your Customer Success Manager (CSM) or [raise a support ticket](/hc/en-us/articles/19708702327572). Raising a support ticket involves submitting a request through our help center to our support team.  
---|---  

Configure the workspace language by following these steps:

1. Navigate to **My profile** > **Preferences** > **Language preferences**.
2. In the **Workspace language** list, select your preferred language.

Your workspace switches to the selected language.


# Set Up the Dashboard

This section guides you through configuring key settings in your MoEngage dashboard to optimize your app's integration and data analysis capabilities.  You'll manage app settings, channel-specific configurations, and account details.  Access the settings menu via the left navigation sidebar.

Configure the dashboard by clicking the **Settings** menu available on the left navigation sidebar.

You can configure the following settings:

* App
* Channel
* Account


## App

App settings help in configuring time zone, conversion goal settings, API settings, and analytics settings.  This section allows you to set up core functionalities related to your application's integration with MoEngage.


### General

In General settings, you can:

* Find your Workspace ID for integration.
* Set the time zone.
* Update app conversion goal and attribute to see insights on app conversions.  Define which in-app actions constitute a successful conversion (e.g., purchase, registration). Configured attributes are displayed as Key Metrics on the dashboard. For more information, refer to [Key Metrics](https://help.moengage.com/hc/en-us/articles/206560453).
* Associate or add new locales.  Add the languages supported by your app to track user language preferences for personalized communication.


### APIs

In APIs settings, you can:

* Get data API settings such as Data API ID and keys.
* View Transaction Push or Report settings such as API ID and API secret.
* Update, add new, or test content API settings such as Name and URL.

For more information, refer to [MoEngage APIs.](https://developers.moengage.com/hc/en-us/categories/4404541620756-API)


### Analytics

In Analytics settings, you can configure settings for:

* Acquisition. For more information, refer to [Acquisition](https://help.moengage.com/hc/en-us/articles/206134153-Acquisition).
* Uninstalls. For more information, refer to [Uninstall](https://help.moengage.com/hc/en-us/articles/209986613-Uninstall).
* Reports. For more information, refer to [Automated Reports](https://help.moengage.com/hc/en-us/articles/210000733-Automated-Campaign-Reports).


### Control Groups

In Control groups settings, you can configure the settings for the global control group. This allows for A/B testing of campaigns.

For more information, refer to [Global Control Group](https://help.moengage.com/hc/en-us/articles/360052305312-Global-Control-Group-).


## Channel

This section allows you to configure settings for various communication channels, such as push notifications, in-app messages, and email marketing.

### Push

Configure settings for push notifications:

* Web Push. For more information, refer to [Configure Web Push Settings](/hc/en-us/articles/210224063).
* Mobile Push.
* Frequency capping, push throttling, and do not disturb the setting.  Frequency capping limits the number of messages sent to users within a specific timeframe. Push throttling manages the rate at which push notifications are sent. Do Not Disturb settings respect user preferences for notification scheduling. For more information, refer to [Frequency Capping](/hc/en-us/articles/15919660670356), [DND](/hc/en-us/articles/15919572705556), and [Push Throttling](/hc/en-us/articles/15916160319764).

Based on the platform that your app or website supports and where you want to send push notifications, enter and upload the respective settings under Android, iOS, and Web Push settings. You can update the settings during SDK integration. For more information on how to update the settings, refer to [SDK integration](https://developers.moengage.com/hc/en-us).


### In-App NATIV

Configure the delay between In-App campaigns.


### Onsite Messaging

Configure the delay between On-Site messages from different campaigns.


### SMS Connector

Configure the following SMS settings:

* SMS Connector configuration. For more information, refer to [Configure SMS Connectors](https://help.moengage.com/hc/en-us/articles/4408413593492-Overview#sms-connector-configuration-0-0).
* SMS General settings. For more information, refer to [Configure SMS](https://help.moengage.com/hc/en-us/articles/7455149158676).
* SMS Frequency Capping (FC) and Do Not Disturb (DND) setting. For more information, refer to [Frequency Capping](/hc/en-us/articles/115003135246) and [DND](/hc/en-us/articles/15919572705556).


### Emails

Configure Email SMTP settings on the dashboard for Email campaigns. You can configure the SMTP attributes depending on your Email Service provider. For more information, refer to [Email Settings](https://help.moengage.com/hc/en-us/articles/208137513-Configuring-connectors).


### Cards

Configure the following settings:

* URL
* Security Headers


### Preference Management

Configure opted-out users from future campaigns of SMS, Push, and Email.


## Account

For more information, refer to [Account Management](https://help.moengage.com/hc/en-us/categories/360002692372-Account-Management-). This section allows you to manage your account details, team members, and billing information.

### Team Management

Invite team members and change the roles of existing team members. For more information, refer to [Access Roles](https://help.moengage.com/hc/en-us/articles/210855743-Access-Roles).


### Billing

Add payment methods and access the billing history for your MoEngage Account.


# Next Steps

Your Dashboard is now fully set up to start creating segments and launching targeted campaigns.  You can now leverage MoEngage's features to personalize and optimize your marketing efforts. For more information, refer to [creating user segments](https://help.moengage.com/hc/en-us/articles/206169646-Creating-user-segments) and [campaigns](https://help.moengage.com/hc/en-us/articles/360058167752-MoEngage-Channels).
