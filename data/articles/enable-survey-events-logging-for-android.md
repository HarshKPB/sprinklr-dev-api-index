---
title: "Enable Survey Events Logging for Android"
slug: enable-survey-events-logging-for-android
url: https://dev.sprinklr.com/enable-survey-events-logging-for-android
---

# Enable Survey Events Logging for Android

# Enable Survey Events Logging for Android
 

The Sprinklr Survey Kit SDK supports a logging system that can capture events at different levels. You can use this setup to efficiently track, debug, and manage various events within the app.




 Copy Code



SPRSurveyLoggerConfig loggerConfig = new SPRSurveyLoggerConfig() 
        .setEnableLogs(true) 
        .setLevel(SPRSurveyLoggerConfig.SPRLogLevel.SPR_INFO) 
        .setLoggerTransport((level, logs) -> Log.d("Logger: ", logs.toString())); 
 
SPRSurveyManager.shared.setLoggerConfig(loggerConfig); 

## Parameters
















****````






**









| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| enableLogs | Optional | Boolean | Enables or disables logging output.         Supported Values:true or false |
| level | Optional | SPRSurveyLogLevel | Sets the logging level.         See Supported Log Levels table. |
| loggerTransport | Optional (Required when enableLogs is set to true) | SPRSurveyLoggerTransport | The object responsible for handling log output. |

### Supported Log Levels










































| Log Level | Description |
| --- | --- |
| OFF | Disables all logging. No log messages will be recorded. |
| FATAL | Logs only the most severe error events that will presumably lead the application to abort. |
| ERROR | Logs things that went wrong so that either something failed or the system had to resort to a fallback that the user may have noticed. |
| WARN | Logs things that went wrong, but were recoverable so that a user should not have noticed. |
| INFO | Logs primarily large business-logic steps such as the SDK connects, sends, and receives messages. |
| DEBUG | Logs details of the inner workings of the SDK logic and network stack. |
| TRACE | Logs high-traffic logs; tracks many objects as they move through the SDK. |
| ALL | Enables all logging levels, capturing every log message. |

## Related Resources

See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-android)

	 [](https://dev.sprinklr.com/enable-survey-events-logging-for-android)

[Back to top](https://dev.sprinklr.com/enable-survey-events-logging-for-android)
