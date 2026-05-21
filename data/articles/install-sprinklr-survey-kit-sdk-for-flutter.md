---
title: "Install Sprinklr Survey Kit SDK for Flutter"
slug: install-sprinklr-survey-kit-sdk-for-flutter
url: https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-flutter
---

# Install Sprinklr Survey Kit SDK for Flutter

# Install Sprinklr Survey Kit SDK for Flutter
 

Sprinklr Survey Kit (`spr_survey_kit`) is distributed as a restricted Flutter package. It must be added as a local/path dependency that you receive from Sprinklr.

**Dev Notes: **To get the Sprinklr Survey Kit Flutter plugin, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## Installing the Sprinklr Survey Kit SDK

- After the plugin is shared by Sprinklr, download it to a local folder accessible by your Flutter app.

- In `pubspec.yaml`, add the dependency:



dependencies:
  flutter:
    sdk: flutter
  spr_survey_kit:
    path:



- Run the following command to install:



flutter pub get



## Android Setup

Update your main Android activity to extend `FlutterFragmentActivity`. This is required for proper survey UI rendering (and for compatibility with other plugins using fragments).

### Example

**Kotlin**



package com.spr.surveyapp
import io.flutter.embedding.android.FlutterFragmentActivity
class MainActivity : FlutterFragmentActivity()



**Java**



package com.spr.surveyapp;
import io.flutter.embedding.android.FlutterFragmentActivity;
public class MainActivity extends FlutterFragmentActivity {
}



## iOS Setup

From your Flutter project root:



cd ios
pod install
cd ..



## Import and Create Instance



import 'package:spr_survey_kit/spr_survey_kit.dart';
final SPRSurveyKit surveyKit = SPRSurveyKit();



SPRSurveyKit is a singleton, so you can reuse the same instance across the app.

## Next Steps

[Initialize Sprinklr Survey Kit SDK for Flutter](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-flutter)

	 [](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-flutter)

[Back to top](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-flutter)
