# Indeks Condition (88)

Condition memeriksa suatu keadaan dan meneruskan flow ke cabang **true** atau **false**. Gunakan condition untuk membuat flow bereaksi berbeda tergantung situasi.

Daftar berikut diurutkan alfabetis. Ringkasan diambil dari paragraf pembuka dokumentasi asli (bahasa Inggris) agar tetap akurat.

| No. | Nama | Ringkasan |
| ---: | --- | --- |
| 1 | [Action Sound Playing](condition_action_sound_playing.md) | The condition Action Sound Playing checks if an action Sound is currently playing a sound. |
| 2 | [Active Cyanogen/LineageOS Profile](condition_active_cyanogen_mod_profile.md) | The condition Active Cyanogen/LineageOS Profile checks whether one of the listed profiles is active. |
| 3 | [Active Network Type](condition_active_network_type.md) | The condition Active Network Type checks if a network (usually WiFi or Mobile) is active and usable for data traffic. |
| 4 | [Airplane Mode On](condition_airplane_mode_on.md) | The condition Airplane Mode On checks whether the airplane mode is on or not. |
| 5 | [Android Wear Device Connected](condition_android_wear_device_connected.md) | The condition Android Wear Device Connected checks whether a particular Android Wear device is currently connected to the main device. |
| 6 | [App Process Running](condition_app_process_running.md) | The condition App Process Running checks whether the process hosting an app is currently running. |
| 7 | [App Task Running](condition_app_task_running.md) | The condition App Task Running checks whether a task for one of the specified packages is currently running. |
| 8 | [Audio Manager Mode](condition_audio_manager_mode.md) | The condition Audio Manager Mode checks whether the device is currently configured to use the desired audio manager mode. |
| 9 | [Audio Stream Active](condition_audio_stream_active.md) | The condition Audio Stream Active checks if the defined audio stream is currently in active use. |
| 10 | [Audio Volume](condition_audio_volume.md) | The condition Audio Volume checks whether the volume of the selected stream type is above or below a certain level. |
| 11 | [Auto Sync Enabled](condition_auto_sync_enabled.md) | The condition Auto Sync Enabled checks whether the automatic synchronisation is turned on or off either globally (the master switch) or for a specific account/authority. |
| 12 | [Auto-rotate Screen Enabled](condition_auto_rotate_screen_enabled.md) | The condition Auto-rotate Screen Enabled checks whether the system setting to automatically rotate the screen is enabled or not. |
| 13 | [Battery Level](condition_battery_level.md) | The condition Battery Level checks whether the battery level is above or below a certain level. |
| 14 | [Battery Level (Android Wear)](condition_battery_level_wear.md) | The condition Battery Level (Android Wear) checks whether the battery level is above or below a certain level. |
| 15 | [Battery Level BLE (Experimental)](condition_battery_level_ble.md) | The condition Battery Level BLE (Experimental) checks the battery level of a Bluetooth LE device that supports the standardized Battery service. |
| 16 | [Battery Saver Mode Enabled](condition_power_save_mode_enabled.md) | The condition Battery Saver Mode Enabled checks whether the battery saver mode is active or not (Android 5+). |
| 17 | [Biometric Authentication Dialog](condition_biometric_authentication_dialog.md) | The condition Biometric Authentication Dialog shows the authentication dialog of the system and validates a biometric attribute like a fingerprint. |
| 18 | [Bluetooth Device Connected](condition_bluetooth_device_connected.md) | The condition Bluetooth Device Connected checks whether a connection to a Bluetooth device exists. |
| 19 | [Bluetooth Enabled](condition_bluetooth_enabled.md) | The condition Bluetooth Enabled checks whether bluetooth is turned on or off. |
| 20 | [Bluetooth LE Device Available](condition_bluetooth_le_device_available.md) | The condition Bluetooth LE Device Available executes a BT LE scan to test if a device is currently available. |
| 21 | [Bluetooth SCO On](condition_bluetooth_sco_on.md) | The condition Bluetooth SCO On checks whether communications use Bluetooth SCO or not. |
| 22 | [Calendar Event](condition_calendar_event.md) | The condition Calendar Event checks, whether an event on the calendar is currently active. |
| 23 | [Call State](condition_call_state.md) | The condition Call State checks whether a call is currently active or not. |
| 24 | [Confirmation Dialog](condition_confirmation_dialog.md) | The condition Confirmation Dialog shows a dialog with a question and continues flow execution depending on the button pressed. |
| 25 | [Custom Widget Overlay Showing](condition_custom_widget_overlay_showing.md) | The condition Custom Widget Overlay Showing checks if a particular custom widget is currently showing as an overlay. |
| 26 | [Debug Dialog](condition_debug_dialog.md) | The condition Debug Dialog shows a dialog containing all variables and the corresponding values in a dialog. |
| 27 | [Device Idle/Doze Mode Active](condition_device_idle_mode_active.md) | The condition Device Idle/Doze Mode Active checks if the device is currently in idle/doze mode. |
| 28 | [Device Orientation](condition_device_orientation.md) | The condition Device Orientation checks whether the device is in one of the specified orientation. |
| 29 | [Device Storage Space](condition_device_storage_space.md) | The condition Device Storage Space checks the storage space on the filesystem containing the specified path. |
| 30 | [Device Storage Space Low](condition_device_storage_space_low.md) | The condition Device Storage Space Low checks whether the free space of the internal memory of the device is low. |
| 31 | [Dock State](condition_dock_state.md) | The condition Dock State checks whether the device is in one of the docking states or not. |
| 32 | [Execution Count](condition_execution_count.md) | The condition Execution Count checks whether the condition has been executed a certain amount of times. An internal counter is incremented whenever the condition is executed. |
| 33 | [Expression](condition_expression.md) | The condition Expression checks whether the expression is true or not. |
| 34 | [Flashlight On](condition_flashlight_on.md) | The condition Flashlight On checks if the flashlight has been turned on by Automagic. |
| 35 | [Flow Enabled](condition_flow_enabled.md) | The condition Flow Enabled checks whether a flow is enabled or disabled. |
| 36 | [Flow Executing](condition_flow_executing.md) | The condition Flow Executing checks if a particular flow is currently executing. |
| 37 | [Gleeo is Recording](condition_gleeo_recording.md) | The condition Gleeo is Recording checks whether Gleeo Time Tracker is currently recording a specific project or task. |
| 38 | [Gmail Unread Conversation Count](condition_gmail_unread_conversation_count.md) | The condition Gmail Unread Conversation Count checks the number of unread conversations available in the Gmail app on the device. |
| 39 | [Hardware Keyboard State](condition_hardware_keyboard_state.md) | The condition Hardware Keyboard State checks whether the hardware keyboard of the device is currently open or closed. |
| 40 | [Hardware Keyboard Type](condition_hardware_keyboard_type.md) | The condition Hardware Keyboard Type checks if the currently connected hardware keyboard type matches one of the selected types. |
| 41 | [Host Reachable](condition_host_reachable.md) | The condition Host Reachable tests whether a host can be reached by either opening a TCP-connection using a socket or by executing a ping command. |
| 42 | [Interruptions Mode](condition_interruptions_mode.md) | The condition Interruptions Mode checks if the device is in the specified interruption mode. |
| 43 | [Keyguard Locked](condition_keyguard_locked.md) | The condition Keyguard Locked checks whether or not the keyguard is currently active/showing. |
| 44 | [Keyguard with Security](condition_keyguard_secure.md) | The condition Keyguard with Security checks whether a keyguard/lockscreen with a security element (PIN, password, ...) or not (None, Swipe) is set. |
| 45 | [Light Sensor](condition_light_sensor.md) | The condition Light Sensor checks whether the measured value of the light sensor is below or above the defined level. |
| 46 | [Location](condition_location.md) | The condition Location checks whether a location is inside a specific area or not. |
| 47 | [Location Entering](condition_location_entering.md) | The condition Location Entering checks whether an area has been entered or exited. This condition should only be used in conjunction with a Location trigger. |
| 48 | [Location Provider Enabled](condition_location_provider_enabled.md) | The condition Location Provider Enabled checks whether a particular location provider like GPS is enabled or not. |
| 49 | [Magnetic Field Sensor](condition_magnetic_field_sensor.md) | The condition Magnetic Field Sensor checks whether the measured value of the magnetic field sensor is below or above the defined level. |
| 50 | [Microphone Mute](condition_microphone_mute.md) | The condition Microphone Mute checks whether the microphone is currently muted. |
| 51 | [Mobile Datanetwork Enabled](condition_mobile_datanetwork_enabled.md) | The condition Mobile Datanetwork Enabled checks whether the mobile datanetwork is turned on or off. |
| 52 | [Mobile Datanetwork Type](condition_mobile_datanetwork_type.md) | The condition Mobile Datanetwork Type checks if the current datanetwork type matches one selected in the list. |
| 53 | [Music Active](condition_music_active.md) | The condition Music Active checks whether the music audio stream is currently in use. |
| 54 | [Network Connected](condition_network_connected.md) | The condition Network Connected checks if a network connection is currently available. |
| 55 | [NFC Enabled](condition_nfc_enabled.md) | The condition NFC Enabled checks whether NFC is turned on or off. |
| 56 | [Night Mode](condition_night_mode.md) | The condition Night Mode checks whether the device is currently configured to use the desired night mode. |
| 57 | [Notification on Statusbar Displayed](condition_notification_status_bar_displayed.md) | The condition Notification on Statusbar Displayed checks whether a notification of an app is displayed in the statusbar and supplies the information of the first matching… |
| 58 | [Phone Cell CDMA](condition_phone_cell_cdma.md) | The condition Phone Cell CDMA checks whether the phone is connected to one of the specified cells of interest. |
| 59 | [Phone Cell GSM](condition_phone_cell_gsm.md) | The condition Phone Cell GSM checks whether the phone is connected to one of the specified cells of interest. |
| 60 | [Phone Service State](condition_phone_service_state.md) | The condition Phone Service State checks whether the phone service is currently available, unavailable or only emergency calls can be placed. |
| 61 | [Phone Signal Strength](condition_phone_signal_strength.md) | The condition Phone Signal Strength checks whether the signal strength of the mobile network is above or below a certain level. |
| 62 | [Plugin (Experimental)](condition_plugin.md) | The condition Plugin (Experimental) checks the condition of a plugin. |
| 63 | [Power Source Connected](condition_power_connected.md) | The condition Power Source Connected checks whether the device is currently connected to a power source. |
| 64 | [Power Source Connected (Android Wear)](condition_power_connected_wear.md) | The condition Power Source Connected (Android Wear) checks whether the device is currently connected to a power source. |
| 65 | [Pressure Sensor](condition_pressure_sensor.md) | The condition Pressure Sensor checks whether the measured pressure is below or above the defined value. |
| 66 | [Proximity Sensor](condition_proximity_sensor.md) | The condition Proximity Sensor checks whether the measured distance of the proximity sensor is below or above the defined distance. |
| 67 | [Ringer Mode](condition_ringer_mode.md) | The condition Ringer Mode checks whether the device is currently configured to use the desired ringer mode. |
| 68 | [Roaming](condition_roaming.md) | The condition Roaming checks whether you are currently in a roaming location. |
| 69 | [Root Setting Enabled](condition_root_setting_enabled.md) | The condition Root Setting Enabled checks whether the Root setting in Automagic is enabled or not. |
| 70 | [Screen Automatic Brightness Enabled](condition_screen_auto_brightness_enabled.md) | The condition Screen Automatic Brightness Enabled checks whether the setting to change the display brightness automatically depending on the environment is turned on or not. |
| 71 | [Screen On](condition_screen_on.md) | The condition Screen On checks whether the screen is currently turned on. |
| 72 | [Screen Orientation](condition_screen_orientation.md) | The condition Screen Orientation tests whether the device is currently in portrait or landscape mode. |
| 73 | [Service Running](condition_service_running.md) | The condition Service Running checks whether the specified service is currently running. |
| 74 | [Sound Level (Experimental)](condition_sound_level.md) | The condition Sound Level (Experimental) checks whether or not the environment sound exceed a certain level. |
| 75 | [Speakerphone On](condition_speakerphone_on.md) | The condition Speakerphone On checks whether speakerphone is turned on or off. |
| 76 | [Telephony Radio Enabled](condition_telephony_radio_enabled.md) | The condition Telephony Radio Enabled checks if the radio of the phone is enabled or not. |
| 77 | [Theater Mode On (Android Wear)](condition_theater_mode_on_wear.md) | The condition Theater Mode On (Android Wear) checks whether the theater mode is turned on or not. |
| 78 | [Time Range](condition_time_range.md) | The condition Time Range is true when the current time is in the defined time range. |
| 79 | [UI Mode](condition_ui_mode.md) | The condition UI Mode checks whether the device is currently in car, desk, TV or normal UI mode. |
| 80 | [USB Tethering Enabled](condition_usb_tethering_enabled.md) | The condition USB Tethering Enabled checks whether USB tethering is enabled or not. |
| 81 | [Vibrate on Ring Enabled](condition_vibrate_on_ring_enabled.md) | The condition Vibrate on Ring Enabled checks whether the setting to vibrate on ring is enabled or not. |
| 82 | [WiFi Access Point Enabled](condition_wifi_access_point_enabled.md) | The condition WiFi Access Point Enabled checks whether a WiFi configuration is enabled and the system is allowed to connect to this access point. |
| 83 | [WiFi Available](condition_wifi_available.md) | The condition WiFi Available checks whether one specific WiFi access point is currently available. |
| 84 | [WiFi Connected](condition_wifi_connected.md) | The condition WiFi Connected checks whether the device is currently connected to one of the specified WiFi networks. |
| 85 | [WiFi Signal Level](condition_wifi_signal_level.md) | The condition WiFi Signal Level checks the signal level of the connected wifi network. |
| 86 | [WiFi State](condition_wifi_state.md) | The condition WiFi State checks whether the device wireless network adapter is in the specified state. |
| 87 | [WiFi Tethering State](condition_wifi_tethering_state.md) | The condition WiFi Tethering State checks whether the device wireless network adapter is in the specified state. |
| 88 | [Wired Headset Plugged](condition_wired_headset_plugged.md) | The condition Wired Headset Plugged checks whether a wired headset is currently plugged in or not. |

---

[← Katalog komponen](../README.md) · [Semua condition dalam satu berkas](../all-components.md) · [Peta dokumentasi](../../README.md)
