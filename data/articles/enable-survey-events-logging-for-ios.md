---
title: "Enable Survey Events Logging for iOS"
slug: enable-survey-events-logging-for-ios
url: https://dev.sprinklr.com/enable-survey-events-logging-for-ios
---

# Enable Survey Events Logging for iOS

# Enable Survey Events Logging for iOS
 

The Sprinklr Survey Kit SDK supports a logging system that can capture events at different levels. You can use this setup to efficiently track, debug, and manage various events within the app.

### Swift

- Add logger transport where you have defined your `initializeProject` method:




 Copy Code


class ClassName: SPRSurveyLoggerTransport



- Before calling `initializeProject`, add `loggerConfig`:



 Copy Code


let loggerConfig = SPRSurveyLoggerConfig()
        loggerConfig.enableLogs = true
        loggerConfig.level = .INFO
        loggerConfig.loggerTransport = self
        SPRSurveyManager.shared.loggerConfig = loggerConfig



**Dev Notes: **The Swift compiler automatically removes the common prefix (SPR_) for enum members, hence they can be accessed without adding the SPR_ prefix. (example: SPRSurveyLogLevel.INFO).

- Finally, add a custom logger transport function:




 Copy Code


func write(level: SPRSurveyLogLevel, logs: [String]){
        NSLog(logs.first ?? "")
    }




### Objective C

- Add logger transport where you have defined your `takeOff` method:



 Copy Code


@interface ClassName()
@end



- Before calling `takeOff`, add `loggerConfig`:



 Copy Code


SPRSurveyLoggerConfig *loggerConfig = [[SPRSurveyLoggerConfig alloc] init];
    loggerConfig.enableLogs = YES;
    loggerConfig.level = SPRSurveyLogLevelInfo;
    loggerConfig.loggerTransport = self;
    [SPRSurveyManager shared].loggerConfig = loggerConfig;



- Finally, add a custom logger transport function:




 Copy Code


- (void)writeWithLevel:(enum SPRSurveyLogLevel)level logs:(NSArray * _Nonnull)logs {
    NSLog(@"%@", logs);
}




## Parameters
















****
````
````






**







****``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| enableLogs | Optional | Boolean | Enables or disables logging output.         Supported Values:         Swift: true or false         Objective-C: YES or NO |
| level | Optional | SPRSurveyLogLevel | Sets the logging level.         See Supported Log Levels table. |
| loggerTransport | Optional (Required when enableLogs is set to true or YES) | SPRSurveyLoggerTransport | The object responsible for handling log output.         Supported Value: SPRSpecSurveyLoggerTransport |

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

See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)

	 [](https://dev.sprinklr.com/enable-survey-events-logging-for-ios)

[Back to top](https://dev.sprinklr.com/enable-survey-events-logging-for-ios)
