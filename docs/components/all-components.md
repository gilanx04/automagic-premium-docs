---
title: "Complete Component Catalog"
source: https://automagic4android.com/components_all_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
category: catalog
---

# Complete Component Catalog

## Triggers

### [Accessibility Button](triggers/trigger_accessibility_button.md)

The trigger **Accessibility Button** is executed when the additional button on the navigation bar is clicked. Only devices that provide the navigation bar with software buttons support this trigger.

Examples:

- Execute an important flow from within nearly every app directly.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Active Network Type](triggers/trigger_active_network_type.md)

The trigger **Active Network Type** executes a flow when the active network type changes to another type.

#### Settings

##### Network type changed to

Defines for what network types the trigger should be executed

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `network_type` — the network type as number (None=-1, Mobile=0, WiFi=1, WiMAX=6, Bluetooth=7, Ethernet=9)
- `network_type_name` — the name of the network as string like `WIFI` or `MOBILE`
- `network_subtype` — the network subtype as number
- `network_subtype_name` — the network subtype as number
- `network_state` — the network state (CONNECTING, CONNECTED, SUSPENDED, DISCONNECTING, DISCONNECTED, UNKNOWN)
- `network_detailed_state` — the detailed network state (IDLE, SCANNING, CONNECTING, AUTHENTICATING, OBTAINING\_IPADDR, CONNECTED, SUSPENDED, DISCONNECTING, DISCONNECTED, FAILED, BLOCKED, VERIFYING\_POOR\_LINK, CAPTIVE\_PORTAL\_CHECK)
- `network_extra_info` — additional info as string (like SSID), when available
- `network_reason` — the reason of a failure, when available

---

### [Activity Ended](triggers/trigger_activity_ended.md)

The trigger **Activity Ended** is executed when an activity is moved to the background.

#### Settings

##### Package Name

The package name of the app or comma separated list. Glob patterns are supported.

##### Class Name

The class name of the activity or comma separated list. Glob patterns are supported.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `package_name` — the name of the package
- `app_name` — the display name of the app
- `activity_class` — the class of the activity
- `activity_name` — the display name of the activity

---

### [Activity Started](triggers/trigger_activity_started.md)

The trigger **Activity Started** is executed when an activity is moved to the foreground.

Examples:

- Increase the display brightness when Google Maps is started.

#### Settings

##### Method

How the activity should be determined. Method **Usage statistics** can be delayed on some devices.

##### Package Name

The package name of the app or comma separated list. Glob patterns are supported.

##### Class Name

The class name of the activity or comma separated list. Glob patterns are supported.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `package_name` — the name of the package
- `app_name` — the display name of the app
- `activity_class` — the class of the activity
- `activity_name` — the display name of the activity

---

### [Airplane Mode](triggers/trigger_airplane_mode.md)

The trigger **Airplane Mode** is executed when the airplane mode is turned on or off.

Example:

- Disable all flows that are downloading data when the airplane mode is turned on.

#### Settings

##### Airplane Mode On/Off

Whether the trigger should be executed when the airplane mode is turned on or off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Android Wear Device Connected/Disconnected](triggers/trigger_android_wear_device_connected.md)

The trigger **Android Wear Device** is executed when an Android Wear device is connected or disconnected from the main device.

Examples:

- Play an alert sound when the Wear watch is disconnected from the main device.

#### Settings

##### Android Wear device

The target device.

##### Device connected/disconnected

Whether the trigger should be executed when the device is connected or disconnected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `node_id` — the ID of the Wear node

---

### [App Package Event](triggers/trigger_app_package_event.md)

The trigger **App Package Event** is executed when a app/package is installed, updated or removed.

Examples:

- Write the date and time of an app update to a log file for reference.

#### Settings

##### Event

The event type:

- **Added**: A new package has been installed
- **Changed**: A component of a package has been enabled/disabled
- **Data cleared**: The data of the app has been cleared
- **Replaced**: A package has been updated
- **Restarted**: A package has been restarted and all processes of the package have been killed
- **Removed**: A package was removed or is in the process of being updated
- **Fully removed**: A package has been uninstalled (and data deleted) (Android 4)

##### Package Name

The list of package names to check. Glob patterns are supported.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `package_name` — the name of the package
- `app_name` — the display name of the app (only available when app is still installed)
- `uid` — the UID assigned to the package
- `replacing` — true when the package is updated (only set for event *Added* and *Removed*)
- `changed_component_name_list` — the list of changed components (only set for event *Changed*)
- `dont_kill_app` — true when the app should not be killed (only set for event *Changed*)
- `data_removed` — true when also the data has been removed (only set for event *Removed*)

---

### [App Task Ended](triggers/trigger_app_task_ended.md)

The trigger **App Task Ended** is executed when an application is moved to the background or closed respectively the user moved the focus to another app.
The application might still be running in the background or the process hosting the application might still be in memory.

Examples:

- Raise the media volume back to normal when you leave the browser.
- Change the display brightness back to normal when you don't use Google Maps anymore.

#### Settings

##### Method

How the app should be determined. Method **Usage statistics** can be delayed on some devices.

##### Package Name

Enter the name of the package of the application or use the button to show a list of available applications. Glob patterns (\*, ?) can be used to match apps with similar names. A single \*-character matches all apps.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `package_name` — the name of the package
- `app_name` — the display name of the app

---

### [App Task Started](triggers/trigger_app_task_started.md)

The trigger **App Task Started** is executed when an application is moved to the foreground or opened respectively the user moved the focus to this app.

Examples:

- Lower the media volume when you open the browser.
- Raise the display brightness when you start using Google Maps.

#### Settings

##### Method

How the app should be determined. Method **Usage statistics** can be delayed on some devices.

##### Package Name

Enter the name of the package of the application or use the button to show a list of available applications. Glob patterns (\*, ?) can be used to match apps with similar names. A single \*-character matches all apps.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `package_name` — the name of the package
- `app_name` — the display name of the app

---

### [Assist](triggers/trigger_assist.md)

The trigger **Assist** is executed when the home button is long-pressed or dragged upwards (Galaxy Nexus) or the home button is long-pressed and the middle icon is selected (S3).

Warning: This function requires Android 4.1+ and is not officially supported by Android.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Audio Volume](triggers/trigger_audio_volume.md)

The trigger **Audio Volume** is executed when the volume of the device has been changed. Some devices report the volume change slightly delayed.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Vibrate whenever the volume is changed.

#### Settings

##### Sound Type

The type of the audio stream to check.

##### Condition

Whether the condition should check if the volume is above or below the volume level.

##### Volume

The volume value to check.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `volume` — the new volume value
- `old_volume` — the volume value before the change

---

### [Auto Sync State](triggers/trigger_auto_sync_state.md)

The trigger **Auto Sync State** is executed when the auto sync setting is changed to on or off.

Examples:

- Turn an hourly executed download flow off when auto sync is disabled.

#### Settings

##### Auto Sync

**On**
Execute the flow when the auto sync has been turned on.

**Off**
Execute the flow when the auto sync has been turned off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Automagic Notification Selected](triggers/trigger_automagic_notification_selected.md)

The trigger **Automagic Notification Selected** executes a flow when the Automagic-wand notification available in the statusbar is selected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Automagic SMS Delivery Report Received](triggers/trigger_sms_delivery_report_received.md)

The trigger **Automagic SMS Delivery Report Received** is executed when an asynchronous delivery report was received.

Note: Multiple delivery reports can be received per SMS, for example a status 48 (delivery pending) and later status 0 (OK) when the SMS was delivered.

Examples:

- Send an SMS one more time when the delivery report indicates an error.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `sms_receiver` — the original receiver of the SMS
- `sms_text` — the original text of the SMS
- `sms_delivery_report_status` — the status code (0-31=OK, 32-63=delivery pending, >=64=error)

---

### [Automagic Startup](triggers/trigger_automagic_startup.md)

The trigger **Automagic Startup** is executed when the Automagic service is completely started and the flows have been loaded.

Examples:

- Initialise global variables to default values when Automagic started.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Battery Level](triggers/trigger_battery_level.md)

The trigger **Battery Level** is executed whenever the battery level changes and the built in condition about the level holds true.

Examples:

- Lower the display brightness when the battery level falls below 50%.
- Turn off WiFi when the battery level falls below 30%.

#### Settings

##### Battery Level

Defines the condition that must be met to execute the flow:

**becomes lower than**
Executes the flow when the last reported percentage was above the defined level and the current percentage is below the defined level

**becomes higher than**
Executes the flow when the last reported percentage was below the defined level and the current percentage is above the defined level

**becomes equal to**
Executes the flow when the last reported percentage was different than the defined level and the current percentage equals the defined level

**becomes full**
Executes the flow when the last reported battery status was not full and is now full

**lower than**
Executes the flow whenever the reported percentage by the system is below the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**higher than**
Executes the flow whenever the reported percentage by the system is above the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**exactly**
Executes the flow whenever the reported percentage by the system is exactly on the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**full**
Executes the flow whenever the reported battery status by the system is full. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last status has been already full.

##### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery (1=unknown, 2=good, 3=overheat, 4=dead, 5=over voltage, 6=unspecified failure, 7=cold)
- `battery_charge_counter` — Battery capacity in microampere-hours. null when not available
- `battery_current_now` — Instantaneous battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_current_average` — Average battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_energy_counter` — Battery remaining energy in nanowatt-hours. null when not available

---

### [Battery Level (Android Wear)](triggers/trigger_battery_level_wear.md)

The trigger **Battery Level (Android Wear)** is executed whenever the battery level changes and the built in condition about the level holds true.

Examples:

- Lower the display brightness when the battery level falls below 50%.
- Turn off WiFi when the battery level falls below 30%.

#### Settings

##### Android Wear device

The target device.

##### Battery Level

Defines the condition that must be met to execute the flow:

**becomes lower than**
Executes the flow when the last reported percentage was above the defined level and the current percentage is below the defined level

**becomes higher than**
Executes the flow when the last reported percentage was below the defined level and the current percentage is above the defined level

**becomes equal to**
Executes the flow when the last reported percentage was different than the defined level and the current percentage equals the defined level

**becomes full**
Executes the flow when the last reported battery status was not full and is now full

**lower than**
Executes the flow whenever the reported percentage by the system is below the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**higher than**
Executes the flow whenever the reported percentage by the system is above the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**exactly**
Executes the flow whenever the reported percentage by the system is exactly on the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**full**
Executes the flow whenever the reported battery status by the system is full. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last status has been already full.

##### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery (1=unknown, 2=good, 3=overheat, 4=dead, 5=over voltage, 6=unspecified failure, 7=cold)
- `node_id` — the ID of the Wear node

---

### [Battery Low Condition](triggers/trigger_battery_low_okay.md)

The trigger **Battery Low Condition** is executed when the battery level becomes low or when the battery level becomes OK again after it was low.

Examples:

- Lower the display brightness when the battery level becomes low.
- Turn off WiFi when the battery level becomes low.
- Turn on WiFi when the battery level becomes OK again.

#### Settings

##### Battery Condition

**low**
The battery level becomes low (the exact value can differ between different devices).

**OK**
The battery level becomes OK again (the exact value can differ between different devices).

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Battery Saver Mode](triggers/trigger_power_save_mode.md)

The trigger **Battery Saver Mode** is executed when the battery saving mode of the device is changed (Android 5+).
Warning: This function does not work for manufacturer specific battery saving modes like Samsungs (Ultra-)energy saving mode or Sony and HTC specific modes. Please use action **System Setting Changed** on such devices.

Examples:

- Turn off a few flows when the battery saver is activated.

#### Settings

##### Turned On or Off

Whether to execute the flow when the mode was turned on or off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Bluetooth Device Connected](triggers/trigger_bluetooth_device_connected.md)

The trigger **Bluetooth Device Connected** is executed when a bluetooth device is connected.

Examples:

- Turn down the volume when a bluetooth headset is connected.

#### Settings

##### Bluetooth Device

Defines whether the trigger should be executed for all devices or only for a specific device.

##### Bluetooth Device Address

The address of the bluetooth device.

##### Bluetooth Device Name

The name of the bluetooth device.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `name` — the name of the device
- `address` — the address of the device
- `bluetooth_class` — the bluetooth class of the device
- `bond_state` — the bonding state of the device

---

### [Bluetooth Device Disconnected](triggers/trigger_bluetooth_device_disconnected.md)

The trigger **Bluetooth Device Disconnected** is executed when a bluetooth device is disconnected.

Examples:

- Turn up the volume when a bluetooth headset is disconnected.

#### Settings

##### Bluetooth Device

Defines whether the trigger should be executed for all devices or only for a specific device.

##### Bluetooth Device Address

The address of the bluetooth device.

##### Bluetooth Device Name

The name of the bluetooth device.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `name` — the name of the device
- `address` — the address of the device
- `bluetooth_class` — the bluetooth class of the device
- `bond_state` — the bonding state of the device

---

### [Bluetooth State](triggers/trigger_bluetooth_state.md)

The trigger **Bluetooth State** is executed when the bluetooth adapter of the device is turned on or off depending on the settings used.

Examples:

- Enable some flows using the bluetooth adapter as soon as the bluetooth is turned on.

#### Settings

##### Bluetooth state

Defines the bluetooth states to trigger the flow. Selecting multiple states triggers the flow once for each state.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_bluetooth_state` — the state of the bluetooth adapter before
- `bluetooth_state` — the current state of the bluetooth adapter

---

### [Calendar](triggers/trigger_calendar.md)

The trigger **Calendar** is executed on the defined date and time.

Examples:

- Send a reminder mail on the last Friday of each month.
- Export and mail your time tracking data on the first Monday of each month.

Note: You can use the trigger **Time** to execute a flow on every weekday or on every Monday.

#### Settings

##### Date/Time

Defines the date and time when the flow should be executed or the first time a flow should be executed when this is a repeating trigger.

##### Repeats

Defines when this trigger should repeat.

##### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

##### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Calendar Event](triggers/trigger_calendar_event.md)

The trigger **Calendar Event** is executed when an event on the calendar starts or ends.

Examples:

- Mute the ringer when a meeting starts.
- Vibrate 5 minutes before a meeting starts.
- Start recording a task in *Gleeo Time Tracker* when a meeting starts.

#### Settings

##### Trigger at Event Start

Whether the trigger should execute at the start of the event. The duration specifies whether the trigger should execute a certain amount of time before or after the event begins.

##### Trigger at Event End

Whether the trigger should execute at the end of the event. The duration specifies whether the trigger should execute a certain amount of time before or after the event ends.

##### Calendars

A comma separated list of calendar names that should be checked for events. The names can contain glob pattern characters like `*` and `?`.

##### Titles

A comma separated list of event titles to match. The titles can contain glob pattern characters like `*` and `?`.

Examples:

- `Plan*` matches titles like `Planning`, `Plan B` etc.

##### Descriptions

A comma separated list of event descriptions to match. The descriptions can contain glob pattern characters like `*` and `?`.

##### Locations

A comma separated list of event locations to match. The locations can contain glob pattern characters like `*` and `?`.

##### Event Type

Whether the trigger should consider all day events or regular events (not all day) or both.

##### Event Availability

Whether the trigger should consider events marked as free, busy or tentative.

##### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

##### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `event_calendar` — the name of the calendar of the event
- `event_title` — the title of the event
- `event_description` — the description of the event
- `event_location` — the location of the event
- `event_start` — the start time of the event
- `event_end` — the end time of the event
- `event_all_day` — boolean indicating if the event is all day or not
- `event_availability` — FREE, BUSY or TENTATIVE depending on the availability of the event
- `event_id` — the ID of the event

---

### [Car UI Mode](triggers/trigger_car_ui_mode.md)

The trigger **Car UI Mode** is executed when the device is put into car UI mode when placed in a car dock.

Examples:

- Raise the audio volume when the device is put into the car dock.

#### Settings

##### Enter or Exit car UI mode

**Enter**
When selected executes the flow when the device is put into car UI mode.

**Exit**
When selected executes the flow when the car UI mode has been ended.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Clipboard Changed](triggers/trigger_clipboard_changed.md)

The trigger **Clipboard Changed** is executed when the content of the clipboard changes.
Use the action **Copy Text from Clipboard** to access the content of the clipboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `clip_data` — the text of the clipboard

---

### [Command Output](triggers/trigger_command_output.md)

The trigger **Command Output** is executed when a command prints a line containing a specific text.

#### Settings

##### Command

The command to execute. The command is passed to `/bin/sh` to be interpreted or to `su` when *as root* is checked.

##### SE Context

The SE context to use to execute the command. This setting is often required when using Android 5+ or any other device that set SELinux to enforcing. Requires *su* that allows to switch SE context (like SuperSU v1.97+).

##### Working Directory

The path the command is executed in.

##### Output trigger condition

The text which needs to be contained in the output to trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `stdout` — the last 10 lines written to stdout
- `stderr` — the last 10 lines written to stderr
- `output` — the triggering line
- `output_type` — the string `stdout` when the triggering line was written to stdout, stderr otherwise

---

### [Compass](triggers/trigger_compass.md)

The trigger **Compass** executes the flow when the device changes its orientation.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Play a beep sound when the device is heading north.

#### Settings

##### Type

The type of the trigger.

- **Periodic**: executes the flow in periodic time intervals
- **On Change**: executes the flow when the orientation changed for at least some degrees.
- **On Relative Sector Change**: Remembers the device orientation when this trigger is enabled first, divides the orientation into the specified number of equal sectors and executes the flow whenever the device stays in a different sector.

##### Frequency

Defines the frequency between flow executions.

##### Tolerance in Degrees

The minimum amount of change in the device orientation required to execute the flow.

##### trigger when steady

Executes the flow only when the device does not change the direction for a short period of time anymore.

##### Number of Sectors

The number of equal sectors to divide the orientation of the device. The sectors are numbered starting at 1 and incrementing in clockwise order.

Example:
When 4 sectors are desired the 360° possible degrees are divided into 4 sectors with an opening angle of 90° each. The sectors are relative to the initial device orientation when the trigger was enabled.

- Sector 1: 315° to 45°
- Sector 2: 45° to 135°
- Sector 3: 135° to 225°
- Sector 4: 225° to 315°

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `azimuth` — the azimuth in degrees
- `pitch` — the pitch in degrees
- `roll` — the roll in degrees
- `azimuth_sector` — the azimuth sector (1 to Number of Sectors)
- `pitch_sector` — the pitch sector (1 to Number of Sectors)
- `roll_sector` — the roll sector (1 to Number of Sectors)

---

### [Content Provider Changed](triggers/trigger_content_provider_changed.md)

The trigger **Content Provider Changed** is executed whenever the content provider is changed for the specified URI. Note that not all content providers support this feature.

Examples:

- Get notified whenever the MMS database changes so you can check if there's a new message.

#### Settings

##### Content URI

The URI to get changes for (including ancestors).

##### Notify for descendants

Whether changes in descendant URIs should also be detected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `content_uri` — the actual URI for the change

---

### [CyanogenMod Quick Settings Tile Selected](triggers/trigger_cyanogen_mod_quick_settings_tile_selected.md)

The trigger **CyanogenMod Quick Settings Tile Selected** creates a quick settings tile and is executed when the tile is selected/clicked.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Create a QS tile to send an SMS with the current location.

#### Settings

##### Label

The label of the tile. [Variables are supported (replaced when trigger is activated).](#string-inline-expressions)

##### Icon

The icon to use for the tile. [Variables are supported (replaced when trigger is activated).](#string-inline-expressions)

##### Collapse panel

Whether or not the quick settings area should be closed when the tile is selected/clicked.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Daydream State](triggers/trigger_daydream_state.md)

The trigger **Daydream State** is executed when the daydream of the system starts or stops.

#### Settings

##### Daydream Started/Stopped

Whether to trigger on the daydream start or the stop.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Desk UI Mode](triggers/trigger_desk_ui_mode.md)

The trigger **Desk UI Mode** is executed when the device is put into desk UI mode when placed in a desk dock.

Examples:

- Raise the audio volume when the device is put into the desk dock.

#### Settings

##### Enter or Exit desk UI mode

**Enter**
When selected executes the flow when the device is put into desk UI mode.

**Exit**
When selected executes the flow when the desk UI mode has been ended.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Device Idle/Doze Mode](triggers/trigger_device_idle_mode.md)

The trigger **Device Idle/Doze Mode** is executed when the device falls into idle/doze mode or is woken up from this mode.

Examples:

- Deactivate some less important flows when the device enters idle/doze mode.

#### Settings

##### Turned On or Off

Whether the trigger should be executed when the idle/doze mode is turned on or off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Device Orientation](triggers/trigger_device_orientation.md)

The trigger **Device Orientation** executes the flow when the device is moved to the defined orientation.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Reduce the ringer volume when the device screen is facing down.

#### Settings

##### Device Orientation

The desired orientation of the device.

- **Face down:** The display of the device is facing down for example when lying on a table with the display towards the table.
- **Face up:** The display of the device is facing up for example when lying on a table with the display facing away from the table.
- **Face left:** The display faces to the left with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Face right:** The display faces to the right with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Standing upright:** The device is standing upright on a table.
- **Standing upside-down:** The device is standing upside-down on a table.

##### Negate

Whether the condition should be negated or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Device Storage Space Low](triggers/trigger_device_storage_space_low_okay.md)

The trigger **Device Storage Space Low** executes the flow when the internal device storage space becomes low or the free storage space is back to a normal level.

Note: The amount of free space to consider as low is defined by the device manufacturer.
Standard Android considers less than 10% of free internal memory as low.

Example:

- Play a warning sound when the device storage space is low.

#### Settings

##### Device Storage Space

**becomes low**
Executes the flow when the storage space becomes low.

**becomes OK**
Executes the flow when the storage space is back to a normal level.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Display State](triggers/trigger_display_state.md)

The trigger **Display State** is executed when the display is turned on or off.

Examples:

- Turn on WiFi when you turn the display on. Turn WiFi off when you turn the display off.
- Count how many times a day you turn your display on.
- Remind you with a sound alert when you are recording your time and you are starting to use the device.

#### Settings

##### Display On/Off

**On**
Execute the flow when the display has been turned on.

**Off**
Execute the flow when the display has been turned off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Dock Event](triggers/trigger_dock_event.md)

The trigger **Dock Event** is executed when the device is put into a dock (car, desk, some external hardware keyboard).

The dock type can be distinguished using a condition **Dock State**.

Examples:

- Raise the audio volume when the device is put into a dock.

#### Settings

##### Docked/Undocked

**Docked**
When selected executes the flow after the device has been put into a dock.

**Undocked**
When selected executes the flow after the device has been removed from a dock.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `dock_state` — the state/dock type

---

### [File Observer](triggers/trigger_file_observer.md)

The trigger **File Observer** is executed when a path of interest on the filesystem is accessed or changed.

Examples:

- Create a copy of a file after it has been modified.
- Upload a new image to Dropbox when a new subfile is created in folder `/sdcard/DCIM/Camera/`.

#### Settings

##### Paths to Observe

A comma separated list of files or directories to observe. [Variables are supported (replaced when trigger is activated).](#string-inline-expressions)

##### Event Types

The type of events to observe.

- **File accessed**: Data was read from a file
- **Modify**: Data was written to a file
- **Metadata changed**: Metadata (permissions, owner, timestamp) was changed explicitly
- **Writable file closed**: Someone had a file or directory open for writing, and closed it
- **Unwritable file closed**: Someone had a file or directory open read-only, and closed it
- **File opened**: A file or directory was opened
- **File moved from**: A file or subdirectory was moved from the monitored directory
- **File moved to**: A file or subdirectory was moved to the monitored directory
- **Subfile created**: A new file or subdirectory was created under the monitored directory
- **Subfile deleted**: A file was deleted from the monitored directory
- **Delete Self**: The monitored file or directory was deleted; monitoring effectively stops
- **Self moved**: The monitored file or directory was moved; monitoring continues

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `registered_path` — the path of the observed file or directory
- `event` — the event represented as a number:
  - **File accessed**: 1 (0x00000001)
  - **Modify**: 2 (0x00000002)
  - **Metadata changed**: 4 (0x00000004)
  - **Writable file closed**: 8 (0x00000008)
  - **Unwritable file closed**: 16 (0x00000010)
  - **File opened**: 32 (0x00000020)
  - **File moved from**: 64 (0x00000040)
  - **File moved to**: 128 (0x00000080)
  - **Subfile created**: 256 (0x00000100)
  - **Subfile deleted**: 512 (0x00000200)
  - **Delete Self**: 1024 (0x00000400)
  - **Self moved**: 2048 (0x00000800)
- `path` — the path of the file or directory which triggered the event, relative to the main monitored file or directory

---

### [Fingerprint Gesture](triggers/trigger_fingerprint_gesture.md)

The trigger **Fingerprint Gesture** executes a flow when one of the supported gestures is executed on the fingerprint sensor.

Note: Enabling a trigger of this type can prevent other fingerprint apps from handling fingerprint gestures. Please note that this trigger becomes temporarily unavailable when an app or the system requests to scan a fingerprint.

Examples:

- Use a swipe down gesture to show notifications and a left swipe to simulate a back press.

#### Settings

##### Fingerprint Gesture

Defines for what gesture the trigger should be executed

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [General Broadcast](triggers/trigger_general_broadcast.md)

The trigger **General Broadcast** dynamically registers a broadcast receiver at runtime with the specified intent filter.
 Please also see the [Android Developer Documentation](http://developer.android.com/guide/components/intents-filters.html).

Examples:

- Receive the current WiFi signal strength (only when the display is turned on):
  Action: `android.net.wifi.RSSI_CHANGED`
  Access Intent Extras: `value=getInt("newRssi", 0);`

#### Settings

##### Action

The action to use in the intent filter.

##### Category List

The list of categories to use in the intent filter.

##### Data Scheme List

The list of data schemes to use in the intent filter. (like `http`, `content` etc.).

##### Data Authority List

The list of data authorities to use in the intent filter (`host:port`).

##### Data Path Literal List

The list of data paths to use in the intent filter (the specified pattern has to match the entire path)

##### Data Path Prefix List

The list of data paths to use in the intent filter (the specified pattern has to match the prefix of the path)

##### Data Path Glob List

The list of data paths to use in the intent filter (the specified glob pattern has to match the entire path)

##### Data Type List

The list of MIME types to use in the intent filter.

##### Access Intent Extras

Script to access the extras in the received intent.
Following functions are supported:

- `getString(String key)`
- `getChar(String key, String defaultValue)`
- `getBoolean(String key, Boolean defaultValue)`
- `getFloat(String key, Number defaultValue)`
- `getDouble(String key, Number defaultValue)`
- `getByte(String key, Number defaultValue)`
- `getShort(String key, Number defaultValue)`
- `getInt(String key, Number defaultValue)`
- `getLong(String key, Number defaultValue)`
- `getBundle(String key)`
- `getUri(String key)`
- `getBooleanArray(String key)`
- `getByteArray(String key)`
- `getShortArray(String key)`
- `getCharArray(String key)`
- `getIntArray(String key)`
- `getIntegerArrayList(String key)`
- `getLongArray(String key)`
- `getFloatArray(String key)`
- `getDoubleArray(String key)`
- `getStringArray(String key)`
- `getUriArray(String key)`
- `getUriArrayList(String key)`
- `getParcelableAsString(String key)`
- `getParcelableArrayAsString(String key)`
- `getParcelableArrayListAsString(String key)`
- `getParcelable(String key)`

Examples:
```
    value = getString("key1");
    value = getBoolean("key2", true);
    value = getDouble("key3", 1.23);
    value = getInt("key4", 42);
    value = getInt("key5", a+4*b);
```

Data of intents wrapped in a Bundle-extra can be accessed using function `getBundle(String name)`.
Values contained in a bundle can be accessed with the functions used to accessed regular extras but by additionally specifying the bundle.

Example:
```
    bundle = getBundle("key1");
    value = getString(bundle, "key2");
```

compact form:
```
    value = getString(getBundle("key1"), "key2");
```

Example to access the track info of PowerAMP:
```
    track_info = getBundle("track");

    artist = getString(track_info, "artist");
    album = getString(track_info, "album");
    title = getString(track_info, "title");
    path = getString(track_info, "path");
    duration = getInt(track_info, "dur", 0);
```

##### Initial Sticky Broadcast

Whether to ignore the initial broadcast sent for a sticky broadcast or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `action` — the action of the received intent
- `data_string` — the data of the received intent as a string
- `categories` — the list of categories
- `scheme` — the scheme of the received intent
- `type` — the explicitly set MIME type of the received intent

---

### [Gleeo Recording Started](triggers/trigger_gleeo_recording_started.md)

The trigger **Gleeo Recording Started** is executed when a task in **Gleeo Time Tracker** has been started.

#### Settings

##### Domain Filter List

A comma separated list of the domains to accept.

##### Project Filter List

A comma separated list of the projects to accept.

##### Task Filter List

A comma separated list of the tasks to accept.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `domain_name` — contains the name of the domain
- `project_title` — contains the title of the project
- `task_name` — contains the name of the task
- `start` — contains the start date and time of the recording entry

---

### [Gleeo Recording Stopped](triggers/trigger_gleeo_recording_stopped.md)

The trigger **Gleeo Recording Stopped** is executed when a task in **Gleeo Time Tracker** has been stopped.

#### Settings

##### Domain Filter List

A comma separated list of the domains to accept.

##### Project Filter List

A comma separated list of the projects to accept.

##### Task Filter List

A comma separated list of the tasks to accept.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `domain_name` — contains the name of the domain
- `project_title` — contains the title of the project
- `task_name` — contains the name of the task
- `start` — contains the start date and time of the entry
- `end` — contains the end date and time of the entry

---

### [Global Variable](triggers/trigger_global_variable.md)

The trigger **Global Variable** is executed when a different value is assigned to a global variable. The trigger is not executed when the same value is assigned to the variable again.

Examples:

- Show a reminder when you sent more than 10 SMS in one day.

#### Settings

##### Global Variable

The name of the global variable to watch.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `old_` — contains the old value of the global variable before it has been updated

---

### [Global Variable Date/Time](triggers/trigger_global_variable_date.md)

The trigger **Global Variable Date/Time** is executed when the point of time stored in the global variable is reached.

Examples:

- Execute a flow daily on sunrise/sunset.
- Execute a flow in irregular intervals.

#### Settings

##### Global Variable

The name of the global variable containing the point of time.

##### Trigger immediately on missed events

Execute the trigger when the point in time stored in the variable has passed and the trigger did not yet execute the trigger for this point in time (for example when the device was turned off at the date/time specified in the variable or when a past date is assigned to the global variable)

##### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

##### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Gmail Unread Conversation Count](triggers/trigger_gmail_unread_conversation_count.md)

The trigger **Gmail Unread Conversation Count** is executed when the count of unread conversations in the Gmail app on the device changes.

Examples:

- Play a notification sound, when more unread conversations are available.

#### Settings

##### Accounts

The accounts to check. The sum of unread conversations is checked when multiple accounts are specified.

##### Increasing Unread Count

When checked only executes the trigger when the unread conversation count increases.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `count` — the number of unread conversations
- `old_count` — the number of unread conversations before

---

### [GPS Status Event](triggers/trigger_gps_status_event.md)

The trigger **GPS Status Event** is executed, when the system start or stops to use GPS.

Examples:

- Vibrate when the system begins to use GPS for information purposes.

#### Settings

##### GPS Status Event

The type of the event:

- **Started**: executes the trigger when the system starts to use GPS
- **Stopped**: executes the trigger when the system stops to use GPS
- **First fix received**: executes the trigger when the system uses GPS and the first fix has just been determined
- **Satellite status changed**: executes the trigger when the satellite status changes (usually very frequent)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `gps_event_type` — typ of the event (1=started, 2=stopped, 3=first fix, 4=satellite status)
- `satellites` — list containing strings each containing the information of one satellite
- `time_to_first_fix` — number of milliseconds between turning on GPS and receiving the first fix, contains 0 or the last value when no fix was determined yet

---

### [Hardware Key Event](triggers/trigger_key_event.md)

The trigger **Hardware Key Event** is executed when the specified key is pressed/released. Most devices usually only provide hardware keys for volume up and volume down. The power key can usually not be intercepted.

Examples:

- Scroll down in a browser window when the volume down key is pressed.

#### Settings

##### Keys

The list of names of keys that should execute the trigger. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Actions

Whether down, up or both actions should execute the trigger.

##### Block event (blocks down and up actions)

Whether or not the key event should be blocked so that the system does not send the key event to other apps.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `key_code` — the numeric keycode
- `key_code_name` — the name of the keycode
- `key_duration` — the duration of the event in milliseconds
- `key_source_device_id` — the ID of the sending device
- `key_action_down` — whether the action was down
- `key_action_down` — whether the action was up

---

### [Hardware Keyboard State](triggers/trigger_hardware_keyboard_state.md)

The trigger **Hardware Keyboard State** is executed when the hardware keyboard is opened or closed.

Examples:

- Vibrate when the hardware keyboard is opened.

#### Settings

##### Opened or Closed

Whether the trigger should be executed when the keyboard is opened or closed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `keyboard_type` — the type of keyboard (1=unavailable, 2=QWERTY, 3=12-keys)

---

### [Hardware Keyboard Type](triggers/trigger_hardware_keyboard_type.md)

The trigger **Hardware Keyboard Type** is executed when the type of hardware keyboard changes to one of the selected types.

Examples:

- Increase the display timeout when a hardware keyboard is connected.

#### Settings

##### Keyboard type changed to

The type of keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `keyboard_type` — the type of keyboard (1=unavailable, 2=QWERTY, 3=12-keys)

---

### [HTTP Request (Experimental)](triggers/trigger_http_request.md)

The trigger **HTTP Request (Experimental)** is executed when a HTTP request is received using the specified path and port.

Note: The built-in webserver is neither fast nor should you try to upload large files. Please don't use it to run webshops, corporate websites or sites like Slashdot on your phone.

Examples:

- Send an SMS from your Phone using your PC when the URL `http://192.168.1.XX:8080/sms?receiver=12345&text=test` is requested.
- Return a page with the list of files on the SD card when the URL `http://192.168.1.XX:8080/files/xyz` is requested.

#### Settings

##### Path

The path to handle by this trigger. Glob patterns (\*, ?) are supported.
Examples:

- `/automagic/test`
- `/automagic/files/*` to handle all paths that start with `/automagic/files/`

The trigger with the longest path is preferred when multiple triggers match requested path since only one response can be written.
Examples: The first trigger is preferred when two triggers with paths `/automagic/test` and `/automagic/*` are available.

##### Port

The port of the server.

##### Bind to WiFi interface only

Whether to listen for HTTP requests on all interfaces or just on the WiFi interface.

##### Keep WiFi awake

Whether to keep the WiFi radio awake, otherwise the WiFi radio might turn off to save battery and a connection to your device is no longer possible.

##### Finish HTTP Response

Whether to finish the HTTP response by sending an empty response to the client.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `remote_host` — the name or IP of the remote host
- `remote_port` — the port of the remote host
- `request_path` — the decoded path of the request (e.g. `/automagic/test`)
- `method` — the HTTP method (e.g. GET, POST, PUT)
- `header_*` —
  All values of the headers. The name of the variable is built using the prefix `header_` and the name of the header by replacing dash with underscore and converting the name to lowercase.
  Examples:
  - Header `Accept` is stored in variable `header_accept`
  - Header `Accept-Encoding` is stored in variable `header_accept_encoding`Headers leading to an invalid variable name are ignored.
- `param_*` —
  All values of the request parameters. The name of the variable is built using the prefix `param_` and the name of the parameter by converting the name to lowercase.
  Example:
  - Parameter `test` is stored in variable `param_test`Parameters leading to an invalid variable name are ignored.
- `file_*` —
  All paths of the uploaded files. The name of the variable is built using the prefix `file_` and the name of the parameter by converting the name to lowercase.
  Example:
  - Parameter `File` is stored in a variable `file_file`Parameters leading to an invalid variable name are ignored.
- `http_headers` — Map containing all unmodified names and values of the received HTTP headers
- `http_params` — Map containing all unmodified names and values of the received HTTP parameters
- `http_files` — Map containing all unmodified form field names and paths to the uploaded files

---

### [Incoming Call](triggers/trigger_incoming_call.md)

The trigger **Incoming Call** is executed when a call is received depending on the criteria defined in the options.

Examples:

- Start recording in Gleeo Time Tracker when your employer calls.
- Send a mail containing the callers number and time to your mail account.

#### Settings

##### Incoming call numbers

The list of call numbers when the flow should be executed. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter on similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

Warning: The formatting of the incoming number depends on the operator in use. Some operators format the number as an international callnumber like +17001111111, local fixed line network numbers often use the local format.
You have to check the log file to see the exact formatting used or you can add an action **Notification on Screen** with text `{incoming_number}` to see the actual number.

##### Phone state

Defines the state of the call to trigger the flow. Selecting multiple states triggers the flow once for each state.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `incoming_number` — the number of the calling party or null when suppressed
- `call_state` — the state of the call (IDLE, RINGING, OFFHOOK)
- `call_missed_rejected` — true or false whether or not the call has been missed or rejected when the phone enters the idle state
- `contact_name` — the name of the contact if available
- `contact_company` — the company of the contact if available
- `contact_title` — the title of the contact if available
- `contact_note` — the note of the contact if available
- `contact_nickname` — the nickname of the contact if available
- `contact_email` — an email address of the contact if available
- `contact_groups` — the list of groups of the contact if available

---

### [Interruptions Mode](triggers/trigger_interruptions_mode.md)

The trigger **Interruptions Mode** is executed when the device switches to the desired interruption mode.

Examples:

- Disable some flows when no interruptions are allowed.

#### Settings

##### Interruptions Mode

The desired interruption mode.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [K-9 Mail Received](triggers/trigger_k9_mail_received.md)

The trigger **K-9 Mail Received** is executed when [K-9 Mail](https://play.google.com/store/apps/details?id=com.fsck.k9) receives a mail.

Examples:

- Play an alert sound when you receive a mail from the boss.

#### Settings

##### K9 Account List

The comma separated list of accounts to consider (case insensitive). Glob patterns (\*, ?) are supported.

##### Sender List

The comma separated list of sender mail addresses to consider (case insensitive). Glob patterns (\*, ?) are supported.

##### Subject List

The comma separated list of subjects to consider (case insensitive). Glob patterns (\*, ?) are supported.

##### Receiver List

The comma separated list of receiver mail addresses to consider (case insensitive). Glob patterns (\*, ?) are supported.

##### CC List

The comma separated list of CC-mail addresses to consider (case insensitive). Glob patterns (\*, ?) are supported.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `k9_account` — the K-9 Mail account of the mail
- `k9_folder` — the K-9 folder of the mail
- `k9_to` — the recipients of the mail
- `k9_from` — the sender of the mail
- `k9_from_self` — whether or not the mail was sent by yourself (only set on newer versions of K-9)
- `k9_subject` — the subject of the mail
- `k9_sent_date` — the date the mail has been sent
- `k9_cc` — the cc of the mail
- `k9_bcc` — the bcc of the mail

---

### [Launch Browser App Intent Received](triggers/trigger_launch_browser_app_intent_received.md)

The trigger **Launch Browser App Intent Received** is executed when an app or the system wants to launch a browser app.

Examples:

- Detect when the browser key is pressed on a hardware keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Launch Calculator App Intent Received](triggers/trigger_launch_calculator_app_intent_received.md)

The trigger **Launch Calculator App Intent Received** is executed when an app or the system wants to launch a calculator app.

Examples:

- Detect when the calculator key is pressed on a hardware keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Launch Calendar App Intent Received](triggers/trigger_launch_calendar_app_intent_received.md)

The trigger **Launch Calendar App Intent Received** is executed when an app or the system wants to launch a calendar app.

Examples:

- Detect when the calendar key is pressed on a hardware keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Launch Contacts App Intent Received](triggers/trigger_launch_contacts_app_intent_received.md)

The trigger **Launch Contacts App Intent Received** is executed when an app or the system wants to launch a contacts/address book app.

Examples:

- Detect when the contacts key is pressed on a hardware keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Launch Mail App Intent Received](triggers/trigger_launch_mail_app_intent_received.md)

The trigger **Launch Mail App Intent Received** is executed when an app or the system wants to launch a browser app.

Examples:

- Detect when the mail key is pressed on a hardware keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Launch Music App Intent Received](triggers/trigger_launch_music_app_intent_received.md)

The trigger **Launch Music App Intent Received** is executed when an app or the system wants to launch a music app.

Examples:

- Detect when the music key is pressed on a hardware keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Launcher Trigger](triggers/trigger_launcher_trigger.md)

The trigger **Launcher Trigger** is executed when the launcher entry with the name *Launcher Trigger* is manually started or when another app launches the entry.

Examples:

- Start a flow with the Bixby button.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Light Sensor](triggers/trigger_light_sensor.md)

The trigger **Light Sensor** is executed when the measured surrounding light intensity passes the defined value.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

#### Settings

##### Sensitivity

The sensitivity of the slider to define the light level.

##### Light Level

Whether the trigger should execute when the illuminance passes above or below a certain value and the level to use.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `light_level` — the effective illuminance in lux

---

### [Locale Adjusted](triggers/trigger_locale_adjusted.md)

The trigger **Locale Adjusted** is executed when the locale has been changed in the system.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `locale` — the new locale

---

### [Location](triggers/trigger_location.md)

The trigger **Location** is executed when the location is entering the defined region or exiting the defined region.
The accuracy of the location depends heavily on the available location provider.

Tip: Enabling GPS in the phone settings can yield much better location accuracy but might use more battery. Locations with WiFi access points might work accurate enough and GPS can be disabled in the global phone settings to reduce battery strain.

Examples:

- Start recording in Gleeo Time Tracker when you are in the office, stop recording when you leave.
- Switch the ringer to vibrate when you are at your office.
- Turn off the ringer in the church. (Do it manually when it is important!)
- Send an SMS when you are home.

Note: The location is usually checked every 4 minutes when the device is not actively used and the classic method is used. This can result in the GPS icon on the statusbar being visible every 4 minutes. Entering/exiting a location can be missed when you are moving fast through a location with a small radius and the 4 minute check misses the location.
Locations can be reported more often when the device is active or another application also uses the location features (for example when using Google Maps).

#### Settings

##### Method

The method used to detect the geofence.
*Modern* uses the new geofence API provided by Google and should be tuned to use only a minimum amount of battery power.
The algorithms to detect the locations are not known and can vary depending on device model. Please experiment with both methods to see what works best for you.

##### Location

The location used by this trigger.

##### Location Name

The name to use for this location. This name is used in the trigger name and to select an existing location on the map.

##### Radius

The radius around the location in meters.

##### Entering/Exiting

Whether to execute the flow when the location within the defined radius is entered or exited.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `location` — the configured location
- `location_name` — the name of the location
- `entering` — whether the location has been entered or not

---

### [Location Provider State](triggers/trigger_location_provider_state.md)

The trigger **Location Provider State** is executed when a location provider (GPS or Network) is enabled or disabled.

Examples:

- Deactivate a flow that uses GPS when GPS is turned off.

#### Settings

##### Location Provider

The location provider to monitor (GPS or Network)

##### Enabled/Disabled

Whether to trigger when the provider was enabled or disabled.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Login Attempt](triggers/trigger_login_attempt.md)

The trigger **Login Attempt** is executed, whenever someone unsuccessfully tries to login to the device respectively tries to unlock the device.

Examples:

- Take a picture with the front camera when someone enters the wrong PIN code three times.

#### Settings

##### Failed/Successful after failed

- **Failed:** executes the trigger when the login attempt fails
- **Successful after failed:** executes the trigger when the login attempt was successful after it failed one or multiple times before

##### When

- **On every failed attempt:** executes once for every failed attempt
- **On the Nth failed attempt:** executes the trigger exactly once when the number of failed login attempts reach the specified amount of times

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `failed_login_attempt` — the number of failed login attempts

---

### [Magnetic Field Sensor](triggers/trigger_magnetic_field_sensor.md)

The trigger **Magnetic Field Sensor** is executed when the measured magnetic field strength passes the defined value.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Execute a flow when the device is placed near a magnet.

#### Settings

##### Sensitivity

The sensitivity of the slider to define the light level.

##### Magnetic Field Strength

Whether the trigger should execute when the illuminance passes above or below a certain value and the level to use.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `magnetic_field_strength` — the measured strength in micro Tesla

---

### [Media Button Event (Experimental)](triggers/trigger_media_button_event.md)

The trigger **Media Button Event (Experimental)** executes a flow when the system detects a media button event, for example when the play-button is pressed on a headset.

Warning: When an audio player is launched, future events are usually sent to the audio player and not to Automagic anymore. If this is not the desired behaviour, Automagic has to be registered to receive the events again using an action **Reregister Media Button Receiver**.

#### Settings

##### Events

Whether the trigger should be executed for all media button events or only for a specific button.

##### Specific event

The Event/Button that should be reacted upon.
Wired headsets usually generate the event *Headset Hook*.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `key_code` — the numeric keycode
- `key_code_name` — the name of the keycode
- `key_duration` — the duration of the event in milliseconds
- `key_source_device_id` — the ID of the sending device

---

### [Media Session Changed (Experimental)](triggers/trigger_media_session_changed.md)

The trigger **Media Session Changed (Experimental)** is executed when the media session of the specified player changes (new track is played, media image is loaded etc.). A regular change in position alone does not invoke the trigger.

Examples:

- Show the title of the current track in an overlay widget.

#### Settings

##### Package Names

The name of the media player to monitor. Glob patterns (\*, ?) are supported.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `playback_state` — current state (0=none, 1=stopped, 2=paused, 3=playing, 4=fast forwarding, 5=rewinding, 6=buffering, 7=error, 8=connecting, 9=skip to previous, 10=skip to next, 11=skip to item in queue)
- `playback_position` — current position in ms
- `title` — the title
- `subtitle` — the subtitle
- `description` — the description
- `icon` — the current image
- `icon_uri` — the URI to load the image
- `media_duration` — duration of the track in ms

---

### [Mobile Datanetwork Type](triggers/trigger_mobile_datanetwork_type.md)

The trigger **Mobile Datanetwork Type** is executed when the network type switches to one selected in the list.

Examples:

- Play an alert sound when the network switches to GPRS.

#### Settings

##### Network Type

The network types to execute the trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_mobile_network_type` — the type of the network before
- `mobile_network_type` — the type of the network (0=Unknown, 1=GPRS, 2=EDGE, 3=UMTS, 4=CDMA, 5=CDMA - EvDo rev. 0, 6=CDMA - EvDo rev. A, 7=CDMA - 1xRTT, 8=HSDPA, 9=HSUPA, 10=HSPA, 11=iDEN, 12=CDMA - EvDo rev. B, 13=LTE, 14=CDMA - eHRPD, 15=HSPA+)

---

### [Next Alarm](triggers/trigger_next_alarm.md)

The trigger **Next Alarm** is executed when the next alarm set in the Android alarm app is reached.

Warning: This function is not officially supported by Android < 5.0 and might not work on all devices.

Examples:

- Start the coffee machine when you are woken up in the morning.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [NFC State](triggers/trigger_nfc_state.md)

The trigger **NFC State** is executed when the NFC adapter of the device is turned on or off depending on the settings used.

#### Settings

##### NFC state

Defines the NFC states to trigger the flow. Selecting multiple states triggers the flow once for each state.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `nfc_state` — the current state of the NFC adapter

---

### [NFC Tag](triggers/trigger_nfc_tag.md)

The trigger **NFC Tag** executes the flow when an NFC tag is detected.
You can either write a special ID to the NFC tag that will be used to identify the tag and execute the flow (this is the recommended option to use when you have a writable NFC tag) or you can also read the ID of an existing NFC tag. This is especially useful for read-only NFC tags like the ones often found in credit cards or read-only NFC tags (Live Tags, Smart Tags etc.) of some device manufacturers. Please also check the `Tip` in the settings section of this page.

Note: Not all NFC tags are supported.

Examples:

- Turn on the airplane mode when an NFC tag in the bedroom is scanned.

#### Settings

##### Tag Type

Whether an NFC tag is written using a specific ID defined in Automagic (recommended) or an existing NFC tag should be used (does not work with all tags, some devices show an app selection list when other apps are installed that also handle NFC tags).

##### Tag IDs

A comma separated list of tag IDs. Glob patterns can be used to match multiple tag IDs.

##### Write ID to NFC tag

Opens a screen to write the specified IDs to an NFC tag. The NFC tag must be writable and must be able to contain NDEF formatted data.
Multiple IDs can be written to the tag but the tag IDs must contain only regular characters, underscore and numbers.

Option **Write alternate tag information** on the writer screen allows to define whether or not different type of information should be written to the NFC tag.
Some devices show a warning dialog when a regular Automagic NFC tag is scanned since the tag contains a Web-URL.
Writing an alternate tag uses a different URL that avoids this warning message.

Android 4+: Option **Include Android Application Record** on the writer screen allows to define whether or not an additional AAR (Android Application Record) should be written to the tag.
An AAR uses slightly more space on the NFC tag but ensures that the tag is preferably handled by Automagic and not by another app.

##### Read ID from NFC Tag

Opens a screen to read the ID of an existing NFC tag. Glob patterns can be used to match multiple tag IDs.

Tip: Some devices contain apps that can handle generic NFC tags and are shown in a selection list when an NFC tag is scanned. Uninstall or deactivate unused apps when the selection dialog bugs you. You can deactivate apps in the system settings on an Android 4+ device (System settings->Apps->All, Select the app->Deactivate).
For example, you can disable the app **Tags** on a Galaxy Nexus to prevent the selection list from showing.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `nfc_tag_ids` — the scanned tag ID or a comma separated list when the tag contained multiple IDs

---

### [Notification on Screen Displayed](triggers/trigger_notification_screen_displayed.md)

The trigger **Notification on Screen Displayed** is executed when a notification is displayed on the screen.

Note: At least Android 4.0 (ICS) is required.

Examples:

- Read out the text of a notification.

#### Settings

##### Package Name

The comma separated list of apps that displayed the notification. Glob patterns can be used to match multiple packages.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `notification_message` — the text of the displayed notification
- `package_name` — the name of the package that displayed the notification
- `app_name` — the display name of the app

---

### [Notification on Statusbar Displayed](triggers/trigger_notification_status_bar_displayed.md)

The trigger **Notification on Statusbar Displayed** is executed when a notification is displayed in the statusbar.

Examples:

- Turn the screen on when Gmail app receives a mail.

#### Settings

##### Package Name

The comma separated list of apps that displayed the notification. Glob patterns can be used to match multiple packages.

##### Filter

Defines the text that must be contained in one of the available fields.

##### Ignore regular events

Defines whether or not the trigger should execute the flow for regular events.
A notification is considered *regular* when the notification is not marked as ongoing by the posting app.

##### Ignore ongoing events

Defines whether or not the trigger should execute the flow for ongoing events.
A notification is marked as an ongoing event by the application that posts the notification and is usually set when a notification shows some progress like a file download, an app is playing a sound, or an app is running as a foreground service.

##### Ignore group summary

Defines whether or not the trigger should execute the flow for group summaries.
A group summary is an additional notification that is used to group several related notifications together.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `title` — the title of the displayed notification
- `content_title` — the title of the content displayed by the notification
- `content_title_big` — the title of the big content displayed by the notification
- `notification_text` — the textual content of the notification
- `notification_text_big` — the textual content of the big, expanded view of the notification
- `notification_channel_id` — the ID of the notification channel
- `notification_priority` — the priority of the notification (-2=Minimum to 2=Maximum), when available
- `notification_large_icon` — the large icon of the notification, when available
- `notification_when` — the time shown in the notification
- `notification_number` — number shown in the notification, when available
- `notification_vibrate_default` — whether the notification vibrates using the default pattern
- `notification_vibrate_pattern` — vibration pattern as a list of numbers (pause duration in ms, vibrate duration in ms, ...), when available
- `notification_sound_default` — whether the notification should play the default notification sound
- `notification_sound_uri` — the URI of the sound to play, when available
- `notification_people` — a list of relevant people of the notification (list of URIs), when available
- `notification_info_text` — the info text displayed by the notification, when available
- `notification_sub_text` — the sub text displayed by the notification, when available
- `notification_summary_text` — the summary text displayed by the notification, when available
- `notification_progress` — the current progress shown by the notification, when available
- `notification_progress_max` — the maximum progress, when available
- `notification_progress_indeterminate` — whether the progress is indeterminate, when available
- `notification_text_lines` — the text lines shown by the notification, when available
- `notification_background_image_uri` — the URI of the background image to show, when available
- `notification_category` — the category of the notification, when available
- `notification_accent_color` — the accent color of the notification, when available
- `notification_ticker_text` — the scrolling text shown by the notification
- `notification_visibility` — the visibility of the notification (-1=secret, 0=private, 1=public)
- `notification_ongoing` — whether this is an ongoing event
- `notification_foreground_service` — whether this notification is used to mark a foreground service
- `notification_local_only` — whether the notification should be displayed on the local device only
- `notification_group` — the group key of the notification
- `notification_is_group_summary` — whether the notification is the group summary
- `package_name` — the name of the package that displayed the notification
- `app_name` — the display name of the app
- `id` — the id of the notification
- `buttons` — the list of buttons available on the big, expanded notification
- `wearable_actions` — the list of actions displayed on Android Wear

---

### [Notification on Statusbar Removed](triggers/trigger_notification_status_bar_removed.md)

The trigger **Notification on Statusbar Removed** is executed when a notification is removed from the statusbar.

Examples:

- Disable mobile data access when a music app displaying a notification is stopped.

#### Settings

##### Package Name

The comma separated list of apps that displayed the notification. Glob patterns can be used to match multiple packages.

##### Filter

Defines the text that must be contained in one of the available fields.

##### Ignore regular events

Defines whether or not the trigger should execute the flow for regular events.
A notification is considered *regular* when the notification is not marked as ongoing by the posting app.

##### Ignore ongoing events

Defines whether or not the trigger should execute the flow for ongoing events.
A notification is marked as an ongoing event by the application that posts the notification and is usually set when a notification shows some progress like a file download, an app is playing a sound, or an app is running as a foreground service.

##### Ignore group summary

Defines whether or not the trigger should execute the flow for group summaries.
A group summary is an additional notification that is used to group several related notifications together.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `title` — the title of the displayed notification
- `content_title` — the title of the content displayed by the notification
- `content_title_big` — the title of the big content displayed by the notification
- `notification_text` — the textual content of the notification
- `notification_text_big` — the textual content of the big, expanded view of the notification
- `notification_channel_id` — the ID of the notification channel
- `notification_when` — the time shown in the notification
- `notification_number` — number shown in the notification, when available
- `notification_vibrate_default` — whether the notification vibrates using the default pattern
- `notification_vibrate_pattern` — vibration pattern as a list of numbers (pause duration in ms, vibrate duration in ms, ...), when available
- `notification_sound_default` — whether the notification should play the default notification sound
- `notification_sound_uri` — the URI of the sound to play, when available
- `notification_people` — a list of relevant people of the notification (list of URIs), when available
- `notification_info_text` — the info text displayed by the notification, when available
- `notification_sub_text` — the sub text displayed by the notification, when available
- `notification_summary_text` — the summary text displayed by the notification, when available
- `notification_progress` — the current progress shown by the notification, when available
- `notification_progress_max` — the maximum progress, when available
- `notification_progress_indeterminate` — whether the progress is indeterminate, when available
- `notification_text_lines` — the text lines shown by the notification, when available
- `notification_background_image_uri` — the URI of the background image to show, when available
- `notification_category` — the category of the notification, when available
- `notification_accent_color` — the accent color of the notification, when available
- `notification_ticker_text` — the scrolling text shown by the notification
- `notification_visibility` — the visibility of the notification (-1=secret, 0=private, 1=public)
- `notification_ongoing` — whether this is an ongoing event
- `notification_foreground_service` — whether this notification is used to mark a foreground service
- `notification_local_only` — whether the notification should be displayed on the local device only
- `notification_group` — the group key of the notification
- `notification_is_group_summary` — whether the notification is the group summary
- `package_name` — the name of the package that displayed the notification
- `app_name` — the display name of the app
- `id` — the id of the notification

---

### [Notification on Statusbar Selected](triggers/trigger_notification_status_bar_selected.md)

The trigger **Notification on Statusbar Selected** executes the flow when a notification is selected that was previously shown using action **Notification on Statusbar**.

Example:

- Show a notification when the airplane mode is enabled by a flow. Turn airplane mode manually off when the notification in the statusbar is selected.

#### Settings

##### Notification

**Create own Notification**
Creates a new notification on the statusbar.

**Trigger on Notification from Action**
Trigger the flow when a notification supplied by action **Notification on Statusbar** was selected.

##### Icon

The icon to use for this notification.

Custom icons are supported starting with Android 6.

Note: Android will usually show all non-transparent parts as white so it's recommended to create custom PNG images with a transparent background and a white color to paint the contents.
Note: Option 'Custom icon' can lead to crashes on some devices with Android 6.0.

##### Title

The title of the notification.

##### Message

The message of the notification.

##### Play Sound

Plays the default notification sound when checked.

##### Vibrate

Vibrates when checked.

##### Flash LED

Flash the notification LED using the supplied color and blink rate. Notification LED and user defined colors are not supported on all devices.

##### Accent color

The color used by the device for in the notification (usually the background color of the icon in the expanded statusbar).

##### Ongoing

Flags this notification as an ongoing event and prevents the removal of this notification from the statusbar. A notification ID is mandatory when this option is selected.

##### Category (Android 5+)

The category of the notification. The category defines if a notification is allowed to pass the interruptions filter.

##### Priority (Android 4.1+)

Defines the priority of the notification. A notification with a low priority might be displayed in the expanded statusbar only (depends on Android version).

##### Visibility (Android 5+)

Whether notifications are secret, private or public which defines whether the notifications are displayed on the lock screen or not. The Lock screen must also be configured appropriately.

##### Notification IDs

Whether the trigger should be executed for one specific ID or for all notifications. The ID can be defined in the action **Notification on Statusbar**.

##### Big Message (Android 4.1+)

Defines a big message that will be displayed when the notification is expanded (by swiping down on the notification). The notification usually also shows the big message when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting.

##### Large Icon (Android 3+)

Defines whether a large icon should be displayed in the notification.

##### Group (Android 7+)

Defines the group of this notification.

##### Group summary (Android 7+)

Defines whether this notification is the group summary for this group.

##### Actions (Android 4.1+)

Up to three actions displayed as buttons when the notification is expanded (by swiping down on the notification). The notification usually also shows the action buttons when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting.

Tip: Use action **Execute Flows** to execute a complex flow consisting of multiple actions and conditions.

Following variables are supplied to the executed action:

- `action_number`: contains the number of the action (1, 2 or 3)
- `action_text`: the text label of the selected action button on the notification

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `notification_title` — the title of the notification
- `notification_message` — the message of the notification
- `notification_id` — the ID of the selected notification

---

### [Outgoing Call](triggers/trigger_outgoing_call.md)

The trigger **Outgoing Call** is executed when an outgoing call is made and the criteria defined in the options match.

Examples:

- Start recording in Gleeo Time Tracker when you call your employer.
- Send a mail containing the called number and time to your mail account.

#### Settings

##### Called Callnumber List

The list of call numbers when the flow should be executed. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter on similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

Warning: Verify that the called number is formatted to your expectations.
You have to check the log file to see the exact formatting used or you can add an action **Notification on Screen** with text `{called_number}` to see the actual number.

##### Phone state

Defines the state of the call to trigger the flow. Selecting multiple states triggers the flow once for each state.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `called_number` — the number of the called party
- `call_state` — the state of the call (IDLE, OFFHOOK)
- `contact_name` — the name of the contact if available
- `contact_company` — the company of the contact if available
- `contact_title` — the title of the contact if available
- `contact_note` — the note of the contact if available
- `contact_nickname` — the nickname of the contact if available
- `contact_email` — an email address of the contact if available
- `contact_groups` — the list of groups of the contact if available

---

### [Periodic Location Update](triggers/trigger_periodic_location_update.md)

The trigger **Periodic Location Update** is executed in periodic intervals and delivers a location to the executed flow.
The accuracy of the location heavily depends on the selected location provider.

Tip: The higher the time interval between updates the less battery will be used. A frequency of about 4 minutes is recommended.

Examples:

- Record the location every 5 minutes to a file.
- Send an SMS with your location every hour to someone.

#### Settings

##### Location Provider

The location provider to use.

**Network**
This provider uses the location provided by the cell tower and Wi-Fi signals. Depending on environment this provider can deliver location of about 60 meters of accuracy. Locations found using the cell tower can be very inaccurate (up to several kilometers or miles).

**Passive**
This provider delivers the location from the currently active provider (Network or GPS) without activating one of the providers by itself. This might result in very infrequent location updates.

**GPS**
This provider delivers the location using the GPS receiver. This provider usually uses more battery than the network provider.

**High Accuracy (Experimental)**
This provider delivers the finest available location using different sensors available on the device.

**Balanced Power/Accuracy (Experimental)**
This provider delivers the a location with an accuracy of about 100m and uses less battery than the high accuracy provider.

**Low Power (Experimental)**
This provider delivers the a location with an accuracy of about 10km.

**No Power (Experimental)**
This provider will only deliver locations when another app on the device has requested locations.

##### Frequency

The desired time between location updates. The actual time between location updates depends on the location provider when **Enforce Exact Frequency** is not checked.
A location provider (for example GPS) can ignore the specified frequency and deliver updates every few seconds.

##### Enforce Exact Frequency

Ensures that the location is provided in the intervals specified by **Frequency** even when the location provider delivers the location updates more often or less often.

##### Minimum Accuracy (in meters)

Only newer locations with at least the specified accuracy are passed to the flow.
This can be useful to filter out locations calculated using the cell tower when also more exact locations using WiFi are available.

##### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

##### Weekdays

The day on which the trigger should be active.

##### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

##### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

##### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `location` — the reported location
- `location_accuracy` — the accuracy of the location
- `location_altitude` — the altitude of the location when available
- `location_bearing` — the direction of travel in degrees East of true North when available
- `location_speed` — the speed of travel in meters per second when available

---

### [Periodic Timer](triggers/trigger_periodic_timer.md)

The trigger **Periodic Timer** is executed in the specified interval.

Examples:

- Remind about a recording task in Gleeo Time Tracker every 5 minutes.

#### Settings

##### Interval

Defines the time interval between flow executions.

##### Wake device when in sleep mode

Defines whether the device should be woken up from sleep mode.
Disabling this option saves a bit of battery but delays the trigger invocation for an unknown amount of time when the devices is asleep.

##### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

##### Weekdays

The day on which the trigger should be active.

##### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

##### At fixed times

Defines if the timer should execute the flow periodically in the set interval relative to midnight (or at the From-time when a limited time range is in effect).
If this option is not set, the interval starts at the moment when the trigger is enabled.

Examples when a flow is activated at 07:13:

- Option **not set**, Interval 1h: Flow executes at 08:13, 09:13, 10:13, ...
- Option **set**, Interval 1h: Flow executes at 08:00, 09:00, 10:00, ...
- Option **set**, Interval 1h, Time range 07:00 - 09:00: Flow executes at 08:00, 09:00 (next day: 07:00, 08:00, 09:00)
- Option **set**, Interval 1h, Time range 07:30 - 09:30: Flow executes at 07:30, 08:30, 09:30

Note that disabling *Wake device when in sleep mode* can delay the execution when the device is in deep sleep.

##### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

##### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Periodic Timer Inexact](triggers/trigger_periodic_timer_inexact.md)

The trigger **Periodic Timer Inexact** is executed approximately in the specified interval. The device can adjust the time of the trigger a bit and call the trigger when the device is currently also executing other tasks. This trigger uses less battery than the regular trigger **Periodic Timer**

Examples:

- Check approximately once an hour if a server is online.

#### Settings

##### Interval (Inexact)

Defines the time interval between flow executions. Android only supports the times available in this list.

##### Wake device when in sleep mode

Defines whether the device should be woken up from sleep mode.
Disabling this option saves a bit of battery but delays the trigger invocation for an unknown amount of time when the devices is asleep.

##### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

##### Weekdays

The day on which the trigger should be active.

##### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Phone Cell CDMA](triggers/trigger_phone_cell_cdma.md)

The trigger **Phone Cell CDMA** is executed when the device connects or disconnects from the defined cells. Changes within the defined list of cells don't invoke the trigger.

Warning: Some devices don't report the cell to Automagic when the screen is turned off.

Examples:

- Turn WiFi on, when the device connects to one of the cells at home.

#### Settings

##### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

##### Trigger when

Whether the trigger should execute the flow when connected/disconnected from an area defined by a list of cells or on every cell change (can be frequent).

##### Cell List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Cell List to Ignore

A comma separated list of cell IDs to ignore. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Connected / Disconnected

Whether the trigger should be executed when the device connects or disconnects from the listed cells. Changes within the defined list of cells don't invoke the trigger.

##### Wake device

Whether the trigger should wake the CPU of the device every X minutes or not. This is necessary for some devices when the cell is not updated regularly. Consumes more battery when a shorter time interval is chosen.

##### Turn screen on

Whether the display should be turned on briefly or not. This is necessary for some devices when the cell is not updated otherwise. This option increases battery consumption and should only be enabled when the cell is not updated otherwise.

##### Force update

Whether the cell update should be forced. This option increases battery consumption and should only be enabled when the cell is not updated otherwise.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `cell_id` — the cell id, null if unknown
- `base_station_id` — the ID of the base station , -1 if unknown
- `network_id` — the ID of the network, -1 if unknown
- `system_id` — the ID of the system, -1 if unknown
- `base_station_latitude` — the latitude of the base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `base_station_longitude` — the longitude of the base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `last_cell_id` — the last cell id, null if unknown or the trigger was just activated
- `last_base_station_id` — the last ID of the base station , -1 if unknown or the trigger was just activated
- `last_network_id` — the last ID of the network, -1 if unknown or the trigger was just activated
- `last_system_id` — the last ID of the system, -1 if unknown or the trigger was just activated
- `last_base_station_latitude` — the latitude of the last base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `last_base_station_longitude` — the longitude of the last base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `connected` — true when connected to the defined cells, false otherwise
- `disconnected` — true when disconnected from the defined cells, false otherwise

---

### [Phone Cell GSM](triggers/trigger_phone_cell_gsm.md)

The trigger **Phone Cell GSM** is executed when the device connects or disconnects from the defined cells. Changes within the defined list of cells don't invoke the trigger.

Warning: Some devices don't report the cell to Automagic when the screen is turned off.

Examples:

- Turn WiFi on, when the device connects to one of the cells at home.

#### Settings

##### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

##### Trigger when

Whether the trigger should execute the flow when connected/disconnected from an area defined by a list of cells or on every cell change (can be frequent).

##### Location Area Code (LAC) List

A comma separated list of location area codes. A location area is set of base stations and usually covers a large area. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Cell ID (CID) List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Cell ID (CID) List to Ignore

A comma separated list of cell IDs to ignore. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Connected / Disconnected

Whether the trigger should be executed when the device connects or disconnects from the listed cells. Changes within the defined list of cells don't invoke the trigger.

##### Wake device

Whether the trigger should wake the CPU of the device every X minutes or not. This is necessary for some devices when the cell is not updated regularly. Consumes more battery when a shorter time interval is chosen.

##### Turn screen on

Whether the display should be turned on briefly or not. This is necessary for some devices when the cell is not updated otherwise. This option increases battery consumption and should only be enabled when the cell is not updated otherwise.

##### Force update

Whether the cell update should be forced. This option increases battery consumption and should only be enabled when the cell is not updated otherwise.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `lac` — the currently connected cells location area code (LAC), -1 if unknown
- `cid` — the currently connected cells ID (CID), -1 if unknown
- `psc` — the currently connected cells primary synchronization code (PSC), -1 if unknown
- `last_lac` — the last connected cells location area code (LAC), -1 if unknown or the trigger was just activated
- `last_cid` — the last connected cells ID (CID), -1 if unknown or the trigger was just activated
- `last_psc` — the last connected cells primary synchronization code (PSC), -1 if unknown or the trigger was just activated
- `connected` — true when connected to the defined cells, false otherwise
- `disconnected` — true when disconnected from the defined cells, false otherwise

---

### [Phone Service State](triggers/trigger_phone_service_state.md)

The trigger **Phone Service State** is executed when the device detects the specified state.

Warning: Some devices don't send the current service state to applications when the screen is turned off. You can periodically use the action **Turn Screen On** to mitigate this problem.

Examples:

- Play a warning sound when no service is available.

#### Settings

##### SIM

The SIM card.

##### Phone Service State

**In Service**
Execute the flow when the telephony is back to regular operation.

**Out of Service**
Execute the flow when telephony becomes unavailable.

**Emergency Only**
Execute the flow when only emergency numbers can be called.

**Power Off**
Execute the flow when the radio is explicitly powered off.

##### Wake device

Whether the trigger should wake the CPU of the device every X minutes or not. Consumes more battery when a shorter time interval is chosen.

##### Turn screen on

Whether the display should be turned on briefly or not. This option increases battery consumption and should only be enabled when the values are not updated otherwise.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_service_state` — the previous service state (0=in service, 1=out of service, 2=emergency only, 3=power off)
- `service_state` — the current state of the service (0=in service, 1=out of service, 2=emergency only, 3=power off)
- `roaming` — boolean indicating the roaming status

---

### [Phone Signal Strength](triggers/trigger_phone_signal_strength.md)

The trigger **Phone Signal Strength** is executed when the signal strength falls under or raises over the specified value.

Warning: Some devices don't send the current signal strength to applications when the screen is turned off.

Examples:

- Play an alert when the signal strength becomes bad.

#### Settings

##### SIM

The SIM card.

##### Signal Strength Condition

Defines the condition that must be met to execute the flow:

**becomes lower than**
Executes the flow when the last reported value was above the defined level and the current value is below the defined level

**becomes higher than**
Executes the flow when the last reported value was below the defined level and the current value is above the defined level

**becomes equal to**
Executes the flow when the last reported value was different than the defined level and the current value equals the defined level

**lower than**
Executes the flow whenever the reported value by the system is below the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last value has been the same.

**higher than**
Executes the flow whenever the reported value by the system is above the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last value has been the same.

**exactly**
Executes the flow whenever the reported value by the system is exactly on the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last value has been the same.

##### Signal Strength

Defines the signal strength to use.

##### Wake device

Whether the trigger should wake the CPU of the device every X minutes or not. Consumes more battery when a shorter time interval is chosen.

##### Turn screen on

Whether the display should be turned on briefly or not. This option increases battery consumption and should only be enabled when the values are not updated otherwise.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `is_gsm` — true when GSM
- `signal_strength_level` — the signal strength in a value from 0 to 4 like the bars on a standard Android device
- `signal_strength_asu` — the signal strength in ASU (0-31)
- `gsm_signal_strength` — the GSM signal strength (0-31, 99 for unknown, -1 for unavailable)
- `gsm_bit_error_rate` — the GSM bit error rate (0-7, 99 for unknown, -1 for unavailable)
- `cdma_dbm` — the CDMA RSSI value in dBm (-1 for unavailable)
- `cdma_ecio` — the CDMA Ec/Io value in dB\*10 (-1 for unavailable)
- `evdo_dbm` — the EVDO RSSI value in dBm (-1 for unavailable)
- `evdo_ecio` — the EVDO Ec/Io value in dB\*10 (-1 for unavailable)
- `evdo_snr` — the EVDO signal to noise ratio (0-8, -1 for unavailable)
- `lte_dbm` — the LTE RSRP value in dBm (-1 for unavailable)

---

### [Plugin (Experimental)](triggers/trigger_plugin.md)

The trigger **Plugin (Experimental)** executes a flow when the condition of a plugin changes to `true` and/or `false`.
Warning: This function is experimental and might not work with all existing plugins available in Google Play. We can not provide support for plugins.

Note: Plugins can be defined using the interface description available from the app Locale: [Locale developer documentation](http://www.twofortyfouram.com/developer) and Tasker: [Tasker plugin extensions](http://tasker.dinglisch.net/plugins.html).

#### Settings

##### Plugin

List of all available plugins found on the device.

##### Condition

- **becomes true**: when the condition measured in the plugin changes from `false` or `undefined` to `true`
- **becomes false**: when the condition measured in the plugin changes from `true` or `undefined` to `false`

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `condition` — whether the condition became `true` or `false`

---

### [Plugin Event (Experimental)](triggers/trigger_plugin_event.md)

The trigger **Plugin Event (Experimental)** executes a flow when an event-plugin indicates an event.
Warning: This function is experimental and might not work with all existing plugins available in Google Play. We can not provide support for plugins.

Note: Plugins can be defined using the interface description available from the app Locale: [Locale developer documentation](http://www.twofortyfouram.com/developer) and Tasker: [Tasker plugin extensions](http://tasker.dinglisch.net/plugins.html).

#### Settings

##### Plugin

List of all available plugins found on the device.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Power Source](triggers/trigger_power_connected.md)

The trigger **Power Source** is executed when a power source is connected to the device (charger or USB cable).

Examples:

- Turn on WiFi when a power source is connected.
- Increase the screen brightness when a power source is connected.
- Set screen brightness to automatic when a power source is disconnected.

#### Settings

##### Power connected/disconnected

**Connected**
When selected executes the flow when a power source is connected.

- **AC Adapter**: when charging with the AC adapter
- **USB**: when charging over an USB connection
- **Wireless**: when charging wirelessly

**Disconnected**
When selected executes the flow when a power source is disconnected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery
- `battery_charge_counter` — Battery capacity in microampere-hours. null when not available
- `battery_current_now` — Instantaneous battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_current_average` — Average battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_energy_counter` — Battery remaining energy in nanowatt-hours. null when not available

---

### [Power Source (Android Wear)](triggers/trigger_power_connected_wear.md)

The trigger **Power Source (Android Wear)** is executed when a power source is connected to the device (charger or USB cable).

Examples:

- Turn on WiFi when a power source is connected.
- Increase the screen brightness when a power source is connected.
- Set screen brightness to automatic when a power source is disconnected.

#### Settings

##### Android Wear device

The target device.

##### Power connected/disconnected

**Connected**
When selected executes the flow when a power source is connected.

- **AC Adapter**: when charging with the AC adapter
- **USB**: when charging over an USB connection
- **Wireless**: when charging wirelessly

**Disconnected**
When selected executes the flow when a power source is disconnected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery
- `node_id` — the ID of the Wear node

---

### [Pressure Sensor](triggers/trigger_pressure_sensor.md)

The trigger **Pressure Sensor** is executed when the measured pressure of the pressure sensor rises above or declines below a certain level or when the pressure changes at least the specified amount in the given time.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Tip: If you need to check the pressure only every few minutes, it is recommended to use a condition **Pressure Sensor** since the condition will not use the sensor constantly and thus consumes less battery.

Examples:

- Execute a flow when the pressure changes when walking down a stair.

#### Settings

##### Type

- **Declines below**: executes the trigger when the measured pressure falls under a certain value
- **Rises above**: executes the trigger when the measured pressure rises above a certain value
- **Declines within duration**: executes the trigger when the measured pressure declines a certain amount within a given time
- **Rises within duration**: executes the trigger when the measured pressure rises a certain amount within a given time

##### Pressure (in mbar)

The pressure in millibar to compare.

##### Threshold

The minimal change in pressure before the trigger is executed again.

Example:
Type: **Declines below**, Pressure **1000mbar**, Threshold: **5mbar**
The trigger is executed when the pressure declines below 1000mbar. The pressure has to rise to at least 1005mbar again before the trigger is executed again.

##### Change (in mbar)

The change in pressure in mbar.

##### Duration

The duration the pressure change has to happen for the trigger to execute.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `pressure` — the measured pressure in mbar

---

### [Proximity Sensor](triggers/trigger_proximity_sensor.md)

The trigger **Proximity Sensor** is executed when the measured distance of the proximity sensor passes the defined distance.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

#### Settings

##### Distance (in cm)

Whether to execute the trigger when the distance passes above or below the defined distance and the distance in cm.

##### Keep device awake

Ensure that the device does not go into deep sleep while the action is executed. This option increases battery consumption and should only be enabled when the proximity sensor stops working when the display is turned off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `proximity` — the measured value of the proximity sensor

---

### [Quick Settings Tile Selected](triggers/trigger_quick_settings_tile_selected.md)

The trigger **Quick Settings Tile Selected** configures the selected quick settings tile and is executed when the tile is selected/clicked.

Tip: Action **Update Quick Settings Tile** can be used to change the icon, label or state of the tile.

Examples:

- Create a QS tile to send an SMS with the current location.

#### Settings

##### Tile

The tile to use.

##### Icon

The icon to use for the tile. [Variables are supported (replaced when trigger is activated).](#string-inline-expressions)

##### Label

The label of the tile. [Variables are supported (replaced when trigger is activated).](#string-inline-expressions)

##### Collapse panel

Whether or not the quick settings area should be closed when the tile is selected/clicked.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Ringer Mode](triggers/trigger_ringer_mode.md)

The trigger **Ringer Mode** is executed when the device switches to the specified ringer mode.

#### Settings

##### Ringer Mode

The desired ringer mode.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Screen Orientation](triggers/trigger_screen_orientation.md)

The trigger **Screen Orientation** is executed when the orientation of the device changes to portrait or landscape.

Examples:

- Change the active keyboard type depending on screen orientation.

#### Settings

##### Portrait or Landscape

Whether the trigger should be executed when the display changes to portrait or landscape.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Send/Share Intent Received](triggers/trigger_send_intent_received.md)

The trigger **Send/Share Intent Received** is executed when the send/share menu is used in an app and the data is shared with Automagic.

Examples:

- Share a URL in Google+ and directly send this link by SMS to one of your contacts.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `data_string` — the URI of the data this intent is targeting or null
- `mimetype` — the MIME type of the data being sent
- `text` — the data as text when available
- `stream_uri` — the URI of the data when available
- `html_text` — optional data as HTML when available
- `email` — the list of mail receivers when available
- `cc` — the list of mail addresses to CC
- `bcc` — the list of mail addresses to BCC
- `subject` — the subject when available

---

### [Send/Share Multiple Intent Received](triggers/trigger_send_multiple_intent_received.md)

The trigger **Send/Share Multiple Intent Received** is executed when the send/share menu is used in an app and multiple items are shared with Automagic.

Examples:

- Select multiple files in a file manager and share the files with Automagic.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `data_string` — the URI of the data this intent is targeting or null
- `mimetype` — the MIME type of the data being sent
- `texts` — the list of text items when available
- `stream_uris` — the list of URIs when available
- `html_texts` — optional texts as HTML when available
- `email` — the list of mail receivers when available
- `cc` — the list of mail addresses to CC
- `bcc` — the list of mail addresses to BCC
- `subject` — the subject when available

---

### [Shake](triggers/trigger_shake.md)

The trigger **Shake** is executed when the device is shaken.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Raise the screen brightness for 1 minute when the device is shaken.
- Turn silent mode on when the device is shaken.

#### Settings

##### Sensitivity

Defines how strong a shake must be to invoke the trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Shortcut](triggers/trigger_shortcut.md)

The trigger **Shortcut** is executed when a shortcut on the launcher is pressed.
You can create the shortcut and select an icon by pressing the **Install Shortcut** button.

Note: Starting with Android 8 the install shortcut button might not have any effect. In this case you can create the shortcut by saving the trigger then going to the launcher, long press a free area, select *Widgets* then *AM Shortcut* to create a new shortcut.

Examples:

- Turn WiFi on by pressing the shortcut.
- Launch a settings application screen by pressing the shortcut.
- Start recording in Gleeo Time Tracker by pressing the shortcut.

#### Settings

##### Title

The title/name of the shortcut to create. The title is used to identify the Shortcut-trigger in Automagic, which means that a shortcut can execute multiple triggers when two Shortcut-triggers use the same title. The title is passed to the launcher at the time when the button **Install Shortcut** is pressed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Shortcut (Android Wear)](triggers/trigger_shortcut_wear.md)

The trigger **Shortcut (Android Wear)** is executed when a shortcut in the list of Shortcut is selected (see Start -> Shortcut).

Examples:

- Turn WiFi on by pressing the shortcut.
- Launch a settings application screen by pressing the shortcut.
- Start recording in Gleeo Time Tracker by pressing the shortcut.

#### Settings

##### Title

The title/name of the shortcut to create. The title is used to identify the Shortcut-trigger in Automagic, which means that a shortcut can execute multiple triggers when two Shortcut-triggers use the same title.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `node_id` — the ID of the Wear node

---

### [Shutdown](triggers/trigger_shutdown.md)

The trigger **Shutdown** is executed before the device shutdown.
A flow is executed on a best effort basis, Automagic might not have enough time to execute the flow completely or some services or interfaces might already be unavailable when the shutdown is detected.

Examples:

- Vibrate before the device shuts down.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Significant Motion Detected](triggers/trigger_significant_motion_sensor.md)

The trigger **Significant Motion Detected** is executed when the special hardware sensor of the device detects a significant motion. Automagic can not configure how strong or how long the duration of the motion needs to be to activate the sensor.

Warning: This trigger hardware sensors of the device. This special hardware sensor used by this trigger should have a very low battery consumption.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [SIM State](triggers/trigger_sim_state.md)

The trigger **SIM State** is executed when the SIM state changes to one of the selected states.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play a warning sound when the SIM is removed.

#### Settings

##### SIM state changed to

Defines the SIM states to execute the trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_sim_state` — the previous state (0=unknown, 1=absent, 2=PIN required, 3=PUK required, 4=network locked, 5=ready)
- `sim_state` — the new state (0=unknown, 1=absent, 2=PIN required, 3=PUK required, 4=network locked, 5=ready)

---

### [SMS Received](triggers/trigger_sms_receive.md)

The trigger **SMS Received** is executed when an SMS is received depending on the criteria defined in the options.

Examples:

- Play a special alert when an SMS contains the keyword **Alert!**
- Send an SMS containing your location back to the SMS sender when the SMS contains **Where are you?**
- Read the received SMS aloud.
- Delete a password file on the SD card when the SMS contains **house search!**
- Play a repeating sound and vibrate when an SMS contains **device lost!**

Tip: Use a keyword or password that will not be part of a regular SMS to avoid unpleasant surprises.

#### Settings

##### SMS Sender List

The list of call numbers when the flow is executed. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter out similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

Warning: The formatting of the incoming number depends on the operator in use.
You have to check the log file to see the exact formatting used or you can add an action **Notification on Screen** with text `{sms_sender}` to see the actual number.

##### Contains Text

Only executes the flow when the text of the SMS contains the given text (no wildcards supported). The text is not case sensitive.

##### Prevent other apps from receiving the SMS

Prevents the default SMS application from receiving the SMS.

Warning: You may end up overlooking SMS you didn't intend to be matched (due to not having appeared in your messaging app).
Warning: This feature is not supported on Android 4.4+.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `sms_text` — the text of the SMS
- `sms_sender` — the sender of the SMS
- `contact_name` — the name of the contact if available
- `contact_company` — the company of the contact if available
- `contact_title` — the title of the contact if available
- `contact_note` — the note of the contact if available
- `contact_nickname` — the nickname of the contact if available
- `contact_email` — an email address of the contact if available
- `contact_groups` — the list of groups of the contact if available

---

### [SMS Sent](triggers/trigger_sms_sent.md)

The trigger **SMS Sent** is executed when an SMS is sent and stored as a sent SMS in the default SMS outbox of the standard Android SMS database.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Send every sent SMS as a mail to your mail account.

#### Settings

##### SMS Receiver List

The list of call numbers when the flow is executed. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter on similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

##### Contains Text

Only executes the flow when the text of the SMS contains the given text (no wildcards supported). The text is not case sensitive.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `sms_text` — the text of the SMS
- `sms_receiver` — the receiver of the SMS
- `contact_name` — the name of the contact if available
- `contact_company` — the company of the contact if available
- `contact_title` — the title of the contact if available
- `contact_note` — the note of the contact if available
- `contact_nickname` — the nickname of the contact if available
- `contact_email` — an email address of the contact if available
- `contact_groups` — the list of groups of the contact if available

---

### [Sound Level (Experimental)](triggers/trigger_sound_level.md)

The trigger **Sound Level (Experimental)** is executed when the recorded sound level in the environment exceed a certain level.

Warning: This condition records the environment sound using the microphone of the device which does not work, when another app already uses the microphone.

#### Settings

##### Average

If the current sound level should be considered or the duration to record and calculate the sound level.

##### Sensitivity

The sensitivity of the slider to define the sound level.

##### Sound Level

The sound level to check.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `sound_level` — the detected sound level

---

### [Speech Web Search Requested](triggers/trigger_speech_web_search_requested.md)

The trigger **Speech Web Search Requested** is executed when the speech recognition based search is initiated, for example by long-pressing the headset hook button.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `language_model` — `free_form`, `web_search` or null when not set
- `prompt` — prompt to show or null when not set
- `language` — the language code or null when not set
- `web_search_only` — if only a web search should be executed or whether also other actions should be executed
- `origin` — source of the trigger event or null when not set

---

### [Speed](triggers/trigger_speed.md)

The trigger **Speed** is executed when the measured speed of the GPS receiver rises above or declines below a certain level.

Warning: This trigger uses the GPS receiver and might increase battery usage (depending on device model).

Examples:

- Record the location in a file whenever you are driving faster than 120km/h.

#### Settings

##### Type

- **Declines below**: executes the trigger when the reported speed falls under a certain value
- **Rises above**: executes the trigger when the reported speed rises above a certain value

##### Speed

The speed to compare.

##### Unit

The unit of the speed.

##### Threshold

The minimal change in speed before the trigger is executed again.

Example:
Type: **Declines below**, Speed **40km/h**, Threshold: **10km/h**
The trigger is executed when the speed declines under 40km/h. The speed has to rise to at least 50km/h again before the trigger is executed again.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `location` — the reported location
- `location_accuracy` — the accuracy of the location
- `location_altitude` — the altitude of the location when available
- `location_bearing` — the direction of travel in degrees East of true North when available
- `location_speed` — the speed of travel in meters per second

---

### [Step counter](triggers/trigger_step_counter_sensor.md)

The trigger **Step counter** uses the Step counter/Pedometer of the device and executes a flow when the specified number of steps have been counted. The device can optimise the battery usage and inform Automagic less often when the display is turned off.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices do not count the steps when the screen is off.

Examples:

- Create a calendar event 'Training highly recommended' for the next day when less than 1000 steps have been counted for the day.

#### Settings

##### On every nth step (or less frequent)

Defines after how many steps a flow should be executed. The step counter can inform Automagic less often to save battery.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `step_count` — the number of steps since the trigger was enabled
- `step_count_total` — the number of steps counted by the sensor since the last reboot
- `last_step_time` — the point in time of the last detected step. Automagic attempts to provide a regular system time but might fail on some devices due to differences on ROMs.

---

### [Storage Media Event](triggers/trigger_storage_media_event.md)

The trigger **Storage Media Event** is executed when the system mounts or unmounts the SD card or makes other changes involving the storage media.

Examples:

- Disable a flow writing the location to the SD card when the sdcard is removed.

#### Settings

##### Event

Defines the event when the flow should be executed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `path` — the affected path

---

### [System Setting Changed](triggers/trigger_system_setting_changed.md)

The trigger **System Setting Changed** is executed whenever a setting in the systems setting database was changed.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play an alert when the system turns on the blocking mode.

#### Settings

##### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global Settings valid for all users of the device (Android 4.2+)

##### Name

The name of the setting to watch. Glob patterns are supported.

##### Variable

The name of the variable with the new value of the setting to pass to the flow.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `old_setting` — the value of the setting before it was changed
- `setting` — the new value of the setting
- `setting_name` — the name of the setting that changed. Especially useful when multiple settings are watched using a glob pattern.

---

### [System Setting Changed (Android Wear)](triggers/trigger_system_setting_changed_wear.md)

The trigger **System Setting Changed (Android Wear)** is executed whenever a setting in the systems setting database was changed.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play an alert when the system turns on the blocking mode.

#### Settings

##### Android Wear device

The target device.

##### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global Settings valid for all users of the device (Android 4.2+)

##### Name

The name of the setting to watch.

##### Variable

The name of the variable with the new value of the setting to pass to the flow.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `old_setting` — the value of the setting before it was changed
- `setting` — the new value of the setting
- `node_id` — the ID of the Wear node

---

### [Take Note (Android Wear)](triggers/trigger_take_note_wear.md)

The trigger **Take Note (Android Wear)** is executed when a note is taken from the Wear device.

Examples:

- Take a note and directly send the note by email to your inbox.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `note` — the text of the note
- `node_id` — the ID of the Wear node

---

### [Theater Mode (Android Wear)](triggers/trigger_theater_mode_wear.md)

The trigger **Theater Mode (Android Wear)** is executed when the theater mode is turned on or off.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Disable some flows when the theater mode is turned on.

#### Settings

##### Android Wear device

The target device.

##### Theater Mode

Whether the trigger should be executed when the theater mode is turned on or off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `node_id` — the ID of the Wear node

---

### [Time](triggers/trigger_time.md)

The trigger **Time** executes the flow regularly on the specified weekday and time.

Examples:

- Download a PDF newspaper every morning at 6am.
- Turn on airplane mode every evening at 11pm.
- Turn off airplane mode every morning at 6am.

#### Settings

##### Weekdays

The day on which the trigger should execute the flow.

##### Time

The time of the day when the trigger should execute the flow.

##### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

##### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Time Adjusted](triggers/trigger_time_adjusted.md)

The trigger **Time Adjusted** is executed when the time of the system is changed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Timezone Adjusted](triggers/trigger_timezone_adjusted.md)

The trigger **Timezone Adjusted** is executed when the timezone of the system has been changed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `timezone` — the new timezone

---

### [UI Event](triggers/trigger_user_interface_event.md)

The trigger **UI Event** executes a flow when the system detects a change in the user interface, for example when a window is opened, a button is pressed, a list is scrolled, text has been entered etc.

Note: The system informs Automagic not about all events. Some events that occur very frequently can be skipped by the system.

Examples:

- Execute a flow, when the Install button in Google Play is pressed.

#### Settings

##### Event Type

- *Window opened*: A new window, dialog or popup has been opened. The variable `text` often contains the title of the window.
- *Component clicked*: A button or label has been clicked. The variable `text` of image buttons is often empty.
- *Component long clicked*: A button or label has been long clicked. The variable `text` of image buttons is often empty.
- *Component selected*: An element has been selected, e.g. a row in a list or an element in a dropdown.
- *Component focused*: The input focus has been moved to another element.
- *Component scrolled*: A list has been scrolled.
- *Text changed*: The text in a text input fields has been changed.
- *Text selection changed*: The text selection or cursor position has been changed.
- *Announcement*: An app made an announcement like changing the page in a book.

##### Package Name

The list of apps to consider by this trigger. Glob patterns (\*, ?) are supported.

##### Text

The text that should be contained in the event.

##### Remove non-printable characters from text

Whether non-printable unicode characters should be removed from the text like left-to-right marks that might be used in components on the user interface.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `event_type` —
  the event represented by a number:
  - *Window opened*: `32`
  - *View clicked*: `1`
  - *View long clicked*: `2`
  - *View selected*: `4`
  - *View focused*: `8`
  - *Text changed*: `16`
  - *Text selection changed*: `8192`
  - *View scrolled*: `4096`
  - *Announcement*: `16384`
- `content_description` — the content description of the source
- `package_name` — the package name of originating app
- `source_class_name` — the class name of the source
- `source_bounds` — the position and size of the element (null when not determinable)
- `text` — the text of the source or the title of the opened window
- `label` — the label of the source
- `enabled` — whether the source is enabled
- `checked` — whether the source is checked
- `fullscreen` — whether the source is executed in fullscreen mode
- `password` — whether the source is a password field
- `scrollable` — whether the source can be scrolled
- `scroll_x` — the scroll offset of the source left edge in pixels
- `scroll_y` — the scroll offset of the source top edge in pixels
- `from_index` — from index of the element
- `to_index` — to index of the element
- `item_count` — number of elements in a list
- `current_item_index` — item position when the element is contained in a list
- `added_count` — number of added characters when a text is edited
- `removed_count` — number of removed characters when a text is edited
- `before_text` — text before it was changed
- `app_name` — the name of the originating app

---

### [User Activity (Experimental)](triggers/trigger_periodic_user_activity_update.md)

The trigger **User Activity (Experimental)** asks the device to periodically check most probably physical activity of the user like driving a car, riding a bike or walking.

Note: The detection of the current activity is a feature of the device provided by Google. Automagic can not change or improve the quality of the detected activity.

Examples:

- Check the activity every 5 minutes to measure how much time the user walks per day and how much time the user sits in the office.
- Increase the ringer volume when the user is driving in a car.

#### Settings

##### Trigger when

- **Activity detected**: execute the flow when the defined activity begins or ends.
- **Periodically**: execute the flow periodically even when the activity stays the same.

##### Activity

Defines which activity should trigger the flow. **Begin** executes the flow when the detected activity switches to the defined activity and was different before. **Ends** executed the flow when the defined activity was in progress before and is not detected anymore.

##### Enforce Exact Frequency

Ensures that the flow is executed exactly at the defined frequency even when the detected activity changes more or less frequent.

##### Check Frequency

The desired time between activity checks. The actual time between activity updates depends on the device when **Enforce Exact Frequency** is not checked.
The device can detect the activity more frequently when another app is interested in activity updates and uses a shorter update interval. Some devices turn off activity detection when activity `still` is detected and a low power sensor to detect device movement is available.

##### Minimum Confidence

The minimum confidence level to accept (0=unconfident, 100=confident).

##### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

##### Weekdays

The day on which the trigger should be active.

##### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

##### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

##### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `activity_name` — the name of the activity ("in\_vehicle", "on\_bicycle", "on\_foot", "still", "unknown", "tilting", "walking", "running")
- `activity_type` — the type of the activity as a number (0=in\_vehicle, 1=on\_bicycle, 2=on\_foot, 3=still, 4=unknown, 5=tilting, 7=walking, 8=running)
- `activity_confidence` — the confidence in a number from between 0=unconfident and 100=confident
- `activity_time` — the time when the activity was originally detected
- `detected_activities` — list of detected activities sorted by confidence (descending). Each item is a map containing activity\_name, activity\_type, activity\_confidence.

---

### [User Present](triggers/trigger_user_present.md)

The trigger **User Present** executes the flow when the user activates the device and passed the unlock screen.

Example:

- Start the browser when the device is unlocked at home.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [View Web URL Intent Received](triggers/trigger_view_web_url_intent_received.md)

The trigger **View Web URL Intent Received** is executed when an app wants to show a URL in a browser.

Examples:

- Receive a URL request and read the text on a weather site aloud, forwarding all other URL to the browser to be displayed as usual.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `data_string` — the received URL (http:// or https://)
- `categories` — the list of categories
- `scheme` — the scheme of the received intent
- `type` — the explicitly set MIME type of the received intent

---

### [Voice Command Requested](triggers/trigger_voice_command_requested.md)

The trigger **Voice Command Requested** is executed when the voice recognition by a bluetooth headset (or some other means) is requested.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed

---

### [Volume Long Press Event](triggers/trigger_volume_long_press_event.md)

The trigger **Volume Long Press Event** is executed when one of the volume keys is pressed down for a longer duration or hold and then released.

Note: `adb` has to be used to grant a permission to Automagic to use this feature:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.SET_VOLUME_KEY_LONG_PRESS_LISTENER`

Warning: This function is not officially supported by Android and might not work on all devices.
Warning: Activating this trigger prevents that holding the volume button for a longer duration changes the volume.
Warning: This trigger can miss Up events in case an app or dialog is shown while the volume key is held down.
Examples:

- Hold the volume down key pressed to skip to the next song.

#### Settings

##### Keys

The list of names of keys that should execute the trigger. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Press Duration

The minimum amount of time that the key has to be hold to execute the trigger. The Down action will be executed when the specified duration is reached, the up action as soon as the key is released.

##### Actions

Whether down, up or both actions should execute the trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `key_code` — the numeric keycode
- `key_code_name` — the name of the keycode
- `key_duration` — the duration of the event in milliseconds
- `key_source_device_id` — the ID of the sending device
- `key_action_down` — whether the action was down
- `key_action_up` — whether the action was up

---

### [WiFi Connected](triggers/trigger_wifi_connected.md)

The trigger **WiFi Connected** is executed when a connection with the defined network has been established.

Examples:

- Download a file as soon as WiFi is available.

#### Settings

##### SSID List

The list of SSIDs to execute the flow when connected. The list can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

##### Trigger on BSSID changes

Whether to execute the trigger when the BSSID changes (change of the accesspoint within the same SSID).

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `bssid` — the BSSID of the connected WiFi network
- `ssid` — the SSID of the connected WiFi network

---

### [WiFi Disconnected](triggers/trigger_wifi_disconnected.md)

The trigger **WiFi Disconnected** is executed when a connection with the defined network has been separated.

Examples:

- Play an alert when WiFi is not available anymore.
- Turn off flows causing big data transfers.

#### Settings

##### SSID List

The list of SSIDs to execute the flow when disconnected. The list can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `bssid` — the BSSID of the disconnected WiFi network
- `ssid` — the SSID of the disconnected WiFi network

---

### [WiFi Scan Results Available](triggers/trigger_wifi_scan_results_available.md)

The trigger **WiFi Scan Results Available** is executed when the results of a WiFi access point scan are available.

Examples:

- Connect to a free WiFi network when it becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `access_points` — the list of available access points

---

### [WiFi State](triggers/trigger_wifi_state.md)

The trigger **WiFi State** is executed when the devices wireless network adapter changes to one of the defined states.

Examples:

- Enable some download flows when WiFi is turned on.

#### Settings

##### WiFi States

The accepted states.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_wifi_state` — the wifi state (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=unknown)
- `wifi_state` — the wifi state (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=unknown)

---

### [WiFi Tethering State](triggers/trigger_wifi_tethering_state.md)

The trigger **WiFi Tethering State** is executed when the devices wireless network tethering setting changes to one of the defined states.

Examples:

- Play a notification sound when tethering is enabled.

#### Settings

##### WiFi Tethering States

The accepted states.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_tethering_wifi_state` — the wifi tethering state (10=disabling, 11=disabled, 12=enabling, 13=enabled, 14=failed) on older devices (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=failed)
- `wifi_tethering_state` — the wifi tethering state (10=disabling, 11=disabled, 12=enabling, 13=enabled, 14=failed) on older devices (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=failed)

---

### [Wired Headset Plugged](triggers/trigger_wired_headset_plugged.md)

The trigger **Wired Headset Plugged** is executed when a wired headset or earphones have been connected or disconnected.

Examples:

- Turn down the volume when the headset is connected.

#### Settings

##### Wired headset plugged/unplugged

**Plugged**
Execute the flow when the headset has been plugged.

**Unplugged**
Execute the flow when the headset has been unplugged.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `headset_type` — the type of the headset
- `microphone` — whether a microphone is available or not

---

## Conditions

### [Action Sound Playing](conditions/condition_action_sound_playing.md)

The condition **Action Sound Playing** checks if an action Sound is currently playing a sound.

Examples:

- Refresh a stop-button in a widget depending whether a sound is currently playing or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `sound_position` — the playback position of the sound in milliseconds (first sound if multiple playing), null when no sound is playing
- `sound_duration` — the total duration of the sound in milliseconds (first sound if multiple playing), null when the media framework of Android can not determine the duration (live stream etc.)

---

### [Active Cyanogen/LineageOS Profile](conditions/condition_active_cyanogen_mod_profile.md)

The condition **Active Cyanogen/LineageOS Profile** checks whether one of the listed profiles is active.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play a sound only when the active profile is not Cinema.

#### Settings

##### Profile Name List

The profile names to check. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `profile_name` — the name of the active profile

---

### [Active Network Type](conditions/condition_active_network_type.md)

The condition **Active Network Type** checks if a network (usually WiFi or Mobile) is active and usable for data traffic.

Examples:

- Execute a download action only when the current active network is WiFi.

#### Settings

##### Network Type

Defines for what network types the condition should be true

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `network_type` — the network type as number (None=-1, Mobile=0, WiFi=1, WiMAX=6, Bluetooth=7, Ethernet=9)
- `network_type_name` — the name of the network as string like `WIFI` or `MOBILE`
- `network_subtype` — the network subtype as number
- `network_subtype_name` — the network subtype as number
- `network_state` — the network state (CONNECTING, CONNECTED, SUSPENDED, DISCONNECTING, DISCONNECTED, UNKNOWN)
- `network_detailed_state` — the detailed network state (IDLE, SCANNING, CONNECTING, AUTHENTICATING, OBTAINING\_IPADDR, CONNECTED, SUSPENDED, DISCONNECTING, DISCONNECTED, FAILED, BLOCKED, VERIFYING\_POOR\_LINK, CAPTIVE\_PORTAL\_CHECK)
- `network_extra_info` — additional info as string (like SSID), when available
- `network_reason` — the reason of a failure, when available

---

### [Airplane Mode On](conditions/condition_airplane_mode_on.md)

The condition **Airplane Mode On** checks whether the airplane mode is on or not.

Examples:

- Only download a file when airplane mode is turned off.

---

### [Android Wear Device Connected](conditions/condition_android_wear_device_connected.md)

The condition **Android Wear Device Connected** checks whether a particular Android Wear device is currently connected to the main device.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play a notification shound only when not connected to the Android Wear device.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `node_id` — the ID of the Wear node
- `node_name` — the name of the Wear device

---

### [App Process Running](conditions/condition_app_process_running.md)

The condition **App Process Running** checks whether the process hosting an app is currently running.

Note: Android keeps processes in memory even when the process might not be required anymore and enough free memory is available.

Note: The official API used to access this information has been removed by Google on Android 5.1.1 which means that the condition is now marked as *not officially supported*.

Note: The unofficial workarounds to access this information don't work anymore on most devices running Android 7.

#### Settings

##### Package Name

The name of the process to check. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `pid` — the id of the process
- `importance` — the importance of the process. The smaller the value the higher the importance.
- `lru` — least recently used. Smaller value means more recently used.
- `process_state` — State of the process (2=Process hosting the current top activities)
- `uid` — the user id of the process

---

### [App Task Running](conditions/condition_app_task_running.md)

The condition **App Task Running** checks whether a task for one of the specified packages is currently running.

Warning: This function is not officially supported by Android 5+ and might not work on all devices.

#### Settings

##### Method

How the app should be determined. Method **Usage statistics** can be delayed on some devices.

##### Package Name

The name of the app to check. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### check most recent app task only

if only the most recent app task should be checked (this is the active app on many Android versions)

Warning: This option must be activated on Android 5+.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `package_name` — the package name of the foreground app
- `index` — the index of this task. An index of zero denotes the most recent running task.
- `base_activity` — the component launched as the first activity in the task
- `top_activity` — the activity component at the top of the history stack of the task
- `id` — a unique identifier for this task
- `num_running` — the number of activities that are currently running (not stopped and persisted) in this task
- `description` — a description of the task's current state

---

### [Audio Manager Mode](conditions/condition_audio_manager_mode.md)

The condition **Audio Manager Mode** checks whether the device is currently configured to use the desired audio manager mode.

#### Settings

##### Audio Manager Mode

The desired audio manager mode to check.

---

### [Audio Stream Active](conditions/condition_audio_stream_active.md)

The condition **Audio Stream Active** checks if the defined audio stream is currently in active use.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- check if a ringtone is currently played.

#### Settings

##### Audio Stream Type

The type of audio stream to check.

---

### [Audio Volume](conditions/condition_audio_volume.md)

The condition **Audio Volume** checks whether the volume of the selected stream type is above or below a certain level.

Examples:

- Execute a vibrate action only when the music volume is very low.

#### Settings

##### Sound Type

The type of the audio stream to check.

##### Condition

Whether the condition should check if the volume is above or below the volume level.

##### Volume

The volume value to check.

---

### [Auto Sync Enabled](conditions/condition_auto_sync_enabled.md)

The condition **Auto Sync Enabled** checks whether the automatic synchronisation is turned on or off either globally (the master switch) or for a specific account/authority.

Examples:

- Check the current state of auto sync to toggle the setting to the opposite value.

#### Settings

##### Global or Specific

Whether the global master switch should be checked or a specific account/authority.

##### Account

The account to check in format *Type*:*Name*. [Variables are supported.](#string-inline-expressions)

##### Authority

The part/database of the account to check. [Variables are supported.](#string-inline-expressions)

---

### [Auto-rotate Screen Enabled](conditions/condition_auto_rotate_screen_enabled.md)

The condition **Auto-rotate Screen Enabled** checks whether the system setting to automatically rotate the screen is enabled or not.

---

### [Battery Level](conditions/condition_battery_level.md)

The condition **Battery Level** checks whether the battery level is above or below a certain level.

Examples:

- Download a file only when the battery level is above 50%.

#### Settings

##### Battery Level

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported percentage by the system is below the defined level

**higher than**
true when the reported percentage by the system is above the defined level

**exactly**
true when the reported percentage by the system is exactly on the defined level

**full**
true when the reported battery status by the system is full

##### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery (1=unknown, 2=good, 3=overheat, 4=dead, 5=over voltage, 6=unspecified failure, 7=cold)
- `battery_charge_counter` — Battery capacity in microampere-hours. null when not available
- `battery_current_now` — Instantaneous battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_current_average` — Average battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_energy_counter` — Battery remaining energy in nanowatt-hours. null when not available

---

### [Battery Level (Android Wear)](conditions/condition_battery_level_wear.md)

The condition **Battery Level (Android Wear)** checks whether the battery level is above or below a certain level.

Examples:

- Download a file only when the battery level is above 50%.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Battery Level

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported percentage by the system is below the defined level

**higher than**
true when the reported percentage by the system is above the defined level

**exactly**
true when the reported percentage by the system is exactly on the defined level

**full**
true when the reported battery status by the system is full

##### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery (1=unknown, 2=good, 3=overheat, 4=dead, 5=over voltage, 6=unspecified failure, 7=cold)
- `node_id` — the ID of the Wear node

---

### [Battery Level BLE (Experimental)](conditions/condition_battery_level_ble.md)

The condition **Battery Level BLE (Experimental)** checks the battery level of a Bluetooth LE device that supports the standardized Battery service.

Warning: Bluetooth LE is not working reliable on many Android ROMs. Restarting the device or turning Bluetooth off and on again can help when the condition does not work.

Examples:

- Check once a week if the battery of the Polar heart rate sensor is still OK.

#### Settings

##### Bluetooth Device Address

The address of the bluetooth device. [Variables are supported.](#string-inline-expressions)

##### Bluetooth Device Name

The name of the bluetooth device.

##### Battery Level

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported percentage by the device is below the defined level

**higher than**
true when the reported percentage by the device is above the defined level

**exactly**
true when the reported percentage by the device is exactly on the defined level

##### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage

---

### [Battery Saver Mode Enabled](conditions/condition_power_save_mode_enabled.md)

The condition **Battery Saver Mode Enabled** checks whether the battery saver mode is active or not (Android 5+).
Warning: This function does not work for manufacturer specific battery saving modes like Samsungs (Ultra-)energy saving mode or Sony and HTC specific modes. Please use action **Init Variable System Setting** on such devices.

Examples:

- Execute a battery hungry flow only when the battery saver mode is not active.

---

### [Biometric Authentication Dialog](conditions/condition_biometric_authentication_dialog.md)

The condition **Biometric Authentication Dialog** shows the authentication dialog of the system and validates a biometric attribute like a fingerprint.

The dialog is temporarily not shown by the system when the fingerprint scanning failed a few times.

Examples:

- Show an authentication dialog for security reasons before deleting a file.

#### Settings

##### Title

The titel to show (mandatory). [Variables are supported.](#string-inline-expressions)

##### Subtitle

The subtitle to show (optional). [Variables are supported.](#string-inline-expressions)

##### Description

The description to show (optional). [Variables are supported.](#string-inline-expressions)

##### Cancel button label

The label of the cancel button (mandatory). [Variables are supported.](#string-inline-expressions)

##### Activate Timeout

Whether an automatic timeout should be used when the user does not react within the specified time.

##### Duration

The amount of time to automatically close the dialog and to continue the flow.

##### Value on Timeout

Whether the flow should be continued on the true- or false-branch.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `operation` — the operation used to close the dialog.

  Can be one of:
  - `success` when the user successfully authenticated
  - `failure` when the user failed to authenticate
  - `timeout` when the dialog was closed by a timeout
  - `cancel` when the user pressed the back button or back key
- `error_code` — Error code when the dialog was closed by an error
- `error_message` — Error description as text in case the dialog was closed by an error

---

### [Bluetooth Device Connected](conditions/condition_bluetooth_device_connected.md)

The condition **Bluetooth Device Connected** checks whether a connection to a Bluetooth device exists.

Warning: This function is not directly supported by Android. The list of currently connected Bluetooth devices is collected using connect/disconnect events reported to Automagic.
Under certain circumstances, the list of connected devices might not correspond to the list of really connected devices, for example when Automagic is freshly installed and a bluetooth device was already connected. In such cases, the bluetooth adapter must be disabled temporarily and reenabled in the preferences of Android to force the Bluetooth devices to reconnect.

Examples:

- Turn on WiFi in the evening only when one of the Bluetooth devices at home is connected.

#### Settings

##### Bluetooth Device

Defines whether the condition should check if at least one connection to a device exists or if the condition should check a specific device.

##### Bluetooth Device Address

The address of the bluetooth device. [Variables are supported.](#string-inline-expressions)

##### Bluetooth Device Name

The name of the bluetooth device.

##### Bluetooth Profile

Defines the type of connection to check. Not all device support all types.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `connected_devices_addresses` — list of addresses of the connected devices
- `connected_devices_names` — list of names of the connected devices

---

### [Bluetooth Enabled](conditions/condition_bluetooth_enabled.md)

The condition **Bluetooth Enabled** checks whether bluetooth is turned on or off.

Examples:

- Open an app when bluetooth is turned on.

---

### [Bluetooth LE Device Available](conditions/condition_bluetooth_le_device_available.md)

The condition **Bluetooth LE Device Available** executes a BT LE scan to test if a device is currently available.

Examples:

- Scan every 10 minutes if a BT LE beacon is available to turn WiFi on at home.

#### Settings

##### Bluetooth Device Address

The address of the bluetooth device. [Variables are supported.](#string-inline-expressions)

##### Bluetooth Device Name

The name of the bluetooth device.

##### Timeout

The maximum duration of the scan. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `rssi` — measured signal strength, 0 when not available

---

### [Bluetooth SCO On](conditions/condition_bluetooth_sco_on.md)

The condition **Bluetooth SCO On** checks whether communications use Bluetooth SCO or not.

---

### [Calendar Event](conditions/condition_calendar_event.md)

The condition **Calendar Event** checks, whether an event on the calendar is currently active.

Examples:

- Send an SMS to the calling number telling when your meeting ends.
- Don't let the SMS be read aloud in a meeting.

#### Settings

##### Starting

The start time offset the condition should consider an event as active.

##### Ending

The end time offset the condition should consider an event as active.

##### Calendars

A comma separated list of calendar names that should be checked for events. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

##### Titles

A comma separated list of event titles to match. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

Examples:

- `Plan*` matches titles like `Planning`, `Plan B` etc.

##### Descriptions

A comma separated list of event descriptions to match. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

##### Locations

A comma separated list of event locations to match. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

##### Event Type

Whether the trigger should consider all day events or regular events (not all day) or both.

##### Event Availability

Whether the trigger should consider events marked as free, busy or tentative.

##### Multiple Events

The event that should be preferred to fill the variables when multiple events match the defined criteria of the condition.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `event_calendar` — the name of the calendar of the event
- `event_title` — the title of the event
- `event_description` — the description of the event
- `event_location` — the location of the event
- `event_start` — the start time of the event
- `event_end` — the end time of the event
- `event_all_day` — boolean indicating if the event is all day or not
- `event_availability` — FREE, BUSY or TENTATIVE depending on the availability of the event
- `event_id` — the ID of the event

---

### [Call State](conditions/condition_call_state.md)

The condition **Call State** checks whether a call is currently active or not.

#### Settings

##### Phone state

The accepted states.

Note: State **Ringing** is only valid for incoming calls, an outgoing call directly changes the state from **Idle** to **Off-hook**

---

### [Confirmation Dialog](conditions/condition_confirmation_dialog.md)

The condition **Confirmation Dialog** shows a dialog with a question and continues flow execution depending on the button pressed.

Examples:

- Turn on bluetooth but ask for confirmation first.

#### Settings

##### Title

The optional title of the dialog. [Variables are supported.](#string-inline-expressions)

##### Question

The text of the question to ask. [Variables are supported.](#string-inline-expressions)

##### False Button / True Button

The text labels of the buttons that execute the true/false-branch of the condition. [Variables are supported.](#string-inline-expressions)

##### Behavior on Back button

Whether to ignore the back button or to confirm the dialog with true or false.

##### Activate Timeout

Whether an automatic timeout should be used when the user does not react within the specified time.

##### Duration

The amount of time to automatically close the dialog and to continue the flow.

##### Value on Timeout

Whether the flow should be continued on the true- or false-branch.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `operation` — the operation used to close the dialog.

  Can be one of:
  - `yes` when the user pressed the Yes-button
  - `no` when the user pressed the No-button
  - `timeout` when the dialog was closed by a timeout
  - `cancel` when the user pressed the back key and the appropriate option is set

---

### [Custom Widget Overlay Showing](conditions/condition_custom_widget_overlay_showing.md)

The condition **Custom Widget Overlay Showing** checks if a particular custom widget is currently showing as an overlay.

Note: Android sometimes temporarily hides overlays for security reasons. This condition can not detect this circumstance and might assume that the widget is showing.

Examples:

- Execute some actions of a flow only when a particular overlay is showing.

#### Settings

##### Overlay Name List

The names of the overlays to check. The condition evaluates to true when at least one of the overlays is showing. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

---

### [Debug Dialog](conditions/condition_debug_dialog.md)

The condition **Debug Dialog** shows a dialog containing all variables and the corresponding values in a dialog. Buttons can be used to control if the condition continues at **true** or **false**.

Examples:

- Debug a complex flow.

---

### [Device Idle/Doze Mode Active](conditions/condition_device_idle_mode_active.md)

The condition **Device Idle/Doze Mode Active** checks if the device is currently in idle/doze mode.

Examples:

- Only make network access from a flow when the device is not in idle/doze mode to save battery.

---

### [Device Orientation](conditions/condition_device_orientation.md)

The condition **Device Orientation** checks whether the device is in one of the specified orientation.

Examples:

- Beep every 5 minutes when recording your time but only when the device display is not facing down.

#### Settings

##### Device Orientation

The desired orientation of the device.

- **Face down:** The display of the device is facing down for example when lying on a table with the display towards the table.
- **Face up:** The display of the device is facing up for example when lying on a table with the display facing away from the table.
- **Face left:** The display faces to the left with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Face right:** The display faces to the right with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Standing upright:** The device is standing upright on a table.
- **Standing upside-down:** The device is standing upside-down on a table.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `accel_x` — the measured acceleration in m/s^2 on the X-axis
- `accel_y` — the measured acceleration in m/s^2 on the Y-axis
- `accel_z` — the measured acceleration in m/s^2 on the Z-axis

---

### [Device Storage Space](conditions/condition_device_storage_space.md)

The condition **Device Storage Space** checks the storage space on the filesystem containing the specified path.

Example:

- Check every morning if 100MB are still free on the SD card.

#### Settings

##### Filesystem

The path of the filesystem to check. [Variables are supported.](#string-inline-expressions)

##### Compare Free or Used Space

Whether to check the free or used space on the filesystem.

##### Size

The size to check.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `available_blocks` — the number of free blocks available to applications
- `free_blocks` — the number of free blocks inclusive reserved blocks not usable by applications
- `block_count` — the total number of blocks in the filesystem
- `block_size` — the size of the blocks in bytes
- `available_space` — the available space in bytes
- `used_space` — the used space in bytes

---

### [Device Storage Space Low](conditions/condition_device_storage_space_low.md)

The condition **Device Storage Space Low** checks whether the free space of the internal memory of the device is low.

Note: The amount of free space to consider as low is defined by the device manufacturer.
Standard Android considers less than 10% of free internal memory as low.

Example:

- Play a warning sound every 5 minutes when the device storage space is low.

---

### [Dock State](conditions/condition_dock_state.md)

The condition **Dock State** checks whether the device is in one of the docking states or not.

#### Settings

##### Dock States

The accepted docking states.

- **Docked Car**: in a car dock
- **Docked Desk**: in a desk dock
- **Docked Desk (High End, Digital)**: in a high end, digital dock
- **Docked Desk (Low End, Analog Dock)**: in a low end, analog dock
- **Docked Special**: in a special dock like a hardware keyboard for an ASUS Transformer
- **Undocked**: not in a dock

---

### [Execution Count](conditions/condition_execution_count.md)

The condition **Execution Count** checks whether the condition has been executed a certain amount of times. An internal counter is incremented whenever the condition is executed. The counter is reset to zero when the condition is met.

Examples:

- Play an alarm when 2 SMS are received within 5 minutes.
- Turn off the screen when the device is shook 2 times in 10 seconds.

#### Settings

##### Count

The count to compare. [Variables are supported.](#string-inline-expressions)

##### Timed

Only consider executions that happened within the given duration.

##### Duration

The maximum age of executions to consider.

---

### [Expression](conditions/condition_expression.md)

The condition **Expression** checks whether the expression is true or not.

Example Expressions:

- `a==1`
- `b > =3`
- `c < b AND a > 3`
- `(a--)==0`
- `startsWith(a, "test")`
- `a > addDays(b, 4)`
- `isEmpty(files)`

Examples:

- Check if the accuracy of a location is good enough: `location_accuracy<300`
- Check if a counter reached zero: `counter==0`

[See action Script for a description of the scripting language.](#scan-barcode)

#### Settings

##### Expression

The expression to evaluate.

Note: Variables can be used directly in an expression and don't need to be escaped using curly braces.

Example: use `location_accuracy` instead of `{location_accuracy}`.

---

### [Flashlight On](conditions/condition_flashlight_on.md)

The condition **Flashlight On** checks if the flashlight has been turned on by Automagic.

Warning: This condition can only check if the flashlight was turned on by Automagic but not if the flashlight has been turned on by another app.

---

### [Flow Enabled](conditions/condition_flow_enabled.md)

The condition **Flow Enabled** checks whether a flow is enabled or disabled.

#### Settings

##### Flow Name

The exact name of the flow to check. [Variables are supported.](#string-inline-expressions)

---

### [Flow Executing](conditions/condition_flow_executing.md)

The condition **Flow Executing** checks if a particular flow is currently executing.

Examples:

- Don't execute a flow when the flow is already executed.

#### Settings

##### Flow Name

The name of the flow to check. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `flow_execution_contexts` — how many times the flow is currently executing

---

### [Gleeo is Recording](conditions/condition_gleeo_recording.md)

The condition **Gleeo is Recording** checks whether **Gleeo Time Tracker** is currently recording a specific project or task.

#### Settings

##### Domain Filter List

A comma separated list of the domains to accept. [Variables are supported.](#string-inline-expressions)

##### Project Filter List

A comma separated list of the projects to accept. [Variables are supported.](#string-inline-expressions)

##### Task Filter List

A comma separated list of the tasks to accept. [Variables are supported.](#string-inline-expressions)

---

### [Gmail Unread Conversation Count](conditions/condition_gmail_unread_conversation_count.md)

The condition **Gmail Unread Conversation Count** checks the number of unread conversations available in the Gmail app on the device.

Examples:

- Play an alert sound every 5 minutes when unread conversations are available.

#### Settings

##### Condition

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported count is below the defined count

**higher than**
true when the reported count is above the defined count

**exactly**
true when the reported count is exactly matches the defined count

##### Unread Count

The number to compare in the condition.

##### Accounts

The accounts to check. The sum of unread conversations is checked when multiple accounts are specified. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `count` — the number of unread conversations

---

### [Hardware Keyboard State](conditions/condition_hardware_keyboard_state.md)

The condition **Hardware Keyboard State** checks whether the hardware keyboard of the device is currently open or closed.

Examples:

- Play an alert sound only when the keyboard is closed.

#### Settings

##### Open or Closed

Whether the condition should be true when the keyboard is open or closed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `keyboard_type` — the type of keyboard (1=unavailable, 2=QWERTY, 3=12-keys)

---

### [Hardware Keyboard Type](conditions/condition_hardware_keyboard_type.md)

The condition **Hardware Keyboard Type** checks if the currently connected hardware keyboard type matches one of the selected types.

#### Settings

##### Keyboard type

The type of keyboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `keyboard_type` — the type of keyboard (1=unavailable, 2=QWERTY, 3=12-keys)

---

### [Host Reachable](conditions/condition_host_reachable.md)

The condition **Host Reachable** tests whether a host can be reached by either opening a TCP-connection using a socket or by executing a ping command.

Examples:

- Check once an hour if a server can be reached or not.

#### Settings

##### Type

Type of the check:

- **Automatic**: Tries to connect to the host to port 7 to determine if the host is available. This method might use ping on some versions of Android.
- **Socket**: Tries to establish a TCP-connection to the specified host and port. The host is only considered to be reachable when the connection can be successfully established.
- **Ping**: Checks the reachability of the host using a `ping`-command (only one echo-request is sent). This option only works when the `ping`-command is available on the device.

##### Host

The host to check. [Variables are supported.](#string-inline-expressions)

##### Port

The port to connect to (only for type=Socket). [Variables are supported.](#string-inline-expressions)

---

### [Interruptions Mode](conditions/condition_interruptions_mode.md)

The condition **Interruptions Mode** checks if the device is in the specified interruption mode.

Examples:

- Only speak out an SMS when all interruptions are allowed.

#### Settings

##### Interruptions Mode

The mode to check.

---

### [Keyguard Locked](conditions/condition_keyguard_locked.md)

The condition **Keyguard Locked** checks whether or not the keyguard is currently active/showing.

---

### [Keyguard with Security](conditions/condition_keyguard_secure.md)

The condition **Keyguard with Security** checks whether a keyguard/lockscreen with a security element (PIN, password, ...) or not (None, Swipe) is set.

---

### [Light Sensor](conditions/condition_light_sensor.md)

The condition **Light Sensor** checks whether the measured value of the light sensor is below or above the defined level.

Warning: Some devices turn off the sensors when the screen is off.
Warning: Some devices can not determine the current value of the sensor and only deliver a value when the measured value of the sensor changes. This condition does not work on such devices.

#### Settings

##### Sensitivity

The sensitivity of the slider to define the light level.

##### Light Level

Whether the trigger should execute when the illuminance passes above or below a certain value and the level to use.

##### Timeout

The amount of time to wait for a value of the sensor, the condition is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `light_level` — the effective illuminance in lux

---

### [Location](conditions/condition_location.md)

The condition **Location** checks whether a location is inside a specific area or not. The condition can also check if an area is entered or exited by comparing the location of the last execution and the current location.

The condition uses the location already made available to the flow from a location trigger or uses the last known location of the system.
The condition fails when no location is available in the flow and the device does not have a last known location ready. This usually happens when the flow is executed manually. Either use one of the location triggers to execute your flow or explicitly acquire the location using an action **Init Variable Location** before the condition is reached.

Examples:

- Enable WiFi when you enter your office.
- Stop recording in **Gleeo Time Tracker** when you leave your office.

#### Settings

##### Location

The location used by this condition.

##### Location Name

The name to use for this location. This name is used in the condition name and to select an existing location on the map.

##### Radius

The radius around the location in meters.

##### Entering

True when the location was outside the defined location and is inside now.

##### Exiting

True when the location was inside the defined location and is outside now.

##### Ignore when previous state was not known

Ignore entering/exiting when the location has not been known before. This is usually the case when the flow is executed for the first time after starting **Automagic**.

##### Inside

True when the location is inside. This is also true when the location has been inside before and therefore is possibly true for every location provided by a trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `location` — the reported location
- `location_name` — the name of the location
- `entering` — whether the location has been entered or not
- `exiting` — whether the location has been exited or not
- `inside` — whether the location is inside the defined area or not

---

### [Location Entering](conditions/condition_location_entering.md)

The condition **Location Entering** checks whether an area has been entered or exited. This condition should only be used in conjunction with a **Location** trigger.

Examples:

- Enable WiFi when entering a location, disable WiFi when exiting the location.
- Start recording in **Gleeo Time Tracker** when coming to the office, stop recording when exiting the office.

#### Settings

##### Entering/Exiting

Whether the condition should be true when entering or when exiting the location.

---

### [Location Provider Enabled](conditions/condition_location_provider_enabled.md)

The condition **Location Provider Enabled** checks whether a particular location provider like GPS is enabled or not.

Examples:

- Report your location per SMS only when GPS is active.

#### Settings

##### Location Provider

The location provider to check.

**Network**
This provider uses the location provided by the cell tower and Wi-Fi signals. Depending on environment this provider can deliver location of about 60 meters of accuracy. Locations found using the cell tower can be very inaccurate (up to several kilometers or miles).

**Passive**
This provider delivers the location from the currently active provider (Network or GPS) without activating one of the providers by itself. This might result in very infrequent location updates.

**GPS**
This provider delivers the location using the GPS receiver. This provider usually uses more battery than the network provider.

---

### [Magnetic Field Sensor](conditions/condition_magnetic_field_sensor.md)

The condition **Magnetic Field Sensor** checks whether the measured value of the magnetic field sensor is below or above the defined level.

Warning: Some devices turn off the sensors when the screen is off.
Warning: Some devices can not determine the current value of the sensor and only deliver a value when the measured value of the sensor changes. This condition does not work on such devices.

Examples:

- Execute some actions only when the device is placed near a magnet.

#### Settings

##### Sensitivity

The sensitivity of the slider to define the field strength.

##### Magnetic Field Strength

Whether the trigger should execute when the illuminance passes above or below a certain value and the level to use.

##### Timeout

The amount of time to wait for a value of the sensor, the condition is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `magnetic_field_strength` — the measured strength in micro Tesla

---

### [Microphone Mute](conditions/condition_microphone_mute.md)

The condition **Microphone Mute** checks whether the microphone is currently muted.

Examples:

- Play a warning sound when the microphone is mute.

---

### [Mobile Datanetwork Enabled](conditions/condition_mobile_datanetwork_enabled.md)

The condition **Mobile Datanetwork Enabled** checks whether the mobile datanetwork is turned on or off.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Open an app when the mobile datanetwork is turned on.

---

### [Mobile Datanetwork Type](conditions/condition_mobile_datanetwork_type.md)

The condition **Mobile Datanetwork Type** checks if the current datanetwork type matches one selected in the list.

Examples:

- Download a PDF only when the network type is UMTS or LTE.

#### Settings

##### Network Type

The network types to accept.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `mobile_network_type` — the type of the network (0=Unknown, 1=GPRS, 2=EDGE, 3=UMTS, 4=CDMA, 5=CDMA - EvDo rev. 0, 6=CDMA - EvDo rev. A, 7=CDMA - 1xRTT, 8=HSDPA, 9=HSUPA, 10=HSPA, 11=iDEN, 12=CDMA - EvDo rev. B, 13=LTE, 14=CDMA - eHRPD, 15=HSPA+)

---

### [Music Active](conditions/condition_music_active.md)

The condition **Music Active** checks whether the music audio stream is currently in use.

Examples:

- Turn down the media volume when entering a location and the music is playing.

---

### [Network Connected](conditions/condition_network_connected.md)

The condition **Network Connected** checks if a network connection is currently available.

Examples:

- Check that a network connection is available before sending a mail.

---

### [NFC Enabled](conditions/condition_nfc_enabled.md)

The condition **NFC Enabled** checks whether NFC is turned on or off.

Examples:

- Play an alert sound when NFC is turned off when you enter the office.

---

### [Night Mode](conditions/condition_night_mode.md)

The condition **Night Mode** checks whether the device is currently configured to use the desired night mode.

#### Settings

##### Night Mode

The accepted night modes.

---

### [Notification on Statusbar Displayed](conditions/condition_notification_status_bar_displayed.md)

The condition **Notification on Statusbar Displayed** checks whether a notification of an app is displayed in the statusbar and supplies the information of the first matching notification as variables to the flow.

Examples:

- Check every 5 minutes if an Hangout message is displayed in the statusbar and play a notification sound.

#### Settings

##### Package Name

The comma separated list of apps that displayed the notification. Glob patterns can be used to match multiple packages. [Variables are supported.](#string-inline-expressions)

##### Notification ID

The ID of the notification. [Variables are supported.](#string-inline-expressions)

##### Filter

Defines the text that must be contained in one of the available fields. [Variables are supported](#string-inline-expressions) for *contains text* and *matches glob*.

##### Ignore regular events

Defines whether or not the condition should ignore regular events.
A notification is considered *regular* when the notification is not marked as ongoing by the posting app.

##### Ignore ongoing events

Defines whether or not the condition should ignore ongoing events.
A notification is marked as an ongoing event by the application that posts the notification and is usually set when a notification shows some progress like a file download, an app is playing a sound, or an app is running as a foreground service.

##### Ignore group summary

Defines whether or not the condition should ignore group summaries.
A group summary is an additional notification that is used to group several related notifications together.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `title` — the title of the displayed notification
- `content_title` — the title of the content displayed by the notification
- `content_title_big` — the title of the big content displayed by the notification
- `notification_text` — the textual content of the notification
- `notification_text_big` — the textual content of the big, expanded view of the notification
- `notification_channel_id` — the ID of the notification channel
- `notification_priority` — the priority of the notification (-2=Minimum to 2=Maximum), when available
- `notification_large_icon` — the large icon of the notification, when available
- `notification_when` — the time shown in the notification
- `notification_number` — number shown in the notification, when available
- `notification_vibrate_default` — whether the notification vibrates using the default pattern
- `notification_vibrate_pattern` — vibration pattern as a list of numbers (pause duration in ms, vibrate duration in ms, ...), when available
- `notification_sound_default` — whether the notification should play the default notification sound
- `notification_sound_uri` — the URI of the sound to play, when available
- `notification_people` — a list of relevant people of the notification (list of URIs), when available
- `notification_info_text` — the info text displayed by the notification, when available
- `notification_sub_text` — the sub text displayed by the notification, when available
- `notification_summary_text` — the summary text displayed by the notification, when available
- `notification_progress` — the current progress shown by the notification, when available
- `notification_progress_max` — the maximum progress, when available
- `notification_progress_indeterminate` — whether the progress is indeterminate, when available
- `notification_text_lines` — the text lines shown by the notification, when available
- `notification_background_image_uri` — the URI of the background image to show, when available
- `notification_category` — the category of the notification, when available
- `notification_accent_color` — the accent color of the notification, when available
- `notification_ticker_text` — the scrolling text shown by the notification
- `notification_visibility` — the visibility of the notification (-1=secret, 0=private, 1=public)
- `notification_ongoing` — whether this is an ongoing event
- `notification_foreground_service` — whether this notification is used to mark a foreground service
- `notification_local_only` — whether the notification should be displayed on the local device only
- `notification_group` — the group key of the notification
- `notification_is_group_summary` — whether the notification is the group summary
- `package_name` — the name of the package that displayed the notification
- `app_name` — the display name of the app
- `id` — the id of the notification
- `buttons` — the list of buttons available on the big, expanded notification
- `wearable_actions` — the list of actions displayed on Android Wear
- `count` — the number of notifications matching the condition

---

### [Phone Cell CDMA](conditions/condition_phone_cell_cdma.md)

The condition **Phone Cell CDMA** checks whether the phone is connected to one of the specified cells of interest.

Examples:

- Turn on WiFi when the phone cell at home is detected.

#### Settings

##### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

##### Cell List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `triggertime` — the time the trigger executed
- `cell_id` — the cell id, null if unknown
- `base_station_id` — the ID of the base station , -1 if unknown
- `network_id` — the ID of the network, -1 if unknown
- `system_id` — the ID of the system, -1 if unknown
- `base_station_latitude` — the latitude of the base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `base_station_longitude` — the longitude of the base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `neighboring_cells` — the list of neighboring cells. Null or empty if not available
- `cells` — the list of all known cells by the system. Null or empty if not available

---

### [Phone Cell GSM](conditions/condition_phone_cell_gsm.md)

The condition **Phone Cell GSM** checks whether the phone is connected to one of the specified cells of interest.

Examples:

- Turn on WiFi when the phone cell at home is detected.

#### Settings

##### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

##### Location Area Code (LAC) List

A comma separated list of location area codes. A location area is set of base stations and usually covers a large area. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Cell ID (CID) List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `lac` — the currently connected location area code (LAC), -1 if unknown
- `cid` — the currently connected cell ID (CID), -1 if unknown
- `psc` — the primary synchronization code (PSC), -1 if unknown
- `neighboring_cells` — the list of neighboring cells. Null or empty if not available
- `cells` — the list of all known cells by the system. Null or empty if not available

---

### [Phone Service State](conditions/condition_phone_service_state.md)

The condition **Phone Service State** checks whether the phone service is currently available, unavailable or only emergency calls can be placed.

Warning: Some devices don't send the current service state to applications when the screen is turned off.

#### Settings

##### SIM

The SIM card.

##### Phone Service state

The accepted states.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `service_state` — the state of the service (0=in service, 1=out of service, 2=emergency only, 3=power off)
- `roaming` — boolean indicating the roaming status

---

### [Phone Signal Strength](conditions/condition_phone_signal_strength.md)

The condition **Phone Signal Strength** checks whether the signal strength of the mobile network is above or below a certain level.

Warning: Some devices don't send the current signal strength to applications when the screen is turned off. You can use the options to periodically turn the screen on or wake the device.

Examples:

- Beep every five minutes when the network strength is very weak.

#### Settings

##### SIM

The SIM card.

##### Signal Strength Condition

Defines the condition that must be met to execute the flow:

**lower than**
true when the reported signal strength by the system is below the defined level

**higher than**
true when the reported signal strength by the system is above the defined level

**exactly**
true when the reported signal strength by the system is exactly on the defined level

##### Signal Strength

Defines the signal strength to use.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `is_gsm` — true when GSM
- `signal_strength_level` — the signal strength in a value from 0 to 4 like the bars on a standard Android device
- `signal_strength_asu` — the signal strength in ASU (0-31)
- `gsm_signal_strength` — the GSM signal strength (0-31, 99 for unknown, -1 for unavailable)
- `gsm_bit_error_rate` — the GSM bit error rate (0-7, 99 for unknown, -1 for unavailable)
- `cdma_dbm` — the CDMA RSSI value in dBm (-1 for unavailable)
- `cdma_ecio` — the CDMA Ec/Io value in dB\*10 (-1 for unavailable)
- `evdo_dbm` — the EVDO RSSI value in dBm (-1 for unavailable)
- `evdo_ecio` — the EVDO Ec/Io value in dB\*10 (-1 for unavailable)
- `evdo_snr` — the EVDO signal to noise ratio (0-8, -1 for unavailable)
- `lte_dbm` — the LTE RSRP value in dBm (-1 for unavailable)

---

### [Plugin (Experimental)](conditions/condition_plugin.md)

The condition **Plugin (Experimental)** checks the condition of a plugin.

Warning: This function is experimental and might not work with all existing plugins available in Google Play. We can not provide support for plugins.

Note: Plugins can be defined using the interface description available from the app Locale: [Locale developer documentation](http://www.twofortyfouram.com/developer) and Tasker: [Tasker plugin extensions](http://tasker.dinglisch.net/plugins.html).

#### Settings

##### Plugin

List of all available plugins found on the device.

##### replace variables/modify configuration

Script to dynamically replace variables and to modify the configuration passed to the plugin.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `Tasker variables` — takes over the local Tasker variables returned by the plugin (without leading %-character)

---

### [Power Source Connected](conditions/condition_power_connected.md)

The condition **Power Source Connected** checks whether the device is currently connected to a power source.

Examples:

- Turn on WiFi only when the device is connected to an AC adapter.

#### Settings

##### Power connected/disconnected

**Connected**
When a power source is connected.

- **AC Adapter**: when charging with the AC adapter
- **USB**: when charging over an USB connection
- **Wireless**: when charging wirelessly

**Disconnected**
When no power source is connected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery
- `battery_charge_counter` — Battery capacity in microampere-hours. null when not available
- `battery_current_now` — Instantaneous battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_current_average` — Average battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_energy_counter` — Battery remaining energy in nanowatt-hours. null when not available

---

### [Power Source Connected (Android Wear)](conditions/condition_power_connected_wear.md)

The condition **Power Source Connected (Android Wear)** checks whether the device is currently connected to a power source.

Examples:

- Turn on WiFi only when the device is connected to an AC adapter.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Power connected/disconnected

**Connected**
When a power source is connected.

- **AC Adapter**: when charging with the AC adapter
- **USB**: when charging over an USB connection
- **Wireless**: when charging wirelessly

**Disconnected**
When no power source is connected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery
- `node_id` — the ID of the Wear node

---

### [Pressure Sensor](conditions/condition_pressure_sensor.md)

The condition **Pressure Sensor** checks whether the measured pressure is below or above the defined value.

Warning: Some devices turn off the sensors when the screen is off.
Warning: Some devices can not determine the current value of the sensor and only deliver a value when the measured value of the sensor changes. This condition does not work on such devices.

#### Settings

##### Pressure (in mbar)

Whether the condition should check if the pressure is above or below the defined pressure.

##### Timeout

The amount of time to wait for a value of the sensor, the condition is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `pressure` — the measured pressure in mbar

---

### [Proximity Sensor](conditions/condition_proximity_sensor.md)

The condition **Proximity Sensor** checks whether the measured distance of the proximity sensor is below or above the defined distance.

Warning: Some devices turn off the sensors when the screen is off.
Warning: Some devices can not determine the current value of the sensor and only deliver a value when the measured value of the sensor changes. This condition does not work on such devices.

#### Settings

##### Distance (in cm)

Whether the condition should check if the distance is above or below the defined distance and the distance in cm.

##### Timeout

The amount of time to wait for a value of the sensor, the condition is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `proximity` — the measured value of the proximity sensor

---

### [Ringer Mode](conditions/condition_ringer_mode.md)

The condition **Ringer Mode** checks whether the device is currently configured to use the desired ringer mode.

#### Settings

##### Ringer Mode

The desired ringer mode to check.

---

### [Roaming](conditions/condition_roaming.md)

The condition **Roaming** checks whether you are currently in a roaming location.

Examples:

- Only download a file when you are not using a more expensive roaming tariff.

#### Settings

##### SIM

The SIM card.

---

### [Root Setting Enabled](conditions/condition_root_setting_enabled.md)

The condition **Root Setting Enabled** checks whether the Root setting in Automagic is enabled or not.

Examples:

- Execute an action only when root actions are allowed to be executed.

---

### [Screen Automatic Brightness Enabled](conditions/condition_screen_auto_brightness_enabled.md)

The condition **Screen Automatic Brightness Enabled** checks whether the setting to change the display brightness automatically depending on the environment is turned on or not.

---

### [Screen On](conditions/condition_screen_on.md)

The condition **Screen On** checks whether the screen is currently turned on.

Examples:

- Show an alert only when the display is on.

---

### [Screen Orientation](conditions/condition_screen_orientation.md)

The condition **Screen Orientation** tests whether the device is currently in portrait or landscape mode.

#### Settings

##### Portrait or Landscape

Whether the condition should check for portrait or landscape.

---

### [Service Running](conditions/condition_service_running.md)

The condition **Service Running** checks whether the specified service is currently running.

#### Settings

##### Service Class

The class name of the service to check. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `package_name` — the package name of the service
- `service_name` — the display name of the service
- `pid` — the process this service is running in
- `uid` — the user id owning this service
- `active_since` — the time this service has been started (in milliseconds since the device was booted)
- `last_activity_time` — the time this service was last active (in milliseconds since boot not counting sleep phases)
- `restarting` — the time when this service will be started, 0 when the service is currently running
- `foreground` — true when the service is run as a foreground process

---

### [Sound Level (Experimental)](conditions/condition_sound_level.md)

The condition **Sound Level (Experimental)** checks whether or not the environment sound exceed a certain level.

Warning: This condition records the environment sound using the microphone of the device which does not work, when another app already uses the microphone.

#### Settings

##### Average

The duration to record and calculate the sound level.

##### Sensitivity

The sensitivity of the slider to define the sound level.

##### Sound Level

The sound level to check.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `sound_level` — the detected sound level

---

### [Speakerphone On](conditions/condition_speakerphone_on.md)

The condition **Speakerphone On** checks whether speakerphone is turned on or off.

---

### [Telephony Radio Enabled](conditions/condition_telephony_radio_enabled.md)

The condition **Telephony Radio Enabled** checks if the radio of the phone is enabled or not.

Warning: This function is not officially supported by Android and might not work on all devices.

---

### [Theater Mode On (Android Wear)](conditions/condition_theater_mode_on_wear.md)

The condition **Theater Mode On (Android Wear)** checks whether the theater mode is turned on or not.

Warning: This function is not officially supported by Android and might not work on all devices.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

---

### [Time Range](conditions/condition_time_range.md)

The condition **Time Range** is true when the current time is in the defined time range.

Examples:

- Play an alert only during the day.

#### Settings

##### Weekdays

The day on which the condition should check the time range.

##### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

---

### [UI Mode](conditions/condition_ui_mode.md)

The condition **UI Mode** checks whether the device is currently in car, desk, TV or normal UI mode.

Note: Many devices only support the normal UI mode.

#### Settings

##### UI Mode

The UI mode to check.

---

### [USB Tethering Enabled](conditions/condition_usb_tethering_enabled.md)

The condition **USB Tethering Enabled** checks whether USB tethering is enabled or not.

Warning: This function is not officially supported by Android and might not work on all devices.

---

### [Vibrate on Ring Enabled](conditions/condition_vibrate_on_ring_enabled.md)

The condition **Vibrate on Ring Enabled** checks whether the setting to vibrate on ring is enabled or not.

Warning: This function is not officially supported by Android and might not work on all devices.

---

### [WiFi Access Point Enabled](conditions/condition_wifi_access_point_enabled.md)

The condition **WiFi Access Point Enabled** checks whether a WiFi configuration is enabled and the system is allowed to connect to this access point.

#### Settings

##### SSID

The SSID to check. [Variables are supported.](#string-inline-expressions)

---

### [WiFi Available](conditions/condition_wifi_available.md)

The condition **WiFi Available** checks whether one specific WiFi access point is currently available. The condition waits for the first available scan result when wifi has just been enabled and no scan result is available yet.

Note: Starting with Android 6, scan results are only provided to apps when the location services of the system are enabled.

Examples:

- Check if a specific free access point is available and enable this one.

#### Settings

##### SSID List

The comma separated list of SSIDs to accept. The condition is true when one of the access points in the list is available. Glob patterns can be used to match multiple SSIDs. [Variables are supported.](#string-inline-expressions)
The variables supplied by the condition relate to the available access point with the highest signal strength.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `access_points` — the list of available access point SSIDs
- `bssid` — the BSSID of the available access point
- `bssids` — the list of BSSIDs of the available access points
- `ssid` — the SSID of the WiFi network
- `capabilities` — the capabilities of the WiFi network
- `frequency` — the frequency of the WiFi network
- `level` — the signal strength level of the WiFi network

---

### [WiFi Connected](conditions/condition_wifi_connected.md)

The condition **WiFi Connected** checks whether the device is currently connected to one of the specified WiFi networks.

Examples:

- Start recording in **Gleeo Time Tracker** when you are in the office and connected to the wireless network.
- Enable a flow downloading big PDF files only when connected to your free wireless network at home.

#### Settings

##### SSID List

The comma separated list of SSIDs to accept. Glob patterns can be used to match multiple SSIDs. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `bssid` — the BSSID of the connected WiFi network
- `ssid` — the SSID of the connected WiFi network

---

### [WiFi Signal Level](conditions/condition_wifi_signal_level.md)

The condition **WiFi Signal Level** checks the signal level of the connected wifi network.

Note: The current signal strength has to be measured using a wifi scan when the display is turned off. A wifi scan can take a few seconds and increases battery consumption.

#### Settings

##### Signal Level Condition

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported level by the system is below the defined level

**higher than**
true when the reported level by the system is above the defined level

**exactly**
true when the reported level by the system is exactly on the defined level

##### Signal Level

Defines the level to compare (usually in range 0-4).

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `rssi` — the signal strength in dBm
- `signal_strength_level` — the signal strength mapped to levels (usually in range 0-4)

---

### [WiFi State](conditions/condition_wifi_state.md)

The condition **WiFi State** checks whether the device wireless network adapter is in the specified state.

#### Settings

##### WiFi States

The accepted states.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `wifi_state` — the wifi state (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=unknown)

---

### [WiFi Tethering State](conditions/condition_wifi_tethering_state.md)

The condition **WiFi Tethering State** checks whether the device wireless network adapter is in the specified state.

#### Settings

##### WiFi Tethering States

The accepted states.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `wifi_tethering_state` — the wifi tethering state (10=disabling, 11=disabled, 12=enabling, 13=enabled, 14=failed) on older devices (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=failed)

---

### [Wired Headset Plugged](conditions/condition_wired_headset_plugged.md)

The condition **Wired Headset Plugged** checks whether a wired headset is currently plugged in or not.

Examples:

- Turn the volume to maximum only when the headset is not plugged.

---

## Actions

### [Add WiFi Access Point](actions/action_add_wifi_access_point.md)

The action **Add WiFi Access Point** adds a new WiFi configuration and optionally connects to the new WiFi network.

Examples:

- Scan a barcode with WiFi connection information and directly connect to the new WiFi.

#### Settings

##### SSID

The SSID of the Access Point. [Variables are supported.](#string-inline-expressions)

##### Security

Whether to use WEP, WPA or no security. [Variables are supported.](#string-inline-expressions)

##### Password

The password. [Variables are supported.](#string-inline-expressions)

##### Activate

Whether or not to connect to the new WiFi network.

---

### [Answer Ringing Call](actions/action_answer_ringing_call.md)

The action **Answer Ringing Call** answers the currently-ringing call.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Automatically answer a call when you are prepared to answer calls but don't have your hands free.

#### Settings

##### Method

Defines the method to use to answer the call.

---

### [Call Number](actions/action_call_number.md)

The action **Call Number** calls a number by opening the telephone application and directly calling the supplied number.

Example:

- Automatically call a contact at 6pm.

#### Settings

##### SIM

The SIM card.

##### Number

The number to call. [Variables are supported.](#string-inline-expressions)

##### Directly initiate call

Whether the call should be initiated automatically or to only start the dialer interface without calling the number.

---

### [Clear Automagic Log](actions/action_clear_automagic_log.md)

The action **Clear Automagic Log** clears the internal log of Automagic (not the log on the SD-card when enabled in the preferences).

---

### [Close System Dialogs](actions/action_close_system_dialogs.md)

The action **Close System Dialogs** closes system dialogs like the expanded notification area, the expanded quick settings or the power-menu.
Whether dialog is classified as a system dialog or not is controlled by the dialog itself. Regular dialogs and windows can not be closed using this action.

---

### [Combine Images](actions/action_combine_images.md)

The action **Combine Images** allows to superimpose two images on top of each other. The images have to be loaded with action **Init Variable Image File**.

Note: The action has to create a copy of the image in memory so please ensure to scale down the images first when memory becomes an issue.

Examples:

- Superimpose a logo on an image as a watermark.

#### Settings

##### Variable with first image (DST)

The variable containing the base image. The result is saved in this variable. [Variables are supported.](#string-inline-expressions)

##### Variable with second image (SRC)

The variable containing the image to combine with the first one. [Variables are supported.](#string-inline-expressions)

##### Mode

How to combine the two images.

##### Alignment of second image

The alignment of the second image on the first one.

##### X/Y-Offset

The offset of the second image relative to the gravity. [Variables are supported.](#string-inline-expressions)

##### Opacity of second image

The opacity of the second image. [Variables are supported.](#string-inline-expressions)

---

### [Compare Images](actions/action_compare_images.md)

The action **Compare Images** compares two images pixel by pixel and provides an output image that shows the differences in the selected color and provides variables containing the total number of equal and different pixels.

Examples:

- Compare two screenshots to check if the screen contents differ.

#### Settings

##### Image 1 Variable

The name of the variable containing the first image to compare.

##### Top/Left Inset Image 1

The top/left inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](#string-inline-expressions)

##### Bottom/Right Inset Image 1

The bottom/right inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](#string-inline-expressions)

##### Image 2 Variable

The name of the variable containing the second image to compare.

##### Top/Left Inset Image 2

The top/left inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](#string-inline-expressions)

##### Bottom/Right Inset Image 2

The bottom/right inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](#string-inline-expressions)

##### Tolerance

The tolerance that specifies how different the two compared pixels on the two images are allowed to be to still be considered equal.[Variables are supported.](#string-inline-expressions)
Examples:

- 0=no tolerance, pixels have to be absolutely equal
- 0.1=a bit of tolerance, pixels can be a slightly different and still be considered equal

##### Output Color for Differences

The color to use on the resulting image to indicate the differences. Equal pixels are transparent on the resulting image.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `image_data` — the resulting image containing the different pixels in the specified color
- `equal_pixel_count` — the number of equal pixels
- `different_pixel_count` — the number of different pixels

---

### [Connect/Disconnect Bluetooth Device](actions/action_connect_disconnect_bluetooth_device.md)

The action **Connect/Disconnect Bluetooth Device** tries to connect/disconnect to/from a paired bluetooth device (Android 3+ required).

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Connect to the bluetooth headset when a shortcut is pressed.

#### Settings

##### Bluetooth Profile

Defines the type of connection to establish.

##### Bluetooth Device Address

The address of the bluetooth device. [Variables are supported.](#string-inline-expressions)

##### Bluetooth Device Name

The name of the bluetooth device.

##### Connect or disconnect

Whether to connect or disconnect.

---

### [Control Audio Player](actions/action_control_audio_player.md)

The action **Control Audio Player** can launch and control the default audio player of Android. Note that device and manufacturer specific audio players will probably not work.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Pause the audio player when the headphones are disconnected.

#### Settings

##### Control Type

Defines the method used to control the media player:

- **Media Button**: Simulates the press of a media button
- **Broadcast**: Sends a broadcast to the audio service

##### Media Button

The button to press (not all apps handle all buttons):

- **Play**: Starts to play (Android >3)
- **Play/Pause**: Toggles between play and pause
- **Pause**: Pauses the audio player (Android >3)
- **Stop**: Stops the audio player
- **Previous**: Plays the previous track
- **Next**: Plays the next track
- **Fast forward**: Fast forward
- **Rewind**: Rewind
- **Eject**: Ejects the media (for example a CD tray) (Android >3)
- **Close**: Closes the media tray (for example a CD tray) (Android >3)
- **Record**: Starts to record (Android >3)
- **Track**: Switches the audio track (Android >4.4)

##### send to specified app

Whether to let the system choose the app to handle the media button or if the media button event should be sent to a specific app. This is mostly useful when multiple audio players are installed and the event is not handled by the desired player.

##### Package Name

The app to send the media button event to. [Variables are supported.](#string-inline-expressions)

##### Class Name

The component inside the app that should handle the media button. [Variables are supported.](#string-inline-expressions)

##### Action

The action to execute:

- **Launch**: Launches the audio player
- **Play**: Starts to play
- **Play/Pause**: Toggles between play and pause
- **Pause**: Pauses the audio player
- **Stop**: Stops the audio player
- **Previous**: Plays the previous track
- **Next**: Plays the next track
- **Cycle Repeat**: Activates the next cycle mode
- **Toggle Shuffle**: Toggles the shuffle mode on/off

---

### [Control UI](actions/action_control_user_interface.md)

The action **Control UI** uses the accessibility features of the device to control the user interface and allows to automatically press buttons, long-click elements, scroll lists and change the values of checkboxes and radio buttons.

Note: This action controls the user interface by simulating user input, therefore the screen has to be active, unlocked and the user interface must be showing on screen.
The accessibility service of Automagic needs to be enabled in the preferences for this action to work. At least Android 4.1 (Jelly Bean) is required.

Note: Turning on the accessibility service is not possible on some devices when a screen brightness or screen filter app displays an overlay over other controls. Please disable such apps temporarily when pressing the OK button in system settings is not possible.

Examples:

- Start the location settings page and enable/disable GPS.
- Start the device update check by pressing the "Check now" button.

#### Settings

##### Script

Defines the actions to execute.
[See action Script for a description of the basic features of the scripting language.](#string-inline-expressions)

Warning: The following example scripts are highly device specific! Please only use the scripts for reference and don't just copy/paste the scripts. It might click the wrong control elements on your device.

Clear all notifications:
```
notifications();//to expand the notifications
sleep(1000);//wait one second for animations to complete
clicked = click("Clear all notifications");//click the button
if(not clicked) //check whether the button has been successfully clicked
{
    back();//hide the notification when the clear button was not available
}
```

Toggle GPS on/off:
Use an action **Launch App: Settings/Location services** to directly start the GPS settings page
```
sleep(1000);//wait for settings page to show
click("GPS satellites");//toggle setting on/off
sleep(500);
back();//go back to the previous screen
```

Open the Apps drawer:
```
home();//ensure the main home screen is showing
sleep(1000);//wait one second for animations to complete
click("Apps");//open the apps drawer
```

### Supported Functions

- `Boolean sleep(Number milliseconds)`
  Waits for the specified amount of `milliseconds`.
- `Boolean sleep(String duration)`
  Waits for the specified amount of `milliseconds`.
- `Boolean back()`
  Presses the back key.
- `Boolean home()`
  Presses the home key.
- `Boolean notifications()`
  Expands the statusbar.
- `Boolean quickSettings()`
  Opens the quick settings of the status bar.
- `Boolean recents()`
  Opens the recent application list.
- `Boolean powerDialog()`
  Opens the power long-press dialog. (Android 5+)
- `Boolean toggleSplitScreen()`
  Toggles the split screen mode. (Android 7+)
- `Boolean lockScreen()`
  Locks the screen (Android 9+)
- `Boolean takeScreenshot()`
  Takes a screenshot (Android 9+)
- `Boolean click(String pattern)`
  Clicks on the element containing the given glob `pattern`.
- `Boolean click(Number x, Number y)`
  Clicks on the element at the specified location.
- `Boolean clickById(String id)`
  Clicks on the element with the given `id`. (Android 4.3+)
- `Boolean clickByIdAndIndex(String id, Number index)`
  Clicks on the n-th element with the given `id`. (Android 4.3+)
- `Boolean touchGesture(Number startMillis, Number endMillis, List coordinates, ...)`
  Simulates touch screen input by replaying the given coordinates within the specified amount of time. (Android 7+)
- `Boolean longclick(String pattern)`
  Longclicks on the element containing the given glob `pattern`.
- `Boolean longclick(Number x, Number y)`
  Longclicks on the element at the specified location.
- `Boolean longclickById(String id, Number index)`
  Longclicks on the element with the given `id`. (Android 4.3+)
- `Boolean longclickByIdAndIndex(String id, Number index)`
  Longclicks on the n-th element with the given `id`. (Android 4.3+)
- `Boolean check(String pattern)`
  Checks the element containing the given glob `pattern`.
- `Boolean check(Number x, Number y)`
  Checks the element at the specified location.
- `Boolean checkById(String id, Number index)`
  Checks the element with the given `id`. (Android 4.3+)
- `Boolean checkByIdAndIndex(String id, Number index)`
  Checks the n-th element with the given `id`. (Android 4.3+)
- `Boolean isChecked(String pattern)`
  Tests whether the element containing the given glob `pattern` is checked.
- `Boolean isChecked(Number x, Number y)`
  Tests whether the element at the specified location is checked.
- `Boolean isCheckedById(String id)`
  Tests whether the element with the given `id` is checked. (Android 4.3+)
- `Boolean isCheckedByIdAndIndex(String id, Number index)`
  Tests whether the n-th element with the given `id` is checked. (Android 4.3+)
- `Boolean uncheck(String pattern)`
  Unchecks the element containing the given glob `pattern`.
- `Boolean uncheck(Number x, Number y)`
  Unchecks the element at the specified location.
- `Boolean uncheckById(String id)`
  Unchecks the element with the given `id`. (Android 4.3+)
- `Boolean uncheckByIdAndIndex(String id, Number index)`
  Unchecks the n-th element with the given `id`. (Android 4.3+)
- `Boolean scrollForward(String pattern)`
  Scrolls the element containing the given glob `pattern`.
- `Boolean scrollForward(Number x, Number y)`
  Scrolls the element at the specified location.
- `Boolean scrollForwardById(String id)`
  Scrolls the element with the given `id`. (Android 4.3+)
- `Boolean scrollForwardByIdAndIndex(String id, Number index)`
  Scrolls the n-th element with the given `id`. (Android 4.3+)
- `Boolean scrollBackward(String pattern)`
  Scrolls the element containing the given glob `pattern`.
- `Boolean scrollBackward(Number x, Number y)`
  Scrolls the element at the specified location.
- `Boolean scrollBackwardById(String id)`
  Scrolls the element with the given `id`. (Android 4.3+)
- `Boolean scrollBackwardByIdAndIndex(String id, Number index)`
  Scrolls the n-th element with the given `id`. (Android 4.3+)
- `Boolean select(String pattern)`
  Selects the element containing the given glob `pattern`.
- `Boolean select(Number x, Number y)`
  Selects the element at the specified location.
- `Boolean selectById(String id)`
  Selects the element with the given `id`. (Android 4.3+)
- `Boolean selectByIdAndIndex(String id, Number index)`
  Selects the n-th element with the given `id`. (Android 4.3+)
- `Boolean clearSelection(String pattern)`
  Unselects the element containing the given glob `pattern`.
- `Boolean clearSelection(Number x, Number y)`
  Unselects the element at the specified location.
- `Boolean clearSelectionById(String id)`
  Unselects the element with the given `id`. (Android 4.3+)
- `Boolean clearSelectionByIdAndIndex(String id, Number index)`
  Unselects the n-th element with the given `id`. (Android 4.3+)
- `Boolean focus(String pattern)`
  Focuses the element containing the given glob `pattern`.
- `Boolean focus(Number x, Number y)`
  Focuses the element at the specified location.
- `Boolean focusById(String id)`
  Focuses the element with the given `id`. (Android 4.3+)
- `Boolean focusByIdAndIndex(String id, Number index)`
  Focuses the n-th element with the given `id`. (Android 4.3+)
- `Boolean expand(String pattern)`
  Expands the element containing the given glob `pattern`. (Android 4.4+)
- `Boolean expand(Number x, Number y)`
  Expands the element at the specified location. (Android 4.4+)
- `Boolean expandById(String id)`
  Expands the element with the given `id`. (Android 4.4+)
- `Boolean expandByIdAndIndex(String id, Number index)`
  Expands the n-th element with the given `id`. (Android 4.4+)
- `Boolean collapse(String pattern)`
  Collapses the element containing the given glob `pattern`. (Android 4.4+)
- `Boolean collapse(Number x, Number y)`
  Collapses the element at the specified location. (Android 4.4+)
- `Boolean cut()`
  Cuts the text of the focused element. (Android 4.3+)
- `Boolean cut(String pattern)`
  Cuts the text of the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean cut(Number x, Number y)`
  Cuts the text of the element at the specified location. (Android 4.3+)
- `Boolean cutById(String id)`
  Cuts the text of the element with the given `id`. (Android 4.3+)
- `Boolean cutByIdAndIndex(String id, Number index)`
  Cuts the text of the n-th element with the given `id`. (Android 4.3+)
- `Boolean copy()`
  Copies the text of the focused element. (Android 4.3+)
- `Boolean copy(String pattern)`
  Copies the text of the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean copy(Number x, Number y)`
  Copies the text of the element at the specified location. (Android 4.3+)
- `Boolean copyById(String id)`
  Copies the text of the element with the given `id`. (Android 4.3+)
- `Boolean copyByIdAndIndex(String id, Number index)`
  Copies the text of the n-th element with the given `id`. (Android 4.3+)
- `Boolean paste()`
  Pastes text to the focused element. (Android 4.3+)
- `Boolean paste(String pattern)`
  Pastes text to the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean paste(Number x, Number y)`
  Pastes text to the element at the specified location. (Android 4.3+)
- `Boolean pasteById(String id)`
  Pastes text to the element with the given `id`. (Android 4.3+)
- `Boolean pasteByIdAndIndex(String id, Number index)`
  Pastes text to the n-th element with the given `id`. (Android 4.3+)
- `Boolean setSelection2(Number start, Number end)`
  Sets the selection of the focused element to the defined range. (Android 4.3+)
- `Boolean setSelection2(String pattern, Number start, Number end)`
  Sets the selection of the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean setSelection2(Number x, Number y, Number start, Number end)`
  Sets the selection of the element at the specified location. (Android 4.3+)
- `Boolean setSelection2ById(String id, Number start, Number end)`
  Sets the selection of the element with the given `id`. (Android 4.3+)
- `Boolean setSelection2ByIdAndIndex(String id, Number index, Number start, Number end)`
  Sets the selection of the n-th element with the given `id`. (Android 4.3+)
- `Boolean dismiss(String pattern)`
  Dismisses the element containing the given glob `pattern`. (Android 4.4+)
- `Boolean dismiss(Number x, Number y)`
  Dismisses the element at the specified location. (Android 4.4+)
- `Boolean dismissById(String id)`
  Dismisses the element with the given `id`. (Android 4.4+)
- `Boolean dismissByIdAndIndex(String id, Number index)`
  Dismisses the n-th element with the given `id`. (Android 4.4+)
- `String getText()`
  Returns the text of the focused element.
- `String getText(String pattern)`
  Returns the text of the element containing the given glob `pattern`.
- `String getText(Number x, Number y)`
  Returns the text of the element at the specified location.
- `String getTextById(String id)`
  Returns the text of the element with the given `id`. (Android 4.3+)
- `String getTextByIdAndIndex(String id, Number index)`
  Returns the text of the n-th element with the given `id`. (Android 4.3+)
- `String getContentDescription()`
  Returns the content description of the focused element.
- `String getContentDescription(String pattern)`
  Returns the content description of the element containing the given glob `pattern`.
- `String getContentDescription(Number x, Number y)`
  Returns the content description of the element at the specified location.
- `String getContentDescriptionById(String id)`
  Returns the content description of the element with the given `id`. (Android 4.3+)
- `String getContentDescriptionByIdAndIndex(String id, Number index)`
  Returns the content description of the n-th element with the given `id`. (Android 4.3+)
- `String getTextInActiveWindow()`
  Returns the text of all text elements. The order of the text elements can differ from the visual position.
- `String getContentDescriptionInActiveWindow()`
  Returns the content description of all elements. The order of the text elements can differ from the visual position.
- `Boolean setText2(String pattern, String text)`
  Sets the text of the element containing the given glob `pattern`. (Android 5+)
- `Boolean setText2(Number x, Number y, String text)`
  Sets the text of the element at the specified location. (Android 5+)
- `Boolean setText2ById(String id, String text)`
  Sets the text of the element with the given `id`. (Android 5+)
- `Boolean setText2ByIdAndIndex(String id, Number index, String text)`
  Sets the text of the n-th element with the given `id`. (Android 5+)
- `List getBounds(String pattern)`
  Returns the bounds of the element containing the given glob `pattern` in a list with the values [x, y, width, height].
- `List getBoundsById(String id)`
  Returns the bounds of the element with the given `id` in a list with the values [x, y, width, height]. (Android 4.3+)
- `List getBoundsByIdAndIndex(String id, Number index)`
  Returns the bounds of the n-th element with the given `id` in a list with the values [x, y, width, height]. (Android 4.3+)
- `Boolean existsElementById(String id)`
  Returns true when the element with the given `id` exists on the current window. (Android 4.3+)
- `Boolean existsElementByIdAndIndex(String id, Number index)`
  Returns true when the n-th element with the given `id` exists on the current window. (Android 4.3+)
- `Number getNumberOfElementsWithId(String id)`
  Returns number of elements with the defined `id` on the current window. (Android 4.3+)
- `Boolean sendKey(Number keyCode)`
  Simulates the specified key (Automagic input method required).
- `Boolean sendKey(String keyCodeName)`
  Simulates the specified key (Automagic input method required).
- `Boolean sendKey(String keyCodeName, String metaKey, ...)`
  Simulates the specified key with meta key state (Automagic input method required).
- `Boolean sendText(String text)`
  Sends the text to the focused component (Automagic input method required).
- `Boolean setText(String text)`
  Sets the text of the focused component (Automagic input method required).
- `Boolean setSelection(Number start, Number end)`
  Sets the selection of the focused component (Automagic input method required).
- `List getSelection()`
  Returns the start and end position of the cursor in a list with the values [start, end] (Automagic input method required).
- `Boolean selectAll()`
  Selects the text of the focused component (Automagic input method required).

---

### [Copy File](actions/action_copy_file.md)

The action **Copy File** locally copies a file.

Examples:

- Create a weekly backup of the Automagic flows to a file containing the timestamp.

#### Settings

##### Source File

The absolute path of the file to copy. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`

##### Target File (including filename)

The absolute path of the target file. The path has to include the filename of the target file. [Variables are supported.](#string-inline-expressions)

---

### [Copy Files](actions/action_copy_files.md)

The action **Copy Files** locally copies one or a list of files to the specified target directory or file.

Examples:

- Backup all files in directory `/mnt/sdcard/xyz/` to the folder `/mnt/sdcard/xyz_backup/`.

#### Settings

##### Source Files

A comma separated list of files or directories to copy. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

When multiple files are matched, the target has to be a directory. The directory will be created when it does not exist yet.
A directory with an ending slash (like `/mnt/sdcard/`) matches the files contained in the directory like using `/mnt/sdcard/*`.

##### Target

The absolute path of the target file or directory. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Copy Text from Clipboard](actions/action_copy_text_from_clipboard.md)

The action **Copy Text from Clipboard** copies the text on the clipboard to the specified variable.

Examples:

- Send the text on the clipboard directly by sms or text.

#### Settings

##### Variable

The name of the variable to store the content of the clipboard.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `clip_data` — the text of the clipboard

---

### [Copy Text to Clipboard](actions/action_copy_text_to_clipboard.md)

The action **Copy Text to Clipboard** copies the specified text to the clipboard.

Examples:

- Copy the scanned barcode value to the clipboard to paste it in the browser.
- Copy the text of an incoming SMS to the clipboard to paste it in a mail.

#### Settings

##### Text

The text to copy to the clipboard. [Variables are supported.](#string-inline-expressions)

---

### [Create Calendar Event](actions/action_create_calendar_event.md)

The action **Create Calendar Event** creates an event on the specified calendar of the device (Android 4+ required)

Examples:

- Create a calendar event based on the text of a received SMS.
- Create a calendar event for every received call.

#### Settings

##### Calendar

The name of calendar to create the event in. [Variables are supported.](#string-inline-expressions)

##### Start/End Type

Whether the event should be created relative to the time when the action is executed or absolute.

##### Start in

The start offset of the event from now. *1h* creates an event that starts in one hour. [Variables are supported.](#string-inline-expressions)

##### Duration

The desired duration of the event like *1h* or *45m*. [Variables are supported.](#string-inline-expressions)

##### From

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the start time of the event.

##### To

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the end time of the event.

##### All day

When checked creates an event lasting the whole day, the event spans all days intersecting the time span specified in *Start in/Duration* or *From/To*.

##### Title

The title. [Variables are supported.](#string-inline-expressions)

##### Description

The description. [Variables are supported.](#string-inline-expressions)

##### Location

The event location. [Variables are supported.](#string-inline-expressions)

##### Reminders

The reminders to create. [Variables are supported.](#string-inline-expressions)

##### Event Availability

The availability (not all calendars support Tentative).

##### Visibility

The visibility.

---

### [Create Directories](actions/action_create_directories.md)

The action **Create Directories** locally creates one or multiple directories.

Examples:

- Create a target directory `/mnt/sdcard/backup/` before copying files into this directory.

#### Settings

##### Directories

A comma separated list of directories to create. [Variables are supported.](#string-inline-expressions)

---

### [Delete App Cache](actions/action_delete_app_cache.md)

The action **Delete App Cache** deletes the cache files of the specified app. Android ignores this function for system apps.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Delete the browser cache every evening for security purposes.

#### Settings

##### Package Name

The package name of the app. [Variables are supported.](#string-inline-expressions)

---

### [Delete Files](actions/action_delete_files.md)

The action **Delete Files** locally deletes one or multiple files or folders including contained files.

Examples:

- Monthly delete all files in the `/mnt/sdcard/download/` folder.

#### Settings

##### Source Files

A comma separated list of files or directories to delete. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/download/*` matches all files and subfolders in the `download` directory

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Delete Flows](actions/action_delete_flows.md)

The action **Delete Flows** deletes the specified flows.

Examples:

- Delete a flow before the flow is imported again with action **Import Flows/Widgets**.

#### Settings

##### Flow Name List

The comma separated list of flows to delete. Glob patterns are *not* supported. [Variables are supported.](#string-inline-expressions)

##### Delete unused objects

Whether triggers, conditions and actions, that are not used by other flows, should also be deleted or not.

---

### [Delete HTTP Request Cookies](actions/action_delete_http_request_cookies.md)

The action **Delete HTTP Request Cookies** deletes the cookies of the desired domains that are stored by Automagic when executing action *HTTP Request*.

Examples:

- Delete all cookies to ensure that no cookies are sent in the next request.

#### Settings

##### Domain List

The comma separated list domains to delete cookies for. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

---

### [Dismiss Slide to Unlock Keyguard](actions/action_dismiss_slide_to_unlock_keyguard.md)

The action **Dismiss Slide to Unlock Keyguard** unlocks the device when the slid-to-unlock keyguard is used. This action can not unlock a secure keyguard that requires to enter a password, PIN or pattern.

Warning: This function is not officially supported by Android and might not work on all devices.
Some devices require that the screen is off to dismiss the keyguard.
Some devices turn off the screen when the keyguard is dismissed. You can mitigate the problem by adding an action *Turn Screen On* to the flow after dismissing the keyguard.

---

### [Download URL](actions/action_download_url.md)

The action **Download URL** directly downloads a file in the background to the defined directory.

Examples:

- Download a PDF newspaper every morning.

#### Settings

##### URL

The URL to download. [Variables are supported.](#string-inline-expressions)
Examples:

- `http://example.com/newspaper_{triggertime,dateformat,yyyyMMdd}.pdf` becomes `http://example.com/newspaper_20110213.pdf`

##### Directory

The directory to place the downloaded file in. [Variables are supported.](#string-inline-expressions)

##### Filename

The filename to use for the downloaded file. The URL is used to determine the filename if none is provided. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `file_path` — the target path of the downloaded file

---

### [Dropbox Create Directories](actions/action_dropbox_create_directories.md)

The action **Dropbox Create Directories** creates one or multiple directories on Dropbox.

Examples:

- create a directory before files are uploaded.

#### Settings

##### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

##### Path on Dropbox

A comma separated list of directories to create. [Variables are supported.](#string-inline-expressions)

---

### [Dropbox Delete Files](actions/action_dropbox_delete_files.md)

The action **Dropbox Delete Files** deletes the defined files on Dropbox.

Examples:

- Delete all files in a folder before uploading new files to this folder to get rid of files you don't need anymore.

#### Settings

##### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

##### Dropbox Paths

A comma separated list of files or directories to delete on Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Dropbox Download Files](actions/action_dropbox_download_files.md)

The action **Dropbox Download Files** downloads multiple files and directories recursively to your device.

Warning: This action downloads all specified files and overwrites already existing target files. The files will be downloaded even when the same file already exists on the device.

Warning: Dropbox limits the amount of data each user can transfer.

Examples:

- Download each morning the newest file of keypass containing your passwords to ensure you have the newest offline copy available.

#### Settings

##### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

##### Dropbox Paths

A comma separated list of files or directories to download from Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

##### Target

The absolute path of the target directory to download the files to. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Dropbox Init Variable File List](actions/action_dropbox_init_variable_file_list.md)

The action **Dropbox Init Variable File List** lists the files of a directory that match the specified name pattern.

Examples:

- Get a list of files and download only the ones smaller than 1MB.

#### Settings

##### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

##### Variable

The name of the variable to hold the list of files. [Variables are supported.](#string-inline-expressions)

##### File Pattern

The files to list. The file pattern can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

##### Include file attributes

When selected, returns for each file a list of attributes with path, file type, file size and file date.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `files` — the list of files

---

### [Dropbox Upload File](actions/action_dropbox_upload_file.md)

The action **Dropbox Upload File** uploads one file to your Dropbox.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the your Dropbox.

#### Settings

##### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

##### Local File

The absolute path of the local file to upload. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`

##### Path on Dropbox (including filename)

The absolute path of the file on Dropbox. The path has to include the filename of the target file. This allows you to store the file using a different name on your Dropbox. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Dropbox Upload Files](actions/action_dropbox_upload_files.md)

The action **Dropbox Upload Files** uploads one or multiple files and directories recursively to your Dropbox.

Warning: This action uploads all specified files and overwrites already existing target files. The files will be uploaded even when the same file already exists on Dropbox.

Warning: Dropbox limits the amount of data each user can transfer.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the your Dropbox.

#### Settings

##### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

##### Source Files

A comma separated list of files or directories to upload to Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

##### Path on Dropbox

The absolute path of the target on Dropbox to upload the files to. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Enable WiFi Access Point](actions/action_enable_wifi_access_point.md)

The action **Enable WiFi Access Point** enables one of the access point configurations and optionally prevents to connect to other access points by disabling them.

Examples:

- Enable a free access point at home and disable a paid access point.

#### Settings

##### SSID

The SSID of the access point configuration to enable. Glob patterns (\*, ?) are supported when **Disable other access points** is not enabled. [Variables are supported.](#string-inline-expressions)

##### Disable other access points

Whether to disable all other access point configurations or not.

---

### [End Call](actions/action_end_call.md)

The action **End Call** hangs up the current call.

Warning: This function is not officially supported by Android and might not work on all devices.

Warning: This function requires root access on some devices.

Example:

- Let the phone call home for 15 seconds and automatically terminate the call to notify something.

---

### [Execute Command](actions/action_execute_command.md)

The action **Execute Command** executes a shell command and stores the output in variables.

Examples:

- `ls -l` to list all files in the working directory
- `ps` to store the running processes in the defined variable
- `ps > file.txt` to store the running processes in a file
- `cat file1.txt > file2.txt` to copy a file
- `cat /proc/wakelocks` to show the wake locks preventing your device from sleeping

String variables are replaced before the command is passed to the interpreter.
You can use this for example to create a filename based on the current date: `ps > file-{triggertime,datetime,yyyyMMdd}.txt`.

Special characters in the command have to be escaped using backslash or placed in quotes as appropriate:
`cat 'Test File1.txt' > 'Test File2.txt'`
`cat Test\ File1.txt > Test\ File2.txt`

#### Settings

##### Command

Enter the shell command to execute in this field. The command is passed to `/bin/sh` to be interpreted.
The available commands vary from device to device. [Variables are supported.](#string-inline-expressions)

##### Working Directory

The path the command is executed in. [Variables are supported.](#string-inline-expressions)

##### Timeout

The timeout for the command.

##### Variable to store the standard output

The output written by the command to the standard output is stored in the variable defined in this field.

##### Variable to store the error output

The output written by the command to the error output is stored in the variable defined in this field.

##### Variable to store the exit code

The exit code of the command is stored in the variable defined in this field.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `stdout` — the standard output of the command
- `stderr` — the standard error output of the command
- `exit_code` — the exit code of the command

---

### [Execute Flows](actions/action_execute_flows.md)

The action **Execute Flows** executes one or multiple flows specified in the field **Flow pattern list**.

Tip: It's also possible to execute utility flows that don't have their own trigger. Simply don't add a trigger to such a flow but ensure that the flow is enabled.

The executed flow will inherit the execution context with all variables of the parent flow.
The variables usually supplied by the trigger of the target flow will not be available since the trigger of the target flow is bypassed when using this action.

Examples:

- Execute all flows with the words **battery save** in the name when the battery reaches a critical level.

#### Settings

##### Flow pattern list

A comma separated list of flow names to execute. Glob patterns `*` and `?` can be used to match similar named flows.

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*battery save*`

##### Exclude flow pattern list

A comma separated list of flow names to **not** execute even when the field **Flow pattern list** includes the flow.

##### Skip disabled flows without error

Whether disabled flows should be skipped without error or if the flow should be stopped with an error.

##### Wait for called flows to finish

Whether the action should wait until all called flows have been finished or not.

##### Return variables to the calling flow

Whether the local variables of the called flow should be returned to the calling flow.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `flow_count` — the number of flows to execute

---

### [Execute Root Command](actions/action_execute_root_command.md)

The action **Execute Root Command** executes a shell command as root by passing the command to `su` and stores the output in variables.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- `reboot` to reboot the device
- `reboot -p` to shutdown

String variables are replaced before the command is passed to the interpreter.
You can use this for example to create a filename based on the current date: `ps > file-{triggertime,datetime,yyyyMMdd}.txt`.

Special characters in the command have to be escaped using backslash or placed in quotes as appropriate:
`cat 'Test File1.txt' > 'Test File2.txt'`
`cat Test\ File1.txt > Test\ File2.txt`

#### Settings

##### Command

Enter the shell command to execute in this field. The command is passed to `su` to be interpreted.
The available commands vary from device to device. [Variables are supported.](#string-inline-expressions)

##### User

The user to use for executing the command. Defaults to root when not specified. [Variables are supported.](#string-inline-expressions)

##### SE Context

The SE context to use to execute the command. This setting is often required when using Android 5+ or any other device that set SELinux to enforcing. Requires *su* that allows to switch SE context (like SuperSU v1.97+). [Variables are supported.](#string-inline-expressions)

##### Working Directory

The path the command is executed in. [Variables are supported.](#string-inline-expressions)

##### Timeout

The timeout for the command.

##### Variable to store the standard output

The output written by the command to the standard output is stored in the variable defined in this field.

##### Variable to store the error output

The output written by the command to the error output is stored in the variable defined in this field.

##### Variable to store the exit code

The exit code of the command is stored in the variable defined in this field.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `stdout` — the standard output of the command
- `stderr` — the standard error output of the command
- `exit_code` — the exit code of the command

---

### [Execute SSH Command (Experimental)](actions/action_execute_ssh_command.md)

The action **Execute SSH Command** connects to an SSH server and executes a command.

Note: It can not be guaranteed that this action is compatible with all SSH servers.

Examples:

- Execute a command on a NAS every evening.
- Show the free memory of the server on a widget.

#### Settings

##### Server/Port

The IP or name of the SSH server to connect to. [Variables are supported.](#string-inline-expressions)

##### Validate host key

Whether the host key should be checked or not. Skipping the host key check reduces the security of SSH.

##### Username

The username. [Variables are supported.](#string-inline-expressions)

##### Authentication type

Whether to use password authentication or public key authentication. Keyboard interactive authentication is not supported.

##### Password

The password.

##### Private key file

The path to the private key file (OpenSSH format). You may need to convert the key to another format when the key does not work in Automagic. [Variables are supported.](#string-inline-expressions)

##### Public key file

The path to the public key file (OpenSSH format). You may need to convert the key to another format when the key does not work in Automagic. [Variables are supported.](#string-inline-expressions)

##### Passphrase

The passphrase of the key or empty when no passphrase is used.

##### Test connection/Update host key

Tries to establish a connection to the specified server using the given credentials. Variables are not replaced.

##### Command

The command to execute. [Variables are supported.](#string-inline-expressions)

##### Feed input file

Whether to feed an input file to the executed command (like *cat file | ssh user@server command*)

##### Input file

The file to feed to the command. [Variables are supported.](#string-inline-expressions)

##### Timeout

The overall timeout (connect and execute).

##### Store stdout in a variable or file

Whether to store the output of the command in a variable (max. 1MB, text). Binary output should always be stored in a file.

##### Variable to store the standard output

The output written by the command to the standard output is stored in the variable defined in this field.

##### File to store the standard output

The path to the file to store the output of the command. [Variables are supported.](#string-inline-expressions)

##### Variable to store the error output

The output written by the command to the error output is stored in the variable defined in this field.

##### Variable to store the exit code

The exit code of the command is stored in the variable defined in this field.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `stdout` — the standard output of the command
- `stderr` — the standard error output of the command
- `exit_code` — the exit code of the command

---

### [Exit Device Idle/Doze Mode](actions/action_exit_device_idle_mode.md)

The action **Exit Device Idle/Doze Mode** exits the device idle/doze mode.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Exit the device idle/doze mode every morning at 6am to make the device work reliably again.

---

### [Export Flows](actions/action_export_flows.md)

The action **Export Flows** exports the selected flows to the specified file.

Examples:

- Export all flows to a file and upload the file to Dropbox as a backup.

#### Settings

##### Flow pattern list

A comma separated list of flow names to export. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](#string-inline-expressions)

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*time tracking*`

##### Exclude flow pattern list

A comma separated list of flow names to **not** export even when the field **Flow pattern list** includes the flow. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](#string-inline-expressions)

##### Widget pattern list

A comma separated list of widget names to export. Glob patterns `*` and `?` can be used to match similar named widgets. [Variables are supported.](#string-inline-expressions)

##### Exclude widget pattern list

A comma separated list of widget names to **not** export even when the field **Widget pattern list** includes the widget. Glob patterns `*` and `?` can be used to match similar named widgets. [Variables are supported.](#string-inline-expressions)

##### Target File

The path of the target file. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `export_path` — the path of the created file

---

### [Flashlight](actions/action_flashlight.md)

The action **Flashlight** enables or disables the flashlight of the device.

Examples:

- Turn on or off the flashlight using a toggle widget.

#### Settings

##### Flashlight

Whether to turn the flashlight on or off.

---

### [FTP Create Directories](actions/action_ftp_create_directories.md)

The action **FTP Create Directories** creates one or multiple directories on an FTP server.

Examples:

- create a directory before files are uploaded.

#### Settings

##### Protocol

Whether to use regular FTP (unencrypted), FTPS (Implicit FTP over SSL/TLS, default port 990) or FTPES (Explicit FTP over SSL/TLS).

##### Data Channel Protection (only for FTPS and FTPES)

Whether data transferred on the data channel should be encrypted (P) or not (C).

##### Server/Port

The name or IP and port (default 21) of the FTP server. [Variables are supported.](#string-inline-expressions)

##### Username

The username to connect. [Variables are supported.](#string-inline-expressions)

##### Password

The password to connect. [Variables are supported.](#string-inline-expressions)

##### Server Directories

A comma separated list of directories to create. [Variables are supported.](#string-inline-expressions)

##### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](#string-inline-expressions)

---

### [FTP Delete Files](actions/action_ftp_delete_files.md)

The action **FTP Delete Files** deletes the files specified on the FTP server.

Examples:

- Recursively delete all files in a directory on the server before uploading new files.

#### Settings

##### Protocol

Whether to use regular FTP (unencrypted), FTPS (Implicit FTP over SSL/TLS, default port 990) or FTPES (Explicit FTP over SSL/TLS).

##### Data Channel Protection (only for FTPS and FTPES)

Whether data transferred on the data channel should be encrypted (P) or not (C).

##### Server/Port

The name or IP and port (default 21) of the FTP server. [Variables are supported.](#string-inline-expressions)

##### Username

The username to connect. [Variables are supported.](#string-inline-expressions)

##### Password

The password to connect. [Variables are supported.](#string-inline-expressions)

##### Paths on Server

A comma separated list of files or directories to delete on the server. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/pub/export*` matches all files with a name starting with `export` in folder `/pub`

##### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [FTP Download Files](actions/action_ftp_download_files.md)

The action **FTP Download Files** downloads files and folders stored on an FTP server.

Examples:

- Recursively download a directory with music every morning.

#### Settings

##### Protocol

Whether to use regular FTP (unencrypted), FTPS (Implicit FTP over SSL/TLS, default port 990) or FTPES (Explicit FTP over SSL/TLS).

##### Data Channel Protection (only for FTPS and FTPES)

Whether data transferred on the data channel should be encrypted (P) or not (C).

##### Server/Port

The name or IP and port (default 21) of the FTP server. [Variables are supported.](#string-inline-expressions)

##### Username

The username to connect. [Variables are supported.](#string-inline-expressions)

##### Password

The password to connect. [Variables are supported.](#string-inline-expressions)

##### Paths on Server

A comma separated list of files or directories to download from the server. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/pub/export*` matches all files with a name starting with `export` in folder `/pub`

##### Local Directory

The absolute path of the target directory to download the files to. [Variables are supported.](#string-inline-expressions)

##### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [FTP Init Variable File List](actions/action_ftp_init_variable_file_list.md)

The action **FTP Init Variable File List** lists the files of a directory that match the specified name pattern.

Examples:

- Get a list of files and download only the ones smaller than 1MB.

#### Settings

##### Protocol

Whether to use regular FTP (unencrypted), FTPS (Implicit FTP over SSL/TLS, default port 990) or FTPES (Explicit FTP over SSL/TLS).

##### Data Channel Protection (only for FTPS and FTPES)

Whether data transferred on the data channel should be encrypted (P) or not (C).

##### Server/Port

The name or IP and port (default 21) of the FTP server. [Variables are supported.](#string-inline-expressions)

##### Username

The username to connect. [Variables are supported.](#string-inline-expressions)

##### Password

The password to connect. [Variables are supported.](#string-inline-expressions)

##### Variable

The name of the variable to hold the list of files. [Variables are supported.](#string-inline-expressions)

##### File Pattern

The files to list. The file pattern can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

##### Include file attributes

When selected, returns for each file a list of attributes with path, file type, file size and file date.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `files` — the list of files

---

### [FTP Upload File](actions/action_ftp_upload_file.md)

The action **FTP Upload File** uploads one file to an FTP server.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the your company server.

#### Settings

##### Protocol

Whether to use regular FTP (unencrypted), FTPS (Implicit FTP over SSL/TLS, default port 990) or FTPES (Explicit FTP over SSL/TLS).

##### Data Channel Protection (only for FTPS and FTPES)

Whether data transferred on the data channel should be encrypted (P) or not (C).

##### Server/Port

The name or IP and port (default 21) of the FTP server. [Variables are supported.](#string-inline-expressions)

##### Username

The username to connect. [Variables are supported.](#string-inline-expressions)

##### Password

The password to connect. [Variables are supported.](#string-inline-expressions)

##### Local File

The absolute path of the local file to upload. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`

##### Path on Server (including filename)

The absolute path of the file on the FTP server. The path has to include the filename of the target file. This allows you to store the file using a different name on your server. [Variables are supported.](#string-inline-expressions)

##### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [FTP Upload Files](actions/action_ftp_upload_files.md)

The action **FTP Upload Files** uploads files and folders to an FTP server.

Examples:

- Recursively upload a directory with photos every morning to an FTP server.

#### Settings

##### Protocol

Whether to use regular FTP (unencrypted), FTPS (Implicit FTP over SSL/TLS, default port 990) or FTPES (Explicit FTP over SSL/TLS).

##### Data Channel Protection (only for FTPS and FTPES)

Whether data transferred on the data channel should be encrypted (P) or not (C).

##### Server/Port

The name or IP and port (default 21) of the FTP server. [Variables are supported.](#string-inline-expressions)

##### Username

The username to connect. [Variables are supported.](#string-inline-expressions)

##### Password

The password to connect. [Variables are supported.](#string-inline-expressions)

##### Local Paths

A comma separated list of files or directories to upload to the server. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

##### Server Directory

The absolute path of the target directory on the server to upload the files to. [Variables are supported.](#string-inline-expressions)

##### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Gleeo Create Entry](actions/action_gleeo_create_entry.md)

The action **Gleeo Create Entry** creates an entry of the specified project and task in **Gleeo Time Tracker**.

Examples:

- Track the amount of time spent in the Twitter app and create an entry in Gleeo Time Tracker at the end of the day.

#### Settings

##### Domain

The name of the domain to create an entry for. [Variables are supported.](#string-inline-expressions)

##### Project

The name of the project to create an entry for. [Variables are supported.](#string-inline-expressions)

##### Task

The task of the entry to create. The task will be created in **Gleeo Time Tracker** when it not already exists.
The task name can be defined dynamically using variables.

Examples:

- `Phone Support for {incoming_number}` becomes `Phone Support for 17001111111`
- `Visiting {trigger}` becomes `Visiting Customer X` (use different location triggers named `Customer X`, `Customer Y` etc.)

##### Details

The details of the entry. [Variables are supported.](#string-inline-expressions)

##### Extra 1

Extra 1 of the entry. [Variables are supported.](#string-inline-expressions)

##### Extra 2

Extra 2 of the entry. [Variables are supported.](#string-inline-expressions)

##### Variable containing the start time

The name of the variable (without curly braces) containing the start time. [Variables are supported.](#string-inline-expressions)

##### Variable containing the end time

The name of the variable (without curly braces) containing the start time. [Variables are supported.](#string-inline-expressions)

##### Move to Background

Whether to move **Gleeo Time Tracker** to the background when the entry has been created.

---

### [Gleeo Filesystem Export](actions/action_gleeo_export_to_filesystem.md)

The action **Gleeo Filesystem Export** creates a CSV export of the defined projects and time range.

Examples:

- Backup all data in Gleeo Time Tracker to the SD card.
- Export the current month by pressing a shortcut on the launcher and attach the created file to a Google Mail message draft.
- Each month export all recorded entries of the month to the SD card and send the file by mail to your employer.

#### Settings

##### Domains to Export

The list of domains to export. [Variables are supported.](#string-inline-expressions)

##### Projects to Export

The list of projects to export. [Variables are supported.](#string-inline-expressions)

##### Tasks to Export

The list of tasks to export. [Variables are supported.](#string-inline-expressions)

##### Time Range

The time range to export.

##### CSV Column Delimiter

The delimiter used to separate two columns. Excel users can set this to `Semicolon` to simplify the import in Excel.

##### Target File

The file to store the exported data in. Variables can be used to create dynamic file names based on time.

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`
- `/mnt/sdcard/export_{export_start_time,dateformat,yyyy_MM_dd}-{export_end_time,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_03_01-2011_03_31.csv`

##### Encoding

The encoding used to save the file.

##### Attach to Mail

Opens the desired Mail App and attaches the CSV file.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `export_start_time` — the start time of the exported time range
- `export_end_time` — the end time of the exported time range
- `export_path` — the absolute path of the exported file

---

### [Gleeo Start Recording](actions/action_gleeo_start_recording.md)

The action **Gleeo Start Recording** starts recording the defined project and task in **Gleeo Time Tracker** when this task is not already recording.

Examples:

- Start tracking the time when you arrive at your office.
- Start tracking the time when your employer calls.
- Start tracking the time when you press a shortcut on the launcher.

#### Settings

##### Domain

The name of the domain to start recording. [Variables are supported.](#string-inline-expressions)

##### Project

The name of the project to start recording. [Variables are supported.](#string-inline-expressions)

##### Task

The task to start recording. The task will be created in **Gleeo Time Tracker** when it not already exists.
[Variables are supported.](#string-inline-expressions)

Examples:

- `Phone Support for {incoming_number}` becomes `Phone Support for 17001111111`
- `Visiting {trigger}` becomes `Visiting Customer X` (use different location triggers named `Customer X`, `Customer Y` etc.)

##### Details

The details of the entry. [Variables are supported.](#string-inline-expressions)

##### Extra 1

Extra 1 of the entry. [Variables are supported.](#string-inline-expressions)

##### Extra 2

Extra 2 of the entry. [Variables are supported.](#string-inline-expressions)

##### Move to Background

Whether to move **Gleeo Time Tracker** to the background when the task has been started.

---

### [Gleeo Stop Recording](actions/action_gleeo_stop_recording.md)

The action **Gleeo Stop Recording** stops recording the currently recording task in **Gleeo Time Tracker**.

Examples:

- Stop tracking the time when you leave your office.
- Stop tracking the time every evening at 6pm and show an alert when you forgot to stop recording.

#### Settings

##### Domains to Stop

The name of the domain to stop recording.
Glob patterns are supported. [Variables are supported.](#string-inline-expressions)

##### Projects to Stop

The name of the project to stop recording.
Glob patterns are supported. [Variables are supported.](#string-inline-expressions)

##### Tasks to Stop

The tasks to stop recording.
Glob patterns are supported.[Variables are supported.](#string-inline-expressions)

##### Move to Background

Whether to move **Gleeo Time Tracker** to the background when the task has been stopped.

---

### [Google Drive Create Directories (Experimental)](actions/action_google_drive_create_directories.md)

The action **Google Drive Create Directories (Experimental)** creates one or multiple directories on Google Drive.

Examples:

- create a directory before files are uploaded.

#### Settings

##### Device account

The account to access Google Drive.

##### Google Drive Directories

A comma separated list of directories to create. [Variables are supported.](#string-inline-expressions)

---

### [Google Drive Delete Files (Experimental)](actions/action_google_drive_delete_files.md)

The action **Google Drive Delete Files (Experimental)** deletes the defined files on Dropbox.

Examples:

- Delete all files in a folder before uploading new files to this folder to get rid of files you don't need anymore.

#### Settings

##### Device account

The account to access Google Drive.

##### Google Drive Paths

A comma separated list of files or directories to delete on Google Drive. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Google Drive Download Files (Experimental)](actions/action_google_drive_download_files.md)

The action **Google Drive Download Files (Experimental)** downloads multiple files and directories recursively to your device.

Warning: This action downloads all specified files and overwrites already existing target files. The files will be downloaded even when the same file already exists on the device.

Note: Google Drive allows to create duplicate files which is not possible on a regular filesystem. Automagic only considers the newest file in such a case and ignores duplicates.
Note: Google Documents are not downloaded.

Examples:

- Download each morning the newest file of keypass containing your passwords to ensure you have the newest offline copy available.

#### Settings

##### Device account

The account to access Google Drive.

##### Google Drive Paths

A comma separated list of files or directories to download from Google Drive. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

##### Target

The absolute path of the target directory to download the files to. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Google Drive Init Variable File List](actions/action_google_drive_init_variable_file_list.md)

The action **Google Drive Init Variable File List** lists the files of a directory that match the specified name pattern.

Examples:

- Get a list of files and download only the ones smaller than 1MB.

#### Settings

##### Device account

The account to access Google Drive.

##### Variable

The name of the variable to hold the list of files. [Variables are supported.](#string-inline-expressions)

##### File Pattern

The files to list. The file pattern can contain glob pattern characters like `*` and `?`. [Variables are supported.](#string-inline-expressions)

##### Include file attributes

When selected, returns for each file a list of attributes with path, file type, file size and file date.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `files` — the list of files

---

### [Google Drive Upload Files (Experimental)](actions/action_google_drive_upload_files.md)

The action **Google Drive Upload Files (Experimental)** uploads one or multiple files and directories recursively to your Google Drive.

Warning: This action uploads all specified files and overwrites already existing target files.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the Google Drive.

#### Settings

##### Device account

The account to access Google Drive.

##### Source Files

A comma separated list of files or directories to upload to Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

##### Path on Google Drive

The absolute path of the target on Google Drive to upload the files to. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Hide Custom Widget Overlay](actions/action_hide_custom_widget_overlay.md)

The action **Hide Custom Widget Overlay** hides a previously shown overlay.

#### Settings

##### Overlay names

The names/identifications of the overlays to hide.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `widget_x_offset` — X-offset of the hidden widget.
- `widget_y_offset` — Y-offset of the hidden widget.

---

### [Hide Custom Widget Overlay (Android Wear)](actions/action_hide_custom_widget_overlay_wear.md)

The action **Hide Custom Widget Overlay (Android Wear)** hides a previously shown overlay.

#### Settings

##### Android Wear device

The device to hide the widget on. [Variables are supported.](#string-inline-expressions)

##### Overlay name

The name/identification of the overlay to hide.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `widget_x_offset` — X-offset of the hidden widget.
- `widget_y_offset` — Y-offset of the hidden widget.

---

### [HTTP Request](actions/action_http_request.md)

The action **HTTP Request** requests a resource from a server using the specified HTTP request method.

Note: This action is meant to be used for technical requests (REST and the like) and to process the response using scripts. If you simply want to download a file please use the action *Download URL*.
The action terminates with a status code of -1 for general errors. It will terminate with an error when not even a connection to the server can be established (network not available, IP can not be resolved etc.). Use an Exception-connection to handle such errors.

Examples:

- Fetch a web page of a weather service and test if it contains the word *rain*.
- Get the price of a product from an online retailers REST service.

#### Settings

##### URL

The URL to request. [Variables are supported.](#string-inline-expressions)
Examples:

- `http://example.com/weather.html?ts={triggertime,dateformat,yyyyMMdd}` becomes `http://example.com/weather.html?ts=20110213`

##### Verify certificates (https)

Whether certificates should be checked or not. Can be useful to ignore errors for self-signed certificates.

##### Authentication

Whether username and password should be passed to the server using basic authentication.

##### Username

The username to pass to the server. [Variables are supported.](#string-inline-expressions)

##### Password

The password to pass to the server. [Variables are supported.](#string-inline-expressions)

##### Client certificate

If a client certificate should be used.

##### Client certificate path

Path to the PKCS#12 file. [Variables are supported.](#string-inline-expressions)

##### Client certificate password

The password to access the client certificate. [Variables are supported.](#string-inline-expressions)

##### Network Type

Whether to use the currently available default network or send the request on the WiFi or cellular network.

##### Request Method

The HTTP request method to use. Not all methods are supported by all devices.

##### Content Type

The content type to use in the request as header Content-Type. [Variables are supported.](#string-inline-expressions)

##### Form Field List

Comma separated list with key=value to send as `application/x-www-form-urlencoded` to the server. The values are automatically URL encoded. [Variables are supported.](#string-inline-expressions)

Example: `Firstname=Hugo,Lastname=Habicht`

##### Data

The text data to send to the server. [Variables are supported.](#string-inline-expressions)

##### Form Field Name

The name of the form field to use for the uploaded file. [Variables are supported.](#string-inline-expressions)

##### File to upload

The path of the file to upload. The filename for the request is automatically determined based on the specified file. [Variables are supported.](#string-inline-expressions)

##### Timeout

The timeout to use.

##### Custom HTTP Headers

A text containing the custom HTTP headers to send. [Variables are supported.](#string-inline-expressions)

Each line should start with the header name and a colon followed by the value to send.

Examples:

- `User-Agent: my own user agent`
- `SOAPAction: "test"`

##### Store response in a variable or file

Whether to store the response in a variable or a file.

##### Variable

The name of the variable to store the response in. The response is converted to a string. [Variables are supported.](#string-inline-expressions)

Warning: Responses larger than 1MB are not supported in a variable.

##### Encoding

The encoding to use to read the response from the server. Leave empty to use the encoding as specified by the servers response.

##### File

The path to store the file in. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- name as declared in the field Variable — the response as string
- `status_code` — the numeric HTTP status code, -1 when a general error occurs
- `error_message` — error message when the request could not be executed and `status_code` is set to -1
- `header_*` —
  All values of the response headers. The name of the variable is built using the prefix `header_` and the name of the header by replacing dash with underscore and converting the name to lowercase.
  Examples:
  - Header `Accept` is stored in variable `header_accept`
  - Header `Accept-Encoding` is stored in variable `header_accept_encoding`Values of headers that are specified multiple times in the response are provided as a list.
  Headers leading to an invalid variable name are ignored.

---

### [Import Flows](actions/action_import_flows.md)

The action **Import Flows** imports all flows of the specified file. The imported flows are **disabled**. Already existing flows are not imported.
Flows can be enabled after importing when desired using action **Set Flow State** and the variable `{imported_flow_names,listformat,comma}`.

Examples:

- Import a flow to lock the device on the stolen device.

#### Settings

##### File

The file to import. [Variables are supported.](#string-inline-expressions)

##### Replace existing

Whether or not to replace existing Flows, Triggers, Actions, Conditions and Widgets with the same name.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `imported_flow_names` — the list of imported flows
- `duplicate_flow_names` — the list of duplicate flows that have not been imported

---

### [Init Variable Contact List](actions/action_init_variable_contact_list.md)

The action **Init Variable Contact List** stores the list of contacts in the specified variable.

Examples:

- Show the starred contacts in a selection list before calling the selected contact.

#### Settings

##### Type

Whether to show all contacts of the address book or only the contacts of the selected groups.

##### Group names

The names of the groups to load. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `contact_list` — the list of contacts

---

### [Init Variable File List](actions/action_init_variable_file_list.md)

The action **Init Variable File List** lists all files or only the newly added files in a directory and stores the list in a variable.

Examples:

- Send all files of a directory by mail to your mail account.
- Send all new backup files of **Gleeo Time Tracker** to your inbox.

#### Settings

##### Variable

The name of the variable to hold the list of files.

##### File Pattern

The files to list. The file pattern can contain glob pattern characters like `*` and `?`.

Examples:

- `/mnt/sdcard/folder/*`
- `/mnt/sdcard/GTT-export-20120101.csv`
- `/mnt/sdcard/GTT-export-*.csv`
- `/mnt/sdcard/file1,/mnt/sdcard/file2,/mnt/sdcard/file3`

##### Include changes only

Whether to store all files matching the pattern specified in **File Pattern** or only the new files.
A file is considered to be new when it was not available the last time this action executed or the size of the file changed or the last modified time of the file has changed since the last execution of this action.

##### Include file attributes

When selected, returns for each file a list of attributes with path, file type, file size and file date.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `files` — the list of files

---

### [Init Variable Image File](actions/action_init_variable_image_file.md)

The action **Init Variable Image File** loads the pixel data of an image into the specified local variable to modify the image with action **Modify Image** or to read color values of pixels with script function **getPixelColor**.

Warning: Loading large images uses a lot of internal memory which could cause Automagic to crash in the worst case. It's recommended to read only one image into memory and not to load very large images.

Examples:

- Load an image, shrink the size and send the smaller file by mail.

#### Settings

##### File

The path or URL to the image file. [Variables are supported.](#string-inline-expressions)

##### Variable

The name of the local variable to store the pixel data. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `image_data` — the local variable of the image
- `image_width` — the width of the image
- `image_height` — the height of the image

---

### [Init Variable Image Metadata](actions/action_init_variable_image_metadata.md)

The action **Init Variable Image Metadata** extracts the metadata (e.g. Exif tags) from an image and stores the values in a map (key=label/name of the tag, value=description or raw value of the tag).

Example to read the GPS location in an action **Script**:
`location = getMapValue(image_metadata, "gps_location");`

Tip: Condition **Debug Dialog** can be used to display the keys and values stored in the map.

Examples:

- Extract the GPS location and the thumbnail from a JPEG image.

#### Settings

##### File

The path to the image file. [Variables are supported.](#string-inline-expressions)

##### Variable

The name of the variable to store the map with the values in. [Variables are supported.](#string-inline-expressions)

##### Parse dates

Defines if date strings should be converted to proper date/time values or if the string should be stored as a string in the map.

##### Include metadata directory name

Whether to include the name of the metadata directory in the key of each read tag.

##### Get raw values

Defines if the metadata values should be converted to a human readable form or if the values should be loaded as is.

##### Extract thumbnail

Defines if an available thumbnail should be extracted from the metadata and stored in variable `thumbnail_image`.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `image_metadata` — the map containing the extracted tag names/labels and the extracted values for each tag
- `thumbnail_image` — the thumbnail image extracted from the image metadata

---

### [Init Variable Location](actions/action_init_variable_location.md)

The action **Init Variable Location** acquires one location from the defined provider and stores the location in the variable.

Note: Getting one location can take several seconds to complete. The passive provider might not return a location until another app is activating one of the location providers.

Examples:

- Send the location in response to an SMS containing the text **Where are you?** to the sender.
- Store the location coordinates in a file when the employer calls.
- Send the location and phone number by mail whenever you call someone.

#### Settings

##### Variable

The name of the variable to store the location in.

##### New or Last Known Location

Defines if the action should acquire a new location or if the action should use the last known location. Loading the last known location uses almost is very fast but might return an outdated location or no location might be available when the device was freshly started.

##### Location Provider

The location provider to use.
**Network**
This provider uses the location provided by the cell tower and Wi-Fi signals. Depending on environment this provider can deliver location of about 60 meters of accuracy. Locations found using the cell tower can be very inaccurate (up to several kilometers or miles).

**Passive**
This provider delivers the location from the currently active provider (Network or GPS) without activating one of the providers by itself. This might result in very infrequent location updates.

**GPS**
This provider delivers the location using the GPS receiver. This provider usually uses more battery than the network provider.

**High Accuracy (Experimental)**
This provider delivers the finest available location using different sensors available on the device.

**Balanced Power/Accuracy (Experimental)**
This provider delivers the a location with an accuracy of about 100m and uses less battery than the high accuracy provider.

**Low Power (Experimental)**
This provider delivers the a location with an accuracy of about 10km.

**No Power (Experimental)**
This provider will only deliver locations when another app on the device has requested locations.

##### Minimum Accuracy (in meters)

Only newer locations with at least this accuracy are accepted.
This can be useful to filter out locations calculated using the cell tower when also more exact locations using WiFi are available.

##### Timeout

The maximum amount of time to wait for a location fix, otherwise terminate the flow with an error.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `location` — the reported location
- `location_accuracy` — the accuracy of the location
- `location_altitude` — the altitude of the location when available (not available on all devices)
- `location_bearing` — the direction of travel in degrees East of true North when available (not available on all devices)
- `location_speed` — the speed of travel in meters per second when available (not available on all devices)

---

### [Init Variable Next Alarm](actions/action_init_variable_next_alarm.md)

The action **Init Variable Next Alarm** fills the time of the next currently known alarm into the specified variable.

Warning: This function is not officially supported by Android < 5.0 and might not work on all devices.

Examples:

- Get the time of the next alarm to show a reminder one hour before the alarm is reached.

#### Settings

##### Variable

The name of the variable.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `next_alarm` — the time of the next alarm or null when no alarm is set

---

### [Init Variable Notifications on Statusbar](actions/action_init_variable_notifications_status_bar.md)

The action **Init Variable Notifications on Statusbar** stores all currently shown notifications as a list in a variable.

Examples:

- Send the texts of all shown notifications by mail to your account when you receive an SMS with the text *get notifications*.

#### Settings

##### Variable

The name of the variable to store the list of notifications.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `notifications` —
  the list of all notifications with a map containing following keys for each notification:

  `title`

  the title of the displayed notification

  `content_title`

  the title of the content displayed by the notification

  `content_title_big`

  the title of the big content displayed by the notification

  `notification_text` (This function is not officially supported by Android and does not work with all notifications)

  the textual content of the notification

  `notification_text_big` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the textual content of the big, expanded view of the notification

  `notification_channel_id` (Android 8.0+)

  the ID of the notification channel

  `notification_priority` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the priority of the notification (-2=Minimum to 2=Maximum), when available

  `notification_large_icon` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the large icon of the notification, when available

  `notification_when`

  the time shown in the notification

  `notification_number`

  number shown in the notification, when available

  `notification_vibrate_default`

  whether the notification vibrates using the default pattern

  `notification_vibrate_pattern`

  vibration pattern as a list of numbers (pause duration in ms, vibrate duration in ms, ...), when available

  `notification_sound_default`

  whether the notification should play the default notification sound

  `notification_sound_uri`

  the URI of the sound to play, when available

  `notification_people` (Android 4.4+)

  a list of relevant people of the notification (list of URIs), when available

  `notification_info_text` (Android 4.4+)

  the info text displayed by the notification, when available

  `notification_sub_text` (Android 4.4+)

  the sub text displayed by the notification, when available

  `notification_summary_text` (Android 4.4+)

  the summary text displayed by the notification, when available

  `notification_progress` (Android 4.4+)

  the current progress shown by the notification, when available

  `notification_progress_max` (Android 4.4+)

  the maximum progress, when available

  `notification_progress_indeterminate` (Android 4.4+)

  whether the progress is indeterminate, when available

  `notification_text_lines` (Android 4.4+)

  the text lines shown by the notification, when available

  `notification_background_image_uri` (Android 5+)

  the URI of the background image to show, when available

  `notification_category` (Android 5+)

  the category of the notification, when available

  `notification_accent_color` (Android 5+)

  the accent color of the notification, when available

  `notification_ticker_text`

  the scrolling text shown by the notification

  `notification_visibility` (Android 5+)

  the visibility of the notification (-1=secret, 0=private, 1=public)

  `notification_ongoing`

  whether this is an ongoing event

  `notification_foreground_service`

  whether this notification is used to mark a foreground service

  `notification_local_only`

  whether the notification should be displayed on the local device only

  `notification_group` (Android 7+)

  the group key of the notification

  `notification_is_group_summary` (Android 7+)

  whether the notification is the group summary

  `package_name`

  the name of the package that displayed the notification

  `app_name`

  the display name of the app

  `id` (Android 4.3+)

  the id of the notification

  `buttons` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the list of buttons available on the big, expanded notification

---

### [Init Variable Package Info](actions/action_init_variable_package_info.md)

The action **Init Variable Package Info** loads information of the specified apps/packages and stores the information in a map.

Tip: Condition **Debug Dialog** can be used to display the keys and values stored in the map.

Examples:

- Load the list of permissions used by an app and check which permissions have been granted.

### Format

The map contains the package name as the key and a map with the queried information as value. Example shown as JSON:
```
        {
          "package1": {"version_name": xyz, "version_code": 123},
          "package2": {"version_name": xyz, "version_code": 123}
        }
```

Example JSON queried for one app:
```
        {
          "com.android.vending": {
            "version_name": "6.4.12.C-all [0] 2744941", // the version name
            "version_code": 80641200, // the version number
            "first_install_time": 1230796800000, // the time at which the app was first installed (millis since 1970)
            "last_update_time": 1461091018180, // the time at which the app was last updated (millis since 1970)
            "install_location": -1, // -1=auto?, 0=auto, 1=internal only, 2=prefer external
            "application_info": {
              "data_dir": "/data/user/0/com.android.vending", // full path to a directory assigned to the package for its persistent data
              "class_name": "com.google.android.finsky.FinskyApp", // class implementing the Application object
              "source_dir": "/data/app/com.android.vending-2/base.apk", // full path to the base APK for this application
              "label": "Google Play Store", // the label of the app (current locale)
              "uid": 10024, // the kernel user-ID that has been assigned to this application
              "icon_uri": "android.resource://com.android.vending/2130903045", // URI to load the icon of the app
              "target_sdk_version": 23, // the API level that the application targets
              "enabled": true // whether or not the Android system can instantiate components of the application
            },
            "requested_permissions": [
              {
                "permission": "android.permission.WRITE_EXTERNAL_STORAGE", // the name of the permission
                "requested_permission_flag": 3, // 1=requested, 3=requested & granted
                "label": "modify or delete the contents of your USB storage", // the label of the permission
                "description": "Allows the app to write to the USB storage.", // the description of the permission
                "protection_level": 1, // protection level as number
                "protection_level_text": "dangerous", // protection level expressed as text
                "group": "android.permission-group.STORAGE", // the group name of the permission
                "group_label": "Storage", // the permission group label
                "group_description": "access photos, media, and files on your device" // the permission group description
              }, ...
            ],
            "activity_info": [
              {
                "name": "com.android.vending.AssetBrowserActivity",
                "label": "Play Store",
                "icon_uri": "android.resource://com.android.vending/2130903045",
                "enabled": true, // whether the activity is enabled
                "exported": true // whether the activity can be used by other apps
                "permission": "com.google.android..." // permission required to access this activity (when defined)
              },
            ],
            "receiver_info": [
              {
                "name": "com.google.android.gcm.GCMBroadcastReceiver",
                "label": "Google Play Store",
                "enabled": true,
                "exported": true,
                "permission": "com.google.android.c2dm.permission.SEND"
              }, ...
            ],
            "provider_info": [
              {
                "name": "com.google.android.finsky.providers.RecentSuggestionsProvider",
                "label": "Google Play Store",
                "authority": "com.google.android.finsky.RecentSuggestionsProvider",
                "enabled": true,
                "exported": false
              }, ...
            ],
            "service_info": [
              {
                "name": "com.google.android.finsky.services.ReviewsService",
                "label": "Google Play Store",
                "enabled": true,
                "exported": true
              }, ...
            ]
          }, ...
        }
```

Please note that additional key value pairs might be added in future versions of Automagic.

#### Settings

##### Type

Whether to query information about all installed packages or only a few selected packages.

##### Package Names

The list of packages to query. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### Include permission infos

If information about permissions requested by the app should be queried.

##### Include activity infos

If information about activities defined by the app should be queried.

##### Include receiver infos

If information about receivers defined by the app should be queried.

##### Include provider infos

If information about content providers defined by the app should be queried.

##### Include service infos

If information about services defined by the app should be queried.

##### Variable

The name of the variable to store the result in.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `package_info` — the map containing the queried information

---

### [Init Variable Random Number](actions/action_init_variable_random_number.md)

The action **Init Variable Random Number** generates a random number in a defined interval.

Examples:

- Simulate to throw a dice.
- Play a random sound for every received SMS.

#### Settings

##### Variable

The variable to store the random number in.

##### Lowest Value

The lowest generated value.

##### Highest Value

The highest generated value.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `n` — contains the generated random value

---

### [Init Variable System Setting](actions/action_init_variable_system_setting.md)

The action **Init Variable System Setting** reads a value from the system setting database and stores the value in a variable.

#### Settings

##### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global Settings valid for all users of the device (Android 4.2+)

##### Name

The name of the setting to read. [Variables are supported.](#string-inline-expressions)

##### Variable

The name of the variable to store the value in. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `setting` — the value of the setting

---

### [Init Variable System Setting (Android Wear)](actions/action_init_variable_system_setting_wear.md)

The action **Init Variable System Setting (Android Wear)** reads a value from the system setting database and stores the value in a variable.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global Settings valid for all users of the device (Android 4.2+)

##### Name

The name of the setting to read. [Variables are supported.](#string-inline-expressions)

##### Variable

The name of the variable to store the value in. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `setting` — the value of the setting

---

### [Init Variable Text File](actions/action_init_variable_text_file.md)

The action **Init Variable Text File** reads the contents of a text file into the specified variable. Files up to 1MB are supported. Binary files are not supported.

Examples:

- Read a text file containing a mail template and send the text by mail.

#### Settings

##### File

The path of the file to load. [Variables are supported.](#string-inline-expressions)

##### Encoding

The encoding used to decode the bytes of the file to text.

##### Variable

The name of the variable to store the text in. [Variables are supported.](#string-inline-expressions)

##### Strip BOM

Whether the BOM (byte order mark) potentially found at the beginning of UTF encoded file should be removed from the resulting string or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `file_text` — the name of the variable to store the text in

---

### [Init Variable WiFi Access Point List](actions/action_init_variable_wifi_access_point_list.md)

The action **Init Variable WiFi Access Point List** lists all configured or only enabled/disabled wifi networks into a variable.

Examples:

- Show a list of WiFI networks and allow to connect to the selected one.

#### Settings

##### Access Point Criteria

Whether all configured networks should be listed or only the enabled or disabled networks.

##### Variable for SSID list

The name of the variable to hold the list.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `access_points` — the SSID-list of wifi networks

---

### [Init Variables Bluetooth Device List](actions/action_init_variables_bluetooth_device_list.md)

The action **Init Variables Bluetooth Device List** lists all paired, connected or not connected bluetooth devices in a variable.

Examples:

- Show a dialog of all not connected bluetooth devices and attempt to connect to a selected device.

#### Settings

##### Device Criteria

Whether to list all paired, connected or not connected devices.

##### Variable for device name list

The name of the variable to store the device names.

##### Variable for device address list

The name of the variable to store the device addresses.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `device_names` — the device names as a list
- `device_addresses` — the device addresses as a list

---

### [Init Variables Call Log](actions/action_init_variables_call_log_call.md)

The action **Init Variables Call Log** initializes variables with the values of the last entry of the call log.

Examples:

- Update a widget with the values of the last call.

#### Settings

##### Query Criteria

Specifies which call should be stored in the variables.

##### Variable for Call Number

The name of the variable to store the call number.

##### Variable for Call Date/Time

The name of the variable to store the point in time of the call.

##### Variable for Call Duration

The name of the variable to store the call duration.

##### Variable for Call Type

The name of the variable to store the call type (1=incoming, 2=outgoing, 3=missed).

##### Variable for Call Contact Name

The name of the variable to store the contact name.

##### Variable for Call New Flag

The name of the variable to store if the call log entry has not been marked acknowledged.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `call_number` — the call number
- `call_time` — the time of the call in millis since 1970
- `call_duration` — the call duration in seconds
- `call_type` — the call type (1=incoming, 2=outgoing, 3=missed)
- `call_cached_name` — the name of the contact (might be outdated when the contact has been modified in the contacts afterwards)
- `call_new` — true or false whether the entry in the call log has not been acknowledged yet

---

### [Init Variables Contact Info](actions/action_init_variables_contact_info.md)

The action **Init Variables Contact Info** loads information of the specified contact and stores the information in a map.

Tip: Condition **Debug Dialog** can be used to display the keys and values stored in the map.

Examples:

- Show all phone numbers of a contact.

Example JSON of a contact:
```
        {
          "display_name": "Contact XYZ", // name of the contact
          "photo_thumb_uri": "content://com.android.contacts/contacts/124/photo", // URI of the small image
          "photo_uri": "content://com.android.contacts/display_photo/3", // URI of the larger image
          "last_time_contacted": 1479667934531, // point in time of the last contact, 0 when not known
          "starred": true, // whether the contact is in the favorites or not
          "times_contacted": 1, // count of contacts (according to contact app)
          "phone_list": [{ // list of phone numbers
            "number": "+41987654321",
            "type": 2,
            "type_label": "Mobile"
          }, ... ],
          "organization_list": [{ // list of organizations
            "company": "Company X",
            "type": 2,
            "type_label": "Other",
            "title": "Company"
          }, ... ],
          "note_list": [{ // list of notes
              "note": "Note 1"
            }, ... ],
          "nickname_list": [{ // list of nicknames
            "nickname": "MR. incredible",
            "type": 0,
            "type_label": "Other"
          }, ... ],
          "email_list": [{ // list of email addresses
            "email": "example@gmail.com",
            "type": 1,
            "type_label": "Home"
          }, ... ],
          "relation_list": [{ // list of relations
            "relation": "Person 123",
            "type": 1,
            "type_label": "Assistant
          }, ... ],
          "structured_postal_list": [{ // list of addresses
            "formatted_address": "Mainstreet X\n1234 City",
            "type": 1,
            "type_label": "Home",
            "street": "Mainstreet X",
            "city": "City",
            "postcode": "1234"
          }, ... ],
          "structured_name_list": [{ // list of the names
            "display_name": "Contact XYZ",
            "given_name": "Contact",
            "family_name": "XYZ"
          }, ... ],
          "website_list": [{ // list of websites
            "url": "www.automagic4android.com",
            "type": 7,
            "type_label": "Other"
          }, ... ],
          "sip_address_list": [{ // list of the SIP addresses
            "number": "+41987654321",
            "type": 2,
            "type_label": "Mobile"
          }, ... ],
          "event_list": [{ // list of events
            "start_date": "1978-07-04",
            "type": 3,
            "type_label": "Birthday"
          }, ...],
          "group_list": [ // list of the groups
            "Group1",
            "Group2",
            "Group3"
          ]
        }
```

Please note that additional key value pairs might be added in future versions of Automagic.

Examples of access to values in action **Script**:
```
        name = contact_info["display_name"];
        photo_uri = contact_info["photo_uri"];
        phone1 = contact_info["phone_list"][0]["number"];
        phone2 = contact_info["phone_list"][1]["number"];
        phone2type = contact_info["phone_list"][1]["type_label"];
        nickname1 = contact_info["nickname_list"][0]["nickname"];
```

#### Settings

##### Search type

Defines how the contact should be searched. The first found contact is used to provide the information.

##### Search value

The value used to search the contact. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `contact_info` — the map containing the queried information

---

### [Init Variables Device Orientation](actions/action_init_variables_device_orientation.md)

The action **Init Variables Device Orientation** measures the device orientation using the accelerometer and magnetometer sensors of the device.

Warning: This action uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Show your current orientation value in a popup.
- Select the task to record by changing the device orientation.

#### Settings

##### Variable for Azimuth

The name of the variable to store the azimuth of the device (in degrees).

##### Variable for Pitch

The name of the variable to store the pitch of the device (in degrees).

##### Variable for Roll

The name of the variable to store the roll of the device (in degrees).

##### Timeout

The amount of time to wait for a value of the sensor, the action is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `azimuth` — the azimuth in degrees
- `pitch` — the pitch in degrees
- `roll` — the roll in degrees

---

### [Init Variables File Info](actions/action_init_variables_file_info.md)

The action **Init Variables File Info** provides information about a file as variables to the flow.

Examples:

- Check if a file is older than one week and delete the file.

#### Settings

##### File

The file to check. [Variables are supported.](#string-inline-expressions)

##### File Type

The variable to store the file type (`dir`, `file` or `other`).

##### File Exists

Variable to store whether the file exist or not.

##### File Size

Variable to store the size of the file in bytes.

##### recursive for directory

For directories whether to collect the size of all directly contained files or to also recursively traverse and sum the size of all subdirectories.

##### File Last Modified

Variable to store the last modification timestamp.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `file_type` — the type of the file (`dir`, `file` or `other`)
- `file_exists` — if the file exist or not (`true` or `false`)
- `file_size` — size of the file in bytes (or the sum of the files in directory)
- `file_last_modified` — timestamp of the last modification

---

### [Init Variables Gleeo Project Structure](actions/action_init_variables_gleeo_project_structure.md)

The action **Init Variables Gleeo Project Structure** initializes a variable with the domains, projects or tasks from *Gleeo Time Tracker*.

Examples:

- Load all Tasks of a project to show a selection list in Automagic.

#### Settings

##### Type

Whether to query the domains, projects or tasks.

##### Variable for Domains

The name of the variable for the domains. [Variables are supported.](#string-inline-expressions)

##### Variable for Projects

The name of the variable for the projects. [Variables are supported.](#string-inline-expressions)

##### All or Domain specific

Whether to query all projects or just the projects of one particular domain. [Variables are supported.](#string-inline-expressions)

##### Domain

The name of the domain to query. [Variables are supported.](#string-inline-expressions)

##### Variable for Tasks

The name of the variable for the tasks. [Variables are supported.](#string-inline-expressions)

##### All or Project specific

Whether to query all tasks or just the tasks of one particular project. [Variables are supported.](#string-inline-expressions)

##### Project

The name of the project to query. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `domains` — the list of domains
- `projects` — the list of projects
- `tasks` — the list of tasks

---

### [Init Variables Gleeo Recording](actions/action_init_variables_gleeo_recording.md)

The action **Init Variables Gleeo Recording** checks if a task is recording in **Gleeo Time Tracker** and stores the recording project and task in variables.

Examples:

- Store the recording task when someone calls and start recording the same task again when the call ends.
- Don't use a funny alert sound when you are working for a special project.

#### Settings

##### Variable for Recording Boolean

The name of the variable to store the boolean whether **Gleeo Time Tracker** is currently recording.

##### Variable for Recording Domain Title

The name of the variable to store the domain **Gleeo Time Tracker** is currently recording.

##### Variable for Recording Project Name

The name of the variable to store the project **Gleeo Time Tracker** is currently recording.

##### Variable for Recording Task Name

The name of the variable to store the task **Gleeo Time Tracker** is currently recording.

##### Variable for Recording Start Time

The name of the variable to store the start time of the currently recording task.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `recording` — the recording boolean
- `recording_domain_name` — the domain name
- `recording_project_title` — the project name
- `recording_task_name` — the task name
- `recording_start` — the start time of the currently recording task

---

### [Init Variables Media Metadata](actions/action_init_variables_media_metadata.md)

The action **Init Variables Media Metadata** loads the metadata of a media file into local variables (see variables section below).

Examples:

- Load the title of an mp3 and show the title in a notification.

#### Settings

##### File

The path or URL to the media file. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `media_cd_track_number` — the order of the audio data source on its original recording or null
- `media_album` — the album title or null
- `media_artist` — the artist or null
- `media_author` — the author or null
- `media_composer` — the composer or null
- `media_date` — the date when the data source was created or modified or null
- `media_genre` — the content type or genre or null
- `media_title` — the title or null
- `media_year` — the year when the data source was created or modified or null
- `media_duration` — the playback duration in milliseconds or null
- `media_num_tracks` — the number of tracks or null
- `media_writer` — the writer (such as lyricist) or null
- `media_mimetype` — the mime type or null
- `media_albumartist` — the performers/artist or null
- `media_disc_number` — the disc number or null
- `media_compilation` — the music album compilation or null
- `media_has_audio` — true if the media contains audio content
- `media_has_video` — true if the media contains video content
- `media_video_width` — the width of the video or null
- `media_video_height` — the height of the video or null
- `media_bitrate` — the bitrate of the media (in bits/sec) or null
- `media_location` — the location or null
- `media_video_rotation` — the video rotation angle in degrees or null
- `media_album_art` — the album art or null

---

### [Init Variables Media Session (Experimental)](actions/action_init_variables_media_session.md)

The action **Init Variables Media Session (Experimental)** fills the information of the media session of the specified media player into variables.

Examples:

- Check if Google Play Music is playing a track.

#### Settings

##### Package Names

The name of the media player to check. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `playback_state` — current state (0=none, 1=stopped, 2=paused, 3=playing, 4=fast forwarding, 5=rewinding, 6=buffering, 7=error, 8=connecting, 9=skip to previous, 10=skip to next, 11=skip to item in queue)
- `playback_position` — current position in ms
- `title` — the title
- `subtitle` — the subtitle
- `description` — the description
- `icon` — the current image
- `icon_uri` — the URI to load the image
- `media_duration` — duration of the track in ms

---

### [Init Variables Network Statistics](actions/action_init_variables_network_statistics.md)

The action **Init Variables Network Statistics** queries the transferred amount of data of the specified network interfaces.
The network statistics are recorded by the operating system itself and is stored in blocks of two hours (device dependent). Queries that don't fall on such a two hour limit, will be interpolated (device dependent) so results might not be accurate especially for short time intervals.
The data of the network statistics is stored for each UID (user identification) of the executed process. Many apps/packages of the system are aggregated under UID 1000 and can not be differentiated further. The package selection shows the UID in brackets.
Data not available to the network statistics of the device can not be considered by this action (e.g. when a device is factory reset).

Examples:

- Periodically check the amount of data transferred by a specific app and show a warning when 100 MB are exceeded.

#### Settings

##### Network interface

Whether to return mobile and/or WiFi statistics data.

##### Date range

The date range to query.

##### Cycle start day

The day of month when the bill cycle starts. [Variables are supported.](#string-inline-expressions)

##### From

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the start time of the event.

##### To

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the end time of the event.

##### Type

Whether to query information about all installed packages or only a few selected packages (based on UID).

##### Package Names for UIDs

The list of packages to query to determine the UIDs. Glob patterns (\*, ?) are supported. [Variables are supported.](#string-inline-expressions)

##### State

Whether to return foreground and/or background data.

##### Variable for transmitted bytes

The name of the variable to store the transmitted bytes.

##### Variable for received bytes

The name of the variable to store the received bytes.

##### Variable for total bytes

The name of the variable to store the total transferred bytes.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `transmitted_bytes` — the transmitted data in bytes
- `received_bytes` — the received data in bytes
- `total_bytes` — the total transferred data in bytes

---

### [Init Variables Network Traffic](actions/action_init_variables_network_traffic.md)

The action **Init Variables Network Traffic** initializes variables with the transmitted and received bytes since device boot of the system or a specific user ID that runs a given app.

Note: Some devices do not collect user/app specific values. This is also a known problem of Android 4.3.

Examples:

- Store the number of transferred data for each day in a log file.

#### Settings

##### Traffic

Whether the overall transferred data of the system should be stored or the transferred data transmitted by a particular app (respectively user ID).

##### Variable for total transmitted bytes

The name of the variable to store the sent bytes since device boot.

##### Variable for total received bytes

The name of the variable to store the received bytes since device boot.

##### Variable for mobile transmitted bytes

The name of the variable to store the sent bytes since device boot on the mobile interfaces.

##### Variable for mobile received bytes

The name of the variable to store the received bytes since device boot on the mobile interfaces.

##### Package Name

The name of the package to check (respectively the user that runs the app). [Variables are supported.](#string-inline-expressions)

##### Variable for transmitted bytes

The name of the variable to store the sent bytes of the user ID running the specified app since device boot.

##### Variable for received bytes

The name of the variable to store the received bytes of the user ID running the specified app since device boot.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `total_transmitted_bytes` — number of sent bytes or -1 when the device does not support this statistic
- `total_received_bytes` — number of received bytes or -1 when the device does not support this statistic
- `mobile_transmitted_bytes` — number of sent bytes over the mobile interfaces or -1 when the device does not support this statistic
- `mobile_received_bytes` — number of received bytes over the mobile interfaces or -1 when the device does not support this statistic
- `uid_transmitted_bytes` — number of sent bytes of the user ID or -1 when the device does not support this statistic
- `uid_received_bytes` — number of received bytes of the user ID or -1 when the device does not support this statistic

---

### [Init Variables Phone Info](actions/action_init_variables_phone_info.md)

The action **Init Variables Phone Info** initializes the desired variables (not all values are available on all devices).

Examples:

- Check the network operator once an hour.

#### Settings

##### SIM

The SIM card.

##### Variable Device ID (e.g. IMEI/MEID/ESN)

The name of the variable.

##### Variable Software Version (e.g. IMEI/SV)

The name of the variable.

##### Variable Line 1 Number (e.g. MSISDN)

The name of the variable.

##### Variable Network Country ISO

The name of the variable.

##### Variable Network Operator (e.g. MCC+MNC)

The name of the variable.

##### Variable Network Operator Name

The name of the variable.

##### Variable Phone Type

The name of the variable.

##### Variable SIM State

The name of the variable.

##### Variable SIM Country ISO

The name of the variable.

##### Variable SIM Operator

The name of the variable.

##### Variable SIM Operator Name

The name of the variable.

##### Variable SIM Serial Number

The name of the variable.

##### Variable Subscriber ID (e.g. IMSI)

The name of the variable.

##### Variable Voice Mail Alpha Tag

The name of the variable.

##### Variable Voice Mail Number

The name of the variable.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `device_id` — the device ID (e.g. IMEI/MEID/ESN), null when unavailable
- `device_software_version` — the software version (e.g. IMEI/SV), null when unavailable
- `line1_number` — the phone number string for line 1 (e.g. MSISDN), null when unavailable
- `network_country_iso` — the ISO country code (only when registered to a network, unreliable on CDMA)
- `network_operator` — numeric network operator name MCC+MNC (only when registered to a network, unreliable on CDMA)
- `network_operator_name` — network operator name (only when registered to a network, unreliable on CDMA)
- `phone_type` — type of the phone (0=no, 1=GSM, 2=CDMA, 3=SIP)
- `sim_state` — State of the SIM (0=unknown, 1=absent, 2=PIN required, 3=PUK required, 4=network locked, 5=ready)
- `sim_country_iso` — SIM ISO country code
- `sim_operator` — SIM MCC+MNC (only available when SIM in state ready)
- `sim_operator_name` — service provider name SPN (only available when SIM in state ready)
- `sim_serial_number` — serial number of the SIM, null when unavailable
- `subscriber_id` — the subscriber ID (e.g. IMSI), null when unavailable
- `voice_mail_alpha_tag` — the alphabetic identifier associated with the voice mail number
- `voice_mail_number` — the voice mail number, null when unavailable

---

### [Input Dialog](actions/action_input_dialog.md)

The action **Input Dialog** shows an input dialog with an input text field, password field, single- or multi-selection list.

Examples:

- Ask the user whether he wants to turn WiFi off or not.
- Ask for the password to use for an FTP upload.
- Ask whether airplane mode should be activated in the evening. Activate airplane mode when the user does not respond within 30 seconds.

#### Settings

##### Input Dialog Type

The type of the input dialog to show.

Can be one of:

- `Multi-line text` for multiple lines of plain text input
- `Single-line text` for a single line of plain text input
- `Password` for a password input
- `PIN` for a pin input
- `Number` to type number characters
- `Phone number` to type characters used in phone numbers
- `Date` to show a date picker
- `Time` to show a time picker
- `Date & Time` to show a dialog with a date & time picker
- `Single Choice Menu` for a list of values like a menu without OK, Cancel buttons
- `Multi Choice` for a list of values the user can choose multiple values from

##### Title

The title of the input dialog. [Variables are supported.](#string-inline-expressions)

##### Prompt (only applicable to `Text` and `Password`)

The question or input description to show in the input dialog. [Variables are supported.](#string-inline-expressions)

##### List Values (only applicable to `Single Choice` and `Multi Choice`)

A comma separated list of values to show as values the user can choose from. [Variables are supported.](#string-inline-expressions)

##### Default Value

The default value provided when the user does not change the input value. This value is also provided when the user cancels the dialog or hits the back key. [Variables are supported.](#string-inline-expressions)
Whether the user has cancelled the dialog can be evaluated using the variable `operation` (see below).

The default value for date/time input types must be formatted as specified below:

- `Date`: Pattern `yyyy-MM-dd` for example `2014-01-25` or when using a variable `{variable,dateformat,yyyy-MM-dd}`
- `Time`: Pattern `HH:mm` (24-hour format) for example `14:20` or when using a variable `{variable,dateformat,HH:mm}`
- `Date & Time`: Pattern `yyyy-MM-dd HH:mm` (time in 24-hour format) for example `2014-01-25 14:20` or when using a variable `{variable,dateformat,yyyy-MM-dd HH:mm}`

Values not formatted according to the rules above are ignored.

##### Font size

The size of the font used to enter text values.

##### Activate Timeout

Whether an automatic timeout should provide a value to the flow when the user does not react within the specified time.

##### Duration

The amount of time to automatically close the dialog and to continue the flow.

##### Value on Timeout

The value to provide to the flow when a timeout occurred. [Variables are supported.](#string-inline-expressions)

##### Options

- *Show when locked*: Show the input dialog even when the device is locked
- *Turn screen on*: Turn the screen on when the dialog is shown initially
- *Keep screen on*: Keep the screen on as long as the dialog is shown (power button still allows turn off the screen)
- *Enlarge dialog width*: Enlarge the width of the dialog to cover almost the entire screen
- *Keyboard hint to capitalize sentences*: Give a hint to the keyboard that sentences should be started with an uppercase letter

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `operation` — the operation used to close the dialog.

  Can be one of:
  - `ok` when the user pressed the OK button
  - `cancel` when the user pressed the cancel button or the back key
  - `timeout` when the dialog was closed by a timeout
- `value` —
  the selected value in the dialog or the list of values in case of `Multi Choice` or a date when the input dialog type was of type date/time.
  `value` for type *time* is the entered time of the current date.
- `index` — the index of the selected value of a `Single Choice` list or -1 when not definable
- `indices` — the indices of the selected values of a `Multi Choice` list or -1 for every not definable value

---

### [Input Speech (Android Wear)](actions/action_input_speech_wear.md)

The action **Input Speech (Android Wear)** starts the speech recognition of the device and provides the recognized text to the flow in variable `value`. The speech recognition engine usually requires network access.

Examples:

- Control Automagic using spoken commands.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### UI Mode

Whether user interface should be shown or the speech recognition should be executed in the background.

##### Prompt

An optional title to show in the user interface. This setting might be ignored by the engine. [Variables are supported.](#string-inline-expressions)

##### Language

Optional the desired language to use in the speech recognition engine. This setting might be ignored by the engine. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `value` — the recognized text
- `operation` — whether the recognition was successful (ok) or not (cancel)

---

### [Input Speech (Experimental)](actions/action_input_speech.md)

The action **Input Speech (Experimental)** starts the speech recognition of the device and provides the recognized text to the flow in variable `value`. The speech recognition engine usually requires network access.

Examples:

- Control Automagic using spoken commands.

#### Settings

##### UI Mode

Whether user interface should be shown or the speech recognition should be executed in the background.

##### Prompt

An optional title to show in the user interface. This setting might be ignored by the engine. [Variables are supported.](#string-inline-expressions)

##### Language

Optional the desired language to use in the speech recognition engine. This setting might be ignored by the engine. [Variables are supported.](#string-inline-expressions)

##### Use Bluetooth headset (Android 3+)

Whether or not a Bluetooth headset is used.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `value` — the recognized text
- `operation` — whether the recognition was successful (ok) or not (cancel)

---

### [Kill App](actions/action_kill_app.md)

The action **Kill App** kills the processes of an app running in the background.

Warning: The operating system does not allow to kill an app currently running in the foreground.

Examples:

- Kill the browser app when another app is started to reclaim memory.

#### Settings

##### Package Name

The name of the package to kill. [Variables are supported.](#string-inline-expressions)

---

### [Kill App Process](actions/action_kill_app_process.md)

The action **Kill App Process** sends the defined signal to the process using the `kill` command.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Kill the browser app when another app is started to reclaim memory.

#### Settings

##### Package Name

The name of the package to kill. [Variables are supported.](#string-inline-expressions)

##### Signal

The signal to send.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `pid` — the id of the process
- `importance` — the importance of the process. The smaller the value the higher the importance.
- `lru` — least recently used. Smaller value means more recently used.
- `uid` — the user id of the process

---

### [Launch App](actions/action_launch_app.md)

The action **Launch App** starts an app or a specific activity of an app.

Tip: Some activities require special permissions to be launched. Check the log after testing the action when an activity fails to start.

Examples:

- Start the development settings directly using a shortcut.
- Start the shopping list app when you are near the shopping mall.

#### Settings

##### Package Name

The name of the package to launch. [Variables are supported.](#string-inline-expressions)

##### Class Name

The specific activity to launch.
Leave empty to launch the default activity of a package. [Variables are supported.](#string-inline-expressions)

---

### [Launch Shortcut](actions/action_launch_shortcut.md)

The action **Launch Shortcut** starts a previously defined shortcut.

A new shortcut can either be built with button *Build Shortcut* or you can let Automagic capture the shortcut by leaving the action configuration open and by creating the shortcut in the other app. Automagic will show a notification on screen *Shortcut captured by Automagic* when the shortcut was properly detected by Automagic. Note that not all apps support both ways to create a shortcut.

Examples:

- Open a specific settings page.
- Play an audio playlist.
- Directly display a contact.

---

### [Lock Device](actions/action_lock_device.md)

The action **Lock Device** immediately locks the device.

Note: The device admin functions have to be enabled in the preferences to use this action.

Examples:

- Lock the device when an SMS contains **device lost!**.

---

### [Mail with Gmail](actions/action_mail_gmail.md)

The action **Mail with Gmail** sends a mail using your Gmail account.

Note: If you have enabled **2-step verification** in your Google account then you need to create an application specific password for login in the settings of your google account: <https://www.google.com/settings/security>

Examples:

- Forward every SMS as a mail to your inbox.
- Send your location every 30 minutes to your girlfriend.
- Send the new **Gleeo Time Tracker** backups to your inbox.

#### Settings

##### Authentication

Whether to use an account available on the device (OAuth) or to enter an account name and password.

##### Mail Account

The account name to use like `xyz@gmail.com`. [Variables are supported.](#string-inline-expressions)

##### Password

The password to your mail account. [Variables are supported.](#string-inline-expressions)

Info: The password is stored encrypted on the internal device storage and is not part of the regular `flows.xml` file.

##### To

The mail address of the recipient. [Variables are supported.](#string-inline-expressions)

##### Reply To

The address to send responses to. [Variables are supported.](#string-inline-expressions)

##### Subject

The subject of the mail. [Variables are supported.](#string-inline-expressions)

##### Body

The message body of the mail. [Variables are supported.](#string-inline-expressions)

##### Body MIME Type

Whether the body should is HTML or should be interpreted as plain unformatted text.

##### Files to Attach

The comma separated list of files to attach. [Variables are supported.](#string-inline-expressions)

Tip: Files stored in a list by action **Init Variable File List** can be formatted using `{files,listformat,comma}` to a comma separated list.

---

### [Map Values](actions/action_map_values.md)

The action **Map Values** takes an input value (the key) and maps it to an output value.

Examples:

- Scan the barcode on the laboratory door and map the value to a project/task to start the time tracker.

#### Settings

##### Input Value

The input value to map to another value. [Variables are supported.](#string-inline-expressions)

Examples:

- `{barcode_text}` to map a barcode
- `{incoming_number}` to map the number of an incoming call

##### Mapping Definition

The definition used to specify how the values should be mapped to the target values. [Variables are supported.](#string-inline-expressions)

Mapping example:
`key1=>value1`
`key2=>value2`

The part before the assignment operator (`=>`) is used to specify the key values to match. A comma separated list can be used to specify multiple keys for one target value. Glob pattern characters `*` and `?` can also be used to match multiple values.
The part after the assignment operator (`=>`) defines the target value to use as the map value.
The mapping rules are evaluated line by line from top to bottom. The first matching rule is applied.

Multi key mapping example:
`key1=>value1`
`key2,key3,key4=>value2`

Glob pattern mapping example:
`key1=>value1`
`key?=>value2`
`key*=>value3`

In the above example, the value `key1` would be mapped to `value1` because it is the first line matching the input value.
The values `key2` to `key9` would be matched by the second rule.
The value `key123` would be matched by the third rule.

When no rule matches the output value is set to `null`.

If you want to map a few known bar codes to meaningful task names but also want to use the plain barcode when no mapping rule matches, you can use the following approach (the input value would be set to `{barcode_text}` in this example):

Mapping definition:
`123321123=>Meeting`
`989878945=>Office`
`*=>{barcode_text}`

The third rule matches all unknown bar code values and maps the value to the original value. You can also use a condition **Expression** to detect not mappable values.

The last twenty not mappable values detected while executing the action will be remembered in a list and can be added by using the button **Add unmapped values...**

##### Output Variable

The name of the variable to store the result in (usually without curly braces except when you want to create dynamically named variables). [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `mapped_value` — the target value

---

### [Message Dialog](actions/action_message_dialog.md)

The action **Message Dialog** shows a dialog with a message and an optional title.

Examples:

- Show the text of an incoming SMS directly in a dialog.

#### Settings

##### Title

The optional title of the dialog. [Variables are supported.](#string-inline-expressions)

##### Message

The message to show in the dialog. [Variables are supported.](#string-inline-expressions)

##### Button Label

The label of the button. The button is not shown when the text is empty. [Variables are supported.](#string-inline-expressions)

##### Activate Timeout

Whether an automatic timeout should automatically hide after the specified time.

##### Duration

The amount of time to automatically close the dialog and to continue the flow.

---

### [Modify Automagic Notification on Statusbar](actions/action_modify_automagic_notification_status_bar.md)

The action **Modify Automagic Notification on Statusbar** modifies the permanent notification usually shown by Automagic for technical reasons. The appearance of a modified notification is reset to the default when one of the settings in Automagic pertaining to the notification is changed.

Examples:

- Show a different icon when a particular flow is running.

#### Settings

##### Icon

The icon to use for this notification.

Custom icons are supported starting with Android 6.

Note: Android will usually show all non-transparent parts as white so it's recommended to create custom PNG images with a transparent background and a white color to paint the contents.
Note: Option 'Custom icon' can lead to crashes on some devices with Android 6.0.

##### Title

The title of the notification. [Variables are supported.](#string-inline-expressions)

##### Message

The message of the notification. [Variables are supported.](#string-inline-expressions)

##### Accent color

The color used by the device for in the notification (usually the background color of the icon in the expanded statusbar).

##### Category (Android 5+)

The category of the notification. The category defines if a notification is allowed to pass the interruptions filter.

##### Priority (Android 4.1+)

Defines the priority of the notification. A notification with a low priority might be displayed in the expanded statusbar only (depends on Android version).

##### Visibility (Android 5+)

Whether notifications are secret, private or public which defines whether the notifications are displayed on the lock screen or not. The Lock screen must also be configured appropriately.

##### Big Message (Android 4.1+)

Defines a big message that will be displayed when the notification is expanded (by swiping down on the notification). The notification usually also shows the big message when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting. [Variables are supported.](#string-inline-expressions)

##### Show progressbar

Defines whether a progressbar should be shown in the notification.

##### Indeterminate progress

Whether the progress should be indeterminate.

##### Progressbar value / Max value

The current value of the progress and the maximum value (100%). [Variables are supported.](#string-inline-expressions)

##### Large Icon (Android 3+)

Defines whether a large icon should be displayed in the notification. [Variables are supported.](#string-inline-expressions)

##### Group (Android 7+)

Defines the group of this notification. [Variables are supported.](#string-inline-expressions)

##### Group summary (Android 7+)

Defines whether this notification is the group summary for this group. [Variables are supported.](#string-inline-expressions)

##### Actions (Android 4.1+)

Up to three actions displayed as buttons when the notification is expanded (by swiping down on the notification). The notification usually also shows the action buttons when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting.

Tip: Use action **Execute Flows** to execute a complex flow consisting of multiple actions and conditions.

Following variables are supplied to the executed action:

- `action_number`: contains the number of the action (1, 2 or 3)
- `action_text`: the text label of the selected action button on the notification

---

### [Modify Call Log](actions/action_modify_call_log.md)

The action **Modify Call Log** marks the entries of the call log as acknowledged or clears the call log.

Examples:

- Delete the call log every Monday morning.

#### Settings

##### Operation

if the entries should be marked as acknowledged or if the call log should be cleared.

##### Numbers

The list of call numbers to delete. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter on similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

---

### [Modify Image](actions/action_modify_image.md)

The action **Modify Image** can be used to modify an image that was previously loaded with an action **Init Variable Image File**.

Examples:

- Load an image, shrink the size and send the smaller file by mail.

#### Settings

##### Variable

The name of the variable holding the pixel data of the image. [Variables are supported.](#string-inline-expressions)

##### Operation

The type of modification to apply to the image:

- *Scale*: change the size of the image either respecting the aspect ratio or by distorting the image
- *Rotate*: rotates the image by 90° or 180°
- *Mirror*: mirrors the image horizontally or vertically
- *Crop & Scale*: extracts the largest possible area from the center of the image by respecting the aspect ratio of the original image and scales to the desired size
- *Crop to Selection*: crops the image to the defined area

##### Width (Scale)

The new width of the image. The width is adjusted proportionally, when only the new height is specified. [Variables are supported.](#string-inline-expressions)

##### Height (Scale)

The new height of the image. The height is adjusted proportionally, when only the new width is specified. [Variables are supported.](#string-inline-expressions)

##### Rotate

How the image should be rotated.

##### Mirror

If the image should be mirrored horizontally or vertically.

##### Width (Crop & Scale)

The new width of the image. [Variables are supported.](#string-inline-expressions)

##### Height (Crop & Scale)

The new height of the image. [Variables are supported.](#string-inline-expressions)

##### X, Y (Crop to Selection)

The X and Y position of the selection. [Variables are supported.](#string-inline-expressions)

##### Width, Height (Crop to Selection)

The width and height of the selection. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `image_data` — the local variable of the image
- `image_width` — the width of the image after the modification
- `image_height` — the height of the image after the modification

---

### [Modify Notification Channel](actions/action_modify_notification_channel.md)

The action **Modify Notification Channel** modifies a notification channel.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Change notifications about app updates to important at day and unimportant at night to avoid interruptions at night.

#### Settings

##### Package Name

The package name of the app to modify the settings for. [Variables are supported.](#string-inline-expressions)

##### Notification channel ID

The ID of the channel. [Variables are supported.](#string-inline-expressions)

##### Importance

How important notifications should be treated.

##### Sound

The sound to play.

##### Lockscreen visibility

How the notifications should be shown on the lockscreen.

##### Show notification dot

Whether to show a notification dot or not.

##### Override Do Not Disturb

Whether to ignore DnD mode or not.

##### Vibrate

Whether notifications should vibrate or not.

##### Flash LED

Whether notifications should activate the notification light.

---

### [Move Files](actions/action_move_files.md)

The action **Move Files** locally moves one or a list of files to the specified target directory or file.
A move is implemented to use a `rename` operation when possible. If a `rename` is not possible, the file/folder is copied to the target directory and afterwards the source is deleted.

Examples:

- Move all files in directory `/mnt/sdcard/xyz/` to the folder `/mnt/sdcard/xyz_backup/`.
- Rename directory `/mnt/sdcard/xyz` to `/mnt/sdcard/xyz_backup`.

#### Settings

##### Source Files

A comma separated list of files or directories to move. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

When multiple files are matched the target has to be a directory. The directory will be created when it does not exist yet.
A directory with an ending slash (like `/mnt/sdcard/`) matches the files contained in the directory like using `/mnt/sdcard/*`.

##### Target

The absolute path of the target file or directory. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Notification on Screen](actions/action_notification_screen.md)

The action **Notification on Screen** shows a notification on the screen for a short period of time.

Examples:

- Show a notification when a background flow sends your location by mail.
- Show a notification with the text of a received SMS.

#### Settings

##### Type

Whether a simple text or a custom widget should be shown in the notification.

##### Text

The text to show. [Variables are supported.](#string-inline-expressions)

##### Widget

The name of the widget to display. [Variables are supported.](#string-inline-expressions)

##### Width/Height

The size of the overlay. [Variables are supported.](#string-inline-expressions)

##### Opacity

The transparency respectively opacity of the widget.

##### Stretch widget

Whether the widget should be stretched to fill the entire area of the overlay.

##### Duration

Whether to show the duration for a short duration (about 2 seconds) or longer (about 4 seconds).

##### Custom position

Whether the notification should be show at the default location or at a custom defined position.

##### Gravity

The position to align the notification on the screen.

##### X/Y-Offset

The offset of the notification relative to the gravity. [Variables are supported.](#string-inline-expressions)

---

### [Notification on Screen (Android Wear)](actions/action_notification_screen_wear.md)

The action **Notification on Screen (Android Wear)** shows a notification on the screen for a short period of time.

Examples:

- Show a notification when a background flow sends your location by mail.
- Show a notification with the text of a received SMS.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Type

Whether a simple text or a custom widget should be shown in the notification.

##### Text

The text to show. [Variables are supported.](#string-inline-expressions)

##### Widget

The name of the widget to display. [Variables are supported.](#string-inline-expressions)

##### Width/Height

The size of the overlay. [Variables are supported.](#string-inline-expressions)

##### Opacity

The transparency respectively opacity of the widget.

##### Stretch widget

Whether the widget should be stretched to fill the entire area of the overlay.

##### Duration

Whether to show the duration for a short duration (about 2 seconds) or longer (about 4 seconds).

##### Custom position

Whether the notification should be show at the default location or at a custom defined position.

##### Gravity

The position to align the notification on the screen.

##### X/Y-Offset

The offset of the notification relative to the gravity. [Variables are supported.](#string-inline-expressions)

---

### [Notification on Statusbar](actions/action_notification_status_bar.md)

The action **Notification on Statusbar** shows a notification on the status bar. The notification is displayed until the notification is clicked or clear is pressed.

Examples:

- Show a notification when a background flow sends your location by mail.

#### Settings

##### Icon

The icon to use for this notification.

Custom icons are supported starting with Android 6.

Note: Android will usually show all non-transparent parts as white so it's recommended to create custom PNG images with a transparent background and a white color to paint the contents.
Note: Option 'Custom icon' can lead to crashes on some devices with Android 6.0.

##### Title

The title of the notification. [Variables are supported.](#string-inline-expressions)

##### Message

The message of the notification. [Variables are supported.](#string-inline-expressions)

##### Channel (Android 8+)

The ID of the notification channel to use. [Variables are supported.](#string-inline-expressions)
Apps can not change the channel settings once the channel has been created. Use the button **Channel settings…** to change the settings once the channel has been created or use an action **Modify Notification Channel** to change the settings on supported devices.
The initial channel settings are inferred from the settings in the notification action based on the settings like **Play Sound**, **Vibrate**, **Flash LED**, **Priority** and **Visibility**.

##### Play Sound

Plays the default notification sound when checked.

##### Vibrate

Vibrates when checked.

##### Flash LED

Flash the notification LED using the supplied color and blink rate. Notification LED and user defined colors are not supported on all devices.

##### Local only

Whether it's recommended to show this notification only on the main device but not on paired devices like an Android Wear watch.

##### Accent color

The color used by the device for in the notification (usually the background color of the icon in the expanded statusbar).

##### Ongoing

Flags this notification as an ongoing event and prevents the removal of this notification from the statusbar. A notification ID is mandatory when this option is selected.

##### Keep on Clear

Prevents the removal of this notification from the statusbar. A notification ID is mandatory when this option is selected.

##### Notification ID

Defines the ID (a number from 1 to 999) to use as the identification of this notification. [Variables are supported.](#string-inline-expressions)
This is useful when the notification is used for trigger **Notification on Statusbar Selected** or when the notification is used to show a profile like status.
A notification with the same ID replaces an older notification of the same ID. The notification can be removed from the statusbar using the action **Remove Notification on Statusbar**.

The button **Remove, X** can be used to remove a notification with this ID on the statusbar.

##### Category (Android 5+)

The category of the notification. The category defines if a notification is allowed to pass the interruptions filter.

##### Priority (Android 4.1+)

Defines the priority of the notification. A notification with a low priority might be displayed in the expanded statusbar only (depends on Android version).
Settings like **Play Sound** and **Vibrate** can be ignored by the system when the priority is low or forced when the priority is high.

Note: On Android 8+ the priority is mapped to notification channel importance as follows: Minimum‑>Low, Low‑>Medium, Normal‑>High, High‑>Urgent, Maximum‑>Maximum.

##### Visibility (Android 5+)

Whether notifications are secret, private or public which defines whether the notifications are displayed on the lock screen or not. The lock screen must also be configured appropriately.

##### Big Message (Android 4.1+)

Defines a big message that will be displayed when the notification is expanded (by swiping down on the notification). The notification usually also shows the big message when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting. [Variables are supported.](#string-inline-expressions)

##### Show progressbar

Defines whether a progressbar should be shown in the notification.

##### Indeterminate progress

Whether the progress should be indeterminate.

##### Progressbar value / Max value

The current value of the progress and the maximum value (100%). [Variables are supported.](#string-inline-expressions)

##### Large Icon (Android 3+)

Defines whether a large icon should be displayed in the notification. [Variables are supported.](#string-inline-expressions)

##### Group (Android 7+)

Defines the group of this notification. [Variables are supported.](#string-inline-expressions)

##### Group summary (Android 7+)

Defines whether this notification is the group summary for this group. [Variables are supported.](#string-inline-expressions)

##### Actions (Android 4.1+)

Up to three actions displayed as buttons when the notification is expanded (by swiping down on the notification). The notification usually also shows the action buttons when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting.

Tip: Use action **Execute Flows** to execute a complex flow consisting of multiple actions and conditions.

Following variables are supplied to the executed action:

- `action_number`: contains the number of the action (1, 2 or 3)
- `action_text`: the text label of the selected action button on the notification

##### Actions for Android Wear (Android 4.1+)

Up to three actions to show on an Android Wear device. When such an action is defined, the other actions are usually not displayed anymore on the Android Wear device.

Tip: Use action **Execute Flows** to execute a complex flow consisting of multiple actions and conditions.

Following variables are supplied to the executed action:

- `action_number`: contains the number of the action (1, 2 or 3)
- `action_text`: the text label of the selected action button on the notification
- `input_value`: the selected input value or the recognized text of the speech input

---

### [Open URL in Browser](actions/action_open_browser_url.md)

The action **Open URL in Browser** opens the browser with the specified URL.

Tip: The browser can also be used to download a file by using a URL pointing to a PDF or other downloadable file.

Examples:

- Open a news page every morning.
- Download a PDF every morning at 5am.

#### Settings

##### URL

The url to open. [Variables are supported.](#string-inline-expressions)

Tip: You can use a variable to open n URL that changes dynamically by date.

`http://test.com/newspaper_{triggertime,dateformat,yyyyMMdd}.pdf`

will be replaced to

`http://test.com/newspaper_20120123.pdf`

##### Use defined app

Whether to use a defined app to open the URL or to let the system choose the most appropriate app.

##### Package Name

The app to open the URL. [Variables are supported.](#string-inline-expressions)

##### Class Name

The component inside the app to open the URL with. [Variables are supported.](#string-inline-expressions)

---

### [Perform Action on Notification on Statusbar](actions/action_perform_action_notification_status_bar.md)

The action **Perform Action on Notification on Statusbar** clicks the notification or one of the action buttons which are usually available in the big, expanded notification on Android 4.1+.
The flow must be executed by a trigger **Notification on Statusbar Displayed** or the action after a condition **Notification on Statusbar Displayed** otherwise Automagic has no possibility to access the notification.

Warning: Android 4.1+ is required. This function is not officially supported by Android and might not work on all devices.

Examples:

- Automatically archive a mail when the mail contains a specific text.

#### Settings

##### Action Type

Whether to perform a click on the notification or to perform a click on a button of the notification or to execute an action of a wearable.

##### Button

The label of the button to click. The label needs to match the entered text exactly. [Variables are supported.](#string-inline-expressions)

##### Wearable Action

The name of the wearable action. [Variables are supported.](#string-inline-expressions)

##### Input

The text to pass to the wearable action (only takes effect when the action allows text input). [Variables are supported.](#string-inline-expressions)

---

### [Plugin (Experimental)](actions/action_plugin.md)

The action **Plugin (Experimental)** executes the action defined in a plugin. Most plugins don't offer a way to let Automagic wait for the plugin to finish. You can use an action **Sleep** to wait a short amount of time.

Warning: This function is experimental and might not work with all existing plugins available in Google Play. We can not provide support for plugins.

Note: Plugins can be defined using the interface description available from the app Locale: [Locale developer documentation](http://www.twofortyfouram.com/developer) and Tasker: [Tasker plugin extensions](http://tasker.dinglisch.net/plugins.html).

#### Settings

##### Plugin

List of all available plugins found on the device.

##### replace variables/modify configuration

Script to dynamically replace variables and to modify the configuration passed to the plugin.

##### Synchronous with Timeout

Whether the plugin should be invoked synchronously and Automagic should wait for the plugin to return a result or not.
Only a few new plugins support this mechanism, this mechanism should usually not be used when the plugin does not request to be executed this way. This option will automatically be enabled when the plugin is configured and the plugin supports synchronous execution.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `Tasker variables` — takes over the local Tasker variables returned by the plugin (without leading %-character)

---

### [Post Tweet](actions/action_post_tweet.md)

The action **Post Tweet** posts a regular Twitter message.

Examples:

- Tweet your location every hour.

#### Settings

##### Twitter Account

The Twitter account used to send the message.

##### Message

The message to send. [Variables are supported.](#string-inline-expressions)

##### Image files

The images to attach to the tweet. [Variables are supported.](#string-inline-expressions)

---

### [Post Twitter Direct Message](actions/action_post_twitter_direct_message.md)

The action **Post Twitter Direct Message** posts a Twitter direct message to one recipient.

Examples:

- Tweet your location every hour to your wife.

#### Settings

##### Twitter Account

The Twitter account used to send the message.

##### To

The recipient of the direct message (without leading @). [Variables are supported.](#string-inline-expressions)

##### Message

The message to send. [Variables are supported.](#string-inline-expressions)

---

### [Query Content Provider](actions/action_query_content_provider.md)

The action **Query Content Provider** allows to load data from a content provider of another app. A content provider presents data to Automagic as one or more tables that are similar to the tables found in a relational database.

Warning: This function allows to access data that's not officially made available by Android which might not be available on all device models and Android Version.

#### Settings

##### Content URI

The URI of the content provider data. [Variables are supported.](#string-inline-expressions)

##### Projection

The list of tables to return. [Variables are supported.](#string-inline-expressions)

##### Selection

A filter declaring which rows to return, formatted like an SQL WHERE clause (excluding the WHERE itself). The selection can include ?-characters that will be replaced by the values provided in the *Selection Arguments* from the content provider. [Variables are supported.](#string-inline-expressions)

##### Selection Arguments

The values to use in the selection for each provided ?-character. [Variables are supported.](#string-inline-expressions)

##### Sort Order

How to order the rows, formatted as an SQL ORDER BY clause (excluding the ORDER BY itself). [Variables are supported.](#string-inline-expressions)

##### Result Type

Defines how Automagic should provide the data to the flow:

- `Table`: Provides a list of rows each containing a list of values to the flow.
- `Table (transposed)`: Same as table but transposed. Provides a list for each column containing all values of the column.
- `List`: Converts the returned table to a flat list.
- `Single value`: Provides only the first value of the returned data to the flow.
- `Text`: Converts the returned table to a CSV-text.

##### Include header row

Whether or not the returned result should include a row with the column titles.

##### Variable

The name of the variable to store the result in. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `result` — the resulting data as defined in *Resultat-Typ*

---

### [Reboot](actions/action_reboot.md)

The action **Reboot** restarts the device.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Restart the device every morning at 6am.

#### Settings

##### Options

Options to pass to the kernel when the device is restarted. For example `recovery` to boot into recovery mode. [Variables are supported.](#string-inline-expressions)

---

### [Remove Notification Missed Calls](actions/action_remove_missed_calls_notification.md)

The action **Remove Notification Missed Calls** removes the missed calls notification in the statusbar.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Remove the missed calls notification when a number on a blocking list called in your absence.

---

### [Remove Notification on Statusbar](actions/action_remove_notification_status_bar.md)

The action **Remove Notification on Statusbar** removes the specified or all notifications on the statusbar added by the action **Notification on Statusbar**.

Example:

- Show a notification when a sound profile is active and remove the notification when the sound profile is deactivated.

#### Settings

##### Notification Type

Whether the action should affect only notifications of Automagic or notifications of all apps in general (Android 4.3+)

##### Automagic Notification ID

The ID of the notification to remove. The ID must match the ID used in the action **Notification on Statusbar**. [Variables are supported.](#string-inline-expressions)
**All** removes all removable notifications of Automagic irrespective of the ID.

##### Notifications

Whether to remove all removable notifications or only the notifications of the specified app.

##### Package Names

The names of the packages/apps to remove the notifications from. [Variables are supported.](#string-inline-expressions)

##### Notification ID

The ID of the notification to remove. [Variables are supported.](#string-inline-expressions)
Trigger **Notification on Statusbar Displayed** provides the ID of the notification in variable `id`. Use `{id}` to remove the notification that triggered the flow.

##### Filter

Defines the text that must be contained in one of the available fields. [Variables are supported](#string-inline-expressions) for *contains text* and *matches glob*.

---

### [Remove WiFi Access Point](actions/action_remove_wifi_access_point.md)

The action **Remove WiFi Access Point** removes a WiFi configuration.

Warning: This function can only remove access points that have been added by Automagic on Android 6+.

Examples:

- Remove a previously added public access point to clean up the list.

#### Settings

##### SSID

The SSID of the Access Point. [Variables are supported.](#string-inline-expressions)

---

### [Request Sync](actions/action_request_sync.md)

The action **Request Sync** starts the synchronisation process of one or multiple accounts or some parts of the accounts. The order and the exact timing of the synchronisation is controlled by Android.
The action does not wait for the synchronisation to finish.

Examples:

- Disable the automatic synchronisation to save battery but execute the synchronisation manually every hour between 8am and 8pm.

#### Settings

##### Accounts

The accounts to synchronize in format *Type*:*Name*.
Glob patterns can be used to match multiple accounts. [Variables are supported.](#string-inline-expressions)

- `*` synchronises all accounts
- `Google:*` synchronises all Google accounts

##### Authorities

The parts/databases of the accounts to synchronize. Specify a `*` to synchronize all parts of the account.
Glob patterns can be used to match multiple authorities. [Variables are supported.](#string-inline-expressions)

- `*` synchronises all authorities of the specified accounts
- `com.android.calendar` synchronises all calendars of the specified accounts

---

### [Reregister Media Button Receiver](actions/action_reregister_media_button_receiver.md)

The action **Reregister Media Button Receiver** registers Automagic as a receiver of media button events again.
This is useful in conjunction with trigger **Media Button Receiver** when another app requested to receive the media button events and Automagic thus does not receive the events anymore.

---

### [Restore Audio Volumes](actions/action_restore_audio_stream_volume.md)

The action **Restore Audio Volumes** restores the audio volumes previously stored in global variables by action **Store Audio Volumes**.

Examples:

- Store the audio volumes when a meeting begins, set all volumes to zero and restore the previously volumes when the meeting ends.

#### Settings

##### Alarm

Whether or not to restore the alarm volume and the name of the variable to restore the volume from.

##### DTMF

Whether or not to restore the DTMF volume and the name of the variable to restore the volume from.

##### Music

Whether or not to restore the music volume and the name of the variable to restore the volume from.

##### Notification

Whether or not to restore the notification volume and the name of the variable to restore the volume from.

##### Ring

Whether or not to restore the ringtone volume and the name of the variable to restore the volume from.

##### System

Whether or not to restore the system volume and the name of the variable to restore the volume from.

##### Voice Call

Whether or not to restore the voice call volume and the name of the variable to restore the volume from.

##### Ringer Mode

Whether or not to restore the ringer mode and the name of the variable to restore the value from.

##### Interruptions Mode

Whether or not to restore the interruptions mode and the name of the variable to restore the value from.

---

### [Save Variable in Image File](actions/action_save_variable_image_file.md)

The action **Save Variable in Image File** saves the pixel data that was previously loaded with an action **Init Variable Image File** into a file.

Examples:

- Load an image, shrink the size and send the smaller file by mail.

#### Settings

##### Variable

The name of the variable holding the pixel data of the image. [Variables are supported.](#string-inline-expressions)

##### File

The path of the file to store the image in. The type is determined by the file extension. (.jpg, .webp and .png are supported). [Variables are supported.](#string-inline-expressions)

##### Image quality

How much the file should be compressed (0=small file/bad image quality, 100=big file/good image quality). The image quality is ignored for PNG-files. [Variables are supported.](#string-inline-expressions)

---

### [Save Widget to Image File](actions/action_save_widget_image_file.md)

The action **Save Widget to Image File** saves the current image of a widget to a file.

Examples:

- Add a text over an image and send the resulting image as an email attachment.

#### Settings

##### Widget

The name of the widget to save as an image. [Variables are supported.](#string-inline-expressions)

##### File

The path of the file to store the image in. The type is determined by the file extension. (.jpg, .webp and .png are supported). [Variables are supported.](#string-inline-expressions)

##### Image quality

How much the file should be compressed (0=small file/bad image quality, 100=big file/good image quality). The image quality is ignored for PNG-files. [Variables are supported.](#string-inline-expressions)

---

### [Scan Barcode](actions/action_scan_barcode.md)

The action **Scan Barcode** opens an activity to scan a barcode using the camera of the device.

Tip: You can use an action **Map Values** to map known barcode values like a QR code on a laboratory door to a project/task.

Examples:

- Start recording the time in **Gleeo Time Tracker** based on a barcode on a laboratory door.
- Scan a barcode on a book and open the browser to search the book on Amazon.

#### Settings

##### Timeout

The timeout duration to automatically cancel the barcode scan.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `operation` — the operation used to close the scan barcode activity.

  Can be one of:
  - `ok` when a bar code has been successfully scanned
  - `cancel` when the user pressed the back button or another button to leave the activity
  - `timeout` when the activity was closed by a timeout
- `barcode_text` — the value of the barcode as a text string
- `barcode_format` — the format of the barcode

---

### [Script](actions/action_script.md)

The action **Script** executes a script doing some simple calculations and can be used to modify variables.

### Script Description

### Reserved Keywords

Following list of keywords are reserved and are therefore not allowed to be used as a variable name:
```
 abstract alias and AND assert
    boolean break byte
    case catch char class const continue
    def default do double
    else elsif ensure enum extends
    false final finally float for
    goto
    if implements import in instanceof int interface
    long
    mod
    native new next not NOT null
    or OR
    package private protected public
    redo repeat rescue retry return
    self short static strictfp super switch synchronized
    then this throw throws to transient true try
    undef unless until
    void volatile
    when while
    xor XOR
    yield
```

Only a few of the reserved keywords are currently used but are reserved for future extensions of the scripting language.

### Comments

Scripts can contain comments that are not executed when the script is interpreted.

- text after `//` to the end of the line
- text between `/*` and `*/`. Such a comment can also span multiple lines.

Examples:
```
    a=1+2;//this is a comment
    b=a+3;
    c=b+a;
    /* this is a
        multiline comment */
    d=c*2;
```

### Variables

A value like a number or a string can be stored in a variable using the assignment operator `=`
Variable names are case sensitive. A variable name has to start with a letter, a currency symbol (such as "$") or a connecting punctuation character (such as "\_"). The rest of the variable name can also contain digits. Unicode characters are supported, but it is highly recommended to use US-ASCII characters.

Examples:
```
    a = 3;//assign the number three to the variable a
    b = a;//assign the value stored in variable a to the variable b
```

There exist two types of variable scopes:

#### Flow Local

Every variable declared in a script, expression or inline script is by default flow local as long as the name of the variable does not start with `global_`.

Examples of flow local variables with a value assigned:

- `a = 1;`   number one stored in a variable called 'a'
- `var1 = 1.234;`   decimal number 1.234 stored in a variable called 'var1'
- `var_123 = "Hello World";`   string "Hello World" stored in a variable called 'var\_123'
- `_m = true;`   boolean value 'true' stored in a variable called '\_m'
- `var2 = a;`   stores the value stored in variable 'a' in a variable called 'var2'

#### Global

Every variable that starts with `global_` is global and therefore accessible by other flows and will also be persisted to the external memory and reloaded when you stop/restart the Automagic service.

Examples of global variables with a value assigned:

- `global_a = 1;`   number one stored in a variable called 'global\_a'
- `global_var1 = 1.234;`   decimal number 1.234 stored in a variable called 'global\_var1'
- `global_var_123 = "Hello World";`   string "Hello World" stored in a variable called 'global\_var\_123'
- `global_m = true;`   boolean value 'true' stored in a variable called 'global\_m'

Variables are references to values (like a pointer). Assigning the value stored in a variable to another variable does not copy the value but both variables point to the exact same value.
This is especially important when modifiable values like lists are used.
Example:
```
    a = newList(1, 2, 3);
    b = a;
    //at this point both variables a and b point to the exact
    // same list (the list only exists once)
    addElement(a, 4);
    //the list now contains 1, 2, 3, 4
    //both variables a and b still point to the same list

    //both loops therefore print the values 1, 2, 3 and 4 in the log:
    for (x in a)
    {
        log("{x}");
    }

    for (x in b)
    {
        log("{x}");
    }
```

### Operators

Following operators are supported in expressions:

- `+`    addition and string concatenation
- `-`    subtraction
- `*`    multiplication
- `/`    division
- `%`    modulo division
- `<`    less than
- `<=`    less than or equal
- `>`    greater than
- `>=`    greater than or equal
- `==`    equal
- `!=`    not equal
- `AND`, `&&`    and
- `OR`, `||`    or
- `XOR`, `^`    exclusive or
- `NOT`, `!`    not (unary)

### Expressions

An expression is a construct made up of variables, operators and function calls, that evaluates to a single value.

Examples:

- `42`
- `1+2`
- `a=1`
- `b=a+1`
- `c=(a+1)*(b-3)`
- `global_a=1`
- `a=sqrt(9)`
- `b=addDays(triggertime, 3)`
- `c=replace("hello automagic", "automagic", "world")`
- `b=addDays(triggertime, sqrt(9))`
- `b="Hello " + "World"`
- `a=true`
- `b=false`
- `c=a AND b OR c>=5`
- `c=NOT a AND NOT b`

#### String Inline Expressions

Inline expressions in strings can be used to replace a part of the string by a variable or expression. The rules described here also apply to the text fields of triggers, conditions and actions documented in the help page with Variables are supported.
An inline expression is enclosed in curly braces: `{expression}`

Example simple inline expressions:

- `var1="Test";
  var2="This is a {var1}";`
  'var2' will contain the string "This is a Test" after the script is evaluated
- `var="one plus two is {1 + 2}";`
  'var' is evaluated to "one plus two is 3"

Inline expressions can be formatted by defining a format type and depending on the format type a pattern to use: `{var,formattype,pattern}`

Example inline expressions with formatting:

- `var="Today is {getDate(),dateformat,dd.MM.yyyy}";`
  'var' will contain the string "Today is 21.07.2012"
- `var="It's {getDate(),dateformat,HH:mm}";`
  'var' will contain the string "It's 12:32"
- `var="It's {getDate(),dateformat,timezone,UTC,HH:mm}";`
  'var' will contain the string "It's 10:32"
- `var="Value: {1.456789,numberformat,0.00}";`
  'var' is evaluated to "Value: 1.46"
- `var="I'm here: {location,locationformat,decimal}";`
  'var' is evaluated to "I'm here: 46.76817,7.603751"
- `var="{files,listformat,comma}";`
  'var' is evaluated to "/mnt/sdcard/file1,/mnt/sdcard/file2"

Supported format types:

- `dateformat`: Formats the date using the specified date pattern. See [pattern characters](../reference/date-format-patterns.md) for a description of the supported patterns.
  The optional sub-format `timezone` along with the name of the timezone can be used to define the timezone used to format the date/time. Accepted timezone names are either UTC, GMT or the Olson name of a timezone name of the form *Area/Location*, such as `America/Los_Angeles` (device dependent). GMT is used for unknown timezone names.
  Examples:
  - `{triggertime,dateformat,timezone,UTC,HH:mm}`
  - `{triggertime,dateformat,timezone,America/Los_Angeles,HH:mm}`
  - `{triggertime,dateformat,timezone,Europe/London,HH:mm}`
  - `{triggertime,dateformat,timezone,Europe/Paris,HH:mm}`
  - `{triggertime,dateformat,timezone,Africa/Harare,HH:mm}`
- `numberformat`: Formats the number using the specified decimal format. See [pattern characters](../reference/number-format-patterns.md) for a description of the supported patterns.
- `locationformat`: Formats the address of the location when available in a single line of text when no format is specified. (Data connection is required)
  Following locationformat patterns are supported:
  - `multiline`: Formats the address as a multiline text. (Data connection is required)
  - `decimal`: Formats latitude,longitude as decimal numbers (+/-DDD.DDDDD). Example: 46.76817,7.603751.
  - `microdegrees`: Formats latitude,longitude multiplied by 1'000'000 as integers. Example: 46768355,7604022. This format can be useful in a call to a REST service.
  - `swiss`: Formats latitude,longitude converted to the [Swiss coordinate system](http://de.wikipedia.org/wiki/Schweizer_Landeskoordinaten).
- `listformat`: Formats the list of values as a multiline text with one item per line when no pattern is specified.
  Following listformat patterns are supported:
  - `comma`: Formats the list of values as a comma separated list.
  - `semicolon`: Formats the list of values as a semicolon separated list.
- `jsonformat`: Formats the value as JSON fragment.

Inline expressions in strings with single quotes are not interpreted. This can be helpful for regular expressions, where a quantifier like **{2}** in the pattern **([0-9]){2}.\*** should not be replaced with **2**.

Example:

- `var='Today is {getDate(),dateformat,dd.MM.yyyy}';`
  'var' is evaluated to 'Today is {getDate(),dateformat,dd.MM.yyyy}'

### Control Structures

#### `if` Statement

An if statement can be used to evaluate a block of code when a condition is true.
Example:
```
    if (a<3)
    {
        b = 0;
    }
    else
    {
        b = 1;
    }
```

In this example variable `b` is assigned the value zero when the variable `a` contains a value less than 3, `b` is assigned the value one when the variable `a` contains a value greater or equal to 3.

#### `for` Loop

A for loop evaluates a block of code for every value in a list of values.
Example:
```
    list=newList(1, 2, 3);

    for (a in list)
    {
        log("a contains {a}");
    }
```

This example would print the following output in the log:
```
    a contains 1
    a contains 2
    a contains 3
```

#### Numeric List Creation Expression

Since it is very common to create a list containing a sequence of numeric values there is a shorthand to create such a list using `[<number> to <number>, <step size>]`:
Examples:
```
    list = [1 to 10];//without the optional step size

    for (a in list)
    {
        log(a);
    }
    //logs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    //inlined
    for (a in [1 to 10])
    {
        log(a);
    }
    //logs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    //inlined with step size of 2
    for (a in [1 to 10, 2])
    {
        log(a);
    }
    //logs 1, 3, 5, 7, 9

    //inlined with negative step size of -3
    for (a in [10 to 1, -3])
    {
        log(a);
    }
    //logs 10, 7, 4, 1
```

#### Access to list and map entries

Single values of lists and maps can be accessed with brackets.
Examples:
```
    list = [1 to 10];
    a = list[0];//get first element of the list: 1
    a = list[1];//get second element of the list: 2

    list[2] = 999;//assigns 999 to the third element of the list

    map = newMap();
    map["key1"] = 1;//creates a map entry key1-->1
    map["key2"] = 2;//creates a map entry key2-->2

    a = map["key1"];//gets the value of entry with key1: 1
    a = map["key2"];//gets the value of entry with key2: 2
```

#### `while` Loop

A while-loop evaluates a block of code as long as a condition is true.
Example:
```
    a = 0;

    while (a < 10)
    {
        log(a);
        a = a + 1;
    }
    //logs 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

#### `return` statement

The return statement can be used to terminate a script early and optionally to return a given value.
Example:
```
    a = null;
    if (a == null)
    {
        return;
    }

    log("X");//not reached since return terminates the script
```

#### `break` statement

The break statement can be used to terminate a loop and to continue the script after the loop body.
Example:
```
    for (a in [1 to 10])
    {
        if (a == 4)
        {
            break;
        }
        log(a);
    }

    log("X");
    //logs 1, 2, 3, X
```

#### `continue` statement

The continue statement can be used to immediately continue with the next iteration of the loop.
Example:
```
    for (a in [1 to 10])
    {
        if (a == 4)
        {
            continue;
        }
        log(a);
    }

    log("X");
    //logs 1, 2, 3, 5, 6, 7, 8, 9, 10, X
```

### Functions

Built in functions can be called to calculate trigonometric values, create lists, extract values from an XML and much more.
Examples:
```
    a = sin(1.2);//evaluates to 0.932039...
    a = max(1, 2, 3, 4, 5);//evaluates to 5
    a = isEmpty([1 to 10]);//evaluates to false
    a = containsElement([1 to 10, 2], 3);//evaluates to true
```

Tip: Please also see the [Script examples](../reference/script-examples.md) page that shows some commonly used script snippets.

- `Object convertNull(Object value, Object defaultValue)`
  Returns the value of the first argument or returns `default` when the value is null.
- `Number abs(Number value)`
  Returns the absolute value of `value`.
- `Number pow(Number base, Number exponent)`
  Returns the value of the first argument raised to the power of the second argument.
- `Number sqrt(Number a)`
  Returns the square root of the number.
- `Number sin(Number a)`
  Returns the sine of the angle in radians.
- `Number cos(Number a)`
  Returns the cosine of the angle in radians.
- `Number tan(Number a)`
  Returns the tangent of the angle in radians.
- `Number asin(Number a)`
  Returns the sine of the angle in radians.
- `Number acos(Number a)`
  Returns the arc cosine of the angle in radians.
- `Number atan(Number a)`
  Returns the arc tangent of the angle in radians.
- `Number atan2(Number y, Number x)`
  Returns the angle of the polar representation of the rectangular coordinate (x, y).
- `Number sinh(Number a)`
  Returns the hyperbolic sine of the value.
- `Number cosh(Number a)`
  Returns the hyperbolic cosine of the value.
- `Number tanh(Number a)`
  Returns the hyperbolic tangent of the value.
- `Number log10(Number a)`
  Returns the base 10 logarithm of the value.
- `Number ln(Number a)`
  Returns the natural logarithm (base *e*) of the value.
- `Number toRadians(Number a)`
  Converts the Number from degrees to radians.
- `Number toDegrees(Number a)`
  Converts the Number from radians to degrees.
- `Number round(Number a)`
  Rounds the number to the nearest integer.
- `Number ceil(Number a)`
  Returns the next highest integer value by rounding up value if necessary.
- `Number floor(Number a)`
  Returns the next lowest integer value by rounding down value if necessary.
- `Date addDays(Date d, Number a)`
  Returns a new date by adding `a` number of days to the date `d`.
- `Date addHours(Date d, Number a)`
  Returns a new date by adding `a` number of hours to the date `d`.
- `Date addMinutes(Date d, Number a)`
  Returns a new Date by adding `a` number of minutes to the date `d`.
- `Date addSeconds(Date d, Number a)`
  Returns a new date by adding `a` number of seconds to the date `d`.
- `Date getDate()`
  Returns the current date and time.
- `Date getDate(String date, String pattern)`
  Converts the string to a date using the specified pattern. (see [pattern characters](../reference/date-format-patterns.md))
- `Date getDate(Number year, Number month, Number day)`
  Returns the Date specified by the arguments.
- `Date getDate(Number year, Number month, Number day, Number hours, Number minutes, Number seconds)`
  Returns the date specified by the arguments.
- `Date getDate(Date date, Number hours, Number minutes, Number seconds)`
  Returns the date specified by the arguments.
- `Date getDate(Date date, Number hours, Number minutes, Number seconds, String timezone)`
  Returns the date specified by the arguments in the defined timezone.
- `Number getUptimeMillis()`
  Returns milliseconds since boot, not counting time spent in deep sleep.
- `Number getElapsedRealtimeMillis()`
  Returns milliseconds since boot, including time spent in sleep.
- `Number getDurationMillis(String duration)`
  Returns the duration in milliseconds specified by the duration string (e.g. "2m 15s" returns 135000).
- `String getDurationString(Number duration)`
  Returns the duration string representing the specified milliseconds (e.g. 135000 returns "2m 15s").
- `Number getByteSize(String byteSize)`
  Returns the number of bytes specified by the string (e.g. "10kb 15b" returns 10255).
- `String getByteSizeString(Number byteSize)`
  Returns the formatted byte string representing the specified bytes (e.g. 10255 returns "10kb 15b").
- `Number toNumber(String number)`
  Converts the specified parameter to a number.
- `Number min(Number n1, Number n2, ...)`
  Returns the smallest number of the arguments.
- `Number max(Number n1, Number n2, ...)`
  Returns the largest number of the arguments.
- `Boolean isEmpty(String s)`
  Returns whether the string is empty or not.
- `Number length(String s)`
  Returns the number of characters in string `s`.
- `String substring(String s, Number start, Number end)`
  Returns the substring of the specified string.
- `String substring(String s, Number start)`
  Returns the substring starting at the specified index.
- `String left(String s, Number length)`
  Returns the first `length` characters of the specified string.
- `String right(String s, Number length)`
  Returns the last `length` characters of the specified string.
- `Number indexOf(String s, String search)`
  Returns the first index of `search` in `s`.
- `Number indexOf(String s, String search, Number start)`
  Returns the first index of `search` after `start` in `s`.
- `Number lastIndexOf(String s, String search)`
  Returns the last index of `search` in `s`.
- `Number lastIndexOf(String s, String search, Number start)`
  Returns the last index of `search` before `start` in `s`.
- `Boolean startsWith(String s, String prefix)`
  Checks whether the string `s` starts with `prefix`.
- `Boolean endsWith(String s, String suffix)`
  Checks whether the string `s` ends with `suffix`.
- `Boolean contains(String s, String search)`
  Checks whether the string `s` contains the substring `search`.
- `List split(String s, String pattern)`
  Splits the string `s` into a list of strings by using the regular expression `pattern` as the delimiter. (see [Regular expressions](../reference/regular-expressions.md))
- `List splitCSVRecord(String s)`
  Splits the comma delimited string `s` into a list of tokens. Takes double quotes for escaped fields into consideration.
- `List splitCSVRecords(String s)`
  Splits multiple lines of a comma delimited string `s` into a list (per line) of list of tokens. Takes double quotes for escaped fields into consideration.
- `String join(List list, String delimiter)`
  Joins the elements of the list into a string by separating the elements with the specified `delimiter`.
- `Boolean matches(String s, String pattern)`
  Returns whether the string `s` matches the regular expression `pattern`. (see [Regular expressions](../reference/regular-expressions.md))
- `Boolean matches(String s, String pattern, List groups)`
  Returns whether the string `s` matches the regular expression `pattern` and fills the captured groups into the existing list `groups`. (see [Regular expressions](../reference/regular-expressions.md))
- `List findAll(String s, String pattern)`
  Returns a list of all matched values in `s` of regex `pattern`. (see [Regular expressions](../reference/regular-expressions.md))
- `List findAll(String s, String pattern, boolean returnGroups)`
  Returns a list of all matched values in `s` of regex `pattern`. Optionally item consists of a list of the matched groups. (see [Regular expressions](../reference/regular-expressions.md))
- `String replace(String s, String search, String replace)`
  Returns a modified string by replacing all occurrences of `search` with `replace` in string `s`.
- `String replaceAll(String s, String regex, String replacement)`
  Returns a modified string by replacing all substrings matching `regex` with `replacement` in string `s`. (see [Regular expressions](../reference/regular-expressions.md))
- `String trim(String s)`
  Returns a modified string by removing all leading and trailing whitespace from string `s`.
- `String concat(Object o1, ...)`
  Returns the string concatenation of the specified objects.
- `String toUpperCase(String s)`
  Converts the string to upper case using the rules of the default locale.
- `String toLowerCase(String s)`
  Converts the string to lower case using the rules of the default locale.
- `String encodeURLForm(String urlPart)`
  URL-encodes the specified `urlPart` (for application/x-www-form-urlencoded, spaces are encoded as +).
- `String encodeURL(String urlPart)`
  URL-encodes the specified `urlPart` (spaces are encoded as %20).
- `String encodeHTML(String text)`
  HTML-encodes the specified `text`.
- `List newList(Object o1, ...)`
  Returns a new list containing the specified objects.
- `List copyList(List list)`
  Returns a copy of specified list (flat copy).
- `Number length(List list)`
  Returns the number of elements in `list`.
- `Boolean isEmpty(List list)`
  Returns whether the list contains any elements or not.
- `List addElement(List list, Object o1)`
  Returns the same list after adding the object at the end of the list. Returns a new list when the list should not exist yet.
- `List addElement(List list, Number index, Object o1)`
  Returns the same list after adding the object at the specified index (zero based).
- `List addAllElements(List list, List elementsToAdd)`
  Returns the same list after adding all elements specified in list `elementsToAdd`.
- `List removeDuplicateElements(List list)`
  Returns the same list after removing all duplicates.
- `List removeElementValue(List list, Object o1)`
  Returns the same list after removing all elements with the specified value.
- `List removeAllElementValues(List list, List elementsToRemove)`
  Returns the same list after removing all elements contained in the second list.
- `Boolean containsElement(List list, Object o1)`
  Returns `true` when the list contains the specified element.
- `Object removeElement(List list, Number index)`
  Removes the object at the specified index (zero based) and returns the removed object.
- `List removeElements(List list, Number fromIndex, Number toIndex)`
  Removes the objects at the specified index range (zero based, [fromIndex,toIndex[) and returns the removed objects in a list.
- `Object getElement(List list, Number index)`
  Returns the object at the specified index (zero based).
- `List setElement(List list, Number index, Object value)`
  Sets the object at the specified index (zero based).
- `Object getRandomElement(List list)`
  Returns a random element of the list.
- `List shuffleList(List list)`
  Randomly shuffles the elements of the list.
- `Number indexOfElement(List list, Object value)`
  Returns the first index of the element in the list or -1 when the element is not contained in the list.
- `Number indexOfElement(List list, Object value, Number start)`
  Returns the first index of the element in the list that is bigger or equal to `start` or -1 when the element is not contained in the list.
- `List sort(List list, Boolean casesensitive, Boolean natural)`
  Modifies the list by sorting the values.
- `List reverse(List list)`
  Modifies the list by reversing the order of the contained values.
- `Map newMap()`
  Returns a new empty map
- `Map newMapFromValues(String key1, Object value1, ...)`
  Returns a new map initialized to contain the specified keys and values.
- `Boolean isEmpty(Map map)`
  Returns whether the map contains any elements or not.
- `Number length(Map map)`
  Returns the number of elements in `map`.
- `Map copyMap(Map map)`
  Returns a copy of specified map (flat copy).
- `Map addMapEntry(Map map, String key, Object value)`
  Adds a new entry `key->value` to the map and returns the map. Returns a new map when the map should not exist yet.
- `Map addAllMapEntries(Map map, Map entriesToAdd)`
  Adds all entries of the second map to the first map and returns the first map.
- `Object getMapValue(Map map, String key)`
  Returns the object for `key` or `null` when no mapping for key exists.
- `Object getMapValue(Map map, String key, Object default)`
  Returns the object for `key` or `default` when no mapping for key exists or `map` is null.
- `Object removeMapEntry(Map map, String key)`
  Removes the entry for the given `key` and returns the value.
- `List getMapKeys(Map map)`
  Returns a list of the keys of `map`.
- `List getMapValues(Map map)`
  Returns a list of the values of `map`.
- `String evaluateXPathAsString(String xml, String xpath)`
  Evaluates the XPath expression on the given XML and returns the result as a string. (see [XPath Specification](http://www.w3.org/TR/xpath/))
- `String hash(String value, String encoding, String algorithm)`
  Calculates the hash of `value` using the specified `encoding` (like `UTF-8` or `UTF-16LE`) and hashing `algorithm` (like `MD5` or `SHA1`).
- `String toJSON(Object value)`
  Converts the specified object to a JSON string.
- `String toJSON(Object value, Boolean indent)`
  Converts the specified object to a JSON string, indented or not.
- `Object fromJSON(String value)`
  Converts the specified JSON string into an object.
- `Object log(Object value)`
  Logs the specified object in the Automagic log and returns the unmodified object.
- `Object eval(String script)`
  Evaluates the string as a script and returns the value of the last expression.
- `Number random()`
  Returns a random number between 0.0 and 1.0 (exclusive).
- `Number random(Number low, Number high)`
  Returns a random number between `low` and `high` (inclusive).
- `Boolean sleep(Number milliseconds)`
  Waits for the specified amount of `milliseconds`.
- `Boolean sleep(String duration)`
  Waits for the specified `duration` like "2m 30s".
- `Boolean existsFile(String path)`
  Checks whether the file denoted by `path` exists or not.
- `Boolean isDirectory(String path)`
  Checks whether the file denoted by `path` is a directory.
- `String getExternalStorageDir()`
  Returns the path to the primary external storage directory.
- `Number getPixelColor(Bitmap image_data, Number x, Number y)`
  Returns the color (argb) of the pixel of the `image` at location `x`, `y`.
- `Number getRed(Number color)`
  Returns the red component of the specified `color`.
- `Number getGreen(Number color)`
  Returns the green component of the specified `color`.
- `Number getBlue(Number color)`
  Returns the blue component of the specified `color`.
- `Number getAlpha(Number color)`
  Returns the alpha component of the specified `color`.
- `Number newColor(Number a, Number r, Number g, Number b)`
  Returns a new color from the specified ARGB components.
- `Number distance(Location loc1, Location loc2)`
  Calculates the distance between locations `loc1` and `loc2` in meters.
- `Location newLocation(Number latitude, Number longitude)`
  Creates a new Location for the specified `latitude` and `longitude`.
- `String setHTTPResponseHeader(String header, String value)`
  Sets the HTTP response header to the specified value and returns the value.
- `Number setHTTPResponseStatus(Number status)`
  Sets the HTTP response status to the specified value and returns the value.
- `Boolean isList(Object value)`
  Returns whether the specified value is a List or not.
- `Boolean isMap(Object value)`
  Returns whether the specified value is a Map or not.
- `Boolean isString(Object value)`
  Returns whether the specified value is a String or not.
- `Boolean isNumber(Object value)`
  Returns whether the specified value is a Number or not.
- `Boolean isBoolean(Object value)`
  Returns whether the specified value is a Boolean or not.
- `Boolean isLocation(Object value)`
  Returns whether the specified value is a Location or not.
- `Object getWidgetElementProperty(String widgetName, String elementName, String property)`
  Gets the current value of the property of the specified widget element.
- `Object setWidgetElementProperty(String widgetName, String elementName, String property, Object value)`
  Sets the given property of the specified widget element to `value`.
- `Boolean refreshWidget(String widgetName, Boolean reloadImages)`
  Refreshes the widget and optionally also reloads images.
- `String getAppName(String packageName)`
  Returns the display name of the app from the specified package or null when not available.
- `String getActivityName(String packageName, String className)`
  Returns the display name of the activity from the specified package and class or null when not available.
- `String getServiceName(String packageName, String className)`
  Returns the display name of the service from the specified package and class or null when not available.
- `List getFlowNames()`
  Returns a list containing the names of all flows.
- `List getFlowNamesByGroup(String group)`
  Returns a list containing the names of the flows of the specified `group`.
- `List getFlowGroupNames()`
  Returns a list containing the names of the flow groups.
- `List getWidgetNames()`
  Returns a list containing the names of all widgets.
- `Map getFlowStatisticsDuration()`
  Returns a map of the executed flows. Key=Flow name, Value=total execution duration in milliseconds, sorted by value descending.
- `Map getFlowStatisticsCount()`
  Returns a map of the executed flows. Key=Flow name, Value=total execution count, sorted by value descending.
- `Boolean resetFlowStatistics()`
  Resets the flow statistics.
- `Object getValue(String name, Object default)`
  Returns the value of the variable named `name` or returns `default` when the variable is undefined or null.
- `Object setValue(String name, Object value)`
  Sets the variable named `name` to `value` and returns `value`
- `Object removeVariable(String name)`
  Removes the variable named `name`.
- `List getVariableNames()`
  Returns a list of all variables currently available (local and global).
- `Number getAndroidSDKVersion()`
  Returns the SDK version number of the Android framework. (see [Android API versions](https://source.android.com/source/build-numbers.html#platform-code-names-versions-api-levels-and-ndk-releases))
- `Object getContext()`
  Returns the context of the application.
- `Object callJavaStaticMethod(String className, String methodSignature, Object params, ...)`
  Calls the defined public static method of the defined class.
- `Object callJavaConstructor(String className, String constructorSignature, Object params, ...)`
  Calls the public constructor of the defined class.
- `Object callJavaMethod(Object obj, String className, String methodSignature, Object params, ...)`
  Calls the specified instance method on the defined object.
- `Object getJavaStaticField(String className, String fieldName)`
  Returns the value of the specified public static field.
- `Object setJavaStaticField(String className, String fieldName, Object value)`
  Sets the value of the specified public static field.
- `Object getJavaField(Object obj, String className, String fieldName)`
  Returns the value of the specified public instance field.
- `Object setJavaField(Object obj, String className, String fieldName, Object value)`
  Sets the value of the specified public instance field.

Note: Are you missing a function? Please let us know in the forum.

### Advanced Topics

Every executable expression in a script evaluates to a value. A block of code evaluates to the value produced by the last expression in the block and allows to create inline scripts with multiple expressions:
```
    s = "{a=1;b=2}";
    log(s);//logs 2

    a = true;
    b = if (a) 1 else 2;
    log(b);//logs 1

    for (a in [0 to 10])
    {
        log(if(a<5) "X" else "-");
    }
    //logs X, X, X, X, X, -, -, -, -, -, -

    b=0;
    log(for(a in [1 to 10]) {b=b+a});
    //logs 55
```

---

### [Seek Action Sound](actions/action_seek_action_sound.md)

The action **Seek Action Sound** seeks in the currently executing action **Sound**.

Examples:

- Seek to the beginning of a song.

#### Settings

##### Seek Type

Whether to seek to a specific absolute position or to fast forward/backward the specified duration.

##### Position

The position respectively the duration to seek. [Variables are supported.](#string-inline-expressions)

---

### [Send Broadcast](actions/action_send_broadcast.md)

The action **Send Broadcast** send a broadcast using the specified intent. Please also see the [documentation of the Android Intent class](http://developer.android.com/reference/android/content/Intent.html).

Tip: Some broadcast receivers require special permissions to be launched. Check the log after testing the action when the broadcast receiver fails.

Examples:

- Control an app that exposes its actions using a broadcast receiver.

#### Settings

##### Action

The action to use in the intent. [Variables are supported.](#string-inline-expressions)

##### Category List

The list of categories as a comma separated list to add to the intent. [Variables are supported.](#string-inline-expressions)

##### Data URI

The data URI to set on the intent. [Variables are supported.](#string-inline-expressions)

##### Mime Type

The mime type to set on the intent. [Variables are supported.](#string-inline-expressions)

##### Package Name

The specific package to launch. [Variables are supported.](#string-inline-expressions)

##### Class Name

The specific class to launch. [Variables are supported.](#string-inline-expressions)

##### Flag List

The flags to add to the intent.

##### Extras

A script used to add an unlimited number of extras to the intent.

Additionally to the regular built in functions of Automagic also the following functions are available to add the extras to the intent:

- `putString(key, value)`
- `putBoolean(key, value)`
- `putFloat(key, value)`
- `putDouble(key, value)`
- `putByte(key, value)`
- `putShort(key, value)`
- `putChar(key, value)`
- `putInt(key, value)`
- `putLong(key, value)`
- `putUri(key, value)`
- `putBooleanArray(key, value)`
- `putByteArray(key, value)`
- `putIntArray(key, value)`
- `putIntegerArrayList(key, value)`
- `putLongArray(key, value)`
- `putFloatArray(key, value)`
- `putDoubleArray(key, value)`
- `putShortArray(key, value)`
- `putCharArray(key, value)`
- `putStringArray(key, value)`
- `putStringArrayList(key, value)`
- `putUriArray(key, value)`
- `putUriArrayList(key, value)`

Example:
```
putString("key1", "Hello");
putBoolean("key2", true);
putDouble("key3", 1.23);
putInt("key4", 42);
putInt("key5", a+4*b);
```

[See action Script for a description of the scripting language.](#scan-barcode)

##### Send ordered broadcast

Whether Automagic should send an ordered broadcast which allows a broadcast receiver to provide a result to Automagic.

##### Access Result Extras

Script to access the returned extras.
Following functions are supported:

- `getString(String key)`
- `getChar(String key, String defaultValue)`
- `getBoolean(String key, Boolean defaultValue)`
- `getFloat(String key, Number defaultValue)`
- `getDouble(String key, Number defaultValue)`
- `getByte(String key, Number defaultValue)`
- `getShort(String key, Number defaultValue)`
- `getInt(String key, Number defaultValue)`
- `getLong(String key, Number defaultValue)`
- `getBundle(String key)`
- `getUri(String key)`
- `getBooleanArray(String key)`
- `getByteArray(String key)`
- `getShortArray(String key)`
- `getCharArray(String key)`
- `getIntArray(String key)`
- `getIntegerArrayList(String key)`
- `getLongArray(String key)`
- `getFloatArray(String key)`
- `getDoubleArray(String key)`
- `getStringArray(String key)`
- `getUriArray(String key)`
- `getUriArrayList(String key)`
- `getParcelableAsString(String key)`
- `getParcelableArrayAsString(String key)`
- `getParcelableArrayListAsString(String key)`
- `getParcelable(String key)`

[See action Script for a description of the scripting language.](#scan-barcode)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `result_code` — the returned result code
- `operation` — string "ok", when result\_code was -1, "cancel" otherwise
- `data_string` — the data of the received intent as a string
- `abort_broadcast` — boolean flag indicating whether or not the broadcast receiver aborted the broadcast.

---

### [Send SMS](actions/action_send_sms.md)

The action **Send SMS** sends an SMS to the specified phone number.

Examples:

- Send an SMS with your location as a response to an SMS containing the text **Where are you?**.
- Send an SMS to your partner when you are on your way home.

#### Settings

##### SIM

The SIM card.

##### To

The number to send the SMS to. [Variables are supported.](#string-inline-expressions)

Example:

- use `{sms_sender}` to fill in the phone number received in an **SMS Received** trigger.

##### Message

The message to send. [Variables are supported.](#string-inline-expressions)

Example:

- use `{location,locationformat}` to fill in a nearby address of the location. The location can be determined using an action **Init Variable Location**.

##### Truncate

Whether to truncate the message text to fit within one SMS or to send the message using multiple SMS parts.

##### SMS Sending Limit

Defines how many SMS can be sent within the given amount of time. The action interrupts the flow with an error when the limit is exceeded.

##### Store sent SMS

Whether to store the sent SMS in the sent messages of the devices messaging app or not. This function is not officially supported by Android and might not work on all devices. Android 4.4+ automatically stores all sent SMS.

##### Delivery Report Options

Whether to request a delivery report and whether the report should be synchronous which blocks the action until the report is received or the timeout elapsed or to asynchronously deliver the report to trigger *Automagic SMS Deliver Report Received*.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `sms_delivery_report_status` — the status code (0-31=OK, 32-63=delivery pending, >64=error)

---

### [Send USSD Request](actions/action_send_ussd_request.md)

The action **Send USSD Request** sends a USSD request to the provider.

Warning: Some versions of Android don't properly handle USSD request failures so a dialog of the system might be shown when a USSD request fails which causes the action to timeout after 30 seconds.

Examples:

- Query the prepaid balance.

#### Settings

##### SIM

The SIM card.

##### USSD Request

The request to send. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `ussd_failure_code` —
- `ussd_response` — the response text

---

### [Send Wake on LAN Packet](actions/action_send_wake_on_lan_packet.md)

The action **Send Wake on LAN Packet** sends a Wake on LAN packet using UDP to the specified IP address and port.

Examples:

- Start your NAS (Network Attached Storage) daily at 6am.

#### Settings

##### MAC Address

The MAC address to send the packet data. [Variables are supported.](#string-inline-expressions)

##### IP/Port

The IP address to send the packet to. [Variables are supported.](#string-inline-expressions)

---

### [Set Airplane Mode](actions/action_set_airplane_mode.md)

The action **Set Airplane Mode** sets the airplane mode of the phone on or off.

Warning: This function requires root access starting with Android 4.2 and is not officially supported by Android.

Examples:

- Reduce radiation at night by turning on the airplane mode.
- Turn on airplane mode to reduce battery usage when battery level is below 20%.

#### Settings

##### Method

The method used to toggle the airplane mode. It highly depends on device which method works better.

##### Turn Airplane Mode On/Off

Whether to turn airplane mode on or off.

---

### [Set Alarm](actions/action_set_alarm.md)

The action **Set Alarm** creates an alarm in the alarm app available on the device.

Warning: Not all alarm apps support all options.

#### Settings

##### Label

The label to use in the alarm. Not supported by all alarm apps. [Variables are supported.](#string-inline-expressions)

##### Hour (0–23)

The hour to use in the alarm. [Variables are supported.](#string-inline-expressions)

##### Minutes (0–59)

The minutes to use in the alarm. [Variables are supported.](#string-inline-expressions)

##### Alarm

The alarm to play. Not supported by all alarm apps. [Variables are supported.](#string-inline-expressions)

##### Vibrate

Whether or not the device should vibrate. Not supported by all alarm apps.

##### Skip UI

Whether or not the alarm app should be displayed after setting the alarm. Not supported by all alarm apps.

---

### [Set App Notification Peekable](actions/action_set_app_notification_peekable.md)

The action **Set App Notification Peekable** changes the setting whether app notifications of an app can be emphasized by sliding briefly into view.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Turn the peekable setting off for some apps when watching a movie.

#### Settings

##### Package Name

The name of the package to change the notification peekable setting. [Variables are supported.](#string-inline-expressions)

---

### [Set App Notification Priority](actions/action_set_app_notification_priority.md)

The action **Set App Notification Priority** changes the setting whether app notifications are important or not for a particular app.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Change the priority of mail notifications to unimportant at night.

#### Settings

##### Package Name

The name of the package to change the setting. [Variables are supported.](#string-inline-expressions)

---

### [Set App Notification State](actions/action_set_app_notification_state.md)

The action **Set App Notification State** enables or disables the capability of an app to post notifications.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Prevent that an incoming call displays a notification when the device is surveyed in the background.

#### Settings

##### Package Name

The name of the package to turn notifications on or off. [Variables are supported.](#string-inline-expressions)

---

### [Set Audio Manager Mode](actions/action_set_audio_manager_mode.md)

The action **Set Audio Manager Mode** changes the mode of the audio manager to either **Normal**, **Ringtone** or **In call**.
The audio mode encompasses audio routing AND the behavior of the telephony layer.

#### Settings

##### Audio Manager Mode

The mode to set.

---

### [Set Audio Stream Volume](actions/action_set_audio_stream_volume.md)

The action **Set Audio Stream Volume** changes the volume of a audio stream of a specific type.

Examples:

- Reduce ringer volume when you are in your office.
- Increase music volume when you plug in the earphones.

#### Settings

##### Sound Type

The type of the audio stream to adjust.

##### Change Type

Whether to set an absolute value, to raise, lower mute or unmute the volume. Keep same can be used to just show the volume level popup.

##### Volume

The volume level to use. The maximum level differs for the different audio streams. [Variables are supported.](#string-inline-expressions)

##### Play Sound

Whether to play the short volume adjustment sound when the action is executed. Some devices never play a sound when the volume is changed.

##### Show Volume Level Popup

Whether to show a popup indicating the new volume level.

---

### [Set Auto Sync State](actions/action_set_auto_sync_state.md)

The action **Set Auto Sync State** turns the automatic synchronisation on or off.

Examples:

- Turn the automatic synchronisation off at night.
- Turn off the automatic synchronisation of the company account on weekends.

#### Settings

##### Auto Sync

Whether to turn auto sync on or off.

##### Global or Specific

Whether to change the auto sync globally or only for a the specified accounts/authorities. Changing the global switch does not change the settings of the individual accounts/authorities.

##### Accounts

The accounts to change in format *Type*:*Name*.
Glob patterns can be used to match multiple accounts. [Variables are supported.](#string-inline-expressions)

- `*` changes all accounts
- `Google:*` changes all Google accounts

##### Authorities

The parts/databases of the accounts to change. Specify a `*` to change all parts of the account.
Glob patterns can be used to match multiple authorities. [Variables are supported.](#string-inline-expressions)

- `*` changes all authorities of the specified accounts
- `com.android.calendar` changes all calendars of the specified accounts

---

### [Set Accelerometer Rotation](actions/action_set_auto_rotate_screen_state.md)

The action **Set Accelerometer Rotation** turns on or off the **Auto-rotate screen** setting.

Note: An application can request to use the accelerometer for screen orientation changes, even when this setting is turned off.

#### Settings

##### Auto-rotate screen

Whether the system should automatically rotate the screen depending on the orientation of the device or not.

---

### [Set Battery Saver Mode](actions/action_set_power_save_mode.md)

The action **Set Battery Saver Mode** turns on the battery saver mode of the device (Android 5+). Battery saver mode can not be enabled when the device is charging.

Warning: This function does not work for manufacturer specific battery saving modes like Samsungs (Ultra-)energy saving mode or Sony and HTC specific modes. Please use action **Set System Setting** on such devices.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Turn on the battery saver at night when no charging adapter is available.

#### Settings

##### Battery Saver

Whether to turn the battery saver mode on or off.

---

### [Set Bluetooth SCO State](actions/action_set_bluetooth_sco_state.md)

The action **Set Bluetooth SCO State** turns Bluetooth SCO for communications on or off.

Examples:

- Turn Bluetooth SCO off even when a headset is connected.

#### Settings

##### Bluetooth SCO

Whether to turn Bluetooth SCO on or off.

Check **Start Bluetooth SCO** to route the audio to the bluetooth device or **Stop Bluetooth SCO** to stop routing the audio to your bluetooth device when it was previously started with Automagic.

Note: Starting/stopping Bluetooth SCO is not supported on all devices and is known to be buggy on some devices.

---

### [Set Bluetooth State](actions/action_set_bluetooth_state.md)

The action **Set Bluetooth State** turns Bluetooth globally on or off.

Examples:

- Turn Bluetooth on when the phone is connected to a power source.
- Turn Bluetooth off when the battery level is below 30%.

#### Settings

##### Bluetooth

Whether to turn Bluetooth on or off.

---

### [Set Bluetooth Tethering State](actions/action_set_bluetooth_tethering_state.md)

The action **Set Bluetooth Tethering State** turns Bluetooth tethering setting on or off.

Note: This action does not supply the Bluetooth tethering feature by itself, it only turns on the setting. Some providers remove the Bluetooth tethering feature. This action can **not** turn on tethering on such a phone.

Warning: This function is not officially supported by Android and might not work on all devices.

Warning: This function requires Android 3+.

#### Settings

##### Bluetooth Tethering

Whether to turn Bluetooth tethering on or off.

---

### [Set Camera Usage State](actions/action_set_camera_usage_state.md)

The action **Set Camera Usage State** allows or denies the camera usage for apps.

Examples:

- Avoid that an app can use the camera for privacy reasons.

#### Settings

##### Camera usage

Whether apps should be allowed to use the cameras.

---

### [Set Car UI Mode](actions/action_set_car_ui_mode.md)

The action **Set Car UI Mode** puts the device into car UI mode.

Note: Not supported by all devices.

Examples:

- Launch the car dock UI mode of an app when you don't actually own the car dock.

#### Settings

##### Car UI Mode

Whether to turn the car UI mode on or off.

##### Launch Dock/Home

Whether or not to start the dock/home screen when available on this device.

---

### [Set Cyanogen/LineageOS Profile](actions/action_set_cyanogen_mod_profile.md)

The action **Set Cyanogen/LineageOS Profile** changes the currently set Cyanogen/LineageOS profile.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Change the profile to 'at home' when the WiFi is connected.

#### Settings

##### Profile Name

The name of the profile to activate. [Variables are supported.](#string-inline-expressions)

---

### [Set Data Roaming State](actions/action_set_data_roaming_state.md)

The action **Set Data Roaming State** turns the global data roaming setting on or off.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Example:

- Activate data roaming abroad every morning for 10 minutes to synchronize the mails and deactivate data roaming again for the rest of the day.

#### Settings

##### Data Roaming

Whether to turn data roaming on or off.

---

### [Set Default Input Method](actions/action_set_default_input_method.md)

The action **Set Default Input Method** changes the current input method/keyboard.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Use Hacker's Keyboard in landscape mode and otherwise the default keyboard.

#### Settings

##### Input Method

The keyboard to use.

---

### [Set Ringtone](actions/action_set_default_ringtone.md)

The action **Set Ringtone** sets the default ringtone of the specified type (ringtone, alarm or notification).

Examples:

- Use a different ringtone at home.

#### Settings

##### Type

The type of ringtone to set.

##### Select Sound

To select the sound of the category above.

---

### [Set Disabled Keyguard Features](actions/action_set_disabled_keyguard_features.md)

The action **Set Disabled Keyguard Features** asks the system to disable the specified list of features on the lock screen (usually only affects secure lock screens like PIN, password lock screen).

Note: Other active device administrators might also disable some features. Automagic has no possibility to remove restrictions imposed by other device administrators.

Examples:

- Disable notifications on the lock screen when not at home.

#### Settings

##### Features to disable

The features that should be disabled.

---

### [Set Flow State](actions/action_set_flow_state.md)

The action **Set Flow State** enables or disables one or many flows.

Examples:

- Disable all flows using networking features when you are roaming.
- Disable all time tracking flows on Saturday and Sunday.

#### Settings

##### Flow pattern list

A comma separated list of flow names to enable or disable. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](#string-inline-expressions)

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*time tracking*`

##### Exclude flow pattern list

A comma separated list of flow names to **not** affect even when the field **Flow pattern list** includes the flow. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](#string-inline-expressions)

##### Enable or disable flows

Whether to enable or disable the flows.

---

### [Set GPS State](actions/action_set_gps_state.md)

The action **Set GPS State** turns GPS globally on or off.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Turn GPS on when Google Maps is started.

#### Settings

##### GPS

Whether to turn GPS on or off.

---

### [Set Immersive Mode](actions/action_set_immersive_mode.md)

The action **Set Immersive Mode** forces immersive/fullscreen mode.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play a game in immersive mode even when the game itself does not yet allow to select this mode.

#### Settings

##### Immersive Mode

The mode to force:

- **Reset to default**: Resets to the device default so the device can use the default mode
- **Without navigation**: Force fullscreen/immersive mode with navigation buttons hidden
- **With navigation**: Force fullscreen/immersive mode with navigation buttons shown

##### Show status bar notification to reset

Shows a lock icon in the statusbar to indicate that an immersive mode is enforced. Selecting the notification resets to the default value and is the same as executing this action with *Reset to default*

---

### [Set Interruptions Mode](actions/action_set_interruptions_mode.md)

The action **Set Interruptions Mode** changes the mode whether alarms and notifications are allowed to interrupt you.

Examples:

- Turn off interruptions at night.

#### Settings

##### Method

The method used to toggle the interruptions mode.

##### Interruptions Mode

The new mode to use.

---

### [Set Keyguard State](actions/action_set_keyguard_state.md)

The action **Set Keyguard State** globally disables or reenables the keyguard after it was disabled by this action.

Warning: The device keyguard will not turn on even when locking the device using the power button when the keyguard is disabled using this action (device specific).

Warning: The official API will be removed in a future release of Android and this action will stop working depending on Android version and device manufacturer.

Examples:

- Disable the keyguard when the shopping list is started from the background in a specific location.
- Reenable the keyguard when the shopping list app is stopped.

#### Settings

##### Keyguard

Whether to disable or reenable the keyguard when it was previously disabled by this action.

---

### [Set LineageOS System Setting](actions/action_set_lineage_system_setting.md)

The action **Set LineageOS System Setting** stores the specified value in the settings database of the system.

Warning: Modifying system settings to unsupported values can possibly harm your device or crash the system. Use at your own risk!

Note: Changes to some settings are not immediately picked up by the system but require an additional event to occur like turning the screen off and back on. Some settings need to be changed by special APIs, changing the value of such settings in the settings database are ignored by the system.

Note: `adb` can be used on some versions of Android to grant the permissions to modify settings from category **secure** and **global** without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic lineageos.permission.WRITE_SECURE_SETTINGS`

Examples:

- Change the value of a ROM specific setting not available in a regular action in Automagic.

#### Settings

##### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global settings valid for all users of the device

##### Name

The name of the setting to modify. [Variables are supported.](#string-inline-expressions)

##### Value

The value to store in the system settings database. [Variables are supported.](#string-inline-expressions)

---

### [Set Live Wallpaper](actions/action_set_live_wallpaper.md)

The action **Set Live Wallpaper** changes the wallpaper of the phone to the defined live wallpaper.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Change the wallpaper at home.
- Change the wallpaper when an SMS is received.

#### Settings

##### Live Wallpaper

The componentname of the live wallpaper to set. [Variables are supported.](#string-inline-expressions)

---

### [Set Lock Pattern State](actions/action_set_lock_pattern_state.md)

The action **Set Lock Pattern State** enables or disables the system setting whether the lock pattern should be used as the screen lock.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Example:

- Deactivate the pattern lock at home

#### Settings

##### Lock Pattern

Whether to enable or disable the lock pattern.

##### Method

- **Secure setting**: Changes the setting in the regular settings database of Android (Android 4.2 and below)
- **Database**: Directly accesses the database containing the lock settings (Android 4.3+)
- **Service**: Asks the system service to change the setting (Android 4.3+)

---

### [Set Lock PIN/Password](actions/action_set_lock_password.md)

The action **Set Lock PIN/Password** sets the PIN/Password of the screen lock or resets the screen lock.

The action can be used to deactivate the screen lock:

1. Important: Set the screen lock in the settings of Android to 'None'
2. activate the desired PIN/Password screen lock in the settings of Android
3. use the option 'Clear PIN/Password' in the action to disable the screen lock

Note: The procedure might not work on all Android versions. The screen lock will not be dismissed when the lock screen is currently showing on screen.

Starting with Android 7, you can only use the action to set the PIN/Password when no PIN/Password is set yet so you can no longer use the action to remove a PIN/Password, except when Automagic is set as the [device owner](../reference/device-owner.md).

Examples:

- Deactivate the screen lock when you are connected to the WiFi at home.

#### Settings

##### Clear or Set PIN/Password

Whether to set a PIN/Password or to clear the PIN/Password.

##### PIN or Password

Whether you want to set a PIN or a Password.

##### Manual or from Variable

Whether the PIN/password is defined within the action itself or whether the action should set the PIN/password contained in a variable at the time when the action is executed.

##### PIN

The PIN to set.

##### Password

The password to set.

##### Variable

The name of the variable containing the PIN/Password to use (at the time the action is executed).

---

### [Set Microphone Mute](actions/action_set_microphone_mute.md)

The action **Set Microphone Mute** mutes or unmutes the microphone of the phone.

Examples:

- Mute the microphone when the device screen is facing down.

#### Settings

##### Mute Microphone

Whether to mute or unmute the microphone.

---

### [Set Mobile Datanetwork State](actions/action_set_mobile_datanetwork_state.md)

The action **Set Mobile Datanetwork State** turns the mobile datanetwork on or off.

Warning: This function is not officially supported by Android and might not work on all devices.

Warning: This function requires root access on some devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Turn the mobile datanetwork off at night.

#### Settings

##### Mobile Datanetwork

Whether to turn mobile datanetwork on or off.

---

### [Set Mobile Network Mode (2G/3G)](actions/action_set_mobile_network_mode.md)

The action **Set Mobile Network Mode (2G/3G)** changes the network mode of the phone.

Warning: This function is not officially supported by Android and might not work on all devices.

#### Settings

##### Mobile Network Mode

The network mode to use. Strikethrough values are most likely not supported by the device.

---

### [Set Network Location State](actions/action_set_network_location_state.md)

The action **Set Network Location State** changes the setting whether the system can use WiFi access points and the mobile network to determine your location.

Note: Android shows a confirmation dialog on some devices.
Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Turn on the network location when Google Maps is started.

#### Settings

##### Network Location

Whether the network location provider can be used to determine the location.

---

### [Set NFC State](actions/action_set_nfc_state.md)

The action **Set NFC State** turns NFC globally on or off.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Turn NFC on when entering the office to scan NFC tags.

#### Settings

##### NFC

Whether to turn NFC on or off.

---

### [Set Night Mode](actions/action_set_night_mode.md)

The action **Set Night Mode** turns the night mode of the device on or off or activates the automatic switch based on time and location. Changes to the night mode are only effective when the car or desk mode is enabled on a device.
Note: Not supported by all devices.

Examples:

- Activate the night mode of the device at 10pm and turn back to normal mode at 6am.

#### Settings

##### Night Mode

Whether to turn night mode on, off or let the device handle the mode switching based on time and location.

---

### [Set Proximity Screen Off State](actions/action_set_proximity_screen_off_state.md)

The action **Set Proximity Screen Off State** turns on the function of Android that turns the display off, when the proximity sensor detects an object.

Warning: This function is not officially supported by Android <4.4 and might not work on all devices.

Examples:

- Turn the display for a VoIP-app off, whenever the device is held to the head.

#### Settings

##### Proximity Screen Off

Whether to turn the feature on or off.

##### Show notification to reset

Whether to show a notification to reset or not.

---

### [Set Restrict Background Data State](actions/action_set_restrict_background_data_state.md)

The action **Set Restrict Background Data State**

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Restrict background data at night to reduce data transfer.

#### Settings

##### Restrict background data

Whether to restrict background data or not.

---

### [Set Ringer Mode](actions/action_set_ringer_mode.md)

The action **Set Ringer Mode** changes the ringer to either **Normal**, **Silent** or **Vibrate** mode.

Note for Android 5+: The real silent mode has been removed by Google on Android 5. Activating silent mode instead switches the device interruption mode to **Priority interruptions only**. Please use action **Set Interruptions Mode** to switch between all three interruption modes.

Note for Android 6+: Google introduced a new mode called **Alarms only**. Activating silent mode now switches the device interruption/do not disturb mode to **Alarms only**. Please use action **Set Interruptions Mode** to switch between all four interruption modes.

Examples:

- Turn your phone to vibrate in your office.
- Turn your phone to normal mode when plugged in to a power adapter.
- Turn your phone to normal and maximise the ringer volume when you get an SMS containing the text **Phone Lost!**

#### Settings

##### Ringer Mode

The ringer mode to set.

---

### [Set Screen Brightness](actions/action_set_screen_brightness.md)

The action **Set Screen Brightness** changes the screen brightness.

Examples:

- Turn down the screen brightness when the battery is below 50%.
- Turn the screen brightness to maximum when the power adapter is connected.

#### Settings

##### Automatic brightness

Whether to use automatic brightness or the value specified using the slider. [Variables are supported.](#string-inline-expressions)

##### Adaptive brightness

Whether adaptive brightness should be changed to the defined value. [Variables are supported.](#string-inline-expressions)

Warning: This function is not officially supported by Android and might not work on all devices.

##### Force update

Whether it should be ensured that the system applies the new values immediately. Otherwise the changes might take effect when the screen is turned on the next time on some versions of Android. Disabling this option can avoid flickering on some devices.

---

### [Set Screen Orientation](actions/action_set_screen_orientation.md)

The action **Set Screen Orientation** forces the device to use the specified screen orientation setting. It can be used to force the screen to always use landscape mode or to use the sensor to enable reverse portrait and reverse landscape orientations.

Warning: This function is not officially supported by Android and might not work on all devices. Some apps like launchers or games might crash when the screen can not be changed to the rotation required by the app.

Examples:

- Force the device to use landscape mode even for the launcher.

#### Settings

##### Screen Orientation

The orientation setting to force:

- **Reset to default**: Reset to device default so the orientation is determined by the system
- **Landscape**: Force landscape
- **Portrait**: Force portrait
- **Sensor**: Force the use of the sensor detected orientation, even when an app requests landscape only
- **Don't use sensor**: Don't allow the use of the sensor to determine the orientation
- **Sensor Landscape**: Landscape or reverse landscape as determined by the sensor (from Android 2.3)
- **Sensor Portrait**: Portrait or reverse portrait as determined by the sensor (from Android 2.3)
- **Reverse Landscape**: Force reverse landscape (from Android 2.3)
- **Reverse Portrait**: Force reverse portrait (from Android 2.3)
- **Sensor all orientations**: All four possible orientations as determined by the sensor (from Android 2.3)

##### Show status bar notification to reset

Shows a lock icon in the statusbar to indicate that an orientation setting is enforced. Selecting the notification resets to the default value and is the same as executing this action with *Reset to default*

---

### [Set Screen Timeout](actions/action_set_screen_timeout.md)

The action **Set Screen Timeout** changes the screen timeout.

Examples:

- Raise the screen timeout to **10 Minutes** when the browser is started.
- Lower the screen timeout to **15 Seconds** when the battery is almost empty.

#### Settings

##### Screen Timeout

The new screen timeout to set.

Note: Not all devices support all timeouts. Some devices round the value to the most similar value as soon as the Android settings page is opened.
Other devices modify the value to the minimum of (15 seconds) when the value is not supported.

---

### [Set Speakerphone State](actions/action_set_speakerphone_state.md)

The action **Set Speakerphone State** turns the speakerphone of the phone on or off. On most devices a call must be active for this action to have any effect.

Examples:

- Turn the speakerphone on an incoming call and the phone is in the car dock.

#### Settings

##### Speakerphone

Whether to turn the speakerphone on or off.

---

### [Set System Locale](actions/action_set_system_locale.md)

The action **Set System Locale** changes the currently use system locale.

Warning: This function is not officially supported by Android and might not work on all devices.
Warning: This function requires root access, is not officially supported by Android and might not work on all devices. (Android 4.2+)

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.CHANGE_CONFIGURATION`

#### Settings

##### Locale

The technical name of the locale to set. [Variables are supported.](#string-inline-expressions)

---

### [Set System Setting](actions/action_set_system_setting.md)

The action **Set System Setting** stores the specified value in the settings database of the system.

Warning: Modifying system settings to unsupported values can possibly harm your device or crash the system. Use at your own risk!

Note: Changes to some settings are not immediately picked up by the system but require an additional event to occur like turning the screen off and back on. Some settings need to be changed by special APIs, changing the value of such settings in the settings database are ignored by the system.

Note: `adb` can be used on some versions of Android to grant the permissions to modify settings from category **secure** and **global** without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Change the value of a ROM specific setting not available in a regular action in Automagic.

#### Settings working on different devices (not available on all devices)

##### Pulse notification light/LED

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `notification_light_pulse` |
| Value: | `0` = off `1` = on |

##### Night mode (Android 7+, when activated in System UI tuner)

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Secure` |
| Name: | `twilight_mode` |
| Value: | `0` = off `1` = on `2` = automatic |

##### Location mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Secure` |
| Name: | `location_mode` |
| Value: | `0` = location mode off `1` = Device only `2` = Battery saving `3` = High accuracy |

Alternatively:

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Secure` |
| Name: | `location_providers_allowed` |
| Value: | `+gps` = turn GPS on `-gps` = turn GPS off `+network` = turn Network on `-network` = turn Network off |
| Warning: Only change one value at a time! Changing multiple values at once will result in an inconsistent setting value which can only be fixed by a factory reset. | |

##### Mobile data

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Global` |
| Name: | `mobile_data` |
| Value: | `0` = mobile data off `1` = mobile data on |

#### LG specific settings (not available on all devices)

##### Pulse notification light/LED

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `lge_notification_light_pulse` |
| Value: | `0` = off `1` = on |

#### Samsung S3 specific settings (not available on all devices)

##### Driving mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `driving_mode_on` |
| Value: | `0` = off `1` = on |

##### Power saving mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `psm_switch` |
| Value: | `0` = off `1` = on |

##### Blocking mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `dormant_switch_onoff` |
| Value: | `0` = off `1` = on |

##### Multi window mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `multi_window_enabled` |
| Value: | `0` = off `1` = on |

##### S Beam mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `sbeam_mode` |
| Value: | `0` = off `1` = on |

##### Vibration intensity

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `VIB_RECVCALL_MAGNITUDE` `VIB_NOTIFICATION_MAGNITUDE` `VIB_FEEDBACK_MAGNITUDE` |
| Value: | `0` = weak to `5` = strong |

#### Samsung S5 specific settings (not available on all devices)

##### Car mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `car_mode_on` |
| Value: | `0` = off `1` = on |

##### Power saving mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `powersaving_switch` |
| Value: | `0` = off `1` = on |

##### Blocking mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `dormant_switch_onoff` |
| Value: | `0` = off `1` = on |

##### Multi window mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `multi_window_enabled` |
| Value: | `0` = off `1` = on |

##### Toolbox

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `toolbox_onoff` |
| Value: | `0` = off `1` = on |

##### Smart stay

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `intelligent_sleep_mode` |
| Value: | `0` = off `1` = on |

##### Smart pause

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `smart_pause` |
| Value: | `0` = off `1` = on |

##### Touch sensitivity

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `auto_adjust_touch` |
| Value: | `0` = off `1` = on |

##### Vibration intensity

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `VIB_RECVCALL_MAGNITUDE` `VIB_NOTIFICATION_MAGNITUDE` `VIB_FEEDBACK_MAGNITUDE` |
| Value: | `0` = weak to `5` = strong |

#### CyanogenMod specific settings (not available on all devices)

##### Expanded desktop

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `expanded_desktop_state` |
| Value: | `0` = off `1` = on |

#### Settings

##### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global settings valid for all users of the device (Android 4.2+)

##### Name

The name of the setting to modify. [Variables are supported.](#string-inline-expressions)

##### Value

The value to store in the system settings database. [Variables are supported.](#string-inline-expressions)

---

### [Set System Setting (Android Wear)](actions/action_set_system_setting_wear.md)

The action **Set System Setting (Android Wear)** stores the specified value in the settings database of the system.

Warning: Modifying system settings to unsupported values can possibly harm your device or crash the system. Use at your own risk!

Note: Changes to some settings are not immediately picked up by the system but require an addition event to occur like turning the screen off and back on. Some settings need to be changed by special APIs, changing the value of such settings in the settings database are ignored by the system.

Examples:

- Change the value of a ROM specific setting not available in a regular action in Automagic.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global settings valid for all users of the device (Android 4.2+)

##### Name

The name of the setting to modify. [Variables are supported.](#string-inline-expressions)

##### Value

The value to store in the system settings database. [Variables are supported.](#string-inline-expressions)

---

### [Set Telephony Radio State](actions/action_set_telephony_radio_state.md)

The action **Set Telephony Radio State** turns the radio of the phone on or off.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Turn off the radio at night to save battery.

#### Settings

##### Method

Defines the method to use to turn the radio on/off.

##### Telephony Radio

Whether to turn the radio on or off.

---

### [Set Timer](actions/action_set_timer.md)

The action **Set Timer** creates a timer in a compatible timer app installed on the device.

#### Settings

##### Label

The label of the timer. [Variables are supported.](#string-inline-expressions)

##### Duration

The duration of the timer (second granularity). [Variables are supported.](#string-inline-expressions)

##### Skip UI

Whether or not the timer app should be displayed after setting the timer.

---

### [Set USB Debugging State](actions/action_set_usb_debugging_state.md)

The action **Set USB Debugging State** enables or disables the USB debugging setting.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Example:

- Enable USB debugging at work and at home but disable USB debugging elsewhere.

#### Settings

##### USB Debugging

Whether to turn USB debugging on or off.

---

### [Set USB Tethering State](actions/action_set_usb_tethering_state.md)

The action **Set USB Tethering State** turns USB tethering on or off.

Note: This action does not supply the USB tethering feature by itself, it only turns on the setting. Some providers remove the USB tethering feature. This action can **not** turn on tethering on such a phone.

Warning: This function is not officially supported by Android and might not work on all devices.

Warning: This function requires root access starting with Android 4.0.

Examples:

- Turn on USB tethering when USB is connected.
- Turn off USB tethering when the battery level is below 50%.

#### Settings

##### USB Tethering

Whether to turn USB tethering on or off.

---

### [Set Vibrate on Ring State](actions/action_set_vibrate_on_ring_state.md)

The action **Set Vibrate on Ring State** changes the setting whether the device should vibrate on ring or not.

Warning: This function is not officially supported by Android and might not work on all devices.

#### Settings

##### Vibrate on Ring

Whether to change the setting to vibrate on ring should be turned on or off.

---

### [Set Wallpaper](actions/action_set_wallpaper.md)

The action **Set Wallpaper** changes the wallpaper of the phone to the defined static image.

Examples:

- Change the wallpaper at home.
- Change the wallpaper when an SMS is received.

#### Settings

##### Path to wallpaper image

The path to the image file to use as the wallpaper. [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `wallpaper_path` — the path of the set wallpaper

---

### [Set WiFi Access Point Priority](actions/action_set_wifi_access_point_priority.md)

The action **Set WiFi Access Point Priority** sets the priority of an access point configuration to control which access point is chosen to connect to by the phone.

Note: The algorithm used by the device to determine which access point to use and if the device will reconnect to another access point is not known and might vary between devices, versions and manufacturer.

Examples:

- Prefer a free access point over a paid one when both access points are available.

#### Settings

##### SSID

The SSID of the access point configuration to modify.

##### Priority

The priority to use.

---

### [Set WiFi Sleep Policy](actions/action_set_wifi_sleep_policy.md)

The action **Set WiFi Sleep Policy** changes the currently active sleep policy.

Warning: This function requires root access starting with Android 4.2 and is not officially supported by Android.

Examples:

- Always activate WiFi even when you are not using your mobile phone to keep the connection to your media center active.
- Only activate WiFi when you actively use your mobile phone.

#### Settings

##### Keep WiFi on during sleep

Whether WiFi should stay active when your mobile phone is in sleep mode or not.

Note: Disabling WiFi when the device is not active can increase mobile data usage when applications transmit data in the background.

---

### [Set WiFi State](actions/action_set_wifi_state.md)

The action **Set WiFi State** turns WiFi globally on or off.

Examples:

- Turn WiFi on when the phone is connected to a power source.
- Turn WiFi off when the battery level is below 30%.

#### Settings

##### Wifi

Whether to turn WiFi on or off.

---

### [Set WiFi State (Android Wear)](actions/action_set_wifi_state_wear.md)

The action **Set WiFi State (Android Wear)** turns WiFi globally on or off.

Examples:

- Turn WiFi on when the phone is connected to a power source.
- Turn WiFi off when the battery level is below 30%.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Wifi

Whether to turn WiFi on or off.

---

### [Set Wifi Tethering State](actions/action_set_wifi_tethering_state.md)

The action **Set Wifi Tethering State** turns WiFi tethering on or off.

Note: This action does not supply the WiFi tethering feature by itself, it only turns on the setting. Some providers remove the WiFi tethering feature. This action can **not** turn on tethering on such a phone.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Turn on WiFi tethering when a power adapter is connected.
- Turn off WiFi tethering when the battery level is below 50%.

#### Settings

##### Method

Defines the method to use to turn tethering on/off.

##### WiFi Tethering

Whether to turn WiFi tethering on or off.

##### WiFi Tethering

Whether to turn WiFi tethering on or off.

##### Turn WiFi on

Whether to turn WiFi on or off when tethering is turned off.

---

### [Show Call Log](actions/action_show_call_log.md)

The action **Show Call Log** opens the built-in App to show the call log.

---

### [Show Control UI Gesture Recorder](actions/action_show_control_user_interface_gesture_recorder.md)

The action **Show Control UI Gesture Recorder** shows the dialog for recording gestures to simulate user interactions (like action **Control UI->Show overlay control->Gesture**)

Examples:

- Show the recording UI after a delay in case the red buttons are preventing navigation to the desired target UI.

---

### [Show Control UI Infos](actions/action_show_control_user_interface_infos.md)

The action **Show Control UI Infos** shows the dialog for recording clicks to simulate user interactions (like action **Control UI->Show overlay control->Info**)

Examples:

- Show the recording UI after a delay in case the red buttons are preventing navigation to the desired target UI.

---

### [Show Custom Widget Overlay](actions/action_show_custom_widget_overlay.md)

The action **Show Custom Widget Overlay** displays a custom Widget (defined within Automagic) on an arbitrary position on the display. The overlay is also shown on the lock screen on many Android versions.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Show the battery percentage as a semi-transparent rectangle over the statusbar.
- Prevent accidental touches by displaying an overlay that covers the entire screen.
- Shade the screen to a darker level than the built-in screen brightness control allows by displaying a semi transparent overlay covering the entire screen.

#### Settings

##### Overlay name

The name/identification of the overlay. The same name can be used to hide the overlay using action **Hide Custom Widget Overlay.**
The same identification can be used in multiple actions to display the same overlay in different configurations depending on situation (e.g.different settings when in landscape or portrait).

##### Widget

The name of the widget to display. [Variables are supported.](#string-inline-expressions)

##### Width/Height

The size of the overlay. [Variables are supported.](#string-inline-expressions)

##### Gravity

The position to align the overlay on the screen.

##### X/Y-Offset

The offset of the overlay relative to the gravity. [Variables are supported.](#string-inline-expressions)

##### Draggable

Whether the overlay can be moved on the screen using Drag&Drop.

##### Opacity

The transparency respectively opacity of the widget.

##### Clickable

Whether the overlay should react to clicks/touches. Warning: A clickable overlay blocks the touches of underlying elements!

##### Stretch widget

Whether the widget should be stretched to fill the entire area of the overlay.

##### Use accessibility service (Android 5.1+)

Uses the accessibility service to show the overlay and thus could be shown even on the lock screen on some versions of Android

##### Attempt to show on top

Whether Automagic should attempt to show the widget on top of everything else (over statusbar and lock screen).
This option might not work on all devices, especially on newer versions of Android (Android 8+).
This option can prevent certain apps like video players to temporarily override the screen brightness.

##### Don't restrict positions

Whether the system should allow to place the widget outside the regular display area. On some versions of Android this also allows to place the in the area of the navigation bar.
Older Version of Android only respect this option when option **Use accessibility service** is enabled.

---

### [Show Custom Widget Overlay (Android Wear)](actions/action_show_custom_widget_overlay_wear.md)

The action **Show Custom Widget Overlay (Android Wear)** displays a custom Widget (defined within Automagic) on an arbitrary position on the display.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Show the battery percentage as a semi-transparent rectangle over the statusbar.
- Prevent accidental touches by displaying an overlay that covers the entire screen.
- Shade the screen to a darker level than the built-in screen brightness control allows by displaying a semi transparent overlay covering the entire screen.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Overlay name

The name/identification of the overlay. The same name can be used to hide the overlay using action **Hide Custom Widget Overlay.**
The same identification can be used in multiple actions to display the same overlay in different configurations depending on situation (e.g.different settings when in landscape or portrait).

##### Widget

The name of the widget to display. [Variables are supported.](#string-inline-expressions)

##### Width/Height

The size of the overlay. [Variables are supported.](#string-inline-expressions)

##### Gravity

The position to align the overlay on the screen.

##### X/Y-Offset

The offset of the overlay relative to the gravity. [Variables are supported.](#string-inline-expressions)

##### Draggable

Whether the overlay can be moved on the screen using Drag&Drop.

##### Opacity

The transparency respectively opacity of the widget.

##### Clickable

Whether the overlay should react to clicks/touches. Warning: A clickable overlay blocks the touches of underlying elements!

##### Stretch widget

Whether the widget should be stretched to fill the entire area of the overlay.

##### Attempt to show on top

Whether Automagic should attempt to show the widget on top of everything else (over statusbar and lock screen).
This option might not work on all devices, especially on newer versions of Android (Android 8+).
This option can prevent certain apps like video players to temporarily override the screen brightness.

---

### [Show Home Screen](actions/action_show_home_screen.md)

The action **Show Home Screen** launches the home screen.

#### Settings

##### Page

The number of the page to show (only supported by a few launchers). [Variables are supported.](#string-inline-expressions)

Note for developers: The selected page is passed as an int-extra with name *net.dinglisch.android.tasker.extras.HOME\_PAGE* to the launcher.

---

### [Show Input Method Selector](actions/action_show_input_method_selector.md)

The action **Show Input Method Selector** shows the screen to select the input method/keyboard.

Examples:

- Open the input method selector to change the keyboard using action **Control UI**.

---

### [Shutdown](actions/action_shutdown.md)

The action **Shutdown** shuts the device down.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

---

### [Silence Ringer](actions/action_silence_ringer.md)

The action **Silence Ringer** silences the ringer and stops the vibrator when an incoming call is currently ringing.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Silence the ringer on a call after 5 seconds when you are in a meeting.

---

### [Sleep](actions/action_sleep.md)

The action **Sleep** pauses the flow execution for a certain amount of time.

Note: Please uncheck the option *Keep device awake* when the period is longer than one to two minutes and the functions of the flow does not require an active device CPU.

Examples:

- Sleep a second when a vibrate action is executing.
- Slow down a countdown flow.

#### Settings

##### Duration

The amount of time to sleep. [Variables are supported.](#string-inline-expressions)

##### Keep device awake

Ensure that the device does not go into deep sleep while the action is executed.
Unchecking this option will not prevent the device from falling into deep sleep mode. The device will be woken up when the specified period has elapsed.

##### Wakeup from idle/doze (Android 6+)

Defines if this action is allowed resume from idle/doze mode. (see [Device Idle/Doze Mode](../reference/device-idle-mode.md))

---

### [Snooze Notification on Statusbar](actions/action_snooze_notification_status_bar.md)

The action **Snooze Notification on Statusbar** asks the system to hide a notification for a defined amount of time.
The flow must be executed by a trigger **Notification on Statusbar Displayed** or the action after a condition **Notification on Statusbar Displayed** otherwise Automagic has no possibility to access the notification.

Examples:

- Hide a notification for a missed call for one hour.

#### Settings

##### Duration

The duration. [Variables are supported.](#string-inline-expressions)

---

### [Sound](actions/action_sound.md)

The action **Sound** plays the selected sound.

Examples:

- Beep every 5 minutes when **Gleeo Time Tracker** is recording.
- Play an additional alert when an SMS is received.

#### Settings

##### Sound Type

The type of sound to select.

Possible settings:

- **Built-in sound**: to select a built-in notification, alarm or ringtone
- **File**: to select an arbitrary audio file to play

##### Sound

The name of the selected ringtone, notification or alarm sound.

##### File

The path or the URL to the audio file to play. [Variables are supported.](#string-inline-expressions)

##### Audio Stream Type

The stream to use to play the sound.

##### Start Position

The start position in milliseconds to use to start the playback. [Variables are supported.](#string-inline-expressions)

##### Show status bar notification to stop sound

Shows a status bar notification when the sound is playing that stops the sound when selected.

##### Wait for sound to finish

Makes the action wait for the sound to finish before continuing with the next element in the flow.

##### Request audio focus

Defines whether or not and how Automagic should request audio focus. This causes other apps like music players to pause playback or to temporarily lower the volume.

Possible settings:

- **Transient**: Automagic requests temporary audio focus, other apps usually pause playback temporarily (depends on app)
- **Transient may duck**: Automagic requests temporary audio focus, other apps either temporarily pause playback or temporarily lower the volume (depends on app)
- **Normal**: Automagic requests the normal audio focus, other apps usually pause/stop playback (depends on app)

---

### [Speech Output](actions/action_speech_output.md)

The action **Speech Output** uses the default text to speech engine installed to read the defined text.

Examples:

- Read out the incoming SMS.
- Read the current time when you press a shortcut.

#### Settings

##### Voice

The voice/language to use. The list of available voices depends on the installed TTS engine.

##### Audio Stream Type

The type of the audio stream to use to emit the speech output.

##### Text

The text to speak. [Variables are supported.](#string-inline-expressions)

Examples:

- use `{triggertime,dateformat,HH:mm:ss}` to read the time

##### Speech Rate

Whether or not to use a custom speech rate (0.5=slow, 1.0=normal, 2.0=fast). Not supported by all text to speech engines. [Variables are supported.](#string-inline-expressions)

##### Pitch

Whether or not to use a custom pitch (0.5=low, 1.0=normal, 2.0=high). Not supported by all text to speech engines. [Variables are supported.](#string-inline-expressions)

##### Synthesis Embedded

When checked the engine must not use network access to synthesise the speech. Not supported by all text to speech engines.

##### Synthesis Network

When checked the engine must use network based synthesis. Not supported by all text to speech engines.

##### Show status bar notification to stop speaking

Shows a status bar notification when the tts engine is speaking that stops the speaking when selected.

##### Request audio focus

Defines whether or not and how Automagic should request audio focus. This causes other apps like music players to pause playback or to temporarily lower the volume.

Possible settings:

- **Transient**: Automagic requests temporary audio focus, other apps usually pause playback temporarily (depends on app)
- **Transient may duck**: Automagic requests temporary audio focus, other apps either temporarily pause playback or temporarily lower the volume (depends on app)
- **Normal**: Automagic requests the normal audio focus, other apps usually pause/stop playback (depends on app)

---

### [Start Activity](actions/action_start_activity.md)

The action **Start Activity** starts an activity using the specified intent. Please also see the [documentation of the Android Intent class](http://developer.android.com/reference/android/content/Intent.html).

Tip: Some activities require special permissions to be launched. Check the log after testing the action when an activity fails to start.

Examples:

- Start a specific action exposed by another application.
- Start a Skype call:
  - Action: **android.intent.action.VIEW**
  - Data URI: **skype:echo123**
- Dial a number (without calling):
  - Action: **android.intent.action.DIAL**
  - Data URI: **tel:99**
- Starting a mail app with a predefined subject:
  - Action: **android.intent.action.SEND**
  - Data MIME Type: **text/plain**
  - Extras: **putString("android.intent.extra.SUBJECT", "test")**

#### Settings

##### Action

The action to use in the intent. [Variables are supported.](#string-inline-expressions)

##### Category List

The list of categories as a comma separated list to add to the intent. [Variables are supported.](#string-inline-expressions)

##### Data URI

The data URI to set on the intent. [Variables are supported.](#string-inline-expressions)

##### Mime Type

The mime type to set on the intent. [Variables are supported.](#string-inline-expressions)

##### Package Name

The specific package to launch. [Variables are supported.](#string-inline-expressions)

##### Class Name

The specific activity to launch. [Variables are supported.](#string-inline-expressions)

##### Launch bounds (Android 7+)

Whether the activity should be started at the defined position and size. This feature only has an effect on devices supporting freeform mode.
[Variables are supported.](#string-inline-expressions)

##### Flag List

The flags to add to the intent. Note that the flag `Intent.FLAG_ACTIVITY_NEW_TASK` is always added to the intent.

##### Extras

A script used to add an unlimited number of extras to the intent.

Additionally to the regular built in functions of Automagic also the following functions are available to add the extras to the intent:

- `putString(key, value)`
- `putBoolean(key, value)`
- `putFloat(key, value)`
- `putDouble(key, value)`
- `putByte(key, value)`
- `putShort(key, value)`
- `putChar(key, value)`
- `putInt(key, value)`
- `putLong(key, value)`
- `putUri(key, value)`
- `putBooleanArray(key, value)`
- `putByteArray(key, value)`
- `putIntArray(key, value)`
- `putIntegerArrayList(key, value)`
- `putLongArray(key, value)`
- `putFloatArray(key, value)`
- `putDoubleArray(key, value)`
- `putShortArray(key, value)`
- `putCharArray(key, value)`
- `putStringArray(key, value)`
- `putStringArrayList(key, value)`
- `putUriArray(key, value)`
- `putUriArrayList(key, value)`

Example:
```
putString("key1", "Hello");
putBoolean("key2", true);
putDouble("key3", 1.23);
putInt("key4", 42);
putInt("key5", a+4*b);
```

[See action Script for a description of the scripting language.](#scan-barcode)

##### Wait for result

Whether Automagic should wait for the activity to return a result (only works when supported by the activity).

##### Access Result Extras

Script to access the extras in the returned intent.
Following functions are supported:

- `getString(String key)`
- `getChar(String key, String defaultValue)`
- `getBoolean(String key, Boolean defaultValue)`
- `getFloat(String key, Number defaultValue)`
- `getDouble(String key, Number defaultValue)`
- `getByte(String key, Number defaultValue)`
- `getShort(String key, Number defaultValue)`
- `getInt(String key, Number defaultValue)`
- `getLong(String key, Number defaultValue)`
- `getBundle(String key)`
- `getUri(String key)`
- `getBooleanArray(String key)`
- `getByteArray(String key)`
- `getShortArray(String key)`
- `getCharArray(String key)`
- `getIntArray(String key)`
- `getIntegerArrayList(String key)`
- `getLongArray(String key)`
- `getFloatArray(String key)`
- `getDoubleArray(String key)`
- `getStringArray(String key)`
- `getUriArray(String key)`
- `getUriArrayList(String key)`
- `getParcelableAsString(String key)`
- `getParcelableArrayAsString(String key)`
- `getParcelableArrayListAsString(String key)`
- `getParcelable(String key)`

[See action Script for a description of the scripting language.](#scan-barcode)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `result_code` — the returned result code
- `operation` — string "ok", when result\_code was -1, "cancel" otherwise
- `action` — the action of the received intent
- `data_string` — the data of the received intent as a string
- `categories` — the list of categories
- `scheme` — the scheme of the received intent
- `type` — the explicitly set MIME type of the received intent

---

### [Start Daydream](actions/action_start_daydream.md)

The action **Start Daydream** starts the daydream configured in the Android settings.

Warning: This function is not officially supported by Android and might not work on all devices.

Note: The action requires Android 4.2+.

Examples:

- Start to daydream when a shortcut is clicked.

---

### [Start Recording Audio](actions/action_start_recording_audio.md)

The action **Start Recording Audio** starts recording the specified audio source to the defined file. Only one audio file can be captured at a time.
The recording can be stopped manually using the shown statusbar notification or by executing the action **Stop Recording Audio**.

Warning: Some audio sources are not supported on most devices due to technical or legal reasons.

Examples:

- Start recording the audio of an incoming call.
- Record the audio at night between 1am and 2am.
- Record the audio for 10 minutes when an SMS arrives and send the resulting audio file to your mail account.

#### Settings

##### Audio Source

The audio source to record.

Warning: The voice audio sources are not supported on most devices due to technical or legal reasons.

##### Audio Encoder

The audio encoding to use to compress the recorded audio.

##### Maximum Duration

The maximum duration to use when recording audio.

##### File

The path of the file to store the recorded audio in. A file ending of `m4a` or `mp4` is recommended. [Variables are supported.](#string-inline-expressions)

Example:

- `/mnt/sdcard/audio_{triggertime,dateformat,yyyy_MM_dd}.m4a` becomes `/mnt/sdcard/audio_2011_02_13.m4a`

##### Show status bar notification to stop recording

Shows a status bar notification when audio is recording to stop.

---

### [Start Recording Screen (Experimental)](actions/action_start_recording_screen.md)

The action **Start Recording Screen (Experimental)** starts to record the screen as a video to the defined file. Only one recording session can be active at the same time.
The recording can be stopped manually using the shown statusbar notification or by executing the action **Stop Recording Screen**.

Examples:

- Record the screen for a few seconds when the device was stolen.

#### Settings

##### Resolution

The resolution.

##### Bit rate

The bit rate..

##### File

The path of the file to store the recorded video in. A file ending of `mp4` is recommended. [Variables are supported.](#string-inline-expressions)

##### Record audio

Whether to record audio using the device microphone or not.

##### Show status bar notification to stop recording

When enabled shows a status bar notification to stop recording.

---

### [Start Service](actions/action_start_service.md)

The action **Start Service** starts a service using the specified intent. Please also see the [documentation of the Android Intent class](http://developer.android.com/reference/android/content/Intent.html).

Tip: Some services require special permissions to be launched. Check the log after testing the action when a service fails to start.

#### Settings

##### Action

The action to use in the intent. [Variables are supported.](#string-inline-expressions)

##### Category List

The list of categories as a comma separated list to add to the intent. [Variables are supported.](#string-inline-expressions)

##### Data URI

The data URI to set on the intent. [Variables are supported.](#string-inline-expressions)

##### Mime Type

The mime type to set on the intent. [Variables are supported.](#string-inline-expressions)

##### Package Name

The specific package to launch. [Variables are supported.](#string-inline-expressions)

##### Class Name

The specific service to launch. [Variables are supported.](#string-inline-expressions)

##### Flag List

The flags to add to the intent.

##### Extras

A script used to add an unlimited number of extras to the intent.

Additionally to the regular built in functions of Automagic also the following functions are available to add the extras to the intent:

- `putString(key, value)`
- `putBoolean(key, value)`
- `putFloat(key, value)`
- `putDouble(key, value)`
- `putByte(key, value)`
- `putShort(key, value)`
- `putChar(key, value)`
- `putInt(key, value)`
- `putLong(key, value)`
- `putUri(key, value)`
- `putBooleanArray(key, value)`
- `putByteArray(key, value)`
- `putIntArray(key, value)`
- `putIntegerArrayList(key, value)`
- `putLongArray(key, value)`
- `putFloatArray(key, value)`
- `putDoubleArray(key, value)`
- `putShortArray(key, value)`
- `putCharArray(key, value)`
- `putStringArray(key, value)`
- `putStringArrayList(key, value)`
- `putUriArray(key, value)`
- `putUriArrayList(key, value)`

Example:
```
putString("key1", "Hello");
putBoolean("key2", true);
putDouble("key3", 1.23);
putInt("key4", 42);
putInt("key5", a+4*b);
```

[See action Script for a description of the scripting language.](#scan-barcode)

---

### [Stop Action Sound](actions/action_stop_action_sound.md)

The action **Stop Action Sound** stops a currently executing action **Sound**

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `sound_position` — the playback position of the stopped sound in milliseconds (first sound if multiple playing), null when no sound was stopped
- `sound_duration` — the total duration of the sound in milliseconds (first sound if multiple playing), null when the media framework of Android can not determine the duration (live stream etc.)

---

### [Stop Action Speech Output](actions/action_stop_action_speech_output.md)

The action **Stop Action Speech Output** stops a currently executing action **Speech Output**

---

### [Stop Flows](actions/action_stop_flows.md)

The action **Stop Flows** stops one or multiple flows specified in the field **Flow pattern list** as soon as possible. Use an action **Set Flow State** to disable flows.

Examples:

- Stop a wake-up flow when the device is shaken.

#### Settings

##### Flow pattern list

A comma separated list of flow names to stop. Glob patterns `*` and `?` can be used to match similar named flows.

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*battery save*`

##### Exclude flow pattern list

A comma separated list of flow names to **not** stop, even when the field **Flow pattern list** includes the flow.

---

### [Stop Recording Audio](actions/action_stop_recording_audio.md)

The action **Stop Recording Audio** stops the currently recording audio started with action **Start Recording Audio**.

Examples:

- Stop recording a call when the call ends.

---

### [Stop Recording Screen (Experimental)](actions/action_stop_recording_screen.md)

The action **Stop Recording Screen (Experimental)** stops a recording that was previously started with action **Start Recording Screen**.

---

### [Store Audio Volumes](actions/action_store_audio_stream_volume.md)

The action **Store Audio Volumes** stores the currently set audio volumes in global variables to restore using action **Restore Audio Volumes**.

Examples:

- Store the audio volumes when a meeting begins, set all volumes to zero and restore the previously volumes when the meeting ends.

#### Settings

##### Alarm

Whether or not to store the alarm volume and the name of the variable to store the volume in.

##### DTMF

Whether or not to store the DTMF volume and the name of the variable to store the volume in.

##### Music

Whether or not to store the music volume and the name of the variable to store the volume in.

##### Notification

Whether or not to store the notification volume and the name of the variable to store the volume in.

##### Ring

Whether or not to store the ringtone volume and the name of the variable to store the volume in.

##### System

Whether or not to store the system volume and the name of the variable to store the volume in.

##### Voice Call

Whether or not to store the voice call volume and the name of the variable to store the volume in.

##### Ringer Mode

Whether or not to store the ringer mode and the name of the variable to store the value in.

##### Interruptions Mode

Whether or not to store the interruptions mode and the name of the variable to store the value in.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- names of the variables defined in the text fields — the volumes, ringer mode and interruptions mode as numbers

---

### [Take Picture](actions/action_take_picture.md)

The action **Take Picture** takes a picture using the built-in camera app or directly in the background without showing a user interface/preview (Android 4+)

Examples:

- Take a picture once an hour and upload the image to Dropbox.

#### Settings

##### Recording Mode

Whether to use the camera app or to take the picture in the background without user interface (Android 4+).

##### Target File

The target file to save the picture. [Variables are supported.](#string-inline-expressions)

##### Camera

The camera to use to take the picture.

##### Picture Size

The resolution of the image.

##### Zoom

The zoom ratio.

##### Scene Mode

The scene mode.

##### Flash Mode

Whether to use the flash or not.

##### White Balance

The white balance setting to use.

##### Focus Mode

The focus mode to use.

##### Effect

The effect to apply to the image. Not all effects work with all cameras. Often the effect is ignored for the front-facing camera.

##### Await preview images

Whether or not Automagic should await that the camera produces valid preview images before it takes the picture. Can be unchecked to take pictures faster or to workaround issues when the camera does not produce any preview images and thus runs into a timeout.

##### Delay to fix black picture

Whether or not and how long Automagic should delay taking the picture after the camera has been initialized by Android. On some devices a delay of about 2 seconds can prevent the camera from producing black pictures.

##### Add to gallery

Whether or not the image should be made available in the gallery app. Otherwise the picture will become available when the system scans the device for media files the next time.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `picture_path` — the target path of the picture

---

### [Take Screenshot (Experimental)](actions/action_take_screenshot.md)

The action **Take Screenshot (Experimental)** creates a screenshot of the currently displayed screen.

Tip: Action **Execute Root Command: screencap -p image.png** can be used on many rooted devices to take a screenshot on older versions of Android.

Note: Android delivers the screen content compressed to Automagic, the quality of the image is not always optimal. Some devices only allow to take screenshots with a low resolution.

Note: Views that are marked as secure by the displaying app can not be recorded.

Note: The display has to be turned on to take a screenshot.

Examples:

- Create a screenshot and send the image as an attachment as an EMail when a special SMS is received.

#### Settings

##### Resolution

The resolution.

##### File

The path of the file to store [Variables are supported.](#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](#string-inline-expressions)

#### Supplied Variables

- `operation` — "ok" when successful, "cancel" when interrupted
- `output_path` — the target path of the screenshot

---

### [Turn Screen On](actions/action_turn_screen_on.md)

The action **Turn Screen On** turns the screen on for a few seconds.

Examples:

- Turn the screen on when an SMS arrives.

#### Settings

##### Screen Brightness

Whether the screen should be fully turned on or only dimmed.

Note: Some devices ignore this setting and always use the bright mode.

##### Duration

The amount of time to keep the screen on. [Variables are supported.](#string-inline-expressions)

Note: Some devices ignore this setting and use a longer duration.

##### Reset user activity timer

Whether or not to reset the user activity timer. Resetting the timer keeps the screen on a little bit longer.

Note: Some devices ignore this setting.

---

### [Turn Screen On (Android Wear)](actions/action_turn_screen_on_wear.md)

The action **Turn Screen On (Android Wear)** turns the screen on for a few seconds.

Examples:

- Turn the screen on when an SMS arrives.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

---

### [Unzip Files](actions/action_unzip_files.md)

The action **Unzip Files** unzips all files and folders contained in the ZIP file to the specified target folder.

Examples:

- Unzip all files in `archive.zip` to directory `/mnt/sdcard/xyz/`.

#### Settings

##### ZIP File

The ZIP File to uncompress. [Variables are supported.](#string-inline-expressions)

##### Target Directory

The absolute path of the target directory to unzip the archive to. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

### [Update Media Database (Experimental)](actions/action_update_media_database.md)

The action **Update Media Database (Experimental)** checks the specified file or folder to delete not existing files from the media database and scans all existing files so the system can add them to the media database when desired.

Note: Please note that scanning of files is a heavy weight process and should be executed only infrequently. It's not recommended to scan the entire external storage.

Examples:

- Scan a new folder after the folder has been copied to ensure that images are shown immediately in the gallery.

#### Settings

##### File

The file or folder to scan. [Variables are supported.](#string-inline-expressions)

---

### [Update Quick Settings Tile](actions/action_update_quick_settings_tile.md)

The action **Update Quick Settings Tile** updates a tile that was create with trigger **Quick Settings Tile Selected**.

Note: Deactivating/activating a flow containing the trigger **Quick Settings Tile Selected** will update the tile with the information available to the trigger.

Examples:

- Change the icon of a tile when a particular system setting was turned off.

#### Settings

##### Tile

The tile to use.

##### Icon

The icon to use for the tile. [Variables are supported (replaced when trigger is activated).](#string-inline-expressions)

##### Label

The label of the tile. [Variables are supported (replaced when trigger is activated).](#string-inline-expressions)

##### State

The state of the tile.

---

### [Vibrate](actions/action_vibrate.md)

The action **Vibrate** vibrates with a specific pattern.

Examples:

- Vibrate when WiFi has been disconnected.
- Vibrate when entering a location.

#### Settings

##### Pattern Type

Whether to use a predefined pattern or to enter/record a custom pattern.

##### Vibrate Pattern

The vibration pattern to use.
A custom pattern can be composed using a list of numbers in milliseconds to turn the vibrator on/off like *0,500,1000,500* (0ms pause, 500ms vibration, 1000ms pause, 500ms vibration).

---

### [Vibrate (Android Wear)](actions/action_vibrate_wear.md)

The action **Vibrate (Android Wear)** vibrates with a specific pattern.

Examples:

- Vibrate when WiFi has been disconnected.
- Vibrate when entering a location.

#### Settings

##### Android Wear device

The target device. [Variables are supported.](#string-inline-expressions)

##### Pattern Type

Whether to use a predefined pattern or to enter/record a custom pattern.

##### Vibrate Pattern

The vibration pattern to use.
A custom pattern can be composed using a list of numbers in milliseconds to turn the vibrator on/off like *0,500,1000,500* (0ms pause, 500ms vibration, 1000ms pause, 500ms vibration).

---

### [Voice Search (Experimental)](actions/action_voice_search.md)

The action **Voice Search (Experimental)** starts the built-in voice search of the system. The speech recognition engine usually requires network access.

#### Settings

##### Prompt

An optional title to show in the user interface. This setting might be ignored by the engine. [Variables are supported.](#string-inline-expressions)

##### Language

Optional the desired language to use in the speech recognition engine. This setting might be ignored by the engine. [Variables are supported.](#string-inline-expressions)

---

### [WiFi Reassociate](actions/action_wifi_reassociate.md)

The action **WiFi Reassociate** reconnects to the currently active access point.

---

### [WiFi Scan](actions/action_wifi_scan.md)

The action **WiFi Scan** starts a scan for available access points.

Note: This is an asynchronous operation and you have to use a trigger **WiFi Scan Results Available** to process the results.

Examples:

- Start a WiFi scan when you are coming home to faster connect to the access point.

---

### [Write HTTP Response File (Experimental)](actions/action_write_http_response_file.md)

The action **Write HTTP Response File (Experimental)** writes the specified file as a response to a HTTP request. The flow must be invoked by a trigger *HTTP Request* to write a response.

Example:

- Fetch a file on your Android device from your desktop PC when connected to the same WiFi network.

#### Settings

##### File

The name of the file to deliver. [Variables are supported.](#string-inline-expressions)

##### Custom HTTP Headers

A text containing the custom HTTP headers to send. [Variables are supported.](#string-inline-expressions)

Each line should start with the header name and a colon followed by the value to send.

Examples:

- `User-Agent: my own user agent`
- `SOAPAction: "test"`

---

### [Write HTTP Response Text (Experimental)](actions/action_write_http_response_text.md)

The action **Write HTTP Response Text (Experimental)** writes the specified text as a response to a HTTP request. The flow must be invoked by a trigger *HTTP Request* to write a response.

Example:

- Return a page with device information when a specific page is requested.

#### Settings

##### Text

The text to write. [Variables are supported.](#string-inline-expressions)

##### Content Type

The content type (like text/plain or text/html) of the content. The content type is only considered when no data has been returned to the client yet. [Variables are supported.](#string-inline-expressions)

##### Custom HTTP Headers

A text containing the custom HTTP headers to send. [Variables are supported.](#string-inline-expressions)

Each line should start with the header name and a colon followed by the value to send.

Examples:

- `User-Agent: my own user agent`
- `SOAPAction: "test"`

##### Finish HTTP Response

Whether to finish the HTTP response by sending the text immediately to the client.

---

### [Write to File](actions/action_write_to_file.md)

The action **Write to File** writes the defined text to the specified file. The action automatically creates the file when the file does not exist yet.

Examples:

- Record your location every 20 minutes to a file.
- Write all incoming SMS to a file.

#### Settings

##### File

The file to write the text to. [Variables are supported.](#string-inline-expressions)

##### Text

The text to write into the file. The text can contain multiple lines. [Variables are supported.](#string-inline-expressions)

##### Append

Whether to append the text to the end of the file or to overwrite the file.

---

### [Write to Log](actions/action_write_to_log.md)

The action **Write to Log** appends the defined text to the log file.

Examples:

- Log a variable to debug a flow.

#### Settings

##### Text

The text to write to the log file. [Variables are supported.](#string-inline-expressions)

---

### [Zip Files](actions/action_zip_files.md)

The action **Zip Files** creates a Zip archive containing the specified files and directories.

Examples:

- Zip all files in directory `/mnt/sdcard/xyz/` to the zip file `/mnt/sdcard/backup.zip`.

#### Settings

##### Source Files

A comma separated list of files or directories to zip. Glob patterns can be used to match multiple files. [Variables are supported.](#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

The files in the ZIP file are stored relative based on the parent directory of the files to archive:

- Source Files `/mnt/sdcard/export*` will store all export\* files directly (without parent folder) in the ZIP file
- Source Files `/mnt/sdcard/download/` (note the trailing slash) will store all files in folder download directly (without parent folder) in the ZIP file
- Source Files `/mnt/sdcard/download` (no trailing slash) will store the folder `download` and its contained files in the ZIP file

##### ZIP File

The absolute path of the target ZIP file to create. [Variables are supported.](#string-inline-expressions)

##### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Katalog komponen](README.md) · [Indeks trigger](triggers/README.md) · [Indeks condition](conditions/README.md) · [Indeks action](actions/README.md)
