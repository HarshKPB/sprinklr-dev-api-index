---
title: "Enable Survey Events Logging for Flutter"
slug: enable-survey-events-logging-for-flutter
url: https://dev.sprinklr.com/enable-survey-events-logging-for-flutter
---

# Enable Survey Events Logging for Flutter

# Enable Survey Events Logging for Flutter
 

The Sprinklr Survey Kit SDK supports a logging system that can capture events at different levels. You can use this setup to efficiently track, debug, and manage various events within the app.

## Register Logging Handler



StreamSubscription? logSub;
Future registerLogHandler() async {
  logSub = await surveyKit.onLog((LogData log) {
    final LogLevel level = log.level;
    final List messages = log.logs;
    // Example: basic console logging
    // print('[$level] ${messages.join(' ')}');
    if (level == LogLevel.error || level == LogLevel.fatal) {
      // Send errors to your error tracking service
    }
  });
}



## Parameters
















****````






**







****``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| callback | Required | Function | The function called when logs are generated.         Usage: Receives logLevel and logs as arguments. |
| logLevel | Required | LogLevel | The severity level of the log.         See Supported Log Levels table. |
| logs | Required | string[] | Array of log messages.         Example: ["SDK initialized", "Intercept evaluation passed"] |

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

See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-flutter)

	 [](https://dev.sprinklr.com/enable-survey-events-logging-for-flutter)

[Back to top](https://dev.sprinklr.com/enable-survey-events-logging-for-flutter)
