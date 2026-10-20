# Indeks Trigger (127)

Trigger adalah titik awal sebuah flow. Komponen di bagian ini memicu eksekusi ketika peristiwa tertentu terjadi, misalnya baterai berubah, WiFi tersambung, atau waktu tertentu tiba.

Daftar berikut diurutkan alfabetis. Ringkasan diambil dari paragraf pembuka dokumentasi asli (bahasa Inggris) agar tetap akurat.

| No. | Nama | Ringkasan |
| ---: | --- | --- |
| 1 | [Accessibility Button](trigger_accessibility_button.md) | The trigger Accessibility Button is executed when the additional button on the navigation bar is clicked. |
| 2 | [Active Network Type](trigger_active_network_type.md) | The trigger Active Network Type executes a flow when the active network type changes to another type. |
| 3 | [Activity Ended](trigger_activity_ended.md) | The trigger Activity Ended is executed when an activity is moved to the background. |
| 4 | [Activity Started](trigger_activity_started.md) | The trigger Activity Started is executed when an activity is moved to the foreground. |
| 5 | [Airplane Mode](trigger_airplane_mode.md) | The trigger Airplane Mode is executed when the airplane mode is turned on or off. |
| 6 | [Android Wear Device Connected/Disconnected](trigger_android_wear_device_connected.md) | The trigger Android Wear Device is executed when an Android Wear device is connected or disconnected from the main device. |
| 7 | [App Package Event](trigger_app_package_event.md) | The trigger App Package Event is executed when a app/package is installed, updated or removed. |
| 8 | [App Task Ended](trigger_app_task_ended.md) | The trigger App Task Ended is executed when an application is moved to the background or closed respectively the user moved the focus to another app. |
| 9 | [App Task Started](trigger_app_task_started.md) | The trigger App Task Started is executed when an application is moved to the foreground or opened respectively the user moved the focus to this app. |
| 10 | [Assist](trigger_assist.md) | The trigger Assist is executed when the home button is long-pressed or dragged upwards (Galaxy Nexus) or the home button is long-pressed and the middle icon is selected (S3). |
| 11 | [Audio Volume](trigger_audio_volume.md) | The trigger Audio Volume is executed when the volume of the device has been changed. Some devices report the volume change slightly delayed. |
| 12 | [Auto Sync State](trigger_auto_sync_state.md) | The trigger Auto Sync State is executed when the auto sync setting is changed to on or off. |
| 13 | [Automagic Notification Selected](trigger_automagic_notification_selected.md) | The trigger Automagic Notification Selected executes a flow when the Automagic-wand notification available in the statusbar is selected. |
| 14 | [Automagic SMS Delivery Report Received](trigger_sms_delivery_report_received.md) | The trigger Automagic SMS Delivery Report Received is executed when an asynchronous delivery report was received. |
| 15 | [Automagic Startup](trigger_automagic_startup.md) | The trigger Automagic Startup is executed when the Automagic service is completely started and the flows have been loaded. |
| 16 | [Battery Level](trigger_battery_level.md) | The trigger Battery Level is executed whenever the battery level changes and the built in condition about the level holds true. |
| 17 | [Battery Level (Android Wear)](trigger_battery_level_wear.md) | The trigger Battery Level (Android Wear) is executed whenever the battery level changes and the built in condition about the level holds true. |
| 18 | [Battery Low Condition](trigger_battery_low_okay.md) | The trigger Battery Low Condition is executed when the battery level becomes low or when the battery level becomes OK again after it was low. |
| 19 | [Battery Saver Mode](trigger_power_save_mode.md) | The trigger Battery Saver Mode is executed when the battery saving mode of the device is changed (Android 5+). |
| 20 | [Bluetooth Device Connected](trigger_bluetooth_device_connected.md) | The trigger Bluetooth Device Connected is executed when a bluetooth device is connected. |
| 21 | [Bluetooth Device Disconnected](trigger_bluetooth_device_disconnected.md) | The trigger Bluetooth Device Disconnected is executed when a bluetooth device is disconnected. |
| 22 | [Bluetooth State](trigger_bluetooth_state.md) | The trigger Bluetooth State is executed when the bluetooth adapter of the device is turned on or off depending on the settings used. |
| 23 | [Calendar](trigger_calendar.md) | The trigger Calendar is executed on the defined date and time. |
| 24 | [Calendar Event](trigger_calendar_event.md) | The trigger Calendar Event is executed when an event on the calendar starts or ends. |
| 25 | [Car UI Mode](trigger_car_ui_mode.md) | The trigger Car UI Mode is executed when the device is put into car UI mode when placed in a car dock. |
| 26 | [Clipboard Changed](trigger_clipboard_changed.md) | The trigger Clipboard Changed is executed when the content of the clipboard changes. Use the action Copy Text from Clipboard to access the content of the clipboard. |
| 27 | [Command Output](trigger_command_output.md) | The trigger Command Output is executed when a command prints a line containing a specific text. |
| 28 | [Compass](trigger_compass.md) | The trigger Compass executes the flow when the device changes its orientation. |
| 29 | [Content Provider Changed](trigger_content_provider_changed.md) | The trigger Content Provider Changed is executed whenever the content provider is changed for the specified URI. Note that not all content providers support this feature. |
| 30 | [CyanogenMod Quick Settings Tile Selected](trigger_cyanogen_mod_quick_settings_tile_selected.md) | The trigger CyanogenMod Quick Settings Tile Selected creates a quick settings tile and is executed when the tile is selected/clicked. |
| 31 | [Daydream State](trigger_daydream_state.md) | The trigger Daydream State is executed when the daydream of the system starts or stops. |
| 32 | [Desk UI Mode](trigger_desk_ui_mode.md) | The trigger Desk UI Mode is executed when the device is put into desk UI mode when placed in a desk dock. |
| 33 | [Device Idle/Doze Mode](trigger_device_idle_mode.md) | The trigger Device Idle/Doze Mode is executed when the device falls into idle/doze mode or is woken up from this mode. |
| 34 | [Device Orientation](trigger_device_orientation.md) | The trigger Device Orientation executes the flow when the device is moved to the defined orientation. |
| 35 | [Device Storage Space Low](trigger_device_storage_space_low_okay.md) | The trigger Device Storage Space Low executes the flow when the internal device storage space becomes low or the free storage space is back to a normal level. |
| 36 | [Display State](trigger_display_state.md) | The trigger Display State is executed when the display is turned on or off. |
| 37 | [Dock Event](trigger_dock_event.md) | The trigger Dock Event is executed when the device is put into a dock (car, desk, some external hardware keyboard). |
| 38 | [File Observer](trigger_file_observer.md) | The trigger File Observer is executed when a path of interest on the filesystem is accessed or changed. |
| 39 | [Fingerprint Gesture](trigger_fingerprint_gesture.md) | The trigger Fingerprint Gesture executes a flow when one of the supported gestures is executed on the fingerprint sensor. |
| 40 | [General Broadcast](trigger_general_broadcast.md) | The trigger General Broadcast dynamically registers a broadcast receiver at runtime with the specified intent filter. Please also see the Android Developer Documentation. |
| 41 | [Gleeo Recording Started](trigger_gleeo_recording_started.md) | The trigger Gleeo Recording Started is executed when a task in Gleeo Time Tracker has been started. |
| 42 | [Gleeo Recording Stopped](trigger_gleeo_recording_stopped.md) | The trigger Gleeo Recording Stopped is executed when a task in Gleeo Time Tracker has been stopped. |
| 43 | [Global Variable](trigger_global_variable.md) | The trigger Global Variable is executed when a different value is assigned to a global variable. |
| 44 | [Global Variable Date/Time](trigger_global_variable_date.md) | The trigger Global Variable Date/Time is executed when the point of time stored in the global variable is reached. |
| 45 | [Gmail Unread Conversation Count](trigger_gmail_unread_conversation_count.md) | The trigger Gmail Unread Conversation Count is executed when the count of unread conversations in the Gmail app on the device changes. |
| 46 | [GPS Status Event](trigger_gps_status_event.md) | The trigger GPS Status Event is executed, when the system start or stops to use GPS. |
| 47 | [Hardware Key Event](trigger_key_event.md) | The trigger Hardware Key Event is executed when the specified key is pressed/released. Most devices usually only provide hardware keys for volume up and volume down. |
| 48 | [Hardware Keyboard State](trigger_hardware_keyboard_state.md) | The trigger Hardware Keyboard State is executed when the hardware keyboard is opened or closed. |
| 49 | [Hardware Keyboard Type](trigger_hardware_keyboard_type.md) | The trigger Hardware Keyboard Type is executed when the type of hardware keyboard changes to one of the selected types. |
| 50 | [HTTP Request (Experimental)](trigger_http_request.md) | The trigger HTTP Request (Experimental) is executed when a HTTP request is received using the specified path and port. |
| 51 | [Incoming Call](trigger_incoming_call.md) | The trigger Incoming Call is executed when a call is received depending on the criteria defined in the options. |
| 52 | [Interruptions Mode](trigger_interruptions_mode.md) | The trigger Interruptions Mode is executed when the device switches to the desired interruption mode. |
| 53 | [K-9 Mail Received](trigger_k9_mail_received.md) | The trigger K-9 Mail Received is executed when K-9 Mail receives a mail. |
| 54 | [Launch Browser App Intent Received](trigger_launch_browser_app_intent_received.md) | The trigger Launch Browser App Intent Received is executed when an app or the system wants to launch a browser app. |
| 55 | [Launch Calculator App Intent Received](trigger_launch_calculator_app_intent_received.md) | The trigger Launch Calculator App Intent Received is executed when an app or the system wants to launch a calculator app. |
| 56 | [Launch Calendar App Intent Received](trigger_launch_calendar_app_intent_received.md) | The trigger Launch Calendar App Intent Received is executed when an app or the system wants to launch a calendar app. |
| 57 | [Launch Contacts App Intent Received](trigger_launch_contacts_app_intent_received.md) | The trigger Launch Contacts App Intent Received is executed when an app or the system wants to launch a contacts/address book app. |
| 58 | [Launch Mail App Intent Received](trigger_launch_mail_app_intent_received.md) | The trigger Launch Mail App Intent Received is executed when an app or the system wants to launch a browser app. |
| 59 | [Launch Music App Intent Received](trigger_launch_music_app_intent_received.md) | The trigger Launch Music App Intent Received is executed when an app or the system wants to launch a music app. |
| 60 | [Launcher Trigger](trigger_launcher_trigger.md) | The trigger Launcher Trigger is executed when the launcher entry with the name Launcher Trigger is manually started or when another app launches the entry. |
| 61 | [Light Sensor](trigger_light_sensor.md) | The trigger Light Sensor is executed when the measured surrounding light intensity passes the defined value. |
| 62 | [Locale Adjusted](trigger_locale_adjusted.md) | The trigger Locale Adjusted is executed when the locale has been changed in the system. |
| 63 | [Location](trigger_location.md) | The trigger Location is executed when the location is entering the defined region or exiting the defined region. |
| 64 | [Location Provider State](trigger_location_provider_state.md) | The trigger Location Provider State is executed when a location provider (GPS or Network) is enabled or disabled. |
| 65 | [Login Attempt](trigger_login_attempt.md) | The trigger Login Attempt is executed, whenever someone unsuccessfully tries to login to the device respectively tries to unlock the device. |
| 66 | [Magnetic Field Sensor](trigger_magnetic_field_sensor.md) | The trigger Magnetic Field Sensor is executed when the measured magnetic field strength passes the defined value. |
| 67 | [Media Button Event (Experimental)](trigger_media_button_event.md) | The trigger Media Button Event (Experimental) executes a flow when the system detects a media button event, for example when the play-button is pressed on a headset. |
| 68 | [Media Session Changed (Experimental)](trigger_media_session_changed.md) | The trigger Media Session Changed (Experimental) is executed when the media session of the specified player changes (new track is played, media image is loaded etc.). |
| 69 | [Mobile Datanetwork Type](trigger_mobile_datanetwork_type.md) | The trigger Mobile Datanetwork Type is executed when the network type switches to one selected in the list. |
| 70 | [Next Alarm](trigger_next_alarm.md) | The trigger Next Alarm is executed when the next alarm set in the Android alarm app is reached. |
| 71 | [NFC State](trigger_nfc_state.md) | The trigger NFC State is executed when the NFC adapter of the device is turned on or off depending on the settings used. |
| 72 | [NFC Tag](trigger_nfc_tag.md) | The trigger NFC Tag executes the flow when an NFC tag is detected. You can either write a special ID to the NFC tag that will be used to identify the tag and execute the flow… |
| 73 | [Notification on Screen Displayed](trigger_notification_screen_displayed.md) | The trigger Notification on Screen Displayed is executed when a notification is displayed on the screen. |
| 74 | [Notification on Statusbar Displayed](trigger_notification_status_bar_displayed.md) | The trigger Notification on Statusbar Displayed is executed when a notification is displayed in the statusbar. |
| 75 | [Notification on Statusbar Removed](trigger_notification_status_bar_removed.md) | The trigger Notification on Statusbar Removed is executed when a notification is removed from the statusbar. |
| 76 | [Notification on Statusbar Selected](trigger_notification_status_bar_selected.md) | The trigger Notification on Statusbar Selected executes the flow when a notification is selected that was previously shown using action Notification on Statusbar. |
| 77 | [Outgoing Call](trigger_outgoing_call.md) | The trigger Outgoing Call is executed when an outgoing call is made and the criteria defined in the options match. |
| 78 | [Periodic Location Update](trigger_periodic_location_update.md) | The trigger Periodic Location Update is executed in periodic intervals and delivers a location to the executed flow. |
| 79 | [Periodic Timer](trigger_periodic_timer.md) | The trigger Periodic Timer is executed in the specified interval. |
| 80 | [Periodic Timer Inexact](trigger_periodic_timer_inexact.md) | The trigger Periodic Timer Inexact is executed approximately in the specified interval. |
| 81 | [Phone Cell CDMA](trigger_phone_cell_cdma.md) | The trigger Phone Cell CDMA is executed when the device connects or disconnects from the defined cells. Changes within the defined list of cells don't invoke the trigger. |
| 82 | [Phone Cell GSM](trigger_phone_cell_gsm.md) | The trigger Phone Cell GSM is executed when the device connects or disconnects from the defined cells. Changes within the defined list of cells don't invoke the trigger. |
| 83 | [Phone Service State](trigger_phone_service_state.md) | The trigger Phone Service State is executed when the device detects the specified state. |
| 84 | [Phone Signal Strength](trigger_phone_signal_strength.md) | The trigger Phone Signal Strength is executed when the signal strength falls under or raises over the specified value. |
| 85 | [Plugin (Experimental)](trigger_plugin.md) | The trigger Plugin (Experimental) executes a flow when the condition of a plugin changes to true and/or false. |
| 86 | [Plugin Event (Experimental)](trigger_plugin_event.md) | The trigger Plugin Event (Experimental) executes a flow when an event-plugin indicates an event. |
| 87 | [Power Source](trigger_power_connected.md) | The trigger Power Source is executed when a power source is connected to the device (charger or USB cable). |
| 88 | [Power Source (Android Wear)](trigger_power_connected_wear.md) | The trigger Power Source (Android Wear) is executed when a power source is connected to the device (charger or USB cable). |
| 89 | [Pressure Sensor](trigger_pressure_sensor.md) | The trigger Pressure Sensor is executed when the measured pressure of the pressure sensor rises above or declines below a certain level or when the pressure changes at least… |
| 90 | [Proximity Sensor](trigger_proximity_sensor.md) | The trigger Proximity Sensor is executed when the measured distance of the proximity sensor passes the defined distance. |
| 91 | [Quick Settings Tile Selected](trigger_quick_settings_tile_selected.md) | The trigger Quick Settings Tile Selected configures the selected quick settings tile and is executed when the tile is selected/clicked. |
| 92 | [Ringer Mode](trigger_ringer_mode.md) | The trigger Ringer Mode is executed when the device switches to the specified ringer mode. |
| 93 | [Screen Orientation](trigger_screen_orientation.md) | The trigger Screen Orientation is executed when the orientation of the device changes to portrait or landscape. |
| 94 | [Send/Share Intent Received](trigger_send_intent_received.md) | The trigger Send/Share Intent Received is executed when the send/share menu is used in an app and the data is shared with Automagic. |
| 95 | [Send/Share Multiple Intent Received](trigger_send_multiple_intent_received.md) | The trigger Send/Share Multiple Intent Received is executed when the send/share menu is used in an app and multiple items are shared with Automagic. |
| 96 | [Shake](trigger_shake.md) | The trigger Shake is executed when the device is shaken. |
| 97 | [Shortcut](trigger_shortcut.md) | The trigger Shortcut is executed when a shortcut on the launcher is pressed. You can create the shortcut and select an icon by pressing the Install Shortcut button. |
| 98 | [Shortcut (Android Wear)](trigger_shortcut_wear.md) | The trigger Shortcut (Android Wear) is executed when a shortcut in the list of Shortcut is selected (see Start -> Shortcut). |
| 99 | [Shutdown](trigger_shutdown.md) | The trigger Shutdown is executed before the device shutdown. A flow is executed on a best effort basis, Automagic might not have enough time to execute the flow completely or… |
| 100 | [Significant Motion Detected](trigger_significant_motion_sensor.md) | The trigger Significant Motion Detected is executed when the special hardware sensor of the device detects a significant motion. |
| 101 | [SIM State](trigger_sim_state.md) | The trigger SIM State is executed when the SIM state changes to one of the selected states. |
| 102 | [SMS Received](trigger_sms_receive.md) | The trigger SMS Received is executed when an SMS is received depending on the criteria defined in the options. |
| 103 | [SMS Sent](trigger_sms_sent.md) | The trigger SMS Sent is executed when an SMS is sent and stored as a sent SMS in the default SMS outbox of the standard Android SMS database. |
| 104 | [Sound Level (Experimental)](trigger_sound_level.md) | The trigger Sound Level (Experimental) is executed when the recorded sound level in the environment exceed a certain level. |
| 105 | [Speech Web Search Requested](trigger_speech_web_search_requested.md) | The trigger Speech Web Search Requested is executed when the speech recognition based search is initiated, for example by long-pressing the headset hook button. |
| 106 | [Speed](trigger_speed.md) | The trigger Speed is executed when the measured speed of the GPS receiver rises above or declines below a certain level. |
| 107 | [Step counter](trigger_step_counter_sensor.md) | The trigger Step counter uses the Step counter/Pedometer of the device and executes a flow when the specified number of steps have been counted. |
| 108 | [Storage Media Event](trigger_storage_media_event.md) | The trigger Storage Media Event is executed when the system mounts or unmounts the SD card or makes other changes involving the storage media. |
| 109 | [System Setting Changed](trigger_system_setting_changed.md) | The trigger System Setting Changed is executed whenever a setting in the systems setting database was changed. |
| 110 | [System Setting Changed (Android Wear)](trigger_system_setting_changed_wear.md) | The trigger System Setting Changed (Android Wear) is executed whenever a setting in the systems setting database was changed. |
| 111 | [Take Note (Android Wear)](trigger_take_note_wear.md) | The trigger Take Note (Android Wear) is executed when a note is taken from the Wear device. |
| 112 | [Theater Mode (Android Wear)](trigger_theater_mode_wear.md) | The trigger Theater Mode (Android Wear) is executed when the theater mode is turned on or off. |
| 113 | [Time](trigger_time.md) | The trigger Time executes the flow regularly on the specified weekday and time. |
| 114 | [Time Adjusted](trigger_time_adjusted.md) | The trigger Time Adjusted is executed when the time of the system is changed. |
| 115 | [Timezone Adjusted](trigger_timezone_adjusted.md) | The trigger Timezone Adjusted is executed when the timezone of the system has been changed. |
| 116 | [UI Event](trigger_user_interface_event.md) | The trigger UI Event executes a flow when the system detects a change in the user interface, for example when a window is opened, a button is pressed, a list is scrolled… |
| 117 | [User Activity (Experimental)](trigger_periodic_user_activity_update.md) | The trigger User Activity (Experimental) asks the device to periodically check most probably physical activity of the user like driving a car, riding a bike or walking. |
| 118 | [User Present](trigger_user_present.md) | The trigger User Present executes the flow when the user activates the device and passed the unlock screen. |
| 119 | [View Web URL Intent Received](trigger_view_web_url_intent_received.md) | The trigger View Web URL Intent Received is executed when an app wants to show a URL in a browser. |
| 120 | [Voice Command Requested](trigger_voice_command_requested.md) | The trigger Voice Command Requested is executed when the voice recognition by a bluetooth headset (or some other means) is requested. |
| 121 | [Volume Long Press Event](trigger_volume_long_press_event.md) | The trigger Volume Long Press Event is executed when one of the volume keys is pressed down for a longer duration or hold and then released. |
| 122 | [WiFi Connected](trigger_wifi_connected.md) | The trigger WiFi Connected is executed when a connection with the defined network has been established. |
| 123 | [WiFi Disconnected](trigger_wifi_disconnected.md) | The trigger WiFi Disconnected is executed when a connection with the defined network has been separated. |
| 124 | [WiFi Scan Results Available](trigger_wifi_scan_results_available.md) | The trigger WiFi Scan Results Available is executed when the results of a WiFi access point scan are available. |
| 125 | [WiFi State](trigger_wifi_state.md) | The trigger WiFi State is executed when the devices wireless network adapter changes to one of the defined states. |
| 126 | [WiFi Tethering State](trigger_wifi_tethering_state.md) | The trigger WiFi Tethering State is executed when the devices wireless network tethering setting changes to one of the defined states. |
| 127 | [Wired Headset Plugged](trigger_wired_headset_plugged.md) | The trigger Wired Headset Plugged is executed when a wired headset or earphones have been connected or disconnected. |

---

[← Katalog komponen](../README.md) · [Semua trigger dalam satu berkas](../all-components.md) · [Peta dokumentasi](../../README.md)
